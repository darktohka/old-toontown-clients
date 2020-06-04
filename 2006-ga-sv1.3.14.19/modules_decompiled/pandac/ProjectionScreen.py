# File: P (Python 2.2)

import types
import libpandafx
import libpandafxDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class ProjectionScreen(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandafxDowncasts,
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ProjectionScreen__overloaded_constructor_atomicstring(self, name):
        self.this = libpandafx._inP1uO4VUBz(name)
        self.userManagesMemory = 1

    
    def _ProjectionScreen__overloaded_constructor(self):
        self.this = libpandafx._inP1uO4FAAN()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandafx._inP1uO4k7Q4()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setProjector(self, projector):
        returnValue = libpandafx._inP1uO4KtME(self.this, projector.this)
        return returnValue

    
    def getProjector(self):
        returnValue = libpandafx._inP1uO4qx3t(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def generateScreen(self, projector, screenName, numXVerts, numYVerts, distance, fillRatio):
        returnValue = libpandafx._inP1uO4DKPY(self.this, projector.this, screenName, numXVerts, numYVerts, distance, fillRatio)
        import GeomNode
        returnObject = GeomNode.GeomNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def regenerateScreen(self, projector, screenName, numXVerts, numYVerts, distance, fillRatio):
        returnValue = libpandafx._inP1uO4asPG(self.this, projector.this, screenName, numXVerts, numYVerts, distance, fillRatio)
        return returnValue

    
    def makeFlatMesh(self, thisNp, camera):
        returnValue = libpandafx._inP1uO4G914(self.this, thisNp.this, camera.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setTexcoordName(self, texcoordName):
        returnValue = libpandafx._inP1uO4ilGE(self.this, texcoordName)
        return returnValue

    
    def getTexcoordName(self):
        returnValue = libpandafx._inP1uO4d3gx(self.this)
        return returnValue

    
    def setInvertUvs(self, invertUvs):
        returnValue = libpandafx._inP1uO4xsWS(self.this, invertUvs)
        return returnValue

    
    def getInvertUvs(self):
        returnValue = libpandafx._inP1uO4SQ8g(self.this)
        return returnValue

    
    def setVignetteOn(self, vignetteOn):
        returnValue = libpandafx._inP1uO4dO6S(self.this, vignetteOn)
        return returnValue

    
    def getVignetteOn(self):
        returnValue = libpandafx._inP1uO4VhFT(self.this)
        return returnValue

    
    def setVignetteColor(self, vignetteColor):
        returnValue = libpandafx._inP1uO4CmW1(self.this, vignetteColor.this)
        return returnValue

    
    def getVignetteColor(self):
        returnValue = libpandafx._inP1uO4SAXj(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setFrameColor(self, frameColor):
        returnValue = libpandafx._inP1uO4Tjpi(self.this, frameColor.this)
        return returnValue

    
    def getFrameColor(self):
        returnValue = libpandafx._inP1uO4ViMC(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def recompute(self):
        returnValue = libpandafx._inP1uO49AIQ(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._ProjectionScreen__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._ProjectionScreen__overloaded_constructor_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


