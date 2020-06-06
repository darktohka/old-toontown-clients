# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class VBase2D(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _VBase2D__overloaded_constructor(self):
        self.this = libpanda._inPVZN3GdnQ()
        self.userManagesMemory = 1

    
    def _VBase2D__overloaded_constructor_ptrConstLVecBase2d(self, copy):
        self.this = libpanda._inPVZN3CUdE(copy.this)
        self.userManagesMemory = 1

    
    def _VBase2D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPVZN3i9B6(fillValue)
        self.userManagesMemory = 1

    
    def _VBase2D__overloaded_constructor_double_double(self, x, y):
        self.this = libpanda._inPVZN3CY0M(x, y)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3cILs:
            libpanda._inPVZN3cILs(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN3xrvf()
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN352lD()
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN372zf()
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def getClassType():
        returnValue = libpanda._inPVZN3vAPQ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase2D__overloaded_assign_ptrLVecBase2d_ptrConstLVecBase2d(self, copy):
        returnValue = libpanda._inPVZN3G77A(self.this, copy.this)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase2D__overloaded_assign_ptrLVecBase2d_double(self, fillValue):
        returnValue = libpanda._inPVZN3jNf2(self.this, fillValue)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase2D__overloaded___getitem___ptrLVecBase2d_int(self, i):
        returnValue = libpanda._inPVZN35ZXF(self.this, i)
        return returnValue

    
    def _VBase2D__overloaded___getitem___ptrConstLVecBase2d_int(self, i):
        returnValue = libpanda._inPVZN3cHLi(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPVZN3muWQ(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPVZN3Urv1(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPVZN3QsPh(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPVZN3QIIm(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPVZN33_g8(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPVZN3KZlY(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPVZN3K9dd(self.this, value)
        return returnValue

    
    def addToCell(self, i, value):
        returnValue = libpanda._inPVZN30P6a(self.this, i, value)
        return returnValue

    
    def addX(self, value):
        returnValue = libpanda._inPVZN3rQCX(self.this, value)
        return returnValue

    
    def addY(self, value):
        returnValue = libpanda._inPVZN3r06b(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPVZN3u9TU(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPVZN38xWH(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPVZN3sasc(self.this, fillValue)
        return returnValue

    
    def set(self, x, y):
        returnValue = libpanda._inPVZN3bAy_(self.this, x, y)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPVZN3cCJC(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPVZN3Leos(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPVZN3gLYM(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPVZN3trA7(self.this, other.this)
        return returnValue

    
    def _VBase2D__overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPVZN3cKgs(self.this, other.this)
        return returnValue

    
    def _VBase2D__overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d_double(self, other, threshold):
        returnValue = libpanda._inPVZN3e1W3(self.this, other.this, threshold)
        return returnValue

    
    def _VBase2D__overloaded_getHash_ptrConstLVecBase2d(self):
        returnValue = libpanda._inPVZN3F_5A(self.this)
        return returnValue

    
    def _VBase2D__overloaded_getHash_ptrConstLVecBase2d_double(self, threshold):
        returnValue = libpanda._inPVZN31_3f(self.this, threshold)
        return returnValue

    
    def _VBase2D__overloaded_addHash_ptrConstLVecBase2d_unsignedint(self, hash):
        returnValue = libpanda._inPVZN3wrvP(self.this, hash)
        return returnValue

    
    def _VBase2D__overloaded_addHash_ptrConstLVecBase2d_unsignedint_double(self, hash, threshold):
        returnValue = libpanda._inPVZN3_Zma(self.this, hash, threshold)
        return returnValue

    
    def _VBase2D__overloaded___sub___ptrConstLVecBase2d(self):
        returnValue = libpanda._inPVZN34yP_(self.this)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase2D__overloaded___sub___ptrConstLVecBase2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPVZN3FmLa(self.this, other.this)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPVZN3FWpG(self.this, other.this)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN3P52U(self.this, scalar)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3IRtF(self.this, scalar)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPVZN3zz2s(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPVZN38DYA(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPVZN3WC3U(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPVZN3X6rF(self.this, scalar)
        return self

    
    def _VBase2D__overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPVZN3nTK9(self.this, other.this)
        return returnValue

    
    def _VBase2D__overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d_double(self, other, threshold):
        returnValue = libpanda._inPVZN3_OqN(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPVZN3SB9W(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase2D__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase2D__overloaded_constructor_double(*_args)
            
            if isinstance(_args[0], VBase2D):
                return self._VBase2D__overloaded_constructor_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D> '
        elif numArgs == 2:
            return self._VBase2D__overloaded_constructor_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase2D__overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d(*_args)
        elif numArgs == 2:
            return self._VBase2D__overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase2D__overloaded_getHash_ptrConstLVecBase2d(*_args)
        elif numArgs == 1:
            return self._VBase2D__overloaded_getHash_ptrConstLVecBase2d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase2D__overloaded___getitem___ptrConstLVecBase2d_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase2D__overloaded_addHash_ptrConstLVecBase2d_unsignedint(*_args)
        elif numArgs == 2:
            return self._VBase2D__overloaded_addHash_ptrConstLVecBase2d_unsignedint_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase2D__overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d(*_args)
        elif numArgs == 2:
            return self._VBase2D__overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase2D__overloaded___sub___ptrConstLVecBase2d(*_args)
        elif numArgs == 1:
            return self._VBase2D__overloaded___sub___ptrConstLVecBase2d_ptrConstLVecBase2d(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase2D__overloaded_assign_ptrLVecBase2d_double(*_args)
            
            if isinstance(_args[0], VBase2D):
                return self._VBase2D__overloaded_assign_ptrLVecBase2d_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


