# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class VBase3D(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _VBase3D__overloaded_constructor(self):
        self.this = libpanda._inPVZN3jiry()
        self.userManagesMemory = 1

    
    def _VBase3D__overloaded_constructor_ptrConstLVecBase3d(self, copy):
        self.this = libpanda._inPVZN3uakN(copy.this)
        self.userManagesMemory = 1

    
    def _VBase3D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPVZN3_fFc(fillValue)
        self.userManagesMemory = 1

    
    def _VBase3D__overloaded_constructor_double_double_double(self, x, y, z):
        self.this = libpanda._inPVZN3pccq(x, y, z)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3wwsX:
            libpanda._inPVZN3wwsX(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN3trfB()
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3ExVl()
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3HxjB()
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPVZN3Bxxd()
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def getClassType():
        returnValue = libpanda._inPVZN3yA_x()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase3D__overloaded_assign_ptrLVecBase3d_ptrConstLVecBase3d(self, copy):
        returnValue = libpanda._inPVZN3yavJ(self.this, copy.this)
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase3D__overloaded_assign_ptrLVecBase3d_double(self, fillValue):
        returnValue = libpanda._inPVZN3_NPY(self.this, fillValue)
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase3D__overloaded___getitem___ptrLVecBase3d_int(self, i):
        returnValue = libpanda._inPVZN3KmHn(self.this, i)
        return returnValue

    
    def _VBase3D__overloaded___getitem___ptrConstLVecBase3d_int(self, i):
        returnValue = libpanda._inPVZN3IH7D(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPVZN37uGy(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPVZN3gqfX(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPVZN38t_C(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPVZN38J4H(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPVZN38lwM(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPVZN3j_Qe(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPVZN3fZV6(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPVZN3f9N_(self.this, value)
        return returnValue

    
    def setZ(self, value):
        returnValue = libpanda._inPVZN3eBGE(self.this, value)
        return returnValue

    
    def addToCell(self, i, value):
        returnValue = libpanda._inPVZN3LMq8(self.this, i, value)
        return returnValue

    
    def addX(self, value):
        returnValue = libpanda._inPVZN30Qy4(self.this, value)
        return returnValue

    
    def addY(self, value):
        returnValue = libpanda._inPVZN300q9(self.this, value)
        return returnValue

    
    def addZ(self, value):
        returnValue = libpanda._inPVZN33YjC(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPVZN3d9D2(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPVZN3LxGp(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPVZN3xac_(self.this, fillValue)
        return returnValue

    
    def set(self, x, y, z):
        returnValue = libpanda._inPVZN3L816(self.this, x, y, z)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPVZN34N6j(self.this, other.this)
        return returnValue

    
    def cross(self, other):
        returnValue = libpanda._inPVZN3vmLU(self.this, other.this)
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def lessThan(self, other):
        returnValue = libpanda._inPVZN3f_c1(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPVZN35E4P(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPVZN3Ckg_(self.this, other.this)
        return returnValue

    
    def getStandardizedHpr(self):
        returnValue = libpanda._inPVZN3wK45(self.this)
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase3D__overloaded_compareTo_ptrConstLVecBase3d_ptrConstLVecBase3d(self, other):
        returnValue = libpanda._inPVZN3AqT1(self.this, other.this)
        return returnValue

    
    def _VBase3D__overloaded_compareTo_ptrConstLVecBase3d_ptrConstLVecBase3d_double(self, other, threshold):
        returnValue = libpanda._inPVZN3DVKA(self.this, other.this, threshold)
        return returnValue

    
    def _VBase3D__overloaded_getHash_ptrConstLVecBase3d(self):
        returnValue = libpanda._inPVZN3Q_pi(self.this)
        return returnValue

    
    def _VBase3D__overloaded_getHash_ptrConstLVecBase3d_double(self, threshold):
        returnValue = libpanda._inPVZN3BwnB(self.this, threshold)
        return returnValue

    
    def _VBase3D__overloaded_addHash_ptrConstLVecBase3d_unsignedint(self, hash):
        returnValue = libpanda._inPVZN3lrfx(self.this, hash)
        return returnValue

    
    def _VBase3D__overloaded_addHash_ptrConstLVecBase3d_unsignedint_double(self, hash, threshold):
        returnValue = libpanda._inPVZN3jZW8(self.this, hash, threshold)
        return returnValue

    
    def _VBase3D__overloaded___sub___ptrConstLVecBase3d(self):
        returnValue = libpanda._inPVZN3Ey_f(self.this)
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase3D__overloaded___sub___ptrConstLVecBase3d_ptrConstLVecBase3d(self, other):
        returnValue = libpanda._inPVZN3ZG_i(self.this, other.this)
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPVZN3Z2dP(self.this, other.this)
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN36_m2(self.this, scalar)
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN37Wdn(self.this, scalar)
        returnObject = VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPVZN3azWw(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPVZN3bD4D(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPVZN3FCn2(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPVZN3K6bn(self.this, scalar)
        return self

    
    def crossInto(self, other):
        returnValue = libpanda._inPVZN3mWqm(self.this, other.this)
        return returnValue

    
    def _VBase3D__overloaded_almostEqual_ptrConstLVecBase3d_ptrConstLVecBase3d(self, other):
        returnValue = libpanda._inPVZN3gl6W(self.this, other.this)
        return returnValue

    
    def _VBase3D__overloaded_almostEqual_ptrConstLVecBase3d_ptrConstLVecBase3d_double(self, other, threshold):
        returnValue = libpanda._inPVZN36Cbn(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPVZN3hBt4(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase3D__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase3D__overloaded_constructor_double(*_args)
            
            if isinstance(_args[0], VBase3D):
                return self._VBase3D__overloaded_constructor_ptrConstLVecBase3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D> '
        elif numArgs == 3:
            return self._VBase3D__overloaded_constructor_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase3D__overloaded_almostEqual_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        elif numArgs == 2:
            return self._VBase3D__overloaded_almostEqual_ptrConstLVecBase3d_ptrConstLVecBase3d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase3D__overloaded_getHash_ptrConstLVecBase3d(*_args)
        elif numArgs == 1:
            return self._VBase3D__overloaded_getHash_ptrConstLVecBase3d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase3D__overloaded___getitem___ptrConstLVecBase3d_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase3D__overloaded_addHash_ptrConstLVecBase3d_unsignedint(*_args)
        elif numArgs == 2:
            return self._VBase3D__overloaded_addHash_ptrConstLVecBase3d_unsignedint_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase3D__overloaded_compareTo_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        elif numArgs == 2:
            return self._VBase3D__overloaded_compareTo_ptrConstLVecBase3d_ptrConstLVecBase3d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase3D__overloaded___sub___ptrConstLVecBase3d(*_args)
        elif numArgs == 1:
            return self._VBase3D__overloaded___sub___ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase3D__overloaded_assign_ptrLVecBase3d_double(*_args)
            
            if isinstance(_args[0], VBase3D):
                return self._VBase3D__overloaded_assign_ptrLVecBase3d_ptrConstLVecBase3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


