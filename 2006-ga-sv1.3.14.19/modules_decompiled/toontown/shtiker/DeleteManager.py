# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal

class DeleteManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DeleteManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def generate(self):
        self.accept('deleteItems', self.d_setInventory)

    
    def disable(self):
        self.ignore('deleteItems')

    
    def d_setInventory(self, newInventoryString):
        self.sendUpdate('setInventory', [
            newInventoryString])


