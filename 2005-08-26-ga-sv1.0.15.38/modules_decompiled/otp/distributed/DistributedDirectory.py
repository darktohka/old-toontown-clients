# File: D (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject, ESGenerated

class DistributedDirectory(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDirectory')
    
    def __init__(self, cr):
        DistributedObject.__init__(self, cr)

    
    def setName(self, name):
        self.name = name

    
    def announceGenerate(self):
        if self.activeState != ESGenerated:
            messenger.send('newDistributedDirectory', [
                self.name,
                self])
        
        DistributedObject.announceGenerate(self)


