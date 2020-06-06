# File: G (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BaseParticleRenderer

class GeomParticleRenderer(BaseParticleRenderer.BaseParticleRenderer, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _GeomParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_ptrPandaNode(self, am, geomNode):
        self.this = libpandaphysics._inPKBUAewJz(am, geomNode.this)
        self.userManagesMemory = 1

    
    def _GeomParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode(self, am):
        self.this = libpandaphysics._inPKBUAQt3X(am)
        self.userManagesMemory = 1

    
    def _GeomParticleRenderer__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAqpfG()
        self.userManagesMemory = 1

    
    def _GeomParticleRenderer__overloaded_constructor_ptrConstGeomParticleRenderer(self, copy):
        self.this = libpandaphysics._inPKBUAc5c7(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAcZ5b:
            libpandaphysics._inPKBUAcZ5b(self.this)
        

    
    def setGeomNode(self, node):
        returnValue = libpandaphysics._inPKBUA1Hy2(self.this, node.this)
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

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._GeomParticleRenderer__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._GeomParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode(_args[0])
            elif isinstance(_args[0], GeomParticleRenderer):
                return self._GeomParticleRenderer__overloaded_constructor_ptrConstGeomParticleRenderer(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <GeomParticleRenderer> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import PandaNode
                if isinstance(_args[1], PandaNode.PandaNode):
                    return self._GeomParticleRenderer__overloaded_constructor___enum__ParticleRendererAlphaMode_ptrPandaNode(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <PandaNode.PandaNode> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


