# File: M (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.showbase.PythonUtil import invertDictLossless
from toontown.coghq import MintRoomSpecs
from toontown.toonbase import ToontownGlobals
from direct.showbase.PythonUtil import normalDistrib, lerp
import random

def printAllCashbotInfo():
    print 'roomId: roomName'
    for (roomId, roomName) in MintRoomSpecs.CashbotMintRoomId2RoomName.items():
        print '%s: %s' % (roomId, roomName)
    
    print '\nroomId: numBattles'
    for (roomId, numBattles) in MintRoomSpecs.roomId2numBattles.items():
        print '%s: %s' % (roomId, numBattles)
    
    print '\nmintId floor roomIds'
    printMintRoomIds()
    print '\nmintId floor numRooms'
    printNumRooms()
    print '\nmintId floor numBattles'
    printNumBattles()


def iterateCashbotMints(func):
    ToontownGlobals = ToontownGlobals
    import toontown.toonbase
    for mintId in [
        ToontownGlobals.CashbotMintIntA,
        ToontownGlobals.CashbotMintIntB,
        ToontownGlobals.CashbotMintIntC]:
        for floorNum in xrange(ToontownGlobals.MintNumFloors[mintId]):
            func(MintLayout(mintId, floorNum))
        
    


def printMintInfo():
    
    def func(ml):
        print ml

    iterateCashbotMints(func)


def printMintRoomIds():
    
    def func(ml):
        print ml.getMintId(), ml.getFloorNum(), ml.getRoomIds()

    iterateCashbotMints(func)


def printMintRoomNames():
    
    def func(ml):
        print ml.getMintId(), ml.getFloorNum(), ml.getRoomNames()

    iterateCashbotMints(func)


def printNumRooms():
    
    def func(ml):
        print ml.getMintId(), ml.getFloorNum(), ml.getNumRooms()

    iterateCashbotMints(func)


def printNumBattles():
    
    def func(ml):
        print ml.getMintId(), ml.getFloorNum(), ml.getNumBattles()

    iterateCashbotMints(func)


class MintLayout:
    notify = DirectNotifyGlobal.directNotify.newCategory('MintLayout')
    
    def __init__(self, mintId, floorNum):
        self.mintId = mintId
        self.floorNum = floorNum
        self.roomIds = []
        self.hallways = []
        self.numRooms = 1 + ToontownGlobals.MintNumRooms[self.mintId][self.floorNum]
        self.numHallways = self.numRooms - 1
        rng = self.getRng()
        startingRoomNames = MintRoomSpecs.CashbotMintEntrances
        middleRoomNames = MintRoomSpecs.CashbotMintMiddleRooms
        finalRoomNames = MintRoomSpecs.CashbotMintFinalRooms
        numBattlesLeft = ToontownGlobals.MintNumBattles[mintId]
        
        def getRoomId(roomName):
            return MintRoomSpecs.CashbotMintRoomName2RoomId[roomName]

        
        def getRoomName(roomId):
            return MintRoomSpecs.CashbotMintRoomId2RoomName[roomId]

        finalRoomId = getRoomId(rng.choice(finalRoomNames))
        numBattlesLeft -= MintRoomSpecs.getNumBattles(finalRoomId)
        middleRoomIds = []
        middleRoomsLeft = self.numRooms - 2
        numBattles2middleRoomIds = invertDictLossless(MintRoomSpecs.middleRoomId2numBattles)
        allBattleRooms = []
        for (num, roomIds) in numBattles2middleRoomIds.items():
            if num > 0:
                allBattleRooms.extend(roomIds)
            
        
        
        def chooseBattleRooms(numBattlesLeft, allBattleRoomIds, baseIndex = 0, chosenBattleRooms = []):
            while baseIndex < len(allBattleRoomIds):
                nextRoomId = allBattleRoomIds[baseIndex]
                baseIndex += 1
                newNumBattlesLeft = numBattlesLeft - MintRoomSpecs.middleRoomId2numBattles[nextRoomId]
                if newNumBattlesLeft < 0:
                    continue
                elif newNumBattlesLeft == 0:
                    chosenBattleRooms.append(nextRoomId)
                    return chosenBattleRooms
                
                chosenBattleRooms.append(nextRoomId)
                result = chooseBattleRooms(newNumBattlesLeft, allBattleRoomIds, baseIndex, chosenBattleRooms)
                if result is not None:
                    return result
                else:
                    del chosenBattleRooms[-1:]
            return None

        while 1:
            allBattleRoomIds = list(allBattleRooms)
            rng.shuffle(allBattleRoomIds)
            battleRoomIds = chooseBattleRooms(numBattlesLeft, allBattleRoomIds)
            if battleRoomIds is not None:
                break
            
            MintLayout.notify.info('could not find a valid set of battle rooms, trying again')
        middleRoomIds.extend(battleRoomIds)
        middleRoomsLeft -= len(battleRoomIds)
        if middleRoomsLeft > 0:
            actionRoomIds = numBattles2middleRoomIds[0]
            for i in xrange(middleRoomsLeft):
                roomId = rng.choice(actionRoomIds)
                actionRoomIds.remove(roomId)
                middleRoomIds.append(roomId)
            
        
        self.roomIds.append(getRoomId(rng.choice(startingRoomNames)))
        rng.shuffle(middleRoomIds)
        self.roomIds.extend(middleRoomIds)
        self.roomIds.append(finalRoomId)
        connectorRoomNames = MintRoomSpecs.CashbotMintConnectorRooms
        for i in xrange(self.numHallways):
            self.hallways.append(rng.choice(connectorRoomNames))
        

    
    def getNumRooms(self):
        return len(self.roomIds)

    
    def getRoomId(self, n):
        return self.roomIds[n]

    
    def getRoomIds(self):
        return self.roomIds[:]

    
    def getRoomNames(self):
        names = []
        for roomId in self.roomIds:
            names.append(MintRoomSpecs.CashbotMintRoomId2RoomName[roomId])
        
        return names

    
    def getNumHallways(self):
        return len(self.hallways)

    
    def getHallwayModel(self, n):
        return self.hallways[n]

    
    def getNumBattles(self):
        numBattles = 0
        for roomId in self.getRoomIds():
            numBattles += MintRoomSpecs.roomId2numBattles[roomId]
        
        return numBattles

    
    def getMintId(self):
        return self.mintId

    
    def getFloorNum(self):
        return self.floorNum

    
    def getRng(self):
        return random.Random(self.mintId * self.floorNum)

    
    def __str__(self):
        return 'MintLayout: id=%s, floor=%s, numRooms=%s, numBattles=%s' % (self.mintId, self.floorNum, self.getNumRooms(), self.getNumBattles())

    
    def __repr__(self):
        return str(self)


