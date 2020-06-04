# File: P (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class PointerToBaseRefCountObjvectorunsignedchar(FFIExternalObject.FFIExternalObject):
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
        

    
    def isNull(self):
        returnValue = libpandaexpress._inPJoxtq_Ug(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpandaexpress._inPJoxtcLaW(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inPJoxtVyqz(self.this, out.this)
        return returnValue


