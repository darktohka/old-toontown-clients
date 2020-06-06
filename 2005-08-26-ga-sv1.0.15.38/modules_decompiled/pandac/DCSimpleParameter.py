# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject
import DCParameter

class DCSimpleParameter(DCParameter.DCParameter, FFIExternalObject.FFIExternalObject):
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
        if libdirect and libdirect._inP5HfQ7dUM:
            libdirect._inP5HfQ7dUM(self.this)
        

    
    def getType(self):
        returnValue = libdirect._inP5HfQdLgm(self.this)
        return returnValue

    
    def hasModulus(self):
        returnValue = libdirect._inP5HfQL3kT(self.this)
        return returnValue

    
    def getModulus(self):
        returnValue = libdirect._inP5HfQ_9h_(self.this)
        return returnValue

    
    def getDivisor(self):
        returnValue = libdirect._inP5HfQBZIP(self.this)
        return returnValue


