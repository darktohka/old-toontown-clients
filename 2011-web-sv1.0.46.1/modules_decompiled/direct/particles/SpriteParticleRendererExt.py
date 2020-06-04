# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\particles\SpriteParticleRendererExt.py
from pandac.PandaModules import SpriteParticleRenderer

class SpriteParticleRendererExt(SpriteParticleRenderer):
    __module__ = __name__
    sourceTextureName = None
    sourceFileName = None
    sourceNodeName = None

    def getSourceTextureName(self):
        if self.sourceTextureName == None:
            SpriteParticleRendererExt.sourceTextureName = base.config.GetString('particle-sprite-texture', 'maps/lightbulb.rgb')
        return self.sourceTextureName

    def setSourceTextureName(self, name):
        self.sourceTextureName = name

    def setTextureFromFile(self, fileName=None):
        if fileName == None:
            fileName = self.getSourceTextureName()
        t = loader.loadTexture(fileName)
        if t != None:
            self.setTexture(t, t.getYSize())
            self.setSourceTextureName(fileName)
            return True
        else:
            print "Couldn't find rendererSpriteTexture file: %s" % fileName
            return False
        return

    def addTextureFromFile(self, fileName=None):
        if self.getNumAnims() == 0:
            return self.setTextureFromFile(fileName)
        if fileName == None:
            fileName = self.getSourceTextureName()
        t = loader.loadTexture(fileName)
        if t != None:
            self.addTexture(t, t.getYSize())
            return True
        else:
            print "Couldn't find rendererSpriteTexture file: %s" % fileName
            return False
        return

    def getSourceFileName(self):
        if self.sourceFileName == None:
            SpriteParticleRendererExt.sourceFileName = base.config.GetString('particle-sprite-model', 'models/misc/smiley')
        return self.sourceFileName

    def setSourceFileName(self, name):
        self.sourceFileName = name

    def getSourceNodeName(self):
        if self.sourceNodeName == None:
            SpriteParticleRendererExt.sourceNodeName = base.config.GetString('particle-sprite-node', '**/*')
        return self.sourceNodeName

    def setSourceNodeName(self, name):
        self.sourceNodeName = name

    def setTextureFromNode(self, modelName=None, nodeName=None, sizeFromTexels=False):
        if modelName == None:
            modelName = self.getSourceFileName()
            if nodeName == None:
                nodeName = self.getSourceNodeName()
        m = loader.loadModel(modelName)
        if m == None:
            print "SpriteParticleRendererExt: Couldn't find model: %s!" % modelName
            return False
        np = m.find(nodeName)
        if np.isEmpty():
            print "SpriteParticleRendererExt: Couldn't find node: %s!" % nodeName
            m.removeNode()
            return False
        self.setFromNode(np, modelName, nodeName, sizeFromTexels)
        self.setSourceFileName(modelName)
        self.setSourceNodeName(nodeName)
        m.removeNode()
        return True

    def addTextureFromNode(self, modelName=None, nodeName=None, sizeFromTexels=False):
        if self.getNumAnims() == 0:
            return self.setTextureFromNode(modelName, nodeName, sizeFromTexels)
        if modelName == None:
            modelName = self.getSourceFileName()
            if nodeName == None:
                nodeName = self.getSourceNodeName()
        m = loader.loadModel(modelName)
        if m == None:
            print "SpriteParticleRendererExt: Couldn't find model: %s!" % modelName
            return False
        np = m.find(nodeName)
        if np.isEmpty():
            print "SpriteParticleRendererExt: Couldn't find node: %s!" % nodeName
            m.removeNode()
            return False
        self.addFromNode(np, modelName, nodeName, sizeFromTexels)
        m.removeNode()
        return True