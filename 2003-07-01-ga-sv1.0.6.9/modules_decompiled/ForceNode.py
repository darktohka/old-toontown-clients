# File: F (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PandaNode

class ForceNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpandaphysics._inP9fJJIBy9(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJGQOV()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def clear(self):
        returnValue = libpandaphysics._inP9fJJcXNM(self.this)
        return returnValue

    
    def getForce(self, index):
        returnValue = libpandaphysics._inP9fJJRzsU(self.this, index)
        import BaseForce
        returnObject = BaseForce.BaseForce(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumForces(self):
        returnValue = libpandaphysics._inP9fJJUpP4(self.this)
        return returnValue

    
    def addForce(self, force):
        returnValue = libpandaphysics._inP9fJJXnvh(self.this, force.this)
        return returnValue

    
    def addForcesFrom(self, other):
        returnValue = libpandaphysics._inP9fJJ_hJz(self.this, other.this)
        return returnValue

    
    def _ForceNode__overloaded_removeForce_ptrForceNode_ptrBaseForce(self, f):
        returnValue = libpandaphysics._inP9fJJhgaF(self.this, f.this)
        return returnValue

    
    def _ForceNode__overloaded_removeForce_ptrForceNode_int(self, index):
        returnValue = libpandaphysics._inP9fJJ_QKj(self.this, index)
        return returnValue

    
    def removeForce(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import BaseForce
            if isinstance(_args[0], types.IntType):
                return self._ForceNode__overloaded_removeForce_ptrForceNode_int(_args[0])
            elif isinstance(_args[0], BaseForce.BaseForce):
                return self._ForceNode__overloaded_removeForce_ptrForceNode_ptrBaseForce(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BaseForce.BaseForce> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


