# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\fishing\FourCornerBingo.py
from direct.directnotify import DirectNotifyGlobal
from toontown.fishing import BingoGlobals
from toontown.fishing import BingoCardBase

class FourCornerBingo(BingoCardBase.BingoCardBase):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FourCornerBingo')
    corners = [
     0, BingoGlobals.CARD_ROWS - 1, BingoGlobals.CARD_COLS * (BingoGlobals.CARD_ROWS - 1), BingoGlobals.CARD_COLS * BingoGlobals.CARD_ROWS - 1]

    def __init__(self, cardSize=BingoGlobals.CARD_SIZE, rowSize=BingoGlobals.CARD_ROWS, colSize=BingoGlobals.CARD_COLS):
        BingoCardBase.BingoCardBase.__init__(self, cardSize, rowSize, colSize)
        self.gameType = BingoGlobals.FOURCORNER_CARD

    def checkForWin(self, id):
        corners = self.corners
        if self.cellCheck(corners[0]) and self.cellCheck(corners[1]) and self.cellCheck(corners[2]) and self.cellCheck(corners[3]):
            return BingoGlobals.WIN
        return BingoGlobals.NO_UPDATE

    def checkForColor(self, id):
        (topLeft, topRight, bottomLeft, bottomRight) = (0, 0, 0, 0)
        if id == self.corners[0]:
            topLeft = 1
        elif id == self.corners[1]:
            topRight = 1
        elif id == self.corners[2]:
            bottomLeft = 1
        elif id == self.corners[3]:
            bottomRight = 1
        return topLeft or topRight or bottomLeft or bottomRight

    def checkForBingo(self):
        return self.checkForWin(0)