# File: L (Python 2.2)

from ShowBaseGlobal import *
import ToontownGlobals
import DistributedObject
import DirectNotifyGlobal
import Localizer

class LobbyManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('LobbyManager')
    SetFactoryZoneMsg = 'setFactoryZone'
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def generate(self):
        self.notify.debug('generate')
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        self.notify.debug('disable')
        self.ignoreAll()

    
    def getSuitDoorOrigin(self):
        return 1

    
    def getBossLevel(self):
        return 0


