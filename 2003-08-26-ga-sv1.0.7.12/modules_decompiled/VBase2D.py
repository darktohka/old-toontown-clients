# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class VBase2D(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _VBase2D__overloaded_constructor(self):
        self.this = libpanda._inPUZN3GdnQ()
        self.userManagesMemory = 1

    
    def _VBase2D__overloaded_constructor_ptrConstLVecBase2d(self, copy):
        self.this = libpanda._inPUZN3CUdE(copy.this)
        self.userManagesMemory = 1

    
    def _VBase2D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPUZN3j9B6(fillValue)
        self.userManagesMemory = 1

    
    def _VBase2D__overloaded_constructor_double_double(self, x, y):
        self.this = libpanda._inPUZN3CY0M(x, y)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3fILs:
            libpanda._inPUZN3fILs(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN3xrvf()
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN352lD()
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN372zf()
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def getClassType():
        returnValue = libpanda._inPUZN3vAPQ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase2D__overloaded_assign_ptrLVecBase2d_ptrConstLVecBase2d(self, copy):
        returnValue = libpanda._inPUZN3G77A(self.this, copy.this)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase2D__overloaded_assign_ptrLVecBase2d_double(self, fillValue):
        returnValue = libpanda._inPUZN3iNf2(self.this, fillValue)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase2D__overloaded___getitem___ptrLVecBase2d_int(self, i):
        returnValue = libpanda._inPUZN35ZXF(self.this, i)
        return returnValue

    
    def _VBase2D__overloaded___getitem___ptrConstLVecBase2d_int(self, i):
        returnValue = libpanda._inPUZN3bHLi(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPUZN3muWQ(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPUZN3Vrv1(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPUZN3RsPh(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPUZN3RIIm(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPUZN3w_g8(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPUZN3KZlY(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPUZN3K9dd(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPUZN3u9TU(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPUZN38xWH(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPUZN3sasc(self.this, fillValue)
        return returnValue

    
    def set(self, x, y):
        returnValue = libpanda._inPUZN3YAy_(self.this, x, y)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPUZN3cCJC(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPUZN3Ieos(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPUZN3gLYM(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPUZN3srA7(self.this, other.this)
        return returnValue

    
    def _VBase2D__overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPUZN3dKgs(self.this, other.this)
        return returnValue

    
    def _VBase2D__overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d_double(self, other, threshold):
        returnValue = libpanda._inPUZN3f1W3(self.this, other.this, threshold)
        return returnValue

    
    def _VBase2D__overloaded___sub___ptrConstLVecBase2d(self):
        returnValue = libpanda._inPUZN33yP_(self.this)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase2D__overloaded___sub___ptrConstLVecBase2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPUZN3FmLa(self.this, other.this)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPUZN3FWpG(self.this, other.this)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3P52U(self.this, scalar)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3IRtF(self.this, scalar)
        returnObject = VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPUZN38z2s(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPUZN38DYA(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPUZN3WC3U(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPUZN3X6rF(self.this, scalar)
        return self

    
    def _VBase2D__overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPUZN3kTK9(self.this, other.this)
        return returnValue

    
    def _VBase2D__overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d_double(self, other, threshold):
        returnValue = libpanda._inPUZN3_OqN(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPUZN3SB9W(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase2D__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._VBase2D__overloaded_constructor_double(_args[0])
            elif isinstance(_args[0], VBase2D):
                return self._VBase2D__overloaded_constructor_ptrConstLVecBase2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase2D__overloaded_constructor_double_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], VBase2D):
                return self._VBase2D__overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2D> '
        elif numArgs == 2:
            if isinstance(_args[0], VBase2D):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase2D__overloaded_almostEqual_ptrConstLVecBase2d_ptrConstLVecBase2d_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase2D__overloaded___sub___ptrConstLVecBase2d()
        elif numArgs == 1:
            if isinstance(_args[0], VBase2D):
                return self._VBase2D__overloaded___sub___ptrConstLVecBase2d_ptrConstLVecBase2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._VBase2D__overloaded_assign_ptrLVecBase2d_double(_args[0])
            elif isinstance(_args[0], VBase2D):
                return self._VBase2D__overloaded_assign_ptrLVecBase2d_ptrConstLVecBase2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._VBase2D__overloaded___getitem___ptrConstLVecBase2d_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], VBase2D):
                return self._VBase2D__overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2D> '
        elif numArgs == 2:
            if isinstance(_args[0], VBase2D):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase2D__overloaded_compareTo_ptrConstLVecBase2d_ptrConstLVecBase2d_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


