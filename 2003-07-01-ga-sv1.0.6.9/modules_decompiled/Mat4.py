# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class Mat4(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Mat4__overloaded_constructor(self):
        self.this = libpanda._inPUZN30VSC()
        self.userManagesMemory = 1

    
    def _Mat4__overloaded_constructor_ptrConstLMatrix3f(self, upper3):
        self.this = libpanda._inPUZN3fs5c(upper3.this)
        self.userManagesMemory = 1

    
    def _Mat4__overloaded_constructor_ptrConstLMatrix3f_ptrConstLVecBase3f(self, upper3, trans):
        self.this = libpanda._inPUZN37_z9(upper3.this, trans.this)
        self.userManagesMemory = 1

    
    def _Mat4__overloaded_constructor_ptrConstLMatrix4f(self, other):
        self.this = libpanda._inPUZN3U354(other.this)
        self.userManagesMemory = 1

    
    def _Mat4__overloaded_constructor_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
        self.this = libpanda._inPUZN3rfiq(e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN37ZvL:
            libpanda._inPUZN37ZvL(self.this)
        

    
    def identMat():
        returnValue = libpanda._inPUZN3rczP()
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identMat = staticmethod(identMat)
    
    def _Mat4__overloaded_translateMat_ptrConstLVecBase3f(trans):
        returnValue = libpanda._inPUZN3jyza(trans.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_translateMat_ptrConstLVecBase3f = staticmethod(_Mat4__overloaded_translateMat_ptrConstLVecBase3f)
    
    def _Mat4__overloaded_translateMat_float_float_float(tx, ty, tz):
        returnValue = libpanda._inPUZN3Q9hS(tx, ty, tz)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_translateMat_float_float_float = staticmethod(_Mat4__overloaded_translateMat_float_float_float)
    
    def _Mat4__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPUZN38AQA(angle, axis.this, cs)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat4__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem)
    
    def _Mat4__overloaded_rotateMat_float_ptrLVecBase3f(angle, axis):
        returnValue = libpanda._inPUZN3zUuW(angle, axis.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_rotateMat_float_ptrLVecBase3f = staticmethod(_Mat4__overloaded_rotateMat_float_ptrLVecBase3f)
    
    def _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPUZN3TFBu(angle, axis.this, cs)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem)
    
    def _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(angle, axis):
        returnValue = libpanda._inPUZN3l_5A(angle, axis.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f = staticmethod(_Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f)
    
    def _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem(angle, axis, resultMat, cs):
        returnValue = libpanda._inPUZN3e71s(angle, axis.this, resultMat.this, cs)
        return returnValue

    _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem = staticmethod(_Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem)
    
    def _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f(angle, axis, resultMat):
        returnValue = libpanda._inPUZN3RMA0(angle, axis.this, resultMat.this)
        return returnValue

    _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f = staticmethod(_Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f)
    
    def _Mat4__overloaded_scaleMat_ptrConstLVecBase3f(scale):
        returnValue = libpanda._inPUZN3OJ8L(scale.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_scaleMat_ptrConstLVecBase3f = staticmethod(_Mat4__overloaded_scaleMat_ptrConstLVecBase3f)
    
    def _Mat4__overloaded_scaleMat_float(scale):
        returnValue = libpanda._inPUZN3gj9H(scale)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_scaleMat_float = staticmethod(_Mat4__overloaded_scaleMat_float)
    
    def _Mat4__overloaded_scaleMat_float_float_float(sx, sy, sz):
        returnValue = libpanda._inPUZN3waqH(sx, sy, sz)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_scaleMat_float_float_float = staticmethod(_Mat4__overloaded_scaleMat_float_float_float)
    
    def yToZUpMat():
        returnValue = libpanda._inPUZN3lIST()
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    yToZUpMat = staticmethod(yToZUpMat)
    
    def zToYUpMat():
        returnValue = libpanda._inPUZN3lG2Q()
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zToYUpMat = staticmethod(zToYUpMat)
    
    def convertMat(_from, to):
        returnValue = libpanda._inPUZN3gP4Q(_from, to)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    convertMat = staticmethod(convertMat)
    
    def getClassType():
        returnValue = libpanda._inPUZN3P3r6()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Mat4__overloaded_assign_ptrLMatrix4f_ptrConstLMatrix4f(self, other):
        returnValue = libpanda._inPUZN3nLb0(self.this, other.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat4__overloaded_assign_ptrLMatrix4f_float(self, fillValue):
        returnValue = libpanda._inPUZN3I5tl(self.this, fillValue)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def fill(self, fillValue):
        returnValue = libpanda._inPUZN3hn3a(self.this, fillValue)
        return returnValue

    
    def set(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
        returnValue = libpanda._inPUZN3c_Gk(self.this, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
        return returnValue

    
    def setUpper3(self, upper3):
        returnValue = libpanda._inPUZN3QITa(self.this, upper3.this)
        return returnValue

    
    def getUpper3(self):
        returnValue = libpanda._inPUZN31ZhQ(self.this)
        import Mat3
        returnObject = Mat3.Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4__overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase3f(self, row, v):
        returnValue = libpanda._inPUZN32ZkG(self.this, row, v.this)
        return returnValue

    
    def _Mat4__overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase4f(self, row, v):
        returnValue = libpanda._inPUZN3iZUo(self.this, row, v.this)
        return returnValue

    
    def _Mat4__overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase3f(self, col, v):
        returnValue = libpanda._inPUZN3b83N(self.this, col, v.this)
        return returnValue

    
    def _Mat4__overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase4f(self, col, v):
        returnValue = libpanda._inPUZN338nv(self.this, col, v.this)
        return returnValue

    
    def _Mat4__overloaded_getRow_ptrConstLMatrix4f_ptrLVecBase4f_int(self, resultVec, row):
        returnValue = libpanda._inPUZN3o__u(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat4__overloaded_getRow_ptrConstLMatrix4f_int(self, row):
        returnValue = libpanda._inPUZN3xxRA(self.this, row)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol(self, col):
        returnValue = libpanda._inPUZN3COlH(self.this, col)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4__overloaded_getRow3_ptrConstLMatrix4f_ptrLVecBase3f_int(self, resultVec, row):
        returnValue = libpanda._inPUZN3SF7x(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat4__overloaded_getRow3_ptrConstLMatrix4f_int(self, row):
        returnValue = libpanda._inPUZN3IMW2(self.this, row)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol3(self, col):
        returnValue = libpanda._inPUZN3nop9(self.this, col)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4__overloaded___call___ptrLMatrix4f_int_int(self, row, col):
        returnValue = libpanda._inPUZN3Ahy4(self.this, row, col)
        return returnValue

    
    def _Mat4__overloaded___call___ptrConstLMatrix4f_int_int(self, row, col):
        returnValue = libpanda._inPUZN3_lka(self.this, row, col)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPUZN3WXs6(self.this)
        return returnValue

    
    def getCell(self, row, col):
        returnValue = libpanda._inPUZN3GYcZ(self.this, row, col)
        return returnValue

    
    def setCell(self, row, col, value):
        returnValue = libpanda._inPUZN3kUBv(self.this, row, col, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPUZN3VP14(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPUZN3YsX4(self.this)
        return returnValue

    
    def _Mat4__overloaded_begin_ptrLMatrix4f(self):
        returnValue = libpanda._inPUZN3KK3S(self.this)
        return returnValue

    
    def _Mat4__overloaded_begin_ptrConstLMatrix4f(self):
        returnValue = libpanda._inPUZN3BQDa(self.this)
        return returnValue

    
    def _Mat4__overloaded_end_ptrLMatrix4f(self):
        returnValue = libpanda._inPUZN3m_kL(self.this)
        return returnValue

    
    def _Mat4__overloaded_end_ptrConstLMatrix4f(self):
        returnValue = libpanda._inPUZN3hxNr(self.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPUZN38l5V(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPUZN3L59n(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPUZN3IOaf(self.this, other.this)
        return returnValue

    
    def _Mat4__overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f(self, other):
        returnValue = libpanda._inPUZN3zB6N(self.this, other.this)
        return returnValue

    
    def _Mat4__overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f_float(self, other, threshold):
        returnValue = libpanda._inPUZN3mOfK(self.this, other.this, threshold)
        return returnValue

    
    def xform(self, v):
        returnValue = libpanda._inPUZN3lWbi(self.this, v.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformPoint(self, v):
        returnValue = libpanda._inPUZN3F0Ie(self.this, v.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformVec(self, v):
        returnValue = libpanda._inPUZN3b7Sw(self.this, v.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, other1, other2):
        returnValue = libpanda._inPUZN3cv3G(self.this, other1.this, other2.this)
        return returnValue

    
    def scaleMultiply(self, scaleVector, otherMat):
        returnValue = libpanda._inPUZN3vey5(self.this, scaleVector.this, otherMat.this)
        return returnValue

    
    def _Mat4__overloaded___mul___ptrConstLMatrix4f_ptrConstLMatrix4f(self, other):
        returnValue = libpanda._inPUZN3cFZQ(self.this, other.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4__overloaded___mul___ptrConstLMatrix4f_float(self, scalar):
        returnValue = libpanda._inPUZN3blu8(self.this, scalar)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3LKP_(self.this, scalar)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPUZN3Fv0o(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPUZN3ljbp(self.this, other.this)
        return self

    
    def _Mat4__overloaded___imul___ptrLMatrix4f_ptrConstLMatrix4f(self, other):
        returnValue = libpanda._inPUZN31Ogo(self.this, other.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat4__overloaded___imul___ptrLMatrix4f_float(self, scalar):
        returnValue = libpanda._inPUZN3Nn8Q(self.this, scalar)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPUZN3dceS(self.this, scalar)
        return self

    
    def transposeFrom(self, other):
        returnValue = libpanda._inPUZN3rI6L(self.this, other.this)
        return returnValue

    
    def transposeInPlace(self):
        returnValue = libpanda._inPUZN39umP(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPUZN3Vtqe(self.this, other.this)
        return returnValue

    
    def invertAffineFrom(self, other):
        returnValue = libpanda._inPUZN3LvHn(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPUZN3gOP_(self.this)
        return returnValue

    
    def _Mat4__overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f(self, other):
        returnValue = libpanda._inPUZN37Lgj(self.this, other.this)
        return returnValue

    
    def _Mat4__overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f_float(self, other, threshold):
        returnValue = libpanda._inPUZN39SSI(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPUZN30k4O(self.this, out.this)
        return returnValue

    
    def _Mat4__overloaded_write_ptrConstLMatrix4f_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPUZN3wC_F(self.this, out.this, indentLevel)
        return returnValue

    
    def _Mat4__overloaded_write_ptrConstLMatrix4f_ptrOstream(self, out):
        returnValue = libpanda._inPUZN3sZZP(self.this, out.this)
        return returnValue

    
    def scaleMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return Mat4._Mat4__overloaded_scaleMat_float(_args[0])
            elif isinstance(_args[0], VBase3.VBase3):
                return Mat4._Mat4__overloaded_scaleMat_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return Mat4._Mat4__overloaded_scaleMat_float_float_float(_args[0], _args[1], _args[2])
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
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return Mat4._Mat4__overloaded_translateMat_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return Mat4._Mat4__overloaded_translateMat_float_float_float(_args[0], _args[1], _args[2])
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
            return self._Mat4__overloaded_constructor()
        elif numArgs == 1:
            import Mat3
            if isinstance(_args[0], Mat4):
                return self._Mat4__overloaded_constructor_ptrConstLMatrix4f(_args[0])
            elif isinstance(_args[0], Mat3.Mat3):
                return self._Mat4__overloaded_constructor_ptrConstLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4> <Mat3.Mat3> '
        elif numArgs == 2:
            import Mat3
            if isinstance(_args[0], Mat3.Mat3):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._Mat4__overloaded_constructor_ptrConstLMatrix3f_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3.Mat3> '
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
                                                                            return self._Mat4__overloaded_constructor_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8], _args[9], _args[10], _args[11], _args[12], _args[13], _args[14], _args[15])
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
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return Mat4._Mat4__overloaded_rotateMat_float_ptrLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    if isinstance(_args[2], types.IntType):
                        return Mat4._Mat4__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    rotateMat = staticmethod(rotateMat)
    
    def rotateMatNormaxis(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return Mat4._Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    if isinstance(_args[2], types.IntType):
                        return Mat4._Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                    elif isinstance(_args[2], Mat4):
                        return Mat4._Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Mat4> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    if isinstance(_args[2], Mat4):
                        if isinstance(_args[3], types.IntType):
                            return Mat4._Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Mat4> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '

    rotateMatNormaxis = staticmethod(rotateMatNormaxis)
    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Mat4):
                return self._Mat4__overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4> '
        elif numArgs == 2:
            if isinstance(_args[0], Mat4):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Mat4__overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def begin(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4__overloaded_begin_ptrConstLMatrix4f()
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def end(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4__overloaded_end_ptrConstLMatrix4f()
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def __imul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat4__overloaded___imul___ptrLMatrix4f_float(_args[0])
            elif isinstance(_args[0], Mat4):
                return self._Mat4__overloaded___imul___ptrLMatrix4f_ptrConstLMatrix4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def getRow3(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._Mat4__overloaded_getRow3_ptrConstLMatrix4f_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                if isinstance(_args[1], types.IntType):
                    return self._Mat4__overloaded_getRow3_ptrConstLMatrix4f_ptrLVecBase3f_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._Mat4__overloaded_getRow_ptrConstLMatrix4f_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                if isinstance(_args[1], types.IntType):
                    return self._Mat4__overloaded_getRow_ptrConstLMatrix4f_ptrLVecBase4f_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Mat4__overloaded_write_ptrConstLMatrix4f_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._Mat4__overloaded_write_ptrConstLMatrix4f_ptrOstream_int(_args[0], _args[1])
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
                    return self._Mat4__overloaded___call___ptrConstLMatrix4f_int_int(_args[0], _args[1])
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
                return self._Mat4__overloaded___mul___ptrConstLMatrix4f_float(_args[0])
            elif isinstance(_args[0], Mat4):
                return self._Mat4__overloaded___mul___ptrConstLMatrix4f_ptrConstLMatrix4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Mat4):
                return self._Mat4__overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4> '
        elif numArgs == 2:
            if isinstance(_args[0], Mat4):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Mat4__overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCol(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase4
                import VBase3
                if isinstance(_args[1], VBase4.VBase4):
                    return self._Mat4__overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase4f(_args[0], _args[1])
                elif isinstance(_args[1], VBase3.VBase3):
                    return self._Mat4__overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def setRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase4
                import VBase3
                if isinstance(_args[1], VBase4.VBase4):
                    return self._Mat4__overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase4f(_args[0], _args[1])
                elif isinstance(_args[1], VBase3.VBase3):
                    return self._Mat4__overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat4__overloaded_assign_ptrLMatrix4f_float(_args[0])
            elif isinstance(_args[0], Mat4):
                return self._Mat4__overloaded_assign_ptrLMatrix4f_ptrConstLMatrix4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


