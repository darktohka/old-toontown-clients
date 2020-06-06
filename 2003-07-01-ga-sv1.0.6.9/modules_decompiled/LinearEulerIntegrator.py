# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import FFIExternalObject
import LinearIntegrator

class LinearEulerIntegrator(LinearIntegrator.LinearIntegrator, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpandaphysics._inP9fJJUpBu()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        


