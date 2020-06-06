# File: R (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import BaseParticleEmitter

class RingEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _RingEmitter__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUA__j2()
        self.userManagesMemory = 1

    
    def _RingEmitter__overloaded_constructor_ptrConstRingEmitter(self, copy):
        self.this = libpandaphysics._inPKBUAhrbu(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAg60H:
            libpandaphysics._inPKBUAg60H(self.this)
        

    
    def setRadius(self, r):
        returnValue = libpandaphysics._inPKBUAHjXu(self.this, r)
        return returnValue

    
    def setAngle(self, angle):
        returnValue = libpandaphysics._inPKBUA23Hl(self.this, angle)
        return returnValue

    
    def getRadius(self):
        returnValue = libpandaphysics._inPKBUA32I_(self.this)
        return returnValue

    
    def getAngle(self):
        returnValue = libpandaphysics._inPKBUARZ9k(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._RingEmitter__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._RingEmitter__overloaded_constructor_ptrConstRingEmitter(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


