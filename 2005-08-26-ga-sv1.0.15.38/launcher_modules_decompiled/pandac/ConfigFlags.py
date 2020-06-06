# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class ConfigFlags(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    VTString = 2
    VTSearchPath = 8
    VTBool = 4
    VTUndefined = 0
    VTEnum = 7
    VTInt = 5
    VTDouble = 6
    VTList = 1
    VTFilename = 3
    FDynamic = 16384
    FOpen = 4096
    FDconfig = 32768
    FTrustLevelMask = 4095
    FClosed = 8192
    
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
        if libpandaexpress and libpandaexpress._inPKoxtt5ax:
            libpandaexpress._inPKoxtt5ax(self.this)
        


