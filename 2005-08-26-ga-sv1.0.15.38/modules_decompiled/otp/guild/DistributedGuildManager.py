# File: D (Python 2.2)

from direct.distributed.ClockDelta import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

class DistributedGuildManager(DistributedObject.DistributedObject):
    neverDisable = 1
    
    def __init__(self, air):
        DistributedObject.DistributedObject.__init__(self, air)
        self.guildListId = None

    
    def generate(self):
        if self.cr.guildManager != None:
            self.cr.guildManager.delete()
        
        self.cr.guildManager = self
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        self.ignoreAll()
        DistributedObject.DistributedObject.delete(self)

    
    def load(self):
        pass

    
    def sendCreateRequest(self, newGuildName):
        self.sendUpdate('requestCreate', [
            newGuildName])

    
    def rejectCreate(self, reasonId):
        print 'guild created rejected %s %s' % (reasonId, '')

    
    def getGuildListId(self):
        return self.guildListId


