# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import BaseParticleRenderer

class LineParticleRenderer(BaseParticleRenderer.BaseParticleRenderer, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LineParticleRenderer__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAEZz7()
        self.userManagesMemory = 1

    
    def _LineParticleRenderer__overloaded_constructor_ptrConstLVecBase4f_ptrConstLVecBase4f___enum__ParticleRendererAlphaMode(self, head, tail, alphaMode):
        self.this = libpandaphysics._inPKBUAsY3q(head.this, tail.this, alphaMode)
        self.userManagesMemory = 1

    
    def _LineParticleRenderer__overloaded_constructor_ptrConstLineParticleRenderer(self, copy):
        self.this = libpandaphysics._inPKBUAWkxE(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAcZ5b:
            libpandaphysics._inPKBUAcZ5b(self.this)
        

    
    def setHeadColor(self, c):
        returnValue = libpandaphysics._inPKBUA_Gxm(self.this, c.this)
        return returnValue

    
    def setTailColor(self, c):
        returnValue = libpandaphysics._inPKBUAHL4t(self.this, c.this)
        return returnValue

    
    def getHeadColor(self):
        returnValue = libpandaphysics._inPKBUAS8gD(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getTailColor(self):
        returnValue = libpandaphysics._inPKBUApyoK(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LineParticleRenderer__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._LineParticleRenderer__overloaded_constructor_ptrConstLineParticleRenderer(*_args)
        elif numArgs == 3:
            return self._LineParticleRenderer__overloaded_constructor_ptrConstLVecBase4f_ptrConstLVecBase4f___enum__ParticleRendererAlphaMode(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '


