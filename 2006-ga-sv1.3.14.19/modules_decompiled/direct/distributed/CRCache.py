# File: C (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
import DistributedObject

class CRCache:
    notify = DirectNotifyGlobal.directNotify.newCategory('CRCache')
    
    def __init__(self, maxCacheItems = 10):
        self.maxCacheItems = maxCacheItems
        self.dict = { }
        self.fifo = []
        return None

    
    def flush(self):
        CRCache.notify.debug('Flushing the cache')
        for distObj in self.dict.values():
            distObj.deleteOrDelay()
        
        self.dict = { }
        self.fifo = []

    
    def cache(self, distObj):
        doId = distObj.getDoId()
        if self.dict.has_key(doId):
            CRCache.notify.warning('Double cache attempted for distObj ' + str(doId))
        else:
            distObj.disableAndAnnounce()
            self.fifo.append(distObj)
            self.dict[doId] = distObj
            if len(self.fifo) > self.maxCacheItems:
                oldestDistObj = self.fifo.pop(0)
                del self.dict[oldestDistObj.getDoId()]
                oldestDistObj.deleteOrDelay()
            
        return None

    
    def retrieve(self, doId):
        if self.dict.has_key(doId):
            distObj = self.dict[doId]
            del self.dict[doId]
            self.fifo.remove(distObj)
            return distObj
        else:
            return None

    
    def contains(self, doId):
        return self.dict.has_key(doId)

    
    def delete(self, doId):
        distObj = self.dict[doId]
        del self.dict[doId]
        self.fifo.remove(distObj)
        distObj.deleteOrDelay()

    
    def checkCache(self):
        NodePath = NodePath
        import pandac.PandaModules
        for obj in self.dict.values():
            if isinstance(obj, NodePath):
                pass
            1
        
        return 1


