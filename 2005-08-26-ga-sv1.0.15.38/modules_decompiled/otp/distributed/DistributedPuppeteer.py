# File: D (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

class DistributedPuppeteer(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPuppeteer')
    notify.setDebug(1)
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        return None

    
    def requestPuppet(self):
        self.sendUpdate('requestPuppet', [])

    
    def acceptPuppet(self):
        self.notify.debug('accepted puppet')

    
    def rejectPuppet(self):
        self.notify.debug('rejected puppet')


