# File: C (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from toontown.hood import Place

class CogHQBasement(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogHQBasement')
    
    def __init__(self, hood, parentFSM, doneEvent):
        Place.Place.__init__(self, hood, doneEvent)
        self.parentFSM = parentFSM


