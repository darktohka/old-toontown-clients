# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import QuatD

class LRotationd(QuatD.QuatD, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _LRotationd__overloaded_constructor(self):
        self.this = libpanda._inPUZN3UT9o()
        self.userManagesMemory = 1

    
    def _LRotationd__overloaded_constructor_ptrConstLMatrix3d(self, parameter0):
        self.this = libpanda._inPUZN31jtU(parameter0.this)
        self.userManagesMemory = 1

    
    def _LRotationd__overloaded_constructor_ptrConstLMatrix4d(self, parameter0):
        self.this = libpanda._inPUZN31o7V(parameter0.this)
        self.userManagesMemory = 1

    
    def _LRotationd__overloaded_constructor_ptrConstLQuaterniond(self, parameter0):
        self.this = libpanda._inPUZN361Oh(parameter0.this)
        self.userManagesMemory = 1

    
    def _LRotationd__overloaded_constructor_ptrConstLVector3d_double(self, parameter0, parameter1):
        self.this = libpanda._inPUZN3Idpy(parameter0.this, parameter1)
        self.userManagesMemory = 1

    
    def _LRotationd__overloaded_constructor_double_double_double(self, parameter0, parameter1, parameter2):
        self.this = libpanda._inPUZN35Iug(parameter0, parameter1, parameter2)
        self.userManagesMemory = 1

    
    def _LRotationd__overloaded_constructor_double_double_double_double(self, parameter0, parameter1, parameter2, parameter3):
        self.this = libpanda._inPUZN3B9cz(parameter0, parameter1, parameter2, parameter3)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN38CDF:
            libpanda._inPUZN38CDF(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPUZN3KPCY()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _LRotationd__overloaded___mul___ptrConstLRotationd_ptrConstLQuaterniond(self, other):
        returnValue = libpanda._inPUZN3ukuN(self.this, other.this)
        import QuatD
        returnObject = QuatD.QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _LRotationd__overloaded___mul___ptrConstLRotationd_ptrConstLRotationd(self, other):
        returnValue = libpanda._inPUZN31Z8I(self.this, other.this)
        returnObject = LRotationd(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LRotationd__overloaded_constructor()
        elif numArgs == 1:
            import QuatD
            import Mat4D
            import Mat3D
            if isinstance(_args[0], QuatD.QuatD):
                return self._LRotationd__overloaded_constructor_ptrConstLQuaterniond(_args[0])
            elif isinstance(_args[0], Mat4D.Mat4D):
                return self._LRotationd__overloaded_constructor_ptrConstLMatrix4d(_args[0])
            elif isinstance(_args[0], Mat3D.Mat3D):
                return self._LRotationd__overloaded_constructor_ptrConstLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Mat4D.Mat4D> <Mat3D.Mat3D> '
        elif numArgs == 2:
            import Vec3D
            if isinstance(_args[0], Vec3D.Vec3D):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._LRotationd__overloaded_constructor_ptrConstLVector3d_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Vec3D.Vec3D> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._LRotationd__overloaded_constructor_double_double_double(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._LRotationd__overloaded_constructor_double_double_double_double(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import QuatD
            if isinstance(_args[0], QuatD.QuatD):
                return self._LRotationd__overloaded___mul___ptrConstLRotationd_ptrConstLQuaterniond(_args[0])
            elif isinstance(_args[0], LRotationd):
                return self._LRotationd__overloaded___mul___ptrConstLRotationd_ptrConstLRotationd(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <LRotationd> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


