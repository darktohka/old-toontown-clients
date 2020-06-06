# File: M (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject

class Mersenne(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, seed):
        self.this = libdirect._inPL4GTllv3(seed)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inPL4GTA4FJ:
            libdirect._inPL4GTA4FJ(self.this)
        

    
    def getUint31(self):
        returnValue = libdirect._inPL4GTBSDv(self.this)
        return returnValue


