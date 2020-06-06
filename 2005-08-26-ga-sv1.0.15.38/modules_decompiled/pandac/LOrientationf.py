# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import Quat

class LOrientationf(Quat.Quat, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LOrientationf__overloaded_constructor(self):
        self.this = libpanda._inPVZN3cX4n()
        self.userManagesMemory = 1

    
    def _LOrientationf__overloaded_constructor_ptrConstLMatrix3f(self, parameter0):
        self.this = libpanda._inPVZN3kodg(parameter0.this)
        self.userManagesMemory = 1

    
    def _LOrientationf__overloaded_constructor_ptrConstLMatrix4f(self, parameter0):
        self.this = libpanda._inPVZN3loku(parameter0.this)
        self.userManagesMemory = 1

    
    def _LOrientationf__overloaded_constructor_ptrConstLQuaternionf(self, parameter0):
        self.this = libpanda._inPVZN3_eNF(parameter0.this)
        self.userManagesMemory = 1

    
    def _LOrientationf__overloaded_constructor_ptrConstLVector3f_float(self, parameter0, parameter1):
        self.this = libpanda._inPVZN3Os13(parameter0.this, parameter1)
        self.userManagesMemory = 1

    
    def _LOrientationf__overloaded_constructor_float_float_float_float(self, parameter0, parameter1, parameter2, parameter3):
        self.this = libpanda._inPVZN3WFbK(parameter0, parameter1, parameter2, parameter3)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3u4Y_:
            libpanda._inPVZN3u4Y_(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPVZN3yKEa()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _LOrientationf__overloaded___mul___ptrConstLOrientationf_ptrConstLQuaternionf(self, other):
        returnValue = libpanda._inPVZN31nPz(self.this, other.this)
        returnObject = LOrientationf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _LOrientationf__overloaded___mul___ptrConstLOrientationf_ptrConstLRotationf(self, other):
        returnValue = libpanda._inPVZN3yr_X(self.this, other.this)
        returnObject = LOrientationf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LOrientationf__overloaded_constructor(*_args)
        elif numArgs == 1:
            import Quat
            if isinstance(_args[0], Quat.Quat):
                return self._LOrientationf__overloaded_constructor_ptrConstLQuaternionf(*_args)
            
            import Mat4
            if isinstance(_args[0], Mat4.Mat4):
                return self._LOrientationf__overloaded_constructor_ptrConstLMatrix4f(*_args)
            
            import Mat3
            if isinstance(_args[0], Mat3.Mat3):
                return self._LOrientationf__overloaded_constructor_ptrConstLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Quat.Quat> <Mat4.Mat4> <Mat3.Mat3> '
        elif numArgs == 2:
            return self._LOrientationf__overloaded_constructor_ptrConstLVector3f_float(*_args)
        elif numArgs == 4:
            return self._LOrientationf__overloaded_constructor_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 4 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import LRotationf
            if isinstance(_args[0], LRotationf.LRotationf):
                return self._LOrientationf__overloaded___mul___ptrConstLOrientationf_ptrConstLRotationf(*_args)
            
            import Quat
            if isinstance(_args[0], Quat.Quat):
                return self._LOrientationf__overloaded___mul___ptrConstLOrientationf_ptrConstLQuaternionf(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <LRotationf.LRotationf> <Quat.Quat> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


