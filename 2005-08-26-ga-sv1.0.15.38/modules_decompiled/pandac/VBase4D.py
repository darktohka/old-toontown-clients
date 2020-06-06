# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class VBase4D(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _VBase4D__overloaded_constructor(self):
        self.this = libpanda._inPVZN3fAuU()
        self.userManagesMemory = 1

    
    def _VBase4D__overloaded_constructor_ptrConstLVecBase4d(self, copy):
        self.this = libpanda._inPVZN3KfrW(copy.this)
        self.userManagesMemory = 1

    
    def _VBase4D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPVZN35BJ_(fillValue)
        self.userManagesMemory = 1

    
    def _VBase4D__overloaded_constructor_double_double_double_double(self, x, y, z, w):
        self.this = libpanda._inPVZN3GENf(x, y, z, w)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3E_ND:
            libpanda._inPVZN3E_ND(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN3YrPj()
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3QxFH()
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3SxTj()
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPVZN3sxh_()
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def unitW():
        returnValue = libpanda._inPVZN3Vx3q()
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitW = staticmethod(unitW)
    
    def getClassType():
        returnValue = libpanda._inPVZN3GAvT()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase4D__overloaded_assign_ptrLVecBase4d_ptrConstLVecBase4d(self, copy):
        returnValue = libpanda._inPVZN3e6iS(self.this, copy.this)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase4D__overloaded_assign_ptrLVecBase4d_double(self, fillValue):
        returnValue = libpanda._inPVZN3IM_5(self.this, fillValue)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase4D__overloaded___getitem___ptrLVecBase4d_int(self, i):
        returnValue = libpanda._inPVZN3mm3I(self.this, i)
        return returnValue

    
    def _VBase4D__overloaded___getitem___ptrConstLVecBase4d_int(self, i):
        returnValue = libpanda._inPVZN31Hrl(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPVZN3Pu2T(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPVZN3_qP5(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPVZN3rtvk(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPVZN3rJop(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPVZN3rlgu(self.this)
        return returnValue

    
    def getW(self):
        returnValue = libpanda._inPVZN3rx3f(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPVZN3f_AA(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPVZN3jGFc(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPVZN3ji9g(self.this, value)
        return returnValue

    
    def setZ(self, value):
        returnValue = libpanda._inPVZN3je2l(self.this, value)
        return returnValue

    
    def setW(self, value):
        returnValue = libpanda._inPVZN3jqMX(self.this, value)
        return returnValue

    
    def addToCell(self, i, value):
        returnValue = libpanda._inPVZN3fMae(self.this, i, value)
        return returnValue

    
    def addX(self, value):
        returnValue = libpanda._inPVZN3ARia(self.this, value)
        return returnValue

    
    def addY(self, value):
        returnValue = libpanda._inPVZN3A1af(self.this, value)
        return returnValue

    
    def addZ(self, value):
        returnValue = libpanda._inPVZN3AZTk(self.this, value)
        return returnValue

    
    def addW(self, value):
        returnValue = libpanda._inPVZN3ANqV(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPVZN3x8zX(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPVZN3Xx2K(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPVZN3FbMg(self.this, fillValue)
        return returnValue

    
    def set(self, x, y, z, w):
        returnValue = libpanda._inPVZN3dT7O(self.this, x, y, z, w)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPVZN3VfrF(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPVZN3zfP_(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPVZN3eFYT(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPVZN3alAC(self.this, other.this)
        return returnValue

    
    def _VBase4D__overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d(self, other):
        returnValue = libpanda._inPVZN30LH_(self.this, other.this)
        return returnValue

    
    def _VBase4D__overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d_double(self, other, threshold):
        returnValue = libpanda._inPVZN3319I(self.this, other.this, threshold)
        return returnValue

    
    def _VBase4D__overloaded_getHash_ptrConstLVecBase4d(self):
        returnValue = libpanda._inPVZN38_ZE(self.this)
        return returnValue

    
    def _VBase4D__overloaded_getHash_ptrConstLVecBase4d_double(self, threshold):
        returnValue = libpanda._inPVZN3SwXj(self.this, threshold)
        return returnValue

    
    def _VBase4D__overloaded_addHash_ptrConstLVecBase4d_unsignedint(self, hash):
        returnValue = libpanda._inPVZN3JoPT(self.this, hash)
        return returnValue

    
    def _VBase4D__overloaded_addHash_ptrConstLVecBase4d_unsignedint_double(self, hash, threshold):
        returnValue = libpanda._inPVZN3XZGe(self.this, hash, threshold)
        return returnValue

    
    def _VBase4D__overloaded___sub___ptrConstLVecBase4d(self):
        returnValue = libpanda._inPVZN3QyvB(self.this)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase4D__overloaded___sub___ptrConstLVecBase4d_ptrConstLVecBase4d(self, other):
        returnValue = libpanda._inPVZN3tnyr(self.this, other.this)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPVZN3tXQY(self.this, other.this)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN3W_WY(self.this, scalar)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3XWNJ(self.this, scalar)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPVZN3hw2z(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPVZN3iAYH(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPVZN35DXY(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPVZN3_7LJ(self.this, scalar)
        return self

    
    def _VBase4D__overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d(self, other):
        returnValue = libpanda._inPVZN3coqw(self.this, other.this)
        return returnValue

    
    def _VBase4D__overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d_double(self, other, threshold):
        returnValue = libpanda._inPVZN39ILB(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPVZN31Bda(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase4D__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase4D__overloaded_constructor_double(*_args)
            
            if isinstance(_args[0], VBase4D):
                return self._VBase4D__overloaded_constructor_ptrConstLVecBase4d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D> '
        elif numArgs == 4:
            return self._VBase4D__overloaded_constructor_double_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 4 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase4D__overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d(*_args)
        elif numArgs == 2:
            return self._VBase4D__overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase4D__overloaded_getHash_ptrConstLVecBase4d(*_args)
        elif numArgs == 1:
            return self._VBase4D__overloaded_getHash_ptrConstLVecBase4d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase4D__overloaded___getitem___ptrConstLVecBase4d_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase4D__overloaded_addHash_ptrConstLVecBase4d_unsignedint(*_args)
        elif numArgs == 2:
            return self._VBase4D__overloaded_addHash_ptrConstLVecBase4d_unsignedint_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase4D__overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d(*_args)
        elif numArgs == 2:
            return self._VBase4D__overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase4D__overloaded___sub___ptrConstLVecBase4d(*_args)
        elif numArgs == 1:
            return self._VBase4D__overloaded___sub___ptrConstLVecBase4d_ptrConstLVecBase4d(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase4D__overloaded_assign_ptrLVecBase4d_double(*_args)
            
            if isinstance(_args[0], VBase4D):
                return self._VBase4D__overloaded_assign_ptrLVecBase4d_ptrConstLVecBase4d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


