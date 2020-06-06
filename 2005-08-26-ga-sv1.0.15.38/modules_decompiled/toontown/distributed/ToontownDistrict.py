# File: T (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from otp.distributed import DistributedDistrict

class ToontownDistrict(DistributedDistrict.DistributedDistrict):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownDistrict')
    
    def setAvatarCount(self, avatarCount):
        self.avatarCount = avatarCount

    
    def setNewAvatarCount(self, newAvatarCount):
        self.newAvatarCount = newAvatarCount

    
    def setStats(self, avatarCount, newAvatarCount):
        self.setAvatarCount(avatarCount)
        self.setNewAvatarCount(newAvatarCount)


