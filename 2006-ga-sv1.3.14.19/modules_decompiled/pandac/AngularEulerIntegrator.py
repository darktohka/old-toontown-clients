# File: A (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
from direct.ffi import FFIExternalObject
import AngularIntegrator

class AngularEulerIntegrator(AngularIntegrator.AngularIntegrator, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaphysics._inP9fJJ4P7V()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        


