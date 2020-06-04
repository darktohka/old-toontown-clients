# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import Quat

class LRotationf(Quat.Quat, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LRotationf__overloaded_constructor(self):
        self.this = libpanda._inPVZN31ufs()
        self.userManagesMemory = 1

    
    def _LRotationf__overloaded_constructor_ptrConstLMatrix3f(self, parameter0):
        self.this = libpanda._inPVZN3oHWm(parameter0.this)
        self.userManagesMemory = 1

    
    def _LRotationf__overloaded_constructor_ptrConstLMatrix4f(self, parameter0):
        self.this = libpanda._inPVZN3oMkn(parameter0.this)
        self.userManagesMemory = 1

    
    def _LRotationf__overloaded_constructor_ptrConstLQuaternionf(self, parameter0):
        self.this = libpanda._inPVZN3dC6k(parameter0.this)
        self.userManagesMemory = 1

    
    def _LRotationf__overloaded_constructor_ptrConstLVector3f_float(self, parameter0, parameter1):
        self.this = libpanda._inPVZN3zssT(parameter0.this, parameter1)
        self.userManagesMemory = 1

    
    def _LRotationf__overloaded_constructor_float_float_float(self, parameter0, parameter1, parameter2):
        self.this = libpanda._inPVZN3LwNm(parameter0, parameter1, parameter2)
        self.userManagesMemory = 1

    
    def _LRotationf__overloaded_constructor_float_float_float_float(self, parameter0, parameter1, parameter2, parameter3):
        self.this = libpanda._inPVZN36t_a(parameter0, parameter1, parameter2, parameter3)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3Rd7l:
            libpanda._inPVZN3Rd7l(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPVZN3scCI()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _LRotationf__overloaded___mul___ptrConstLRotationf_ptrConstLQuaternionf(self, other):
        returnValue = libpanda._inPVZN3cT59(self.this, other.this)
        import Quat
        returnObject = Quat.Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _LRotationf__overloaded___mul___ptrConstLRotationf_ptrConstLRotationf(self, other):
        returnValue = libpanda._inPVZN3ttc8(self.this, other.this)
        returnObject = LRotationf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LRotationf__overloaded_constructor(*_args)
        elif numArgs == 1:
            import Quat
            if isinstance(_args[0], Quat.Quat):
                return self._LRotationf__overloaded_constructor_ptrConstLQuaternionf(*_args)
            
            import Mat4
            if isinstance(_args[0], Mat4.Mat4):
                return self._LRotationf__overloaded_constructor_ptrConstLMatrix4f(*_args)
            
            import Mat3
            if isinstance(_args[0], Mat3.Mat3):
                return self._LRotationf__overloaded_constructor_ptrConstLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Quat.Quat> <Mat4.Mat4> <Mat3.Mat3> '
        elif numArgs == 2:
            return self._LRotationf__overloaded_constructor_ptrConstLVector3f_float(*_args)
        elif numArgs == 3:
            return self._LRotationf__overloaded_constructor_float_float_float(*_args)
        elif numArgs == 4:
            return self._LRotationf__overloaded_constructor_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], LRotationf):
                return self._LRotationf__overloaded___mul___ptrConstLRotationf_ptrConstLRotationf(*_args)
            
            import Quat
            if isinstance(_args[0], Quat.Quat):
                return self._LRotationf__overloaded___mul___ptrConstLRotationf_ptrConstLQuaternionf(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <LRotationf> <Quat.Quat> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


