# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4D

class Point4D(VBase4D.VBase4D, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Point4D__overloaded_constructor(self):
        self.this = libpanda._inPUZN3tU0d()
        self.userManagesMemory = 1

    
    def _Point4D__overloaded_constructor_ptrConstLVecBase4d(self, copy):
        self.this = libpanda._inPUZN3IZW9(copy.this)
        self.userManagesMemory = 1

    
    def _Point4D__overloaded_constructor_double(self, fillValue):
        self.this = libpanda._inPUZN306e0(fillValue)
        self.userManagesMemory = 1

    
    def _Point4D__overloaded_constructor_double_double_double_double(self, x, y, z, w):
        self.this = libpanda._inPUZN3CpeG(x, y, z, w)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3z0AF:
            libpanda._inPUZN3z0AF(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN3q1Cs()
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3B0r4()
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3ZH14()
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPUZN3RW_4()
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def unitW():
        returnValue = libpanda._inPUZN3Jlh4()
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitW = staticmethod(unitW)
    
    def getClassType():
        returnValue = libpanda._inPUZN3mbiH()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Point4D__overloaded_assign_ptrLPoint4d_ptrConstLVecBase4d(self, copy):
        returnValue = libpanda._inPUZN3YHeA(self.this, copy.this)
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point4D__overloaded_assign_ptrLPoint4d_double(self, fillValue):
        returnValue = libpanda._inPUZN3MxVL(self.this, fillValue)
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Point4D__overloaded___sub___ptrConstLPoint4d(self):
        returnValue = libpanda._inPUZN31LCJ(self.this)
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4D__overloaded___sub___ptrConstLPoint4d_ptrConstLPoint4d(self, other):
        returnValue = libpanda._inPUZN3xIuA(self.this, other.this)
        import Vec4D
        returnObject = Vec4D.Vec4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4D__overloaded___sub___ptrConstLPoint4d_ptrConstLVecBase4d(self, other):
        returnValue = libpanda._inPUZN3TcGi(self.this, other.this)
        import VBase4D
        returnObject = VBase4D.VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4D__overloaded___sub___ptrConstLPoint4d_ptrConstLVector4d(self, other):
        returnValue = libpanda._inPUZN30T5Y(self.this, other.this)
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4D__overloaded___add___ptrConstLPoint4d_ptrConstLVecBase4d(self, other):
        returnValue = libpanda._inPUZN3ISFi(self.this, other.this)
        import VBase4D
        returnObject = VBase4D.VBase4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Point4D__overloaded___add___ptrConstLPoint4d_ptrConstLVector4d(self, other):
        returnValue = libpanda._inPUZN3zh4Y(self.this, other.this)
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3re_H(self.this, scalar)
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN39DAo(self.this, scalar)
        returnObject = Point4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Point4D__overloaded_constructor()
        elif numArgs == 1:
            import VBase4D
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Point4D__overloaded_constructor_double(_args[0])
            elif isinstance(_args[0], VBase4D.VBase4D):
                return self._Point4D__overloaded_constructor_ptrConstLVecBase4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D.VBase4D> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._Point4D__overloaded_constructor_double_double_double_double(_args[0], _args[1], _args[2], _args[3])
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
            return self._Point4D__overloaded___sub___ptrConstLPoint4d()
        elif numArgs == 1:
            import VBase4D
            import Vec4D
            if isinstance(_args[0], VBase4D.VBase4D):
                return self._Point4D__overloaded___sub___ptrConstLPoint4d_ptrConstLVecBase4d(_args[0])
            elif isinstance(_args[0], Vec4D.Vec4D):
                return self._Point4D__overloaded___sub___ptrConstLPoint4d_ptrConstLVector4d(_args[0])
            elif isinstance(_args[0], Point4D):
                return self._Point4D__overloaded___sub___ptrConstLPoint4d_ptrConstLPoint4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4D.VBase4D> <Vec4D.Vec4D> <Point4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4D
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Point4D__overloaded_assign_ptrLPoint4d_double(_args[0])
            elif isinstance(_args[0], VBase4D.VBase4D):
                return self._Point4D__overloaded_assign_ptrLPoint4d_ptrConstLVecBase4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4D.VBase4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4D
            import Vec4D
            if isinstance(_args[0], VBase4D.VBase4D):
                return self._Point4D__overloaded___add___ptrConstLPoint4d_ptrConstLVecBase4d(_args[0])
            elif isinstance(_args[0], Vec4D.Vec4D):
                return self._Point4D__overloaded___add___ptrConstLPoint4d_ptrConstLVector4d(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4D.VBase4D> <Vec4D.Vec4D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


