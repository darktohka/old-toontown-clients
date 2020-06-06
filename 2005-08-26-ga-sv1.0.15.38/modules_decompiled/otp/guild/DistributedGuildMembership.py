# File: D (Python 2.2)

from direct.distributed.ClockDelta import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

class DistributedGuildMembership(DistributedObject.DistributedObject):
    
    def __init__(self, air):
        DistributedObject.DistributedObject.__init__(self, air)

    
    def delete(self):
        self.ignoreAll()
        DistributedObject.DistributedObject.delete(self)


