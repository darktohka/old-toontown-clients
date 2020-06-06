# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LinearRandomForce

class LinearJitterForce(LinearRandomForce.LinearRandomForce, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LinearJitterForce__overloaded_constructor_ptrConstLinearJitterForce(self, copy):
        self.this = libpandaphysics._inP9fJJXcP8(copy.this)
        self.userManagesMemory = 1

    
    def _LinearJitterForce__overloaded_constructor_float_bool(self, a, m):
        self.this = libpandaphysics._inP9fJJ0EEl(a, m)
        self.userManagesMemory = 1

    
    def _LinearJitterForce__overloaded_constructor_float(self, a):
        self.this = libpandaphysics._inP9fJJkctU(a)
        self.userManagesMemory = 1

    
    def _LinearJitterForce__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJE51r()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJDAAU()
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
            return self._LinearJitterForce__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._LinearJitterForce__overloaded_constructor_float(*_args)
            
            if isinstance(_args[0], LinearJitterForce):
                return self._LinearJitterForce__overloaded_constructor_ptrConstLinearJitterForce(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <LinearJitterForce> '
        elif numArgs == 2:
            return self._LinearJitterForce__overloaded_constructor_float_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


