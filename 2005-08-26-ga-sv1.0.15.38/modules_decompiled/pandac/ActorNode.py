# File: A (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PhysicalNode

class ActorNode(PhysicalNode.PhysicalNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ActorNode__overloaded_constructor_ptrConstActorNode(self, copy):
        self.this = libpandaphysics._inP9fJJGS52(copy.this)
        self.userManagesMemory = 1

    
    def _ActorNode__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaphysics._inP9fJJy4dn(name)
        self.userManagesMemory = 1

    
    def _ActorNode__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJI6QP()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJ2_Zr()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getPhysicsObject(self):
        returnValue = libpandaphysics._inP9fJJDMRz(self.this)
        import PhysicsObject
        returnObject = PhysicsObject.PhysicsObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setContactVector(self, contactVector):
        returnValue = libpandaphysics._inP9fJJYUGc(self.this, contactVector.this)
        return returnValue

    
    def getContactVector(self):
        returnValue = libpandaphysics._inP9fJJjR9_(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def updateTransform(self):
        returnValue = libpandaphysics._inP9fJJ__bD(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ActorNode__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._ActorNode__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], ActorNode):
                return self._ActorNode__overloaded_constructor_ptrConstActorNode(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <ActorNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


