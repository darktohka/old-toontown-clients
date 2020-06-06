# File: G (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import BaseParticleRenderer

class GeomParticleRenderer(BaseParticleRenderer.BaseParticleRenderer, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _GeomParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_ptrPandaNode(self, am, geomNode):
        self.this = libpandaphysics._inPKBUAfwJz(am, geomNode.this)
        self.userManagesMemory = 1

    
    def _GeomParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode(self, am):
        self.this = libpandaphysics._inPKBUAQt3X(am)
        self.userManagesMemory = 1

    
    def _GeomParticleRenderer__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAqpfG()
        self.userManagesMemory = 1

    
    def _GeomParticleRenderer__overloaded_constructor_ptrConstGeomParticleRenderer(self, copy):
        self.this = libpandaphysics._inPKBUAf5c7(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAcZ5b:
            libpandaphysics._inPKBUAcZ5b(self.this)
        

    
    def setGeomNode(self, node):
        returnValue = libpandaphysics._inPKBUA2Hy2(self.this, node.this)
        return returnValue

    
    def getGeomNode(self):
        returnValue = libpandaphysics._inPKBUAWLyT(self.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _GeomParticleRenderer__overloaded_writeLinearForces_ptrConstGeomParticleRenderer_ptrOstream_int(self, out, indent):
        returnValue = libpandaphysics._inPKBUADC1b(self.this, out.this, indent)
        return returnValue

    
    def _GeomParticleRenderer__overloaded_writeLinearForces_ptrConstGeomParticleRenderer_ptrOstream(self, out):
        returnValue = libpandaphysics._inPKBUAmK_H(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._GeomParticleRenderer__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._GeomParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode(*_args)
            
            if isinstance(_args[0], GeomParticleRenderer):
                return self._GeomParticleRenderer__overloaded_constructor_ptrConstGeomParticleRenderer(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <GeomParticleRenderer> '
        elif numArgs == 2:
            return self._GeomParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_ptrPandaNode(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def writeLinearForces(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._GeomParticleRenderer__overloaded_writeLinearForces_ptrConstGeomParticleRenderer_ptrOstream(*_args)
        elif numArgs == 2:
            return self._GeomParticleRenderer__overloaded_writeLinearForces_ptrConstGeomParticleRenderer_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


