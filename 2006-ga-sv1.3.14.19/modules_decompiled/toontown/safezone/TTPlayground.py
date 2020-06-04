# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase import ToontownGlobals
import Playground
import whrandom
from toontown.launcher import DownloadForceAcknowledge

class TTPlayground(Playground.Playground):
    
    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)

    
    def load(self):
        Playground.Playground.load(self)

    
    def unload(self):
        Playground.Playground.unload(self)

    
    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        taskMgr.doMethodLater(1, self._TTPlayground__birds, 'TT-birds')

    
    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.remove('TT-birds')

    
    def _TTPlayground__birds(self, task):
        base.playSfx(whrandom.choice(self.loader.birdSound))
        t = whrandom.random() * 20.0 + 1
        taskMgr.doMethodLater(t, self._TTPlayground__birds, 'TT-birds')
        return Task.done

    
    def doRequestLeave(self, requestStatus):
        self.fsm.request('trialerFA', [
            requestStatus])

    
    def enterDFA(self, requestStatus):
        doneEvent = 'dfaDoneEvent'
        self.accept(doneEvent, self.enterDFACallback, [
            requestStatus])
        self.dfa = DownloadForceAcknowledge.DownloadForceAcknowledge(doneEvent)
        if requestStatus['hoodId'] == ToontownGlobals.MyEstate:
            self.dfa.enter(base.cr.hoodMgr.getPhaseFromHood(ToontownGlobals.MyEstate))
        else:
            self.dfa.enter(5)

    
    def showPaths(self):
        CCharPaths = CCharPaths
        import toontown.classicchars
        TTLocalizer = TTLocalizer
        import toontown.toonbase
        self.showPathPoints(CCharPaths.getPaths(TTLocalizer.Mickey))


