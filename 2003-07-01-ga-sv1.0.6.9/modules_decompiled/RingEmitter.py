# File: R (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticleEmitter

class RingEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _RingEmitter__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUA__j2()
        self.userManagesMemory = 1

    
    def _RingEmitter__overloaded_constructor_ptrConstRingEmitter(self, copy):
        self.this = libpandaphysics._inPKBUAirbu(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAg60H:
            libpandaphysics._inPKBUAg60H(self.this)
        

    
    def setRadius(self, r):
        returnValue = libpandaphysics._inPKBUAIjXu(self.this, r)
        return returnValue

    
    def setAngle(self, angle):
        returnValue = libpandaphysics._inPKBUA33Hl(self.this, angle)
        return returnValue

    
    def getRadius(self):
        returnValue = libpandaphysics._inPKBUA02I_(self.this)
        return returnValue

    
    def getAngle(self):
        returnValue = libpandaphysics._inPKBUAQZ9k(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._RingEmitter__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], RingEmitter):
                return self._RingEmitter__overloaded_constructor_ptrConstRingEmitter(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RingEmitter> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


