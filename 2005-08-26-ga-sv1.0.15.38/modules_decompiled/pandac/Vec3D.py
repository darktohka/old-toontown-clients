# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import VBase3D

class Vec3D(VBase3D.VBase3D, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Vec3D__overloaded_constructor(self):
        self.this = libpanda._inPVZN3Dyhn()
        self.userManagesMemory = 1

    
    def _Vec3D__overloaded_constructor_ptrConstLVecBase3d(self, copy):
        self.this = libpanda._inPVZN3vfOH(copy.this)
        self.userManagesMemory = 1

    
    def _Vec3D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPVZN3vhGS(fillValue)
        self.userManagesMemory = 1

    
    def _Vec3D__overloaded_constructor_double_double_double(self, x, y, z):
        self.this = libpanda._inPVZN3_Wm1(x, y, z)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3JvLs:
            libpanda._inPVZN3JvLs(self.this)
        

    
    def zero():
        returnValue = libpanda._inPVZN33lRk()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPVZN3p3Z5()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPVZN3pbR_()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPVZN3o_KD()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def _Vec3D__overloaded_up___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN38N5k(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_up___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_up___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_up():
        returnValue = libpanda._inPVZN3I8sB()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_up = staticmethod(_Vec3D__overloaded_up)
    
    def _Vec3D__overloaded_right___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN3QtOm(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_right___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_right___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_right():
        returnValue = libpanda._inPVZN3xMXe()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_right = staticmethod(_Vec3D__overloaded_right)
    
    def _Vec3D__overloaded_forward___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN38FXy(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_forward___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_forward___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_forward():
        returnValue = libpanda._inPVZN3PT7r()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_forward = staticmethod(_Vec3D__overloaded_forward)
    
    def _Vec3D__overloaded_down___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN3gtYb(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_down___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_down___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_down():
        returnValue = libpanda._inPVZN3KBKd()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_down = staticmethod(_Vec3D__overloaded_down)
    
    def _Vec3D__overloaded_left___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN32UWG(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_left___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_left___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_left():
        returnValue = libpanda._inPVZN3cxJI()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_left = staticmethod(_Vec3D__overloaded_left)
    
    def _Vec3D__overloaded_back___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPVZN3WP96(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_back___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_back___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_back():
        returnValue = libpanda._inPVZN3Myv8()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_back = staticmethod(_Vec3D__overloaded_back)
    
    def _Vec3D__overloaded_rfu_double_double_double___enum__CoordinateSystem(right, fwd, up, cs):
        returnValue = libpanda._inPVZN3uPAa(right, fwd, up, cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_rfu_double_double_double___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_rfu_double_double_double___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_rfu_double_double_double(right, fwd, up):
        returnValue = libpanda._inPVZN3nVMh(right, fwd, up)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_rfu_double_double_double = staticmethod(_Vec3D__overloaded_rfu_double_double_double)
    
    def getClassType():
        returnValue = libpanda._inPVZN3H5wV()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Vec3D__overloaded_assign_ptrLVector3d_ptrConstLVecBase3d(self, copy):
        returnValue = libpanda._inPVZN3zYfy(self.this, copy.this)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec3D__overloaded_assign_ptrLVector3d_double(self, fillValue):
        returnValue = libpanda._inPVZN3pe8O(self.this, fillValue)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec3D__overloaded___sub___ptrConstLVector3d(self):
        returnValue = libpanda._inPVZN3PtNF(self.this)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3D__overloaded___sub___ptrConstLVector3d_ptrConstLVecBase3d(self, other):
        returnValue = libpanda._inPVZN3BpRn(self.this, other.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3D__overloaded___sub___ptrConstLVector3d_ptrConstLVector3d(self, other):
        returnValue = libpanda._inPVZN3Ts7B(self.this, other.this)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3D__overloaded___add___ptrConstLVector3d_ptrConstLVecBase3d(self, other):
        returnValue = libpanda._inPVZN3hqqm(self.this, other.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3D__overloaded___add___ptrConstLVector3d_ptrConstLVector3d(self, other):
        returnValue = libpanda._inPVZN3zxUB(self.this, other.this)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def length(self):
        returnValue = libpanda._inPVZN3btoh(self.this)
        return returnValue

    
    def lengthSquared(self):
        returnValue = libpanda._inPVZN3qMn8(self.this)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPVZN3XBTq(self.this)
        return returnValue

    
    def cross(self, other):
        returnValue = libpanda._inPVZN3Pzz8(self.this, other.this)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def angleRad(self, other):
        returnValue = libpanda._inPVZN3_6Zy(self.this, other.this)
        return returnValue

    
    def angleDeg(self, other):
        returnValue = libpanda._inPVZN3lnWj(self.this, other.this)
        return returnValue

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPVZN3_54j(self.this, scalar)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPVZN3uQal(self.this, scalar)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def down(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_down(*_args)
        elif numArgs == 1:
            return Vec3D._Vec3D__overloaded_down___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    down = staticmethod(down)
    
    def right(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_right(*_args)
        elif numArgs == 1:
            return Vec3D._Vec3D__overloaded_right___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    right = staticmethod(right)
    
    def rfu(*_args):
        numArgs = len(_args)
        if numArgs == 3:
            return Vec3D._Vec3D__overloaded_rfu_double_double_double(*_args)
        elif numArgs == 4:
            return Vec3D._Vec3D__overloaded_rfu_double_double_double___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

    rfu = staticmethod(rfu)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec3D__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Vec3D__overloaded_constructor_double(*_args)
            
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return self._Vec3D__overloaded_constructor_ptrConstLVecBase3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
        elif numArgs == 3:
            return self._Vec3D__overloaded_constructor_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

    
    def forward(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_forward(*_args)
        elif numArgs == 1:
            return Vec3D._Vec3D__overloaded_forward___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    forward = staticmethod(forward)
    
    def left(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_left(*_args)
        elif numArgs == 1:
            return Vec3D._Vec3D__overloaded_left___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    left = staticmethod(left)
    
    def back(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_back(*_args)
        elif numArgs == 1:
            return Vec3D._Vec3D__overloaded_back___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    back = staticmethod(back)
    
    def up(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_up(*_args)
        elif numArgs == 1:
            return Vec3D._Vec3D__overloaded_up___enum__CoordinateSystem(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    up = staticmethod(up)
    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec3D__overloaded___sub___ptrConstLVector3d(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], Vec3D):
                return self._Vec3D__overloaded___sub___ptrConstLVector3d_ptrConstLVector3d(*_args)
            
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return self._Vec3D__overloaded___sub___ptrConstLVector3d_ptrConstLVecBase3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec3D> <VBase3D.VBase3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._Vec3D__overloaded_assign_ptrLVector3d_double(*_args)
            
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return self._Vec3D__overloaded_assign_ptrLVector3d_ptrConstLVecBase3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Vec3D):
                return self._Vec3D__overloaded___add___ptrConstLVector3d_ptrConstLVector3d(*_args)
            
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return self._Vec3D__overloaded___add___ptrConstLVector3d_ptrConstLVecBase3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Vec3D> <VBase3D.VBase3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


