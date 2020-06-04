# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\toon\DistributedNPCBlockerAI.py
from otp.ai.AIBaseGlobal import *
from pandac.PandaModules import *
from DistributedNPCToonBaseAI import *
import NPCToons
from direct.task.Task import Task

class DistributedNPCBlockerAI(DistributedNPCToonBaseAI):
    __module__ = __name__

    def __init__(self, air, npcId):
        DistributedNPCToonBaseAI.__init__(self, air, npcId)
        self.tutorial = 0

    def delete(self):
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.ignoreAll()
        DistributedNPCToonBaseAI.delete(self)

    def setTutorial(self, val):
        self.tutorial = val

    def getTutorial(self):
        return self.tutorial

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        DistributedNPCToonBaseAI.avatarEnter(self)
        av = self.air.doId2do.get(avId)
        if av is None:
            self.notify.warning('toon isnt there! toon: %s' % avId)
            return
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit, extraArgs=[avId])
        self.sendStartMovie(avId)
        return

    def sendStartMovie(self, avId):
        self.busy = avId
        self.sendUpdate('setMovie', [NPCToons.BLOCKER_MOVIE_START, self.npcId, avId, ClockDelta.globalClockDelta.getRealNetworkTime()])
        if not self.tutorial:
            taskMgr.doMethodLater(NPCToons.CLERK_COUNTDOWN_TIME, self.sendTimeoutMovie, self.uniqueName('clearMovie'))

    def sendTimeoutMovie(self, task):
        self.timedOut = 1
        self.sendUpdate('setMovie', [NPCToons.BLOCKER_MOVIE_TIMEOUT, self.npcId, self.busy, ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendClearMovie(None)
        return Task.done

    def sendClearMovie(self, task):
        self.busy = 0
        self.timedOut = 0
        self.sendUpdate('setMovie', [NPCToons.BLOCKER_MOVIE_CLEAR, self.npcId, 0, ClockDelta.globalClockDelta.getRealNetworkTime()])
        return Task.done

    def __handleUnexpectedExit(self, avId):
        self.notify.warning('avatar:' + str(avId) + ' has exited unexpectedly')
        if not self.tutorial:
            self.sendTimeoutMovie(None)
        return