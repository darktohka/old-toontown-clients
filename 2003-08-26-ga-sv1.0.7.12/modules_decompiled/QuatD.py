# File: Q (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4D

class QuatD(VBase4D.VBase4D, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _QuatD__overloaded_constructor(self):
        self.this = libpanda._inPUZN3qOX4()
        self.userManagesMemory = 1

    
    def _QuatD__overloaded_constructor_ptrConstLVecBase4d(self, copy):
        self.this = libpanda._inPUZN3xmdo(copy.this)
        self.userManagesMemory = 1

    
    def _QuatD__overloaded_constructor_double_double_double_double(self, parameter0, parameter1, parameter2, parameter3):
        self.this = libpanda._inPUZN35Z6w(parameter0, parameter1, parameter2, parameter3)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3jQ0F:
            libpanda._inPUZN3jQ0F(self.this)
        

    
    def pureImaginary(parameter0):
        returnValue = libpanda._inPUZN3OPmP(parameter0.this)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    pureImaginary = staticmethod(pureImaginary)
    
    def identQuat():
        returnValue = libpanda._inPUZN3maTM()
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identQuat = staticmethod(identQuat)
    
    def getClassType():
        returnValue = libpanda._inPUZN3nxRY()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def xform(self, v):
        returnValue = libpanda._inPUZN3PTTe(self.this, v.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, rhs):
        returnValue = libpanda._inPUZN3GGsA(self.this, rhs.this)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __sub__(self):
        returnValue = libpanda._inPUZN3W_Xk(self.this)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded___mul___ptrLQuaterniond_ptrConstLMatrix3d(self, parameter1):
        returnValue = libpanda._inPUZN3BNgV(self.this, parameter1.this)
        import Mat3D
        returnObject = Mat3D.Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded___mul___ptrLQuaterniond_ptrConstLMatrix4d(self, parameter1):
        returnValue = libpanda._inPUZN39NQ3(self.this, parameter1.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _QuatD__overloaded___mul___ptrConstLQuaterniond_ptrConstLQuaterniond(self, parameter1):
        returnValue = libpanda._inPUZN3qQ0o(self.this, parameter1.this)
        returnObject = QuatD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __imul__(self, parameter1):
        returnValue = libpanda._inPUZN36vdR(self.this, parameter1.this)
        return self

    
    def _QuatD__overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond(self, parameter1):
        returnValue = libpanda._inPUZN3vATv(self.this, parameter1.this)
        return returnValue

    
    def _QuatD__overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond_double(self, parameter1, parameter2):
        returnValue = libpanda._inPUZN3LRVo(self.this, parameter1.this, parameter2)
        return returnValue

    
    def output(self, parameter1):
        returnValue = libpanda._inPUZN3cZ7K(self.this, parameter1.this)
        return returnValue

    
    def _QuatD__overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix3d(self, m):
        returnValue = libpanda._inPUZN3XLcn(self.this, m.this)
        return returnValue

    
    def _QuatD__overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix4d(self, m):
        returnValue = libpanda._inPUZN3P6nn(self.this, m.this)
        return returnValue

    
    def _QuatD__overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix3d(self, m):
        returnValue = libpanda._inPUZN3ea4e(self.this, m.this)
        return returnValue

    
    def _QuatD__overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix4d(self, m):
        returnValue = libpanda._inPUZN32bYi(self.this, m.this)
        return returnValue

    
    def setHpr(self, hpr):
        returnValue = libpanda._inPUZN3hFnX(self.this, hpr.this)
        return returnValue

    
    def getHpr(self):
        returnValue = libpanda._inPUZN3xRIv(self.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getAxis(self):
        returnValue = libpanda._inPUZN3Y4Rc(self.this)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getAngle(self):
        returnValue = libpanda._inPUZN3e8Rb(self.this)
        return returnValue

    
    def getR(self):
        returnValue = libpanda._inPUZN3kYi_(self.this)
        return returnValue

    
    def getI(self):
        returnValue = libpanda._inPUZN3jVi_(self.this)
        return returnValue

    
    def getJ(self):
        returnValue = libpanda._inPUZN31WiG(self.this)
        return returnValue

    
    def getK(self):
        returnValue = libpanda._inPUZN3HQiN(self.this)
        return returnValue

    
    def setR(self, r):
        returnValue = libpanda._inPUZN32srU(self.this, r)
        return returnValue

    
    def setI(self, i):
        returnValue = libpanda._inPUZN33hrV(self.this, i)
        return returnValue

    
    def setJ(self, j):
        returnValue = libpanda._inPUZN35irc(self.this, j)
        return returnValue

    
    def setK(self, k):
        returnValue = libpanda._inPUZN3Ijrj(self.this, k)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPUZN3aleL(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPUZN3LgEt(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPUZN3u3zo(self.this)
        return returnValue

    
    def isIdentity(self):
        returnValue = libpanda._inPUZN3JIif(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._QuatD__overloaded_constructor()
        elif numArgs == 1:
            import VBase4D
            if isinstance(_args[0], VBase4D.VBase4D):
                return self._QuatD__overloaded_constructor_ptrConstLVecBase4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4D.VBase4D> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._QuatD__overloaded_constructor_double_double_double_double(_args[0], _args[1], _args[2], _args[3])
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
            if isinstance(_args[0], QuatD):
                return self._QuatD__overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <QuatD> '
        elif numArgs == 2:
            if isinstance(_args[0], QuatD):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._QuatD__overloaded_almostEqual_ptrConstLQuaterniond_ptrConstLQuaterniond_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <QuatD> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def extractToMatrix(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4D
            import Mat3D
            if isinstance(_args[0], Mat4D.Mat4D):
                return self._QuatD__overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix4d(_args[0])
            elif isinstance(_args[0], Mat3D.Mat3D):
                return self._QuatD__overloaded_extractToMatrix_ptrConstLQuaterniond_ptrLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat3D.Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4D
            import Mat3D
            if isinstance(_args[0], QuatD):
                return self._QuatD__overloaded___mul___ptrConstLQuaterniond_ptrConstLQuaterniond(_args[0])
            elif isinstance(_args[0], Mat4D.Mat4D):
                return self._QuatD__overloaded___mul___ptrLQuaterniond_ptrConstLMatrix4d(_args[0])
            elif isinstance(_args[0], Mat3D.Mat3D):
                return self._QuatD__overloaded___mul___ptrLQuaterniond_ptrConstLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <QuatD> <Mat4D.Mat4D> <Mat3D.Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def setFromMatrix(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4D
            import Mat3D
            if isinstance(_args[0], Mat4D.Mat4D):
                return self._QuatD__overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix4d(_args[0])
            elif isinstance(_args[0], Mat3D.Mat3D):
                return self._QuatD__overloaded_setFromMatrix_ptrLQuaterniond_ptrConstLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat3D.Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


