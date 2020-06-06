# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LinearForce

class LinearFrictionForce(LinearForce.LinearForce, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LinearFrictionForce__overloaded_constructor_ptrConstLinearFrictionForce(self, copy):
        self.this = libpandaphysics._inP9fJJt_V5(copy.this)
        self.userManagesMemory = 1

    
    def _LinearFrictionForce__overloaded_constructor_float_float_bool(self, coef, a, m):
        self.this = libpandaphysics._inP9fJJ1Aho(coef, a, m)
        self.userManagesMemory = 1

    
    def _LinearFrictionForce__overloaded_constructor_float_float(self, coef, a):
        self.this = libpandaphysics._inP9fJJfgK3(coef, a)
        self.userManagesMemory = 1

    
    def _LinearFrictionForce__overloaded_constructor_float(self, coef):
        self.this = libpandaphysics._inP9fJJZk3b(coef)
        self.userManagesMemory = 1

    
    def _LinearFrictionForce__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJvrU5()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJxun1()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCoef(self, coef):
        returnValue = libpandaphysics._inP9fJJ6iox(self.this, coef)
        return returnValue

    
    def getCoef(self):
        returnValue = libpandaphysics._inP9fJJOTwt(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LinearFrictionForce__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._LinearFrictionForce__overloaded_constructor_float(*_args)
            
            if isinstance(_args[0], LinearFrictionForce):
                return self._LinearFrictionForce__overloaded_constructor_ptrConstLinearFrictionForce(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <LinearFrictionForce> '
        elif numArgs == 2:
            return self._LinearFrictionForce__overloaded_constructor_float_float(*_args)
        elif numArgs == 3:
            return self._LinearFrictionForce__overloaded_constructor_float_float_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '


