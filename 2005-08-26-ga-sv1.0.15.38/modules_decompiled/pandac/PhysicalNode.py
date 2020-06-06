# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class PhysicalNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
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
        self.this = libpandaphysics._inP9fJJQNir(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJohu_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def clear(self):
        returnValue = libpandaphysics._inP9fJJvC_W(self.this)
        return returnValue

    
    def getPhysical(self, index):
        returnValue = libpandaphysics._inP9fJJGi58(self.this, index)
        import Physical
        returnObject = Physical.Physical(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumPhysicals(self):
        returnValue = libpandaphysics._inP9fJJHtda(self.this)
        return returnValue

    
    def addPhysical(self, physical):
        returnValue = libpandaphysics._inP9fJJmr3_(self.this, physical.this)
        return returnValue

    
    def addPhysicalsFrom(self, other):
        returnValue = libpandaphysics._inP9fJJG36z(self.this, other.this)
        return returnValue

    
    def _PhysicalNode__overloaded_removePhysical_ptrPhysicalNode_ptrPhysical(self, physical):
        returnValue = libpandaphysics._inP9fJJz6iS(self.this, physical.this)
        return returnValue

    
    def _PhysicalNode__overloaded_removePhysical_ptrPhysicalNode_int(self, index):
        returnValue = libpandaphysics._inP9fJJOXfn(self.this, index)
        return returnValue

    
    def _PhysicalNode__overloaded_write_ptrConstPhysicalNode_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJXwip(self.this, out.this, indent)
        return returnValue

    
    def _PhysicalNode__overloaded_write_ptrConstPhysicalNode_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJOEwa(self.this, out.this)
        return returnValue

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PhysicalNode__overloaded_write_ptrConstPhysicalNode_ptrOstream(*_args)
        elif numArgs == 2:
            return self._PhysicalNode__overloaded_write_ptrConstPhysicalNode_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def removePhysical(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._PhysicalNode__overloaded_removePhysical_ptrPhysicalNode_int(*_args)
            
            import Physical
            if isinstance(_args[0], Physical.Physical):
                return self._PhysicalNode__overloaded_removePhysical_ptrPhysicalNode_ptrPhysical(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <Physical.Physical> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


