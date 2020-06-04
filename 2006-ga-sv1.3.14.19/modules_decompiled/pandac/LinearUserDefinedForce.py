# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LinearForce

class LinearUserDefinedForce(LinearForce.LinearForce, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LinearUserDefinedForce__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJosNC()
        self.userManagesMemory = 1

    
    def _LinearUserDefinedForce__overloaded_constructor_ptrConstLinearUserDefinedForce(self, copy):
        self.this = libpandaphysics._inP9fJJOyYN(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJnYsf()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LinearUserDefinedForce__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._LinearUserDefinedForce__overloaded_constructor_ptrConstLinearUserDefinedForce(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


