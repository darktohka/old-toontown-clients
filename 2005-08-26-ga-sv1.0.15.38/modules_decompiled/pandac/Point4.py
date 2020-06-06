# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import VBase4

class Point4(VBase4.VBase4, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Point4__overloaded_constructor(self):
        self.this = libpanda._inPVZN3zUXk()
        self.userManagesMemory = 1

    
    def _Point4__overloaded_constructor_ptrConstLVecBase4f(self, copy):
        self.this = libpanda._inPVZN3SD57(copy.this)
        self.userManagesMemory = 1

    
    def _Point4__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPVZN3Cj8c(fillValue)
        self.userManagesMemory = 1

    
    def _Point4__overloaded_constructor_float_float_float_float(self, x, y, z, w):
        self.this = libpanda._inPVZN3zr8M(x, y, z, w)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3Q5Hh:
            libpanda._inPVZN3Q5Hh(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN3q1J6()
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3C0yG()
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3aH8G()
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPVZN3SWGH()
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def unitW():
        returnValue = libpanda._inPVZN3KloG()
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitW = staticmethod(unitW)
    
    def getClassType():
        returnValue = libpanda._inPVZN3nbpV()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Point4__overloaded_assign_ptrLPoint4f_ptrConstLVecBase4f(self, copy):
        returnValue = libpanda._inPVZN3bZBR(self.this, copy.this)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point4__overloaded_assign_ptrLPoint4f_float(self, fillValue):
        returnValue = libpanda._inPVZN3qdAN(self.this, fillValue)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point4__overloaded___sub___ptrConstLPoint4f(self):
        returnValue = libpanda._inPVZN30LJX(self.this)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLPoint4f(self, other):
        returnValue = libpanda._inPVZN3MM2G(self.this, other.this)
        import Vec4
        returnObject = Vec4.Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPVZN3Tupy(self.this, other.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLVector4f(self, other):
        returnValue = libpanda._inPVZN3XbFn(self.this, other.this)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4__overloaded___add___ptrConstLPoint4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPVZN3Icoy(self.this, other.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4__overloaded___add___ptrConstLPoint4f_ptrConstLVector4f(self, other):
        returnValue = libpanda._inPVZN3opEn(self.this, other.this)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN3Udt9(self.this, scalar)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3rXwd(self.this, scalar)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Point4__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Point4__overloaded_constructor_float(*_args)
            
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._Point4__overloaded_constructor_ptrConstLVecBase4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4.VBase4> '
        elif numArgs == 4:
            return self._Point4__overloaded_constructor_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 4 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Point4__overloaded___sub___ptrConstLPoint4f(*_args)
        elif numArgs == 1:
            import Vec4
            if isinstance(_args[0], Vec4.Vec4):
                return self._Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLVector4f(*_args)
            
            if isinstance(_args[0], Point4):
                return self._Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLPoint4f(*_args)
            
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLVecBase4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec4.Vec4> <Point4> <VBase4.VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Point4__overloaded_assign_ptrLPoint4f_float(*_args)
            
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._Point4__overloaded_assign_ptrLPoint4f_ptrConstLVecBase4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4.VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Vec4
            if isinstance(_args[0], Vec4.Vec4):
                return self._Point4__overloaded___add___ptrConstLPoint4f_ptrConstLVector4f(*_args)
            
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._Point4__overloaded___add___ptrConstLPoint4f_ptrConstLVecBase4f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec4.Vec4> <VBase4.VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


