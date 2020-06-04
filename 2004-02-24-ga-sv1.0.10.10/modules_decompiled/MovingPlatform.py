# File: M (Python 2.2)

from ShowBaseGlobal import *
from IntervalGlobal import *
import DirectObject
import ToontownGlobals
import DirectNotifyGlobal
import types

class MovingPlatform(DirectObject.DirectObject, NodePath):
    notify = DirectNotifyGlobal.directNotify.newCategory('MovingPlatform')
    
    def __init__(self):
        self.hasLt = 0
        DirectObject.DirectObject.__init__(self)
        NodePath.__init__(self)

    
    def setupCopyModel(self, parentToken, model, floorNodeName = None, parentingNode = None):
        if floorNodeName is None:
            floorNodeName = 'floor'
        
        if type(parentToken) == types.IntType:
            parentToken = ToontownGlobals.SPDynamic + parentToken
        
        self.parentToken = parentToken
        self.name = 'MovingPlatform-%s' % parentToken
        self.assign(hidden.attachNewNode(self.name))
        self.model = model.copyTo(self)
        self.ownsModel = 1
        floorList = self.model.findAllMatches('**/%s' % floorNodeName).asList()
        for floor in floorList:
            floor.setName(self.name)
        
        if parentingNode == None:
            parentingNode = self
        
        toonbase.tcr.parentMgr.registerParent(self.parentToken, parentingNode)
        self.parentingNode = parentingNode
        self.accept('enter%s' % self.name, self._MovingPlatform__handleEnter)
        self.accept('exit%s' % self.name, self._MovingPlatform__handleExit)

    
    def setupEntity(self, entityId, parent, floorNodeName = None):
        self.parentToken = ToontownGlobals.SPDynamic + entityId
        self.assign(parent)
        self.ownsModel = 0
        self.name = floorNodeName
        toonbase.tcr.parentMgr.registerParent(self.parentToken, parent)
        self.parentingNode = parent
        self.accept('enter%s' % self.name, self._MovingPlatform__handleEnter)
        self.accept('exit%s' % self.name, self._MovingPlatform__handleExit)

    
    def destroy(self):
        toonbase.tcr.parentMgr.unregisterParent(self.parentToken)
        self.ignoreAll()
        if self.hasLt:
            self._MovingPlatform__releaseLt()
        
        if self.ownsModel:
            self.model.removeNode()
            del self.model
        

    
    def getEnterEvent(self):
        return '%s-enter' % self.name

    
    def getExitEvent(self):
        return '%s-exit' % self.name

    
    def releaseLocalToon(self):
        if self.hasLt:
            self._MovingPlatform__releaseLt()
        

    
    def _MovingPlatform__handleEnter(self, collEntry):
        self.notify.info('on movingPlatform %s' % self.name)
        self._MovingPlatform__grabLt()
        messenger.send(self.getEnterEvent())

    
    def _MovingPlatform__handleExit(self, collEntry):
        self.notify.info('off movingPlatform %s' % self.name)
        self._MovingPlatform__releaseLt()
        messenger.send(self.getExitEvent())

    
    def _MovingPlatform__handleOnFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == self.name:
            self._MovingPlatform__handleEnter(collEntry)
        

    
    def _MovingPlatform__handleOffFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == self.name:
            self._MovingPlatform__handleExit(collEntry)
        

    
    def _MovingPlatform__grabLt(self):
        toonbase.localToon.b_setParent(self.parentToken)
        self.hasLt = 1

    
    def _MovingPlatform__releaseLt(self):
        if toonbase.localToon.getParent().compareTo(self.parentingNode) == 0:
            toonbase.localToon.b_setParent(ToontownGlobals.SPRender)
            toonbase.localToon.controlManager.currentControls.doDeltaPos()
        
        self.hasLt = 0


