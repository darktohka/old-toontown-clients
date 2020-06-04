# File: G (Python 2.2)

from IntervalGlobal import *
import BasicEntities
import MovingPlatform

class GearEntity(BasicEntities.NodePathEntity):
    
    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.initGear()

    
    def destroy(self):
        self.destroyGear()
        BasicEntities.NodePathEntity.destroy(self)

    
    def initGear(self):
        model = loader.loadModelCopy('phase_9/models/cogHQ/FactoryGearB')
        self.gearParent = self.attachNewNode('gearParent-%s' % self.entId)
        if self.orientation == 'horizontal':
            vertNodes = model.findAllMatches('**/VerticalCollisions').asList()
            for node in vertNodes:
                node.stash()
            
            mPlat = MovingPlatform.MovingPlatform()
            mPlat.setupCopyModel(self.entId, model, 'HorizontalFloor')
            model = mPlat
        else:
            horizNodes = model.findAllMatches('**/HorizontalCollisions').asList()
            for node in horizNodes:
                node.stash()
            
            model.setZ(0.14999999999999999)
            model.flattenLight()
        model.setScale(self.gearScale)
        model.flattenLight()
        if self.orientation == 'vertical':
            self.gearParent.setP(-90)
        
        self.model = model
        self.model.reparentTo(self.gearParent)
        self.startRotate()

    
    def destroyGear(self):
        self.stopRotate()
        if isinstance(self.model, MovingPlatform.MovingPlatform):
            self.model.destroy()
        else:
            self.model.removeNode()
        del self.model
        self.gearParent.removeNode()
        del self.gearParent

    
    def startRotate(self):
        self.stopRotate()
        
        try:
            ivalDur = 360.0 / self.degreesPerSec
        except ZeroDivisionError:
            pass

        hOffset = 360.0
        if ivalDur < 0.0:
            ivalDur = -ivalDur
            hOffset = -hOffset
        
        self.rotateIval = LerpHprInterval(self.model, ivalDur, Vec3(hOffset, 0, 0), startHpr = Vec3(0, 0, 0), name = 'gearRot-%s' % self.entId)
        self.rotateIval.loop()
        self.rotateIval.setT((globalClock.getFrameTime() - self.level.startTime) + ivalDur * self.phaseShift)

    
    def stopRotate(self):
        if hasattr(self, 'rotateIval'):
            self.rotateIval.pause()
            del self.rotateIval
        

    if __dev__:
        
        def setDegreesPerSec(self, degreesPerSec):
            self.degreesPerSec = degreesPerSec
            self.startRotate()

        
        def setPhaseShift(self, phaseShift):
            self.phaseShift = phaseShift
            self.startRotate()

        
        def attribChanged(self, attrib, value):
            self.destroyGear()
            self.initGear()

    

