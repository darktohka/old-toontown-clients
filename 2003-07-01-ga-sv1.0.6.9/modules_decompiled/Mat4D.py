# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class Mat4D(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Mat4D__overloaded_constructor(self):
        self.this = libpanda._inPUZN3Urx_()
        self.userManagesMemory = 1

    
    def _Mat4D__overloaded_constructor_ptrConstLMatrix3d(self, upper3):
        self.this = libpanda._inPUZN3RSTZ(upper3.this)
        self.userManagesMemory = 1

    
    def _Mat4D__overloaded_constructor_ptrConstLMatrix3d_ptrConstLVecBase3d(self, upper3, trans):
        self.this = libpanda._inPUZN3y2xB(upper3.this, trans.this)
        self.userManagesMemory = 1

    
    def _Mat4D__overloaded_constructor_ptrConstLMatrix4d(self, other):
        self.this = libpanda._inPUZN3oOT1(other.this)
        self.userManagesMemory = 1

    
    def _Mat4D__overloaded_constructor_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
        self.this = libpanda._inPUZN3LfZS(e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3yVmH:
            libpanda._inPUZN3yVmH(self.this)
        

    
    def identMat():
        returnValue = libpanda._inPUZN3AfTM()
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identMat = staticmethod(identMat)
    
    def _Mat4D__overloaded_translateMat_ptrConstLVecBase3d(trans):
        returnValue = libpanda._inPUZN3SDJX(trans.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_translateMat_ptrConstLVecBase3d = staticmethod(_Mat4D__overloaded_translateMat_ptrConstLVecBase3d)
    
    def _Mat4D__overloaded_translateMat_double_double_double(tx, ty, tz):
        returnValue = libpanda._inPUZN3ufAu(tx, ty, tz)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_translateMat_double_double_double = staticmethod(_Mat4D__overloaded_translateMat_double_double_double)
    
    def _Mat4D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPUZN3blkA(angle, axis.this, cs)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat4D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem)
    
    def _Mat4D__overloaded_rotateMat_double_ptrLVecBase3d(angle, axis):
        returnValue = libpanda._inPUZN3yawN(angle, axis.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_rotateMat_double_ptrLVecBase3d = staticmethod(_Mat4D__overloaded_rotateMat_double_ptrLVecBase3d)
    
    def _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPUZN39B_S(angle, axis.this, cs)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem)
    
    def _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(angle, axis):
        returnValue = libpanda._inPUZN3bFts(angle, axis.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d = staticmethod(_Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d)
    
    def _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem(angle, axis, resultMat, cs):
        returnValue = libpanda._inPUZN365kn(angle, axis.this, resultMat.this, cs)
        return returnValue

    _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem = staticmethod(_Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem)
    
    def _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d(angle, axis, resultMat):
        returnValue = libpanda._inPUZN3u6SM(angle, axis.this, resultMat.this)
        return returnValue

    _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d = staticmethod(_Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d)
    
    def _Mat4D__overloaded_scaleMat_ptrConstLVecBase3d(scale):
        returnValue = libpanda._inPUZN338_F(scale.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_scaleMat_ptrConstLVecBase3d = staticmethod(_Mat4D__overloaded_scaleMat_ptrConstLVecBase3d)
    
    def _Mat4D__overloaded_scaleMat_double(scale):
        returnValue = libpanda._inPUZN3H84Q(scale)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_scaleMat_double = staticmethod(_Mat4D__overloaded_scaleMat_double)
    
    def _Mat4D__overloaded_scaleMat_double_double_double(sx, sy, sz):
        returnValue = libpanda._inPUZN3UzZ0(sx, sy, sz)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_scaleMat_double_double_double = staticmethod(_Mat4D__overloaded_scaleMat_double_double_double)
    
    def yToZUpMat():
        returnValue = libpanda._inPUZN3MIyP()
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    yToZUpMat = staticmethod(yToZUpMat)
    
    def zToYUpMat():
        returnValue = libpanda._inPUZN3MGWN()
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zToYUpMat = staticmethod(zToYUpMat)
    
    def convertMat(_from, to):
        returnValue = libpanda._inPUZN35OYN(_from, to)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    convertMat = staticmethod(convertMat)
    
    def getClassType():
        returnValue = libpanda._inPUZN3m3L3()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Mat4D__overloaded_assign_ptrLMatrix4d_ptrConstLMatrix4d(self, other):
        returnValue = libpanda._inPUZN3OVfu(self.this, other.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat4D__overloaded_assign_ptrLMatrix4d_double(self, fillValue):
        returnValue = libpanda._inPUZN3ASXw(self.this, fillValue)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def fill(self, fillValue):
        returnValue = libpanda._inPUZN3ssm9(self.this, fillValue)
        return returnValue

    
    def set(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
        returnValue = libpanda._inPUZN3F5Uz(self.this, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
        return returnValue

    
    def setUpper3(self, upper3):
        returnValue = libpanda._inPUZN34JsI(self.this, upper3.this)
        return returnValue

    
    def getUpper3(self):
        returnValue = libpanda._inPUZN3cZBN(self.this)
        import Mat3D
        returnObject = Mat3D.Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4D__overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase3d(self, row, v):
        returnValue = libpanda._inPUZN34DFT(self.this, row, v.this)
        return returnValue

    
    def _Mat4D__overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase4d(self, row, v):
        returnValue = libpanda._inPUZN3kD10(self.this, row, v.this)
        return returnValue

    
    def _Mat4D__overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase3d(self, col, v):
        returnValue = libpanda._inPUZN3dmWa(self.this, col, v.this)
        return returnValue

    
    def _Mat4D__overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase4d(self, col, v):
        returnValue = libpanda._inPUZN3JmG8(self.this, col, v.this)
        return returnValue

    
    def _Mat4D__overloaded_getRow_ptrConstLMatrix4d_ptrLVecBase4d_int(self, resultVec, row):
        returnValue = libpanda._inPUZN3Qxez(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat4D__overloaded_getRow_ptrConstLMatrix4d_int(self, row):
        returnValue = libpanda._inPUZN3Wxx8(self.this, row)
        import VBase4D
        returnObject = VBase4D.VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol(self, col):
        returnValue = libpanda._inPUZN3rPFE(self.this, col)
        import VBase4D
        returnObject = VBase4D.VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4D__overloaded_getRow3_ptrConstLMatrix4d_ptrLVecBase3d_int(self, resultVec, row):
        returnValue = libpanda._inPUZN3fTWu(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat4D__overloaded_getRow3_ptrConstLMatrix4d_int(self, row):
        returnValue = libpanda._inPUZN3TL2y(self.this, row)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol3(self, col):
        returnValue = libpanda._inPUZN3_pJ6(self.this, col)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4D__overloaded___call___ptrLMatrix4d_int_int(self, row, col):
        returnValue = libpanda._inPUZN3ZgS1(self.this, row, col)
        return returnValue

    
    def _Mat4D__overloaded___call___ptrConstLMatrix4d_int_int(self, row, col):
        returnValue = libpanda._inPUZN3gkEX(self.this, row, col)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPUZN3vXM3(self.this)
        return returnValue

    
    def getCell(self, row, col):
        returnValue = libpanda._inPUZN3tb8V(self.this, row, col)
        return returnValue

    
    def setCell(self, row, col, value):
        returnValue = libpanda._inPUZN3b2F1(self.this, row, col, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPUZN3sPV1(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPUZN3xv30(self.this)
        return returnValue

    
    def _Mat4D__overloaded_begin_ptrLMatrix4d(self):
        returnValue = libpanda._inPUZN3jKXP(self.this)
        return returnValue

    
    def _Mat4D__overloaded_begin_ptrConstLMatrix4d(self):
        returnValue = libpanda._inPUZN3mQjW(self.this)
        return returnValue

    
    def _Mat4D__overloaded_end_ptrLMatrix4d(self):
        returnValue = libpanda._inPUZN3PBFI(self.this)
        return returnValue

    
    def _Mat4D__overloaded_end_ptrConstLMatrix4d(self):
        returnValue = libpanda._inPUZN3_wtn(self.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPUZN3Xz9P(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPUZN3Q4WW(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPUZN3QPzN(self.this, other.this)
        return returnValue

    
    def _Mat4D__overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d(self, other):
        returnValue = libpanda._inPUZN3az9H(self.this, other.this)
        return returnValue

    
    def _Mat4D__overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d_double(self, other, threshold):
        returnValue = libpanda._inPUZN3lGtQ(self.this, other.this, threshold)
        return returnValue

    
    def xform(self, v):
        returnValue = libpanda._inPUZN3N133(self.this, v.this)
        import VBase4D
        returnObject = VBase4D.VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformPoint(self, v):
        returnValue = libpanda._inPUZN3T1IX(self.this, v.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformVec(self, v):
        returnValue = libpanda._inPUZN38CVq(self.this, v.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, other1, other2):
        returnValue = libpanda._inPUZN3U8DL(self.this, other1.this, other2.this)
        return returnValue

    
    def scaleMultiply(self, scaleVector, otherMat):
        returnValue = libpanda._inPUZN3c9iA(self.this, scaleVector.this, otherMat.this)
        return returnValue

    
    def _Mat4D__overloaded___mul___ptrConstLMatrix4d_ptrConstLMatrix4d(self, other):
        returnValue = libpanda._inPUZN33TdK(self.this, other.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4D__overloaded___mul___ptrConstLMatrix4d_double(self, scalar):
        returnValue = libpanda._inPUZN39_TF(self.this, scalar)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3NI1G(self.this, scalar)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPUZN38vNX(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPUZN3cj0X(self.this, other.this)
        return self

    
    def _Mat4D__overloaded___imul___ptrLMatrix4d_ptrConstLMatrix4d(self, other):
        returnValue = libpanda._inPUZN3MO5W(self.this, other.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat4D__overloaded___imul___ptrLMatrix4d_double(self, scalar):
        returnValue = libpanda._inPUZN3WUUT(self.this, scalar)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPUZN3m93U(self.this, scalar)
        return self

    
    def transposeFrom(self, other):
        returnValue = libpanda._inPUZN3oYQI(self.this, other.this)
        return returnValue

    
    def transposeInPlace(self):
        returnValue = libpanda._inPUZN3ivGM(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPUZN3NuDN(self.this, other.this)
        return returnValue

    
    def invertAffineFrom(self, other):
        returnValue = libpanda._inPUZN3g2mD(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPUZN3LOv7(self.this)
        return returnValue

    
    def _Mat4D__overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d(self, other):
        returnValue = libpanda._inPUZN3qIgc(self.this, other.this)
        return returnValue

    
    def _Mat4D__overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d_double(self, other, threshold):
        returnValue = libpanda._inPUZN3rOXn(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPUZN3dkYL(self.this, out.this)
        return returnValue

    
    def _Mat4D__overloaded_write_ptrConstLMatrix4d_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPUZN3XBeC(self.this, out.this, indentLevel)
        return returnValue

    
    def _Mat4D__overloaded_write_ptrConstLMatrix4d_ptrOstream(self, out):
        returnValue = libpanda._inPUZN3XY5L(self.this, out.this)
        return returnValue

    
    def scaleMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3D
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return Mat4D._Mat4D__overloaded_scaleMat_double(_args[0])
            elif isinstance(_args[0], VBase3D.VBase3D):
                return Mat4D._Mat4D__overloaded_scaleMat_ptrConstLVecBase3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return Mat4D._Mat4D__overloaded_scaleMat_double_double_double(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    scaleMat = staticmethod(scaleMat)
    
    def translateMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return Mat4D._Mat4D__overloaded_translateMat_ptrConstLVecBase3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return Mat4D._Mat4D__overloaded_translateMat_double_double_double(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    translateMat = staticmethod(translateMat)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4D__overloaded_constructor()
        elif numArgs == 1:
            import Mat3D
            if isinstance(_args[0], Mat4D):
                return self._Mat4D__overloaded_constructor_ptrConstLMatrix4d(_args[0])
            elif isinstance(_args[0], Mat3D.Mat3D):
                return self._Mat4D__overloaded_constructor_ptrConstLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> <Mat3D.Mat3D> '
        elif numArgs == 2:
            import Mat3D
            if isinstance(_args[0], Mat3D.Mat3D):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return self._Mat4D__overloaded_constructor_ptrConstLMatrix3d_ptrConstLVecBase3d(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> '
        elif numArgs == 16:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                            if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                if isinstance(_args[9], types.FloatType) or isinstance(_args[9], types.IntType):
                                                    if isinstance(_args[10], types.FloatType) or isinstance(_args[10], types.IntType):
                                                        if isinstance(_args[11], types.FloatType) or isinstance(_args[11], types.IntType):
                                                            if isinstance(_args[12], types.FloatType) or isinstance(_args[12], types.IntType):
                                                                if isinstance(_args[13], types.FloatType) or isinstance(_args[13], types.IntType):
                                                                    if isinstance(_args[14], types.FloatType) or isinstance(_args[14], types.IntType):
                                                                        if isinstance(_args[15], types.FloatType) or isinstance(_args[15], types.IntType):
                                                                            return self._Mat4D__overloaded_constructor_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8], _args[9], _args[10], _args[11], _args[12], _args[13], _args[14], _args[15])
                                                                        else:
                                                                            raise TypeError, 'Invalid argument 15, expected one of: <types.FloatType> '
                                                                    else:
                                                                        raise TypeError, 'Invalid argument 14, expected one of: <types.FloatType> '
                                                                else:
                                                                    raise TypeError, 'Invalid argument 13, expected one of: <types.FloatType> '
                                                            else:
                                                                raise TypeError, 'Invalid argument 12, expected one of: <types.FloatType> '
                                                        else:
                                                            raise TypeError, 'Invalid argument 11, expected one of: <types.FloatType> '
                                                    else:
                                                        raise TypeError, 'Invalid argument 10, expected one of: <types.FloatType> '
                                                else:
                                                    raise TypeError, 'Invalid argument 9, expected one of: <types.FloatType> '
                                            else:
                                                raise TypeError, 'Invalid argument 8, expected one of: <types.FloatType> '
                                        else:
                                            raise TypeError, 'Invalid argument 7, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 16 '

    
    def rotateMat(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return Mat4D._Mat4D__overloaded_rotateMat_double_ptrLVecBase3d(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    if isinstance(_args[2], types.IntType):
                        return Mat4D._Mat4D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    rotateMat = staticmethod(rotateMat)
    
    def rotateMatNormaxis(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return Mat4D._Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    if isinstance(_args[2], types.IntType):
                        return Mat4D._Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                    elif isinstance(_args[2], Mat4D):
                        return Mat4D._Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Mat4D> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    if isinstance(_args[2], Mat4D):
                        if isinstance(_args[3], types.IntType):
                            return Mat4D._Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Mat4D> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '

    rotateMatNormaxis = staticmethod(rotateMatNormaxis)
    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Mat4D):
                return self._Mat4D__overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> '
        elif numArgs == 2:
            if isinstance(_args[0], Mat4D):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Mat4D__overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def begin(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4D__overloaded_begin_ptrConstLMatrix4d()
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def end(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4D__overloaded_end_ptrConstLMatrix4d()
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def __imul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat4D__overloaded___imul___ptrLMatrix4d_double(_args[0])
            elif isinstance(_args[0], Mat4D):
                return self._Mat4D__overloaded___imul___ptrLMatrix4d_ptrConstLMatrix4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def getRow3(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._Mat4D__overloaded_getRow3_ptrConstLMatrix4d_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                if isinstance(_args[1], types.IntType):
                    return self._Mat4D__overloaded_getRow3_ptrConstLMatrix4d_ptrLVecBase3d_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._Mat4D__overloaded_getRow_ptrConstLMatrix4d_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            import VBase4D
            if isinstance(_args[0], VBase4D.VBase4D):
                if isinstance(_args[1], types.IntType):
                    return self._Mat4D__overloaded_getRow_ptrConstLMatrix4d_ptrLVecBase4d_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4D.VBase4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Mat4D__overloaded_write_ptrConstLMatrix4d_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._Mat4D__overloaded_write_ptrConstLMatrix4d_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __call__(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._Mat4D__overloaded___call___ptrConstLMatrix4d_int_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat4D__overloaded___mul___ptrConstLMatrix4d_double(_args[0])
            elif isinstance(_args[0], Mat4D):
                return self._Mat4D__overloaded___mul___ptrConstLMatrix4d_ptrConstLMatrix4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Mat4D):
                return self._Mat4D__overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> '
        elif numArgs == 2:
            if isinstance(_args[0], Mat4D):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Mat4D__overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCol(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase4D
                import VBase3D
                if isinstance(_args[1], VBase4D.VBase4D):
                    return self._Mat4D__overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase4d(_args[0], _args[1])
                elif isinstance(_args[1], VBase3D.VBase3D):
                    return self._Mat4D__overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase3d(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase4D.VBase4D> <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def setRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase4D
                import VBase3D
                if isinstance(_args[1], VBase4D.VBase4D):
                    return self._Mat4D__overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase4d(_args[0], _args[1])
                elif isinstance(_args[1], VBase3D.VBase3D):
                    return self._Mat4D__overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase3d(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase4D.VBase4D> <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat4D__overloaded_assign_ptrLMatrix4d_double(_args[0])
            elif isinstance(_args[0], Mat4D):
                return self._Mat4D__overloaded_assign_ptrLMatrix4d_ptrConstLMatrix4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


