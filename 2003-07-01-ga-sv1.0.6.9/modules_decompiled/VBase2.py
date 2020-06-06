# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class VBase2(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _VBase2__overloaded_constructor(self):
        self.this = libpanda._inPUZN3gaIU()
        self.userManagesMemory = 1

    
    def _VBase2__overloaded_constructor_ptrConstLVecBase2f(self, copy):
        self.this = libpanda._inPUZN3VQfL(copy.this)
        self.userManagesMemory = 1

    
    def _VBase2__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPUZN3kRq3(fillValue)
        self.userManagesMemory = 1

    
    def _VBase2__overloaded_constructor_float_float(self, x, y):
        self.this = libpanda._inPUZN3oQsK(x, y)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3IcDN:
            libpanda._inPUZN3IcDN(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN3fGvP()
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3bClz()
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3VCzP()
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def getClassType():
        returnValue = libpanda._inPUZN3KNOA()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase2__overloaded_assign_ptrLVecBase2f_ptrConstLVecBase2f(self, copy):
        returnValue = libpanda._inPUZN3_ub0(self.this, copy.this)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase2__overloaded_assign_ptrLVecBase2f_float(self, fillValue):
        returnValue = libpanda._inPUZN38fng(self.this, fillValue)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase2__overloaded___getitem___ptrLVecBase2f_int(self, i):
        returnValue = libpanda._inPUZN3b1X1(self.this, i)
        return returnValue

    
    def _VBase2__overloaded___getitem___ptrConstLVecBase2f_int(self, i):
        returnValue = libpanda._inPUZN36qLS(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPUZN3I5WA(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPUZN3z_vl(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPUZN3uYPR(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPUZN3u8IW(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPUZN3nQnT(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPUZN3jvpl(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPUZN3jLiq(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPUZN3MuTE(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPUZN3aEX3(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPUZN391nF(self.this, fillValue)
        return returnValue

    
    def set(self, x, y):
        returnValue = libpanda._inPUZN3lT_9(self.this, x, y)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPUZN3CRXz(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPUZN3OkIg(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPUZN3vsYs(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPUZN3oMAb(self.this, other.this)
        return returnValue

    
    def _VBase2__overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f(self, other):
        returnValue = libpanda._inPUZN3KWAg(self.this, other.this)
        return returnValue

    
    def _VBase2__overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f_float(self, other, threshold):
        returnValue = libpanda._inPUZN3gmxE(self.this, other.this, threshold)
        return returnValue

    
    def _VBase2__overloaded___sub___ptrConstLVecBase2f(self):
        returnValue = libpanda._inPUZN3VPOu(self.this)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase2__overloaded___sub___ptrConstLVecBase2f_ptrConstLVecBase2f(self, other):
        returnValue = libpanda._inPUZN3LcrN(self.this, other.this)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPUZN3LsJ6(self.this, other.this)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN30d1B(self.this, scalar)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN311py(self.this, scalar)
        returnObject = VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPUZN3_q3M(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPUZN34aZg(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPUZN3iYvI(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPUZN3hgj5(self.this, scalar)
        return self

    
    def _VBase2__overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f(self, other):
        returnValue = libpanda._inPUZN3KeTt(self.this, other.this)
        return returnValue

    
    def _VBase2__overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f_float(self, other, threshold):
        returnValue = libpanda._inPUZN3nTFd(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPUZN3pO8G(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase2__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._VBase2__overloaded_constructor_float(_args[0])
            elif isinstance(_args[0], VBase2):
                return self._VBase2__overloaded_constructor_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase2__overloaded_constructor_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], VBase2):
                return self._VBase2__overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2> '
        elif numArgs == 2:
            if isinstance(_args[0], VBase2):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase2__overloaded_almostEqual_ptrConstLVecBase2f_ptrConstLVecBase2f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase2__overloaded___sub___ptrConstLVecBase2f()
        elif numArgs == 1:
            if isinstance(_args[0], VBase2):
                return self._VBase2__overloaded___sub___ptrConstLVecBase2f_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._VBase2__overloaded_assign_ptrLVecBase2f_float(_args[0])
            elif isinstance(_args[0], VBase2):
                return self._VBase2__overloaded_assign_ptrLVecBase2f_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._VBase2__overloaded___getitem___ptrConstLVecBase2f_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], VBase2):
                return self._VBase2__overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2> '
        elif numArgs == 2:
            if isinstance(_args[0], VBase2):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase2__overloaded_compareTo_ptrConstLVecBase2f_ptrConstLVecBase2f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


