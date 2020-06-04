# File: D (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

class DistributedPuppeteer(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPuppeteer')
    notify.setDebug(1)
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        return None

    
    def startPuppet(self, puppet):
        self.notify.debug('Starting puppet %d' % puppet.doId)

    
    def stopPuppet(self, puppet):
        self.notify.debug('Stopping puppet %d' % puppet.doId)

    
    def requestPuppet(self, type):
        self.sendUpdate('requestPuppet', [
            type])

    
    def acceptPuppet(self, type):
        self.notify.debug('accepted puppet type = %s' % type)

    
    def rejectPuppet(self, type):
        self.notify.debug('rejected puppet type = %s' % type)


