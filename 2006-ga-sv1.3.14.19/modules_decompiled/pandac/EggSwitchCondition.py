# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggObject

class EggSwitchCondition(EggObject.EggObject, FFIExternalObject.FFIExternalObject):
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
        if libpandaegg and libpandaegg._inPkAOMBLwZ:
            libpandaegg._inPkAOMBLwZ(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMgiFq()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def makeCopy(self):
        returnValue = libpandaegg._inPkAOMMAjk(self.this)
        returnObject = EggSwitchCondition(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def write(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMdfeb(self.this, out.this, indentLevel)
        return returnValue

    
    def transform(self, mat):
        returnValue = libpandaegg._inPkAOMXbAk(self.this, mat.this)
        return returnValue


