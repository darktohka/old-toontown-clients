# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject
import DCDeclaration

class DCTypedef(DCDeclaration.DCDeclaration, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
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
        if libdirect and libdirect._inP5HfQ9AVj:
            libdirect._inP5HfQ9AVj(self.this)
        

    
    def getNumber(self):
        returnValue = libdirect._inP5HfQ3FUN(self.this)
        return returnValue

    
    def getName(self):
        returnValue = libdirect._inP5HfQVrMq(self.this)
        return returnValue

    
    def getDescription(self):
        returnValue = libdirect._inP5HfQnZ2F(self.this)
        return returnValue

    
    def isBogusTypedef(self):
        returnValue = libdirect._inP5HfQnwBq(self.this)
        return returnValue

    
    def isImplicitTypedef(self):
        returnValue = libdirect._inP5HfQ3UT1(self.this)
        return returnValue


