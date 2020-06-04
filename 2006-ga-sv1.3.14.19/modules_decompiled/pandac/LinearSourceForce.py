# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LinearDistanceForce

class LinearSourceForce(LinearDistanceForce.LinearDistanceForce, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LinearSourceForce__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJ76nW()
        self.userManagesMemory = 1

    
    def _LinearSourceForce__overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float_float_bool(self, p, f, r, a, mass):
        self.this = libpandaphysics._inP9fJJSjwD(p.this, f, r, a, mass)
        self.userManagesMemory = 1

    
    def _LinearSourceForce__overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float_float(self, p, f, r, a):
        self.this = libpandaphysics._inP9fJJMEul(p.this, f, r, a)
        self.userManagesMemory = 1

    
    def _LinearSourceForce__overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float(self, p, f, r):
        self.this = libpandaphysics._inP9fJJmKnZ(p.this, f, r)
        self.userManagesMemory = 1

    
    def _LinearSourceForce__overloaded_constructor_ptrConstLinearSourceForce(self, copy):
        self.this = libpandaphysics._inP9fJJmBjF(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJQ1Mb()
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
            return self._LinearSourceForce__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._LinearSourceForce__overloaded_constructor_ptrConstLinearSourceForce(*_args)
        elif numArgs == 3:
            return self._LinearSourceForce__overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float(*_args)
        elif numArgs == 4:
            return self._LinearSourceForce__overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float_float(*_args)
        elif numArgs == 5:
            return self._LinearSourceForce__overloaded_constructor_ptrConstLPoint3f___enum__FalloffType_float_float_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 4 5 '


