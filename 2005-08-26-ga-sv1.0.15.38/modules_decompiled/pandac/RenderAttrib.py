# File: R (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount

class RenderAttrib(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    MLessEqual = 4
    MGreaterEqual = 7
    MNone = 0
    MGreater = 5
    MEqual = 3
    MLess = 2
    MNever = 1
    MNotEqual = 6
    MAlways = 8
    
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
        

    
    def getNumAttribs():
        returnValue = libpanda._inPnJyoHzox()
        return returnValue

    getNumAttribs = staticmethod(getNumAttribs)
    
    def listAttribs(out):
        returnValue = libpanda._inPnJyoHw_H(out.this)
        return returnValue

    listAttribs = staticmethod(listAttribs)
    
    def validateAttribs():
        returnValue = libpanda._inPnJyonA2d()
        return returnValue

    validateAttribs = staticmethod(validateAttribs)
    
    def getClassType():
        returnValue = libpanda._inPnJyoLWjP()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def compareTo(self, other):
        returnValue = libpanda._inPnJyovruE(self.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPnJyooTLC(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPnJyodBRS(self.this, out.this, indentLevel)
        return returnValue


