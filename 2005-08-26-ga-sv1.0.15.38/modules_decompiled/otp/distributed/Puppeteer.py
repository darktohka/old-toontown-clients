# File: P (Python 2.2)

from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal

class Puppeteer(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('Puppeteer')
    
    def __init__(self):
        DirectObject.DirectObject.__init__(self)
        return None

    
    def startPuppet(self, puppet):
        self.notify.debug('Starting puppet %d' % puppet.doId)

    
    def stopPuppet(self, puppet):
        self.notify.debug('Stopping puppet %d' % puppet.doId)


