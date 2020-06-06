# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RenderAttrib

class DepthOffsetAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
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
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoW3rf:
            libpanda._inPnJyoW3rf(self.this)
        

    
    def _DepthOffsetAttrib__overloaded_make_int(offset):
        returnValue = libpanda._inPnJyoYYvF(offset)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _DepthOffsetAttrib__overloaded_make_int = staticmethod(_DepthOffsetAttrib__overloaded_make_int)
    
    def _DepthOffsetAttrib__overloaded_make():
        returnValue = libpanda._inPnJyoTJWU()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _DepthOffsetAttrib__overloaded_make = staticmethod(_DepthOffsetAttrib__overloaded_make)
    
    def getClassType():
        returnValue = libpanda._inPnJyorc0x()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getOffset(self):
        returnValue = libpanda._inPnJyoQ48q(self.this)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return DepthOffsetAttrib._DepthOffsetAttrib__overloaded_make(*_args)
        elif numArgs == 1:
            return DepthOffsetAttrib._DepthOffsetAttrib__overloaded_make_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    make = staticmethod(make)

