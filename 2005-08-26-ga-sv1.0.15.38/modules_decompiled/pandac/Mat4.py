# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class Mat4(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Mat4__overloaded_constructor(self):
        self.this = libpanda._inPVZN30VSC()
        self.userManagesMemory = 1

    
    def _Mat4__overloaded_constructor_ptrConstLMatrix3f(self, upper3):
        self.this = libpanda._inPVZN3fs5c(upper3.this)
        self.userManagesMemory = 1

    
    def _Mat4__overloaded_constructor_ptrConstLMatrix3f_ptrConstLVecBase3f(self, upper3, trans):
        self.this = libpanda._inPVZN36_z9(upper3.this, trans.this)
        self.userManagesMemory = 1

    
    def _Mat4__overloaded_constructor_ptrConstLMatrix4f(self, other):
        self.this = libpanda._inPVZN3X354(other.this)
        self.userManagesMemory = 1

    
    def _Mat4__overloaded_constructor_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
        self.this = libpanda._inPVZN3kfiq(e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN37ZvL:
            libpanda._inPVZN37ZvL(self.this)
        

    
    def identMat():
        returnValue = libpanda._inPVZN3rczP()
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identMat = staticmethod(identMat)
    
    def _Mat4__overloaded_translateMat_ptrConstLVecBase3f(trans):
        returnValue = libpanda._inPVZN3jyza(trans.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_translateMat_ptrConstLVecBase3f = staticmethod(_Mat4__overloaded_translateMat_ptrConstLVecBase3f)
    
    def _Mat4__overloaded_translateMat_float_float_float(tx, ty, tz):
        returnValue = libpanda._inPVZN3Q9hS(tx, ty, tz)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_translateMat_float_float_float = staticmethod(_Mat4__overloaded_translateMat_float_float_float)
    
    def _Mat4__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPVZN38AQA(angle, axis.this, cs)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat4__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem)
    
    def _Mat4__overloaded_rotateMat_float_ptrLVecBase3f(angle, axis):
        returnValue = libpanda._inPVZN3zUuW(angle, axis.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_rotateMat_float_ptrLVecBase3f = staticmethod(_Mat4__overloaded_rotateMat_float_ptrLVecBase3f)
    
    def _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPVZN3SFBu(angle, axis.this, cs)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem)
    
    def _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(angle, axis):
        returnValue = libpanda._inPVZN3l_5A(angle, axis.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f = staticmethod(_Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f)
    
    def _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem(angle, axis, resultMat, cs):
        returnValue = libpanda._inPVZN3R71s(angle, axis.this, resultMat.this, cs)
        return returnValue

    _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem = staticmethod(_Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem)
    
    def _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f(angle, axis, resultMat):
        returnValue = libpanda._inPVZN3QMA0(angle, axis.this, resultMat.this)
        return returnValue

    _Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f = staticmethod(_Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f)
    
    def _Mat4__overloaded_scaleMat_ptrConstLVecBase3f(scale):
        returnValue = libpanda._inPVZN3OJ8L(scale.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_scaleMat_ptrConstLVecBase3f = staticmethod(_Mat4__overloaded_scaleMat_ptrConstLVecBase3f)
    
    def _Mat4__overloaded_scaleMat_float(scale):
        returnValue = libpanda._inPVZN3gj9H(scale)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_scaleMat_float = staticmethod(_Mat4__overloaded_scaleMat_float)
    
    def _Mat4__overloaded_scaleMat_float_float_float(sx, sy, sz):
        returnValue = libpanda._inPVZN3waqH(sx, sy, sz)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_scaleMat_float_float_float = staticmethod(_Mat4__overloaded_scaleMat_float_float_float)
    
    def _Mat4__overloaded_shearMat_ptrConstLVecBase3f___enum__CoordinateSystem(shear, cs):
        returnValue = libpanda._inPVZN346Pp(shear.this, cs)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_shearMat_ptrConstLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat4__overloaded_shearMat_ptrConstLVecBase3f___enum__CoordinateSystem)
    
    def _Mat4__overloaded_shearMat_ptrConstLVecBase3f(shear):
        returnValue = libpanda._inPVZN3J0aS(shear.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_shearMat_ptrConstLVecBase3f = staticmethod(_Mat4__overloaded_shearMat_ptrConstLVecBase3f)
    
    def _Mat4__overloaded_shearMat_float_float_float___enum__CoordinateSystem(shxy, shxz, shyz, cs):
        returnValue = libpanda._inPVZN3lQ9A(shxy, shxz, shyz, cs)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_shearMat_float_float_float___enum__CoordinateSystem = staticmethod(_Mat4__overloaded_shearMat_float_float_float___enum__CoordinateSystem)
    
    def _Mat4__overloaded_shearMat_float_float_float(shxy, shxz, shyz):
        returnValue = libpanda._inPVZN3xxJO(shxy, shxz, shyz)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_shearMat_float_float_float = staticmethod(_Mat4__overloaded_shearMat_float_float_float)
    
    def _Mat4__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(scale, shear, cs):
        returnValue = libpanda._inPVZN3al56(scale.this, shear.this, cs)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem = staticmethod(_Mat4__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem)
    
    def _Mat4__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f(scale, shear):
        returnValue = libpanda._inPVZN3gpnU(scale.this, shear.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f = staticmethod(_Mat4__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f)
    
    def _Mat4__overloaded_scaleShearMat_float_float_float_float_float_float___enum__CoordinateSystem(sx, sy, sz, shxy, shxz, shyz, cs):
        returnValue = libpanda._inPVZN39lik(sx, sy, sz, shxy, shxz, shyz, cs)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_scaleShearMat_float_float_float_float_float_float___enum__CoordinateSystem = staticmethod(_Mat4__overloaded_scaleShearMat_float_float_float_float_float_float___enum__CoordinateSystem)
    
    def _Mat4__overloaded_scaleShearMat_float_float_float_float_float_float(sx, sy, sz, shxy, shxz, shyz):
        returnValue = libpanda._inPVZN3i__t(sx, sy, sz, shxy, shxz, shyz)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4__overloaded_scaleShearMat_float_float_float_float_float_float = staticmethod(_Mat4__overloaded_scaleShearMat_float_float_float_float_float_float)
    
    def yToZUpMat():
        returnValue = libpanda._inPVZN3lIST()
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    yToZUpMat = staticmethod(yToZUpMat)
    
    def zToYUpMat():
        returnValue = libpanda._inPVZN3lG2Q()
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zToYUpMat = staticmethod(zToYUpMat)
    
    def convertMat(_from, to):
        returnValue = libpanda._inPVZN3gP4Q(_from, to)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    convertMat = staticmethod(convertMat)
    
    def getClassType():
        returnValue = libpanda._inPVZN3I3r6()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Mat4__overloaded_assign_ptrLMatrix4f_ptrConstLMatrix4f(self, other):
        returnValue = libpanda._inPVZN3kLb0(self.this, other.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat4__overloaded_assign_ptrLMatrix4f_float(self, fillValue):
        returnValue = libpanda._inPVZN3J5tl(self.this, fillValue)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def fill(self, fillValue):
        returnValue = libpanda._inPVZN3hn3a(self.this, fillValue)
        return returnValue

    
    def set(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
        returnValue = libpanda._inPVZN3b_Gk(self.this, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
        return returnValue

    
    def setUpper3(self, upper3):
        returnValue = libpanda._inPVZN3QITa(self.this, upper3.this)
        return returnValue

    
    def getUpper3(self):
        returnValue = libpanda._inPVZN31ZhQ(self.this)
        import Mat3
        returnObject = Mat3.Mat3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4__overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase3f(self, row, v):
        returnValue = libpanda._inPVZN32ZkG(self.this, row, v.this)
        return returnValue

    
    def _Mat4__overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase4f(self, row, v):
        returnValue = libpanda._inPVZN3lZUo(self.this, row, v.this)
        return returnValue

    
    def _Mat4__overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase3f(self, col, v):
        returnValue = libpanda._inPVZN3b83N(self.this, col, v.this)
        return returnValue

    
    def _Mat4__overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase4f(self, col, v):
        returnValue = libpanda._inPVZN328nv(self.this, col, v.this)
        return returnValue

    
    def _Mat4__overloaded_getRow_ptrConstLMatrix4f_ptrLVecBase4f_int(self, resultVec, row):
        returnValue = libpanda._inPVZN3n__u(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat4__overloaded_getRow_ptrConstLMatrix4f_int(self, row):
        returnValue = libpanda._inPVZN3xxRA(self.this, row)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol(self, col):
        returnValue = libpanda._inPVZN3COlH(self.this, col)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4__overloaded_getRow3_ptrConstLMatrix4f_ptrLVecBase3f_int(self, resultVec, row):
        returnValue = libpanda._inPVZN3dF7x(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat4__overloaded_getRow3_ptrConstLMatrix4f_int(self, row):
        returnValue = libpanda._inPVZN3JMW2(self.this, row)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol3(self, col):
        returnValue = libpanda._inPVZN3kop9(self.this, col)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4__overloaded___call___ptrLMatrix4f_int_int(self, row, col):
        returnValue = libpanda._inPVZN3Hhy4(self.this, row, col)
        return returnValue

    
    def _Mat4__overloaded___call___ptrConstLMatrix4f_int_int(self, row, col):
        returnValue = libpanda._inPVZN3_lka(self.this, row, col)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPVZN3RXs6(self.this)
        return returnValue

    
    def getCell(self, row, col):
        returnValue = libpanda._inPVZN3GYcZ(self.this, row, col)
        return returnValue

    
    def setCell(self, row, col, value):
        returnValue = libpanda._inPVZN3lUBv(self.this, row, col, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPVZN3WP14(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPVZN3bsX4(self.this)
        return returnValue

    
    def _Mat4__overloaded_begin_ptrLMatrix4f(self):
        returnValue = libpanda._inPVZN3KK3S(self.this)
        return returnValue

    
    def _Mat4__overloaded_begin_ptrConstLMatrix4f(self):
        returnValue = libpanda._inPVZN3BQDa(self.this)
        return returnValue

    
    def _Mat4__overloaded_end_ptrLMatrix4f(self):
        returnValue = libpanda._inPVZN3m_kL(self.this)
        return returnValue

    
    def _Mat4__overloaded_end_ptrConstLMatrix4f(self):
        returnValue = libpanda._inPVZN3gxNr(self.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPVZN38l5V(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPVZN3I59n(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPVZN3IOaf(self.this, other.this)
        return returnValue

    
    def _Mat4__overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f(self, other):
        returnValue = libpanda._inPVZN3zB6N(self.this, other.this)
        return returnValue

    
    def _Mat4__overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f_float(self, other, threshold):
        returnValue = libpanda._inPVZN3mOfK(self.this, other.this, threshold)
        return returnValue

    
    def _Mat4__overloaded_getHash_ptrConstLMatrix4f(self):
        returnValue = libpanda._inPVZN3VYMO(self.this)
        return returnValue

    
    def _Mat4__overloaded_getHash_ptrConstLMatrix4f_float(self, threshold):
        returnValue = libpanda._inPVZN3FcZg(self.this, threshold)
        return returnValue

    
    def _Mat4__overloaded_addHash_ptrConstLMatrix4f_unsignedint(self, hash):
        returnValue = libpanda._inPVZN3o8oK(self.this, hash)
        return returnValue

    
    def _Mat4__overloaded_addHash_ptrConstLMatrix4f_unsignedint_float(self, hash, threshold):
        returnValue = libpanda._inPVZN3JGyd(self.this, hash, threshold)
        return returnValue

    
    def xform(self, v):
        returnValue = libpanda._inPVZN3mWbi(self.this, v.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformPoint(self, v):
        returnValue = libpanda._inPVZN3F0Ie(self.this, v.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformVec(self, v):
        returnValue = libpanda._inPVZN3a7Sw(self.this, v.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, other1, other2):
        returnValue = libpanda._inPVZN3cv3G(self.this, other1.this, other2.this)
        return returnValue

    
    def _Mat4__overloaded___mul___ptrConstLMatrix4f_ptrConstLMatrix4f(self, other):
        returnValue = libpanda._inPVZN3cFZQ(self.this, other.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4__overloaded___mul___ptrConstLMatrix4f_float(self, scalar):
        returnValue = libpanda._inPVZN3clu8(self.this, scalar)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3MKP_(self.this, scalar)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPVZN3Ev0o(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPVZN3kjbp(self.this, other.this)
        return self

    
    def _Mat4__overloaded___imul___ptrLMatrix4f_ptrConstLMatrix4f(self, other):
        returnValue = libpanda._inPVZN30Ogo(self.this, other.this)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat4__overloaded___imul___ptrLMatrix4f_float(self, scalar):
        returnValue = libpanda._inPVZN3Nn8Q(self.this, scalar)
        returnObject = Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPVZN3dceS(self.this, scalar)
        return self

    
    def transposeFrom(self, other):
        returnValue = libpanda._inPVZN3rI6L(self.this, other.this)
        return returnValue

    
    def transposeInPlace(self):
        returnValue = libpanda._inPVZN39umP(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPVZN3Vtqe(self.this, other.this)
        return returnValue

    
    def invertAffineFrom(self, other):
        returnValue = libpanda._inPVZN3KvHn(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPVZN3hOP_(self.this)
        return returnValue

    
    def _Mat4__overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f(self, other):
        returnValue = libpanda._inPVZN34Lgj(self.this, other.this)
        return returnValue

    
    def _Mat4__overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f_float(self, other, threshold):
        returnValue = libpanda._inPVZN39SSI(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPVZN30k4O(self.this, out.this)
        return returnValue

    
    def _Mat4__overloaded_write_ptrConstLMatrix4f_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPVZN3wC_F(self.this, out.this, indentLevel)
        return returnValue

    
    def _Mat4__overloaded_write_ptrConstLMatrix4f_ptrOstream(self, out):
        returnValue = libpanda._inPVZN3sZZP(self.this, out.this)
        return returnValue

    
    def scaleMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return Mat4._Mat4__overloaded_scaleMat_float(*_args)
            
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return Mat4._Mat4__overloaded_scaleMat_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        elif numArgs == 3:
            return Mat4._Mat4__overloaded_scaleMat_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    scaleMat = staticmethod(scaleMat)
    
    def shearMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Mat4._Mat4__overloaded_shearMat_ptrConstLVecBase3f(*_args)
        elif numArgs == 2:
            return Mat4._Mat4__overloaded_shearMat_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        elif numArgs == 3:
            return Mat4._Mat4__overloaded_shearMat_float_float_float(*_args)
        elif numArgs == 4:
            return Mat4._Mat4__overloaded_shearMat_float_float_float___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    shearMat = staticmethod(shearMat)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], Mat4):
                return self._Mat4__overloaded_constructor_ptrConstLMatrix4f(*_args)
            
            import Mat3
            if isinstance(_args[0], Mat3.Mat3):
                return self._Mat4__overloaded_constructor_ptrConstLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4> <Mat3.Mat3> '
        elif numArgs == 2:
            return self._Mat4__overloaded_constructor_ptrConstLMatrix3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 16:
            return self._Mat4__overloaded_constructor_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 16 '

    
    def translateMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Mat4._Mat4__overloaded_translateMat_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return Mat4._Mat4__overloaded_translateMat_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    translateMat = staticmethod(translateMat)
    
    def rotateMatNormaxis(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Mat4._Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                        return Mat4._Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
                    
                    if isinstance(_args[2], Mat4):
                        return Mat4._Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f(*_args)
                    
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Mat4> '
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            return Mat4._Mat4__overloaded_rotateMatNormaxis_float_ptrConstLVecBase3f_ptrLMatrix4f___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '

    rotateMatNormaxis = staticmethod(rotateMatNormaxis)
    
    def scaleShearMat(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Mat4._Mat4__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return Mat4._Mat4__overloaded_scaleShearMat_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        elif numArgs == 6:
            return Mat4._Mat4__overloaded_scaleShearMat_float_float_float_float_float_float(*_args)
        elif numArgs == 7:
            return Mat4._Mat4__overloaded_scaleShearMat_float_float_float_float_float_float___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 6 7 '

    scaleShearMat = staticmethod(scaleShearMat)
    
    def rotateMat(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Mat4._Mat4__overloaded_rotateMat_float_ptrLVecBase3f(*_args)
        elif numArgs == 3:
            return Mat4._Mat4__overloaded_rotateMat_float_ptrLVecBase3f___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    rotateMat = staticmethod(rotateMat)
    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4__overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f(*_args)
        elif numArgs == 2:
            return self._Mat4__overloaded_almostEqual_ptrConstLMatrix4f_ptrConstLMatrix4f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def begin(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4__overloaded_begin_ptrConstLMatrix4f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def end(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4__overloaded_end_ptrConstLMatrix4f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def __imul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat4__overloaded___imul___ptrLMatrix4f_float(*_args)
            
            if isinstance(_args[0], Mat4):
                return self._Mat4__overloaded___imul___ptrLMatrix4f_ptrConstLMatrix4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4__overloaded_addHash_ptrConstLMatrix4f_unsignedint(*_args)
        elif numArgs == 2:
            return self._Mat4__overloaded_addHash_ptrConstLMatrix4f_unsignedint_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getRow3(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4__overloaded_getRow3_ptrConstLMatrix4f_int(*_args)
        elif numArgs == 2:
            return self._Mat4__overloaded_getRow3_ptrConstLMatrix4f_ptrLVecBase3f_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4__overloaded_getRow_ptrConstLMatrix4f_int(*_args)
        elif numArgs == 2:
            return self._Mat4__overloaded_getRow_ptrConstLMatrix4f_ptrLVecBase4f_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4__overloaded_write_ptrConstLMatrix4f_ptrOstream(*_args)
        elif numArgs == 2:
            return self._Mat4__overloaded_write_ptrConstLMatrix4f_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCol(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase4
                if isinstance(_args[1], VBase4.VBase4):
                    return self._Mat4__overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase4f(*_args)
                
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._Mat4__overloaded_setCol_ptrLMatrix4f_int_ptrConstLVecBase3f(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def getHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4__overloaded_getHash_ptrConstLMatrix4f(*_args)
        elif numArgs == 1:
            return self._Mat4__overloaded_getHash_ptrConstLMatrix4f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat4__overloaded___mul___ptrConstLMatrix4f_float(*_args)
            
            if isinstance(_args[0], Mat4):
                return self._Mat4__overloaded___mul___ptrConstLMatrix4f_ptrConstLMatrix4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4__overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f(*_args)
        elif numArgs == 2:
            return self._Mat4__overloaded_compareTo_ptrConstLMatrix4f_ptrConstLMatrix4f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __call__(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._Mat4__overloaded___call___ptrConstLMatrix4f_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def setRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase4
                if isinstance(_args[1], VBase4.VBase4):
                    return self._Mat4__overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase4f(*_args)
                
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._Mat4__overloaded_setRow_ptrLMatrix4f_int_ptrConstLVecBase3f(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat4__overloaded_assign_ptrLMatrix4f_float(*_args)
            
            if isinstance(_args[0], Mat4):
                return self._Mat4__overloaded_assign_ptrLMatrix4f_ptrConstLMatrix4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


