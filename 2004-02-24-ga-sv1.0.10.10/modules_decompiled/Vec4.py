# File: V (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4

class Vec4(VBase4.VBase4, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Vec4__overloaded_constructor(self):
        self.this = libpanda._inPUZN32hGZ()
        self.userManagesMemory = 1

    
    def _Vec4__overloaded_constructor_ptrConstLVecBase4f(self, copy):
        self.this = libpanda._inPUZN345R7(copy.this)
        self.userManagesMemory = 1

    
    def _Vec4__overloaded_constructor_float(self, fillValue):
        self.this = libpanda._inPUZN3LgP3(fillValue)
        self.userManagesMemory = 1

    
    def _Vec4__overloaded_constructor_float_float_float_float(self, x, y, z, w):
        self.this = libpanda._inPUZN3HLX9(x, y, z, w)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3EJW3:
            libpanda._inPUZN3EJW3(self.this)
        

    
    def zero():
        returnValue = libpanda._inPUZN3PC0O()
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    zero = staticmethod(zero)
    
    def unitX():
        returnValue = libpanda._inPUZN3wI8j()
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitX = staticmethod(unitX)
    
    def unitY():
        returnValue = libpanda._inPUZN3wk1o()
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitY = staticmethod(unitY)
    
    def unitZ():
        returnValue = libpanda._inPUZN3wAtt()
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitZ = staticmethod(unitZ)
    
    def unitW():
        returnValue = libpanda._inPUZN3xsEf()
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    unitW = staticmethod(unitW)
    
    def getClassType():
        returnValue = libpanda._inPUZN3vYTA()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _Vec4__overloaded_assign_ptrLVector4f_ptrConstLVecBase4f(self, copy):
        returnValue = libpanda._inPUZN3p2Ys(self.this, copy.this)
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec4__overloaded_assign_ptrLVector4f_float(self, fillValue):
        returnValue = libpanda._inPUZN3QfUr(self.this, fillValue)
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Vec4__overloaded___sub___ptrConstLVector4f(self):
        returnValue = libpanda._inPUZN3XMwv(self.this)
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec4__overloaded___sub___ptrConstLVector4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPUZN33RJh(self.this, other.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec4__overloaded___sub___ptrConstLVector4f_ptrConstLVector4f(self, other):
        returnValue = libpanda._inPUZN3pj9u(self.this, other.this)
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec4__overloaded___add___ptrConstLVector4f_ptrConstLVecBase4f(self, other):
        returnValue = libpanda._inPUZN3XUig(self.this, other.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Vec4__overloaded___add___ptrConstLVector4f_ptrConstLVector4f(self, other):
        returnValue = libpanda._inPUZN3JmWu(self.this, other.this)
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def length(self):
        returnValue = libpanda._inPUZN3jCMM(self.this)
        return returnValue

    
    def lengthSquared(self):
        returnValue = libpanda._inPUZN3BsKn(self.this)
        return returnValue

    
    def normalize(self):
        returnValue = libpanda._inPUZN3vg3U(self.this)
        return returnValue

    
    def __mul__(self, scalar):
        returnValue = libpanda._inPUZN3TPWC(self.this, scalar)
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __div__(self, scalar):
        returnValue = libpanda._inPUZN3jn4D(self.this, scalar)
        returnObject = Vec4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Vec4__overloaded_constructor()
        elif numArgs == 1:
            import VBase4
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Vec4__overloaded_constructor_float(_args[0])
            elif isinstance(_args[0], VBase4.VBase4):
                return self._Vec4__overloaded_constructor_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4.VBase4> '
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._Vec4__overloaded_constructor_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
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
            return self._Vec4__overloaded___sub___ptrConstLVector4f()
        elif numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._Vec4__overloaded___sub___ptrConstLVector4f_ptrConstLVecBase4f(_args[0])
            elif isinstance(_args[0], Vec4):
                return self._Vec4__overloaded___sub___ptrConstLVector4f_ptrConstLVector4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> <Vec4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def assign(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Vec4__overloaded_assign_ptrLVector4f_float(_args[0])
            elif isinstance(_args[0], VBase4.VBase4):
                return self._Vec4__overloaded_assign_ptrLVector4f_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase4.VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def __add__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._Vec4__overloaded___add___ptrConstLVector4f_ptrConstLVecBase4f(_args[0])
            elif isinstance(_args[0], Vec4):
                return self._Vec4__overloaded___add___ptrConstLVector4f_ptrConstLVector4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> <Vec4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


