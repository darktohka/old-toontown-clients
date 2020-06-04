# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Namable

class CollisionTraverser(Namable.Namable, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CollisionTraverser__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPHwcayNSW(name)
        self.userManagesMemory = 1

    
    def _CollisionTraverser__overloaded_constructor(self):
        self.this = libpanda._inPHwcaLY8j()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaDjLK:
            libpanda._inPHwcaDjLK(self.this)
        

    
    def setRespectPrevTransform(self, flag):
        returnValue = libpanda._inPHwcadaty(self.this, flag)
        return returnValue

    
    def getRespectPrevTransform(self):
        returnValue = libpanda._inPHwcalqsH(self.this)
        return returnValue

    
    def _CollisionTraverser__overloaded_addCollider_ptrCollisionTraverser_ptrCollisionNode_ptrCollisionHandler(self, node, handler):
        returnValue = libpanda._inPHwcaIXgA(self.this, node.this, handler.this)
        return returnValue

    
    def _CollisionTraverser__overloaded_addCollider_ptrCollisionTraverser_ptrConstNodePath_ptrCollisionHandler(self, collider, handler):
        returnValue = libpanda._inPHwca2H3O(self.this, collider.this, handler.this)
        return returnValue

    
    def _CollisionTraverser__overloaded_removeCollider_ptrCollisionTraverser_ptrCollisionNode(self, node):
        returnValue = libpanda._inPHwcabi2L(self.this, node.this)
        return returnValue

    
    def _CollisionTraverser__overloaded_removeCollider_ptrCollisionTraverser_ptrConstNodePath(self, collider):
        returnValue = libpanda._inPHwcaM6MA(self.this, collider.this)
        return returnValue

    
    def hasCollider(self, collider):
        returnValue = libpanda._inPHwcaWy10(self.this, collider.this)
        return returnValue

    
    def getNumColliders(self):
        returnValue = libpanda._inPHwcaO3k0(self.this)
        return returnValue

    
    def getCollider(self, n):
        returnValue = libpanda._inPHwca8iE2(self.this, n)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getHandler(self, collider):
        returnValue = libpanda._inPHwcaHSoX(self.this, collider.this)
        import CollisionHandler
        returnObject = CollisionHandler.CollisionHandler(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearColliders(self):
        returnValue = libpanda._inPHwcaz8jc(self.this)
        return returnValue

    
    def traverse(self, root):
        returnValue = libpanda._inPHwcaIgJi(self.this, root.this)
        return returnValue

    
    def resetPrevTransform(self, root):
        returnValue = libpanda._inPHwcatQ7L(self.this, root.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPHwcaKrH1(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPHwcaFI_7(self.this, out.this, indentLevel)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CollisionTraverser__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._CollisionTraverser__overloaded_constructor_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def removeCollider(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                return self._CollisionTraverser__overloaded_removeCollider_ptrCollisionTraverser_ptrConstNodePath(*_args)
            
            import CollisionNode
            if isinstance(_args[0], CollisionNode.CollisionNode):
                return self._CollisionTraverser__overloaded_removeCollider_ptrCollisionTraverser_ptrCollisionNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> <CollisionNode.CollisionNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addCollider(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                return self._CollisionTraverser__overloaded_addCollider_ptrCollisionTraverser_ptrConstNodePath_ptrCollisionHandler(*_args)
            
            import CollisionNode
            if isinstance(_args[0], CollisionNode.CollisionNode):
                return self._CollisionTraverser__overloaded_addCollider_ptrCollisionTraverser_ptrCollisionNode_ptrCollisionHandler(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> <CollisionNode.CollisionNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


