# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase3D

class Point3D(VBase3D.VBase3D, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Point3D__overloaded_constructor(self):
        self.this = libpanda._inPUZN3t3tX()
        self.userManagesMemory = 1

    
    def _Point3D__overloaded_constructor_ptrConstLVecBase3d(self, copy):
        self.this = libpanda._inPUZN3SkXG(copy.this)
        self.userManagesMemory = 1

    
    def _Point3D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPUZN30ZYu(fillValue)
        self.userManagesMemory = 1

    
    def _Point3D__overloaded_constructor_double_double_double(self, x, y, z):
        self.this = libpanda._inPUZN3k1qU(x, y, z)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3xLkn:
            libpanda._inPUZN3xLkn(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN3qu0q()
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3BPd3()
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3Zen3()
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPUZN3Rpw3()
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def _Point3D__overloaded_origin___enum__CoordinateSystem(cs):
        returnValue = libpanda._inPUZN3WRr5(cs)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Point3D__overloaded_origin___enum__CoordinateSystem = staticmethod(_Point3D__overloaded_origin___enum__CoordinateSystem)
    
    def _Point3D__overloaded_origin():
        returnValue = libpanda._inPUZN3M1zx()
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Point3D__overloaded_origin = staticmethod(_Point3D__overloaded_origin)
    
    def _Point3D__overloaded_rfu_double_double_double___enum__CoordinateSystem(right, fwd, up, cs):
        returnValue = libpanda._inPUZN328Y0(right, fwd, up, cs)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Point3D__overloaded_rfu_double_double_double___enum__CoordinateSystem = staticmethod(_Point3D__overloaded_rfu_double_double_double___enum__CoordinateSystem)
    
    def _Point3D__overloaded_rfu_double_double_double(right, fwd, up):
        returnValue = libpanda._inPUZN3s_qG(right, fwd, up)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    _Point3D__overloaded_rfu_double_double_double = staticmethod(_Point3D__overloaded_rfu_double_double_double)
    
    def getClassType():
        returnValue = libpanda._inPUZN3mkUG()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Point3D__overloaded_assign_ptrLPoint3d_ptrConstLVecBase3d(self, copy):
        returnValue = libpanda._inPUZN3KoO_(self.this, copy.this)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point3D__overloaded_assign_ptrLPoint3d_double(self, fillValue):
        returnValue = libpanda._inPUZN3MIGK(self.this, fillValue)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point3D__overloaded___sub___ptrConstLPoint3d(self):
        returnValue = libpanda._inPUZN31M0H(self.this)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point3D__overloaded___sub___ptrConstLPoint3d_ptrConstLPoint3d(self, other):
        returnValue = libpanda._inPUZN3HBoO(self.this, other.this)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point3D__overloaded___sub___ptrConstLPoint3d_ptrConstLVecBase3d(self, other):
        returnValue = libpanda._inPUZN3B51g(self.this, other.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point3D__overloaded___sub___ptrConstLPoint3d_ptrConstLVector3d(self, other):
        returnValue = libpanda._inPUZN38fr7(self.this, other.this)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point3D__overloaded___add___ptrConstLPoint3d_ptrConstLVecBase3d(self, other):
        returnValue = libpanda._inPUZN3_u0g(self.this, other.this)
        import VBase3D
        returnObject = VBase3D.VBase3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point3D__overloaded___add___ptrConstLPoint3d_ptrConstLVector3d(self, other):
        returnValue = libpanda._inPUZN37tq7(self.this, other.this)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def cross(self, other):
        returnValue = libpanda._inPUZN33vhl(self.this, other.this)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3rZwG(self.this, scalar)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN39cym(self.this, scalar)
        returnObject = Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def origin(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return Point3D._Point3D__overloaded_origin()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return Point3D._Point3D__overloaded_origin___enum__CoordinateSystem(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    origin = staticmethod(origin)
    
    def rfu(*_args):
        numArgs = len(_args)
        if numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return Point3D._Point3D__overloaded_rfu_double_double_double(_args[0], _args[1], _args[2])
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
                            return Point3D._Point3D__overloaded_rfu_double_double_double___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
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
            return self._Point3D__overloaded_constructor()
        elif numArgs == 1:
            import VBase3D
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Point3D__overloaded_constructor_double(_args[0])
            elif isinstance(_args[0], VBase3D.VBase3D):
                return self._Point3D__overloaded_constructor_ptrConstLVecBase3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._Point3D__overloaded_constructor_double_double_double(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Point3D__overloaded___sub___ptrConstLPoint3d()
        elif numArgs == 1:
            import VBase3D
            import Vec3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return self._Point3D__overloaded___sub___ptrConstLPoint3d_ptrConstLVecBase3d(_args[0])
            elif isinstance(_args[0], Vec3D.Vec3D):
                return self._Point3D__overloaded___sub___ptrConstLPoint3d_ptrConstLVector3d(_args[0])
            elif isinstance(_args[0], Point3D):
                return self._Point3D__overloaded___sub___ptrConstLPoint3d_ptrConstLPoint3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <Vec3D.Vec3D> <Point3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3D
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Point3D__overloaded_assign_ptrLPoint3d_double(_args[0])
            elif isinstance(_args[0], VBase3D.VBase3D):
                return self._Point3D__overloaded_assign_ptrLPoint3d_ptrConstLVecBase3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3D.VBase3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3D
            import Vec3D
            if isinstance(_args[0], VBase3D.VBase3D):
                return self._Point3D__overloaded___add___ptrConstLPoint3d_ptrConstLVecBase3d(_args[0])
            elif isinstance(_args[0], Vec3D.Vec3D):
                return self._Point3D__overloaded___add___ptrConstLPoint3d_ptrConstLVector3d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <Vec3D.Vec3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


