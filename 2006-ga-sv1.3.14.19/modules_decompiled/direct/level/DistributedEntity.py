# File: D (Python 2.2)

from direct.distributed import DistributedObject
import Entity
from direct.directnotify import DirectNotifyGlobal

class DistributedEntity(DistributedObject.DistributedObject, Entity.Entity):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEntity')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        Entity.Entity.__init__(self)

    
    def generateInit(self):
        DistributedEntity.notify.debug('generateInit')
        DistributedObject.DistributedObject.generateInit(self)

    
    def generate(self):
        DistributedEntity.notify.debug('generate')
        DistributedObject.DistributedObject.generate(self)

    
    def setLevelDoId(self, levelDoId):
        DistributedEntity.notify.debug('setLevelDoId: %s' % levelDoId)
        self.levelDoId = levelDoId

    
    def setEntId(self, entId):
        DistributedEntity.notify.debug('setEntId: %s' % entId)
        self.entId = entId

    
    def announceGenerate(self):
        DistributedEntity.notify.debug('announceGenerate (%s)' % self.entId)
        level = base.cr.doId2do[self.levelDoId]
        self.initializeEntity(level, self.entId)
        self.level.onEntityCreate(self.entId)
        DistributedObject.DistributedObject.announceGenerate(self)

    
    def disable(self):
        DistributedEntity.notify.debug('disable (%s)' % self.entId)
        self.destroy()
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        DistributedEntity.notify.debug('delete')
        DistributedObject.DistributedObject.delete(self)


