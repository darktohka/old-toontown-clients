# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4

class Point4(VBase4.VBase4, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Point4__overloaded_constructor(self):
        self.this = libpanda._inPUZN30UXk()
        self.userManagesMemory = 1

    
    def _Point4__overloaded_constructor_ptrConstLVecBase4f(self, copy):
        self.this = libpanda._inPUZN3RD57(copy.this)
        self.userManagesMemory = 1

    
    def _Point4__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPUZN3Cj8c(fillValue)
        self.userManagesMemory = 1

    
    def _Point4__overloaded_constructor_float_float_float_float(self, x, y, z, w):
        self.this = libpanda._inPUZN3zr8M(x, y, z, w)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3R5Hh:
            libpanda._inPUZN3R5Hh(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN3l1J6()
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3C0yG()
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3aH8G()
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPUZN3SWGH()
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def unitW():
        returnValue = libpanda._inPUZN3KloG()
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitW = staticmethod(unitW)
    
    def getClassType():
        returnValue = libpanda._inPUZN3nbpV()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Point4__overloaded_assign_ptrLPoint4f_ptrConstLVecBase4f(self, copy):
        returnValue = libpanda._inPUZN3bZBR(self.this, copy.this)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point4__overloaded_assign_ptrLPoint4f_float(self, fillValue):
        returnValue = libpanda._inPUZN3qdAN(self.this, fillValue)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point4__overloaded___sub___ptrConstLPoint4f(self):
        returnValue = libpanda._inPUZN30LJX(self.this)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLPoint4f(self, other):
        returnValue = libpanda._inPUZN3MM2G(self.this, other.this)
        import Vec4
        returnObject = Vec4.Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPUZN3Supy(self.this, other.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLVector4f(self, other):
        returnValue = libpanda._inPUZN3WbFn(self.this, other.this)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4__overloaded___add___ptrConstLPoint4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPUZN3Jcoy(self.this, other.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4__overloaded___add___ptrConstLPoint4f_ptrConstLVector4f(self, other):
        returnValue = libpanda._inPUZN3ppEn(self.this, other.this)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3Vdt9(self.this, scalar)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3rXwd(self.this, scalar)
        returnObject = Point4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Point4__overloaded_constructor()
        elif numArgs == 1:
            import VBase4
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Point4__overloaded_constructor_float(_args[0])
            elif isinstance(_args[0], VBase4.VBase4):
                return self._Point4__overloaded_constructor_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._Point4__overloaded_constructor_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 4 '

    
    def __sub__(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Point4__overloaded___sub___ptrConstLPoint4f()
        elif numArgs == 1:
            import VBase4
            import Vec4
            if isinstance(_args[0], VBase4.VBase4):
                return self._Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLVecBase4f(_args[0])
            elif isinstance(_args[0], Vec4.Vec4):
                return self._Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLVector4f(_args[0])
            elif isinstance(_args[0], Point4):
                return self._Point4__overloaded___sub___ptrConstLPoint4f_ptrConstLPoint4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> <Vec4.Vec4> <Point4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Point4__overloaded_assign_ptrLPoint4f_float(_args[0])
            elif isinstance(_args[0], VBase4.VBase4):
                return self._Point4__overloaded_assign_ptrLPoint4f_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4.VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            import Vec4
            if isinstance(_args[0], VBase4.VBase4):
                return self._Point4__overloaded___add___ptrConstLPoint4f_ptrConstLVecBase4f(_args[0])
            elif isinstance(_args[0], Vec4.Vec4):
                return self._Point4__overloaded___add___ptrConstLPoint4f_ptrConstLVector4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> <Vec4.Vec4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


