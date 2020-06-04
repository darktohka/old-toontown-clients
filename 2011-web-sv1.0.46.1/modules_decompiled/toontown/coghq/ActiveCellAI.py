# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\ActiveCellAI.py
from otp.level import DistributedEntityAI
from direct.directnotify import DirectNotifyGlobal

class ActiveCellAI(DistributedEntityAI.DistributedEntityAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('ActiveCellAI')

    def __init__(self, level, entId):
        self.state = 0
        self.grid = None
        self.occupantIds = []
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)

        def setGrid(gridId=self.gridId, self=self):
            self.grid = self.level.entities.get(gridId, None)
            if self.grid:
                self.grid.addActiveCell(self)
                return 1
            return 0

        if not setGrid():
            self.accept(self.level.getEntityCreateEvent(self.gridId), setGrid)
        return

    def generate(self):
        DistributedEntityAI.DistributedEntityAI.generate(self)

    def delete(self):
        self.notify.debug('delete')
        self.ignoreAll()
        DistributedEntityAI.DistributedEntityAI.delete(self)

    def getState(self):
        return self.state

    def b_setState(self, state, objId=None):
        self.setState(state, objId)
        self.d_setState(state, objId)

    def d_setState(self, state, objId=None):
        if not objId:
            objId = 0
        self.sendUpdate('setState', [state, objId])

    def setState(self, state, objId=None):
        self.state = state
        if state:
            self.occupantIds.append(objId)
        else:
            try:
                self.occupantIds.remove(objId)
            except:
                self.notify.warning("couldn't remove %s from active cell" % objId)

    def getRowCol(self):
        return [
         self.row, self.col]