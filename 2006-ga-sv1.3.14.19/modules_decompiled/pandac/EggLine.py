# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggPrimitive

class EggLine(EggPrimitive.EggPrimitive, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggLine__overloaded_constructor_ptrConstEggLine(self, copy):
        self.this = libpandaegg._inPkAOMDrFz(copy.this)
        self.userManagesMemory = 1

    
    def _EggLine__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOMX4DQ(name)
        self.userManagesMemory = 1

    
    def _EggLine__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMJipL()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMg2jW:
            libpandaegg._inPkAOMg2jW(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMZ1pB()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMvLAZ(self.this, copy.this)
        returnObject = EggLine(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggLine__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggLine__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggLine):
                return self._EggLine__overloaded_constructor_ptrConstEggLine(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggLine> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


