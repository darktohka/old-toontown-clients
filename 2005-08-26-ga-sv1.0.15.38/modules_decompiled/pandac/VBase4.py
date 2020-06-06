# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class VBase4(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _VBase4__overloaded_constructor(self):
        self.this = libpanda._inPVZN35kRY()
        self.userManagesMemory = 1

    
    def _VBase4__overloaded_constructor_ptrConstLVecBase4f(self, copy):
        self.this = libpanda._inPVZN3dTtd(copy.this)
        self.userManagesMemory = 1

    
    def _VBase4__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPVZN3ity7(fillValue)
        self.userManagesMemory = 1

    
    def _VBase4__overloaded_constructor_float_float_float_float(self, x, y, z, w):
        self.this = libpanda._inPVZN3DRvG(x, y, z, w)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3xsFk:
            libpanda._inPVZN3xsFk(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN3mHPT()
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3xCF3()
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3MdTT()
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPVZN3Odhv()
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def unitW():
        returnValue = libpanda._inPVZN33C3a()
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitW = staticmethod(unitW)
    
    def getClassType():
        returnValue = libpanda._inPVZN3hKuD()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase4__overloaded_assign_ptrLVecBase4f_ptrConstLVecBase4f(self, copy):
        returnValue = libpanda._inPVZN3XuCG(self.this, copy.this)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase4__overloaded_assign_ptrLVecBase4f_float(self, fillValue):
        returnValue = libpanda._inPVZN3GYHk(self.this, fillValue)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase4__overloaded___getitem___ptrLVecBase4f_int(self, i):
        returnValue = libpanda._inPVZN3By34(self.this, i)
        return returnValue

    
    def _VBase4__overloaded___getitem___ptrConstLVecBase4f_int(self, i):
        returnValue = libpanda._inPVZN3TrrV(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPVZN3x62D(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPVZN3d_Pp(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPVZN3JYvU(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPVZN3J8oZ(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPVZN3JQge(self.this)
        return returnValue

    
    def getW(self):
        returnValue = libpanda._inPVZN3JE3P(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPVZN3AQHX(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPVZN3JuJp(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPVZN3JKCu(self.this, value)
        return returnValue

    
    def setZ(self, value):
        returnValue = libpanda._inPVZN3JW6y(self.this, value)
        return returnValue

    
    def setW(self, value):
        returnValue = libpanda._inPVZN3JCRk(self.this, value)
        return returnValue

    
    def addToCell(self, i, value):
        returnValue = libpanda._inPVZN3zyHW(self.this, i, value)
        return returnValue

    
    def addX(self, value):
        returnValue = libpanda._inPVZN3mmmn(self.this, value)
        return returnValue

    
    def addY(self, value):
        returnValue = libpanda._inPVZN3mCfs(self.this, value)
        return returnValue

    
    def addZ(self, value):
        returnValue = libpanda._inPVZN3muXx(self.this, value)
        return returnValue

    
    def addW(self, value):
        returnValue = libpanda._inPVZN3maui(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPVZN3XRyH(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPVZN30F36(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPVZN3W1HJ(self.this, fillValue)
        return returnValue

    
    def set(self, x, y, z, w):
        returnValue = libpanda._inPVZN3__rX(self.this, x, y, z, w)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPVZN32052(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPVZN3xlvx(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPVZN3auYz(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPVZN3mNAi(self.this, other.this)
        return returnValue

    
    def _VBase4__overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPVZN3tXnx(self.this, other.this)
        return returnValue

    
    def _VBase4__overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f_float(self, other, threshold):
        returnValue = libpanda._inPVZN3IZYW(self.this, other.this, threshold)
        return returnValue

    
    def _VBase4__overloaded_getHash_ptrConstLVecBase4f(self):
        returnValue = libpanda._inPVZN3diZ0(self.this)
        return returnValue

    
    def _VBase4__overloaded_getHash_ptrConstLVecBase4f_float(self, threshold):
        returnValue = libpanda._inPVZN3zn_6(self.this, threshold)
        return returnValue

    
    def _VBase4__overloaded_addHash_ptrConstLVecBase4f_unsignedint(self, hash):
        returnValue = libpanda._inPVZN3r3PD(self.this, hash)
        return returnValue

    
    def _VBase4__overloaded_addHash_ptrConstLVecBase4f_unsignedint_float(self, hash, threshold):
        returnValue = libpanda._inPVZN3NEBo(self.this, hash, threshold)
        return returnValue

    
    def _VBase4__overloaded___sub___ptrConstLVecBase4f(self):
        returnValue = libpanda._inPVZN3POux(self.this)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase4__overloaded___sub___ptrConstLVecBase4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPVZN3zdSf(self.this, other.this)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPVZN3ztwL(self.this, other.this)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN3reVF(self.this, scalar)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3r2J2(self.this, scalar)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPVZN3tr3T(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPVZN3tbZn(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPVZN37ZPM(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPVZN37hD9(self.this, scalar)
        return self

    
    def _VBase4__overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPVZN3yKzg(self.this, other.this)
        return returnValue

    
    def _VBase4__overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f_float(self, other, threshold):
        returnValue = libpanda._inPVZN3__lQ(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPVZN3QPcK(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase4__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase4__overloaded_constructor_float(*_args)
            
            if isinstance(_args[0], VBase4):
                return self._VBase4__overloaded_constructor_ptrConstLVecBase4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4> '
        elif numArgs == 4:
            return self._VBase4__overloaded_constructor_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 4 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase4__overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f(*_args)
        elif numArgs == 2:
            return self._VBase4__overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase4__overloaded_getHash_ptrConstLVecBase4f(*_args)
        elif numArgs == 1:
            return self._VBase4__overloaded_getHash_ptrConstLVecBase4f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase4__overloaded___getitem___ptrConstLVecBase4f_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase4__overloaded_addHash_ptrConstLVecBase4f_unsignedint(*_args)
        elif numArgs == 2:
            return self._VBase4__overloaded_addHash_ptrConstLVecBase4f_unsignedint_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase4__overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f(*_args)
        elif numArgs == 2:
            return self._VBase4__overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase4__overloaded___sub___ptrConstLVecBase4f(*_args)
        elif numArgs == 1:
            return self._VBase4__overloaded___sub___ptrConstLVecBase4f_ptrConstLVecBase4f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase4__overloaded_assign_ptrLVecBase4f_float(*_args)
            
            if isinstance(_args[0], VBase4):
                return self._VBase4__overloaded_assign_ptrLVecBase4f_ptrConstLVecBase4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __repr__(self):
        return '%s(%s,%s,%s,%s)' % (self.__class__.__name__, self[0], self[1], self[2], self[3])

    
    def pPrintValues(self):
        return '% 10.4f, % 10.4f, % 10.4f, % 10.4f' % (self[0], self[1], self[2], self[3])


