# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class HTTPEnum(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    HV09 = 0
    HV11 = 2
    HV10 = 1
    HVOther = 3
    MPut = 4
    MConnect = 7
    MPost = 3
    MOptions = 0
    MHead = 2
    MDelete = 5
    MTrace = 6
    MGet = 1
    
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
        if libpandaexpress and libpandaexpress._inP2KOdaejK:
            libpandaexpress._inP2KOdaejK(self.this)
        


