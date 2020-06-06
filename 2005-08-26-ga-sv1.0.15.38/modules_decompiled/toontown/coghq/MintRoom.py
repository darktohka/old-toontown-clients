# File: M (Python 2.2)

from pandac.PandaModules import *
from direct.showbase import DirectObject
from direct.fsm import ClassicFSM, State
from toontown.toonbase import ToontownGlobals
from toontown.coghq import MintRoomSpecs
import random

class MintRoom(DirectObject.DirectObject):
    FloorCollPrefix = 'mintFloorColl'
    CashbotMintDoorFrame = 'phase_10/models/cashbotHQ/DoorFrame'
    
    def __init__(self, path = None):
        if path is not None:
            if path in MintRoomSpecs.CashbotMintConnectorRooms:
                loadFunc = loader.loadModelCopy
            else:
                loadFunc = loader.loadModel
            self.setGeom(loadFunc(path))
        
        self.localToonFSM = ClassicFSM.ClassicFSM('MintRoomLocalToonPresent', [
            State.State('off', self.enterLtOff, self.exitLtOff, [
                'notPresent']),
            State.State('notPresent', self.enterLtNotPresent, self.exitLtNotPresent, [
                'present']),
            State.State('present', self.enterLtPresent, self.exitLtPresent, [
                'notPresent'])], 'notPresent', 'notPresent')
        self.localToonFSM.enterInitialState()

    
    def delete(self):
        del self.localToonFSM

    
    def enter(self):
        self.localToonFSM.request('notPresent')

    
    def exit(self):
        self.localToonFSM.requestFinalState()

    
    def setRoomNum(self, num):
        self.roomNum = num

    
    def getRoomNum(self):
        return self.roomNum

    
    def setGeom(self, geom):
        self._MintRoom__geom = geom

    
    def getGeom(self):
        return self._MintRoom__geom

    
    def _getEntrances(self):
        return self._MintRoom__geom.findAllMatches('**/ENTRANCE*').asList()

    
    def _getExits(self):
        return self._MintRoom__geom.findAllMatches('**/EXIT*').asList()

    
    def attachTo(self, other, rng):
        otherExits = other._getExits()
        entrances = self._getEntrances()
        otherDoor = otherExits[0]
        thisDoor = rng.choice(entrances)
        geom = self.getGeom()
        otherGeom = other.getGeom()
        tempNode = otherDoor.attachNewNode('tempRotNode')
        geom.reparentTo(tempNode)
        geom.clearMat()
        geom.setPos(Vec3(0) - thisDoor.getPos(geom))
        tempNode.setH(-thisDoor.getH(otherDoor))
        geom.wrtReparentTo(otherGeom.getParent())
        tempNode.removeNode()
        doorFrame = loader.loadModelCopy(MintRoom.CashbotMintDoorFrame)
        doorFrame.reparentTo(thisDoor)

    
    def getFloorCollName(self):
        return '%s%s' % (MintRoom.FloorCollPrefix, self.roomNum)

    
    def initFloorCollisions(self):
        allColls = self.getGeom().findAllMatches('**/+CollisionNode').asList()
        floorColls = []
        for coll in allColls:
            bitmask = coll.node().getIntoCollideMask()
            if not (bitmask & ToontownGlobals.FloorBitmask).isZero():
                floorColls.append(coll)
            
        
        if len(floorColls) > 0:
            floorCollName = self.getFloorCollName()
            others = self.getGeom().findAllMatches('**/%s' % floorCollName).asList()
            for other in others:
                other.setName('%s_renamed' % floorCollName)
            
            for floorColl in floorColls:
                floorColl.setName(floorCollName)
            
        

    
    def enterLtOff(self):
        pass

    
    def exitLtOff(self):
        pass

    
    def enterLtNotPresent(self):
        pass

    
    def exitLtNotPresent(self):
        pass

    
    def enterLtPresent(self):
        pass

    
    def exitLtPresent(self):
        pass


