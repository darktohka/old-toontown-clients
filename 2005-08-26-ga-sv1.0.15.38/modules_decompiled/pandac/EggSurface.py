# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggPrimitive

class EggSurface(EggPrimitive.EggPrimitive, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMGAT7:
            libpandaegg._inPkAOMGAT7(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMjy4J()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOM6fZQ(self.this, copy.this)
        returnObject = EggSurface(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setUSubdiv(self, subdiv):
        returnValue = libpandaegg._inPkAOMD1tU(self.this, subdiv)
        return returnValue

    
    def getUSubdiv(self):
        returnValue = libpandaegg._inPkAOM1xT9(self.this)
        return returnValue

    
    def setVSubdiv(self, subdiv):
        returnValue = libpandaegg._inPkAOMDplZ(self.this, subdiv)
        return returnValue

    
    def getVSubdiv(self):
        returnValue = libpandaegg._inPkAOM0VLC(self.this)
        return returnValue


