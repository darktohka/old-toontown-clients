# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggGroup

class EggBin(EggGroup.EggGroup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggBin__overloaded_constructor_ptrConstEggBin(self, copy):
        self.this = libpandaegg._inPkAOME04m(copy.this)
        self.userManagesMemory = 1

    
    def _EggBin__overloaded_constructor_ptrConstEggGroup(self, copy):
        self.this = libpandaegg._inPkAOM5VW_(copy.this)
        self.userManagesMemory = 1

    
    def _EggBin__overloaded_constructor_atomicstring(self, name):
        self.this = libpandaegg._inPkAOMxysi(name)
        self.userManagesMemory = 1

    
    def _EggBin__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMcVXw()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOML46O:
            libpandaegg._inPkAOML46O(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMDJum()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setBinNumber(self, binNumber):
        returnValue = libpandaegg._inPkAOM35b4(self.this, binNumber)
        return returnValue

    
    def getBinNumber(self):
        returnValue = libpandaegg._inPkAOM39QH(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggBin__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._EggBin__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], EggBin):
                return self._EggBin__overloaded_constructor_ptrConstEggBin(*_args)
            
            import EggGroup
            if isinstance(_args[0], EggGroup.EggGroup):
                return self._EggBin__overloaded_constructor_ptrConstEggGroup(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <EggBin> <EggGroup.EggGroup> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


