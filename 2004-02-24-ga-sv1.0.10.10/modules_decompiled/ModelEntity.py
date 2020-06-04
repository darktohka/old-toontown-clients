# File: M (Python 2.2)

from ToontownGlobals import *
import DirectNotifyGlobal
import BasicEntities

class ModelEntity(BasicEntities.NodePathEntity):
    
    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
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
        
        if self.modelPath:
            self.model = loader.loadModel(self.modelPath)
            if self.model:
                self.model.reparentTo(self)
            
        
        if self.modelPath in ('phase_9/models/cogHQ/woodCrateB.bam', 'phase_9/models/cogHQ/metal_crateB.bam'):
            cNode = self.find('**/wall')
            cNode.setZ(-0.75)
            colNode = self.find('**/collision')
            floor = colNode.find('**/floor')
            floor2 = floor.copyTo(colNode)
            floor2.setZ(-0.75)
        

    
    def setModelPath(self, path):
        self.modelPath = path
        self.loadModel()


