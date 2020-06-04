# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\estate\DistributedGardenBox.py
import DistributedLawnDecor
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.ShowBase import *
import GardenGlobals
from toontown.toonbase import TTLocalizer
from toontown.estate import PlantingGUI
from toontown.estate import PlantTreeGUI
from direct.distributed import DistributedNode
from pandac.PandaModules import NodePath
from pandac.PandaModules import Vec3

class DistributedGardenBox(DistributedLawnDecor.DistributedLawnDecor):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGardenPlot')

    def __init__(self, cr):
        DistributedLawnDecor.DistributedLawnDecor.__init__(self, cr)
        self.plantPath = NodePath('plantPath')
        self.plantPath.reparentTo(self)
        self.plotScale = 1.0
        self.plantingGuiDoneEvent = 'plantingGuiDone'
        self.defaultModel = 'phase_5.5/models/estate/planterC'

    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        DistributedLawnDecor.DistributedLawnDecor.announceGenerate(self)

    def doModelSetup(self):
        if self.typeIndex == GardenGlobals.BOX_THREE:
            self.defaultModel = 'phase_5.5/models/estate/planterA'
        elif self.typeIndex == GardenGlobals.BOX_TWO:
            self.defaultModel = 'phase_5.5/models/estate/planterC'
        else:
            self.defaultModel = 'phase_5.5/models/estate/planterD'
            self.collSphereOffset = 0.0
            self.collSphereRadius = self.collSphereRadius * 1.41
            self.plotScale = Vec3(1.0, 1.0, 1.0)

    def setupShadow(self):
        pass

    def loadModel(self):
        self.rotateNode = self.plantPath.attachNewNode('rotate')
        self.model = None
        self.model = loader.loadModel(self.defaultModel)
        self.model.setScale(self.plotScale)
        self.model.reparentTo(self.rotateNode)
        self.stick2Ground()
        return

    def handleEnterPlot(self, entry=None):
        pass

    def handleExitPlot(self, entry=None):
        DistributedLawnDecor.DistributedLawnDecor.handleExitPlot(self, entry)

    def setTypeIndex(self, typeIndex):
        self.typeIndex = typeIndex