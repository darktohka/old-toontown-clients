# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\fishing\NormalBingo.py
from direct.directnotify import DirectNotifyGlobal
from toontown.fishing import BingoGlobals
from toontown.fishing import BingoCardBase

class NormalBingo(BingoCardBase.BingoCardBase):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('NormalBingo')

    def __init__(self, cardSize=BingoGlobals.CARD_SIZE, rowSize=BingoGlobals.CARD_ROWS, colSize=BingoGlobals.CARD_COLS):
        BingoCardBase.BingoCardBase.__init__(self, cardSize, rowSize, colSize)
        self.gameType = BingoGlobals.NORMAL_CARD

    def checkForWin(self, id):
        rowId = int(id / BingoGlobals.CARD_ROWS)
        colId = id % BingoGlobals.CARD_COLS
        rowResult = self.rowCheck(rowId)
        colResult = self.colCheck(colId)
        fDiagResult = self.fDiagCheck(id)
        bDiagResult = self.bDiagCheck(id)
        if rowResult or colResult or fDiagResult or bDiagResult:
            return BingoGlobals.WIN
        return BingoGlobals.NO_UPDATE

    def checkForColor(self, id):
        return 1

    def checkForBingo(self):
        id = self.cardSize / 2
        if self.checkForWin(id):
            return BingoGlobals.WIN
        for i in xrange(BingoGlobals.CARD_ROWS):
            if i != BingoGlobals.CARD_ROWS / 2:
                rowResult = self.rowCheck(i)
                colResult = self.colCheck(i)
                if rowResult | colResult:
                    return BingoGlobals.WIN

        return BingoGlobals.NO_UPDATE