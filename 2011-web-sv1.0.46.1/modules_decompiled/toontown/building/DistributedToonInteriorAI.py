# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedToonInteriorAI.py
from toontown.toonbase.ToontownGlobals import *
from otp.ai.AIBaseGlobal import *
from direct.distributed.ClockDelta import *
import cPickle
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.distributed import DistributedObjectAI
from direct.fsm import State
from toontown.toon import NPCToons

class DistributedToonInteriorAI(DistributedObjectAI.DistributedObjectAI):
    __module__ = __name__

    def __init__(self, block, air, zoneId, building):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.block = block
        self.zoneId = zoneId
        self.building = building
        self.npcs = NPCToons.createNpcsInZone(air, zoneId)
        self.fsm = ClassicFSM.ClassicFSM('DistributedToonInteriorAI', [
         State.State('toon', self.enterToon, self.exitToon, [
          'beingTakenOver']),
         State.State('beingTakenOver', self.enterBeingTakenOver, self.exitBeingTakenOver, []),
         State.State('off', self.enterOff, self.exitOff, [])], 'toon', 'off')
        self.fsm.enterInitialState()

    def delete(self):
        self.ignoreAll()
        for npc in self.npcs:
            npc.requestDelete()

        del self.npcs
        del self.fsm
        del self.building
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def getZoneIdAndBlock(self):
        r = [
         self.zoneId, self.block]
        return r

    def getToonData(self):
        return cPickle.dumps(self.building.savedBy, 1)

    def getState(self):
        r = [
         self.fsm.getCurrentState().getName(), globalClockDelta.getRealNetworkTime()]
        return r

    def setState(self, state):
        self.sendUpdate('setState', [state, globalClockDelta.getRealNetworkTime()])
        self.fsm.request(state)

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterToon(self):
        pass

    def exitToon(self):
        pass

    def enterBeingTakenOver(self):
        pass

    def exitBeingTakenOver(self):
        pass