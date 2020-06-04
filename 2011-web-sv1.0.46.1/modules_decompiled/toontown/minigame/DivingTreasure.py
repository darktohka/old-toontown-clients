# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\DivingTreasure.py
from direct.showbase.DirectObject import DirectObject
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
import DivingGameGlobals

class DivingTreasure(DirectObject):
    __module__ = __name__

    def __init__(self, i):
        self.treasureNode = render.attachNewNode('treasure')
        loadBase = 'phase_4/models/minigames/'
        self.chest = loader.loadModel(loadBase + 'treasure.bam')
        self.chest.reparentTo(self.treasureNode)
        self.chest.setPos(0, 0, -25)
        self.chest.setScale(1, 0.7, 1)
        self.chestId = i
        self.grabbedId = 0
        self.moveLerp = Sequence()
        self.treasureNode.setScale(0.04)
        self.treasureNode.setPos(-15 + 10.0 * i, 0.25, -36.0)
        cSphere = CollisionSphere(0.0, 0.0, 0.0, 45)
        cSphere.setTangible(0)
        name = str(i)
        cSphereNode = CollisionNode(name)
        cSphereNode.setIntoCollideMask(DivingGameGlobals.CollideMask)
        cSphereNode.addSolid(cSphere)
        self.chestNode = cSphereNode
        self.chestCNP = self.treasureNode.attachNewNode(cSphereNode)

    def destroy(self):
        self.ignoreAll()
        del self.chest
        self.moveLerp.finish()
        del self.moveLerp
        self.treasureNode.removeNode()
        del self.treasureNode