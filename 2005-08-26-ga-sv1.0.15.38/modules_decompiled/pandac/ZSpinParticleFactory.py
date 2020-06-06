# File: Z (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import BaseParticleFactory

class ZSpinParticleFactory(BaseParticleFactory.BaseParticleFactory, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ZSpinParticleFactory__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUACYSj()
        self.userManagesMemory = 1

    
    def _ZSpinParticleFactory__overloaded_constructor_ptrConstZSpinParticleFactory(self, copy):
        self.this = libpandaphysics._inPKBUA_nkG(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUATTlV:
            libpandaphysics._inPKBUATTlV(self.this)
        

    
    def setInitialAngle(self, angle):
        returnValue = libpandaphysics._inPKBUAJQKd(self.this, angle)
        return returnValue

    
    def setFinalAngle(self, angle):
        returnValue = libpandaphysics._inPKBUA_A2T(self.this, angle)
        return returnValue

    
    def setInitialAngleSpread(self, spread):
        returnValue = libpandaphysics._inPKBUAZoPY(self.this, spread)
        return returnValue

    
    def setFinalAngleSpread(self, spread):
        returnValue = libpandaphysics._inPKBUAAxxa(self.this, spread)
        return returnValue

    
    def getInitialAngle(self):
        returnValue = libpandaphysics._inPKBUAZ6E9(self.this)
        return returnValue

    
    def getFinalAngle(self):
        returnValue = libpandaphysics._inPKBUAUZT9(self.this)
        return returnValue

    
    def getInitialAngleSpread(self):
        returnValue = libpandaphysics._inPKBUAjK1c(self.this)
        return returnValue

    
    def getFinalAngleSpread(self):
        returnValue = libpandaphysics._inPKBUAuV0_(self.this)
        return returnValue

    
    def setAngularVelocity(self, v):
        returnValue = libpandaphysics._inPKBUALOQE(self.this, v)
        return returnValue

    
    def getAngularVelocity(self):
        returnValue = libpandaphysics._inPKBUAS1Y8(self.this)
        return returnValue

    
    def setAngularVelocitySpread(self, spread):
        returnValue = libpandaphysics._inPKBUAsUGS(self.this, spread)
        return returnValue

    
    def getAngularVelocitySpread(self):
        returnValue = libpandaphysics._inPKBUALycB(self.this)
        return returnValue

    
    def enableAngularVelocity(self, bEnabled):
        returnValue = libpandaphysics._inPKBUAmOcc(self.this, bEnabled)
        return returnValue

    
    def getAngularVelocityEnabled(self):
        returnValue = libpandaphysics._inPKBUA2hT8(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ZSpinParticleFactory__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._ZSpinParticleFactory__overloaded_constructor_ptrConstZSpinParticleFactory(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


