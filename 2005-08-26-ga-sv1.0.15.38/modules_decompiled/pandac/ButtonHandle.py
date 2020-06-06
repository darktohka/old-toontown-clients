# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class ButtonHandle(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPflbo40bO()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPflbowcFL:
            libpanda._inPflbowcFL(self.this)
        

    
    def none():
        returnValue = libpanda._inPflboXMlV()
        returnObject = ButtonHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    none = staticmethod(none)
    
    def getName(self):
        returnValue = libpanda._inPflbooq06(self.this)
        return returnValue

    
    def hasAsciiEquivalent(self):
        returnValue = libpanda._inPflbo2_MD(self.this)
        return returnValue

    
    def getAsciiEquivalent(self):
        returnValue = libpanda._inPflbovhsY(self.this)
        return returnValue

    
    def getIndex(self):
        returnValue = libpanda._inPflboiajp(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPflbo6vL2(self.this, out.this)
        return returnValue


