# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import VBase2D

class Point2D(VBase2D.VBase2D, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Point2D__overloaded_constructor(self):
        self.this = libpanda._inPVZN3tKnR()
        self.userManagesMemory = 1

    
    def _Point2D__overloaded_constructor_ptrConstLVecBase2d(self, copy):
        self.this = libpanda._inPVZN3kCZP(copy.this)
        self.userManagesMemory = 1

    
    def _Point2D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPVZN338Ro(fillValue)
        self.userManagesMemory = 1

    
    def _Point2D__overloaded_constructor_double_double(self, x, y):
        self.this = libpanda._inPVZN3VLaV(x, y)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3_CIK:
            libpanda._inPVZN3_CIK(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN3rnmp()
        returnObject = Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3AGP2()
        returnObject = Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3YRZ2()
        returnObject = Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def getClassType():
        returnValue = libpanda._inPVZN3mtGF()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Point2D__overloaded_assign_ptrLPoint2d_ptrConstLVecBase2d(self, copy):
        returnValue = libpanda._inPVZN39M99(self.this, copy.this)
        returnObject = Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point2D__overloaded_assign_ptrLPoint2d_double(self, fillValue):
        returnValue = libpanda._inPVZN3MH4I(self.this, fillValue)
        returnObject = Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point2D__overloaded___sub___ptrConstLPoint2d(self):
        returnValue = libpanda._inPVZN311lG(self.this)
        returnObject = Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point2D__overloaded___sub___ptrConstLPoint2d_ptrConstLPoint2d(self, other):
        returnValue = libpanda._inPVZN3NGic(self.this, other.this)
        import Vec2D
        returnObject = Vec2D.Vec2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point2D__overloaded___sub___ptrConstLPoint2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPVZN30Vlf(self.this, other.this)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point2D__overloaded___sub___ptrConstLPoint2d_ptrConstLVector2d(self, other):
        returnValue = libpanda._inPVZN3Fode(self.this, other.this)
        returnObject = Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point2D__overloaded___add___ptrConstLPoint2d_ptrConstLVecBase2d(self, other):
        returnValue = libpanda._inPVZN3vLkf(self.this, other.this)
        import VBase2D
        returnObject = VBase2D.VBase2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point2D__overloaded___add___ptrConstLPoint2d_ptrConstLVector2d(self, other):
        returnValue = libpanda._inPVZN3Cmce(self.this, other.this)
        returnObject = Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN3rAiF(self.this, scalar)
        returnObject = Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN36Vkl(self.this, scalar)
        returnObject = Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Point2D__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Point2D__overloaded_constructor_double(*_args)
            
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return self._Point2D__overloaded_constructor_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D.VBase2D> '
        elif numArgs == 2:
            return self._Point2D__overloaded_constructor_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Point2D__overloaded___sub___ptrConstLPoint2d(*_args)
        elif numArgs == 1:
            import Vec2D
            if isinstance(_args[0], Vec2D.Vec2D):
                return self._Point2D__overloaded___sub___ptrConstLPoint2d_ptrConstLVector2d(*_args)
            
            if isinstance(_args[0], Point2D):
                return self._Point2D__overloaded___sub___ptrConstLPoint2d_ptrConstLPoint2d(*_args)
            
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return self._Point2D__overloaded___sub___ptrConstLPoint2d_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec2D.Vec2D> <Point2D> <VBase2D.VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Point2D__overloaded_assign_ptrLPoint2d_double(*_args)
            
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return self._Point2D__overloaded_assign_ptrLPoint2d_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2D.VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Vec2D
            if isinstance(_args[0], Vec2D.Vec2D):
                return self._Point2D__overloaded___add___ptrConstLPoint2d_ptrConstLVector2d(*_args)
            
            import VBase2D
            if isinstance(_args[0], VBase2D.VBase2D):
                return self._Point2D__overloaded___add___ptrConstLPoint2d_ptrConstLVecBase2d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec2D.Vec2D> <VBase2D.VBase2D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


