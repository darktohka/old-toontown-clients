# File: D (Python 2.2)

from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class DistributedTrophyMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrophyMgr')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def generate(self):
        if base.cr.trophyManager != None:
            base.cr.trophyManager.delete()
        
        base.cr.trophyManager = self
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        base.cr.trophyManager = None
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        base.cr.trophyManager = None
        DistributedObject.DistributedObject.delete(self)

    
    def d_requestTrophyScore(self):
        self.sendUpdate('requestTrophyScore', [])


