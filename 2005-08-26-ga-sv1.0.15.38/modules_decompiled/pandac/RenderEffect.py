# File: R (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount

class RenderEffect(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
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
        

    
    def getNumEffects():
        returnValue = libpanda._inPnJyovz2e()
        return returnValue

    getNumEffects = staticmethod(getNumEffects)
    
    def listEffects(out):
        returnValue = libpanda._inPnJyorBxm(out.this)
        return returnValue

    listEffects = staticmethod(listEffects)
    
    def validateEffects():
        returnValue = libpanda._inPnJyoLUB_()
        return returnValue

    validateEffects = staticmethod(validateEffects)
    
    def getClassType():
        returnValue = libpanda._inPnJyo3Lms()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def compareTo(self, other):
        returnValue = libpanda._inPnJyoZvzD(self.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPnJyoLgOf(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPnJyoeXUv(self.this, out.this, indentLevel)
        return returnValue


