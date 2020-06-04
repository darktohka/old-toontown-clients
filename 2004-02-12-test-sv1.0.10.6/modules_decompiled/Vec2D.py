# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase2D

class Vec2D(VBase2D.VBase2D, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Vec2D__overloaded_constructor(self):
        self.this = libpanda._inPUZN3xcd5()
        self.userManagesMemory = 1

    
    def _Vec2D__overloaded_constructor_ptrConstLVecBase2d(self, copy):
        self.this = libpanda._inPUZN3qdIZ(copy.this)
        self.userManagesMemory = 1

    
    def _Vec2D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPUZN3RGDk(fillValue)
        self.userManagesMemory = 1

    
    def _Vec2D__overloaded_constructor_double_double(self, x, y):
        self.this = libpanda._inPUZN3Ay7S(x, y)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3FoGl:
            libpanda._inPUZN3FoGl(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN33FN9()
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3pXVS()
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3p7OX()
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def getClassType():
        returnValue = libpanda._inPUZN3HZsu()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Vec2D__overloaded_assign_ptrLVector2d_ptrConstLVecBase2d(self, copy):
        returnValue = libpanda._inPUZN3zhOK(self.this, copy.this)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec2D__overloaded_assign_ptrLVector2d_double(self, fillValue):
        returnValue = libpanda._inPUZN3p_5n(self.this, fillValue)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec2D__overloaded___sub___ptrConstLVector2d(self):
        returnValue = libpanda._inPUZN3ONJe(self.this)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2D__overloaded___sub___ptrConstLVector2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPUZN3BO__(self.this, other.this)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2D__overloaded___sub___ptrConstLVector2d_ptrConstLVector2d(self, other):
        returnValue = libpanda._inPUZN3qo1a(self.this, other.this)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2D__overloaded___add___ptrConstLVector2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPUZN3hDY_(self.this, other.this)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2D__overloaded___add___ptrConstLVector2d_ptrConstLVector2d(self, other):
        returnValue = libpanda._inPUZN3KsOa(self.this, other.this)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def length(self):
        returnValue = libpanda._inPUZN3bNl6(self.this)
        return returnValue

    
    def lengthSquared(self):
        returnValue = libpanda._inPUZN3qsjV(self.this)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPUZN3XhQD(self.this)
        return returnValue

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3_Z18(self.this, scalar)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3uwW_(self.this, scalar)
        returnObject = Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec2D__overloaded_constructor()
        elif numArgs == 1:
            import VBase2D
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Vec2D__overloaded_constructor_double(_args[0])
            elif isinstance(_args[0], VBase2D.VBase2D):
                return self._Vec2D__overloaded_constructor_ptrConstLVecBase2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D.VBase2D> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Vec2D__overloaded_constructor_double_double(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec2D__overloaded___sub___ptrConstLVector2d()
        elif numArgs == 1:
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return self._Vec2D__overloaded___sub___ptrConstLVector2d_ptrConstLVecBase2d(_args[0])
            elif isinstance(_args[0], Vec2D):
                return self._Vec2D__overloaded___sub___ptrConstLVector2d_ptrConstLVector2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2D.VBase2D> <Vec2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase2D
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Vec2D__overloaded_assign_ptrLVector2d_double(_args[0])
            elif isinstance(_args[0], VBase2D.VBase2D):
                return self._Vec2D__overloaded_assign_ptrLVector2d_ptrConstLVecBase2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D.VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return self._Vec2D__overloaded___add___ptrConstLVector2d_ptrConstLVecBase2d(_args[0])
            elif isinstance(_args[0], Vec2D):
                return self._Vec2D__overloaded___add___ptrConstLVector2d_ptrConstLVector2d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2D.VBase2D> <Vec2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


