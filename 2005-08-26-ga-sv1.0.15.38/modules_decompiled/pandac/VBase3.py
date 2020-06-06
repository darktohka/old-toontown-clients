# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class VBase3(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _VBase3__overloaded_constructor(self):
        self.this = libpanda._inPVZN39GM2()
        self.userManagesMemory = 1

    
    def _VBase3__overloaded_constructor_ptrConstLVecBase3f(self, copy):
        self.this = libpanda._inPVZN3RRmU(copy.this)
        self.userManagesMemory = 1

    
    def _VBase3__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPVZN3BPuZ(fillValue)
        self.userManagesMemory = 1

    
    def _VBase3__overloaded_constructor_float_float_float(self, x, y, z):
        self.this = libpanda._inPVZN3nj6v(x, y, z)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3dkk4:
            libpanda._inPVZN3dkk4(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN3KGfx()
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3mCVV()
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3gCjx()
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPVZN3jCxN()
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def getClassType():
        returnValue = libpanda._inPVZN3dN_h()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase3__overloaded_assign_ptrLVecBase3f_ptrConstLVecBase3f(self, copy):
        returnValue = libpanda._inPVZN3qOP9(self.this, copy.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase3__overloaded_assign_ptrLVecBase3f_float(self, fillValue):
        returnValue = libpanda._inPVZN3rfXC(self.this, fillValue)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase3__overloaded___getitem___ptrLVecBase3f_int(self, i):
        returnValue = libpanda._inPVZN301HX(self.this, i)
        return returnValue

    
    def _VBase3__overloaded___getitem___ptrConstLVecBase3f_int(self, i):
        returnValue = libpanda._inPVZN3nq7z(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPVZN3d5Gi(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPVZN3O_fH(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPVZN3dY_y(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPVZN3d843(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPVZN3dQw8(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPVZN3UQX1(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPVZN3cuZH(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPVZN3cKSM(self.this, value)
        return returnValue

    
    def setZ(self, value):
        returnValue = libpanda._inPVZN3cWKR(self.this, value)
        return returnValue

    
    def addToCell(self, i, value):
        returnValue = libpanda._inPVZN3HyX0(self.this, i, value)
        return returnValue

    
    def addX(self, value):
        returnValue = libpanda._inPVZN31m2F(self.this, value)
        return returnValue

    
    def addY(self, value):
        returnValue = libpanda._inPVZN31CvK(self.this, value)
        return returnValue

    
    def addZ(self, value):
        returnValue = libpanda._inPVZN31unP(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPVZN3jRCm(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPVZN3pFHZ(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPVZN3q1Xn(self.this, fillValue)
        return returnValue

    
    def set(self, x, y, z):
        returnValue = libpanda._inPVZN3Oavy(self.this, x, y, z)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPVZN3aDIV(self.this, other.this)
        return returnValue

    
    def cross(self, other):
        returnValue = libpanda._inPVZN3aJ6l(self.this, other.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def lessThan(self, other):
        returnValue = libpanda._inPVZN3dE8o(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPVZN3Ft4v(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPVZN3BNge(self.this, other.this)
        return returnValue

    
    def getStandardizedHpr(self):
        returnValue = libpanda._inPVZN3W_5p(self.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase3__overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other):
        returnValue = libpanda._inPVZN353zo(self.this, other.this)
        return returnValue

    
    def _VBase3__overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f_float(self, other, threshold):
        returnValue = libpanda._inPVZN38GlN(self.this, other.this, threshold)
        return returnValue

    
    def _VBase3__overloaded_getHash_ptrConstLVecBase3f(self):
        returnValue = libpanda._inPVZN3OipS(self.this)
        return returnValue

    
    def _VBase3__overloaded_getHash_ptrConstLVecBase3f_float(self, threshold):
        returnValue = libpanda._inPVZN3gnPZ(self.this, threshold)
        return returnValue

    
    def _VBase3__overloaded_addHash_ptrConstLVecBase3f_unsignedint(self, hash):
        returnValue = libpanda._inPVZN3H3fh(self.this, hash)
        return returnValue

    
    def _VBase3__overloaded_addHash_ptrConstLVecBase3f_unsignedint_float(self, hash, threshold):
        returnValue = libpanda._inPVZN3wERG(self.this, hash, threshold)
        return returnValue

    
    def _VBase3__overloaded___sub___ptrConstLVecBase3f(self):
        returnValue = libpanda._inPVZN3iO_P(self.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase3__overloaded___sub___ptrConstLVecBase3f_ptrConstLVecBase3f(self, other):
        returnValue = libpanda._inPVZN3f8eW(self.this, other.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPVZN3fM9C(self.this, other.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN3Hdlj(self.this, scalar)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3Y1ZU(self.this, scalar)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPVZN3GqXQ(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPVZN3Ga5j(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPVZN3PZfq(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPVZN3OhTb(self.this, scalar)
        return self

    
    def crossInto(self, other):
        returnValue = libpanda._inPVZN3vCKa(self.this, other.this)
        return returnValue

    
    def _VBase3__overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other):
        returnValue = libpanda._inPVZN32ADH(self.this, other.this)
        return returnValue

    
    def _VBase3__overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f_float(self, other, threshold):
        returnValue = libpanda._inPVZN3jJ12(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPVZN38Oso(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase3__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase3__overloaded_constructor_float(*_args)
            
            if isinstance(_args[0], VBase3):
                return self._VBase3__overloaded_constructor_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3> '
        elif numArgs == 3:
            return self._VBase3__overloaded_constructor_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase3__overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 2:
            return self._VBase3__overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase3__overloaded_getHash_ptrConstLVecBase3f(*_args)
        elif numArgs == 1:
            return self._VBase3__overloaded_getHash_ptrConstLVecBase3f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase3__overloaded___getitem___ptrConstLVecBase3f_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase3__overloaded_addHash_ptrConstLVecBase3f_unsignedint(*_args)
        elif numArgs == 2:
            return self._VBase3__overloaded_addHash_ptrConstLVecBase3f_unsignedint_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase3__overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        elif numArgs == 2:
            return self._VBase3__overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase3__overloaded___sub___ptrConstLVecBase3f(*_args)
        elif numArgs == 1:
            return self._VBase3__overloaded___sub___ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase3__overloaded_assign_ptrLVecBase3f_float(*_args)
            
            if isinstance(_args[0], VBase3):
                return self._VBase3__overloaded_assign_ptrLVecBase3f_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __repr__(self):
        return '%s(%s,%s,%s)' % (self.__class__.__name__, self[0], self[1], self[2])

    
    def pPrintValues(self):
        return '% 10.4f, % 10.4f, % 10.4f' % (self[0], self[1], self[2])


