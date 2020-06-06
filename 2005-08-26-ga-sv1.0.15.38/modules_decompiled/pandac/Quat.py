# File: Q (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import VBase4

class Quat(VBase4.VBase4, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Quat__overloaded_constructor(self):
        self.this = libpanda._inPVZN3rtd_()
        self.userManagesMemory = 1

    
    def _Quat__overloaded_constructor_ptrConstLVecBase4f(self, copy):
        self.this = libpanda._inPVZN3vDxK(copy.this)
        self.userManagesMemory = 1

    
    def _Quat__overloaded_constructor_float_float_float_float(self, parameter0, parameter1, parameter2, parameter3):
        self.this = libpanda._inPVZN3zNTV(parameter0, parameter1, parameter2, parameter3)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3jcwx:
            libpanda._inPVZN3jcwx(self.this)
        

    
    def pureImaginary(parameter0):
        returnValue = libpanda._inPVZN3Qoeb(parameter0.this)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    pureImaginary = staticmethod(pureImaginary)
    
    def identQuat():
        returnValue = libpanda._inPVZN3mmMR()
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identQuat = staticmethod(identQuat)
    
    def getClassType():
        returnValue = libpanda._inPVZN3ndKd()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def xform(self, v):
        returnValue = libpanda._inPVZN3rkOj(self.this, v.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, rhs):
        returnValue = libpanda._inPVZN3eJuF(self.this, rhs.this)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded___sub___ptrConstLQuaternionf(self):
        returnValue = libpanda._inPVZN3XaQp(self.this)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded___sub___ptrConstLQuaternionf_ptrConstLQuaternionf(self, other):
        returnValue = libpanda._inPVZN3b27z(self.this, other.this)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPVZN3I56X(self.this, other.this)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def angleRad(self, other):
        returnValue = libpanda._inPVZN33Uhy(self.this, other.this)
        return returnValue

    
    def angleDeg(self, other):
        returnValue = libpanda._inPVZN3mSn_(self.this, other.this)
        return returnValue

    
    def _Quat__overloaded___mul___ptrLQuaternionf_ptrConstLMatrix3f(self, parameter1):
        returnValue = libpanda._inPVZN3j8YK(self.this, parameter1.this)
        import Mat3
        returnObject = Mat3.Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded___mul___ptrLQuaternionf_ptrConstLMatrix4f(self, parameter1):
        returnValue = libpanda._inPVZN3e9Is(self.this, parameter1.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded___mul___ptrConstLQuaternionf_ptrConstLQuaternionf(self, parameter1):
        returnValue = libpanda._inPVZN3U_6J(self.this, parameter1.this)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded___mul___ptrConstLQuaternionf_float(self, scalar):
        returnValue = libpanda._inPVZN3ppqj(self.this, scalar)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3e9qp(self.this, scalar)
        returnObject = Quat(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __imul__(self, parameter1):
        returnValue = libpanda._inPVZN3MJVd(self.this, parameter1.this)
        return self

    
    def _Quat__overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf(self, other):
        returnValue = libpanda._inPVZN3rHMU(self.this, other.this)
        return returnValue

    
    def _Quat__overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf_float(self, other, threshold):
        returnValue = libpanda._inPVZN3lDKH(self.this, other.this, threshold)
        return returnValue

    
    def isSameDirection(self, other):
        returnValue = libpanda._inPVZN3i2zi(self.this, other.this)
        return returnValue

    
    def almostSameDirection(self, other, threshold):
        returnValue = libpanda._inPVZN3gEa5(self.this, other.this, threshold)
        return returnValue

    
    def output(self, parameter1):
        returnValue = libpanda._inPVZN3clzP(self.this, parameter1.this)
        return returnValue

    
    def _Quat__overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix3f(self, m):
        returnValue = libpanda._inPVZN3QnH2(self.this, m.this)
        return returnValue

    
    def _Quat__overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix4f(self, m):
        returnValue = libpanda._inPVZN3IWR2(self.this, m.this)
        return returnValue

    
    def _Quat__overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix3f(self, m):
        returnValue = libpanda._inPVZN3adwD(self.this, m.this)
        return returnValue

    
    def _Quat__overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix4f(self, m):
        returnValue = libpanda._inPVZN31eQH(self.this, m.this)
        return returnValue

    
    def setHpr(self, hpr):
        returnValue = libpanda._inPVZN3ghkq(self.this, hpr.this)
        return returnValue

    
    def getHpr(self):
        returnValue = libpanda._inPVZN3O1A0(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getAxis(self):
        returnValue = libpanda._inPVZN3YcKh(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getAngle(self):
        returnValue = libpanda._inPVZN3eAIg(self.this)
        return returnValue

    
    def _Quat__overloaded_getUp_ptrConstLQuaternionf___enum__CoordinateSystem(self, cs):
        returnValue = libpanda._inPVZN33KoZ(self.this, cs)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded_getUp_ptrConstLQuaternionf(self):
        returnValue = libpanda._inPVZN3rwSS(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded_getRight_ptrConstLQuaternionf___enum__CoordinateSystem(self, cs):
        returnValue = libpanda._inPVZN3Mxzz(self.this, cs)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded_getRight_ptrConstLQuaternionf(self):
        returnValue = libpanda._inPVZN386me(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded_getForward_ptrConstLQuaternionf___enum__CoordinateSystem(self, cs):
        returnValue = libpanda._inPVZN36X_p(self.this, cs)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Quat__overloaded_getForward_ptrConstLQuaternionf(self):
        returnValue = libpanda._inPVZN3IjTb(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getR(self):
        returnValue = libpanda._inPVZN3k8aD(self.this)
        return returnValue

    
    def getI(self):
        returnValue = libpanda._inPVZN3jxaE(self.this)
        return returnValue

    
    def getJ(self):
        returnValue = libpanda._inPVZN31yaL(self.this)
        return returnValue

    
    def getK(self):
        returnValue = libpanda._inPVZN3H0aS(self.this)
        return returnValue

    
    def setR(self, r):
        returnValue = libpanda._inPVZN33PLX(self.this, r)
        return returnValue

    
    def setI(self, i):
        returnValue = libpanda._inPVZN304KY(self.this, i)
        return returnValue

    
    def setJ(self, j):
        returnValue = libpanda._inPVZN3m5Kf(self.this, j)
        return returnValue

    
    def setK(self, k):
        returnValue = libpanda._inPVZN3YGLm(self.this, k)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPVZN3aBWQ(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPVZN3ed84(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPVZN3vLqt(self.this)
        return returnValue

    
    def isIdentity(self):
        returnValue = libpanda._inPVZN3Jkak(self.this)
        return returnValue

    
    def isAlmostIdentity(self, tolerance):
        returnValue = libpanda._inPVZN34P4N(self.this, tolerance)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Quat__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._Quat__overloaded_constructor_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._Quat__overloaded_constructor_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 4 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Quat__overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf(*_args)
        elif numArgs == 2:
            return self._Quat__overloaded_almostEqual_ptrConstLQuaternionf_ptrConstLQuaternionf_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Quat__overloaded___mul___ptrConstLQuaternionf_float(*_args)
            
            if isinstance(_args[0], Quat):
                return self._Quat__overloaded___mul___ptrConstLQuaternionf_ptrConstLQuaternionf(*_args)
            
            import Mat4
            if isinstance(_args[0], Mat4.Mat4):
                return self._Quat__overloaded___mul___ptrLQuaternionf_ptrConstLMatrix4f(*_args)
            
            import Mat3
            if isinstance(_args[0], Mat3.Mat3):
                return self._Quat__overloaded___mul___ptrLQuaternionf_ptrConstLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Quat> <Mat4.Mat4> <Mat3.Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def getForward(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Quat__overloaded_getForward_ptrConstLQuaternionf(*_args)
        elif numArgs == 1:
            return self._Quat__overloaded_getForward_ptrConstLQuaternionf___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Quat__overloaded___sub___ptrConstLQuaternionf(*_args)
        elif numArgs == 1:
            return self._Quat__overloaded___sub___ptrConstLQuaternionf_ptrConstLQuaternionf(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getRight(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Quat__overloaded_getRight_ptrConstLQuaternionf(*_args)
        elif numArgs == 1:
            return self._Quat__overloaded_getRight_ptrConstLQuaternionf___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def extractToMatrix(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4
            if isinstance(_args[0], Mat4.Mat4):
                return self._Quat__overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix4f(*_args)
            
            import Mat3
            if isinstance(_args[0], Mat3.Mat3):
                return self._Quat__overloaded_extractToMatrix_ptrConstLQuaternionf_ptrLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4.Mat4> <Mat3.Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setFromMatrix(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4
            if isinstance(_args[0], Mat4.Mat4):
                return self._Quat__overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix4f(*_args)
            
            import Mat3
            if isinstance(_args[0], Mat3.Mat3):
                return self._Quat__overloaded_setFromMatrix_ptrLQuaternionf_ptrConstLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4.Mat4> <Mat3.Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def getUp(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Quat__overloaded_getUp_ptrConstLQuaternionf(*_args)
        elif numArgs == 1:
            return self._Quat__overloaded_getUp_ptrConstLQuaternionf___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


