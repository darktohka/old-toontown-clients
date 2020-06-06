# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase2

class Point2(VBase2.VBase2, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Point2__overloaded_constructor(self):
        self.this = libpanda._inPUZN3zKKY()
        self.userManagesMemory = 1

    
    def _Point2__overloaded_constructor_ptrConstLVecBase2f(self, copy):
        self.this = libpanda._inPUZN3tY8N(copy.this)
        self.userManagesMemory = 1

    
    def _Point2__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPUZN3CtvQ(fillValue)
        self.userManagesMemory = 1

    
    def _Point2__overloaded_constructor_float_float(self, x, y):
        self.this = libpanda._inPUZN3qlQB(x, y)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3cPPm:
            libpanda._inPUZN3cPPm(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN3lnt3()
        returnObject = Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3CGWE()
        returnObject = Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3aRgE()
        returnObject = Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def getClassType():
        returnValue = libpanda._inPUZN3ntNT()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Point2__overloaded_assign_ptrLPoint2f_ptrConstLVecBase2f(self, copy):
        returnValue = libpanda._inPUZN3_egO(self.this, copy.this)
        returnObject = Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point2__overloaded_assign_ptrLPoint2f_float(self, fillValue):
        returnValue = libpanda._inPUZN3qvjK(self.this, fillValue)
        returnObject = Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point2__overloaded___sub___ptrConstLPoint2f(self):
        returnValue = libpanda._inPUZN301sU(self.this)
        returnObject = Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point2__overloaded___sub___ptrConstLPoint2f_ptrConstLPoint2f(self, other):
        returnValue = libpanda._inPUZN3ZCqi(self.this, other.this)
        import Vec2
        returnObject = Vec2.Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point2__overloaded___sub___ptrConstLPoint2f_ptrConstLVecBase2f(self, other):
        returnValue = libpanda._inPUZN32nIw(self.this, other.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point2__overloaded___sub___ptrConstLPoint2f_ptrConstLVector2f(self, other):
        returnValue = libpanda._inPUZN3ngps(self.this, other.this)
        returnObject = Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point2__overloaded___add___ptrConstLPoint2f_ptrConstLVecBase2f(self, other):
        returnValue = libpanda._inPUZN3tVHw(self.this, other.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point2__overloaded___add___ptrConstLPoint2f_ptrConstLVector2f(self, other):
        returnValue = libpanda._inPUZN3Y_os(self.this, other.this)
        returnObject = Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3VLR7(self.this, scalar)
        returnObject = Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3rFUb(self.this, scalar)
        returnObject = Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Point2__overloaded_constructor()
        elif numArgs == 1:
            import VBase2
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Point2__overloaded_constructor_float(_args[0])
            elif isinstance(_args[0], VBase2.VBase2):
                return self._Point2__overloaded_constructor_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2.VBase2> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Point2__overloaded_constructor_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Point2__overloaded___sub___ptrConstLPoint2f()
        elif numArgs == 1:
            import VBase2
            import Vec2
            if isinstance(_args[0], VBase2.VBase2):
                return self._Point2__overloaded___sub___ptrConstLPoint2f_ptrConstLVecBase2f(_args[0])
            elif isinstance(_args[0], Vec2.Vec2):
                return self._Point2__overloaded___sub___ptrConstLPoint2f_ptrConstLVector2f(_args[0])
            elif isinstance(_args[0], Point2):
                return self._Point2__overloaded___sub___ptrConstLPoint2f_ptrConstLPoint2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2.VBase2> <Vec2.Vec2> <Point2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase2
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Point2__overloaded_assign_ptrLPoint2f_float(_args[0])
            elif isinstance(_args[0], VBase2.VBase2):
                return self._Point2__overloaded_assign_ptrLPoint2f_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2.VBase2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase2
            import Vec2
            if isinstance(_args[0], VBase2.VBase2):
                return self._Point2__overloaded___add___ptrConstLPoint2f_ptrConstLVecBase2f(_args[0])
            elif isinstance(_args[0], Vec2.Vec2):
                return self._Point2__overloaded___add___ptrConstLPoint2f_ptrConstLVector2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2.VBase2> <Vec2.Vec2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


