# File: P (Python 2.2)

from PandaObject import *
import ToontownGlobals

class PositionExaminer(PandaObject, NodePath):
    
    def __init__(self):
        
        try:
            return None
        except:
            self._PositionExaminer__initialized = 1

        NodePath.__init__(self, hidden.attachNewNode('PositionExaminer'))
        self.cRay = CollisionRay(0.0, 0.0, 6.0, 0.0, 0.0, -1.0)
        self.cRayNode = CollisionNode('cRayNode')
        self.cRayNode.addSolid(self.cRay)
        self.cRayNodePath = self.attachNewNode(self.cRayNode)
        self.cRayNodePath.hide()
        self.cRayBitMask = ToontownGlobals.FloorBitmask
        self.cRayNode.setFromCollideMask(self.cRayBitMask)
        self.cRayNode.setIntoCollideMask(BitMask32.allOff())
        self.cSphere = CollisionSphere(0.0, 0.0, 0.0, 1.5)
        self.cSphereNode = CollisionNode('cSphereNode')
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereBitMask = ToontownGlobals.WallBitmask
        self.cSphereNode.setFromCollideMask(self.cSphereBitMask)
        self.cSphereNode.setIntoCollideMask(BitMask32.allOff())
        self.ccLine = CollisionSegment(0.0, 0.0, 0.0, 1.0, 0.0, 0.0)
        self.ccLineNode = CollisionNode('ccLineNode')
        self.ccLineNode.addSolid(self.ccLine)
        self.ccLineNodePath = self.attachNewNode(self.ccLineNode)
        self.ccLineNodePath.hide()
        self.ccLineBitMask = ToontownGlobals.CameraBitmask
        self.ccLineNode.setFromCollideMask(self.ccLineBitMask)
        self.ccLineNode.setIntoCollideMask(BitMask32.allOff())
        self.cRayTrav = CollisionTraverser()
        self.cRayQueue = CollisionHandlerQueue()
        self.cRayTrav.addCollider(self.cRayNode, self.cRayQueue)
        self.cSphereTrav = CollisionTraverser()
        self.cSphereQueue = CollisionHandlerQueue()
        self.cSphereTrav.addCollider(self.cSphereNode, self.cSphereQueue)
        self.ccLineTrav = CollisionTraverser()
        self.ccLineQueue = CollisionHandlerQueue()
        self.ccLineTrav.addCollider(self.ccLineNode, self.ccLineQueue)

    
    def delete(self):
        del self.cRay
        del self.cRayNode
        self.cRayNodePath.removeNode()
        del self.cRayNodePath
        del self.cSphere
        del self.cSphereNode
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath
        del self.ccLine
        del self.ccLineNode
        self.ccLineNodePath.removeNode()
        del self.ccLineNodePath
        del self.cRayTrav
        del self.cRayQueue
        del self.cSphereTrav
        del self.cSphereQueue
        del self.ccLineTrav
        del self.ccLineQueue

    
    def consider(self, node, pos):
        self.reparentTo(node)
        self.setPos(pos)
        result = None
        self.cRayTrav.traverse(render)
        if self.cRayQueue.getNumEntries() != 0:
            self.cRayQueue.sortEntries()
            floorPoint = self.cRayQueue.getEntry(0).getFromIntersectionPoint()
            if abs(floorPoint[2]) <= 4.0:
                pos += floorPoint
                self.setPos(pos)
                self.cSphereTrav.traverse(render)
                if self.cSphereQueue.getNumEntries() == 0:
                    self.ccLine.setPointA(0, 0, 0)
                    self.ccLine.setPointB(-pos[0], -pos[1], -pos[2])
                    self.ccLineTrav.traverse(render)
                    if self.ccLineQueue.getNumEntries() == 0:
                        result = pos
                    
                
            
        
        self.reparentTo(hidden)
        self.cRayQueue.clearEntries()
        self.cSphereQueue.clearEntries()
        self.ccLineQueue.clearEntries()
        return result


