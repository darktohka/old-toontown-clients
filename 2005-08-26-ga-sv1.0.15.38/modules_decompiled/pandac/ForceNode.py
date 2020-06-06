# File: F (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
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
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpandaphysics._inP9fJJPBy9(name)
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
        returnValue = libpandaphysics._inP9fJJLpP4(self.this)
        return returnValue

    
    def addForce(self, force):
        returnValue = libpandaphysics._inP9fJJYnvh(self.this, force.this)
        return returnValue

    
    def addForcesFrom(self, other):
        returnValue = libpandaphysics._inP9fJJxhJz(self.this, other.this)
        return returnValue

    
    def _ForceNode__overloaded_removeForce_ptrForceNode_ptrBaseForce(self, f):
        returnValue = libpandaphysics._inP9fJJhgaF(self.this, f.this)
        return returnValue

    
    def _ForceNode__overloaded_removeForce_ptrForceNode_int(self, index):
        returnValue = libpandaphysics._inP9fJJ_QKj(self.this, index)
        return returnValue

    
    def _ForceNode__overloaded_writeForces_ptrConstForceNode_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJGWKp(self.this, out.this, indent)
        return returnValue

    
    def _ForceNode__overloaded_writeForces_ptrConstForceNode_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJ6BRM(self.this, out.this)
        return returnValue

    
    def _ForceNode__overloaded_write_ptrConstForceNode_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJuw7S(self.this, out.this, indent)
        return returnValue

    
    def _ForceNode__overloaded_write_ptrConstForceNode_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJOb8p(self.this, out.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ForceNode__overloaded_write_ptrConstForceNode_ptrOstream(*_args)
        elif numArgs == 2:
            return self._ForceNode__overloaded_write_ptrConstForceNode_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def removeForce(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._ForceNode__overloaded_removeForce_ptrForceNode_int(*_args)
            
            import BaseForce
            if isinstance(_args[0], BaseForce.BaseForce):
                return self._ForceNode__overloaded_removeForce_ptrForceNode_ptrBaseForce(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BaseForce.BaseForce> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def writeForces(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._ForceNode__overloaded_writeForces_ptrConstForceNode_ptrOstream(*_args)
        elif numArgs == 2:
            return self._ForceNode__overloaded_writeForces_ptrConstForceNode_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


