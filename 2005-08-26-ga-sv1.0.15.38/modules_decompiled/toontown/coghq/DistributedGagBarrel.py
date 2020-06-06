# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase.PandaObject import *
from direct.interval.IntervalGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal
import DistributedBarrelBase

class DistributedGagBarrel(DistributedBarrelBase.DistributedBarrelBase):
    
    def __init__(self, cr):
        self.gagLevelMax = 0
        DistributedBarrelBase.DistributedBarrelBase.__init__(self, cr)
        self.numGags = 0
        self.gagScale = 13.0

    
    def disable(self):
        DistributedBarrelBase.DistributedBarrelBase.disable(self)
        self.ignoreAll()

    
    def delete(self):
        self.gagModel.removeNode()
        del self.gagModel
        DistributedBarrelBase.DistributedBarrelBase.delete(self)

    
    def applyLabel(self):
        invModel = loader.loadModelCopy('phase_3.5/models/gui/inventory_icons')
        self.invModels = []
        ToontownBattleGlobals = ToontownBattleGlobals
        import toontown.toonbase
        for gagTrack in range(len(ToontownBattleGlobals.AvPropsNew)):
            itemList = []
            for item in range(len(ToontownBattleGlobals.AvPropsNew[gagTrack])):
                itemList.append(invModel.find('**/' + ToontownBattleGlobals.AvPropsNew[gagTrack][item]))
            
            self.invModels.append(itemList)
        
        invModel.removeNode()
        gagTrack = self.getGagTrack()
        gagLevel = self.getGagLevel()
        self.notify.debug('gagTrack = %s, gagLevel = %s' % (gagTrack, gagLevel))
        self.gagModel = self.invModels[gagTrack][gagLevel]
        self.gagModel.reparentTo(self.gagNode)
        self.gagModel.setScale(self.gagScale)
        self.gagModel.setPos(0, -0.10000000000000001, 0)
        del invModel

    
    def setNumGags(self, num):
        self.numGags = num
        if self.gagModel:
            if self.numGags == 0:
                self.gagModel.setColorScale(0.5, 0.5, 0.5, 1)
            else:
                self.gagModel.clearColorScale()
        

    
    def setGrab(self, avId):
        DistributedBarrelBase.DistributedBarrelBase.setGrab(self, avId)

    
    def resetBarrel(self):
        DistributedBarrelBase.DistributedBarrelBase.resetBarrel(self)
        self.gagModel.setScale(self.gagScale)


