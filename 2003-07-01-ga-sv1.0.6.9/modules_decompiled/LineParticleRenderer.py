# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticleRenderer

class LineParticleRenderer(BaseParticleRenderer.BaseParticleRenderer, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _LineParticleRenderer__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUALZz7()
        self.userManagesMemory = 1

    
    def _LineParticleRenderer__overloaded_constructor_ptrConstLVecBase4f_ptrConstLVecBase4f___enum__ParticleRendererAlphaMode(self, head, tail, alphaMode):
        self.this = libpandaphysics._inPKBUArY3q(head.this, tail.this, alphaMode)
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
        returnValue = libpandaphysics._inPKBUAEL4t(self.this, c.this)
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
            return self._LineParticleRenderer__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], LineParticleRenderer):
                return self._LineParticleRenderer__overloaded_constructor_ptrConstLineParticleRenderer(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <LineParticleRenderer> '
        elif numArgs == 3:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                import VBase4
                if isinstance(_args[1], VBase4.VBase4):
                    if isinstance(_args[2], types.IntType):
                        return self._LineParticleRenderer__overloaded_constructor_ptrConstLVecBase4f_ptrConstLVecBase4f___enum__ParticleRendererAlphaMode(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 3 '


