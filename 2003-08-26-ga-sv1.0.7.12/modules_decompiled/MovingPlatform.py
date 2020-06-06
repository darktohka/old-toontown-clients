# File: M (Python 2.2)

from ShowBaseGlobal import *
from IntervalGlobal import *
import DirectObject
import ToontownGlobals
import DirectNotifyGlobal

class MovingPlatform(DirectObject.DirectObject, NodePath):
    notify = DirectNotifyGlobal.directNotify.newCategory('MovingPlatform')
    
    def __init__(self, index, model, floorNodeName = None):
        if floorNodeName is None:
            floorNodeName = 'floor'
        
        self.parentToken = ToontownGlobals.SPDynamic + index
        self.name = 'MovingPlatform-%d' % index
        NodePath.__init__(self, hidden.attachNewNode(self.name))
        self.model = model.copyTo(self)
        self.model.find('**/%s' % floorNodeName).setName(self.name)
        toonbase.tcr.parentMgr.registerParent(self.parentToken, self)
        self.hasLt = 0
        if toonbase.localToon.wantAvatarPhysics:
            self.accept('enter%s' % self.name, self._MovingPlatform__handleEnter)
            self.accept('exit%s' % self.name, self._MovingPlatform__handleExit)
        else:
            self.accept('on-floor', self._MovingPlatform__handleOnFloor)
            self.accept('off-floor', self._MovingPlatform__handleOffFloor)

    
    def destroy(self):
        if self.hasLt:
            self._MovingPlatform__releaseLt()
        
        toonbase.tcr.parentMgr.unregisterParent(self.parentToken)
        self.model.removeNode()
        del self.model
        self.ignoreAll()

    
    def getEnterEvent(self):
        return '%s-enter' % self.name

    
    def getExitEvent(self):
        return '%s-exit' % self.name

    
    def releaseLocalToon(self):
        if self.hasLt:
            self._MovingPlatform__releaseLt()
        

    
    def _MovingPlatform__handleEnter(self, collEntry):
        self.notify.debug('on floor %s' % self.name)
        self._MovingPlatform__grabLt()
        messenger.send(self.getEnterEvent())

    
    def _MovingPlatform__handleExit(self, collEntry):
        self.notify.debug('off floor %s' % self.name)
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
        if toonbase.localToon.getParent().compareTo(self) == 0:
            toonbase.localToon.b_setParent(ToontownGlobals.SPRender)
        
        self.hasLt = 0


