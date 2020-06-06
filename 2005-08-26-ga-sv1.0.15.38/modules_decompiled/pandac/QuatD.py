# File: Q (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import VBase4D

class QuatD(VBase4D.VBase4D, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _QuatD__overloaded_constructor(self):
        self.this = libpanda._inPVZN3rOX4()
        self.userManagesMemory = 1

    
    def _QuatD__overloaded_constructor_ptrConstLVecBase4d(self, copy):
        self.this = libpanda._inPVZN3wmdo(copy.this)
        self.userManagesMemory = 1

    
    def _QuatD__overloaded_constructor_double_double_double_double(self, parameter0, parameter1, parameter2, parameter3):
        self.this = libpanda._inPVZN36Z6w(parameter0, parameter1, parameter2, parameter3)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3jQ0F:
            libpanda._inPVZN3jQ0F(self.this)
        

    
    def pureImaginary(parameter0):
        returnValue = libpanda._inPVZN3OPmP(parameter0.this)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    pureImaginary = staticmethod(pureImaginary)
    
    def identQuat():
        returnValue = libpanda._inPVZN3maTM()
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identQuat = staticmethod(identQuat)
    
    def getClassType():
        returnValue = libpanda._inPVZN3nxRY()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def xform(self, v):
        returnValue = libpanda._inPVZN3PTTe(self.this, v.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, rhs):
        returnValue = libpanda._inPVZN3GGsA(self.this, rhs.this)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded___sub___ptrConstLQuaterniond(self):
        returnValue = libpanda._inPVZN3X_Xk(self.this)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded___sub___ptrConstLQuaterniond_ptrConstLQuaterniond(self, other):
        returnValue = libpanda._inPVZN3Za1S(self.this, other.this)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPVZN3PV02(self.this, other.this)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def angleRad(self, other):
        returnValue = libpanda._inPVZN33sxo(self.this, other.this)
        return returnValue

    
    def angleDeg(self, other):
        returnValue = libpanda._inPVZN3mq30(self.this, other.this)
        return returnValue

    
    def _QuatD__overloaded___mul___ptrLQuaterniond_ptrConstLMatrix3d(self, parameter1):
        returnValue = libpanda._inPVZN3BNgV(self.this, parameter1.this)
        import Mat3D
        returnObject = Mat3D.Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded___mul___ptrLQuaterniond_ptrConstLMatrix4d(self, parameter1):
        returnValue = libpanda._inPVZN38NQ3(self.this, parameter1.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded___mul___ptrConstLQuaterniond_ptrConstLQuaterniond(self, parameter1):
        returnValue = libpanda._inPVZN3rQ0o(self.this, parameter1.this)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded___mul___ptrConstLQuaterniond_double(self, scalar):
        returnValue = libpanda._inPVZN3A0TI(self.this, scalar)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3PASO(self.this, scalar)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __imul__(self, parameter1):
        returnValue = libpanda._inPVZN36vdR(self.this, parameter1.this)
        return self

    
    def _QuatD__overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond(self, other):
        returnValue = libpanda._inPVZN3sATv(self.this, other.this)
        return returnValue

    
    def _QuatD__overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond_double(self, other, threshold):
        returnValue = libpanda._inPVZN3KRVo(self.this, other.this, threshold)
        return returnValue

    
    def isSameDirection(self, other):
        returnValue = libpanda._inPVZN3Zg5d(self.this, other.this)
        return returnValue

    
    def almostSameDirection(self, other, threshold):
        returnValue = libpanda._inPVZN3UNTJ(self.this, other.this, threshold)
        return returnValue

    
    def output(self, parameter1):
        returnValue = libpanda._inPVZN3cZ7K(self.this, parameter1.this)
        return returnValue

    
    def _QuatD__overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix3d(self, m):
        returnValue = libpanda._inPVZN3QLcn(self.this, m.this)
        return returnValue

    
    def _QuatD__overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix4d(self, m):
        returnValue = libpanda._inPVZN3I6nn(self.this, m.this)
        return returnValue

    
    def _QuatD__overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix3d(self, m):
        returnValue = libpanda._inPVZN3ea4e(self.this, m.this)
        return returnValue

    
    def _QuatD__overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix4d(self, m):
        returnValue = libpanda._inPVZN35bYi(self.this, m.this)
        return returnValue

    
    def setHpr(self, hpr):
        returnValue = libpanda._inPVZN3hFnX(self.this, hpr.this)
        return returnValue

    
    def getHpr(self):
        returnValue = libpanda._inPVZN3ORIv(self.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getAxis(self):
        returnValue = libpanda._inPVZN3Y4Rc(self.this)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getAngle(self):
        returnValue = libpanda._inPVZN3e8Rb(self.this)
        return returnValue

    
    def _QuatD__overloaded_getUp_ptrConstLQuaterniond___enum__CoordinateSystem(self, cs):
        returnValue = libpanda._inPVZN33uwU(self.this, cs)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded_getUp_ptrConstLQuaterniond(self):
        returnValue = libpanda._inPVZN3rsaN(self.this)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded_getRight_ptrConstLQuaterniond___enum__CoordinateSystem(self, cs):
        returnValue = libpanda._inPVZN3Mt7u(self.this, cs)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded_getRight_ptrConstLQuaterniond(self):
        returnValue = libpanda._inPVZN38etZ(self.this)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded_getForward_ptrConstLQuaterniond___enum__CoordinateSystem(self, cs):
        returnValue = libpanda._inPVZN36zHl(self.this, cs)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded_getForward_ptrConstLQuaterniond(self):
        returnValue = libpanda._inPVZN3IPaW(self.this)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getR(self):
        returnValue = libpanda._inPVZN3lYi_(self.this)
        return returnValue

    
    def getI(self):
        returnValue = libpanda._inPVZN3kVi_(self.this)
        return returnValue

    
    def getJ(self):
        returnValue = libpanda._inPVZN31WiG(self.this)
        return returnValue

    
    def getK(self):
        returnValue = libpanda._inPVZN3HQiN(self.this)
        return returnValue

    
    def setR(self, r):
        returnValue = libpanda._inPVZN32srU(self.this, r)
        return returnValue

    
    def setI(self, i):
        returnValue = libpanda._inPVZN33hrV(self.this, i)
        return returnValue

    
    def setJ(self, j):
        returnValue = libpanda._inPVZN35irc(self.this, j)
        return returnValue

    
    def setK(self, k):
        returnValue = libpanda._inPVZN3Ljrj(self.this, k)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPVZN3aleL(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPVZN3IgEt(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPVZN3v3zo(self.this)
        return returnValue

    
    def isIdentity(self):
        returnValue = libpanda._inPVZN3JIif(self.this)
        return returnValue

    
    def isAlmostIdentity(self, tolerance):
        returnValue = libpanda._inPVZN3Z4KV(self.this, tolerance)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._QuatD__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._QuatD__overloaded_constructor_ptrConstLVecBase4d(*_args)
        elif numArgs == 4:
            return self._QuatD__overloaded_constructor_double_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 4 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._QuatD__overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond(*_args)
        elif numArgs == 2:
            return self._QuatD__overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._QuatD__overloaded___mul___ptrConstLQuaterniond_double(*_args)
            
            if isinstance(_args[0], QuatD):
                return self._QuatD__overloaded___mul___ptrConstLQuaterniond_ptrConstLQuaterniond(*_args)
            
            import Mat4D
            if isinstance(_args[0], Mat4D.Mat4D):
                return self._QuatD__overloaded___mul___ptrLQuaterniond_ptrConstLMatrix4d(*_args)
            
            import Mat3D
            if isinstance(_args[0], Mat3D.Mat3D):
                return self._QuatD__overloaded___mul___ptrLQuaterniond_ptrConstLMatrix3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <QuatD> <Mat4D.Mat4D> <Mat3D.Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def getForward(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._QuatD__overloaded_getForward_ptrConstLQuaterniond(*_args)
        elif numArgs == 1:
            return self._QuatD__overloaded_getForward_ptrConstLQuaterniond___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._QuatD__overloaded___sub___ptrConstLQuaterniond(*_args)
        elif numArgs == 1:
            return self._QuatD__overloaded___sub___ptrConstLQuaterniond_ptrConstLQuaterniond(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getRight(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._QuatD__overloaded_getRight_ptrConstLQuaterniond(*_args)
        elif numArgs == 1:
            return self._QuatD__overloaded_getRight_ptrConstLQuaterniond___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def extractToMatrix(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4D
            if isinstance(_args[0], Mat4D.Mat4D):
                return self._QuatD__overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix4d(*_args)
            
            import Mat3D
            if isinstance(_args[0], Mat3D.Mat3D):
                return self._QuatD__overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat3D.Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setFromMatrix(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4D
            if isinstance(_args[0], Mat4D.Mat4D):
                return self._QuatD__overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix4d(*_args)
            
            import Mat3D
            if isinstance(_args[0], Mat3D.Mat3D):
                return self._QuatD__overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat3D.Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def getUp(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._QuatD__overloaded_getUp_ptrConstLQuaterniond(*_args)
        elif numArgs == 1:
            return self._QuatD__overloaded_getUp_ptrConstLQuaterniond___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


