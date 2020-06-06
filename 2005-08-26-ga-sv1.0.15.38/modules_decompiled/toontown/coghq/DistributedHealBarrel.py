# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase.PandaObject import *
from direct.interval.IntervalGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal
import DistributedBarrelBase

class DistributedHealBarrel(DistributedBarrelBase.DistributedBarrelBase):
    
    def __init__(self, cr):
        DistributedBarrelBase.DistributedBarrelBase.__init__(self, cr)
        self.numGags = 0
        self.gagScale = 0.59999999999999998

    
    def disable(self):
        DistributedBarrelBase.DistributedBarrelBase.disable(self)
        self.ignoreAll()

    
    def delete(self):
        self.gagModel.removeNode()
        del self.gagModel
        DistributedBarrelBase.DistributedBarrelBase.delete(self)

    
    def applyLabel(self):
        self.gagModel = loader.loadModelCopy('phase_4/models/props/icecream')
        self.gagModel.reparentTo(self.gagNode)
        self.gagModel.find('**/p1_2').clearBillboard()
        self.gagModel.setScale(self.gagScale)
        self.gagModel.setPos(0, -0.10000000000000001, -0.10000000000000001 - self.gagScale)

    
    def setGrab(self, avId):
        DistributedBarrelBase.DistributedBarrelBase.setGrab(self, avId)


