# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class DataGraphTraverser(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPSLSe6KPF()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPSLSekC6u:
            libpanda._inPSLSekC6u(self.this)
        

    
    def traverse(self, node):
        returnValue = libpanda._inPSLSePaYd(self.this, node.this)
        return returnValue

    
    def traverseBelow(self, node, output):
        returnValue = libpanda._inPSLSelThv(self.this, node.this, output.this)
        return returnValue

    
    def collectLeftovers(self):
        returnValue = libpanda._inPSLSe8nIW(self.this)
        return returnValue


