# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
import Playground
import whrandom

class DLPlayground(Playground.Playground):
    
    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)

    
    def showPaths(self):
        CCharPaths = CCharPaths
        import toontown.classicchars
        TTLocalizer = TTLocalizer
        import toontown.toonbase
        self.showPathPoints(CCharPaths.getPaths(TTLocalizer.Donald))


