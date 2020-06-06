# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class Mat3D(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Mat3D__overloaded_constructor(self):
        self.this = libpanda._inPUZN3HKtQ()
        self.userManagesMemory = 1

    
    def _Mat3D__overloaded_constructor_ptrConstLMatrix3d(self, other):
        self.this = libpanda._inPUZN3nwPr(other.this)
        self.userManagesMemory = 1

    
    def _Mat3D__overloaded_constructor_double_double_double_double_double_double_double_double_double(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
        self.this = libpanda._inPUZN30oPv(e00, e01, e02, e10, e11, e12, e20, e21, e22)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3VziA:
            libpanda._inPUZN3VziA(self.this)
        

    
    def identMat():
        returnValue = libpanda._inPUZN3A_Pl()
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identMat = staticmethod(identMat)
    
    def _Mat3D__overloaded_translateMat_ptrConstLVecBase2d(trans):
        returnValue = libpanda._inPUZN3DpG4(trans.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_translateMat_ptrConstLVecBase2d = staticmethod(_Mat3D__overloaded_translateMat_ptrConstLVecBase2d)
    
    def _Mat3D__overloaded_translateMat_double_double(tx, ty):
        returnValue = libpanda._inPUZN3ais7(tx, ty)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_translateMat_double_double = staticmethod(_Mat3D__overloaded_translateMat_double_double)
    
    def _Mat3D__overloaded_rotateMat_double(angle):
        returnValue = libpanda._inPUZN3B6hL(angle)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_rotateMat_double = staticmethod(_Mat3D__overloaded_rotateMat_double)
    
    def _Mat3D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPUZN3aFgZ(angle, axis.this, cs)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat3D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem)
    
    def _Mat3D__overloaded_rotateMat_double_ptrLVecBase3d(angle, axis):
        returnValue = libpanda._inPUZN3y6sm(angle, axis.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_rotateMat_double_ptrLVecBase3d = staticmethod(_Mat3D__overloaded_rotateMat_double_ptrLVecBase3d)
    
    def _Mat3D__overloaded_scaleMat_ptrConstLVecBase2d(scale):
        returnValue = libpanda._inPUZN3kw5e(scale.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleMat_ptrConstLVecBase2d = staticmethod(_Mat3D__overloaded_scaleMat_ptrConstLVecBase2d)
    
    def _Mat3D__overloaded_scaleMat_ptrConstLVecBase3d(scale):
        returnValue = libpanda._inPUZN32c8e(scale.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleMat_ptrConstLVecBase3d = staticmethod(_Mat3D__overloaded_scaleMat_ptrConstLVecBase3d)
    
    def _Mat3D__overloaded_scaleMat_double_double(sx, sy):
        returnValue = libpanda._inPUZN3KYtY(sx, sy)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleMat_double_double = staticmethod(_Mat3D__overloaded_scaleMat_double_double)
    
    def _Mat3D__overloaded_scaleMat_double_double_double(sx, sy, sz):
        returnValue = libpanda._inPUZN3XTVN(sx, sy, sz)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleMat_double_double_double = staticmethod(_Mat3D__overloaded_scaleMat_double_double_double)
    
    def _Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPUZN39h6r(angle, axis.this, cs)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem)
    
    def _Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(angle, axis):
        returnValue = libpanda._inPUZN3YlqF(angle, axis.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d = staticmethod(_Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d)
    
    def convertMat(_from, to):
        returnValue = libpanda._inPUZN35uUm(_from, to)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    convertMat = staticmethod(convertMat)
    
    def getClassType():
        returnValue = libpanda._inPUZN3nXHQ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Mat3D__overloaded_assign_ptrLMatrix3d_ptrConstLMatrix3d(self, other):
        returnValue = libpanda._inPUZN39QZH(self.this, other.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat3D__overloaded_assign_ptrLMatrix3d_double(self, fillValue):
        returnValue = libpanda._inPUZN3ByUJ(self.this, fillValue)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def fill(self, fillValue):
        returnValue = libpanda._inPUZN3tMiW(self.this, fillValue)
        return returnValue

    
    def set(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
        returnValue = libpanda._inPUZN3YSjO(self.this, e00, e01, e02, e10, e11, e12, e20, e21, e22)
        return returnValue

    
    def _Mat3D__overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase2d(self, row, v):
        returnValue = libpanda._inPUZN3MjRK(self.this, row, v.this)
        return returnValue

    
    def _Mat3D__overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase3d(self, row, v):
        returnValue = libpanda._inPUZN34jBs(self.this, row, v.this)
        return returnValue

    
    def _Mat3D__overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase2d(self, col, v):
        returnValue = libpanda._inPUZN3hFlR(self.this, col, v.this)
        return returnValue

    
    def _Mat3D__overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase3d(self, col, v):
        returnValue = libpanda._inPUZN3dGVz(self.this, col, v.this)
        return returnValue

    
    def _Mat3D__overloaded_getRow_ptrConstLMatrix3d_ptrLVecBase3d_int(self, resultVec, row):
        returnValue = libpanda._inPUZN3FRjb(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat3D__overloaded_getRow_ptrConstLMatrix3d_int(self, row):
        returnValue = libpanda._inPUZN3pQuV(self.this, row)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol(self, col):
        returnValue = libpanda._inPUZN3qvBd(self.this, col)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRow2(self, row):
        returnValue = libpanda._inPUZN3CqyE(self.this, row)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol2(self, col):
        returnValue = libpanda._inPUZN3xKGM(self.this, col)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat3D__overloaded___call___ptrLMatrix3d_int_int(self, row, col):
        returnValue = libpanda._inPUZN3YAPO(self.this, row, col)
        return returnValue

    
    def _Mat3D__overloaded___call___ptrConstLMatrix3d_int_int(self, row, col):
        returnValue = libpanda._inPUZN3gEAw(self.this, row, col)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPUZN3u3JQ(self.this)
        return returnValue

    
    def getCell(self, row, col):
        returnValue = libpanda._inPUZN3t75u(self.this, row, col)
        return returnValue

    
    def setCell(self, row, col, value):
        returnValue = libpanda._inPUZN3YWBO(self.this, row, col, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPUZN3tvRO(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPUZN3wP0N(self.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPUZN3Fv3o(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPUZN3QREu(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPUZN3Qgil(self.this, other.this)
        return returnValue

    
    def _Mat3D__overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d(self, other):
        returnValue = libpanda._inPUZN3s_3g(self.this, other.this)
        return returnValue

    
    def _Mat3D__overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d_double(self, other, threshold):
        returnValue = libpanda._inPUZN3Tbnp(self.this, other.this, threshold)
        return returnValue

    
    def xform(self, v):
        returnValue = libpanda._inPUZN3uQNQ(self.this, v.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformPoint(self, v):
        returnValue = libpanda._inPUZN3S1BJ(self.this, v.this)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformVec(self, v):
        returnValue = libpanda._inPUZN3RGPD(self.this, v.this)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, other1, other2):
        returnValue = libpanda._inPUZN3Z5GD(self.this, other1.this, other2.this)
        return returnValue

    
    def _Mat3D__overloaded___mul___ptrConstLMatrix3d_ptrConstLMatrix3d(self, other):
        returnValue = libpanda._inPUZN3lPXj(self.this, other.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat3D__overloaded___mul___ptrConstLMatrix3d_double(self, scalar):
        returnValue = libpanda._inPUZN3_fQe(self.this, scalar)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3Ooxf(self.this, scalar)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def scaleMultiply(self, scaleVector, otherMat):
        returnValue = libpanda._inPUZN3dFtP(self.this, scaleVector.this, otherMat.this)
        return returnValue

    
    def __iadd__(self, other):
        returnValue = libpanda._inPUZN3807u(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPUZN3cIiv(self.this, other.this)
        return self

    
    def _Mat3D__overloaded___imul___ptrLMatrix3d_ptrConstLMatrix3d(self, other):
        returnValue = libpanda._inPUZN3MXnu(self.this, other.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat3D__overloaded___imul___ptrLMatrix3d_double(self, scalar):
        returnValue = libpanda._inPUZN3W0Qs(self.this, scalar)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPUZN3mdyt(self.this, scalar)
        return self

    
    def determinant(self):
        returnValue = libpanda._inPUZN3syFI(self.this)
        return returnValue

    
    def transposeFrom(self, other):
        returnValue = libpanda._inPUZN3bONp(self.this, other.this)
        return returnValue

    
    def transposeInPlace(self):
        returnValue = libpanda._inPUZN3iPDl(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPUZN3NJyk(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPUZN3IurU(self.this)
        return returnValue

    
    def _Mat3D__overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d(self, other):
        returnValue = libpanda._inPUZN3rIZO(self.this, other.this)
        return returnValue

    
    def _Mat3D__overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d_double(self, other, threshold):
        returnValue = libpanda._inPUZN3pOQZ(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPUZN3dEVk(self.this, out.this)
        return returnValue

    
    def _Mat3D__overloaded_write_ptrConstLMatrix3d_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPUZN3Ihab(self.this, out.this, indentLevel)
        return returnValue

    
    def _Mat3D__overloaded_write_ptrConstLMatrix3d_ptrOstream(self, out):
        returnValue = libpanda._inPUZN3X41k(self.this, out.this)
        return returnValue

    
    def scaleMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3D
            import VBase2D
            if isinstance(_args[0], VBase3D.VBase3D):
                return Mat3D._Mat3D__overloaded_scaleMat_ptrConstLVecBase3d(_args[0])
            elif isinstance(_args[0], VBase2D.VBase2D):
                return Mat3D._Mat3D__overloaded_scaleMat_ptrConstLVecBase2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <VBase2D.VBase2D> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return Mat3D._Mat3D__overloaded_scaleMat_double_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return Mat3D._Mat3D__overloaded_scaleMat_double_double_double(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    scaleMat = staticmethod(scaleMat)
    
    def translateMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return Mat3D._Mat3D__overloaded_translateMat_ptrConstLVecBase2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2D.VBase2D> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return Mat3D._Mat3D__overloaded_translateMat_double_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    translateMat = staticmethod(translateMat)
    
    def rotateMatNormaxis(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return Mat3D._Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    if isinstance(_args[2], types.IntType):
                        return Mat3D._Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    rotateMatNormaxis = staticmethod(rotateMatNormaxis)
    
    def rotateMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return Mat3D._Mat3D__overloaded_rotateMat_double(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return Mat3D._Mat3D__overloaded_rotateMat_double_ptrLVecBase3d(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    if isinstance(_args[2], types.IntType):
                        return Mat3D._Mat3D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    rotateMat = staticmethod(rotateMat)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat3D__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], Mat3D):
                return self._Mat3D__overloaded_constructor_ptrConstLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3D> '
        elif numArgs == 9:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                            if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                return self._Mat3D__overloaded_constructor_double_double_double_double_double_double_double_double_double(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8])
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
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 9 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Mat3D__overloaded_write_ptrConstLMatrix3d_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._Mat3D__overloaded_write_ptrConstLMatrix3d_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Mat3D):
                return self._Mat3D__overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3D> '
        elif numArgs == 2:
            if isinstance(_args[0], Mat3D):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Mat3D__overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __imul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat3D__overloaded___imul___ptrLMatrix3d_double(_args[0])
            elif isinstance(_args[0], Mat3D):
                return self._Mat3D__overloaded___imul___ptrLMatrix3d_ptrConstLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Mat3D):
                return self._Mat3D__overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3D> '
        elif numArgs == 2:
            if isinstance(_args[0], Mat3D):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Mat3D__overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __call__(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._Mat3D__overloaded___call___ptrConstLMatrix3d_int_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def setRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3D
                import VBase2D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return self._Mat3D__overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase3d(_args[0], _args[1])
                elif isinstance(_args[1], VBase2D.VBase2D):
                    return self._Mat3D__overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase2d(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> <VBase2D.VBase2D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def setCol(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3D
                import VBase2D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return self._Mat3D__overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase3d(_args[0], _args[1])
                elif isinstance(_args[1], VBase2D.VBase2D):
                    return self._Mat3D__overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase2d(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> <VBase2D.VBase2D> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat3D__overloaded_assign_ptrLMatrix3d_double(_args[0])
            elif isinstance(_args[0], Mat3D):
                return self._Mat3D__overloaded_assign_ptrLMatrix3d_ptrConstLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def getRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._Mat3D__overloaded_getRow_ptrConstLMatrix3d_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                if isinstance(_args[1], types.IntType):
                    return self._Mat3D__overloaded_getRow_ptrConstLMatrix3d_ptrLVecBase3d_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat3D__overloaded___mul___ptrConstLMatrix3d_double(_args[0])
            elif isinstance(_args[0], Mat3D):
                return self._Mat3D__overloaded___mul___ptrConstLMatrix3d_ptrConstLMatrix3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


