# File: L (Python 2.2)

from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
phaseChecker = None

class Loader:
    notify = directNotify.newCategory('Loader')
    modelCount = 0
    
    def __init__(self, base):
        self.base = base
        self.loader = PandaLoader()

    
    def destroy(self):
        del self.base
        del self.loader

    
    def loadModel(self, modelPath, fMakeNodeNamesUnique = 0):
        if phaseChecker:
            phaseChecker(modelPath)
        
        node = self.loader.loadSync(Filename(modelPath))
        if node != None:
            nodePath = NodePath(node)
            if fMakeNodeNamesUnique:
                self.makeNodeNamesUnique(nodePath, 0)
            
        else:
            nodePath = None
        return nodePath

    
    def loadModelOnce(self, modelPath):
        if phaseChecker:
            phaseChecker(modelPath)
        
        node = ModelPool.loadModel(modelPath)
        if node != None:
            nodePath = NodePath.anyPath(node)
        else:
            nodePath = None
        return nodePath

    
    def loadModelOnceUnder(self, modelPath, underNode):
        if phaseChecker:
            phaseChecker(modelPath)
        
        node = ModelPool.loadModel(modelPath)
        if node != None:
            nodePath = NodePath(underNode)
            nodePath.attachNewNode(node)
        else:
            nodePath = None
        return nodePath

    
    def loadModelCopy(self, modelPath):
        if phaseChecker:
            phaseChecker(modelPath)
        
        node = ModelPool.loadModel(modelPath)
        if node != None:
            return NodePath(node.copySubgraph())
        else:
            return None

    
    def loadModelNode(self, modelPath):
        if phaseChecker:
            phaseChecker(modelPath)
        
        return ModelPool.loadModel(modelPath)

    
    def unloadModel(self, modelPath):
        ModelPool.releaseModel(modelPath)

    
    def loadFont(self, modelPath, spaceAdvance = None, pointSize = None, pixelsPerUnit = None, scaleFactor = None, textureMargin = None, polyMargin = None, minFilter = None, magFilter = None, anisotropicDegree = None, lineHeight = None):
        if phaseChecker:
            phaseChecker(modelPath)
        
        font = FontPool.loadFont(modelPath)
        if font == None:
            font = StaticTextFont(PandaNode('empty'))
        
        if hasattr(font, 'setPointSize'):
            if pointSize != None:
                font.setPointSize(pointSize)
            
            if pixelsPerUnit != None:
                font.setPixelsPerUnit(pixelsPerUnit)
            
            if scaleFactor != None:
                font.setScaleFactor(scaleFactor)
            
            if textureMargin != None:
                font.setTextureMargin(textureMargin)
            
            if polyMargin != None:
                font.setPolyMargin(polyMargin)
            
            if minFilter != None:
                font.setMinFilter(minFilter)
            
            if magFilter != None:
                font.setMagFilter(magFilter)
            
            if anisotropicDegree != None:
                font.setAnisotropicDegree(anisotropicDegree)
            
        
        if lineHeight is not None:
            font.setLineHeight(lineHeight)
        
        if spaceAdvance is not None:
            font.setSpaceAdvance(spaceAdvance)
        
        return font

    
    def loadTexture(self, texturePath, alphaPath = None):
        if alphaPath is None:
            if phaseChecker:
                phaseChecker(texturePath)
            
            texture = TexturePool.loadTexture(texturePath)
        elif phaseChecker:
            phaseChecker(texturePath)
        
        texture = TexturePool.loadTexture(texturePath, alphaPath)
        return texture

    
    def unloadTexture(self, texture):
        TexturePool.releaseTexture(texture)

    
    def loadSfx(self, name):
        if phaseChecker:
            phaseChecker(name)
        
        sound = None
        if name:
            sound = base.sfxManagerList[0].getSound(name)
        
        if sound == None:
            Loader.notify.warning('Could not load sound file %s.' % name)
        
        return sound

    
    def loadMusic(self, name):
        sound = None
        if name:
            sound = base.musicManager.getSound(name)
        
        if sound == None:
            Loader.notify.warning('Could not load music file %s.' % name)
        
        return sound

    
    def makeNodeNamesUnique(self, nodePath, nodeCount):
        if nodeCount == 0:
            Loader.modelCount += 1
        
        nodePath.setName(nodePath.getName() + '_%d_%d' % (Loader.modelCount, nodeCount))
        for i in range(nodePath.getNumChildren()):
            nodeCount += 1
            self.makeNodeNamesUnique(nodePath.getChild(i), nodeCount)
        


