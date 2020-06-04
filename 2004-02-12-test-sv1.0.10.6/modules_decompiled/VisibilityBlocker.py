# File: V (Python 2.2)

import Entity

class VisibilityBlocker:
    
    def __init__(self):
        self._VisibilityBlocker__nextSetZoneDoneEvent = None

    
    def destroy(self):
        self.cancelUnblockVis()

    
    def requestUnblockVis(self):
        if self._VisibilityBlocker__nextSetZoneDoneEvent is None:
            self._VisibilityBlocker__nextSetZoneDoneEvent = self.level.cr.getNextSetZoneDoneEvent()
            self.acceptOnce(self._VisibilityBlocker__nextSetZoneDoneEvent, self.okToUnblockVis)
            self.level.forceSetZoneThisFrame()
        

    
    def cancelUnblockVis(self):
        if self._VisibilityBlocker__nextSetZoneDoneEvent is not None:
            self.ignore(self._VisibilityBlocker__nextSetZoneDoneEvent)
            self._VisibilityBlocker__nextSetZoneDoneEvent = None
        

    
    def isWaitingForUnblockVis(self):
        return self._VisibilityBlocker__nextSetZoneDoneEvent is not None

    
    def okToUnblockVis(self):
        self.cancelUnblockVis()


