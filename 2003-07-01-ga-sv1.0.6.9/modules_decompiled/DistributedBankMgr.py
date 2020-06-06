# File: D (Python 2.2)

import DistributedObject
import DirectNotifyGlobal
import Localizer

class DistributedBankMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBankMgr')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def generate(self):
        if toonbase.tcr.bankManager != None:
            toonbase.tcr.bankManager.delete()
        
        toonbase.tcr.bankManager = self
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        toonbase.tcr.bankManager = None
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        toonbase.tcr.bankManager = None
        DistributedObject.DistributedObject.delete(self)

    
    def d_transferMoney(self, amount):
        self.sendUpdate('transferMoney', [
            amount])


