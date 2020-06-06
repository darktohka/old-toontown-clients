# File: D (Python 2.2)

from ToonBaseGlobal import *
from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
import ToontownGlobals
import DirectNotifyGlobal
import FSM
import DistributedDoor
import ZoneUtil
import Suit
import DelayDelete
import FADoorCodes
import DoorTypes
import ToontownDialog

class DistributedHouseDoor(DistributedDoor.DistributedDoor):
    
    def __init__(self, cr):
        DistributedDoor.DistributedDoor.__init__(self, cr)

    
    def generate(self):
        DistributedDoor.DistributedDoor.generate(self)

    
    def disable(self):
        DistributedDoor.DistributedDoor.disable(self)

    
    def delete(self):
        DistributedDoor.DistributedDoor.delete(self)

    
    def getTriggerName(self):
        return 'door_trigger_' + str(self.houseId)

    
    def hideDoorParts(self):
        return None

    
    def announceGenerate(self):
        self.hideDoorParts()
        self.setTriggerName()
        self.accept(self.getEnterTriggerEvent(), self.doorTrigger)
        self.acceptOnce('clearOutToonInterior', self.doorTrigger)

    
    def getBuilding(self):
        if not self.__dict__.has_key('building'):
            if self.doorType == DoorTypes.INT_STANDARD:
                door = render.find('**/leftDoor;+s')
                self.building = door.getParent()
            elif self.doorType == DoorTypes.EXT_STANDARD:
                
                try:
                    self.building = self.cr.doId2do.get(self.houseId).house
                except:
                    self.building = self.cr.playGame.estateLoader.enteredHouse

            
        
        return self.building

    
    def isInterior(self):
        if self.doorType == DoorTypes.INT_STANDARD:
            return 1
        
        return 0

    
    def enterDoor(self):
        messenger.send('DistributedDoor_doorTrigger')
        self.sendUpdate('requestEnter')

    
    def getDoorNodePath(self):
        if self.doorType == DoorTypes.INT_STANDARD:
            otherNP = render.find('**/door_origin')
        elif self.doorType == DoorTypes.EXT_STANDARD:
            building = self.getBuilding()
            otherNP = building.find('**/door')
            if otherNP.isEmpty():
                otherNP = building.find('**/door_origin')
            
        else:
            self.notify.error('No such door type as ' + str(self.doorType))
        return otherNP

    
    def enterClosing(self, ts):
        doorFrameHoleRight = self.findDoorNode('doorFrameHoleRight')
        if doorFrameHoleRight.isEmpty():
            self.notify.warning('enterClosing(): did not find doorFrameHoleRight')
            return None
        
        rightDoor = self.findDoorNode('rightDoor')
        if rightDoor.isEmpty():
            self.notify.warning('enterClosing(): did not find rightDoor')
            return None
        
        otherNP = self.getDoorNodePath()
        trackName = 'doorClose-%d' % self.doId
        self.doorTrack = Sequence(LerpHprInterval(node = rightDoor, duration = 1.0, hpr = VBase3(0, 0, 0), startHpr = VBase3(100, 0, 0), other = otherNP, blendType = 'easeInOut'), Func(doorFrameHoleRight.hide), Func(rightDoor.hide), SoundInterval(self.closeSfx), name = trackName)
        self.doorTrack.start(ts)
        if hasattr(self, 'done'):
            toonbase.tcr.playGame.estateLoader.setHouse(self.houseId)
            zoneId = self.otherZoneId
            if self.doorType == DoorTypes.EXT_STANDARD:
                whereTo = 'house'
            else:
                whereTo = 'estate'
            request = {
                'loader': 'estateLoader',
                'where': whereTo,
                'how': 'doorIn',
                'hoodId': ToontownGlobals.MyEstate,
                'zoneId': zoneId,
                'shardId': None,
                'avId': -1,
                'doorDoId': self.otherDoId }
            messenger.send('doorDoneEvent', [
                request])
        

    
    def setHouseId(self, houseId):
        self.notify.debug('setHouseId')
        self.houseId = houseId


