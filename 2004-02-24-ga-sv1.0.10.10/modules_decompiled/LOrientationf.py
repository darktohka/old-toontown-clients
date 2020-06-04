# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Quat

class LOrientationf(Quat.Quat, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _LOrientationf__overloaded_constructor(self):
        self.this = libpanda._inPUZN3dX4n()
        self.userManagesMemory = 1

    
    def _LOrientationf__overloaded_constructor_ptrConstLMatrix3f(self, parameter0):
        self.this = libpanda._inPUZN3lodg(parameter0.this)
        self.userManagesMemory = 1

    
    def _LOrientationf__overloaded_constructor_ptrConstLMatrix4f(self, parameter0):
        self.this = libpanda._inPUZN3ioku(parameter0.this)
        self.userManagesMemory = 1

    
    def _LOrientationf__overloaded_constructor_ptrConstLQuaternionf(self, parameter0):
        self.this = libpanda._inPUZN3_eNF(parameter0.this)
        self.userManagesMemory = 1

    
    def _LOrientationf__overloaded_constructor_ptrConstLVector3f_float(self, parameter0, parameter1):
        self.this = libpanda._inPUZN3Ps13(parameter0.this, parameter1)
        self.userManagesMemory = 1

    
    def _LOrientationf__overloaded_constructor_float_float_float_float(self, parameter0, parameter1, parameter2, parameter3):
        self.this = libpanda._inPUZN3WFbK(parameter0, parameter1, parameter2, parameter3)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3R4Y_:
            libpanda._inPUZN3R4Y_(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPUZN3yKEa()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _LOrientationf__overloaded___mul___ptrConstLOrientationf_ptrConstLOrientationf(self, other):
        returnValue = libpanda._inPUZN3Nm99(self.this, other.this)
        returnObject = LOrientationf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _LOrientationf__overloaded___mul___ptrConstLOrientationf_ptrConstLQuaternionf(self, other):
        returnValue = libpanda._inPUZN30nPz(self.this, other.this)
        returnObject = LOrientationf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LOrientationf__overloaded_constructor()
        elif numArgs == 1:
            import Quat
            import Mat4
            import Mat3
            if isinstance(_args[0], Quat.Quat):
                return self._LOrientationf__overloaded_constructor_ptrConstLQuaternionf(_args[0])
            elif isinstance(_args[0], Mat4.Mat4):
                return self._LOrientationf__overloaded_constructor_ptrConstLMatrix4f(_args[0])
            elif isinstance(_args[0], Mat3.Mat3):
                return self._LOrientationf__overloaded_constructor_ptrConstLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Quat.Quat> <Mat4.Mat4> <Mat3.Mat3> '
        elif numArgs == 2:
            import Vec3
            if isinstance(_args[0], Vec3.Vec3):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._LOrientationf__overloaded_constructor_ptrConstLVector3f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Vec3.Vec3> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._LOrientationf__overloaded_constructor_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 4 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Quat
            if isinstance(_args[0], Quat.Quat):
                return self._LOrientationf__overloaded___mul___ptrConstLOrientationf_ptrConstLQuaternionf(_args[0])
            elif isinstance(_args[0], LOrientationf):
                return self._LOrientationf__overloaded___mul___ptrConstLOrientationf_ptrConstLOrientationf(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Quat.Quat> <LOrientationf> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


