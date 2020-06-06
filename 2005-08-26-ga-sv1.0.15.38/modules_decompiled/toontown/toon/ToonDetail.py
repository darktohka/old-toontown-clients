# File: T (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from otp.avatar import AvatarDetail
from toontown.toon import DistributedToon

class ToonDetail(AvatarDetail.AvatarDetail):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonDetail')
    
    def createHolder(self):
        return DistributedToon.DistributedToon(base.cr, bFake = True)


