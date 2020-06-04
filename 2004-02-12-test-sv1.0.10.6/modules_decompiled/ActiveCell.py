# File: A (Python 2.2)

from PandaModules import *
import BasicEntities
import DirectNotifyGlobal

class ActiveCell(BasicEntities.DistributedNodePathEntity):
    notify = DirectNotifyGlobal.directNotify.newCategory('ActiveCell')
    
    def __init__(self, cr):
        BasicEntities.DistributedNodePathEntity.__init__(self, cr)
        self.occupantId = -1
        self.state = 0

    
    def announceGenerate(self):
        BasicEntities.DistributedNodePathEntity.announceGenerate(self)
        self.loadModel()

    
    def loadModel(self):
        if 0 and __debug__:
            grid = self.level.entities.get(self.gridId, None)
            if grid:
                pos = grid.getPos() + Vec3(self.col * grid.cellSize, self.row * grid.cellSize, 0)
                model = loader.loadModel('phase_5/models/modules/suit_walls.bam')
                model.setScale(grid.cellSize, 1, grid.cellSize)
                model.setP(-90)
                model.flattenMedium()
                model.setZ(0.050000000000000003)
                model.setColorScale(1, 0, 0, 0.5)
                model.copyTo(self)
                self.setPos(pos)
            
        
        return None

    
    def setState(self, state, objId):
        self.state = state
        self.occupantId = objId

    if __dev__:
        
        def attribChanged(self, *args):
            model = self.find('*')
            if not model.isEmpty():
                model.removeNode()
            
            self.loadModel()

    

