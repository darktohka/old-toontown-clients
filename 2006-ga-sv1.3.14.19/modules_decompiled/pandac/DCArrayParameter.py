# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject
import DCParameter

class DCArrayParameter(DCParameter.DCParameter, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
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
        if libdirect and libdirect._inP5HfQSs2p:
            libdirect._inP5HfQSs2p(self.this)
        

    
    def getElementType(self):
        returnValue = libdirect._inP5HfQAc1p(self.this)
        import DCParameter
        returnObject = DCParameter.DCParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getArraySize(self):
        returnValue = libdirect._inP5HfQPdJT(self.this)
        return returnValue


