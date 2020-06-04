# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RenderAttrib

class CullFaceAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    MCullCounterClockwise = 2
    MCullClockwise = 1
    MCullUnchanged = 3
    MCullNone = 0
    
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
        if libpanda and libpanda._inPnJyoREpA:
            libpanda._inPnJyoREpA(self.this)
        

    
    def _CullFaceAttrib__overloaded_make___enum__Mode(mode):
        returnValue = libpanda._inPnJyoIubb(mode)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _CullFaceAttrib__overloaded_make___enum__Mode = staticmethod(_CullFaceAttrib__overloaded_make___enum__Mode)
    
    def _CullFaceAttrib__overloaded_make():
        returnValue = libpanda._inPnJyonry7()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _CullFaceAttrib__overloaded_make = staticmethod(_CullFaceAttrib__overloaded_make)
    
    def makeReverse():
        returnValue = libpanda._inPnJyo1_sE()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeReverse = staticmethod(makeReverse)
    
    def getClassType():
        returnValue = libpanda._inPnJyodcRA()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getActualMode(self):
        returnValue = libpanda._inPnJyotw1_(self.this)
        return returnValue

    
    def getReverse(self):
        returnValue = libpanda._inPnJyoZ_zu(self.this)
        return returnValue

    
    def getEffectiveMode(self):
        returnValue = libpanda._inPnJyoN1y1(self.this)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return CullFaceAttrib._CullFaceAttrib__overloaded_make(*_args)
        elif numArgs == 1:
            return CullFaceAttrib._CullFaceAttrib__overloaded_make___enum__Mode(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    make = staticmethod(make)

