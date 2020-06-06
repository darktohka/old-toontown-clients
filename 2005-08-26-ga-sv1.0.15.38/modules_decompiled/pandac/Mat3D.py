# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class Mat3D(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Mat3D__overloaded_constructor(self):
        self.this = libpanda._inPVZN3HKtQ()
        self.userManagesMemory = 1

    
    def _Mat3D__overloaded_constructor_ptrConstLMatrix3d(self, other):
        self.this = libpanda._inPVZN3gwPr(other.this)
        self.userManagesMemory = 1

    
    def _Mat3D__overloaded_constructor_double_double_double_double_double_double_double_double_double(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
        self.this = libpanda._inPVZN31oPv(e00, e01, e02, e10, e11, e12, e20, e21, e22)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3VziA:
            libpanda._inPVZN3VziA(self.this)
        

    
    def identMat():
        returnValue = libpanda._inPVZN3D_Pl()
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    identMat = staticmethod(identMat)
    
    def _Mat3D__overloaded_translateMat_ptrConstLVecBase2d(trans):
        returnValue = libpanda._inPVZN3cpG4(trans.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_translateMat_ptrConstLVecBase2d = staticmethod(_Mat3D__overloaded_translateMat_ptrConstLVecBase2d)
    
    def _Mat3D__overloaded_translateMat_double_double(tx, ty):
        returnValue = libpanda._inPVZN3Zis7(tx, ty)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_translateMat_double_double = staticmethod(_Mat3D__overloaded_translateMat_double_double)
    
    def _Mat3D__overloaded_rotateMat_double(angle):
        returnValue = libpanda._inPVZN3B6hL(angle)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_rotateMat_double = staticmethod(_Mat3D__overloaded_rotateMat_double)
    
    def _Mat3D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPVZN3aFgZ(angle, axis.this, cs)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat3D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem)
    
    def _Mat3D__overloaded_rotateMat_double_ptrLVecBase3d(angle, axis):
        returnValue = libpanda._inPVZN3z6sm(angle, axis.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_rotateMat_double_ptrLVecBase3d = staticmethod(_Mat3D__overloaded_rotateMat_double_ptrLVecBase3d)
    
    def _Mat3D__overloaded_scaleMat_ptrConstLVecBase2d(scale):
        returnValue = libpanda._inPVZN3kw5e(scale.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleMat_ptrConstLVecBase2d = staticmethod(_Mat3D__overloaded_scaleMat_ptrConstLVecBase2d)
    
    def _Mat3D__overloaded_scaleMat_ptrConstLVecBase3d(scale):
        returnValue = libpanda._inPVZN32c8e(scale.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleMat_ptrConstLVecBase3d = staticmethod(_Mat3D__overloaded_scaleMat_ptrConstLVecBase3d)
    
    def _Mat3D__overloaded_scaleMat_double_double(sx, sy):
        returnValue = libpanda._inPVZN3KYtY(sx, sy)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleMat_double_double = staticmethod(_Mat3D__overloaded_scaleMat_double_double)
    
    def _Mat3D__overloaded_scaleMat_double_double_double(sx, sy, sz):
        returnValue = libpanda._inPVZN3XTVN(sx, sy, sz)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleMat_double_double_double = staticmethod(_Mat3D__overloaded_scaleMat_double_double_double)
    
    def _Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(angle, axis, cs):
        returnValue = libpanda._inPVZN3yh6r(angle, axis.this, cs)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem)
    
    def _Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(angle, axis):
        returnValue = libpanda._inPVZN3YlqF(angle, axis.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d = staticmethod(_Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d)
    
    def _Mat3D__overloaded_shearMat_ptrConstLVecBase3d___enum__CoordinateSystem(shear, cs):
        returnValue = libpanda._inPVZN3QoP8(shear.this, cs)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_shearMat_ptrConstLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat3D__overloaded_shearMat_ptrConstLVecBase3d___enum__CoordinateSystem)
    
    def _Mat3D__overloaded_shearMat_ptrConstLVecBase3d(shear):
        returnValue = libpanda._inPVZN3xJal(shear.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_shearMat_ptrConstLVecBase3d = staticmethod(_Mat3D__overloaded_shearMat_ptrConstLVecBase3d)
    
    def _Mat3D__overloaded_shearMat_double_double_double___enum__CoordinateSystem(shxy, shxz, shyz, cs):
        returnValue = libpanda._inPVZN31tYK(shxy, shxz, shyz, cs)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_shearMat_double_double_double___enum__CoordinateSystem = staticmethod(_Mat3D__overloaded_shearMat_double_double_double___enum__CoordinateSystem)
    
    def _Mat3D__overloaded_shearMat_double_double_double(shxy, shxz, shyz):
        returnValue = libpanda._inPVZN3n6zT(shxy, shxz, shyz)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_shearMat_double_double_double = staticmethod(_Mat3D__overloaded_shearMat_double_double_double)
    
    def _Mat3D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(scale, shear, cs):
        returnValue = libpanda._inPVZN3ipF0(scale.this, shear.this, cs)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem = staticmethod(_Mat3D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem)
    
    def _Mat3D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d(scale, shear):
        returnValue = libpanda._inPVZN3EtzN(scale.this, shear.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d = staticmethod(_Mat3D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d)
    
    def _Mat3D__overloaded_scaleShearMat_double_double_double_double_double_double___enum__CoordinateSystem(sx, sy, sz, shxy, shxz, shyz, cs):
        returnValue = libpanda._inPVZN3erao(sx, sy, sz, shxy, shxz, shyz, cs)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleShearMat_double_double_double_double_double_double___enum__CoordinateSystem = staticmethod(_Mat3D__overloaded_scaleShearMat_double_double_double_double_double_double___enum__CoordinateSystem)
    
    def _Mat3D__overloaded_scaleShearMat_double_double_double_double_double_double(sx, sy, sz, shxy, shxz, shyz):
        returnValue = libpanda._inPVZN3kqKC(sx, sy, sz, shxy, shxz, shyz)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Mat3D__overloaded_scaleShearMat_double_double_double_double_double_double = staticmethod(_Mat3D__overloaded_scaleShearMat_double_double_double_double_double_double)
    
    def convertMat(_from, to):
        returnValue = libpanda._inPVZN34uUm(_from, to)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    convertMat = staticmethod(convertMat)
    
    def getClassType():
        returnValue = libpanda._inPVZN3nXHQ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Mat3D__overloaded_assign_ptrLMatrix3d_ptrConstLMatrix3d(self, other):
        returnValue = libpanda._inPVZN39QZH(self.this, other.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat3D__overloaded_assign_ptrLMatrix3d_double(self, fillValue):
        returnValue = libpanda._inPVZN3ByUJ(self.this, fillValue)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def fill(self, fillValue):
        returnValue = libpanda._inPVZN3tMiW(self.this, fillValue)
        return returnValue

    
    def set(self, e00, e01, e02, e10, e11, e12, e20, e21, e22):
        returnValue = libpanda._inPVZN3YSjO(self.this, e00, e01, e02, e10, e11, e12, e20, e21, e22)
        return returnValue

    
    def _Mat3D__overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase2d(self, row, v):
        returnValue = libpanda._inPVZN3MjRK(self.this, row, v.this)
        return returnValue

    
    def _Mat3D__overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase3d(self, row, v):
        returnValue = libpanda._inPVZN37jBs(self.this, row, v.this)
        return returnValue

    
    def _Mat3D__overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase2d(self, col, v):
        returnValue = libpanda._inPVZN3hFlR(self.this, col, v.this)
        return returnValue

    
    def _Mat3D__overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase3d(self, col, v):
        returnValue = libpanda._inPVZN3cGVz(self.this, col, v.this)
        return returnValue

    
    def _Mat3D__overloaded_getRow_ptrConstLMatrix3d_ptrLVecBase3d_int(self, resultVec, row):
        returnValue = libpanda._inPVZN3FRjb(self.this, resultVec.this, row)
        return returnValue

    
    def _Mat3D__overloaded_getRow_ptrConstLMatrix3d_int(self, row):
        returnValue = libpanda._inPVZN3pQuV(self.this, row)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol(self, col):
        returnValue = libpanda._inPVZN3qvBd(self.this, col)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRow2(self, row):
        returnValue = libpanda._inPVZN3CqyE(self.this, row)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getCol2(self, col):
        returnValue = libpanda._inPVZN3xKGM(self.this, col)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat3D__overloaded___call___ptrLMatrix3d_int_int(self, row, col):
        returnValue = libpanda._inPVZN3YAPO(self.this, row, col)
        return returnValue

    
    def _Mat3D__overloaded___call___ptrConstLMatrix3d_int_int(self, row, col):
        returnValue = libpanda._inPVZN3nEAw(self.this, row, col)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPVZN3u3JQ(self.this)
        return returnValue

    
    def getCell(self, row, col):
        returnValue = libpanda._inPVZN3u75u(self.this, row, col)
        return returnValue

    
    def setCell(self, row, col, value):
        returnValue = libpanda._inPVZN3YWBO(self.this, row, col, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPVZN3tvRO(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPVZN3wP0N(self.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPVZN3Gv3o(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPVZN3RREu(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPVZN3Rgil(self.this, other.this)
        return returnValue

    
    def _Mat3D__overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d(self, other):
        returnValue = libpanda._inPVZN3t_3g(self.this, other.this)
        return returnValue

    
    def _Mat3D__overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d_double(self, other, threshold):
        returnValue = libpanda._inPVZN3Sbnp(self.this, other.this, threshold)
        return returnValue

    
    def _Mat3D__overloaded_getHash_ptrConstLMatrix3d(self):
        returnValue = libpanda._inPVZN3t7oj(self.this)
        return returnValue

    
    def _Mat3D__overloaded_getHash_ptrConstLMatrix3d_double(self, threshold):
        returnValue = libpanda._inPVZN3ACnK(self.this, threshold)
        return returnValue

    
    def _Mat3D__overloaded_addHash_ptrConstLMatrix3d_unsignedint(self, hash):
        returnValue = libpanda._inPVZN3QfHg(self.this, hash)
        return returnValue

    
    def _Mat3D__overloaded_addHash_ptrConstLMatrix3d_unsignedint_double(self, hash, threshold):
        returnValue = libpanda._inPVZN3e2a4(self.this, hash, threshold)
        return returnValue

    
    def xform(self, v):
        returnValue = libpanda._inPVZN3uQNQ(self.this, v.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformPoint(self, v):
        returnValue = libpanda._inPVZN3S1BJ(self.this, v.this)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xformVec(self, v):
        returnValue = libpanda._inPVZN3RGPD(self.this, v.this)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def multiply(self, other1, other2):
        returnValue = libpanda._inPVZN3Z5GD(self.this, other1.this, other2.this)
        return returnValue

    
    def _Mat3D__overloaded___mul___ptrConstLMatrix3d_ptrConstLMatrix3d(self, other):
        returnValue = libpanda._inPVZN3mPXj(self.this, other.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Mat3D__overloaded___mul___ptrConstLMatrix3d_double(self, scalar):
        returnValue = libpanda._inPVZN3_fQe(self.this, scalar)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3Ooxf(self.this, scalar)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPVZN3_07u(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPVZN3fIiv(self.this, other.this)
        return self

    
    def _Mat3D__overloaded___imul___ptrLMatrix3d_ptrConstLMatrix3d(self, other):
        returnValue = libpanda._inPVZN3PXnu(self.this, other.this)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Mat3D__overloaded___imul___ptrLMatrix3d_double(self, scalar):
        returnValue = libpanda._inPVZN3X0Qs(self.this, scalar)
        returnObject = Mat3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPVZN3ndyt(self.this, scalar)
        return self

    
    def determinant(self):
        returnValue = libpanda._inPVZN3syFI(self.this)
        return returnValue

    
    def transposeFrom(self, other):
        returnValue = libpanda._inPVZN3aONp(self.this, other.this)
        return returnValue

    
    def transposeInPlace(self):
        returnValue = libpanda._inPVZN3lPDl(self.this)
        return returnValue

    
    def invertFrom(self, other):
        returnValue = libpanda._inPVZN3MJyk(self.this, other.this)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPVZN3IurU(self.this)
        return returnValue

    
    def _Mat3D__overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d(self, other):
        returnValue = libpanda._inPVZN3rIZO(self.this, other.this)
        return returnValue

    
    def _Mat3D__overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d_double(self, other, threshold):
        returnValue = libpanda._inPVZN3pOQZ(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPVZN3cEVk(self.this, out.this)
        return returnValue

    
    def _Mat3D__overloaded_write_ptrConstLMatrix3d_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPVZN3Ihab(self.this, out.this, indentLevel)
        return returnValue

    
    def _Mat3D__overloaded_write_ptrConstLMatrix3d_ptrOstream(self, out):
        returnValue = libpanda._inPVZN3U41k(self.this, out.this)
        return returnValue

    
    def translateMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Mat3D._Mat3D__overloaded_translateMat_ptrConstLVecBase2d(*_args)
        elif numArgs == 2:
            return Mat3D._Mat3D__overloaded_translateMat_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    translateMat = staticmethod(translateMat)
    
    def shearMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Mat3D._Mat3D__overloaded_shearMat_ptrConstLVecBase3d(*_args)
        elif numArgs == 2:
            return Mat3D._Mat3D__overloaded_shearMat_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        elif numArgs == 3:
            return Mat3D._Mat3D__overloaded_shearMat_double_double_double(*_args)
        elif numArgs == 4:
            return Mat3D._Mat3D__overloaded_shearMat_double_double_double___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    shearMat = staticmethod(shearMat)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat3D__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._Mat3D__overloaded_constructor_ptrConstLMatrix3d(*_args)
        elif numArgs == 9:
            return self._Mat3D__overloaded_constructor_double_double_double_double_double_double_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 9 '

    
    def scaleMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return Mat3D._Mat3D__overloaded_scaleMat_ptrConstLVecBase3d(*_args)
            
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return Mat3D._Mat3D__overloaded_scaleMat_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <VBase2D.VBase2D> '
        elif numArgs == 2:
            return Mat3D._Mat3D__overloaded_scaleMat_double_double(*_args)
        elif numArgs == 3:
            return Mat3D._Mat3D__overloaded_scaleMat_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    scaleMat = staticmethod(scaleMat)
    
    def rotateMatNormaxis(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Mat3D._Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d(*_args)
        elif numArgs == 3:
            return Mat3D._Mat3D__overloaded_rotateMatNormaxis_double_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    rotateMatNormaxis = staticmethod(rotateMatNormaxis)
    
    def scaleShearMat(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            return Mat3D._Mat3D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        elif numArgs == 3:
            return Mat3D._Mat3D__overloaded_scaleShearMat_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        elif numArgs == 6:
            return Mat3D._Mat3D__overloaded_scaleShearMat_double_double_double_double_double_double(*_args)
        elif numArgs == 7:
            return Mat3D._Mat3D__overloaded_scaleShearMat_double_double_double_double_double_double___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 6 7 '

    scaleShearMat = staticmethod(scaleShearMat)
    
    def rotateMat(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return Mat3D._Mat3D__overloaded_rotateMat_double(*_args)
        elif numArgs == 2:
            return Mat3D._Mat3D__overloaded_rotateMat_double_ptrLVecBase3d(*_args)
        elif numArgs == 3:
            return Mat3D._Mat3D__overloaded_rotateMat_double_ptrLVecBase3d___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '

    rotateMat = staticmethod(rotateMat)
    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat3D__overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d(*_args)
        elif numArgs == 2:
            return self._Mat3D__overloaded_almostEqual_ptrConstLMatrix3d_ptrConstLMatrix3d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __imul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat3D__overloaded___imul___ptrLMatrix3d_double(*_args)
            
            if isinstance(_args[0], Mat3D):
                return self._Mat3D__overloaded___imul___ptrLMatrix3d_ptrConstLMatrix3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat3D__overloaded_addHash_ptrConstLMatrix3d_unsignedint(*_args)
        elif numArgs == 2:
            return self._Mat3D__overloaded_addHash_ptrConstLMatrix3d_unsignedint_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat3D__overloaded_getRow_ptrConstLMatrix3d_int(*_args)
        elif numArgs == 2:
            return self._Mat3D__overloaded_getRow_ptrConstLMatrix3d_ptrLVecBase3d_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat3D__overloaded_write_ptrConstLMatrix3d_ptrOstream(*_args)
        elif numArgs == 2:
            return self._Mat3D__overloaded_write_ptrConstLMatrix3d_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCol(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return self._Mat3D__overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase3d(*_args)
                
                import VBase2D
                if isinstance(_args[1], VBase2D.VBase2D):
                    return self._Mat3D__overloaded_setCol_ptrLMatrix3d_int_ptrConstLVecBase2d(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> <VBase2D.VBase2D> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def getHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Mat3D__overloaded_getHash_ptrConstLMatrix3d(*_args)
        elif numArgs == 1:
            return self._Mat3D__overloaded_getHash_ptrConstLMatrix3d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat3D__overloaded___mul___ptrConstLMatrix3d_double(*_args)
            
            if isinstance(_args[0], Mat3D):
                return self._Mat3D__overloaded___mul___ptrConstLMatrix3d_ptrConstLMatrix3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Mat3D__overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d(*_args)
        elif numArgs == 2:
            return self._Mat3D__overloaded_compareTo_ptrConstLMatrix3d_ptrConstLMatrix3d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __call__(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._Mat3D__overloaded___call___ptrConstLMatrix3d_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def setRow(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                import VBase3D
                if isinstance(_args[1], VBase3D.VBase3D):
                    return self._Mat3D__overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase3d(*_args)
                
                import VBase2D
                if isinstance(_args[1], VBase2D.VBase2D):
                    return self._Mat3D__overloaded_setRow_ptrLMatrix3d_int_ptrConstLVecBase2d(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> <VBase2D.VBase2D> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Mat3D__overloaded_assign_ptrLMatrix3d_double(*_args)
            
            if isinstance(_args[0], Mat3D):
                return self._Mat3D__overloaded_assign_ptrLMatrix3d_ptrConstLMatrix3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


