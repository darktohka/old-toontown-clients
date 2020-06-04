# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\CogdoBarrelRoomAI.py
import random
from sets import Set
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from direct.showbase import PythonUtil
from direct.task import Timer
from direct.task.Task import Task
from toontown.toonbase import ToontownGlobals
from toontown.cogdominium import CogdoBarrelRoomConsts
from toontown.cogdominium import DistributedCogdoBarrelAI

class CogdoBarrelRoomAI:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCogdoBarrelRoomAI')

    def __init__(self, cogdoInteriorAI):
        self.cogdoInteriorAI = cogdoInteriorAI
        self.allBarrelsCollectedTask = self.cogdoInteriorAI.taskName('allBarrelsCollectedTask')
        self.collectionDoneEvent = self.cogdoInteriorAI.taskName('barrelCollectionDone')
        self.collectTimer = None
        self.results = [[], []]
        for i in range(CogdoBarrelRoomConsts.MaxToons):
            if i < len(self.cogdoInteriorAI.toons):
                self.results[0].append(self.cogdoInteriorAI.toons[i])
            else:
                self.results[0].append(0)
            self.results[1].append(0)

        self.spawnedBarrels = []
        self.__spawnBarrels()
        return

    def destroy(self):
        taskMgr.remove(self.allBarrelsCollectedTask)
        if self.collectTimer:
            self.collectTimer.stop()
            self.collectTimer = None
        for barrel in self.spawnedBarrels:
            barrel.requestDelete()

        self.spawnedBarrels = []
        return

    def __spawnBarrels(self):
        self.spawnedBarrels = []

        def spawnBarrel(index):
            barrel = DistributedCogdoBarrelAI.DistributedCogdoBarrelAI(self.cogdoInteriorAI.air, index, self.barrelCollected)
            barrel.generateWithRequired(self.cogdoInteriorAI.zoneId)
            self.spawnedBarrels.append(barrel)

        for i in range(CogdoBarrelRoomConsts.numBarrels()):
            spawnBarrel(i)

    def reset(self):
        for barrel in self.spawnedBarrels:
            barrel.d_setState(CogdoBarrelRoomConsts.StateHidden)

        for i in range(CogdoBarrelRoomConsts.MaxToons):
            self.results[1][i] = 0

    def activate(self):
        self.collectTimer = Timer.Timer()
        self.collectTimer.startCallback(CogdoBarrelRoomConsts.CollectionTime, self.__endCollectionPhase)
        for barrel in self.spawnedBarrels:
            barrel.interactive = True

        taskMgr.remove(self.allBarrelsCollectedTask)
        taskMgr.doMethodLater(CogdoBarrelRoomConsts.AllBarrelsCollectedTime, self.__checkAllBarrelsCollected, self.allBarrelsCollectedTask)

    def __endCollectionPhase(self):
        messenger.send(self.collectionDoneEvent)

    def deactivate(self):
        if self.collectTimer:
            self.collectTimer.stop()
            self.collectTimer = None
        for barrel in self.spawnedBarrels:
            barrel.interactive = False

        return

    def setScore(self, score):
        numGood = int(score * (CogdoBarrelRoomConsts.numBarrels() + 0.5))
        random.shuffle(self.spawnedBarrels)
        for i in range(len(self.spawnedBarrels)):
            if i < numGood:
                state = CogdoBarrelRoomConsts.StateAvailable
            else:
                state = CogdoBarrelRoomConsts.StateCrushed
            self.spawnedBarrels[i].d_setState(state)

    def barrelCollected(self, barrel, avId):
        try:
            playerIndex = self.results[0].index(avId)
            self.results[1][playerIndex] += barrel.laff
        except ValueError:
            self.notify.warning('barrelCollected: Unrecognized avId %s' % avId)

    def __checkAllBarrelsCollected(self, task):
        if not CogdoBarrelRoomConsts.EndWithAllBarrelsCollected:
            return
        if self.__allBarrelsCollected():
            self.__endCollectionPhase()
        else:
            return Task.again

    def __toonIdNeedsLaff(self, toonId):
        toon = self.cogdoInteriorAI.air.doId2do.get(toonId)
        if toon != None:
            return not toon.isToonedUp()
        return

    def __allBarrelsCollected(self):
        toonsNeedingLaff = Set(filter(lambda toon: self.__toonIdNeedsLaff(toon), self.cogdoInteriorAI.toons))
        for barrel in self.spawnedBarrels:
            if not toonsNeedingLaff.issubset(Set(barrel.grabbedBy)):
                return False

        return True

    def __str__(self):
        return str(self.cogdoInteriorAI) + '.CogdoBarrelRoomAI'