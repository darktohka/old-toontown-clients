# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\ActiveCell.py
from pandac.PandaModules import *
from otp.level import BasicEntities
from direct.directnotify import DirectNotifyGlobal

class ActiveCell(BasicEntities.DistributedNodePathEntity):
    __module__ = __name__
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
                model.setZ(0.05)
                model.setColorScale(1, 0, 0, 0.5)
                model.copyTo(self)
                self.setPos(pos)
        return

    def setState(self, state, objId):
        self.state = state
        self.occupantId = objId

    if __dev__:

        def attribChanged(self, *args):
            model = self.find('*')
            if not model.isEmpty():
                model.removeNode()
            self.loadModel()