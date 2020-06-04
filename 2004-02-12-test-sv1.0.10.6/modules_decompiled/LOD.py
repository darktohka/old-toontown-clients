# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class LOD(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
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
        if libpanda and libpanda._inPMAKPXWb1:
            libpanda._inPMAKPXWb1(self.this)
        

    
    def setStressFactor(stressFactor):
        returnValue = libpanda._inPMAKPC1yV(stressFactor)
        return returnValue

    setStressFactor = staticmethod(setStressFactor)
    
    def getStressFactor():
        returnValue = libpanda._inPMAKPYQzx()
        return returnValue

    getStressFactor = staticmethod(getStressFactor)

