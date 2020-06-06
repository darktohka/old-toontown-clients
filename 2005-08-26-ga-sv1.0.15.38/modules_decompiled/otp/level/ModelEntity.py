# File: M (Python 2.2)

from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal
import BasicEntities

class ModelEntity(BasicEntities.NodePathEntity):
    LoadFuncs = {
        'loadModelCopy': loader.loadModelCopy,
        'loadModel': loader.loadModel,
        'loadModelOnce': loader.loadModelOnce }
    
    def __init__(self, level, entId):
        self.collisionsOnly = False
        self.loadType = 'loadModelCopy'
        self.flattenType = 'light'
        self.entInitialized = False
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.entInitialized = True
        self.model = None
        self.loadModel()

    
    def destroy(self):
        if self.model:
            self.model.removeNode()
            del self.model
        
        BasicEntities.NodePathEntity.destroy(self)

    
    def loadModel(self):
        if self.model:
            self.model.removeNode()
            self.model = None
        
        if self.modelPath is None:
            return None
        
        self.model = ModelEntity.LoadFuncs[self.loadType](self.modelPath)
        if self.model:
            self.model.reparentTo(self)
            if self.collisionsOnly:
                if __dev__:
                    self.model.setTransparency(1)
                    self.model.setColorScale(1, 1, 1, 0.10000000000000001)
                else:
                    self.model.hide()
            else:
                self.model.show()
            if self.modelPath in ('phase_9/models/cogHQ/woodCrateB.bam', 'phase_9/models/cogHQ/metal_crateB.bam', 'phase_10/models/cashbotHQ/CBMetalCrate.bam', 'phase_10/models/cogHQ/CBMetalCrate2.bam', 'phase_10/models/cashbotHQ/CBWoodCrate.bam'):
                cNode = self.find('**/wall')
                cNode.setZ(cNode, -0.75)
                colNode = self.find('**/collision')
                floor = colNode.find('**/floor')
                floor2 = floor.copyTo(colNode)
                floor2.setZ(floor2, -0.75)
            
            if self.flattenType == 'light':
                self.model.flattenLight()
            elif self.flattenType == 'medium':
                self.model.flattenMedium()
            elif self.flattenType == 'strong':
                self.model.flattenStrong()
            
        

    
    def setModelPath(self, path):
        self.modelPath = path
        self.loadModel()

    
    def setCollisionsOnly(self, collisionsOnly):
        self.collisionsOnly = collisionsOnly
        self.loadModel()


