# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\estate\DistributedAnimatedStatuary.py
from pandac.PandaModules import NodePath
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.estate import DistributedStatuary
from toontown.estate import GardenGlobals
from direct.actor import Actor

class DistributedAnimatedStatuary(DistributedStatuary.DistributedStatuary):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedAnimatedStatuary')

    def __init__(self, cr):
        self.notify.debug('constructing DistributedAnimatedStatuary')
        DistributedStatuary.DistributedStatuary.__init__(self, cr)

    def loadModel(self):
        self.rotateNode = self.plantPath.attachNewNode('rotate')
        self.model = Actor.Actor()
        animPath = self.modelPath + self.anims[1]
        self.model.loadModel(self.modelPath + self.anims[0])
        self.model.loadAnims(dict([[self.anims[1], animPath]]))
        colNode = self.model.find('**/+CollisionNode')
        if self.typeIndex == 234:
            colNode.setScale(0.5)
        if not colNode.isEmpty():
            (score, multiplier) = ToontownGlobals.PinballScoring[ToontownGlobals.PinballStatuary]
            if self.pinballScore:
                score = self.pinballScore[0]
                multiplier = self.pinballScore[1]
            scoreNodePath = NodePath('statuary-%d-%d' % (score, multiplier))
            colNode.setName('statuaryCol')
            scoreNodePath.reparentTo(colNode.getParent())
            colNode.reparentTo(scoreNodePath)
        self.model.setScale(self.worldScale)
        self.model.reparentTo(self.rotateNode)
        self.model.loop(self.anims[1])

    def setTypeIndex(self, typeIndex):
        DistributedStatuary.DistributedStatuary.setTypeIndex(self, typeIndex)
        self.anims = GardenGlobals.PlantAttributes[typeIndex]['anims']

    def setupShadow(self):
        if self.typeIndex == 234:
            pass
        else:
            DistributedStatuary.DistributedStatuary.setupShadow()