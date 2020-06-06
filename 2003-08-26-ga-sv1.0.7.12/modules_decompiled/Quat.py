# File: Q (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4

class Quat(VBase4.VBase4, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Quat__overloaded_constructor(self):
        self.this = libpanda._inPUZN3qtd_()
        self.userManagesMemory = 1

    
    def _Quat__overloaded_constructor_ptrConstLVecBase4f(self, copy):
        self.this = libpanda._inPUZN3vDxK(copy.this)
        self.userManagesMemory = 1

    
    def _Quat__overloaded_constructor_float_float_float_float(self, parameter0, parameter1, parameter2, parameter3):
        self.this = libpanda._inPUZN3zNTV(parameter0, parameter1, parameter2, parameter3)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3kcwx:
            libpanda._inPUZN3kcwx(self.this)
        

    
    def pureImaginary(parameter0):
        returnValue = libpanda._inPUZN3Qoeb(parameter0.this)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    pureImaginary = staticmethod(pureImaginary)
    
    def identQuat():
        returnValue = libpanda._inPUZN3mmMR()
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identQuat = staticmethod(identQuat)
    
    def getClassType():
        returnValue = libpanda._inPUZN3ndKd()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def xform(self, v):
        returnValue = libpanda._inPUZN3okOj(self.this, v.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, rhs):
        returnValue = libpanda._inPUZN3eJuF(self.this, rhs.this)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __sub__(self):
        returnValue = libpanda._inPUZN3WaQp(self.this)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded___mul___ptrLQuaternionf_ptrConstLMatrix3f(self, parameter1):
        returnValue = libpanda._inPUZN3j8YK(self.this, parameter1.this)
        import Mat3
        returnObject = Mat3.Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded___mul___ptrLQuaternionf_ptrConstLMatrix4f(self, parameter1):
        returnValue = libpanda._inPUZN3f9Is(self.this, parameter1.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded___mul___ptrConstLQuaternionf_ptrConstLQuaternionf(self, parameter1):
        returnValue = libpanda._inPUZN3U_6J(self.this, parameter1.this)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __imul__(self, parameter1):
        returnValue = libpanda._inPUZN3MJVd(self.this, parameter1.this)
        return self

    
    def _Quat__overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf(self, parameter1):
        returnValue = libpanda._inPUZN3rHMU(self.this, parameter1.this)
        return returnValue

    
    def _Quat__overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf_float(self, parameter1, parameter2):
        returnValue = libpanda._inPUZN3lDKH(self.this, parameter1.this, parameter2)
        return returnValue

    
    def output(self, parameter1):
        returnValue = libpanda._inPUZN3clzP(self.this, parameter1.this)
        return returnValue

    
    def _Quat__overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix3f(self, m):
        returnValue = libpanda._inPUZN3XnH2(self.this, m.this)
        return returnValue

    
    def _Quat__overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix4f(self, m):
        returnValue = libpanda._inPUZN3PWR2(self.this, m.this)
        return returnValue

    
    def _Quat__overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix3f(self, m):
        returnValue = libpanda._inPUZN3adwD(self.this, m.this)
        return returnValue

    
    def _Quat__overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix4f(self, m):
        returnValue = libpanda._inPUZN31eQH(self.this, m.this)
        return returnValue

    
    def setHpr(self, hpr):
        returnValue = libpanda._inPUZN3jhkq(self.this, hpr.this)
        return returnValue

    
    def getHpr(self):
        returnValue = libpanda._inPUZN3x1A0(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getAxis(self):
        returnValue = libpanda._inPUZN3ZcKh(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getAngle(self):
        returnValue = libpanda._inPUZN3dAIg(self.this)
        return returnValue

    
    def getR(self):
        returnValue = libpanda._inPUZN3k8aD(self.this)
        return returnValue

    
    def getI(self):
        returnValue = libpanda._inPUZN3jxaE(self.this)
        return returnValue

    
    def getJ(self):
        returnValue = libpanda._inPUZN31yaL(self.this)
        return returnValue

    
    def getK(self):
        returnValue = libpanda._inPUZN3H0aS(self.this)
        return returnValue

    
    def setR(self, r):
        returnValue = libpanda._inPUZN33PLX(self.this, r)
        return returnValue

    
    def setI(self, i):
        returnValue = libpanda._inPUZN304KY(self.this, i)
        return returnValue

    
    def setJ(self, j):
        returnValue = libpanda._inPUZN3m5Kf(self.this, j)
        return returnValue

    
    def setK(self, k):
        returnValue = libpanda._inPUZN3ZGLm(self.this, k)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPUZN3aBWQ(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPUZN3Zd84(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPUZN3uLqt(self.this)
        return returnValue

    
    def isIdentity(self):
        returnValue = libpanda._inPUZN3Ikak(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Quat__overloaded_constructor()
        elif numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._Quat__overloaded_constructor_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._Quat__overloaded_constructor_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 4 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Quat):
                return self._Quat__overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Quat> '
        elif numArgs == 2:
            if isinstance(_args[0], Quat):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Quat__overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Quat> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def extractToMatrix(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4
            import Mat3
            if isinstance(_args[0], Mat4.Mat4):
                return self._Quat__overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix4f(_args[0])
            elif isinstance(_args[0], Mat3.Mat3):
                return self._Quat__overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4.Mat4> <Mat3.Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4
            import Mat3
            if isinstance(_args[0], Quat):
                return self._Quat__overloaded___mul___ptrConstLQuaternionf_ptrConstLQuaternionf(_args[0])
            elif isinstance(_args[0], Mat4.Mat4):
                return self._Quat__overloaded___mul___ptrLQuaternionf_ptrConstLMatrix4f(_args[0])
            elif isinstance(_args[0], Mat3.Mat3):
                return self._Quat__overloaded___mul___ptrLQuaternionf_ptrConstLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Quat> <Mat4.Mat4> <Mat3.Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setFromMatrix(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4
            import Mat3
            if isinstance(_args[0], Mat4.Mat4):
                return self._Quat__overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix4f(_args[0])
            elif isinstance(_args[0], Mat3.Mat3):
                return self._Quat__overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4.Mat4> <Mat3.Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


