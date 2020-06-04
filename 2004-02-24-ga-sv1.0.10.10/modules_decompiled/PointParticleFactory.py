# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticleFactory

class PointParticleFactory(BaseParticleFactory.BaseParticleFactory, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _PointParticleFactory__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAzdmT()
        self.userManagesMemory = 1

    
    def _PointParticleFactory__overloaded_constructor_ptrConstPointParticleFactory(self, copy):
        self.this = libpandaphysics._inPKBUA2QLp(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUATTlV:
            libpandaphysics._inPKBUATTlV(self.this)
        

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PointParticleFactory__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], PointParticleFactory):
                return self._PointParticleFactory__overloaded_constructor_ptrConstPointParticleFactory(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PointParticleFactory> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


