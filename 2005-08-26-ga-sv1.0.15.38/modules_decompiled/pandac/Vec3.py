# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import VBase3

class Vec3(VBase3.VBase3, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Vec3__overloaded_constructor(self):
        self.this = libpanda._inPVZN3hACr()
        self.userManagesMemory = 1

    
    def _Vec3__overloaded_constructor_ptrConstLVecBase3f(self, copy):
        self.this = libpanda._inPVZN3Z8LN(copy.this)
        self.userManagesMemory = 1

    
    def _Vec3__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPVZN36OMJ(fillValue)
        self.userManagesMemory = 1

    
    def _Vec3__overloaded_constructor_float_float_float(self, x, y, z):
        self.this = libpanda._inPVZN3hp6I(x, y, z)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3GySw:
            libpanda._inPVZN3GySw(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN3Mixn()
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3yo58()
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3xExB()
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPVZN3xgqG()
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def _Vec3__overloaded_up___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN3lOZo(cs)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_up___enum__CoordinateSystem = staticmethod(_Vec3__overloaded_up___enum__CoordinateSystem)
    
    def _Vec3__overloaded_up():
        returnValue = libpanda._inPVZN3z_MF()
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_up = staticmethod(_Vec3__overloaded_up)
    
    def _Vec3__overloaded_right___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN33sup(cs)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_right___enum__CoordinateSystem = staticmethod(_Vec3__overloaded_right___enum__CoordinateSystem)
    
    def _Vec3__overloaded_right():
        returnValue = libpanda._inPVZN3YM3h()
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_right = staticmethod(_Vec3__overloaded_right)
    
    def _Vec3__overloaded_forward___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN3n621(cs)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_forward___enum__CoordinateSystem = staticmethod(_Vec3__overloaded_forward___enum__CoordinateSystem)
    
    def _Vec3__overloaded_forward():
        returnValue = libpanda._inPVZN3oQbv()
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_forward = staticmethod(_Vec3__overloaded_forward)
    
    def _Vec3__overloaded_down___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN35s4e(cs)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_down___enum__CoordinateSystem = staticmethod(_Vec3__overloaded_down___enum__CoordinateSystem)
    
    def _Vec3__overloaded_down():
        returnValue = libpanda._inPVZN3jBqg()
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_down = staticmethod(_Vec3__overloaded_down)
    
    def _Vec3__overloaded_left___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN3vT2J(cs)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_left___enum__CoordinateSystem = staticmethod(_Vec3__overloaded_left___enum__CoordinateSystem)
    
    def _Vec3__overloaded_left():
        returnValue = libpanda._inPVZN31_pL()
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_left = staticmethod(_Vec3__overloaded_left)
    
    def _Vec3__overloaded_back___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN3xPd_(cs)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_back___enum__CoordinateSystem = staticmethod(_Vec3__overloaded_back___enum__CoordinateSystem)
    
    def _Vec3__overloaded_back():
        returnValue = libpanda._inPVZN3UzPA()
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_back = staticmethod(_Vec3__overloaded_back)
    
    def _Vec3__overloaded_rfu_float_float_float___enum__CoordinateSystem(right, fwd, up, cs):
        returnValue = libpanda._inPVZN3hSqR(right, fwd, up, cs)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_rfu_float_float_float___enum__CoordinateSystem = staticmethod(_Vec3__overloaded_rfu_float_float_float___enum__CoordinateSystem)
    
    def _Vec3__overloaded_rfu_float_float_float(right, fwd, up):
        returnValue = libpanda._inPVZN3UW9c(right, fwd, up)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3__overloaded_rfu_float_float_float = staticmethod(_Vec3__overloaded_rfu_float_float_float)
    
    def getClassType():
        returnValue = libpanda._inPVZN3g4QZ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Vec3__overloaded_assign_ptrLVector3f_ptrConstLVecBase3f(self, copy):
        returnValue = libpanda._inPVZN3qZGE(self.this, copy.this)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec3__overloaded_assign_ptrLVector3f_float(self, fillValue):
        returnValue = libpanda._inPVZN3R_QE(self.this, fillValue)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec3__overloaded___sub___ptrConstLVector3f(self):
        returnValue = libpanda._inPVZN3WstI(self.this)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3__overloaded___sub___ptrConstLVector3f_ptrConstLVecBase3f(self, other):
        returnValue = libpanda._inPVZN3po44(self.this, other.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3__overloaded___sub___ptrConstLVector3f_ptrConstLVector3f(self, other):
        returnValue = libpanda._inPVZN38f3H(self.this, other.this)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3__overloaded___add___ptrConstLVector3f_ptrConstLVecBase3f(self, other):
        returnValue = libpanda._inPVZN3JrR4(self.this, other.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3__overloaded___add___ptrConstLVector3f_ptrConstLVector3f(self, other):
        returnValue = libpanda._inPVZN3ciQH(self.this, other.this)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def length(self):
        returnValue = libpanda._inPVZN3iiIl(self.this)
        return returnValue

    
    def lengthSquared(self):
        returnValue = libpanda._inPVZN3CMHA(self.this)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPVZN3uAzt(self.this)
        return returnValue

    
    def cross(self, other):
        returnValue = libpanda._inPVZN3XSXn(self.this, other.this)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def angleRad(self, other):
        returnValue = libpanda._inPVZN3i1_1(self.this, other.this)
        return returnValue

    
    def angleDeg(self, other):
        returnValue = libpanda._inPVZN3Se7m(self.this, other.this)
        return returnValue

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN3cvTb(self.this, scalar)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3sH0c(self.this, scalar)
        returnObject = Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def down(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3._Vec3__overloaded_down(*_args)
        elif numArgs == 1:
            return Vec3._Vec3__overloaded_down___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    down = staticmethod(down)
    
    def right(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3._Vec3__overloaded_right(*_args)
        elif numArgs == 1:
            return Vec3._Vec3__overloaded_right___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    right = staticmethod(right)
    
    def rfu(*_args):
        numArgs = len(_args)
        if numArgs == 3:
            return Vec3._Vec3__overloaded_rfu_float_float_float(*_args)
        elif numArgs == 4:
            return Vec3._Vec3__overloaded_rfu_float_float_float___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

    rfu = staticmethod(rfu)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec3__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Vec3__overloaded_constructor_float(*_args)
            
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._Vec3__overloaded_constructor_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        elif numArgs == 3:
            return self._Vec3__overloaded_constructor_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

    
    def forward(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3._Vec3__overloaded_forward(*_args)
        elif numArgs == 1:
            return Vec3._Vec3__overloaded_forward___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    forward = staticmethod(forward)
    
    def left(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3._Vec3__overloaded_left(*_args)
        elif numArgs == 1:
            return Vec3._Vec3__overloaded_left___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    left = staticmethod(left)
    
    def back(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3._Vec3__overloaded_back(*_args)
        elif numArgs == 1:
            return Vec3._Vec3__overloaded_back___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    back = staticmethod(back)
    
    def up(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3._Vec3__overloaded_up(*_args)
        elif numArgs == 1:
            return Vec3._Vec3__overloaded_up___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    up = staticmethod(up)
    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec3__overloaded___sub___ptrConstLVector3f(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], Vec3):
                return self._Vec3__overloaded___sub___ptrConstLVector3f_ptrConstLVector3f(*_args)
            
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._Vec3__overloaded___sub___ptrConstLVector3f_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec3> <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Vec3__overloaded_assign_ptrLVector3f_float(*_args)
            
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._Vec3__overloaded_assign_ptrLVector3f_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Vec3):
                return self._Vec3__overloaded___add___ptrConstLVector3f_ptrConstLVector3f(*_args)
            
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._Vec3__overloaded___add___ptrConstLVector3f_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec3> <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


