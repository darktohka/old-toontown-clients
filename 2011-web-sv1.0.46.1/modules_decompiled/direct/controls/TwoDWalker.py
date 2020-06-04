# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\controls\TwoDWalker.py
from GravityWalker import *

class TwoDWalker(GravityWalker):
    __module__ = __name__
    notify = directNotify.newCategory('TwoDWalker')
    wantDebugIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    wantFloorSphere = base.config.GetBool('want-floor-sphere', 0)
    earlyEventSphere = base.config.GetBool('early-event-sphere', 0)

    def __init__(self, gravity=-32.174, standableGround=0.707, hardLandingForce=16.0):
        self.notify.debug('Constructing TwoDWalker')
        GravityWalker.__init__(self)

    def handleAvatarControls(self, task):
        jump = inputState.isSet('forward')
        if self.lifter.isOnGround():
            if self.isAirborne:
                self.isAirborne = 0
                impact = self.lifter.getImpactVelocity()
                messenger.send('jumpLand')
            self.priorParent = Vec3.zero()
        else:
            if self.isAirborne == 0:
                pass
            self.isAirborne = 1
        return Task.cont

    def jumpPressed(self):
        if self.lifter.isOnGround():
            if self.isAirborne == 0:
                if self.mayJump:
                    self.lifter.addVelocity(self.avatarControlJumpForce)
                    messenger.send('jumpStart')
                    self.isAirborne = 1