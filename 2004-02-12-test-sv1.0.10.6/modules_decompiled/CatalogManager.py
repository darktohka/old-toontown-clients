# File: C (Python 2.2)

import DistributedObject
import DirectNotifyGlobal

class CatalogManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('CatalogManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def generate(self):
        if toonbase.tcr.catalogManager != None:
            toonbase.tcr.catalogManager.delete()
        
        toonbase.tcr.catalogManager = self
        DistributedObject.DistributedObject.generate(self)
        if toonbase.localToon.catalogScheduleNextTime == 0:
            self.d_startCatalog()
        

    
    def disable(self):
        toonbase.tcr.catalogManager = None
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        toonbase.tcr.catalogManager = None
        DistributedObject.DistributedObject.delete(self)

    
    def d_startCatalog(self):
        self.sendUpdate('startCatalog', [])


