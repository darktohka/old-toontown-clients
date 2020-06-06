# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class VBase4(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _VBase4__overloaded_constructor(self):
        self.this = libpanda._inPUZN35kRY()
        self.userManagesMemory = 1

    
    def _VBase4__overloaded_constructor_ptrConstLVecBase4f(self, copy):
        self.this = libpanda._inPUZN3dTtd(copy.this)
        self.userManagesMemory = 1

    
    def _VBase4__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPUZN3dsy7(fillValue)
        self.userManagesMemory = 1

    
    def _VBase4__overloaded_constructor_float_float_float_float(self, x, y, z, w):
        self.this = libpanda._inPUZN3DRvG(x, y, z, w)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3wsFk:
            libpanda._inPUZN3wsFk(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN3mHPT()
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3yCF3()
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3MdTT()
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPUZN3Pdhv()
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def unitW():
        returnValue = libpanda._inPUZN33C3a()
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitW = staticmethod(unitW)
    
    def getClassType():
        returnValue = libpanda._inPUZN3hKuD()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _VBase4__overloaded_assign_ptrLVecBase4f_ptrConstLVecBase4f(self, copy):
        returnValue = libpanda._inPUZN3XuCG(self.this, copy.this)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase4__overloaded_assign_ptrLVecBase4f_float(self, fillValue):
        returnValue = libpanda._inPUZN3HYHk(self.this, fillValue)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _VBase4__overloaded___getitem___ptrLVecBase4f_int(self, i):
        returnValue = libpanda._inPUZN3Ay34(self.this, i)
        return returnValue

    
    def _VBase4__overloaded___getitem___ptrConstLVecBase4f_int(self, i):
        returnValue = libpanda._inPUZN3TrrV(self.this, i)
        return returnValue

    
    def isNan(self):
        returnValue = libpanda._inPUZN3x62D(self.this)
        return returnValue

    
    def getCell(self, i):
        returnValue = libpanda._inPUZN3a_Pp(self.this, i)
        return returnValue

    
    def getX(self):
        returnValue = libpanda._inPUZN3JYvU(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPUZN3J8oZ(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPUZN3JQge(self.this)
        return returnValue

    
    def getW(self):
        returnValue = libpanda._inPUZN3JE3P(self.this)
        return returnValue

    
    def setCell(self, i, value):
        returnValue = libpanda._inPUZN3AQHX(self.this, i, value)
        return returnValue

    
    def setX(self, value):
        returnValue = libpanda._inPUZN3IuJp(self.this, value)
        return returnValue

    
    def setY(self, value):
        returnValue = libpanda._inPUZN3IKCu(self.this, value)
        return returnValue

    
    def setZ(self, value):
        returnValue = libpanda._inPUZN3IW6y(self.this, value)
        return returnValue

    
    def setW(self, value):
        returnValue = libpanda._inPUZN3ICRk(self.this, value)
        return returnValue

    
    def getData(self):
        returnValue = libpanda._inPUZN3XRyH(self.this)
        return returnValue

    
    def getNumComponents(self):
        returnValue = libpanda._inPUZN31F36(self.this)
        return returnValue

    
    def fill(self, fillValue):
        returnValue = libpanda._inPUZN3W1HJ(self.this, fillValue)
        return returnValue

    
    def set(self, x, y, z, w):
        returnValue = libpanda._inPUZN3__rX(self.this, x, y, z, w)
        return returnValue

    
    def dot(self, other):
        returnValue = libpanda._inPUZN33052(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPUZN32lvx(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPUZN3duYz(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPUZN3ZOAi(self.this, other.this)
        return returnValue

    
    def _VBase4__overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPUZN3iXnx(self.this, other.this)
        return returnValue

    
    def _VBase4__overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f_float(self, other, threshold):
        returnValue = libpanda._inPUZN3IZYW(self.this, other.this, threshold)
        return returnValue

    
    def _VBase4__overloaded___sub___ptrConstLVecBase4f(self):
        returnValue = libpanda._inPUZN3OOux(self.this)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _VBase4__overloaded___sub___ptrConstLVecBase4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPUZN3zdSf(self.this, other.this)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __add__(self, other):
        returnValue = libpanda._inPUZN3ztwL(self.this, other.this)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3reVF(self.this, scalar)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3s2J2(self.this, scalar)
        returnObject = VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iadd__(self, other):
        returnValue = libpanda._inPUZN3tr3T(self.this, other.this)
        return self

    
    def __isub__(self, other):
        returnValue = libpanda._inPUZN3ubZn(self.this, other.this)
        return self

    
    def __imul__(self, scalar):
        returnValue = libpanda._inPUZN37ZPM(self.this, scalar)
        return self

    
    def __idiv__(self, scalar):
        returnValue = libpanda._inPUZN36hD9(self.this, scalar)
        return self

    
    def _VBase4__overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPUZN3zKzg(self.this, other.this)
        return returnValue

    
    def _VBase4__overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f_float(self, other, threshold):
        returnValue = libpanda._inPUZN3__lQ(self.this, other.this, threshold)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPUZN3QPcK(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase4__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._VBase4__overloaded_constructor_float(_args[0])
            elif isinstance(_args[0], VBase4):
                return self._VBase4__overloaded_constructor_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._VBase4__overloaded_constructor_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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
            if isinstance(_args[0], VBase4):
                return self._VBase4__overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4> '
        elif numArgs == 2:
            if isinstance(_args[0], VBase4):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase4__overloaded_almostEqual_ptrConstLVecBase4f_ptrConstLVecBase4f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._VBase4__overloaded___sub___ptrConstLVecBase4f()
        elif numArgs == 1:
            if isinstance(_args[0], VBase4):
                return self._VBase4__overloaded___sub___ptrConstLVecBase4f_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._VBase4__overloaded_assign_ptrLVecBase4f_float(_args[0])
            elif isinstance(_args[0], VBase4):
                return self._VBase4__overloaded_assign_ptrLVecBase4f_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __getitem__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._VBase4__overloaded___getitem___ptrConstLVecBase4f_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def compareTo(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], VBase4):
                return self._VBase4__overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4> '
        elif numArgs == 2:
            if isinstance(_args[0], VBase4):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._VBase4__overloaded_compareTo_ptrConstLVecBase4f_ptrConstLVecBase4f_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


