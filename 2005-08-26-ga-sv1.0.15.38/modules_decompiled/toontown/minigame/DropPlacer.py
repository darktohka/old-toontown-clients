# File: D (Python 2.2)

import CatchGameGlobals
import DropScheduler

class DropPlacer:
    
    def __init__(self, game, dropTypes):
        self.game = game
        self.dropTypes = dropTypes
        self.dtIndex = 0
        self.scheduler = DropScheduler.DropScheduler(CatchGameGlobals.GameDuration, self.game.FirstDropDelay, self.game.DropPeriod, self.game.MaxDropDuration, self.game.FasterDropDelay, self.game.FasterDropPeriodMult)

    
    def doneDropping(self):
        return self.scheduler.doneDropping()

    
    def getT(self):
        return self.scheduler.getT()

    
    def stepT(self):
        self.scheduler.stepT()

    
    def getNextDropTypeName(self):
        if self.dtIndex >= len(self.dropTypes):
            self.game.notify.debug('warning: defaulting to anvil')
            typeName = 'anvil'
        else:
            typeName = self.dropTypes[self.dtIndex]
        self.dtIndex += 1
        return typeName

    
    def getRandomColRow(self):
        col = self.game.randomNumGen.randrange(0, self.game.DropColumns)
        row = self.game.randomNumGen.randrange(0, self.game.DropRows)
        return [
            col,
            row]

    
    def getNextDrop(self):
        raise RuntimeError, 'DropPlacer.getNextDrop should never be called'



class RandomDropPlacer(DropPlacer):
    
    def __init__(self, game, dropTypes):
        DropPlacer.__init__(self, game, dropTypes)

    
    def getNextDrop(self):
        (col, row) = self.getRandomColRow()
        drop = [
            self.getT(),
            self.getNextDropTypeName(),
            [
                col,
                row]]
        self.stepT()
        return drop



class RegionDropPlacer(DropPlacer):
    
    def __init__(self, game, dropTypes):
        DropPlacer.__init__(self, game, dropTypes)
        BaseDropRegionTable = [
            [
                1,
                1,
                2,
                3,
                3],
            [
                1,
                1,
                2,
                3,
                3],
            [
                0,
                1,
                2,
                3,
                4],
            [
                0,
                1,
                2,
                3,
                4],
            [
                0,
                1,
                2,
                3,
                4]]
        DropRegionTables = [
            BaseDropRegionTable,
            BaseDropRegionTable,
            [
                [
                    1,
                    2,
                    2,
                    3,
                    3,
                    4],
                [
                    1,
                    1,
                    2,
                    3,
                    4,
                    4],
                [
                    1,
                    1,
                    2,
                    3,
                    4,
                    4],
                [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5],
                [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5],
                [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5]],
            [
                [
                    1,
                    1,
                    2,
                    2,
                    2,
                    3,
                    3],
                [
                    1,
                    1,
                    2,
                    2,
                    2,
                    3,
                    3],
                [
                    0,
                    1,
                    2,
                    2,
                    2,
                    3,
                    4],
                [
                    0,
                    1,
                    2,
                    2,
                    2,
                    3,
                    4],
                [
                    0,
                    1,
                    2,
                    2,
                    2,
                    3,
                    4],
                [
                    0,
                    1,
                    2,
                    2,
                    2,
                    3,
                    4],
                [
                    0,
                    1,
                    2,
                    2,
                    2,
                    3,
                    4]]]
        self.DropRegionTable = DropRegionTables[self.game.getNumPlayers() - 1]
        self.DropRegion2GridCoordList = { }
        for row in range(len(self.DropRegionTable)):
            rowList = self.DropRegionTable[row]
            for column in range(len(rowList)):
                region = rowList[column]
                if not self.DropRegion2GridCoordList.has_key(region):
                    self.DropRegion2GridCoordList[region] = []
                
                self.DropRegion2GridCoordList[region].append([
                    row,
                    column])
            
        
        self.DropRegions = self.DropRegion2GridCoordList.keys()
        self.DropRegions.sort()
        self.emptyDropRegions = self.DropRegions[:]
        self.fallingObjs = []

    
    def getNextDrop(self):
        t = self.getT()
        while len(self.fallingObjs):
            (landTime, dropRegion) = self.fallingObjs[0]
            if landTime > t:
                break
            
            self.fallingObjs = self.fallingObjs[1:]
            if dropRegion not in self.emptyDropRegions:
                self.emptyDropRegions.append(dropRegion)
            
        candidates = self.emptyDropRegions
        if len(candidates) == 0:
            candidates = self.DropRegions
        
        dropRegion = self.game.randomNumGen.choice(candidates)
        (row, col) = self.game.randomNumGen.choice(self.DropRegion2GridCoordList[dropRegion])
        dropTypeName = self.getNextDropTypeName()
        drop = [
            t,
            dropTypeName,
            [
                row,
                col]]
        duration = self.game.BaselineDropDuration
        self.fallingObjs.append([
            t + duration,
            dropRegion])
        if dropRegion in self.emptyDropRegions:
            self.emptyDropRegions.remove(dropRegion)
        
        self.stepT()
        return drop



class PathDropPlacer(DropPlacer):
    
    def __init__(self, game, dropTypes):
        DropPlacer.__init__(self, game, dropTypes)
        self.moves = [
            [
                0,
                -1],
            [
                1,
                -1],
            [
                1,
                0],
            [
                1,
                1],
            [
                0,
                1],
            [
                -1,
                1],
            [
                -1,
                0],
            [
                -1,
                -1]]
        self.paths = []
        for i in xrange(self.game.getNumPlayers()):
            dir = self.game.randomNumGen.randrange(0, len(self.moves))
            (col, row) = self.getRandomColRow()
            path = {
                'direction': dir,
                'location': [
                    col,
                    row] }
            self.paths.append(path)
        
        self.curPathIndex = 0

    
    def getValidDirection(self, col, row, dir):
        redirectTop = [
            (6, 2),
            2,
            2,
            3,
            4,
            5,
            6,
            6]
        redirectRight = [
            0,
            0,
            (0, 4),
            4,
            4,
            5,
            6,
            7]
        redirectBottom = [
            0,
            1,
            2,
            2,
            (2, 6),
            6,
            6,
            7]
        redirectLeft = [
            0,
            1,
            2,
            3,
            4,
            4,
            (4, 0),
            0]
        redirectTopRight = [
            6,
            (6, 4),
            4,
            4,
            4,
            5,
            6,
            6]
        redirectBottomRight = [
            0,
            0,
            0,
            (0, 6),
            6,
            6,
            6,
            7]
        redirectBottomLeft = [
            0,
            1,
            2,
            2,
            2,
            (2, 0),
            0,
            0]
        redirectTopLeft = [
            2,
            2,
            2,
            3,
            4,
            4,
            4,
            (4, 2)]
        tables = [
            None,
            redirectTop,
            redirectBottom,
            None,
            redirectLeft,
            redirectTopLeft,
            redirectBottomLeft,
            None,
            redirectRight,
            redirectTopRight,
            redirectBottomRight]
        if col == 0:
            colIndex = 1
        elif col == self.game.DropColumns - 1:
            colIndex = 2
        else:
            colIndex = 0
        if row == 0:
            rowIndex = 1
        elif row == self.game.DropRows - 1:
            rowIndex = 2
        else:
            rowIndex = 0
        index = (colIndex << 2) + rowIndex
        redirectTable = tables[index]
        if not redirectTable:
            return dir
        
        newDir = redirectTable[dir]
        if type(newDir) != type(1):
            newDir = self.game.randomNumGen.choice(newDir)
        
        return newDir

    
    def getNextDrop(self):
        path = self.paths[self.curPathIndex]
        (col, row) = path['location']
        dir = path['direction']
        turns = [
            -1,
            0,
            0,
            1]
        turn = self.game.randomNumGen.choice(turns)
        if turn:
            dir = (dir + turn) % len(self.moves)
        
        dir = self.getValidDirection(col, row, dir)
        (dCol, dRow) = self.moves[dir]
        col += dCol
        row += dRow
        col = min(max(col, 0), self.game.DropColumns - 1)
        row = min(max(row, 0), self.game.DropRows - 1)
        path['location'] = [
            col,
            row]
        path['direction'] = dir
        self.curPathIndex = (self.curPathIndex + 1) % len(self.paths)
        drop = [
            self.getT(),
            self.getNextDropTypeName(),
            [
                col,
                row]]
        self.stepT()
        return drop


