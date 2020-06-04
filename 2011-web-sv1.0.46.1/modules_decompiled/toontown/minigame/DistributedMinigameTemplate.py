# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\DistributedMinigameTemplate.py
from pandac.PandaModules import *
from toontown.toonbase.ToonBaseGlobal import *
from DistributedMinigame import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from toontown.toonbase import TTLocalizer

class DistributedMinigameTemplate(DistributedMinigame):
    __module__ = __name__

    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)
        self.gameFSM = ClassicFSM.ClassicFSM('DistributedMinigameTemplate', [
         State.State('off', self.enterOff, self.exitOff, [
          'play']),
         State.State('play', self.enterPlay, self.exitPlay, [
          'cleanup']),
         State.State('cleanup', self.enterCleanup, self.exitCleanup, [])], 'off', 'cleanup')
        self.addChildGameFSM(self.gameFSM)

    def getTitle(self):
        return TTLocalizer.MinigameTemplateTitle

    def getInstructions(self):
        return TTLocalizer.MinigameTemplateInstructions

    def getMaxDuration(self):
        return 0

    def load(self):
        self.notify.debug('load')
        DistributedMinigame.load(self)

    def unload(self):
        self.notify.debug('unload')
        DistributedMinigame.unload(self)
        self.removeChildGameFSM(self.gameFSM)
        del self.gameFSM

    def onstage(self):
        self.notify.debug('onstage')
        DistributedMinigame.onstage(self)

    def offstage(self):
        self.notify.debug('offstage')
        DistributedMinigame.offstage(self)

    def handleDisabledAvatar(self, avId):
        self.notify.debug('handleDisabledAvatar')
        self.notify.debug('avatar ' + str(avId) + ' disabled')
        DistributedMinigame.handleDisabledAvatar(self, avId)

    def setGameReady(self):
        if not self.hasLocalToon:
            return
        self.notify.debug('setGameReady')
        if DistributedMinigame.setGameReady(self):
            return

    def setGameStart(self, timestamp):
        if not self.hasLocalToon:
            return
        self.notify.debug('setGameStart')
        DistributedMinigame.setGameStart(self, timestamp)
        self.gameFSM.request('play')

    def enterOff(self):
        self.notify.debug('enterOff')

    def exitOff(self):
        pass

    def enterPlay(self):
        self.notify.debug('enterPlay')
        self.gameOver()

    def exitPlay(self):
        pass

    def enterCleanup(self):
        self.notify.debug('enterCleanup')

    def exitCleanup(self):
        pass