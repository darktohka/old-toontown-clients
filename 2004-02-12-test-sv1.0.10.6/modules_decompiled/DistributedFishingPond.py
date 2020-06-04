# File: D (Python 2.2)

import DistributedObject
import DirectNotifyGlobal
import ToontownGlobals
import Localizer
import FishGlobals
from PandaModules import Vec3
import Task

class DistributedFishingPond(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingPond')
    pollInterval = 0.5
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.notify.debug('init')
        self.targets = { }
        self.area = None
        self.localToonBobPos = None
        self.localToonSpot = None

    
    def disable(self):
        self.stopCheckingTargets()
        DistributedObject.DistributedObject.disable(self)

    
    def setArea(self, area):
        self.area = area

    
    def getArea(self):
        return self.area

    
    def addTarget(self, target):
        self.notify.debug('addTarget: %s' % target)
        self.targets[target.getDoId()] = target

    
    def removeTarget(self, target):
        self.notify.debug('removeTarget: %s' % target)
        del self.targets[target.getDoId()]

    
    def startCheckingTargets(self, spot, bobPos):
        self.localToonSpot = spot
        self.localToonBobPos = bobPos
        taskMgr.doMethodLater(self.pollInterval * 2, self.checkTargets, self.taskName('checkTargets'))

    
    def stopCheckingTargets(self):
        taskMgr.remove(self.taskName('checkTargets'))
        self.localToonSpot = None
        self.localToonBobPos = None

    
    def checkTargets(self, task = None):
        for target in self.targets.values():
            targetPos = target.getPos(render)
            distVec = Vec3(targetPos - self.localToonBobPos)
            dist = distVec.length()
            if dist < target.getRadius():
                self.notify.debug('checkTargets: hit target: %s' % target.getDoId())
                self.d_hitTarget(target)
                return Task.done
            
        
        taskMgr.doMethodLater(self.pollInterval, self.checkTargets, self.taskName('checkTargets'))
        return Task.done

    
    def d_hitTarget(self, target):
        self.localToonSpot.hitTarget()
        self.sendUpdate('hitTarget', [
            target.getDoId()])


