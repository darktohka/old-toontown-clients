# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import RenderAttrib

class AlphaTestAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyopWov:
            libpanda._inPkJyopWov(self.this)
        

    
    def make(mode, referenceAlpha):
        returnValue = libpanda._inPkJyoQcHT(mode, referenceAlpha)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    make = staticmethod(make)
    
    def getClassType():
        returnValue = libpanda._inPkJyoO7w8()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getReferenceAlpha(self):
        returnValue = libpanda._inPkJyohz_c(self.this)
        return returnValue

    
    def getMode(self):
        returnValue = libpanda._inPkJyooV_S(self.this)
        return returnValue


