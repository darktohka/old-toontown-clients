# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import AnimGroup

class AnimBundle(AnimGroup.AnimGroup, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name, fps, numFrames):
        self.this = libpanda._inPn9gM3LBr(name, fps, numFrames)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPn9gMNcAI:
            libpanda._inPn9gMNcAI(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPn9gMzlnG()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getBaseFrameRate(self):
        returnValue = libpanda._inPn9gM6Ty_(self.this)
        return returnValue

    
    def getNumFrames(self):
        returnValue = libpanda._inPn9gMRxeQ(self.this)
        return returnValue


