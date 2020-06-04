# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedCrushableEntityAI.py
from otp.level import DistributedEntityAI
from direct.directnotify import DirectNotifyGlobal

class DistributedCrushableEntityAI(DistributedEntityAI.DistributedEntityAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCrushableEntityAI')

    def __init__(self, level, entId):
        self.isCrushable = 0
        self.crushCellId = None
        self.crushCell = None
        self.grid = None
        self.width = 1
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)
        return

    def generate(self):
        DistributedEntityAI.DistributedEntityAI.generate(self)
        self.setActiveCrushCell()
        if self.level:
            self.attachToGrid()

    def delete(self):
        self.ignoreAll()
        DistributedEntityAI.DistributedEntityAI.delete(self)

    def destroy(self):
        if self.crushCell != None:
            self.crushCell.unregisterCrushable(self.entId)
            self.crushCell = None
        DistributedEntityAI.DistributedEntityAI.destroy(self)
        return

    def attachToGrid(self):
        if self.gridId is not None:

            def setGrid(gridId=self.gridId, self=self):
                grid = self.level.entities.get(gridId, None)
                if grid:
                    self.grid = grid
                    self.grid.addObjectByPos(self.entId, self.pos, self.width)
                    self.b_setPosition(self.getPosition())
                    self.initGridDependents()
                    return 1
                return 0

            self.level.setEntityCreateCallback(self.gridId, setGrid)
        return

    def initGridDependents(self):
        pass

    def setActiveCrushCell(self):
        if self.crushCellId != None:
            self.notify.debug('setActiveCrushCell, entId: %d' % self.entId)
            self.crushCell = self.level.entities.get(self.crushCellId, None)
            if self.crushCell == None:
                self.accept(self.level.getEntityCreateEvent(self.crushCellId), self.setActiveCrushCell)
            else:
                self.isCrushable = 1
                self.crushCell.registerCrushable(self.entId)
        return

    def b_setPosition(self, pos):
        self.d_setPosition(pos)
        self.setPosition(pos)

    def d_setPosition(self, pos):
        self.sendUpdate('setPosition', [pos[0], pos[1], pos[2]])

    def setPosition(self, pos):
        self.pos = pos

    def getPosition(self):
        return self.grid.getObjPos(self.entId)

    def updateGrid(self):
        pass

    def doCrush(self, crusherId, axis):
        pass

    def setGridId(self, gridId):
        self.gridId = gridId
        self.attachToGrid()

    def setCrushCellId(self, crushCellId):
        self.crushCellId = crushCellId
        self.setActiveCrushCell()