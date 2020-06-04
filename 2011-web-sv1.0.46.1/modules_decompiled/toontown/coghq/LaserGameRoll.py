# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\LaserGameRoll.py
from toontown.coghq import LaserGameBase
from direct.distributed import ClockDelta
from direct.task import Task
import random

class LaserGameRoll(LaserGameBase.LaserGameBase):
    __module__ = __name__

    def __init__(self, funcSuccess, funcFail, funcSendGrid, funcSetGrid):
        LaserGameBase.LaserGameBase.__init__(self, funcSuccess, funcFail, funcSendGrid, funcSetGrid)
        self.setGridSize(5, 5)
        self.blankGrid()

    def win(self):
        if not self.finshed:
            self.blankGrid()
            self.funcSendGrid()
        LaserGameBase.LaserGameBase.win(self)

    def lose(self):
        self.blankGrid()
        self.funcSendGrid()
        LaserGameBase.LaserGameBase.lose(self)

    def startGrid(self):
        LaserGameBase.LaserGameBase.startGrid(self)
        for column in range(0, self.gridNumX):
            for row in range(0, self.gridNumY):
                tile = random.choice([10, 13])
                self.gridData[column][row] = tile

        for column in range(0, self.gridNumX):
            self.gridData[column][self.gridNumY - 1] = 12

    def hit(self, hitX, hitY, oldx=-1, oldy=-1):
        if self.finshed:
            return
        if self.gridData[hitX][hitY] == 10:
            self.gridData[hitX][hitY] = 13
        elif self.gridData[hitX][hitY] == 13:
            self.gridData[hitX][hitY] = 10
        if self.checkForWin():
            self.win()
        else:
            self.funcSendGrid()

    def checkForWin(self):
        count1 = 0
        count2 = 0
        for column in range(0, self.gridNumX):
            for row in range(0, self.gridNumY):
                if self.gridData[column][row] == 10:
                    count1 += 1
                elif self.gridData[column][row] == 13:
                    count2 += 1

        if count1 and count2:
            return 0
        else:
            return 1