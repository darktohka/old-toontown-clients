# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import LinearRandomForce

class LinearNoiseForce(LinearRandomForce.LinearRandomForce, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _LinearNoiseForce__overloaded_constructor_ptrConstLinearNoiseForce(self, copy):
        self.this = libpandaphysics._inP9fJJif_B(copy.this)
        self.userManagesMemory = 1

    
    def _LinearNoiseForce__overloaded_constructor_float_bool(self, a, m):
        self.this = libpandaphysics._inP9fJJhrE1(a, m)
        self.userManagesMemory = 1

    
    def _LinearNoiseForce__overloaded_constructor_float(self, a):
        self.this = libpandaphysics._inP9fJJN_EG(a)
        self.userManagesMemory = 1

    
    def _LinearNoiseForce__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJqAku()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJepMh()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LinearNoiseForce__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._LinearNoiseForce__overloaded_constructor_float(_args[0])
            elif isinstance(_args[0], LinearNoiseForce):
                return self._LinearNoiseForce__overloaded_constructor_ptrConstLinearNoiseForce(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <LinearNoiseForce> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._LinearNoiseForce__overloaded_constructor_float_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


