# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class VBase2(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _VBase2__overloaded_constructor(self):
        self.this = libpanda._inPVZN3gaIU()
        self.userManagesMemory = 1

    
    def _VBase2__overloaded_constructor_ptrConstLVecBase2f(self, copy):
        self.this = libpanda._inPVZN3VQfL(copy.this)
        self.userManagesMemory = 1

    
    def _VBase2__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPVZN3lRq3(fillValue)
        self.userManagesMemory = 1

    
    def _VBase2__overloaded_constructor_float_float(self, x, y):
        self.this = libpanda._inPVZN3oQsK(x, y)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3IcDN:
            libpanda._inPVZN3IcDN(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN3fGvP()
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3aClz()
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3VCzP()
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def getClassType():
        returnValue = libpanda._inPVZN3KNOA()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase2__overloaded_assign_ptrLVecBase2f_ptrConstLVecBase2f(self, copy):
        returnValue = libpanda._inPVZN3_ub0(self.this, copy.this)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase2__overloaded_assign_ptrLVecBase2f_float(self, fillValue):
        returnValue = libpanda._inPVZN3_fng(self.this, fillValue)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase2__overloaded___getitem___ptrLVecBase2f_int(self, i):
        returnValue = libpanda._inPVZN3Y1X1(self.this, i)
        return returnValue

    
    def _VBase2__overloaded___getitem___ptrConstLVecBase2f_int(self, i):
        returnValue = libpanda._inPVZN36qLS(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPVZN3I5WA(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPVZN3y_vl(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPVZN3uYPR(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPVZN3u8IW(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPVZN3nQnT(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPVZN3gvpl(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPVZN3gLiq(self.this, value)
        return returnValue

    
    def addToCell(self, i, value):
        returnValue = libpanda._inPVZN3qznS(self.this, i, value)
        return returnValue

    
    def addX(self, value):
        returnValue = libpanda._inPVZN3BpGk(self.this, value)
        return returnValue

    
    def addY(self, value):
        returnValue = libpanda._inPVZN3BN_o(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPVZN3MuTE(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPVZN3dEX3(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPVZN391nF(self.this, fillValue)
        return returnValue

    
    def set(self, x, y):
        returnValue = libpanda._inPVZN3mT_9(self.this, x, y)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPVZN39RXz(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPVZN3JkIg(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPVZN3ssYs(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPVZN3oMAb(self.this, other.this)
        return returnValue

    
    def _VBase2__overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f(self, other):
        returnValue = libpanda._inPVZN3VWAg(self.this, other.this)
        return returnValue

    
    def _VBase2__overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f_float(self, other, threshold):
        returnValue = libpanda._inPVZN3gmxE(self.this, other.this, threshold)
        return returnValue

    
    def _VBase2__overloaded_getHash_ptrConstLVecBase2f(self):
        returnValue = libpanda._inPVZN3it5w(self.this)
        return returnValue

    
    def _VBase2__overloaded_getHash_ptrConstLVecBase2f_float(self, threshold):
        returnValue = libpanda._inPVZN3cmf3(self.this, threshold)
        return returnValue

    
    def _VBase2__overloaded_addHash_ptrConstLVecBase2f_unsignedint(self, hash):
        returnValue = libpanda._inPVZN3T3v_(self.this, hash)
        return returnValue

    
    def _VBase2__overloaded_addHash_ptrConstLVecBase2f_unsignedint_float(self, hash, threshold):
        returnValue = libpanda._inPVZN3kEhk(self.this, hash, threshold)
        return returnValue

    
    def _VBase2__overloaded___sub___ptrConstLVecBase2f(self):
        returnValue = libpanda._inPVZN3WPOu(self.this)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase2__overloaded___sub___ptrConstLVecBase2f_ptrConstLVecBase2f(self, other):
        returnValue = libpanda._inPVZN3LcrN(self.this, other.this)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPVZN3KsJ6(self.this, other.this)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN30d1B(self.this, scalar)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN301py(self.this, scalar)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPVZN3_q3M(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPVZN3_aZg(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPVZN3iYvI(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPVZN3igj5(self.this, scalar)
        return self

    
    def _VBase2__overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f(self, other):
        returnValue = libpanda._inPVZN3NeTt(self.this, other.this)
        return returnValue

    
    def _VBase2__overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f_float(self, other, threshold):
        returnValue = libpanda._inPVZN3nTFd(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPVZN3pO8G(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase2__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase2__overloaded_constructor_float(*_args)
            
            if isinstance(_args[0], VBase2):
                return self._VBase2__overloaded_constructor_ptrConstLVecBase2f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2> '
        elif numArgs == 2:
            return self._VBase2__overloaded_constructor_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase2__overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f(*_args)
        elif numArgs == 2:
            return self._VBase2__overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase2__overloaded_getHash_ptrConstLVecBase2f(*_args)
        elif numArgs == 1:
            return self._VBase2__overloaded_getHash_ptrConstLVecBase2f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase2__overloaded___getitem___ptrConstLVecBase2f_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addHash(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase2__overloaded_addHash_ptrConstLVecBase2f_unsignedint(*_args)
        elif numArgs == 2:
            return self._VBase2__overloaded_addHash_ptrConstLVecBase2f_unsignedint_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._VBase2__overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f(*_args)
        elif numArgs == 2:
            return self._VBase2__overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase2__overloaded___sub___ptrConstLVecBase2f(*_args)
        elif numArgs == 1:
            return self._VBase2__overloaded___sub___ptrConstLVecBase2f_ptrConstLVecBase2f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._VBase2__overloaded_assign_ptrLVecBase2f_float(*_args)
            
            if isinstance(_args[0], VBase2):
                return self._VBase2__overloaded_assign_ptrLVecBase2f_ptrConstLVecBase2f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


