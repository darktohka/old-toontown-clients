# File: F (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from toontown.fishing import BingoGlobals
from toontown.fishing import BingoCardBase

class FourCornerBingo(BingoCardBase.BingoCardBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('FourCornerBingo')
    corners = [
        0,
        BingoGlobals.CARD_ROWS - 1,
        BingoGlobals.CARD_COLS * (BingoGlobals.CARD_ROWS - 1),
        BingoGlobals.CARD_COLS * BingoGlobals.CARD_ROWS - 1]
    
    def __init__(self, cardSize = BingoGlobals.CARD_SIZE, rowSize = BingoGlobals.CARD_ROWS, colSize = BingoGlobals.CARD_COLS):
        BingoCardBase.BingoCardBase.__init__(self, cardSize, rowSize, colSize)
        self.gameType = BingoGlobals.FOURCORNER_CARD
        self.topLeft = 0
        self.topRight = 0
        self.bottomLeft = 0
        self.bottomRight = 0

    
    def checkForWin(self, id):
        if id == self.corners[0] and self.cellCheck(id):
            self.topLeft = 1
        elif id == self.corners[1] and self.cellCheck(id):
            self.topRight = 1
        elif id == self.corners[2] and self.cellCheck(id):
            self.bottomLeft = 1
        elif id == self.corners[3] and self.cellCheck(id):
            self.bottomRight = 1
        
        if self.topLeft and self.topRight and self.bottomLeft and self.bottomRight:
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
        
        if not topLeft and topRight and bottomLeft:
            pass
        return bottomRight

    
    def checkForBingo(self):
        result = BingoGlobals.NO_UPDATE
        for id in self.corners:
            result = self.checkForWin(id)
        
        return result


