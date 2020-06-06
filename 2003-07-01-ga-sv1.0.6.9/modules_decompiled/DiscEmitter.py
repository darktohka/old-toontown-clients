# File: D (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticleEmitter

class DiscEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DiscEmitter__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAMaqQ()
        self.userManagesMemory = 1

    
    def _DiscEmitter__overloaded_constructor_ptrConstDiscEmitter(self, copy):
        self.this = libpandaphysics._inPKBUAZaXE(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAg60H:
            libpandaphysics._inPKBUAg60H(self.this)
        

    
    def setRadius(self, r):
        returnValue = libpandaphysics._inPKBUA8VPM(self.this, r)
        return returnValue

    
    def setOuterAngle(self, oAngle):
        returnValue = libpandaphysics._inPKBUAzAyy(self.this, oAngle)
        return returnValue

    
    def setInnerAngle(self, iAngle):
        returnValue = libpandaphysics._inPKBUA0naY(self.this, iAngle)
        return returnValue

    
    def setOuterMagnitude(self, oMag):
        returnValue = libpandaphysics._inPKBUAS8hk(self.this, oMag)
        return returnValue

    
    def setInnerMagnitude(self, iMag):
        returnValue = libpandaphysics._inPKBUAx2JK(self.this, iMag)
        return returnValue

    
    def setCubicLerping(self, clerp):
        returnValue = libpandaphysics._inPKBUAD6_D(self.this, clerp)
        return returnValue

    
    def getRadius(self):
        returnValue = libpandaphysics._inPKBUAwO_c(self.this)
        return returnValue

    
    def getOuterAngle(self):
        returnValue = libpandaphysics._inPKBUAQHU_(self.this)
        return returnValue

    
    def getInnerAngle(self):
        returnValue = libpandaphysics._inPKBUAUl9j(self.this)
        return returnValue

    
    def getOuterMagnitude(self):
        returnValue = libpandaphysics._inPKBUAS43h(self.this)
        return returnValue

    
    def getInnerMagnitude(self):
        returnValue = libpandaphysics._inPKBUArrfH(self.this)
        return returnValue

    
    def getCubicLerping(self):
        returnValue = libpandaphysics._inPKBUAW_1y(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DiscEmitter__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], DiscEmitter):
                return self._DiscEmitter__overloaded_constructor_ptrConstDiscEmitter(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <DiscEmitter> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


