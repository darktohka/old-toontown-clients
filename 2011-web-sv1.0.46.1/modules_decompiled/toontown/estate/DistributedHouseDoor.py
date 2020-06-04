# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\estate\DistributedHouseDoor.py
from toontown.toonbase.ToonBaseGlobal import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from direct.distributed import DistributedObject
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.MessengerGlobal import messenger
from direct.fsm import ClassicFSM
from toontown.building import DistributedDoor
from toontown.hood import ZoneUtil
from toontown.suit import Suit
from toontown.building import FADoorCodes
from toontown.building import DoorTypes

class DistributedHouseDoor(DistributedDoor.DistributedDoor):
    __module__ = __name__

    def __init__(self, cr):
        DistributedDoor.DistributedDoor.__init__(self, cr)

    def disable(self):
        DistributedDoor.DistributedDoor.disable(self)
        self.ignoreAll()

    def setZoneIdAndBlock(self, zoneId, block):
        self.houseId = block
        DistributedDoor.DistributedDoor.setZoneIdAndBlock(self, zoneId, block)

    def getTriggerName(self):
        return 'door_trigger_' + str(self.houseId)

    def hideDoorParts(self):
        pass

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        if self.doorType == DoorTypes.EXT_STANDARD:
            house = base.cr.doId2do.get(self.houseId)
            if house and house.house_loaded:
                self.__gotRelatedHouse()
            else:
                self.acceptOnce('houseLoaded-%d' % self.houseId, self.__gotRelatedHouse)
        elif self.doorType == DoorTypes.INT_STANDARD:
            door = render.find('**/leftDoor;+s')
            if door.isEmpty():
                self.acceptOnce('houseInteriorLoaded-%d' % self.zoneId, self.__gotRelatedHouse)
            else:
                self.__gotRelatedHouse()

    def __gotRelatedHouse(self):
        self.doPostAnnounceGenerate()
        self.bHasFlat = not self.findDoorNode('door*flat', True).isEmpty()
        self.hideDoorParts()
        self.setTriggerName()
        self.accept(self.getEnterTriggerEvent(), self.doorTrigger)
        self.acceptOnce('clearOutToonInterior', self.doorTrigger)
        self.zoneDoneLoading = 0

    def getBuilding(self, allowEmpty=False):
        if not self.__dict__.has_key('building'):
            if self.doorType == DoorTypes.INT_STANDARD:
                door = render.find('**/leftDoor;+s')
                self.building = door.getParent()
            elif self.doorType == DoorTypes.EXT_STANDARD:
                if self.houseId:
                    self.building = self.cr.playGame.hood.loader.houseId2house.get(self.houseId, None)
        if allowEmpty:
            return self.building
        return self.building

    def isInterior(self):
        if self.doorType == DoorTypes.INT_STANDARD:
            return 1
        return 0

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
            return
        rightDoor = self.findDoorNode('rightDoor')
        if rightDoor.isEmpty():
            self.notify.warning('enterClosing(): did not find rightDoor')
            return
        otherNP = self.getDoorNodePath()
        trackName = 'doorClose-%d' % self.doId
        if self.rightSwing:
            h = 100
        else:
            h = -100
        self.finishDoorTrack()
        self.doorTrack = Sequence(LerpHprInterval(nodePath=rightDoor, duration=1.0, hpr=VBase3(0, 0, 0), startHpr=VBase3(h, 0, 0), other=otherNP, blendType='easeInOut'), Func(doorFrameHoleRight.hide), Func(self.hideIfHasFlat, rightDoor), SoundInterval(self.closeSfx, node=rightDoor), name=trackName)
        self.doorTrack.start(ts)
        if hasattr(self, 'done'):
            base.cr.playGame.hood.loader.setHouse(self.houseId)
            zoneId = self.otherZoneId
            if self.doorType == DoorTypes.EXT_STANDARD:
                whereTo = 'house'
            else:
                whereTo = 'estate'
            request = {'loader': 'safeZoneLoader', 'where': whereTo, 'how': 'doorIn', 'hoodId': ToontownGlobals.MyEstate, 'zoneId': zoneId, 'shardId': None, 'avId': -1, 'allowRedirect': 0, 'doorDoId': self.otherDoId}
            messenger.send('doorDoneEvent', [request])
        return