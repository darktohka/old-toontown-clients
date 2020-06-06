# File: R (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RenderAttrib

class RenderModeAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    MFilled = 0
    MWireframe = 1
    
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
        if libpanda and libpanda._inPnJyoDu_B:
            libpanda._inPnJyoDu_B(self.this)
        

    
    def _RenderModeAttrib__overloaded_make___enum__Mode_float(mode, lineWidth):
        returnValue = libpanda._inPnJyo8VB1(mode, lineWidth)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderModeAttrib__overloaded_make___enum__Mode_float = staticmethod(_RenderModeAttrib__overloaded_make___enum__Mode_float)
    
    def _RenderModeAttrib__overloaded_make___enum__Mode(mode):
        returnValue = libpanda._inPnJyo9BMo(mode)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderModeAttrib__overloaded_make___enum__Mode = staticmethod(_RenderModeAttrib__overloaded_make___enum__Mode)
    
    def getClassType():
        returnValue = libpanda._inPnJyoN0p3()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getMode(self):
        returnValue = libpanda._inPnJyoEaf_(self.this)
        return returnValue

    
    def getLineWidth(self):
        returnValue = libpanda._inPnJyoVxaK(self.this)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return RenderModeAttrib._RenderModeAttrib__overloaded_make___enum__Mode(*_args)
        elif numArgs == 2:
            return RenderModeAttrib._RenderModeAttrib__overloaded_make___enum__Mode_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    make = staticmethod(make)

