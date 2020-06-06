# File: M (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
from direct.showbase import DirectObject
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
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
        if len(floorList) == 0:
            MovingPlatform.notify.warning('no floors in model')
            return None
        
        for floor in floorList:
            floor.setName(self.name)
        
        if parentingNode == None:
            parentingNode = self
        
        base.cr.parentMgr.registerParent(self.parentToken, parentingNode)
        self.parentingNode = parentingNode
        self.accept('enter%s' % self.name, self._MovingPlatform__handleEnter)
        self.accept('exit%s' % self.name, self._MovingPlatform__handleExit)

    
    def destroy(self):
        base.cr.parentMgr.unregisterParent(self.parentToken)
        self.ignoreAll()
        if self.hasLt:
            self._MovingPlatform__releaseLt()
        
        if self.ownsModel:
            self.model.removeNode()
            del self.model
        
        if hasattr(self, 'parentingNode') and self.parentingNode is self:
            del self.parentingNode
        

    
    def getEnterEvent(self):
        return '%s-enter' % self.name

    
    def getExitEvent(self):
        return '%s-exit' % self.name

    
    def releaseLocalToon(self):
        if self.hasLt:
            self._MovingPlatform__releaseLt()
        

    
    def _MovingPlatform__handleEnter(self, collEntry):
        self.notify.debug('on movingPlatform %s' % self.name)
        self._MovingPlatform__grabLt()
        messenger.send(self.getEnterEvent())

    
    def _MovingPlatform__handleExit(self, collEntry):
        self.notify.debug('off movingPlatform %s' % self.name)
        self._MovingPlatform__releaseLt()
        messenger.send(self.getExitEvent())

    
    def _MovingPlatform__handleOnFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == self.name:
            self._MovingPlatform__handleEnter(collEntry)
        

    
    def _MovingPlatform__handleOffFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == self.name:
            self._MovingPlatform__handleExit(collEntry)
        

    
    def _MovingPlatform__grabLt(self):
        base.localAvatar.b_setParent(self.parentToken)
        self.hasLt = 1

    
    def _MovingPlatform__releaseLt(self):
        if base.localAvatar.getParent().compareTo(self.parentingNode) == 0:
            base.localAvatar.b_setParent(ToontownGlobals.SPRender)
            base.localAvatar.controlManager.currentControls.doDeltaPos()
        
        self.hasLt = 0


