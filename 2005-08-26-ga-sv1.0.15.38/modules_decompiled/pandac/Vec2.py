# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import VBase2

class Vec2(VBase2.VBase2, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Vec2__overloaded_constructor(self):
        self.this = libpanda._inPVZN3Qv_8()
        self.userManagesMemory = 1

    
    def _Vec2__overloaded_constructor_ptrConstLVecBase2f(self, copy):
        self.this = libpanda._inPVZN3_wFf(copy.this)
        self.userManagesMemory = 1

    
    def _Vec2__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPVZN3tvIb(fillValue)
        self.userManagesMemory = 1

    
    def _Vec2__overloaded_constructor_float_float(self, x, y):
        self.this = libpanda._inPVZN3Os00(x, y)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3D7Pp:
            libpanda._inPVZN3D7Pp(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN3MCtA()
        returnObject = Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3yI1V()
        returnObject = Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3ykua()
        returnObject = Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def getClassType():
        returnValue = libpanda._inPVZN3hYMy()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Vec2__overloaded_assign_ptrLVector2f_ptrConstLVecBase2f(self, copy):
        returnValue = libpanda._inPVZN3rg1b(self.this, copy.this)
        returnObject = Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec2__overloaded_assign_ptrLVector2f_float(self, fillValue):
        returnValue = libpanda._inPVZN3OfPd(self.this, fillValue)
        returnObject = Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec2__overloaded___sub___ptrConstLVector2f(self):
        returnValue = libpanda._inPVZN3VMph(self.this)
        returnObject = Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2__overloaded___sub___ptrConstLVector2f_ptrConstLVecBase2f(self, other):
        returnValue = libpanda._inPVZN3pPmQ(self.this, other.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2__overloaded___sub___ptrConstLVector2f_ptrConstLVector2f(self, other):
        returnValue = libpanda._inPVZN3Dbxg(self.this, other.this)
        returnObject = Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2__overloaded___add___ptrConstLVector2f_ptrConstLVecBase2f(self, other):
        returnValue = libpanda._inPVZN3JC_P(self.this, other.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec2__overloaded___add___ptrConstLVector2f_ptrConstLVector2f(self, other):
        returnValue = libpanda._inPVZN3jfKg(self.this, other.this)
        returnObject = Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def length(self):
        returnValue = libpanda._inPVZN3hCF_(self.this)
        return returnValue

    
    def lengthSquared(self):
        returnValue = libpanda._inPVZN3DsDZ(self.this)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPVZN3ugwG(self.this)
        return returnValue

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN3dPP0(self.this, scalar)
        returnObject = Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3tnx1(self.this, scalar)
        returnObject = Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec2__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Vec2__overloaded_constructor_float(*_args)
            
            import VBase2
            if isinstance(_args[0], VBase2.VBase2):
                return self._Vec2__overloaded_constructor_ptrConstLVecBase2f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2.VBase2> '
        elif numArgs == 2:
            return self._Vec2__overloaded_constructor_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec2__overloaded___sub___ptrConstLVector2f(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], Vec2):
                return self._Vec2__overloaded___sub___ptrConstLVector2f_ptrConstLVector2f(*_args)
            
            import VBase2
            if isinstance(_args[0], VBase2.VBase2):
                return self._Vec2__overloaded___sub___ptrConstLVector2f_ptrConstLVecBase2f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec2> <VBase2.VBase2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Vec2__overloaded_assign_ptrLVector2f_float(*_args)
            
            import VBase2
            if isinstance(_args[0], VBase2.VBase2):
                return self._Vec2__overloaded_assign_ptrLVector2f_ptrConstLVecBase2f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2.VBase2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Vec2):
                return self._Vec2__overloaded___add___ptrConstLVector2f_ptrConstLVector2f(*_args)
            
            import VBase2
            if isinstance(_args[0], VBase2.VBase2):
                return self._Vec2__overloaded___add___ptrConstLVector2f_ptrConstLVecBase2f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec2> <VBase2.VBase2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


