# File: S (Python 2.2)

from ShowBaseGlobal import *
import DistributedObject
import DirectNotifyGlobal

class SafeZoneManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('SafeZoneManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        return None

    
    def generate(self):
        self.accept('enterSafeZone', self.d_enterSafeZone)
        self.accept('exitSafeZone', self.d_exitSafeZone)
        return None

    
    def disable(self):
        self.ignoreAll()
        return None

    
    def d_enterSafeZone(self):
        self.sendUpdate('enterSafeZone', [])
        return None

    
    def d_exitSafeZone(self):
        self.sendUpdate('exitSafeZone', [])
        return None


