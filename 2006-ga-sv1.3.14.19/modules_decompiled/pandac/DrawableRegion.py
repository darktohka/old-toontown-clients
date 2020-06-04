# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class DrawableRegion(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
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
        if libpanda and libpanda._inPO9cYD3lD:
            libpanda._inPO9cYD3lD(self.this)
        

    
    def setClearColorActive(self, clearColorActive):
        returnValue = libpanda._inPO9cY5_NM(self.this, clearColorActive)
        return returnValue

    
    def getClearColorActive(self):
        returnValue = libpanda._inPO9cYQ__5(self.this)
        return returnValue

    
    def setClearDepthActive(self, clearDepthActive):
        returnValue = libpanda._inPO9cY_x_a(self.this, clearDepthActive)
        return returnValue

    
    def getClearDepthActive(self):
        returnValue = libpanda._inPO9cYklwI(self.this)
        return returnValue

    
    def setClearColor(self, color):
        returnValue = libpanda._inPO9cYrSVN(self.this, color.this)
        return returnValue

    
    def getClearColor(self):
        returnValue = libpanda._inPO9cY4kxz(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setClearDepth(self, depth):
        returnValue = libpanda._inPO9cYw_6X(self.this, depth)
        return returnValue

    
    def getClearDepth(self):
        returnValue = libpanda._inPO9cYMYjC(self.this)
        return returnValue

    
    def isAnyClearActive(self):
        returnValue = libpanda._inPO9cY0Gt_(self.this)
        return returnValue


