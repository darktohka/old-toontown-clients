# File: D (Python 2.2)

from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class DistributedBankMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBankMgr')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def generate(self):
        if base.cr.bankManager != None:
            base.cr.bankManager.delete()
        
        base.cr.bankManager = self
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        base.cr.bankManager = None
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        base.cr.bankManager = None
        DistributedObject.DistributedObject.delete(self)

    
    def d_transferMoney(self, amount):
        self.sendUpdate('transferMoney', [
            amount])


