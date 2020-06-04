# File: M (Python 2.2)

from direct.showbase.PandaObject import *
from direct.showbase.ShowBaseGlobal import *
import Playground
import whrandom
from direct.fsm import State
from direct.actor import Actor
from toontown.toonbase import ToontownGlobals

class MMPlayground(Playground.Playground):
    
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
        return None

    
    def exitOff(self):
        return None

    
    def enterOnPiano(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPMinniesPiano)

    
    def exitOnPiano(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPRender)

    
    def showPaths(self):
        CCharPaths = CCharPaths
        import toontown.classicchars
        TTLocalizer = TTLocalizer
        import toontown.toonbase
        self.showPathPoints(CCharPaths.getPaths(TTLocalizer.Minnie))


