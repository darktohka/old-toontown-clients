# File: I (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class Istream(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxt8pc4:
            libpandaexpress._inPJoxt8pc4(self.this)
        

    
    def get(self):
        returnValue = libpandaexpress._inPJoxtnuln(self.this)
        return returnValue


