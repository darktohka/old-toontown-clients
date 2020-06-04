# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\DivingGameToonSD.py
from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.interval.IntervalGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from direct.fsm import ClassicFSM
from direct.fsm import State
import CatchGameGlobals

class DivingGameToonSD(StateData.StateData):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DivingGameToonSD')
    FallBackAnim = 'slip-backward'
    FallFwdAnim = 'slip-forward'
    CatchNeutralAnim = 'catch-neutral'
    CatchRunAnim = 'catch-run'
    EatNeutralAnim = 'catch-eatneutral'
    EatNRunAnim = 'catch-eatnrun'
    status = ''
    animList = [
     FallBackAnim, FallFwdAnim, CatchNeutralAnim, CatchRunAnim, EatNeutralAnim, EatNRunAnim]

    def __init__(self, avId, game):
        self.avId = avId
        self.game = game
        self.isLocal = avId == base.localAvatar.doId
        self.toon = self.game.getAvatar(self.avId)
        self.unexpectedExit = False
        self.fsm = ClassicFSM.ClassicFSM('CatchGameAnimFSM-%s' % self.avId, [
         State.State('init', self.enterInit, self.exitInit, [
          'normal']),
         State.State('normal', self.enterNormal, self.exitNormal, [
          'freeze', 'treasure']),
         State.State('treasure', self.enterTreasure, self.exitTreasure, [
          'freeze', 'normal']),
         State.State('freeze', self.enterFreeze, self.exitFreeze, [
          'normal']),
         State.State('cleanup', self.enterCleanup, self.exitCleanup, [])], 'init', 'cleanup')

    def load(self):
        self.setAnimState('off', 1.0)
        for anim in self.animList:
            self.toon.pose(anim, 0)

    def unload(self):
        del self.fsm
        self.game = None
        return

    def enter(self):
        self.fsm.enterInitialState()

    def exit(self, unexpectedExit=False):
        self.unexpectedExit = unexpectedExit
        if not unexpectedExit:
            self.fsm.requestFinalState()

    def enterInit(self):
        self.notify.debug('enterInit')
        self.status = 'init'

    def exitInit(self):
        pass

    def enterNormal(self):
        self.status = 'normal'
        self.notify.debug('enterNormal')
        self.setAnimState('dive', 1.0)

    def exitNormal(self):
        self.setAnimState('off', 1.0)

    def enterTreasure(self):
        self.status = 'treasure'
        self.notify.debug('enterTreasure')
        self.setAnimState('swimhold', 1.0)

    def exitTreasure(self):
        self.notify.debug('exitTreasure')

    def enterFreeze(self):
        self.status = 'freeze'
        self.notify.debug('enterFreeze')
        self.setAnimState('cringe', 1.0)

    def exitFreeze(self):
        pass

    def enterCleanup(self):
        self.status = 'cleanup'
        self.notify.debug('enterCleanup')
        if self.toon:
            self.toon.resetLOD()

    def exitCleanup(self):
        pass

    def setAnimState(self, newState, playRate):
        if not self.unexpectedExit:
            self.toon.setAnimState(newState, playRate)