# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggPrimitive

class EggCurve(EggPrimitive.EggPrimitive, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    CTHpr = 2
    CTT = 3
    CTXyz = 1
    CTNone = 0
    
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
        if libpandaegg and libpandaegg._inPkAOMlP_s:
            libpandaegg._inPkAOMlP_s(self.this)
        

    
    def stringCurveType(cString):
        returnValue = libpandaegg._inPkAOM5L8d(cString)
        return returnValue

    stringCurveType = staticmethod(stringCurveType)
    
    def getClassType():
        returnValue = libpandaegg._inPkAOMsThz()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOM9d8E(self.this, copy.this)
        returnObject = EggCurve(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setSubdiv(self, subdiv):
        returnValue = libpandaegg._inPkAOM6saC(self.this, subdiv)
        return returnValue

    
    def getSubdiv(self):
        returnValue = libpandaegg._inPkAOM_WHg(self.this)
        return returnValue

    
    def setCurveType(self, type):
        returnValue = libpandaegg._inPkAOMupv_(self.this, type)
        return returnValue

    
    def getCurveType(self):
        returnValue = libpandaegg._inPkAOM6DD5(self.this)
        return returnValue


