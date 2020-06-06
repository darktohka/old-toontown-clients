# File: T (Python 2.2)

from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
from direct.showbase import Loader
from toontown.toontowngui import ToontownLoadingScreen

class ToontownLoader(Loader.Loader):
    
    def __init__(self, base):
        Loader.Loader.__init__(self, base)
        self.inBulkBlock = None
        self.blockName = None
        self.loadingScreen = ToontownLoadingScreen.ToontownLoadingScreen()

    
    def destroy(self):
        self.loadingScreen.destroy()
        del self.loadingScreen
        Loader.Loader.destroy(self)

    
    def beginBulkLoad(self, name, label, range, gui, tipCategory):
        Loader.Loader.notify.info("starting bulk load of block '%s'" % name)
        if self.inBulkBlock:
            Loader.Loader.notify.warning("Tried to start a block ('%s'), but am already in a block ('%s')" % (name, self.blockName))
            return None
        
        self.inBulkBlock = 1
        self.blockName = name
        self.loadingScreen.begin(range, label, gui, tipCategory)

    
    def endBulkLoad(self, name):
        if not (self.inBulkBlock):
            Loader.Loader.notify.warning("Tried to end a block ('%s'), but not in one" % name)
            return None
        
        if name != self.blockName:
            Loader.Loader.notify.warning("Tried to end a block ('%s'), other then the current one ('%s')" % (name, self.blockName))
            return None
        
        self.inBulkBlock = None
        (expectedCount, loadedCount) = self.loadingScreen.end()
        Loader.Loader.notify.info("At end of block '%s', expected %s, loaded %s" % (self.blockName, expectedCount, loadedCount))

    
    def abortBulkLoad(self):
        if self.inBulkBlock:
            Loader.Loader.notify.info("Aborting block ('%s')" % self.blockName)
            self.inBulkBlock = None
            self.loadingScreen.abort()
        

    
    def tick(self):
        if self.inBulkBlock:
            self.loadingScreen.tick()
            
            try:
                base.cr.considerHeartbeat()
            except:
                pass

        

    
    def loadModel(self, modelPath):
        ret = Loader.Loader.loadModel(self, modelPath)
        self.tick()
        return ret

    
    def loadModelOnce(self, modelPath):
        ret = Loader.Loader.loadModelOnce(self, modelPath)
        self.tick()
        return ret

    
    def loadModelCopy(self, modelPath):
        ret = Loader.Loader.loadModelCopy(self, modelPath)
        self.tick()
        return ret

    
    def loadModelNode(self, modelPath):
        ret = Loader.Loader.loadModelNode(self, modelPath)
        self.tick()
        return ret

    
    def loadFont(self, *args, **kw):
        ret = Loader.Loader.loadFont(self, *args, **args)
        self.tick()
        return ret

    
    def loadTexture(self, texturePath, alphaPath = None):
        ret = Loader.Loader.loadTexture(self, texturePath, alphaPath)
        self.tick()
        if alphaPath:
            self.tick()
        
        return ret

    
    def loadSfx(self, soundPath):
        ret = Loader.Loader.loadSfx(self, soundPath)
        self.tick()
        return ret

    
    def loadMusic(self, soundPath):
        ret = Loader.Loader.loadMusic(self, soundPath)
        self.tick()
        return ret

    
    def loadDNAFileAI(self, dnaStore, dnaFile):
        ret = loadDNAFileAI(dnaStore, dnaFile, CSDefault)
        self.tick()
        return ret

    
    def loadDNAFile(self, dnaStore, dnaFile):
        ret = loadDNAFile(dnaStore, dnaFile, CSDefault, 0)
        self.tick()
        return ret


