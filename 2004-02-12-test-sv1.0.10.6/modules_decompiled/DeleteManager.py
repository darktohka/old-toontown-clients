# File: D (Python 2.2)

from ShowBaseGlobal import *
import DistributedObject
import DirectNotifyGlobal

class DeleteManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DeleteManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        return None

    
    def generate(self):
        self.accept('deleteItems', self.d_setInventory)
        return None

    
    def disable(self):
        self.ignore('deleteItems')
        return None

    
    def d_setInventory(self, newInventoryString):
        self.sendUpdate('setInventory', [
            newInventoryString])
        return None


