# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\MMPlayground.py
from pandac.PandaModules import *
import Playground, random
from direct.fsm import ClassicFSM, State
from direct.actor import Actor
from toontown.toonbase import ToontownGlobals

class MMPlayground(Playground.Playground):
    __module__ = __name__

    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.activityFsm = ClassicFSM.ClassicFSM('Activity', [
         State.State('off', self.enterOff, self.exitOff, [
          'OnPiano']),
         State.State('OnPiano', self.enterOnPiano, self.exitOnPiano, [
          'off'])], 'off', 'off')
        self.activityFsm.enterInitialState()

    def load(self):
        Playground.Playground.load(self)

    def unload(self):
        del self.activityFsm
        Playground.Playground.unload(self)

    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)

    def exit(self):
        Playground.Playground.exit(self)

    def handleBookClose(self):
        Playground.Playground.handleBookClose(self)

    def teleportInDone(self):
        Playground.Playground.teleportInDone(self)

    def enterOff(self):
        return

    def exitOff(self):
        return

    def enterOnPiano(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPMinniesPiano)

    def exitOnPiano(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPRender)

    def showPaths(self):
        from toontown.classicchars import CCharPaths
        from toontown.toonbase import TTLocalizer
        self.showPathPoints(CCharPaths.getPaths(TTLocalizer.Minnie))