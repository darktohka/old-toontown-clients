# File: D (Python 2.2)

from toontown.toonbase.ToontownGlobals import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.catalog import CatalogItem
from toontown.toonbase import ToontownGlobals
from direct.distributed import DistributedObject
from toontown.toonbase import TTLocalizer
import DistributedHouseItem
from direct.distributed import DistributedSmoothNode
from direct.task import Task
import HouseGlobals

class DistributedFurnitureItem(DistributedHouseItem.DistributedHouseItem, DistributedSmoothNode.DistributedSmoothNode):
    notify = directNotify.newCategory('DistributedFurnitureItem')
    
    def __init__(self, cr):
        DistributedHouseItem.DistributedHouseItem.__init__(self, cr)
        DistributedSmoothNode.DistributedSmoothNode.__init__(self, cr)
        NodePath.__init__(self)
        self._DistributedFurnitureItem__broadcastFrequency = 0.25
        self._DistributedFurnitureItem__adjustStarted = 0
        self.furnitureMgr = None
        self.transmitRelativeTo = None

    
    def generate(self):
        DistributedHouseItem.DistributedHouseItem.generate(self)
        self._DistributedFurnitureItem__taskName = self.taskName('sendRequestPosHpr')

    
    def announceGenerate(self):
        DistributedHouseItem.DistributedHouseItem.announceGenerate(self)
        self.load()

    
    def load(self):
        pass

    
    def disable(self):
        taskMgr.remove(self._DistributedFurnitureItem__taskName)
        self.stopSmooth()
        self.furnitureMgr.dfitems.remove(self)
        self.furnitureMgr = None
        DistributedHouseItem.DistributedHouseItem.disable(self)

    
    def delete(self):
        self.removeNode()
        del self.item
        DistributedHouseItem.DistributedHouseItem.delete(self)

    
    def setItem(self, furnitureMgrId, blob):
        self.furnitureMgr = self.cr.doId2do[furnitureMgrId]
        self.furnitureMgr.dfitems.append(self)
        self.item = CatalogItem.getItem(blob, store = CatalogItem.Customization)
        self.assign(self.loadModel())
        interior = self.furnitureMgr.getInteriorObject()
        self.reparentTo(interior.interior)

    
    def loadModel(self):
        return self.item.loadModel()

    
    def startAdjustPosHpr(self):
        if self._DistributedFurnitureItem__adjustStarted:
            return None
        
        self._DistributedFurnitureItem__adjustStarted = 1
        self.clearSmoothing()
        taskMgr.remove(self._DistributedFurnitureItem__taskName)
        posHpr = self._DistributedFurnitureItem__getPosHpr()
        self._DistributedFurnitureItem__oldPosHpr = posHpr
        self.sendRequestPosHpr(0, *posHpr)
        taskMgr.doMethodLater(self._DistributedFurnitureItem__broadcastFrequency, self._DistributedFurnitureItem__posHprBroadcast, self._DistributedFurnitureItem__taskName)

    
    def _DistributedFurnitureItem__posHprBroadcast(self, task):
        posHpr = self._DistributedFurnitureItem__getPosHpr()
        if not self._DistributedFurnitureItem__comparePosHpr(posHpr, self._DistributedFurnitureItem__oldPosHpr, 0.10000000000000001):
            pass
        1
        self._DistributedFurnitureItem__oldPosHpr = posHpr
        self.sendRequestPosHpr(0, *posHpr)
        taskMgr.doMethodLater(self._DistributedFurnitureItem__broadcastFrequency, self._DistributedFurnitureItem__posHprBroadcast, self._DistributedFurnitureItem__taskName)
        return Task.done

    
    def stopAdjustPosHpr(self):
        if not (self._DistributedFurnitureItem__adjustStarted):
            return None
        
        self._DistributedFurnitureItem__adjustStarted = 0
        taskMgr.remove(self._DistributedFurnitureItem__taskName)
        posHpr = self._DistributedFurnitureItem__getPosHpr()
        self.sendRequestPosHpr(1, *posHpr)
        del self._DistributedFurnitureItem__oldPosHpr

    
    def sendRequestPosHpr(self, final, x, y, z, h, p, r):
        t = globalClockDelta.getFrameNetworkTime()
        self.sendUpdate('requestPosHpr', (final, x, y, z, h, p, r, t))

    
    def setMode(self, mode, avId):
        if mode == HouseGlobals.FURNITURE_MODE_START:
            if avId != base.localAvatar.getDoId():
                self.startSmooth()
            
        elif mode == HouseGlobals.FURNITURE_MODE_STOP:
            if avId != base.localAvatar.getDoId():
                self.stopSmooth()
            
        elif mode == HouseGlobals.FURNITURE_MODE_OFF:
            pass
        else:
            self.notify.warning('setMode: unknown mode: %s avId: %s' % (mode, avId))

    
    def _DistributedFurnitureItem__getPosHpr(self):
        if self.transmitRelativeTo == None:
            pos = self.getPos()
            hpr = self.getHpr()
        else:
            pos = self.getPos(self.transmitRelativeTo)
            hpr = self.getHpr(self.transmitRelativeTo)
        return (pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2])

    
    def _DistributedFurnitureItem__comparePosHpr(self, a, b, threshold):
        for i in range(len(a)):
            if abs(a[i] - b[i]) >= threshold:
                return 1
            
        
        return 0


