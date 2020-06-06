# File: A (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import AngularForce

class AngularVectorForce(AngularForce.AngularForce, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _AngularVectorForce__overloaded_constructor_ptrConstAngularVectorForce(self, copy):
        self.this = libpandaphysics._inP9fJJaKTX(copy.this)
        self.userManagesMemory = 1

    
    def _AngularVectorForce__overloaded_constructor_ptrConstLVector3f(self, vec):
        self.this = libpandaphysics._inP9fJJesiq(vec.this)
        self.userManagesMemory = 1

    
    def _AngularVectorForce__overloaded_constructor_float_float_float(self, x, y, z):
        self.this = libpandaphysics._inP9fJJW9fj(x, y, z)
        self.userManagesMemory = 1

    
    def _AngularVectorForce__overloaded_constructor_float_float(self, x, y):
        self.this = libpandaphysics._inP9fJJoL6s(x, y)
        self.userManagesMemory = 1

    
    def _AngularVectorForce__overloaded_constructor_float(self, x):
        self.this = libpandaphysics._inP9fJJBigk(x)
        self.userManagesMemory = 1

    
    def _AngularVectorForce__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJ_SEb()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJu8B7()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _AngularVectorForce__overloaded_setVector_ptrAngularVectorForce_ptrConstLVector3f(self, v):
        returnValue = libpandaphysics._inP9fJJJPXM(self.this, v.this)
        return returnValue

    
    def _AngularVectorForce__overloaded_setVector_ptrAngularVectorForce_float_float_float(self, x, y, z):
        returnValue = libpandaphysics._inP9fJJOCkG(self.this, x, y, z)
        return returnValue

    
    def getLocalVector(self):
        returnValue = libpandaphysics._inP9fJJl4vl(self.this)
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
            return self._AngularVectorForce__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._AngularVectorForce__overloaded_constructor_float(*_args)
            
            import Vec3
            if isinstance(_args[0], Vec3.Vec3):
                return self._AngularVectorForce__overloaded_constructor_ptrConstLVector3f(*_args)
            
            if isinstance(_args[0], AngularVectorForce):
                return self._AngularVectorForce__overloaded_constructor_ptrConstAngularVectorForce(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Vec3.Vec3> <AngularVectorForce> '
        elif numArgs == 2:
            return self._AngularVectorForce__overloaded_constructor_float_float(*_args)
        elif numArgs == 3:
            return self._AngularVectorForce__overloaded_constructor_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '

    
    def setVector(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._AngularVectorForce__overloaded_setVector_ptrAngularVectorForce_ptrConstLVector3f(*_args)
        elif numArgs == 3:
            return self._AngularVectorForce__overloaded_setVector_ptrAngularVectorForce_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


