# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\DistCogdoBoardroomGame.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from toontown.cogdominium.DistCogdoLevelGame import DistCogdoLevelGame
from toontown.cogdominium.CogdoBoardroomGameBase import CogdoBoardroomGameBase
from toontown.cogdominium import CogdoBoardroomGameConsts as Consts
from toontown.toonbase import ToontownTimer
from toontown.toonbase import TTLocalizer as TTL

class DistCogdoBoardroomGame(CogdoBoardroomGameBase, DistCogdoLevelGame):
    __module__ = __name__
    notify = directNotify.newCategory('DistCogdoBoardroomGame')

    def __init__(self, cr):
        DistCogdoLevelGame.__init__(self, cr)

    def getTitle(self):
        return TTL.BoardroomGameTitle

    def getInstructions(self):
        return TTL.BoardroomGameInstructions

    def announceGenerate(self):
        DistCogdoLevelGame.announceGenerate(self)
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.setScale(Consts.Settings.TimerScale.get())
        self.timer.stash()

    def disable(self):
        self.timer.destroy()
        self.timer = None
        DistCogdoLevelGame.disable(self)
        return

    def enterGame(self):
        DistCogdoLevelGame.enterGame(self)
        timeLeft = Consts.GameDuration.get() - (globalClock.getRealTime() - self.getStartTime())
        self.timer.setTime(timeLeft)
        self.timer.countdown(timeLeft, self.timerExpired)
        self.timer.unstash()

    def enterFinish(self):
        DistCogdoLevelGame.enterFinish(self)
        timeLeft = Consts.FinishDuration.get() - (globalClock.getRealTime() - self.getFinishTime())
        self.timer.setTime(timeLeft)
        self.timer.countdown(timeLeft, self.timerExpired)
        self.timer.unstash()

    def timerExpired(self):
        pass

    if __dev__:

        def _handleTimerScaleChanged(self, timerScale):
            if hasattr(self, 'timer'):
                self.timer.setScale(timerScale)