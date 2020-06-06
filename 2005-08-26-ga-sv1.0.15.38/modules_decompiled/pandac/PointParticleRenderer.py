# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import BaseParticleRenderer

class PointParticleRenderer(BaseParticleRenderer.BaseParticleRenderer, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    PPBLENDLIFE = 1
    PPBLENDVEL = 2
    PPONECOLOR = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod_ptrConstLVecBase4f_ptrConstLVecBase4f(self, ad, pointSize, bt, bm, sc, ec):
        self.this = libpandaphysics._inPKBUAJ8x3(ad, pointSize, bt, bm, sc.this, ec.this)
        self.userManagesMemory = 1

    
    def _PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod_ptrConstLVecBase4f(self, ad, pointSize, bt, bm, sc):
        self.this = libpandaphysics._inPKBUAOmML(ad, pointSize, bt, bm, sc.this)
        self.userManagesMemory = 1

    
    def _PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod(self, ad, pointSize, bt, bm):
        self.this = libpandaphysics._inPKBUA0kEa(ad, pointSize, bt, bm)
        self.userManagesMemory = 1

    
    def _PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType(self, ad, pointSize, bt):
        self.this = libpandaphysics._inPKBUAW_vy(ad, pointSize, bt)
        self.userManagesMemory = 1

    
    def _PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_float(self, ad, pointSize):
        self.this = libpandaphysics._inPKBUALWut(ad, pointSize)
        self.userManagesMemory = 1

    
    def _PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode(self, ad):
        self.this = libpandaphysics._inPKBUAg3Ul(ad)
        self.userManagesMemory = 1

    
    def _PointParticleRenderer__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAIwvl()
        self.userManagesMemory = 1

    
    def _PointParticleRenderer__overloaded_constructor_ptrConstPointParticleRenderer(self, copy):
        self.this = libpandaphysics._inPKBUAC0H3(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAcZ5b:
            libpandaphysics._inPKBUAcZ5b(self.this)
        

    
    def setPointSize(self, pointSize):
        returnValue = libpandaphysics._inPKBUAn3gj(self.this, pointSize)
        return returnValue

    
    def setStartColor(self, sc):
        returnValue = libpandaphysics._inPKBUAdFkn(self.this, sc.this)
        return returnValue

    
    def setEndColor(self, ec):
        returnValue = libpandaphysics._inPKBUAEzEQ(self.this, ec.this)
        return returnValue

    
    def setBlendType(self, bt):
        returnValue = libpandaphysics._inPKBUAsUyU(self.this, bt)
        return returnValue

    
    def setBlendMethod(self, bm):
        returnValue = libpandaphysics._inPKBUAHTEJ(self.this, bm)
        return returnValue

    
    def getPointSize(self):
        returnValue = libpandaphysics._inPKBUAd9NK(self.this)
        return returnValue

    
    def getStartColor(self):
        returnValue = libpandaphysics._inPKBUABJrm(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getEndColor(self):
        returnValue = libpandaphysics._inPKBUAaeEq(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getBlendType(self):
        returnValue = libpandaphysics._inPKBUAR8v5(self.this)
        return returnValue

    
    def getBlendMethod(self):
        returnValue = libpandaphysics._inPKBUANfkE(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PointParticleRenderer__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode(*_args)
            
            if isinstance(_args[0], PointParticleRenderer):
                return self._PointParticleRenderer__overloaded_constructor_ptrConstPointParticleRenderer(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PointParticleRenderer> '
        elif numArgs == 2:
            return self._PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_float(*_args)
        elif numArgs == 3:
            return self._PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType(*_args)
        elif numArgs == 4:
            return self._PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod(*_args)
        elif numArgs == 5:
            return self._PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod_ptrConstLVecBase4f(*_args)
        elif numArgs == 6:
            return self._PointParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_float___enum__PointParticleBlendType___enum__ParticleRendererBlendMethod_ptrConstLVecBase4f_ptrConstLVecBase4f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 5 6 '


