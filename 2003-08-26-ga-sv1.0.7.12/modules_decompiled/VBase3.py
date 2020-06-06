# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class VBase3(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _VBase3__overloaded_constructor(self):
        self.this = libpanda._inPUZN38GM2()
        self.userManagesMemory = 1

    
    def _VBase3__overloaded_constructor_ptrConstLVecBase3f(self, copy):
        self.this = libpanda._inPUZN3RRmU(copy.this)
        self.userManagesMemory = 1

    
    def _VBase3__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPUZN3BPuZ(fillValue)
        self.userManagesMemory = 1

    
    def _VBase3__overloaded_constructor_float_float_float(self, x, y, z):
        self.this = libpanda._inPUZN3kj6v(x, y, z)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3ckk4:
            libpanda._inPUZN3ckk4(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN3LGfx()
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3mCVV()
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3hCjx()
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPUZN3jCxN()
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def getClassType():
        returnValue = libpanda._inPUZN3eN_h()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase3__overloaded_assign_ptrLVecBase3f_ptrConstLVecBase3f(self, copy):
        returnValue = libpanda._inPUZN3rOP9(self.this, copy.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase3__overloaded_assign_ptrLVecBase3f_float(self, fillValue):
        returnValue = libpanda._inPUZN3rfXC(self.this, fillValue)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase3__overloaded___getitem___ptrLVecBase3f_int(self, i):
        returnValue = libpanda._inPUZN301HX(self.this, i)
        return returnValue

    
    def _VBase3__overloaded___getitem___ptrConstLVecBase3f_int(self, i):
        returnValue = libpanda._inPUZN3mq7z(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPUZN3c5Gi(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPUZN3O_fH(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPUZN3aY_y(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPUZN3a843(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPUZN3aQw8(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPUZN3TQX1(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPUZN3cuZH(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPUZN3cKSM(self.this, value)
        return returnValue

    
    def setZ(self, value):
        returnValue = libpanda._inPUZN3cWKR(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPUZN3gRCm(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPUZN3pFHZ(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPUZN3p1Xn(self.this, fillValue)
        return returnValue

    
    def set(self, x, y, z):
        returnValue = libpanda._inPUZN3Navy(self.this, x, y, z)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPUZN3aDIV(self.this, other.this)
        return returnValue

    
    def cross(self, other):
        returnValue = libpanda._inPUZN3VJ6l(self.this, other.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def lessThan(self, other):
        returnValue = libpanda._inPUZN3iF8o(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPUZN3Et4v(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPUZN3BNge(self.this, other.this)
        return returnValue

    
    def _VBase3__overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other):
        returnValue = libpanda._inPUZN3_3zo(self.this, other.this)
        return returnValue

    
    def _VBase3__overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f_float(self, other, threshold):
        returnValue = libpanda._inPUZN38GlN(self.this, other.this, threshold)
        return returnValue

    
    def _VBase3__overloaded___sub___ptrConstLVecBase3f(self):
        returnValue = libpanda._inPUZN3iO_P(self.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase3__overloaded___sub___ptrConstLVecBase3f_ptrConstLVecBase3f(self, other):
        returnValue = libpanda._inPUZN3f8eW(self.this, other.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPUZN3fM9C(self.this, other.this)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3Ydlj(self.this, scalar)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3Y1ZU(self.this, scalar)
        returnObject = VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPUZN3GqXQ(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPUZN3Ha5j(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPUZN3OZfq(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPUZN3OhTb(self.this, scalar)
        return self

    
    def crossInto(self, other):
        returnValue = libpanda._inPUZN3vCKa(self.this, other.this)
        return returnValue

    
    def _VBase3__overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other):
        returnValue = libpanda._inPUZN32ADH(self.this, other.this)
        return returnValue

    
    def _VBase3__overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f_float(self, other, threshold):
        returnValue = libpanda._inPUZN3iJ12(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPUZN39Oso(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase3__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._VBase3__overloaded_constructor_float(_args[0])
            elif isinstance(_args[0], VBase3):
                return self._VBase3__overloaded_constructor_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._VBase3__overloaded_constructor_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], VBase3):
                return self._VBase3__overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3> '
        elif numArgs == 2:
            if isinstance(_args[0], VBase3):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase3__overloaded_almostEqual_ptrConstLVecBase3f_ptrConstLVecBase3f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase3__overloaded___sub___ptrConstLVecBase3f()
        elif numArgs == 1:
            if isinstance(_args[0], VBase3):
                return self._VBase3__overloaded___sub___ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._VBase3__overloaded_assign_ptrLVecBase3f_float(_args[0])
            elif isinstance(_args[0], VBase3):
                return self._VBase3__overloaded_assign_ptrLVecBase3f_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._VBase3__overloaded___getitem___ptrConstLVecBase3f_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], VBase3):
                return self._VBase3__overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3> '
        elif numArgs == 2:
            if isinstance(_args[0], VBase3):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase3__overloaded_compareTo_ptrConstLVecBase3f_ptrConstLVecBase3f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


