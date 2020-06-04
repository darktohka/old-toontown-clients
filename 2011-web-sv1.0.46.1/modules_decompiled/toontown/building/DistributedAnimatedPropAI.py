# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedAnimatedPropAI.py
from otp.ai.AIBaseGlobal import *
from direct.distributed.ClockDelta import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.distributed import DistributedObjectAI
from direct.fsm import State

class DistributedAnimatedPropAI(DistributedObjectAI.DistributedObjectAI):
    __module__ = __name__

    def __init__(self, air, propId):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.fsm = ClassicFSM.ClassicFSM('DistributedAnimatedPropAI', [
         State.State('off', self.enterOff, self.exitOff, [
          'playing']),
         State.State('attract', self.enterAttract, self.exitAttract, [
          'playing']),
         State.State('playing', self.enterPlaying, self.exitPlaying, [
          'attract'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.propId = propId
        self.avatarId = 0

    def delete(self):
        self.fsm.requestFinalState()
        del self.fsm
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def getPropId(self):
        return self.propId

    def getAvatarInteract(self):
        return self.avatarId

    def getInitialState(self):
        return [
         self.fsm.getCurrentState().getName(), globalClockDelta.getRealNetworkTime()]

    def getOwnerDoId(self):
        return self.ownerDoId

    def requestInteract(self):
        avatarId = self.air.getAvatarIdFromSender()
        stateName = self.fsm.getCurrentState().getName()
        if stateName != 'playing':
            self.sendUpdate('setAvatarInteract', [avatarId])
            self.avatarId = avatarId
            self.fsm.request('playing')
        else:
            self.sendUpdateToAvatarId(avatarId, 'rejectInteract', [])

    def requestExit(self):
        avatarId = self.air.getAvatarIdFromSender()
        if avatarId == self.avatarId:
            stateName = self.fsm.getCurrentState().getName()
            if stateName == 'playing':
                self.sendUpdate('avatarExit', [avatarId])
                self.fsm.request('attract')

    def getState(self):
        return [
         self.fsm.getCurrentState().getName(), globalClockDelta.getRealNetworkTime()]

    def d_setState(self, state):
        self.sendUpdate('setState', [state, globalClockDelta.getRealNetworkTime()])

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterAttract(self):
        self.d_setState('attract')

    def exitAttract(self):
        pass

    def enterPlaying(self):
        self.d_setState('playing')

    def exitPlaying(self):
        pass