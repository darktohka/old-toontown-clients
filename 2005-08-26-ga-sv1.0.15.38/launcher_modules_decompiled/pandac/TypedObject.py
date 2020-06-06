# File: T (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class TypedObject(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
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
        if libpandaexpress and libpandaexpress._inPKoxtDv_2:
            libpandaexpress._inPKoxtDv_2(self.this)
        

    
    def getClassType():
        returnValue = libpandaexpress._inPKoxtEGqZ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getType(self):
        returnValue = libpandaexpress._inPKoxt1uxI(self.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        returnValue = libpandaexpress._inPKoxtm7AU(self.this)
        return returnValue

    
    def isOfType(self, handle):
        returnValue = libpandaexpress._inPKoxtnFKt(self.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        returnValue = libpandaexpress._inPKoxt7Xzz(self.this, handle.this)
        return returnValue


