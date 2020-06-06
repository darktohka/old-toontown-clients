# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpandaphysics._inP9fJJTNir(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJrhu_()
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
        returnValue = libpandaphysics._inP9fJJHi58(self.this, index)
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
        returnValue = libpandaphysics._inP9fJJnr3_(self.this, physical.this)
        return returnValue

    
    def addPhysicalsFrom(self, other):
        returnValue = libpandaphysics._inP9fJJF36z(self.this, other.this)
        return returnValue

    
    def _PhysicalNode__overloaded_removePhysical_ptrPhysicalNode_ptrPhysical(self, physical):
        returnValue = libpandaphysics._inP9fJJz6iS(self.this, physical.this)
        return returnValue

    
    def _PhysicalNode__overloaded_removePhysical_ptrPhysicalNode_int(self, index):
        returnValue = libpandaphysics._inP9fJJNXfn(self.this, index)
        return returnValue

    
    def removePhysical(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Physical
            if isinstance(_args[0], types.IntType):
                return self._PhysicalNode__overloaded_removePhysical_ptrPhysicalNode_int(_args[0])
            elif isinstance(_args[0], Physical.Physical):
                return self._PhysicalNode__overloaded_removePhysical_ptrPhysicalNode_ptrPhysical(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <Physical.Physical> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


