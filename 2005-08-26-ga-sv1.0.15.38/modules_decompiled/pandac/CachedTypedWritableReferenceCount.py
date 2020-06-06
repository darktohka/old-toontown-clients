# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount

class CachedTypedWritableReferenceCount(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
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
        

    
    def getClassType():
        returnValue = libpanda._inPflboXAeA()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getCacheRefCount(self):
        returnValue = libpanda._inPflbo3cWf(self.this)
        return returnValue

    
    def cacheRef(self):
        returnValue = libpanda._inPflboEGtE(self.this)
        return returnValue

    
    def cacheUnref(self):
        returnValue = libpanda._inPflboC2Hz(self.this)
        return returnValue

    
    def testCacheRefCountIntegrity(self):
        returnValue = libpanda._inPflboKHQe(self.this)
        return returnValue


