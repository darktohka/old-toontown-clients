# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\LaserGameAvoid.py
from toontown.coghq import LaserGameBase
from direct.distributed import ClockDelta
from direct.task import Task
import random

class LaserGameAvoid(LaserGameBase.LaserGameBase):
    __module__ = __name__

    def __init__(self, funcSuccess, funcFail, funcSendGrid, funcSetGrid):
        LaserGameBase.LaserGameBase.__init__(self, funcSuccess, funcFail, funcSendGrid, funcSetGrid)
        self.setGridSize(8, 8)
        self.blankGrid()
        self.cycleName = simbase.air.trueUniqueName('AvoidGame')

    def delete(self):
        LaserGameBase.LaserGameBase.delete(self)
        self.endTask()

    def win(self):
        if not self.finshed:
            self.blankGrid()
            self.funcSendGrid()
            self.endTask()
        LaserGameBase.LaserGameBase.win(self)

    def lose(self):
        self.endTask()
        self.blankGrid()
        self.funcSendGrid()
        LaserGameBase.LaserGameBase.lose(self)

    def endTask(self):
        taskMgr.remove(self.cycleName)

    def startGrid(self):
        LaserGameBase.LaserGameBase.startGrid(self)
        for column in range(0, self.gridNumX):
            for row in range(0, self.gridNumY):
                tile = random.choice([0, 14, 12])
                self.gridData[column][row] = tile

        taskMgr.doMethodLater(2.5, self.__cycle, self.cycleName)

    def __cycle(self, taskMgrFooler=0):
        if not hasattr(self, 'gridNumX'):
            return Task.done
        for column in range(0, self.gridNumX):
            for row in range(0, self.gridNumY):
                if self.gridData[column][row] == 0:
                    tile = random.choice([0, 14])
                    self.gridData[column][row] = tile
                elif self.gridData[column][row] == 14:
                    tile = 12
                    self.gridData[column][row] = tile
                elif self.gridData[column][row] == 12:
                    tile = 0
                    self.gridData[column][row] = tile

        if not self.finshed:
            taskMgr.doMethodLater(2.5, self.__cycle, self.cycleName)
            self.funcSendGrid()
        return Task.done