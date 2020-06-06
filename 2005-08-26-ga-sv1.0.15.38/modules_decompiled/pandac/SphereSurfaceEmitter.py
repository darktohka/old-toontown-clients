# File: S (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import BaseParticleEmitter

class SphereSurfaceEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _SphereSurfaceEmitter__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAZ_XN()
        self.userManagesMemory = 1

    
    def _SphereSurfaceEmitter__overloaded_constructor_ptrConstSphereSurfaceEmitter(self, copy):
        self.this = libpandaphysics._inPKBUAa66a(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAg60H:
            libpandaphysics._inPKBUAg60H(self.this)
        

    
    def setRadius(self, r):
        returnValue = libpandaphysics._inPKBUAD2aF(self.this, r)
        return returnValue

    
    def getRadius(self):
        returnValue = libpandaphysics._inPKBUAjRgH(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._SphereSurfaceEmitter__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._SphereSurfaceEmitter__overloaded_constructor_ptrConstSphereSurfaceEmitter(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


