# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class CollisionTraverser(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPHwcaIY8j()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaDjLK:
            libpanda._inPHwcaDjLK(self.this)
        

    
    def addCollider(self, node, handler):
        returnValue = libpanda._inPHwcaIXgA(self.this, node.this, handler.this)
        return returnValue

    
    def removeCollider(self, node):
        returnValue = libpanda._inPHwcabi2L(self.this, node.this)
        return returnValue

    
    def hasCollider(self, node):
        returnValue = libpanda._inPHwcaQzix(self.this, node.this)
        return returnValue

    
    def getNumColliders(self):
        returnValue = libpanda._inPHwcaP3k0(self.this)
        return returnValue

    
    def getCollider(self, n):
        returnValue = libpanda._inPHwca_iE2(self.this, n)
        import CollisionNode
        returnObject = CollisionNode.CollisionNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getHandler(self, node):
        returnValue = libpanda._inPHwcaCAgr(self.this, node.this)
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
        returnValue = libpanda._inPHwcaJgJi(self.this, root.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPHwcaNrH1(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPHwcaGI_7(self.this, out.this, indentLevel)
        return returnValue


