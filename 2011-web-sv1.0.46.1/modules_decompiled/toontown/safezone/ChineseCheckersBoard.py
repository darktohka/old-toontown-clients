# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\ChineseCheckersBoard.py


class ChineseCheckersBoard:
    __module__ = __name__

    def __init__(self):
        self.squareList = []
        for x in range(121):
            self.squareList.append(CheckersSquare(x))

        self.squareList[0].setAdjacent([None, 1, 2, None, None, None])
        self.squareList[1].setAdjacent([None, 3, 4, 2, 0, None])
        self.squareList[2].setAdjacent([1, 4, 5, None, None, 0])
        self.squareList[3].setAdjacent([None, 6, 7, 4, 1, None])
        self.squareList[4].setAdjacent([3, 7, 8, 5, 2, 1])
        self.squareList[5].setAdjacent([4, 8, 9, None, None, 2])
        self.squareList[6].setAdjacent([None, 14, 15, 7, 3, None])
        self.squareList[7].setAdjacent([6, 15, 16, 8, 4, 3])
        self.squareList[8].setAdjacent([7, 16, 17, 9, 5, 4])
        self.squareList[9].setAdjacent([8, 17, 18, None, None, 5])
        self.squareList[10].setAdjacent([None, None, 23, 11, None, None])
        self.squareList[11].setAdjacent([10, 23, 24, 12, None, None])
        self.squareList[12].setAdjacent([11, 24, 25, 13, None, None])
        self.squareList[13].setAdjacent([12, 25, 26, 14, None, None])
        self.squareList[14].setAdjacent([13, 26, 27, 15, 6, None])
        self.squareList[15].setAdjacent([14, 27, 28, 16, 7, 6])
        self.squareList[16].setAdjacent([15, 28, 29, 17, 8, 7])
        self.squareList[17].setAdjacent([16, 29, 30, 18, 9, 8])
        self.squareList[18].setAdjacent([17, 30, 31, 19, None, 9])
        (self.squareList[19].setAdjacent([18, 31, 32, 20, None, None]),)
        self.squareList[20].setAdjacent([19, 32, 33, 21, None, None])
        self.squareList[21].setAdjacent([20, 33, 34, 22, None, None])
        self.squareList[22].setAdjacent([21, 34, None, None, None, None])
        self.squareList[23].setAdjacent([None, None, 35, 24, 11, 10])
        self.squareList[24].setAdjacent([23, 35, 36, 25, 12, 11])
        self.squareList[25].setAdjacent([24, 36, 37, 26, 13, 12])
        self.squareList[26].setAdjacent([25, 37, 38, 27, 14, 13])
        self.squareList[27].setAdjacent([26, 38, 39, 28, 15, 14])
        self.squareList[28].setAdjacent([27, 39, 40, 29, 16, 15])
        self.squareList[29].setAdjacent([28, 40, 41, 30, 17, 16])
        self.squareList[30].setAdjacent([29, 41, 42, 31, 18, 17])
        self.squareList[31].setAdjacent([30, 42, 43, 32, 19, 18])
        self.squareList[32].setAdjacent([31, 43, 44, 33, 20, 19])
        self.squareList[33].setAdjacent([32, 44, 45, 34, 21, 20])
        self.squareList[34].setAdjacent([33, 45, None, None, 22, 21])
        self.squareList[35].setAdjacent([None, None, 46, 36, 24, 23])
        self.squareList[36].setAdjacent([35, 46, 47, 37, 25, 24])
        self.squareList[37].setAdjacent([36, 47, 48, 38, 26, 25])
        self.squareList[38].setAdjacent([37, 48, 49, 39, 27, 26])
        self.squareList[39].setAdjacent([38, 49, 50, 40, 28, 27])
        self.squareList[40].setAdjacent([39, 50, 51, 41, 29, 28])
        self.squareList[41].setAdjacent([40, 51, 52, 42, 30, 29])
        self.squareList[42].setAdjacent([41, 52, 53, 43, 31, 30])
        self.squareList[43].setAdjacent([42, 53, 54, 44, 32, 31])
        self.squareList[44].setAdjacent([43, 54, 55, 45, 33, 32])
        self.squareList[45].setAdjacent([44, 55, None, None, 34, 33])
        self.squareList[46].setAdjacent([None, None, 56, 47, 36, 35])
        self.squareList[47].setAdjacent([46, 56, 57, 48, 37, 36])
        self.squareList[48].setAdjacent([47, 57, 58, 49, 38, 37])
        self.squareList[49].setAdjacent([48, 58, 59, 50, 39, 38])
        self.squareList[50].setAdjacent([49, 59, 60, 51, 40, 39])
        self.squareList[51].setAdjacent([50, 60, 61, 52, 41, 40])
        self.squareList[52].setAdjacent([51, 61, 62, 53, 42, 41])
        self.squareList[53].setAdjacent([52, 62, 63, 54, 43, 42])
        self.squareList[54].setAdjacent([53, 63, 64, 55, 44, 43])
        self.squareList[55].setAdjacent([54, 64, None, None, 45, 44])
        self.squareList[56].setAdjacent([None, 65, 66, 57, 47, 46])
        self.squareList[57].setAdjacent([56, 66, 67, 58, 48, 47])
        self.squareList[58].setAdjacent([57, 67, 68, 59, 49, 48])
        self.squareList[59].setAdjacent([58, 68, 69, 60, 50, 49])
        self.squareList[60].setAdjacent([59, 69, 70, 61, 51, 50])
        self.squareList[61].setAdjacent([60, 70, 71, 62, 52, 51])
        self.squareList[62].setAdjacent([61, 71, 72, 63, 53, 52])
        self.squareList[63].setAdjacent([62, 72, 73, 64, 54, 53])
        self.squareList[64].setAdjacent([63, 73, 74, None, 55, 54])
        self.squareList[65].setAdjacent([None, 75, 76, 66, 56, None])
        self.squareList[66].setAdjacent([65, 76, 77, 67, 57, 56])
        self.squareList[67].setAdjacent([66, 77, 78, 68, 58, 57])
        self.squareList[68].setAdjacent([67, 78, 79, 69, 59, 58])
        self.squareList[69].setAdjacent([68, 79, 80, 70, 60, 61])
        self.squareList[70].setAdjacent([69, 80, 81, 71, 61, 60])
        self.squareList[71].setAdjacent([70, 81, 82, 72, 62, 61])
        self.squareList[72].setAdjacent([71, 82, 83, 73, 63, 62])
        self.squareList[73].setAdjacent([72, 83, 84, 74, 64, 63])
        self.squareList[74].setAdjacent([73, 84, 85, None, None, 64])
        self.squareList[75].setAdjacent([None, 86, 87, 76, 65, None])
        self.squareList[76].setAdjacent([75, 87, 88, 77, 66, 65])
        self.squareList[77].setAdjacent([76, 88, 89, 78, 67, 66])
        self.squareList[78].setAdjacent([77, 89, 90, 79, 68, 67])
        self.squareList[79].setAdjacent([78, 90, 91, 80, 69, 68])
        self.squareList[80].setAdjacent([79, 91, 92, 81, 70, 69])
        self.squareList[81].setAdjacent([80, 92, 93, 82, 71, 70])
        self.squareList[82].setAdjacent([81, 93, 94, 83, 72, 71])
        self.squareList[83].setAdjacent([82, 94, 95, 84, 73, 72])
        self.squareList[84].setAdjacent([83, 95, 96, 85, 74, 73])
        self.squareList[85].setAdjacent([84, 96, 97, None, None, 74])
        self.squareList[86].setAdjacent([None, 98, 99, 87, 75, None])
        self.squareList[87].setAdjacent([86, 99, 100, 88, 76, 75])
        self.squareList[88].setAdjacent([87, 100, 101, 89, 77, 76])
        self.squareList[89].setAdjacent([88, 101, 102, 90, 78, 77])
        self.squareList[90].setAdjacent([89, 102, 103, 91, 79, 78])
        self.squareList[91].setAdjacent([90, 103, 104, 92, 80, 79])
        self.squareList[92].setAdjacent([91, 104, 105, 93, 81, 80])
        self.squareList[93].setAdjacent([92, 105, 106, 94, 82, 81])
        self.squareList[94].setAdjacent([93, 106, 107, 95, 83, 82])
        self.squareList[95].setAdjacent([94, 107, 108, 96, 84, 83])
        self.squareList[96].setAdjacent([95, 108, 109, 97, 85, 84])
        self.squareList[97].setAdjacent([96, 109, 110, None, None, 85])
        self.squareList[98].setAdjacent([None, None, None, 99, 86, None])
        self.squareList[99].setAdjacent([98, None, None, 100, 87, 86])
        self.squareList[100].setAdjacent([99, None, None, 101, 88, 87])
        self.squareList[101].setAdjacent([100, None, None, 102, 89, 88])
        self.squareList[102].setAdjacent([101, None, 111, 103, 90, 89])
        self.squareList[103].setAdjacent([102, 111, 112, 104, 91, 90])
        self.squareList[104].setAdjacent([103, 112, 113, 105, 92, 91])
        self.squareList[105].setAdjacent([104, 113, 114, 106, 93, 92])
        self.squareList[106].setAdjacent([105, 114, None, 107, 94, 93])
        self.squareList[107].setAdjacent([106, None, None, 108, 95, 94])
        self.squareList[108].setAdjacent([107, None, None, 109, 96, 95])
        self.squareList[109].setAdjacent([108, None, None, 110, 97, 96])
        self.squareList[110].setAdjacent([109, None, None, None, None, 97])
        self.squareList[111].setAdjacent([None, None, 115, 112, 103, 102])
        self.squareList[112].setAdjacent([111, 115, 116, 113, 104, 103])
        self.squareList[113].setAdjacent([112, 116, 117, 114, 105, 104])
        self.squareList[114].setAdjacent([113, 117, None, None, 106, 105])
        self.squareList[115].setAdjacent([None, None, 118, 116, 112, 111])
        self.squareList[116].setAdjacent([115, 118, 119, 117, 113, 112])
        self.squareList[117].setAdjacent([116, 119, None, None, 114, 113])
        self.squareList[118].setAdjacent([None, None, 120, 119, 116, 115])
        self.squareList[119].setAdjacent([118, 120, None, None, 117, 116])
        self.squareList[120].setAdjacent([None, None, None, None, 119, 118])
        return

    def delete(self):
        for x in self.squareList:
            x.delete()

        del self.squareList

    def getSquare(self, arrayLoc):
        return self.squareList[arrayLoc]

    def getSquareOffset(self, arrayLoc):
        return self.squareList[(arrayLoc - 1)]

    def getState(self, squareNum):
        return self.squareList[squareNum].getState()

    def getStateOffset(self, arrayLoc):
        return self.squareList[(squareNum - 1)].getState()

    def setState(self, squareNum, newState):
        self.squareList[squareNum].setState(newState)

    def setStateOffset(self, squareNum, newState):
        self.squareList[(squareNum - 1)].setState(newState)

    def getAdjacent(self, squareNum):
        return self.squareList[squareNum].adjacent

    def getAdjacentOffset(self, squareNum):
        return self.squareList[(squareNum - 1)].adjacent

    def getStates(self):
        retList = []
        for x in range(121):
            retList.append(self.squareList[x].getState())

        return retList

    def setStates(self, squares):
        y = 0
        for x in range(121):
            self.squareList[x].setState(squares[x])


class CheckersSquare:
    __module__ = __name__

    def __init__(self, tileNu):
        self.tileNum = tileNu
        self.state = 0
        self.adjacent = []

    def delete(self):
        del self.tileNum
        del self.state
        del self.adjacent

    def setAdjacent(self, adjList):
        for x in adjList:
            self.adjacent.append(x)

    def getAdjacent(self):
        return self.adjacent

    def setState(self, newState):
        self.state = newState

    def getState(self):
        return self.state

    def getNum(self):
        return self.tileNum