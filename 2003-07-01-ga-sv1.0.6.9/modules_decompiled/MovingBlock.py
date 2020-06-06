# File: M (Python 2.2)

from ShowBaseGlobal import *
from IntervalGlobal import *
import DirectObject
import ToontownGlobals

class MovingBlock(DirectObject.DirectObject, NodePath):
    
    def __init__(self, index, model):
        self.token = ToontownGlobals.SPDynamic + index
        self.name = 'MovingBlock-%d' % index
        NodePath.__init__(self, hidden.attachNewNode(self.name))
        self.model = model.copyTo(self)
        self.model.find('**/floor').setName(self.name)
        toonbase.tcr.token2nodePath[self.token] = self
        self.accept('on-floor', self._MovingBlock__handleOnFloor)
        self.accept('off-floor', self._MovingBlock__handleOffFloor)
        return None

    
    def delete(self):
        del toonbase.tcr.token2nodePath[self.token]
        self.model.removeNode()
        del self.model
        self.ignore('on-floor')
        self.ignore('off-floor')
        return None

    
    def _MovingBlock__handleOnFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == self.name:
            print 'on floor %s' % self.name
            toonbase.localToon.b_setParent(self.token)
            base.drive.node().setPos(toonbase.localToon.getPos())
            base.drive.node().setHpr(toonbase.localToon.getHpr())
        
        return None

    
    def _MovingBlock__handleOffFloor(self, collEntry):
        if collEntry.getIntoNode().getName() == self.name:
            print 'off floor %s' % self.name
            toonbase.localToon.b_setParent(ToontownGlobals.SPRender)
            base.drive.node().setPos(toonbase.localToon.getPos())
            base.drive.node().setHpr(toonbase.localToon.getHpr())
        
        return None


