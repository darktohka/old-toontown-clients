# File: S (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import BaseParticleRenderer

class SpriteParticleRenderer(BaseParticleRenderer.BaseParticleRenderer, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    STFromNode = 1
    STTexture = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _SpriteParticleRenderer__overloaded_constructor_ptrConstSpriteParticleRenderer(self, copy):
        self.this = libpandaphysics._inPKBUATL04(copy.this)
        self.userManagesMemory = 1

    
    def _SpriteParticleRenderer__overloaded_constructor_ptrTexture(self, tex):
        self.this = libpandaphysics._inPKBUAd0Mb(tex.this)
        self.userManagesMemory = 1

    
    def _SpriteParticleRenderer__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUACqZT()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAcZ5b:
            libpandaphysics._inPKBUAcZ5b(self.this)
        

    
    def getSourceType(self):
        returnValue = libpandaphysics._inPKBUARv8R(self.this)
        return returnValue

    
    def setFromNode(self, nodePath):
        returnValue = libpandaphysics._inPKBUA_bAP(self.this, nodePath.this)
        return returnValue

    
    def setTexture(self, tex):
        returnValue = libpandaphysics._inPKBUAsbbZ(self.this, tex.this)
        return returnValue

    
    def setLlUv(self, llUv):
        returnValue = libpandaphysics._inPKBUAg2Qj(self.this, llUv.this)
        return returnValue

    
    def setUrUv(self, urUv):
        returnValue = libpandaphysics._inPKBUAKsff(self.this, urUv.this)
        return returnValue

    
    def setColor(self, color):
        returnValue = libpandaphysics._inPKBUAQJ7q(self.this, color.this)
        return returnValue

    
    def setXScaleFlag(self, animateXRatio):
        returnValue = libpandaphysics._inPKBUA0uOC(self.this, animateXRatio)
        return returnValue

    
    def setYScaleFlag(self, animateYRatio):
        returnValue = libpandaphysics._inPKBUAMpOe(self.this, animateYRatio)
        return returnValue

    
    def setAnimAngleFlag(self, animateTheta):
        returnValue = libpandaphysics._inPKBUADpse(self.this, animateTheta)
        return returnValue

    
    def setInitialXScale(self, initialXScale):
        returnValue = libpandaphysics._inPKBUAFv64(self.this, initialXScale)
        return returnValue

    
    def setFinalXScale(self, finalXScale):
        returnValue = libpandaphysics._inPKBUA6PRG(self.this, finalXScale)
        return returnValue

    
    def setInitialYScale(self, initialYScale):
        returnValue = libpandaphysics._inPKBUALvDH(self.this, initialYScale)
        return returnValue

    
    def setFinalYScale(self, finalYScale):
        returnValue = libpandaphysics._inPKBUAe3VG(self.this, finalYScale)
        return returnValue

    
    def setNonanimatedTheta(self, theta):
        returnValue = libpandaphysics._inPKBUARm_e(self.this, theta)
        return returnValue

    
    def setAlphaBlendMethod(self, bm):
        returnValue = libpandaphysics._inPKBUAvlsQ(self.this, bm)
        return returnValue

    
    def setAlphaDisable(self, ad):
        returnValue = libpandaphysics._inPKBUA4EbD(self.this, ad)
        return returnValue

    
    def getTexture(self):
        returnValue = libpandaphysics._inPKBUAcWud(self.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getLlUv(self):
        returnValue = libpandaphysics._inPKBUAnEn7(self.this)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getUrUv(self):
        returnValue = libpandaphysics._inPKBUAcR23(self.this)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getColor(self):
        returnValue = libpandaphysics._inPKBUATSQe(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getXScaleFlag(self):
        returnValue = libpandaphysics._inPKBUAFsYl(self.this)
        return returnValue

    
    def getYScaleFlag(self):
        returnValue = libpandaphysics._inPKBUAChYB(self.this)
        return returnValue

    
    def getAnimAngleFlag(self):
        returnValue = libpandaphysics._inPKBUAS3Kv(self.this)
        return returnValue

    
    def getInitialXScale(self):
        returnValue = libpandaphysics._inPKBUA9dBl(self.this)
        return returnValue

    
    def getFinalXScale(self):
        returnValue = libpandaphysics._inPKBUAyH8a(self.this)
        return returnValue

    
    def getInitialYScale(self):
        returnValue = libpandaphysics._inPKBUA_dIz(self.this)
        return returnValue

    
    def getFinalYScale(self):
        returnValue = libpandaphysics._inPKBUAePBb(self.this)
        return returnValue

    
    def getNonanimatedTheta(self):
        returnValue = libpandaphysics._inPKBUAqpFo(self.this)
        return returnValue

    
    def getAlphaBlendMethod(self):
        returnValue = libpandaphysics._inPKBUApCjT(self.this)
        return returnValue

    
    def getAlphaDisable(self):
        returnValue = libpandaphysics._inPKBUAb0hv(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._SpriteParticleRenderer__overloaded_constructor(*_args)
        elif numArgs == 1:
            import Texture
            if isinstance(_args[0], Texture.Texture):
                return self._SpriteParticleRenderer__overloaded_constructor_ptrTexture(*_args)
            
            if isinstance(_args[0], SpriteParticleRenderer):
                return self._SpriteParticleRenderer__overloaded_constructor_ptrConstSpriteParticleRenderer(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Texture.Texture> <SpriteParticleRenderer> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    sourceTextureName = None
    sourceFileName = None
    sourceNodeName = None
    
    def getSourceTextureName(self):
        if self.sourceTextureName == None:
            SpriteParticleRenderer.sourceTextureName = base.config.GetString('particle-sprite-texture', 'phase_3/maps/eyes.jpg')
        
        return self.sourceTextureName

    
    def setSourceTextureName(self, name):
        self.sourceTextureName = name

    
    def setTextureFromFile(self, fileName = None):
        if fileName == None:
            fileName = self.getSourceTextureName()
        else:
            self.setSourceTextureName(fileName)
        t = loader.loadTexture(fileName)
        if t != None:
            self.setTexture(t)
        else:
            print "Couldn't find rendererSpriteTexture file: %s" % fileName

    
    def getSourceFileName(self):
        if self.sourceFileName == None:
            SpriteParticleRenderer.sourceFileName = base.config.GetString('particle-sprite-model', 'phase_3.5/models/props/suit-particles')
        
        return self.sourceFileName

    
    def setSourceFileName(self, name):
        self.sourceFileName = name

    
    def getSourceNodeName(self):
        if self.sourceNodeName == None:
            SpriteParticleRenderer.sourceNodeName = base.config.GetString('particle-sprite-node', '**/fire')
        
        return self.sourceNodeName

    
    def setSourceNodeName(self, name):
        self.sourceNodeName = name

    
    def setTextureFromNode(self, modelName = None, nodeName = None):
        if modelName == None:
            modelName = self.getSourceFileName()
        else:
            self.setSourceFileName(modelName)
        if nodeName == None:
            nodeName = self.getSourceNodeName()
        else:
            self.setSourceNodeName(nodeName)
        m = loader.loadModelOnce(modelName)
        if m == None:
            print "SpriteParticleRenderer: Couldn't find model: %s!" % modelName
            return None
        
        nodeName = self.getSourceNodeName()
        np = m.find(nodeName)
        if np.isEmpty():
            print "SpriteParticleRenderer: Couldn't find node: %s!" % nodeName
            m.removeNode()
            return None
        
        self.setFromNode(np)
        m.removeNode()


