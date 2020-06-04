# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\hood\MailboxOneAnimatedProp.py
from toontown.hood import ZeroAnimatedProp
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal

class MailboxOneAnimatedProp(ZeroAnimatedProp.ZeroAnimatedProp):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('MailboxOneAnimatedProp')
    PauseTimeMult = base.config.GetFloat('zero-pause-mult', 1.0)
    PhaseInfo = {0: ('tt_a_ara_dod_mailbox_firstMoveFlagSpin1', 40 * PauseTimeMult), 1: (('tt_a_ara_dod_mailbox_firstMoveStruggle', 'tt_a_ara_dod_mailbox_firstMoveJump'), 20 * PauseTimeMult), 2: ('tt_a_ara_dod_mailbox_firstMoveFlagSpin2', 10 * PauseTimeMult), 3: ('tt_a_ara_dod_mailbox_firstMoveFlagSpin3', 8 * PauseTimeMult), 4: ('tt_a_ara_dod_mailbox_firstMoveJumpSummersault', 6 * PauseTimeMult), 5: ('tt_a_ara_dod_mailbox_firstMoveJumpFall', 4 * PauseTimeMult), 6: ('tt_a_ara_dod_mailbox_firstMoveJump3Summersaults', 2 * PauseTimeMult)}
    PhaseWeStartAnimating = 3

    def __init__(self, node):
        ZeroAnimatedProp.ZeroAnimatedProp.__init__(self, node, 'mailbox', self.PhaseInfo, ToontownGlobals.MAILBOX_ZERO_HOLIDAY)

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