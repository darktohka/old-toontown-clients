# File: E (Python 2.2)

from direct.directnotify import DirectNotifyGlobal

class EntityCreatorBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('EntityCreator')
    
    def __init__(self, level):
        self.level = level
        self.entType2Ctor = { }

    
    def createEntity(self, entId):
        entType = self.level.getEntityType(entId)
        if not self.entType2Ctor.has_key(entType):
            self.notify.error('unknown entity type: %s (ent%s)' % (entType, entId))
        
        ent = self.doCreateEntity(self.entType2Ctor[entType], entId)
        return ent

    
    def getEntityTypes(self):
        return self.entType2Ctor.keys()

    
    def privRegisterType(self, entType, ctor):
        if self.entType2Ctor.has_key(entType):
            self.notify.warning('replacing %s ctor %s with %s' % (entType, self.entType2Ctor[entType], ctor))
        
        self.entType2Ctor[entType] = ctor

    
    def privRegisterTypes(self, type2ctor):
        for (entType, ctor) in type2ctor.items():
            self.privRegisterType(entType, ctor)
        


