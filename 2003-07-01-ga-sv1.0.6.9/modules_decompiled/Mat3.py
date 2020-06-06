# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class Mat3(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Mat3__overloaded_constructor(self):
        self.this = libpanda._inPUZN3l0PU()
        self.userManagesMemory = 1

    
    def _Mat3__overloaded_constructor_ptrConstLMatrix3f(self, other):
        self.this = libpanda._inPUZN3tN2u(other.this)
        self.userManagesMemory = 1

    
    def _Mat3__overloaded_constructor_float_float_float_float_float_float_float_float_float(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
        self.this = libpanda._inPUZN3Qz8c(e00, e01, e02, e10, e11, e12, e20, e21, e22)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3s2pE:
            libpanda._inPUZN3s2pE(self.this)
        

    
    def identMat():
        returnValue = libpanda._inPUZN3r8vo()
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identMat = staticmethod(identMat)
    
    def _Mat3__overloaded_translateMat_ptrConstLVecBase2f(trans):
        returnValue = libpanda._inPUZN38Yv7(trans.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_translateMat_ptrConstLVecBase2f = staticmethod(_Mat3__overloaded_translateMat_ptrConstLVecBase2f)
    
    def _Mat3__overloaded_translateMat_float_float(tx, ty):
        returnValue = libpanda._inPUZN31aHR(tx, ty)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_translateMat_float_float = staticmethod(_Mat3__overloaded_translateMat_float_float)
    
    def _Mat3__overloaded_rotateMat_float(angle):
        returnValue = libpanda._inPUZN3wS2A(angle)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_rotateMat_float = staticmethod(_Mat3__overloaded_rotateMat_float)
    
    def _Mat3__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPUZN3zgNZ(angle, axis.this, cs)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat3__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem)
    
    def _Mat3__overloaded_rotateMat_float_ptrLVecBase3f(angle, axis):
        returnValue = libpanda._inPUZN3z0rv(angle, axis.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_rotateMat_float_ptrLVecBase3f = staticmethod(_Mat3__overloaded_rotateMat_float_ptrLVecBase3f)
    
    def _Mat3__overloaded_scaleMat_ptrConstLVecBase2f(scale):
        returnValue = libpanda._inPUZN3cF2k(scale.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleMat_ptrConstLVecBase2f = staticmethod(_Mat3__overloaded_scaleMat_ptrConstLVecBase2f)
    
    def _Mat3__overloaded_scaleMat_ptrConstLVecBase3f(scale):
        returnValue = libpanda._inPUZN3Op4k(scale.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleMat_ptrConstLVecBase3f = staticmethod(_Mat3__overloaded_scaleMat_ptrConstLVecBase3f)
    
    def _Mat3__overloaded_scaleMat_float_float(sx, sy):
        returnValue = libpanda._inPUZN3JKk6(sx, sy)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleMat_float_float = staticmethod(_Mat3__overloaded_scaleMat_float_float)
    
    def _Mat3__overloaded_scaleMat_float_float_float(sx, sy, sz):
        returnValue = libpanda._inPUZN3w6ng(sx, sy, sz)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleMat_float_float_float = staticmethod(_Mat3__overloaded_scaleMat_float_float_float)
    
    def _Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPUZN3Sl9G(angle, axis.this, cs)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem)
    
    def _Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(angle, axis):
        returnValue = libpanda._inPUZN3if2Z(angle, axis.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f = staticmethod(_Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f)
    
    def convertMat(_from, to):
        returnValue = libpanda._inPUZN3gv0p(_from, to)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    convertMat = staticmethod(convertMat)
    
    def getClassType():
        returnValue = libpanda._inPUZN3IXnT()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Mat3__overloaded_assign_ptrLMatrix3f_ptrConstLMatrix3f(self, other):
        returnValue = libpanda._inPUZN3WGVN(self.this, other.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat3__overloaded_assign_ptrLMatrix3f_float(self, fillValue):
        returnValue = libpanda._inPUZN3JZp_(self.this, fillValue)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def fill(self, fillValue):
        returnValue = libpanda._inPUZN3hH0z(self.this, fillValue)
        return returnValue

    
    def set(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
        returnValue = libpanda._inPUZN3z3qU(self.this, e00, e01, e02, e10, e11, e12, e20, e21, e22)
        return returnValue

    
    def _Mat3__overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase2f(self, row, v):
        returnValue = libpanda._inPUZN3K5w9(self.this, row, v.this)
        return returnValue

    
    def _Mat3__overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase3f(self, row, v):
        returnValue = libpanda._inPUZN355gf(self.this, row, v.this)
        return returnValue

    
    def _Mat3__overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase2f(self, col, v):
        returnValue = libpanda._inPUZN3vDEF(self.this, col, v.this)
        return returnValue

    
    def _Mat3__overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase3f(self, col, v):
        returnValue = libpanda._inPUZN3bc0m(self.this, col, v.this)
        return returnValue

    
    def _Mat3__overloaded_getRow_ptrConstLMatrix3f_ptrLVecBase3f_int(self, resultVec, row):
        returnValue = libpanda._inPUZN3dfDX(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat3__overloaded_getRow_ptrConstLMatrix3f_int(self, row):
        returnValue = libpanda._inPUZN3wROZ(self.this, row)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol(self, col):
        returnValue = libpanda._inPUZN3Cuhg(self.this, col)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRow2(self, row):
        returnValue = libpanda._inPUZN37qSI(self.this, row)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol2(self, col):
        returnValue = libpanda._inPUZN3WJmP(self.this, col)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat3__overloaded___call___ptrLMatrix3f_int_int(self, row, col):
        returnValue = libpanda._inPUZN3HBvR(self.this, row, col)
        return returnValue

    
    def _Mat3__overloaded___call___ptrConstLMatrix3f_int_int(self, row, col):
        returnValue = libpanda._inPUZN3_Fgz(self.this, row, col)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPUZN3R3pT(self.this)
        return returnValue

    
    def getCell(self, row, col):
        returnValue = libpanda._inPUZN3G4Zy(self.this, row, col)
        return returnValue

    
    def setCell(self, row, col, value):
        returnValue = libpanda._inPUZN3l0_H(self.this, row, col, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPUZN3WvxR(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPUZN3bMUR(self.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPUZN3uhzu(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPUZN3IQr_(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPUZN3IhJ3(self.this, other.this)
        return returnValue

    
    def _Mat3__overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f(self, other):
        returnValue = libpanda._inPUZN3FM0m(self.this, other.this)
        return returnValue

    
    def _Mat3__overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f_float(self, other, threshold):
        returnValue = libpanda._inPUZN3wCZj(self.this, other.this, threshold)
        return returnValue

    
    def xform(self, v):
        returnValue = libpanda._inPUZN3Gzw6(self.this, v.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformPoint(self, v):
        returnValue = libpanda._inPUZN3E0BQ(self.this, v.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformVec(self, v):
        returnValue = libpanda._inPUZN3I3MJ(self.this, v.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, other1, other2):
        returnValue = libpanda._inPUZN3RR6_(self.this, other1.this, other2.this)
        return returnValue

    
    def _Mat3__overloaded___mul___ptrConstLMatrix3f_ptrConstLMatrix3f(self, other):
        returnValue = libpanda._inPUZN3OBTp(self.this, other.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat3__overloaded___mul___ptrConstLMatrix3f_float(self, scalar):
        returnValue = libpanda._inPUZN3cFqV(self.this, scalar)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3MqMX(self.this, scalar)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def scaleMultiply(self, scaleVector, otherMat):
        returnValue = libpanda._inPUZN3s2_I(self.this, scaleVector.this, otherMat.this)
        return returnValue

    
    def __iadd__(self, other):
        returnValue = libpanda._inPUZN3E0iA(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPUZN3kIJB(self.this, other.this)
        return self

    
    def _Mat3__overloaded___imul___ptrLMatrix3f_ptrConstLMatrix3f(self, other):
        returnValue = libpanda._inPUZN30XOA(self.this, other.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat3__overloaded___imul___ptrLMatrix3f_float(self, scalar):
        returnValue = libpanda._inPUZN3NH5p(self.this, scalar)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPUZN3d8ar(self.this, scalar)
        return self

    
    def determinant(self):
        returnValue = libpanda._inPUZN33zlL(self.this)
        return returnValue

    
    def transposeFrom(self, other):
        returnValue = libpanda._inPUZN36S3s(self.this, other.this)
        return returnValue

    
    def transposeInPlace(self):
        returnValue = libpanda._inPUZN39Ojo(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPUZN3VKZ2(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPUZN3huLY(self.this)
        return returnValue

    
    def _Mat3__overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f(self, other):
        returnValue = libpanda._inPUZN35LZV(self.this, other.this)
        return returnValue

    
    def _Mat3__overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f_float(self, other, threshold):
        returnValue = libpanda._inPUZN3iSL6(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPUZN30E1n(self.this, out.this)
        return returnValue

    
    def _Mat3__overloaded_write_ptrConstLMatrix3f_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPUZN3xi6e(self.this, out.this, indentLevel)
        return returnValue

    
    def _Mat3__overloaded_write_ptrConstLMatrix3f_ptrOstream(self, out):
        returnValue = libpanda._inPUZN3s5Vo(self.this, out.this)
        return returnValue

    
    def scaleMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            import VBase2
            if isinstance(_args[0], VBase3.VBase3):
                return Mat3._Mat3__overloaded_scaleMat_ptrConstLVecBase3f(_args[0])
            elif isinstance(_args[0], VBase2.VBase2):
                return Mat3._Mat3__overloaded_scaleMat_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> <VBase2.VBase2> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return Mat3._Mat3__overloaded_scaleMat_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return Mat3._Mat3__overloaded_scaleMat_float_float_float(_args[0], _args[1], _args[2])
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
            import VBase2
            if isinstance(_args[0], VBase2.VBase2):
                return Mat3._Mat3__overloaded_translateMat_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2.VBase2> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return Mat3._Mat3__overloaded_translateMat_float_float(_args[0], _args[1])
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
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return Mat3._Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    if isinstance(_args[2], types.IntType):
                        return Mat3._Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    rotateMatNormaxis = staticmethod(rotateMatNormaxis)
    
    def rotateMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return Mat3._Mat3__overloaded_rotateMat_float(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return Mat3._Mat3__overloaded_rotateMat_float_ptrLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    if isinstance(_args[2], types.IntType):
                        return Mat3._Mat3__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    rotateMat = staticmethod(rotateMat)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat3__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], Mat3):
                return self._Mat3__overloaded_constructor_ptrConstLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3> '
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
                                                return self._Mat3__overloaded_constructor_float_float_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8])
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
                return self._Mat3__overloaded_write_ptrConstLMatrix3f_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._Mat3__overloaded_write_ptrConstLMatrix3f_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Mat3):
                return self._Mat3__overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3> '
        elif numArgs == 2:
            if isinstance(_args[0], Mat3):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Mat3__overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __imul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat3__overloaded___imul___ptrLMatrix3f_float(_args[0])
            elif isinstance(_args[0], Mat3):
                return self._Mat3__overloaded___imul___ptrLMatrix3f_ptrConstLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Mat3):
                return self._Mat3__overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3> '
        elif numArgs == 2:
            if isinstance(_args[0], Mat3):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Mat3__overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __call__(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._Mat3__overloaded___call___ptrConstLMatrix3f_int_int(_args[0], _args[1])
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
                import VBase3
                import VBase2
                if isinstance(_args[1], VBase3.VBase3):
                    return self._Mat3__overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase3f(_args[0], _args[1])
                elif isinstance(_args[1], VBase2.VBase2):
                    return self._Mat3__overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase2f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> <VBase2.VBase2> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def setCol(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3
                import VBase2
                if isinstance(_args[1], VBase3.VBase3):
                    return self._Mat3__overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase3f(_args[0], _args[1])
                elif isinstance(_args[1], VBase2.VBase2):
                    return self._Mat3__overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase2f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> <VBase2.VBase2> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat3__overloaded_assign_ptrLMatrix3f_float(_args[0])
            elif isinstance(_args[0], Mat3):
                return self._Mat3__overloaded_assign_ptrLMatrix3f_ptrConstLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def getRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._Mat3__overloaded_getRow_ptrConstLMatrix3f_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                if isinstance(_args[1], types.IntType):
                    return self._Mat3__overloaded_getRow_ptrConstLMatrix3f_ptrLVecBase3f_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Mat3__overloaded___mul___ptrConstLMatrix3f_float(_args[0])
            elif isinstance(_args[0], Mat3):
                return self._Mat3__overloaded___mul___ptrConstLMatrix3f_ptrConstLMatrix3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


