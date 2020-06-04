# File: C (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CInterval

class CLerpInterval(CInterval.CInterval, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts,
        libpandaexpressDowncasts]
    BTNoBlend = 0
    BTEaseInOut = 3
    BTInvalid = 4
    BTEaseOut = 2
    BTEaseIn = 1
    
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
        if libdirect and libdirect._inPSpsCIddL:
            libdirect._inPSpsCIddL(self.this)
        

    
    def stringBlendType(blendType):
        returnValue = libdirect._inPSpsCHWfc(blendType)
        return returnValue

    stringBlendType = staticmethod(stringBlendType)
    
    def getClassType():
        returnValue = libdirect._inPSpsCFioW()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getBlendType(self):
        returnValue = libdirect._inPSpsCg1iu(self.this)
        return returnValue


