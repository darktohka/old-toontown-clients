# File: D (Python 2.2)

from ShowBaseGlobal import *
import Playground
import whrandom

class DLPlayground(Playground.Playground):
    
    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)

    
    def showPaths(self):
        import CCharPaths
        import Localizer
        self.showPathPoints(CCharPaths.getPaths(Localizer.Donald))


