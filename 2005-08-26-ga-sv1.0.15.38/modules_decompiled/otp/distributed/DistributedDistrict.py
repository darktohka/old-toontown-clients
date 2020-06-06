# File: D (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

class DistributedDistrict(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDistrict')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.cr = cr
        self.name = 'NotGiven'
        self.available = 0

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.cr.activeDistrictMap[self.doId] = self
        messenger.send('shardInfoUpdated')

    
    def delete(self):
        if base.cr.distributedDistrict is self:
            base.cr.distributedDistrict = None
        
        if self.cr.activeDistrictMap.has_key(self.doId):
            del self.cr.activeDistrictMap[self.doId]
        
        DistributedObject.DistributedObject.delete(self)
        messenger.send('shardInfoUpdated')

    
    def setAvailable(self, available):
        self.available = available

    
    def setName(self, name):
        self.name = name

    
    def setAvatarCount(self, avatarCount):
        self.avatarCount = avatarCount

    
    def setNewAvatarCount(self, newAvatarCount):
        self.newAvatarCount = newAvatarCount

    
    def setStats(self, avatarCount, newAvatarCount):
        self.setAvatarCount(avatarCount)
        self.setNewAvatarCount(newAvatarCount)


