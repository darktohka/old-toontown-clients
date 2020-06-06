# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import VBase2D

class Vec2D(VBase2D.VBase2D, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Vec2D__overloaded_constructor(self):
        self.this = libpanda._inPVZN3wcd5()
        self.userManagesMemory = 1

    
    def _Vec2D__overloaded_constructor_ptrConstLVecBase2d(self, copy):
        self.this = libpanda._inPVZN3qdIZ(copy.this)
        self.userManagesMemory = 1

    
    def _Vec2D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPVZN3eGDk(fillValue)
        self.userManagesMemory = 1

    
    def _Vec2D__overloaded_constructor_double_double(self, x, y):
        self.this = libpanda._inPVZN3Ay7S(x, y)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3KoGl:
            libpanda._inPVZN3KoGl(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN30FN9()
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3pXVS()
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3p7OX()
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def getClassType():
        returnValue = libpanda._inPVZN34Zsu()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Vec2D__overloaded_assign_ptrLVector2d_ptrConstLVecBase2d(self, copy):
        returnValue = libpanda._inPVZN3zhOK(self.this, copy.this)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec2D__overloaded_assign_ptrLVector2d_double(self, fillValue):
        returnValue = libpanda._inPVZN32_5n(self.this, fillValue)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec2D__overloaded___sub___ptrConstLVector2d(self):
        returnValue = libpanda._inPVZN3ONJe(self.this)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2D__overloaded___sub___ptrConstLVector2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPVZN3AO__(self.this, other.this)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2D__overloaded___sub___ptrConstLVector2d_ptrConstLVector2d(self, other):
        returnValue = libpanda._inPVZN3qo1a(self.this, other.this)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2D__overloaded___add___ptrConstLVector2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPVZN3gDY_(self.this, other.this)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2D__overloaded___add___ptrConstLVector2d_ptrConstLVector2d(self, other):
        returnValue = libpanda._inPVZN3KsOa(self.this, other.this)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def length(self):
        returnValue = libpanda._inPVZN3aNl6(self.this)
        return returnValue

    
    def lengthSquared(self):
        returnValue = libpanda._inPVZN3qsjV(self.this)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPVZN3XhQD(self.this)
        return returnValue

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN3_Z18(self.this, scalar)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3vwW_(self.this, scalar)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec2D__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Vec2D__overloaded_constructor_double(*_args)
            
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return self._Vec2D__overloaded_constructor_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D.VBase2D> '
        elif numArgs == 2:
            return self._Vec2D__overloaded_constructor_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec2D__overloaded___sub___ptrConstLVector2d(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], Vec2D):
                return self._Vec2D__overloaded___sub___ptrConstLVector2d_ptrConstLVector2d(*_args)
            
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return self._Vec2D__overloaded___sub___ptrConstLVector2d_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec2D> <VBase2D.VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Vec2D__overloaded_assign_ptrLVector2d_double(*_args)
            
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return self._Vec2D__overloaded_assign_ptrLVector2d_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D.VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Vec2D):
                return self._Vec2D__overloaded___add___ptrConstLVector2d_ptrConstLVector2d(*_args)
            
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return self._Vec2D__overloaded___add___ptrConstLVector2d_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec2D> <VBase2D.VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


