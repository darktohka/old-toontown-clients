# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\hood\HydrantTwoAnimatedProp.py
from toontown.hood import ZeroAnimatedProp
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal

class HydrantTwoAnimatedProp(ZeroAnimatedProp.ZeroAnimatedProp):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('HydrantTwoAnimatedProp')
    PauseTimeMult = base.config.GetFloat('zero-pause-mult', 1.0)
    PhaseInfo = {0: ('tt_a_ara_ttc_hydrant_firstMoveArmUp1', 40 * PauseTimeMult), 1: ('tt_a_ara_ttc_hydrant_firstMoveStruggle', 20 * PauseTimeMult), 2: ('tt_a_ara_ttc_hydrant_firstMoveArmUp2', 10 * PauseTimeMult), 3: ('tt_a_ara_ttc_hydrant_firstMoveJump', 8 * PauseTimeMult), 4: ('tt_a_ara_ttc_hydrant_firstMoveJumpBalance', 6 * PauseTimeMult), 5: ('tt_a_ara_ttc_hydrant_firstMoveArmUp3', 4 * PauseTimeMult), 6: ('tt_a_ara_ttc_hydrant_firstMoveJumpSpin', 2 * PauseTimeMult)}
    PhaseWeStartAnimating = 5

    def __init__(self, node):
        ZeroAnimatedProp.ZeroAnimatedProp.__init__(self, node, 'hydrant', self.PhaseInfo, ToontownGlobals.HYDRANT_ZERO_HOLIDAY)

    def startIfNeeded(self):
        try:
            self.curPhase = self.getPhaseToRun()
            if self.curPhase >= self.PhaseWeStartAnimating:
                self.request('DoAnim')
        except:
            pass

    def handleNewPhase(self, newPhase):
        if newPhase < self.PhaseWeStartAnimating:
            self.request('Off')
        else:
            self.startIfNeeded()