# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class ClearableRegion(FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPO9cYMobe:
            libpanda._inPO9cYMobe(self.this)
        

    
    def setClearColorActive(self, clearColorActive):
        returnValue = libpanda._inPO9cYrI_a(self.this, clearColorActive)
        return returnValue

    
    def getClearColorActive(self):
        returnValue = libpanda._inPO9cY73cT(self.this)
        return returnValue

    
    def setClearDepthActive(self, clearDepthActive):
        returnValue = libpanda._inPO9cYD0jz(self.this, clearDepthActive)
        return returnValue

    
    def getClearDepthActive(self):
        returnValue = libpanda._inPO9cYIBBs(self.this)
        return returnValue

    
    def setClearColor(self, color):
        returnValue = libpanda._inPO9cYEJb_(self.this, color.this)
        return returnValue

    
    def getClearColor(self):
        returnValue = libpanda._inPO9cYHnZM(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setClearDepth(self, depth):
        returnValue = libpanda._inPO9cYg8RQ(self.this, depth)
        return returnValue

    
    def getClearDepth(self):
        returnValue = libpanda._inPO9cYkm_k(self.this)
        return returnValue

    
    def isAnyClearActive(self):
        returnValue = libpanda._inPO9cYNXIL(self.this)
        return returnValue


