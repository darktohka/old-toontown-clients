# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LinearForce

class LinearVectorForce(LinearForce.LinearForce, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LinearVectorForce__overloaded_constructor_ptrConstLVector3f_float_bool(self, vec, a, mass):
        self.this = libpandaphysics._inP9fJJn_HH(vec.this, a, mass)
        self.userManagesMemory = 1

    
    def _LinearVectorForce__overloaded_constructor_ptrConstLVector3f_float(self, vec, a):
        self.this = libpandaphysics._inP9fJJ5pxV(vec.this, a)
        self.userManagesMemory = 1

    
    def _LinearVectorForce__overloaded_constructor_ptrConstLVector3f(self, vec):
        self.this = libpandaphysics._inP9fJJ51f6(vec.this)
        self.userManagesMemory = 1

    
    def _LinearVectorForce__overloaded_constructor_ptrConstLinearVectorForce(self, copy):
        self.this = libpandaphysics._inP9fJJ2TTR(copy.this)
        self.userManagesMemory = 1

    
    def _LinearVectorForce__overloaded_constructor_float_float_float_float_bool(self, x, y, z, a, mass):
        self.this = libpandaphysics._inP9fJJ_9B9(x, y, z, a, mass)
        self.userManagesMemory = 1

    
    def _LinearVectorForce__overloaded_constructor_float_float_float_float(self, x, y, z, a):
        self.this = libpandaphysics._inP9fJJzxk3(x, y, z, a)
        self.userManagesMemory = 1

    
    def _LinearVectorForce__overloaded_constructor_float_float_float(self, x, y, z):
        self.this = libpandaphysics._inP9fJJpPZK(x, y, z)
        self.userManagesMemory = 1

    
    def _LinearVectorForce__overloaded_constructor_float_float(self, x, y):
        self.this = libpandaphysics._inP9fJJf8n5(x, y)
        self.userManagesMemory = 1

    
    def _LinearVectorForce__overloaded_constructor_float(self, x):
        self.this = libpandaphysics._inP9fJJ1Z3E(x)
        self.userManagesMemory = 1

    
    def _LinearVectorForce__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJnFAc()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJlzdJ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _LinearVectorForce__overloaded_setVector_ptrLinearVectorForce_ptrConstLVector3f(self, v):
        returnValue = libpandaphysics._inP9fJJlk_l(self.this, v.this)
        return returnValue

    
    def _LinearVectorForce__overloaded_setVector_ptrLinearVectorForce_float_float_float(self, x, y, z):
        returnValue = libpandaphysics._inP9fJJVGyt(self.this, x, y, z)
        return returnValue

    
    def getLocalVector(self):
        returnValue = libpandaphysics._inP9fJJM4vu(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LinearVectorForce__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._LinearVectorForce__overloaded_constructor_float(*_args)
            
            import Vec3
            if isinstance(_args[0], Vec3.Vec3):
                return self._LinearVectorForce__overloaded_constructor_ptrConstLVector3f(*_args)
            
            if isinstance(_args[0], LinearVectorForce):
                return self._LinearVectorForce__overloaded_constructor_ptrConstLinearVectorForce(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Vec3.Vec3> <LinearVectorForce> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._LinearVectorForce__overloaded_constructor_float_float(*_args)
            
            import Vec3
            if isinstance(_args[0], Vec3.Vec3):
                return self._LinearVectorForce__overloaded_constructor_ptrConstLVector3f_float(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Vec3.Vec3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._LinearVectorForce__overloaded_constructor_float_float_float(*_args)
            
            import Vec3
            if isinstance(_args[0], Vec3.Vec3):
                return self._LinearVectorForce__overloaded_constructor_ptrConstLVector3f_float_bool(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Vec3.Vec3> '
        elif numArgs == 4:
            return self._LinearVectorForce__overloaded_constructor_float_float_float_float(*_args)
        elif numArgs == 5:
            return self._LinearVectorForce__overloaded_constructor_float_float_float_float_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 5 '

    
    def setVector(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._LinearVectorForce__overloaded_setVector_ptrLinearVectorForce_ptrConstLVector3f(*_args)
        elif numArgs == 3:
            return self._LinearVectorForce__overloaded_setVector_ptrLinearVectorForce_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


