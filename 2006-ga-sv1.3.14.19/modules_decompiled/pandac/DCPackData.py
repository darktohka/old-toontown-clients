# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject

class DCPackData(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libdirect._inP5HfQb_tg()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inP5HfQKLig:
            libdirect._inP5HfQKLig(self.this)
        

    
    def clear(self):
        returnValue = libdirect._inP5HfQi4W4(self.this)
        return returnValue

    
    def getString(self):
        returnValue = libdirect._inP5HfQqSqZ(self.this)
        return returnValue

    
    def getLength(self):
        returnValue = libdirect._inP5HfQR8z_(self.this)
        return returnValue


