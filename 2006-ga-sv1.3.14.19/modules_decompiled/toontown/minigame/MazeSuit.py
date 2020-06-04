# File: M (Python 2.2)

from direct.showbase.PandaObject import *
from toontown.toonbase.ToontownGlobals import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
import Maze
import MazeData
import MazeGameGlobals
from direct.showbase import RandomNumGen
from toontown.suit import Suit
from toontown.suit import SuitDNA

class MazeSuit(PandaObject):
    COLL_SPHERE_NAME = 'MazeSuitSphere'
    COLLISION_EVENT_NAME = 'MazeSuitCollision'
    MOVE_IVAL_NAME = 'moveMazeSuit'
    DIR_UP = 0
    DIR_DOWN = 1
    DIR_LEFT = 2
    DIR_RIGHT = 3
    oppositeDirections = [
        DIR_DOWN,
        DIR_UP,
        DIR_RIGHT,
        DIR_LEFT]
    directionHs = [
        0,
        180,
        90,
        270]
    DEFAULT_SPEED = 4.0
    SUIT_Z = 0.10000000000000001
    
    def __init__(self, serialNum, maze, randomNumGen, cellWalkPeriod, difficulty):
        self.serialNum = serialNum
        self.maze = maze
        self.rng = RandomNumGen.RandomNumGen(randomNumGen)
        self.difficulty = difficulty
        self.suit = Suit.Suit()
        d = SuitDNA.SuitDNA()
        d.newSuit('f')
        self.suit.setDNA(d)
        self.ticPeriod = int(cellWalkPeriod)
        self.cellWalkDuration = float(self.ticPeriod) / float(MazeGameGlobals.SUIT_TIC_FREQ)
        self.turnDuration = 0.59999999999999998 * self.cellWalkDuration

    
    def destroy(self):
        self.suit.delete()

    
    def uniqueName(self, str):
        return str + `self.serialNum`

    
    def gameStart(self, gameStartTime):
        self.gameStartTime = gameStartTime
        self.initCollisions()
        self.startWalkAnim()
        self.occupiedTiles = [
            (self.nextTX, self.nextTY)]
        n = 20
        self.nextThinkTic = self.serialNum * MazeGameGlobals.SUIT_TIC_FREQ / n
        self.fromPos = Point3(0, 0, 0)
        self.toPos = Point3(0, 0, 0)
        self.fromHpr = Point3(0, 0, 0)
        self.toHpr = Point3(0, 0, 0)
        self.moveIval = WaitInterval(1.0)

    
    def gameEnd(self):
        self.moveIval.pause()
        del self.moveIval
        self.shutdownCollisions()
        self.suit.loop('neutral')

    
    def initCollisions(self):
        self.collSphere = CollisionSphere(0, 0, 0, 2.0)
        self.collSphere.setTangible(0)
        self.collNode = CollisionNode(self.uniqueName(self.COLL_SPHERE_NAME))
        self.collNode.setIntoCollideMask(WallBitmask)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.suit.attachNewNode(self.collNode)
        self.collNodePath.hide()
        self.accept(self.uniqueName('enter' + self.COLL_SPHERE_NAME), self.handleEnterSphere)

    
    def shutdownCollisions(self):
        self.ignore(self.uniqueName('enter' + self.COLL_SPHERE_NAME))
        del self.collSphere
        self.collNodePath.removeNode()
        del self.collNodePath
        del self.collNode

    
    def handleEnterSphere(self, collEntry):
        messenger.send(self.COLLISION_EVENT_NAME, [
            self.serialNum])

    
    def _MazeSuit__getWorldPos(self, sTX, sTY):
        (wx, wy) = self.maze.tile2world(sTX, sTY)
        return Point3(wx, wy, self.SUIT_Z)

    
    def onstage(self):
        startPositions = [
            [
                0.25,
                0.25],
            [
                0.75,
                0.75],
            [
                0.25,
                0.75],
            [
                0.75,
                0.25],
            [
                0.20000000000000001,
                0.5],
            [
                0.80000000000000004,
                0.5],
            [
                0.5,
                0.20000000000000001],
            [
                0.5,
                0.80000000000000004],
            [
                0.33000000000000002,
                0.0],
            [
                0.66000000000000003,
                0.0],
            [
                0.33000000000000002,
                1.0],
            [
                0.66000000000000003,
                1.0],
            [
                0.0,
                0.33000000000000002],
            [
                0.0,
                0.66000000000000003],
            [
                1.0,
                0.33000000000000002],
            [
                1.0,
                0.66000000000000003]]
        sTX = int(self.maze.width * startPositions[self.serialNum][0])
        sTY = int(self.maze.height * startPositions[self.serialNum][1])
        c = 0
        lim = 0
        toggle = 0
        direction = 0
        while not self.maze.isWalkable(sTX, sTY):
            if 0 == direction:
                sTX -= 1
            elif 1 == direction:
                sTY -= 1
            elif 2 == direction:
                sTX += 1
            elif 3 == direction:
                sTY += 1
            
            c += 1
            if c > lim:
                c = 0
                direction = (direction + 1) % 4
                toggle += 1
                if not (toggle & 1):
                    lim += 1
                
            
        self.TX = sTX
        self.TY = sTY
        self.direction = self.DIR_DOWN
        self.lastDirection = self.direction
        self.nextTX = self.TX
        self.nextTY = self.TY
        self.suit.reparentTo(render)
        self.suit.setPos(self._MazeSuit__getWorldPos(self.TX, self.TY))
        self.suit.setHpr(self.directionHs[self.direction], 0, 0)
        self.suit.pose('walk', 0)
        self.suit.loop('neutral')

    
    def offstage(self):
        self.suit.reparentTo(hidden)

    
    def startWalkAnim(self):
        self.suit.loop('walk')
        speed = float(MazeData.CELL_WIDTH) / self.cellWalkDuration
        self.suit.setPlayRate(speed / self.DEFAULT_SPEED, 'walk')

    
    def _MazeSuit__applyDirection(self, dir, TX, TY):
        if self.DIR_UP == dir:
            TY += 1
        elif self.DIR_DOWN == dir:
            TY -= 1
        elif self.DIR_LEFT == dir:
            TX -= 1
        elif self.DIR_RIGHT == dir:
            TX += 1
        
        return (TX, TY)

    
    def _MazeSuit__chooseNewWalkDirection(self, unwalkables):
        if not self.rng.randrange(4):
            (newTX, newTY) = self._MazeSuit__applyDirection(self.direction, self.TX, self.TY)
            if self.maze.isWalkable(newTX, newTY, unwalkables):
                return self.direction
            
        
        if self.difficulty >= 0.5:
            if not self.rng.randrange(30):
                oppositeDir = self.oppositeDirections[self.direction]
                (newTX, newTY) = self._MazeSuit__applyDirection(oppositeDir, self.TX, self.TY)
                if self.maze.isWalkable(newTX, newTY, unwalkables):
                    return oppositeDir
                
            
        
        candidateDirs = [
            self.DIR_UP,
            self.DIR_DOWN,
            self.DIR_LEFT,
            self.DIR_RIGHT]
        candidateDirs.remove(self.oppositeDirections[self.direction])
        while len(candidateDirs):
            dir = self.rng.choice(candidateDirs)
            (newTX, newTY) = self._MazeSuit__applyDirection(dir, self.TX, self.TY)
            if self.maze.isWalkable(newTX, newTY, unwalkables):
                return dir
            
            candidateDirs.remove(dir)
        return self.oppositeDirections[self.direction]

    
    def getThinkTimestampTics(self, curTic):
        if curTic < self.nextThinkTic:
            return []
        else:
            r = range(self.nextThinkTic, curTic + 1, self.ticPeriod)
            self.lastTicBeforeRender = r[-1]
            return r

    
    def prepareToThink(self):
        self.occupiedTiles = [
            (self.nextTX, self.nextTY)]

    
    def think(self, curTic, curT, unwalkables):
        self.TX = self.nextTX
        self.TY = self.nextTY
        self.lastDirection = self.direction
        self.direction = self._MazeSuit__chooseNewWalkDirection(unwalkables)
        (self.nextTX, self.nextTY) = self._MazeSuit__applyDirection(self.direction, self.TX, self.TY)
        self.occupiedTiles = [
            (self.TX, self.TY),
            (self.nextTX, self.nextTY)]
        if curTic == self.lastTicBeforeRender:
            fromCoords = self.maze.tile2world(self.TX, self.TY)
            toCoords = self.maze.tile2world(self.nextTX, self.nextTY)
            self.fromPos.set(fromCoords[0], fromCoords[1], self.SUIT_Z)
            self.toPos.set(toCoords[0], toCoords[1], self.SUIT_Z)
            self.moveIval = LerpPosInterval(self.suit, self.cellWalkDuration, self.toPos, startPos = self.fromPos, name = self.uniqueName(self.MOVE_IVAL_NAME))
            if self.direction != self.lastDirection:
                self.fromH = self.directionHs[self.lastDirection]
                toH = self.directionHs[self.direction]
                if self.fromH == 270 and toH == 0:
                    self.fromH = -90
                elif self.fromH == 0 and toH == 270:
                    self.fromH = 360
                
                self.fromHpr.set(self.fromH, 0, 0)
                self.toHpr.set(toH, 0, 0)
                turnIval = LerpHprInterval(self.suit, self.turnDuration, self.toHpr, startHpr = self.fromHpr, name = self.uniqueName('turnMazeSuit'))
                self.moveIval = Parallel(self.moveIval, turnIval, name = self.uniqueName(self.MOVE_IVAL_NAME))
            else:
                self.suit.setH(self.directionHs[self.direction])
            moveStartT = float(self.nextThinkTic) / float(MazeGameGlobals.SUIT_TIC_FREQ)
            self.moveIval.start(curT - moveStartT + self.gameStartTime)
        
        self.nextThinkTic += self.ticPeriod


