# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\distributed\GridParent.py
from pandac.PandaModules import *

class GridParent:
    __module__ = __name__
    GridZone2CellOrigin = {}
    GridZone2count = {}

    @staticmethod
    def getCellOrigin(grid, zoneId):
        tup = (grid, zoneId)
        if tup not in GridParent.GridZone2count:
            GridParent.GridZone2count[tup] = 0
            GridParent.GridZone2CellOrigin[tup] = grid.attachNewNode('cellOrigin-%s' % zoneId)
            cellPos = grid.getZoneCellOrigin(zoneId)
            GridParent.GridZone2CellOrigin[tup].setPos(*cellPos)
        GridParent.GridZone2count[tup] += 1
        return GridParent.GridZone2CellOrigin[tup]

    @staticmethod
    def releaseCellOrigin(grid, zoneId):
        tup = (grid, zoneId)
        GridParent.GridZone2count[tup] -= 1
        if GridParent.GridZone2count[tup] == 0:
            del GridParent.GridZone2count[tup]
            GridParent.GridZone2CellOrigin[tup].removeNode()
            del GridParent.GridZone2CellOrigin[tup]

    def __init__(self, av):
        self.av = av
        self.grid = None
        self.ownCellOrigin = NodePath('cellOrigin')
        self.cellOrigin = self.ownCellOrigin
        return

    def delete(self):
        if self.av:
            if self.av.getParent() == self.cellOrigin:
                self.av.detachNode()
            del self.av
            self.av = None
        if self.ownCellOrigin is not None:
            self.ownCellOrigin.removeNode()
            self.ownCellOrigin = None
        if self.grid is not None:
            self.releaseCellOrigin(self.grid, self.zoneId)
            self.grid = None
            self.zoneId = None
        return

    def setGridParent(self, grid, zoneId, teleport=0):
        if self.av.getParent().isEmpty():
            teleport = 1
        if not teleport:
            self.av.wrtReparentTo(hidden)
        if self.grid is not None:
            self.releaseCellOrigin(self.grid, self.zoneId)
        self.grid = grid
        self.zoneId = zoneId
        self.cellOrigin = self.getCellOrigin(self.grid, self.zoneId)
        if not teleport:
            self.av.wrtReparentTo(self.cellOrigin)
        else:
            self.av.reparentTo(self.cellOrigin)
        return