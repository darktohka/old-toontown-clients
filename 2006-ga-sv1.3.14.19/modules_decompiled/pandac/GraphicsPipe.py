# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class GraphicsPipe(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    OTFullscreenWindow = 2
    OTWindow = 1
    OTTextureBuffer = 8
    OTBuffer = 4
    
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
        

    
    def getClassType():
        returnValue = libpanda._inPO9cYkM1K()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isValid(self):
        returnValue = libpanda._inPO9cYnM8A(self.this)
        return returnValue

    
    def getSupportedTypes(self):
        returnValue = libpanda._inPO9cYpKTv(self.this)
        return returnValue

    
    def supportsType(self, flags):
        returnValue = libpanda._inPO9cYcDZ_(self.this, flags)
        return returnValue

    
    def getDisplayWidth(self):
        returnValue = libpanda._inPO9cYYv10(self.this)
        return returnValue

    
    def getDisplayHeight(self):
        returnValue = libpanda._inPO9cYrAPC(self.this)
        return returnValue

    
    def getInterfaceName(self):
        returnValue = libpanda._inPO9cYheCd(self.this)
        return returnValue


