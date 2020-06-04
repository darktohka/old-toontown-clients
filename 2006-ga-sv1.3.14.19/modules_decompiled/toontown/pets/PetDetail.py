# File: P (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from otp.avatar import AvatarDetail
from toontown.pets import DistributedPet

class PetDetail(AvatarDetail.AvatarDetail):
    notify = DirectNotifyGlobal.directNotify.newCategory('PetDetail')
    
    def createHolder(self):
        print 'Using PetDetail createHolder'
        pet = DistributedPet.DistributedPet(base.cr, bFake = True)
        pet.generate()
        return pet


