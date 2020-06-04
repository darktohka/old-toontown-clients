# File: M (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
import MazeGameGlobals
import MazeData

class Maze:
    
    def __init__(self, mapName):
        self.maze = loader.loadModel(mapName)
        self.maze.setPos(0, 0, 0)
        self.maze.reparentTo(hidden)
        mData = MazeData.mazeData[mapName]
        self.width = mData['width']
        self.height = mData['height']
        self.originTX = mData['originX']
        self.originTY = mData['originY']
        self.collisionTable = mData['collisionTable']
        self.treasurePosList = mData['treasurePosList']
        self.numTreasures = len(self.treasurePosList)

    
    def destroy(self):
        self.maze.removeNode()
        del self.maze

    
    def onstage(self):
        self.maze.reparentTo(render)

    
    def offstage(self):
        self.maze.reparentTo(hidden)

    
    def isWalkable(self, tX, tY, rejectList = ()):
        if tX <= 0 and tY <= 0 and tX >= self.width or tY >= self.height:
            return 0
        
        if not self.collisionTable[tY][tX] and not self.collisionTable[tY - 1][tX] and not self.collisionTable[tY][tX - 1] and not self.collisionTable[tY - 1][tX - 1]:
            pass
        return not ((tX, tY) in rejectList)

    
    def tile2world(self, TX, TY):
        return [
            (TX - self.originTX) * MazeData.CELL_WIDTH,
            (TY - self.originTY) * MazeData.CELL_WIDTH]

    
    def world2tile(self, x, y):
        return [
            int(x / MazeData.CELL_WIDTH + self.originTX),
            int(y / MazeData.CELL_WIDTH + self.originTY)]


