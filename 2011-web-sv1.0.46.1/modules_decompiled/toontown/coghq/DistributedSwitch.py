# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedSwitch.py
from pandac.PandaModules import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from otp.level import BasicEntities
import DistributedSwitchBase, MovingPlatform
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from otp.level import DistributedEntity

class DistributedSwitch(DistributedSwitchBase.DistributedSwitchBase, BasicEntities.DistributedNodePathEntity):
    __module__ = __name__

    def __init__(self, cr):
        BasicEntities.DistributedNodePathEntity.__init__(self, cr)
        self.fsm = ClassicFSM.ClassicFSM('DistributedSwitch', [
         State.State('off', self.enterOff, self.exitOff, [
          'playing', 'attract']),
         State.State('attract', self.enterAttract, self.exitAttract, [
          'playing']),
         State.State('playing', self.enterPlaying, self.exitPlaying, [
          'attract'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.node = None
        self.triggerName = ''
        return

    def setup(self):
        self.setupSwitch()
        self.setState(self.initialState, self.initialStateTimestamp)
        del self.initialState
        del self.initialStateTimestamp
        self.accept('exit%s' % (self.getName(),), self.exitTrigger)
        self.acceptAvatar()

    def takedown(self):
        pass

    setIsOnEvent = DistributedSwitchBase.stubFunction
    setIsOn = DistributedSwitchBase.stubFunction
    setSecondsOn = DistributedSwitchBase.stubFunction

    def generate(self):
        BasicEntities.DistributedNodePathEntity.generate(self)
        self.track = None
        return

    def announceGenerate(self):
        BasicEntities.DistributedNodePathEntity.announceGenerate(self)
        self.setup()

    def disable(self):
        self.ignoreAll()
        self.fsm.request('off')
        BasicEntities.DistributedNodePathEntity.disable(self)
        self.takedown()

    def delete(self):
        del self.fsm
        BasicEntities.DistributedNodePathEntity.delete(self)

    def acceptAvatar(self):
        self.acceptOnce('enter%s' % (self.getName(),), self.enterTrigger)

    def rejectInteract(self):
        self.acceptAvatar()

    def avatarExit(self, avatarId):
        self.acceptAvatar()

    def getName(self):
        return 'switch-%s' % (self.entId,)

    def setupSwitch(self):
        pass

    def switchOnTrack(self):
        pass

    def switchOffTrack(self):
        pass

    def setAvatarInteract(self, avatarId):
        self.avatarId = avatarId

    def setState(self, state, timestamp):
        if self.isGenerated():
            self.fsm.request(state, [globalClockDelta.localElapsedTime(timestamp)])
        else:
            self.initialState = state
            self.initialStateTimestamp = timestamp

    def enterTrigger(self, args=None):
        self.sendUpdate('requestInteract')

    def exitTrigger(self, args=None):
        self.sendUpdate('requestExit')

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterAttract(self, ts):
        track = self.switchOffTrack()
        if track is not None:
            track.start(ts)
            self.track = track
        return

    def exitAttract(self):
        if self.track:
            self.track.finish()
        self.track = None
        return

    def enterPlaying(self, ts):
        track = self.switchOnTrack()
        if track is not None:
            track.start(ts)
            self.track = track
        return

    def exitPlaying(self):
        if self.track:
            self.track.finish()
        self.track = None
        return

    if __dev__:

        def attribChanged(self, attrib, value):
            self.takedown()
            self.setup()