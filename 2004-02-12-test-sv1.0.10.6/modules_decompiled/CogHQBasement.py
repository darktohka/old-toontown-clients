# File: C (Python 2.2)

import DirectNotifyGlobal
import Place

class CogHQBasement(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogHQBasement')
    
    def __init__(self, hood, parentFSM, doneEvent):
        Place.Place.__init__(self, hood, doneEvent)
        self.parentFSM = parentFSM


