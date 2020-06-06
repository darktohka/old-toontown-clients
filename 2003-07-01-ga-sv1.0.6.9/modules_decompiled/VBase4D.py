# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class VBase4D(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _VBase4D__overloaded_constructor(self):
        self.this = libpanda._inPUZN3fAuU()
        self.userManagesMemory = 1

    
    def _VBase4D__overloaded_constructor_ptrConstLVecBase4d(self, copy):
        self.this = libpanda._inPUZN3KfrW(copy.this)
        self.userManagesMemory = 1

    
    def _VBase4D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPUZN36BJ_(fillValue)
        self.userManagesMemory = 1

    
    def _VBase4D__overloaded_constructor_double_double_double_double(self, x, y, z, w):
        self.this = libpanda._inPUZN3GENf(x, y, z, w)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3E_ND:
            libpanda._inPUZN3E_ND(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN3ZrPj()
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3QxFH()
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3TxTj()
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPUZN3txh_()
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def unitW():
        returnValue = libpanda._inPUZN3Wx3q()
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitW = staticmethod(unitW)
    
    def getClassType():
        returnValue = libpanda._inPUZN3GAvT()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase4D__overloaded_assign_ptrLVecBase4d_ptrConstLVecBase4d(self, copy):
        returnValue = libpanda._inPUZN3e6iS(self.this, copy.this)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase4D__overloaded_assign_ptrLVecBase4d_double(self, fillValue):
        returnValue = libpanda._inPUZN3LM_5(self.this, fillValue)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase4D__overloaded___getitem___ptrLVecBase4d_int(self, i):
        returnValue = libpanda._inPUZN3mm3I(self.this, i)
        return returnValue

    
    def _VBase4D__overloaded___getitem___ptrConstLVecBase4d_int(self, i):
        returnValue = libpanda._inPUZN30Hrl(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPUZN3Pu2T(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPUZN38qP5(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPUZN3otvk(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPUZN3oJop(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPUZN3olgu(self.this)
        return returnValue

    
    def getW(self):
        returnValue = libpanda._inPUZN3rx3f(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPUZN3f_AA(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPUZN3jGFc(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPUZN3ii9g(self.this, value)
        return returnValue

    
    def setZ(self, value):
        returnValue = libpanda._inPUZN3ie2l(self.this, value)
        return returnValue

    
    def setW(self, value):
        returnValue = libpanda._inPUZN3jqMX(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPUZN3x8zX(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPUZN3Xx2K(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPUZN3EbMg(self.this, fillValue)
        return returnValue

    
    def set(self, x, y, z, w):
        returnValue = libpanda._inPUZN3dT7O(self.this, x, y, z, w)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPUZN3VfrF(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPUZN3wfP_(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPUZN3eFYT(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPUZN3alAC(self.this, other.this)
        return returnValue

    
    def _VBase4D__overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d(self, other):
        returnValue = libpanda._inPUZN31LH_(self.this, other.this)
        return returnValue

    
    def _VBase4D__overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d_double(self, other, threshold):
        returnValue = libpanda._inPUZN3319I(self.this, other.this, threshold)
        return returnValue

    
    def _VBase4D__overloaded___sub___ptrConstLVecBase4d(self):
        returnValue = libpanda._inPUZN3QyvB(self.this)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase4D__overloaded___sub___ptrConstLVecBase4d_ptrConstLVecBase4d(self, other):
        returnValue = libpanda._inPUZN3ynyr(self.this, other.this)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPUZN3tXQY(self.this, other.this)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3W_WY(self.this, scalar)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3XWNJ(self.this, scalar)
        returnObject = VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPUZN3iw2z(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPUZN3iAYH(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPUZN35DXY(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPUZN3_7LJ(self.this, scalar)
        return self

    
    def _VBase4D__overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d(self, other):
        returnValue = libpanda._inPUZN3doqw(self.this, other.this)
        return returnValue

    
    def _VBase4D__overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d_double(self, other, threshold):
        returnValue = libpanda._inPUZN39ILB(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPUZN31Bda(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase4D__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._VBase4D__overloaded_constructor_double(_args[0])
            elif isinstance(_args[0], VBase4D):
                return self._VBase4D__overloaded_constructor_ptrConstLVecBase4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._VBase4D__overloaded_constructor_double_double_double_double(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 4 '

    
    def almostEqual(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], VBase4D):
                return self._VBase4D__overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4D> '
        elif numArgs == 2:
            if isinstance(_args[0], VBase4D):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase4D__overloaded_almostEqual_ptrConstLVecBase4d_ptrConstLVecBase4d_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase4D__overloaded___sub___ptrConstLVecBase4d()
        elif numArgs == 1:
            if isinstance(_args[0], VBase4D):
                return self._VBase4D__overloaded___sub___ptrConstLVecBase4d_ptrConstLVecBase4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._VBase4D__overloaded_assign_ptrLVecBase4d_double(_args[0])
            elif isinstance(_args[0], VBase4D):
                return self._VBase4D__overloaded_assign_ptrLVecBase4d_ptrConstLVecBase4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._VBase4D__overloaded___getitem___ptrConstLVecBase4d_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], VBase4D):
                return self._VBase4D__overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4D> '
        elif numArgs == 2:
            if isinstance(_args[0], VBase4D):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase4D__overloaded_compareTo_ptrConstLVecBase4d_ptrConstLVecBase4d_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


