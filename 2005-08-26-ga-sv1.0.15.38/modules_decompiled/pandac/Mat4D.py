# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class Mat4D(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Mat4D__overloaded_constructor(self):
        self.this = libpanda._inPVZN3Vrx_()
        self.userManagesMemory = 1

    
    def _Mat4D__overloaded_constructor_ptrConstLMatrix3d(self, upper3):
        self.this = libpanda._inPVZN3RSTZ(upper3.this)
        self.userManagesMemory = 1

    
    def _Mat4D__overloaded_constructor_ptrConstLMatrix3d_ptrConstLVecBase3d(self, upper3, trans):
        self.this = libpanda._inPVZN3y2xB(upper3.this, trans.this)
        self.userManagesMemory = 1

    
    def _Mat4D__overloaded_constructor_ptrConstLMatrix4d(self, other):
        self.this = libpanda._inPVZN3pOT1(other.this)
        self.userManagesMemory = 1

    
    def _Mat4D__overloaded_constructor_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
        self.this = libpanda._inPVZN3LfZS(e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3yVmH:
            libpanda._inPVZN3yVmH(self.this)
        

    
    def identMat():
        returnValue = libpanda._inPVZN3AfTM()
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identMat = staticmethod(identMat)
    
    def _Mat4D__overloaded_translateMat_ptrConstLVecBase3d(trans):
        returnValue = libpanda._inPVZN3SDJX(trans.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_translateMat_ptrConstLVecBase3d = staticmethod(_Mat4D__overloaded_translateMat_ptrConstLVecBase3d)
    
    def _Mat4D__overloaded_translateMat_double_double_double(tx, ty, tz):
        returnValue = libpanda._inPVZN3tfAu(tx, ty, tz)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_translateMat_double_double_double = staticmethod(_Mat4D__overloaded_translateMat_double_double_double)
    
    def _Mat4D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPVZN3blkA(angle, axis.this, cs)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat4D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem)
    
    def _Mat4D__overloaded_rotateMat_double_ptrLVecBase3d(angle, axis):
        returnValue = libpanda._inPVZN3yawN(angle, axis.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_rotateMat_double_ptrLVecBase3d = staticmethod(_Mat4D__overloaded_rotateMat_double_ptrLVecBase3d)
    
    def _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPVZN39B_S(angle, axis.this, cs)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem)
    
    def _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(angle, axis):
        returnValue = libpanda._inPVZN3YFts(angle, axis.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d = staticmethod(_Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d)
    
    def _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem(angle, axis, resultMat, cs):
        returnValue = libpanda._inPVZN375kn(angle, axis.this, resultMat.this, cs)
        return returnValue

    _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem = staticmethod(_Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem)
    
    def _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d(angle, axis, resultMat):
        returnValue = libpanda._inPVZN3u6SM(angle, axis.this, resultMat.this)
        return returnValue

    _Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d = staticmethod(_Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d)
    
    def _Mat4D__overloaded_scaleMat_ptrConstLVecBase3d(scale):
        returnValue = libpanda._inPVZN338_F(scale.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_scaleMat_ptrConstLVecBase3d = staticmethod(_Mat4D__overloaded_scaleMat_ptrConstLVecBase3d)
    
    def _Mat4D__overloaded_scaleMat_double(scale):
        returnValue = libpanda._inPVZN3H84Q(scale)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_scaleMat_double = staticmethod(_Mat4D__overloaded_scaleMat_double)
    
    def _Mat4D__overloaded_scaleMat_double_double_double(sx, sy, sz):
        returnValue = libpanda._inPVZN3XzZ0(sx, sy, sz)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_scaleMat_double_double_double = staticmethod(_Mat4D__overloaded_scaleMat_double_double_double)
    
    def _Mat4D__overloaded_shearMat_ptrConstLVecBase3d___enum__CoordinateSystem(shear, cs):
        returnValue = libpanda._inPVZN3fITj(shear.this, cs)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_shearMat_ptrConstLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat4D__overloaded_shearMat_ptrConstLVecBase3d___enum__CoordinateSystem)
    
    def _Mat4D__overloaded_shearMat_ptrConstLVecBase3d(shear):
        returnValue = libpanda._inPVZN3wpeM(shear.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_shearMat_ptrConstLVecBase3d = staticmethod(_Mat4D__overloaded_shearMat_ptrConstLVecBase3d)
    
    def _Mat4D__overloaded_shearMat_double_double_double___enum__CoordinateSystem(shxy, shxz, shyz, cs):
        returnValue = libpanda._inPVZN31Nbx(shxy, shxz, shyz, cs)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_shearMat_double_double_double___enum__CoordinateSystem = staticmethod(_Mat4D__overloaded_shearMat_double_double_double___enum__CoordinateSystem)
    
    def _Mat4D__overloaded_shearMat_double_double_double(shxy, shxz, shyz):
        returnValue = libpanda._inPVZN3na36(shxy, shxz, shyz)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_shearMat_double_double_double = staticmethod(_Mat4D__overloaded_shearMat_double_double_double)
    
    def _Mat4D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(scale, shear, cs):
        returnValue = libpanda._inPVZN3jJJb(scale.this, shear.this, cs)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat4D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem)
    
    def _Mat4D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d(scale, shear):
        returnValue = libpanda._inPVZN3EN20(scale.this, shear.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d = staticmethod(_Mat4D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d)
    
    def _Mat4D__overloaded_scaleShearMat_double_double_double_double_double_double___enum__CoordinateSystem(sx, sy, sz, shxy, shxz, shyz, cs):
        returnValue = libpanda._inPVZN3fLeP(sx, sy, sz, shxy, shxz, shyz, cs)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_scaleShearMat_double_double_double_double_double_double___enum__CoordinateSystem = staticmethod(_Mat4D__overloaded_scaleShearMat_double_double_double_double_double_double___enum__CoordinateSystem)
    
    def _Mat4D__overloaded_scaleShearMat_double_double_double_double_double_double(sx, sy, sz, shxy, shxz, shyz):
        returnValue = libpanda._inPVZN3kKNp(sx, sy, sz, shxy, shxz, shyz)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat4D__overloaded_scaleShearMat_double_double_double_double_double_double = staticmethod(_Mat4D__overloaded_scaleShearMat_double_double_double_double_double_double)
    
    def yToZUpMat():
        returnValue = libpanda._inPVZN3MIyP()
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    yToZUpMat = staticmethod(yToZUpMat)
    
    def zToYUpMat():
        returnValue = libpanda._inPVZN3MGWN()
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zToYUpMat = staticmethod(zToYUpMat)
    
    def convertMat(_from, to):
        returnValue = libpanda._inPVZN35OYN(_from, to)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    convertMat = staticmethod(convertMat)
    
    def getClassType():
        returnValue = libpanda._inPVZN3n3L3()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Mat4D__overloaded_assign_ptrLMatrix4d_ptrConstLMatrix4d(self, other):
        returnValue = libpanda._inPVZN3PVfu(self.this, other.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat4D__overloaded_assign_ptrLMatrix4d_double(self, fillValue):
        returnValue = libpanda._inPVZN3BSXw(self.this, fillValue)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def fill(self, fillValue):
        returnValue = libpanda._inPVZN3tsm9(self.this, fillValue)
        return returnValue

    
    def set(self, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33):
        returnValue = libpanda._inPVZN3E5Uz(self.this, e00, e01, e02, e03, e10, e11, e12, e13, e20, e21, e22, e23, e30, e31, e32, e33)
        return returnValue

    
    def setUpper3(self, upper3):
        returnValue = libpanda._inPVZN34JsI(self.this, upper3.this)
        return returnValue

    
    def getUpper3(self):
        returnValue = libpanda._inPVZN3cZBN(self.this)
        import Mat3D
        returnObject = Mat3D.Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4D__overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase3d(self, row, v):
        returnValue = libpanda._inPVZN34DFT(self.this, row, v.this)
        return returnValue

    
    def _Mat4D__overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase4d(self, row, v):
        returnValue = libpanda._inPVZN3nD10(self.this, row, v.this)
        return returnValue

    
    def _Mat4D__overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase3d(self, col, v):
        returnValue = libpanda._inPVZN3dmWa(self.this, col, v.this)
        return returnValue

    
    def _Mat4D__overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase4d(self, col, v):
        returnValue = libpanda._inPVZN3ImG8(self.this, col, v.this)
        return returnValue

    
    def _Mat4D__overloaded_getRow_ptrConstLMatrix4d_ptrLVecBase4d_int(self, resultVec, row):
        returnValue = libpanda._inPVZN3Pxez(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat4D__overloaded_getRow_ptrConstLMatrix4d_int(self, row):
        returnValue = libpanda._inPVZN3pwx8(self.this, row)
        import VBase4D
        returnObject = VBase4D.VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol(self, col):
        returnValue = libpanda._inPVZN3rPFE(self.this, col)
        import VBase4D
        returnObject = VBase4D.VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4D__overloaded_getRow3_ptrConstLMatrix4d_ptrLVecBase3d_int(self, resultVec, row):
        returnValue = libpanda._inPVZN3eTWu(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat4D__overloaded_getRow3_ptrConstLMatrix4d_int(self, row):
        returnValue = libpanda._inPVZN3QL2y(self.this, row)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol3(self, col):
        returnValue = libpanda._inPVZN3_pJ6(self.this, col)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4D__overloaded___call___ptrLMatrix4d_int_int(self, row, col):
        returnValue = libpanda._inPVZN3YgS1(self.this, row, col)
        return returnValue

    
    def _Mat4D__overloaded___call___ptrConstLMatrix4d_int_int(self, row, col):
        returnValue = libpanda._inPVZN3gkEX(self.this, row, col)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPVZN3uXM3(self.this)
        return returnValue

    
    def getCell(self, row, col):
        returnValue = libpanda._inPVZN3tb8V(self.this, row, col)
        return returnValue

    
    def setCell(self, row, col, value):
        returnValue = libpanda._inPVZN3Y2F1(self.this, row, col, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPVZN3tPV1(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPVZN3wv30(self.this)
        return returnValue

    
    def _Mat4D__overloaded_begin_ptrLMatrix4d(self):
        returnValue = libpanda._inPVZN3jKXP(self.this)
        return returnValue

    
    def _Mat4D__overloaded_begin_ptrConstLMatrix4d(self):
        returnValue = libpanda._inPVZN3mQjW(self.this)
        return returnValue

    
    def _Mat4D__overloaded_end_ptrLMatrix4d(self):
        returnValue = libpanda._inPVZN3PBFI(self.this)
        return returnValue

    
    def _Mat4D__overloaded_end_ptrConstLMatrix4d(self):
        returnValue = libpanda._inPVZN35wtn(self.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPVZN3Xz9P(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPVZN3Q4WW(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPVZN3QPzN(self.this, other.this)
        return returnValue

    
    def _Mat4D__overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d(self, other):
        returnValue = libpanda._inPVZN3az9H(self.this, other.this)
        return returnValue

    
    def _Mat4D__overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d_double(self, other, threshold):
        returnValue = libpanda._inPVZN3lGtQ(self.this, other.this, threshold)
        return returnValue

    
    def _Mat4D__overloaded_getHash_ptrConstLMatrix4d(self):
        returnValue = libpanda._inPVZN3sbsK(self.this)
        return returnValue

    
    def _Mat4D__overloaded_getHash_ptrConstLMatrix4d_double(self, threshold):
        returnValue = libpanda._inPVZN3Aiqx(self.this, threshold)
        return returnValue

    
    def _Mat4D__overloaded_addHash_ptrConstLMatrix4d_unsignedint(self, hash):
        returnValue = libpanda._inPVZN3T_IH(self.this, hash)
        return returnValue

    
    def _Mat4D__overloaded_addHash_ptrConstLMatrix4d_unsignedint_double(self, hash, threshold):
        returnValue = libpanda._inPVZN3dWef(self.this, hash, threshold)
        return returnValue

    
    def xform(self, v):
        returnValue = libpanda._inPVZN3O133(self.this, v.this)
        import VBase4D
        returnObject = VBase4D.VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformPoint(self, v):
        returnValue = libpanda._inPVZN3T1IX(self.this, v.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformVec(self, v):
        returnValue = libpanda._inPVZN3DCVq(self.this, v.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, other1, other2):
        returnValue = libpanda._inPVZN3U8DL(self.this, other1.this, other2.this)
        return returnValue

    
    def _Mat4D__overloaded___mul___ptrConstLMatrix4d_ptrConstLMatrix4d(self, other):
        returnValue = libpanda._inPVZN33TdK(self.this, other.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat4D__overloaded___mul___ptrConstLMatrix4d_double(self, scalar):
        returnValue = libpanda._inPVZN39_TF(self.this, scalar)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3NI1G(self.this, scalar)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPVZN38vNX(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPVZN3cj0X(self.this, other.this)
        return self

    
    def _Mat4D__overloaded___imul___ptrLMatrix4d_ptrConstLMatrix4d(self, other):
        returnValue = libpanda._inPVZN3MO5W(self.this, other.this)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat4D__overloaded___imul___ptrLMatrix4d_double(self, scalar):
        returnValue = libpanda._inPVZN3WUUT(self.this, scalar)
        returnObject = Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPVZN3m93U(self.this, scalar)
        return self

    
    def transposeFrom(self, other):
        returnValue = libpanda._inPVZN3oYQI(self.this, other.this)
        return returnValue

    
    def transposeInPlace(self):
        returnValue = libpanda._inPVZN3ivGM(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPVZN3NuDN(self.this, other.this)
        return returnValue

    
    def invertAffineFrom(self, other):
        returnValue = libpanda._inPVZN3g2mD(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPVZN3IOv7(self.this)
        return returnValue

    
    def _Mat4D__overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d(self, other):
        returnValue = libpanda._inPVZN3qIgc(self.this, other.this)
        return returnValue

    
    def _Mat4D__overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d_double(self, other, threshold):
        returnValue = libpanda._inPVZN3oOXn(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPVZN3dkYL(self.this, out.this)
        return returnValue

    
    def _Mat4D__overloaded_write_ptrConstLMatrix4d_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPVZN3XBeC(self.this, out.this, indentLevel)
        return returnValue

    
    def _Mat4D__overloaded_write_ptrConstLMatrix4d_ptrOstream(self, out):
        returnValue = libpanda._inPVZN3XY5L(self.this, out.this)
        return returnValue

    
    def scaleMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return Mat4D._Mat4D__overloaded_scaleMat_double(*_args)
            
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return Mat4D._Mat4D__overloaded_scaleMat_ptrConstLVecBase3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
        elif numArgs == 3:
            return Mat4D._Mat4D__overloaded_scaleMat_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    scaleMat = staticmethod(scaleMat)
    
    def shearMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Mat4D._Mat4D__overloaded_shearMat_ptrConstLVecBase3d(*_args)
        elif numArgs == 2:
            return Mat4D._Mat4D__overloaded_shearMat_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        elif numArgs == 3:
            return Mat4D._Mat4D__overloaded_shearMat_double_double_double(*_args)
        elif numArgs == 4:
            return Mat4D._Mat4D__overloaded_shearMat_double_double_double___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    shearMat = staticmethod(shearMat)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4D__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], Mat4D):
                return self._Mat4D__overloaded_constructor_ptrConstLMatrix4d(*_args)
            
            import Mat3D
            if isinstance(_args[0], Mat3D.Mat3D):
                return self._Mat4D__overloaded_constructor_ptrConstLMatrix3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D> <Mat3D.Mat3D> '
        elif numArgs == 2:
            return self._Mat4D__overloaded_constructor_ptrConstLMatrix3d_ptrConstLVecBase3d(*_args)
        elif numArgs == 16:
            return self._Mat4D__overloaded_constructor_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 16 '

    
    def translateMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Mat4D._Mat4D__overloaded_translateMat_ptrConstLVecBase3d(*_args)
        elif numArgs == 3:
            return Mat4D._Mat4D__overloaded_translateMat_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    translateMat = staticmethod(translateMat)
    
    def rotateMatNormaxis(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Mat4D._Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(*_args)
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                        return Mat4D._Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
                    
                    if isinstance(_args[2], Mat4D):
                        return Mat4D._Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d(*_args)
                    
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Mat4D> '
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            return Mat4D._Mat4D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d_ptrLMatrix4d___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '

    rotateMatNormaxis = staticmethod(rotateMatNormaxis)
    
    def scaleShearMat(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Mat4D._Mat4D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        elif numArgs == 3:
            return Mat4D._Mat4D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        elif numArgs == 6:
            return Mat4D._Mat4D__overloaded_scaleShearMat_double_double_double_double_double_double(*_args)
        elif numArgs == 7:
            return Mat4D._Mat4D__overloaded_scaleShearMat_double_double_double_double_double_double___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 6 7 '

    scaleShearMat = staticmethod(scaleShearMat)
    
    def rotateMat(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Mat4D._Mat4D__overloaded_rotateMat_double_ptrLVecBase3d(*_args)
        elif numArgs == 3:
            return Mat4D._Mat4D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    rotateMat = staticmethod(rotateMat)
    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4D__overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d(*_args)
        elif numArgs == 2:
            return self._Mat4D__overloaded_almostEqual_ptrConstLMatrix4d_ptrConstLMatrix4d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def begin(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4D__overloaded_begin_ptrConstLMatrix4d(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def end(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4D__overloaded_end_ptrConstLMatrix4d(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def __imul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat4D__overloaded___imul___ptrLMatrix4d_double(*_args)
            
            if isinstance(_args[0], Mat4D):
                return self._Mat4D__overloaded___imul___ptrLMatrix4d_ptrConstLMatrix4d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4D__overloaded_addHash_ptrConstLMatrix4d_unsignedint(*_args)
        elif numArgs == 2:
            return self._Mat4D__overloaded_addHash_ptrConstLMatrix4d_unsignedint_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getRow3(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4D__overloaded_getRow3_ptrConstLMatrix4d_int(*_args)
        elif numArgs == 2:
            return self._Mat4D__overloaded_getRow3_ptrConstLMatrix4d_ptrLVecBase3d_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4D__overloaded_getRow_ptrConstLMatrix4d_int(*_args)
        elif numArgs == 2:
            return self._Mat4D__overloaded_getRow_ptrConstLMatrix4d_ptrLVecBase4d_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4D__overloaded_write_ptrConstLMatrix4d_ptrOstream(*_args)
        elif numArgs == 2:
            return self._Mat4D__overloaded_write_ptrConstLMatrix4d_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCol(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase4D
                if isinstance(_args[1], VBase4D.VBase4D):
                    return self._Mat4D__overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase4d(*_args)
                
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return self._Mat4D__overloaded_setCol_ptrLMatrix4d_int_ptrConstLVecBase3d(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase4D.VBase4D> <VBase3D.VBase3D> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def getHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat4D__overloaded_getHash_ptrConstLMatrix4d(*_args)
        elif numArgs == 1:
            return self._Mat4D__overloaded_getHash_ptrConstLMatrix4d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat4D__overloaded___mul___ptrConstLMatrix4d_double(*_args)
            
            if isinstance(_args[0], Mat4D):
                return self._Mat4D__overloaded___mul___ptrConstLMatrix4d_ptrConstLMatrix4d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat4D__overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d(*_args)
        elif numArgs == 2:
            return self._Mat4D__overloaded_compareTo_ptrConstLMatrix4d_ptrConstLMatrix4d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __call__(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._Mat4D__overloaded___call___ptrConstLMatrix4d_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def setRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase4D
                if isinstance(_args[1], VBase4D.VBase4D):
                    return self._Mat4D__overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase4d(*_args)
                
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return self._Mat4D__overloaded_setRow_ptrLMatrix4d_int_ptrConstLVecBase3d(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase4D.VBase4D> <VBase3D.VBase3D> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat4D__overloaded_assign_ptrLMatrix4d_double(*_args)
            
            if isinstance(_args[0], Mat4D):
                return self._Mat4D__overloaded_assign_ptrLMatrix4d_ptrConstLMatrix4d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


