# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class Mat3(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Mat3__overloaded_constructor(self):
        self.this = libpanda._inPVZN3l0PU()
        self.userManagesMemory = 1

    
    def _Mat3__overloaded_constructor_ptrConstLMatrix3f(self, other):
        self.this = libpanda._inPVZN3sN2u(other.this)
        self.userManagesMemory = 1

    
    def _Mat3__overloaded_constructor_float_float_float_float_float_float_float_float_float(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
        self.this = libpanda._inPVZN3Qz8c(e00, e01, e02, e10, e11, e12, e20, e21, e22)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3s2pE:
            libpanda._inPVZN3s2pE(self.this)
        

    
    def identMat():
        returnValue = libpanda._inPVZN3q8vo()
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identMat = staticmethod(identMat)
    
    def _Mat3__overloaded_translateMat_ptrConstLVecBase2f(trans):
        returnValue = libpanda._inPVZN39Yv7(trans.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_translateMat_ptrConstLVecBase2f = staticmethod(_Mat3__overloaded_translateMat_ptrConstLVecBase2f)
    
    def _Mat3__overloaded_translateMat_float_float(tx, ty):
        returnValue = libpanda._inPVZN31aHR(tx, ty)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_translateMat_float_float = staticmethod(_Mat3__overloaded_translateMat_float_float)
    
    def _Mat3__overloaded_rotateMat_float(angle):
        returnValue = libpanda._inPVZN3wS2A(angle)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_rotateMat_float = staticmethod(_Mat3__overloaded_rotateMat_float)
    
    def _Mat3__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPVZN3zgNZ(angle, axis.this, cs)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat3__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem)
    
    def _Mat3__overloaded_rotateMat_float_ptrLVecBase3f(angle, axis):
        returnValue = libpanda._inPVZN3y0rv(angle, axis.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_rotateMat_float_ptrLVecBase3f = staticmethod(_Mat3__overloaded_rotateMat_float_ptrLVecBase3f)
    
    def _Mat3__overloaded_scaleMat_ptrConstLVecBase2f(scale):
        returnValue = libpanda._inPVZN3fF2k(scale.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleMat_ptrConstLVecBase2f = staticmethod(_Mat3__overloaded_scaleMat_ptrConstLVecBase2f)
    
    def _Mat3__overloaded_scaleMat_ptrConstLVecBase3f(scale):
        returnValue = libpanda._inPVZN3Np4k(scale.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleMat_ptrConstLVecBase3f = staticmethod(_Mat3__overloaded_scaleMat_ptrConstLVecBase3f)
    
    def _Mat3__overloaded_scaleMat_float_float(sx, sy):
        returnValue = libpanda._inPVZN3KKk6(sx, sy)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleMat_float_float = staticmethod(_Mat3__overloaded_scaleMat_float_float)
    
    def _Mat3__overloaded_scaleMat_float_float_float(sx, sy, sz):
        returnValue = libpanda._inPVZN3x6ng(sx, sy, sz)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleMat_float_float_float = staticmethod(_Mat3__overloaded_scaleMat_float_float_float)
    
    def _Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPVZN3Sl9G(angle, axis.this, cs)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem)
    
    def _Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(angle, axis):
        returnValue = libpanda._inPVZN3if2Z(angle, axis.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f = staticmethod(_Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f)
    
    def _Mat3__overloaded_shearMat_ptrConstLVecBase3f___enum__CoordinateSystem(shear, cs):
        returnValue = libpanda._inPVZN34aMC(shear.this, cs)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_shearMat_ptrConstLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat3__overloaded_shearMat_ptrConstLVecBase3f___enum__CoordinateSystem)
    
    def _Mat3__overloaded_shearMat_ptrConstLVecBase3f(shear):
        returnValue = libpanda._inPVZN3KUWr(shear.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_shearMat_ptrConstLVecBase3f = staticmethod(_Mat3__overloaded_shearMat_ptrConstLVecBase3f)
    
    def _Mat3__overloaded_shearMat_float_float_float___enum__CoordinateSystem(shxy, shxz, shyz, cs):
        returnValue = libpanda._inPVZN3iw5Z(shxy, shxz, shyz, cs)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_shearMat_float_float_float___enum__CoordinateSystem = staticmethod(_Mat3__overloaded_shearMat_float_float_float___enum__CoordinateSystem)
    
    def _Mat3__overloaded_shearMat_float_float_float(shxy, shxz, shyz):
        returnValue = libpanda._inPVZN3wRFn(shxy, shxz, shyz)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_shearMat_float_float_float = staticmethod(_Mat3__overloaded_shearMat_float_float_float)
    
    def _Mat3__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(scale, shear, cs):
        returnValue = libpanda._inPVZN3aF0T(scale.this, shear.this, cs)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat3__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem)
    
    def _Mat3__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f(scale, shear):
        returnValue = libpanda._inPVZN3_Jjt(scale.this, shear.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f = staticmethod(_Mat3__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f)
    
    def _Mat3__overloaded_scaleShearMat_float_float_float_float_float_float___enum__CoordinateSystem(sx, sy, sz, shxy, shxz, shyz, cs):
        returnValue = libpanda._inPVZN3iFf9(sx, sy, sz, shxy, shxz, shyz, cs)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleShearMat_float_float_float_float_float_float___enum__CoordinateSystem = staticmethod(_Mat3__overloaded_scaleShearMat_float_float_float_float_float_float___enum__CoordinateSystem)
    
    def _Mat3__overloaded_scaleShearMat_float_float_float_float_float_float(sx, sy, sz, shxy, shxz, shyz):
        returnValue = libpanda._inPVZN3ie6G(sx, sy, sz, shxy, shxz, shyz)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3__overloaded_scaleShearMat_float_float_float_float_float_float = staticmethod(_Mat3__overloaded_scaleShearMat_float_float_float_float_float_float)
    
    def convertMat(_from, to):
        returnValue = libpanda._inPVZN3jv0p(_from, to)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    convertMat = staticmethod(convertMat)
    
    def getClassType():
        returnValue = libpanda._inPVZN3IXnT()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Mat3__overloaded_assign_ptrLMatrix3f_ptrConstLMatrix3f(self, other):
        returnValue = libpanda._inPVZN3WGVN(self.this, other.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat3__overloaded_assign_ptrLMatrix3f_float(self, fillValue):
        returnValue = libpanda._inPVZN3OZp_(self.this, fillValue)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def fill(self, fillValue):
        returnValue = libpanda._inPVZN3gH0z(self.this, fillValue)
        return returnValue

    
    def set(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
        returnValue = libpanda._inPVZN3z3qU(self.this, e00, e01, e02, e10, e11, e12, e20, e21, e22)
        return returnValue

    
    def _Mat3__overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase2f(self, row, v):
        returnValue = libpanda._inPVZN3N5w9(self.this, row, v.this)
        return returnValue

    
    def _Mat3__overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase3f(self, row, v):
        returnValue = libpanda._inPVZN355gf(self.this, row, v.this)
        return returnValue

    
    def _Mat3__overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase2f(self, col, v):
        returnValue = libpanda._inPVZN3vDEF(self.this, col, v.this)
        return returnValue

    
    def _Mat3__overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase3f(self, col, v):
        returnValue = libpanda._inPVZN3ac0m(self.this, col, v.this)
        return returnValue

    
    def _Mat3__overloaded_getRow_ptrConstLMatrix3f_ptrLVecBase3f_int(self, resultVec, row):
        returnValue = libpanda._inPVZN3dfDX(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat3__overloaded_getRow_ptrConstLMatrix3f_int(self, row):
        returnValue = libpanda._inPVZN3wROZ(self.this, row)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol(self, col):
        returnValue = libpanda._inPVZN3Fuhg(self.this, col)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRow2(self, row):
        returnValue = libpanda._inPVZN37qSI(self.this, row)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol2(self, col):
        returnValue = libpanda._inPVZN3WJmP(self.this, col)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat3__overloaded___call___ptrLMatrix3f_int_int(self, row, col):
        returnValue = libpanda._inPVZN3HBvR(self.this, row, col)
        return returnValue

    
    def _Mat3__overloaded___call___ptrConstLMatrix3f_int_int(self, row, col):
        returnValue = libpanda._inPVZN3_Fgz(self.this, row, col)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPVZN3R3pT(self.this)
        return returnValue

    
    def getCell(self, row, col):
        returnValue = libpanda._inPVZN3H4Zy(self.this, row, col)
        return returnValue

    
    def setCell(self, row, col, value):
        returnValue = libpanda._inPVZN3l0_H(self.this, row, col, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPVZN3WvxR(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPVZN3bMUR(self.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPVZN3vhzu(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPVZN3JQr_(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPVZN3JhJ3(self.this, other.this)
        return returnValue

    
    def _Mat3__overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f(self, other):
        returnValue = libpanda._inPVZN3KM0m(self.this, other.this)
        return returnValue

    
    def _Mat3__overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f_float(self, other, threshold):
        returnValue = libpanda._inPVZN3xCZj(self.this, other.this, threshold)
        return returnValue

    
    def _Mat3__overloaded_getHash_ptrConstLMatrix3f(self):
        returnValue = libpanda._inPVZN3W4In(self.this)
        return returnValue

    
    def _Mat3__overloaded_getHash_ptrConstLMatrix3f_float(self, threshold):
        returnValue = libpanda._inPVZN3G8W5(self.this, threshold)
        return returnValue

    
    def _Mat3__overloaded_addHash_ptrConstLMatrix3f_unsignedint(self, hash):
        returnValue = libpanda._inPVZN3pcnj(self.this, hash)
        return returnValue

    
    def _Mat3__overloaded_addHash_ptrConstLMatrix3f_unsignedint_float(self, hash, threshold):
        returnValue = libpanda._inPVZN3Gmv2(self.this, hash, threshold)
        return returnValue

    
    def xform(self, v):
        returnValue = libpanda._inPVZN3Hzw6(self.this, v.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformPoint(self, v):
        returnValue = libpanda._inPVZN3E0BQ(self.this, v.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformVec(self, v):
        returnValue = libpanda._inPVZN3I3MJ(self.this, v.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, other1, other2):
        returnValue = libpanda._inPVZN3SR6_(self.this, other1.this, other2.this)
        return returnValue

    
    def _Mat3__overloaded___mul___ptrConstLMatrix3f_ptrConstLMatrix3f(self, other):
        returnValue = libpanda._inPVZN3PBTp(self.this, other.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat3__overloaded___mul___ptrConstLMatrix3f_float(self, scalar):
        returnValue = libpanda._inPVZN3cFqV(self.this, scalar)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3MqMX(self.this, scalar)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPVZN3E0iA(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPVZN3kIJB(self.this, other.this)
        return self

    
    def _Mat3__overloaded___imul___ptrLMatrix3f_ptrConstLMatrix3f(self, other):
        returnValue = libpanda._inPVZN30XOA(self.this, other.this)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat3__overloaded___imul___ptrLMatrix3f_float(self, scalar):
        returnValue = libpanda._inPVZN3MH5p(self.this, scalar)
        returnObject = Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPVZN3c8ar(self.this, scalar)
        return self

    
    def determinant(self):
        returnValue = libpanda._inPVZN33zlL(self.this)
        return returnValue

    
    def transposeFrom(self, other):
        returnValue = libpanda._inPVZN3lS3s(self.this, other.this)
        return returnValue

    
    def transposeInPlace(self):
        returnValue = libpanda._inPVZN38Ojo(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPVZN3UKZ2(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPVZN3huLY(self.this)
        return returnValue

    
    def _Mat3__overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f(self, other):
        returnValue = libpanda._inPVZN35LZV(self.this, other.this)
        return returnValue

    
    def _Mat3__overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f_float(self, other, threshold):
        returnValue = libpanda._inPVZN3jSL6(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPVZN3zE1n(self.this, out.this)
        return returnValue

    
    def _Mat3__overloaded_write_ptrConstLMatrix3f_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPVZN3xi6e(self.this, out.this, indentLevel)
        return returnValue

    
    def _Mat3__overloaded_write_ptrConstLMatrix3f_ptrOstream(self, out):
        returnValue = libpanda._inPVZN3t5Vo(self.this, out.this)
        return returnValue

    
    def translateMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Mat3._Mat3__overloaded_translateMat_ptrConstLVecBase2f(*_args)
        elif numArgs == 2:
            return Mat3._Mat3__overloaded_translateMat_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    translateMat = staticmethod(translateMat)
    
    def shearMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Mat3._Mat3__overloaded_shearMat_ptrConstLVecBase3f(*_args)
        elif numArgs == 2:
            return Mat3._Mat3__overloaded_shearMat_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        elif numArgs == 3:
            return Mat3._Mat3__overloaded_shearMat_float_float_float(*_args)
        elif numArgs == 4:
            return Mat3._Mat3__overloaded_shearMat_float_float_float___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    shearMat = staticmethod(shearMat)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat3__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._Mat3__overloaded_constructor_ptrConstLMatrix3f(*_args)
        elif numArgs == 9:
            return self._Mat3__overloaded_constructor_float_float_float_float_float_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 9 '

    
    def scaleMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return Mat3._Mat3__overloaded_scaleMat_ptrConstLVecBase3f(*_args)
            
            import VBase2
            if isinstance(_args[0], VBase2.VBase2):
                return Mat3._Mat3__overloaded_scaleMat_ptrConstLVecBase2f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> <VBase2.VBase2> '
        elif numArgs == 2:
            return Mat3._Mat3__overloaded_scaleMat_float_float(*_args)
        elif numArgs == 3:
            return Mat3._Mat3__overloaded_scaleMat_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    scaleMat = staticmethod(scaleMat)
    
    def rotateMatNormaxis(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Mat3._Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return Mat3._Mat3__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    rotateMatNormaxis = staticmethod(rotateMatNormaxis)
    
    def scaleShearMat(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Mat3._Mat3__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return Mat3._Mat3__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        elif numArgs == 6:
            return Mat3._Mat3__overloaded_scaleShearMat_float_float_float_float_float_float(*_args)
        elif numArgs == 7:
            return Mat3._Mat3__overloaded_scaleShearMat_float_float_float_float_float_float___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 6 7 '

    scaleShearMat = staticmethod(scaleShearMat)
    
    def rotateMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Mat3._Mat3__overloaded_rotateMat_float(*_args)
        elif numArgs == 2:
            return Mat3._Mat3__overloaded_rotateMat_float_ptrLVecBase3f(*_args)
        elif numArgs == 3:
            return Mat3._Mat3__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    rotateMat = staticmethod(rotateMat)
    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat3__overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f(*_args)
        elif numArgs == 2:
            return self._Mat3__overloaded_almostEqual_ptrConstLMatrix3f_ptrConstLMatrix3f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __imul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat3__overloaded___imul___ptrLMatrix3f_float(*_args)
            
            if isinstance(_args[0], Mat3):
                return self._Mat3__overloaded___imul___ptrLMatrix3f_ptrConstLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat3__overloaded_addHash_ptrConstLMatrix3f_unsignedint(*_args)
        elif numArgs == 2:
            return self._Mat3__overloaded_addHash_ptrConstLMatrix3f_unsignedint_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat3__overloaded_getRow_ptrConstLMatrix3f_int(*_args)
        elif numArgs == 2:
            return self._Mat3__overloaded_getRow_ptrConstLMatrix3f_ptrLVecBase3f_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat3__overloaded_write_ptrConstLMatrix3f_ptrOstream(*_args)
        elif numArgs == 2:
            return self._Mat3__overloaded_write_ptrConstLMatrix3f_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCol(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._Mat3__overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase3f(*_args)
                
                import VBase2
                if isinstance(_args[1], VBase2.VBase2):
                    return self._Mat3__overloaded_setCol_ptrLMatrix3f_int_ptrConstLVecBase2f(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> <VBase2.VBase2> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def getHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat3__overloaded_getHash_ptrConstLMatrix3f(*_args)
        elif numArgs == 1:
            return self._Mat3__overloaded_getHash_ptrConstLMatrix3f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat3__overloaded___mul___ptrConstLMatrix3f_float(*_args)
            
            if isinstance(_args[0], Mat3):
                return self._Mat3__overloaded___mul___ptrConstLMatrix3f_ptrConstLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat3__overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f(*_args)
        elif numArgs == 2:
            return self._Mat3__overloaded_compareTo_ptrConstLMatrix3f_ptrConstLMatrix3f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __call__(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._Mat3__overloaded___call___ptrConstLMatrix3f_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def setRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._Mat3__overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase3f(*_args)
                
                import VBase2
                if isinstance(_args[1], VBase2.VBase2):
                    return self._Mat3__overloaded_setRow_ptrLMatrix3f_int_ptrConstLVecBase2f(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> <VBase2.VBase2> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat3__overloaded_assign_ptrLMatrix3f_float(*_args)
            
            if isinstance(_args[0], Mat3):
                return self._Mat3__overloaded_assign_ptrLMatrix3f_ptrConstLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __repr__(self):
        return '%s(\n%s,\n%s,\n%s)' % (self.__class__.__name__, self.getRow(0).pPrintValues(), self.getRow(1).pPrintValues(), self.getRow(2).pPrintValues())

    
    def pPrintValues(self):
        return '\n%s\n%s\n%s' % (self.getRow(0).pPrintValues(), self.getRow(1).pPrintValues(), self.getRow(2).pPrintValues())


