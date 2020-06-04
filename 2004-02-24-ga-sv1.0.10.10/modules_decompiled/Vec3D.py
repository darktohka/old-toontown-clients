# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase3D

class Vec3D(VBase3D.VBase3D, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Vec3D__overloaded_constructor(self):
        self.this = libpanda._inPUZN3Ayhn()
        self.userManagesMemory = 1

    
    def _Vec3D__overloaded_constructor_ptrConstLVecBase3d(self, copy):
        self.this = libpanda._inPUZN3vfOH(copy.this)
        self.userManagesMemory = 1

    
    def _Vec3D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPUZN3vhGS(fillValue)
        self.userManagesMemory = 1

    
    def _Vec3D__overloaded_constructor_double_double_double(self, x, y, z):
        self.this = libpanda._inPUZN38Wm1(x, y, z)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3IvLs:
            libpanda._inPUZN3IvLs(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN32lRk()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3o3Z5()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3obR_()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPUZN3o_KD()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def _Vec3D__overloaded_up___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPUZN3_N5k(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_up___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_up___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_up():
        returnValue = libpanda._inPUZN3I8sB()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_up = staticmethod(_Vec3D__overloaded_up)
    
    def _Vec3D__overloaded_right___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPUZN3RtOm(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_right___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_right___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_right():
        returnValue = libpanda._inPUZN3xMXe()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_right = staticmethod(_Vec3D__overloaded_right)
    
    def _Vec3D__overloaded_forward___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPUZN39FXy(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_forward___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_forward___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_forward():
        returnValue = libpanda._inPUZN3OT7r()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_forward = staticmethod(_Vec3D__overloaded_forward)
    
    def _Vec3D__overloaded_down___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPUZN3gtYb(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_down___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_down___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_down():
        returnValue = libpanda._inPUZN3KBKd()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_down = staticmethod(_Vec3D__overloaded_down)
    
    def _Vec3D__overloaded_left___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPUZN32UWG(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_left___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_left___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_left():
        returnValue = libpanda._inPUZN3cxJI()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_left = staticmethod(_Vec3D__overloaded_left)
    
    def _Vec3D__overloaded_back___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPUZN3XP96(cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_back___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_back___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_back():
        returnValue = libpanda._inPUZN3Nyv8()
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_back = staticmethod(_Vec3D__overloaded_back)
    
    def _Vec3D__overloaded_rfu_double_double_double___enum__CoordinateSystem(right, fwd, up, cs):
        returnValue = libpanda._inPUZN3uPAa(right, fwd, up, cs)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_rfu_double_double_double___enum__CoordinateSystem = staticmethod(_Vec3D__overloaded_rfu_double_double_double___enum__CoordinateSystem)
    
    def _Vec3D__overloaded_rfu_double_double_double(right, fwd, up):
        returnValue = libpanda._inPUZN3mVMh(right, fwd, up)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Vec3D__overloaded_rfu_double_double_double = staticmethod(_Vec3D__overloaded_rfu_double_double_double)
    
    def getClassType():
        returnValue = libpanda._inPUZN3H5wV()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Vec3D__overloaded_assign_ptrLVector3d_ptrConstLVecBase3d(self, copy):
        returnValue = libpanda._inPUZN3yYfy(self.this, copy.this)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec3D__overloaded_assign_ptrLVector3d_double(self, fillValue):
        returnValue = libpanda._inPUZN3pe8O(self.this, fillValue)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec3D__overloaded___sub___ptrConstLVector3d(self):
        returnValue = libpanda._inPUZN3PtNF(self.this)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3D__overloaded___sub___ptrConstLVector3d_ptrConstLVecBase3d(self, other):
        returnValue = libpanda._inPUZN3OpRn(self.this, other.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3D__overloaded___sub___ptrConstLVector3d_ptrConstLVector3d(self, other):
        returnValue = libpanda._inPUZN3Ts7B(self.this, other.this)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3D__overloaded___add___ptrConstLVector3d_ptrConstLVecBase3d(self, other):
        returnValue = libpanda._inPUZN3uqqm(self.this, other.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec3D__overloaded___add___ptrConstLVector3d_ptrConstLVector3d(self, other):
        returnValue = libpanda._inPUZN3zxUB(self.this, other.this)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def length(self):
        returnValue = libpanda._inPUZN3ctoh(self.this)
        return returnValue

    
    def lengthSquared(self):
        returnValue = libpanda._inPUZN3pMn8(self.this)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPUZN3UBTq(self.this)
        return returnValue

    
    def cross(self, other):
        returnValue = libpanda._inPUZN3Ozz8(self.this, other.this)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3954j(self.this, scalar)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3tQal(self.this, scalar)
        returnObject = Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def down(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_down()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return Vec3D._Vec3D__overloaded_down___enum__CoordinateSystem(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    down = staticmethod(down)
    
    def right(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_right()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return Vec3D._Vec3D__overloaded_right___enum__CoordinateSystem(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    right = staticmethod(right)
    
    def rfu(*_args):
        numArgs = len(_args)
        if numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return Vec3D._Vec3D__overloaded_rfu_double_double_double(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.IntType):
                            return Vec3D._Vec3D__overloaded_rfu_double_double_double___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '

    rfu = staticmethod(rfu)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec3D__overloaded_constructor()
        elif numArgs == 1:
            import VBase3D
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Vec3D__overloaded_constructor_double(_args[0])
            elif isinstance(_args[0], VBase3D.VBase3D):
                return self._Vec3D__overloaded_constructor_ptrConstLVecBase3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._Vec3D__overloaded_constructor_double_double_double(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

    
    def forward(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_forward()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return Vec3D._Vec3D__overloaded_forward___enum__CoordinateSystem(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    forward = staticmethod(forward)
    
    def left(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_left()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return Vec3D._Vec3D__overloaded_left___enum__CoordinateSystem(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    left = staticmethod(left)
    
    def back(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_back()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return Vec3D._Vec3D__overloaded_back___enum__CoordinateSystem(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    back = staticmethod(back)
    
    def up(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Vec3D._Vec3D__overloaded_up()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return Vec3D._Vec3D__overloaded_up___enum__CoordinateSystem(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    up = staticmethod(up)
    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec3D__overloaded___sub___ptrConstLVector3d()
        elif numArgs == 1:
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return self._Vec3D__overloaded___sub___ptrConstLVector3d_ptrConstLVecBase3d(_args[0])
            elif isinstance(_args[0], Vec3D):
                return self._Vec3D__overloaded___sub___ptrConstLVector3d_ptrConstLVector3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <Vec3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3D
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Vec3D__overloaded_assign_ptrLVector3d_double(_args[0])
            elif isinstance(_args[0], VBase3D.VBase3D):
                return self._Vec3D__overloaded_assign_ptrLVector3d_ptrConstLVecBase3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return self._Vec3D__overloaded___add___ptrConstLVector3d_ptrConstLVecBase3d(_args[0])
            elif isinstance(_args[0], Vec3D):
                return self._Vec3D__overloaded___add___ptrConstLVector3d_ptrConstLVector3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <Vec3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


