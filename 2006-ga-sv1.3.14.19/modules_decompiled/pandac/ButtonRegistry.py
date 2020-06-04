# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class ButtonRegistry(FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPflbo3pmE:
            libpanda._inPflbo3pmE(self.this)
        

    
    def ptr():
        returnValue = libpanda._inPflbodgyc()
        returnObject = ButtonRegistry(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    ptr = staticmethod(ptr)
    
    def getButton(self, name):
        returnValue = libpanda._inPflboKZsi(self.this, name)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def findAsciiButton(self, asciiEquivalent):
        returnValue = libpanda._inPflbouc8u(self.this, asciiEquivalent)
        import ButtonHandle
        returnObject = ButtonHandle.ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject


