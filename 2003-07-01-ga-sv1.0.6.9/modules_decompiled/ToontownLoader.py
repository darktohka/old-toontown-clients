# File: T (Python 2.2)

from PandaModules import *
from DirectNotifyGlobal import *
from DirectGui import *
import Loader
import Localizer

class ToontownLoader(Loader.Loader):
    
    def __init__(self, base):
        Loader.Loader.__init__(self, base)
        self.inBulkBlock = None
        self.blockName = None
        self.expectedCount = 0
        self.count = 0
        self.gui = loader.loadModel('phase_3/models/gui/progress-background')
        self.gui.find('**/runner').hide()
        self.waitBar = DirectWaitBar(guiId = 'ToontownLoaderWaitBar', parent = self.gui, frameSize = (-1.0600000000000001, 1.0600000000000001, -0.029999999999999999, 0.029999999999999999), pos = (0, 0, -0.84999999999999998), text = '', text_scale = 0.070000000000000007, text_pos = (-1.05, 0.074999999999999997, 0), text_fg = (0, 0, 0.5, 1), text_align = TextNode.ALeft)

    
    def beginBulkLoad(self, name, label, range, gui = 1):
        Loader.Loader.notify.info("starting bulk load of block '%s'" % name)
        if self.inBulkBlock:
            Loader.Loader.notify.warning("Tried to start a block ('%s'), but am already in a block ('%s')" % (name, self.blockName))
            return None
        
        self.inBulkBlock = 1
        self.blockName = name
        self.count = 0
        self.expectedCount = range
        self.waitBar['range'] = range
        self.waitBar['text'] = label
        if gui:
            self.waitBar.reparentTo(self.gui)
            self.gui.reparentTo(aspect2d, NO_FADE_SORT_INDEX)
        else:
            self.waitBar.reparentTo(aspect2d, NO_FADE_SORT_INDEX)
            self.gui.reparentTo(hidden)
        self.waitBar.update(self.count)

    
    def endBulkLoad(self, name):
        if not (self.inBulkBlock):
            Loader.Loader.notify.warning("Tried to end a block ('%s'), but not in one" % name)
            return None
        
        if name != self.blockName:
            Loader.Loader.notify.warning("Tried to end a block ('%s'), other then the current one ('%s')" % (name, self.blockName))
            return None
        
        Loader.Loader.notify.info("At end of block '%s', expected %s, loaded %s" % (self.blockName, self.expectedCount, self.count))
        self.inBulkBlock = None
        self.waitBar.finish()
        self.waitBar.reparentTo(self.gui)
        self.gui.reparentTo(hidden)

    
    def abortBulkLoad(self):
        if self.inBulkBlock:
            Loader.Loader.notify.info("Aborting block ('%s')" % self.blockName)
            self.inBulkBlock = None
            self.gui.reparentTo(hidden)
        

    
    def tick(self):
        if self.inBulkBlock:
            self.count = self.count + 1
            self.waitBar.update(self.count)
            
            try:
                toonbase.tcr.considerHeartbeat()
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


