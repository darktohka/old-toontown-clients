# File: D (Python 2.2)

import DistributedObject
import DirectNotifyGlobal
import Localizer

class DistributedTrophyMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrophyMgr')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def generate(self):
        if toonbase.tcr.trophyManager != None:
            toonbase.tcr.trophyManager.delete()
        
        toonbase.tcr.trophyManager = self
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        toonbase.tcr.trophyManager = None
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        toonbase.tcr.trophyManager = None
        DistributedObject.DistributedObject.delete(self)

    
    def d_requestTrophyScore(self):
        self.sendUpdate('requestTrophyScore', [])


