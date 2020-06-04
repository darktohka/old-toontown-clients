# File: D (Python 2.2)

from IntervalGlobal import *
from ClockDelta import *
import ToontownGlobals
import DirectNotifyGlobal
import FSM
import DistributedDoor
import ZoneUtil
import DelayDelete
import FADoorCodes
import DoorTypes
import ToontownDialog

class DistributedCogHQDoor(DistributedDoor.DistributedDoor):
    
    def __init__(self, cr):
        DistributedDoor.DistributedDoor.__init__(self, cr)
        self.openSfx = base.loadSfx('phase_9/audio/sfx/CHQ_door_open.mp3')
        self.closeSfx = base.loadSfx('phase_9/audio/sfx/CHQ_door_close.mp3')

    
    def wantsNametag(self):
        return 0

    
    def getRequestStatus(self):
        zoneId = self.otherZoneId
        request = {
            'loader': ZoneUtil.getBranchLoaderName(zoneId),
            'where': ZoneUtil.getToonWhereName(zoneId),
            'how': 'doorIn',
            'hoodId': ZoneUtil.getHoodId(zoneId),
            'zoneId': zoneId,
            'shardId': None,
            'avId': -1,
            'allowRedirect': 0,
            'doorDoId': self.otherDoId }
        return request

    
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
        if self.rightSwing:
            h = 100
        else:
            h = -100
        self.doorTrack = Parallel(Sequence(LerpHprInterval(nodePath = rightDoor, duration = 1.0, hpr = VBase3(0, 0, 0), startHpr = VBase3(h, 0, 0), other = otherNP, blendType = 'easeInOut'), Func(doorFrameHoleRight.hide), Func(rightDoor.hide)), Sequence(Wait(0.5), SoundInterval(self.closeSfx, node = rightDoor)), name = trackName)
        self.doorTrack.start(ts)
        if hasattr(self, 'done'):
            request = self.getRequestStatus()
            messenger.send('doorDoneEvent', [
                request])
        

    
    def exitDoorEnterClosing(self, ts):
        doorFrameHoleLeft = self.findDoorNode('doorFrameHoleLeft')
        if doorFrameHoleLeft.isEmpty():
            self.notify.warning('enterOpening(): did not find flatDoors')
            return None
        
        if ZoneUtil.isInterior(self.zoneId):
            doorFrameHoleLeft.setColor(1.0, 1.0, 1.0, 1.0)
        
        if self.leftSwing:
            h = -100
        else:
            h = 100
        leftDoor = self.findDoorNode('leftDoor')
        if not leftDoor.isEmpty():
            otherNP = self.getDoorNodePath()
            trackName = 'doorExitTrack-%d' % self.doId
            self.doorExitTrack = Parallel(Sequence(LerpHprInterval(nodePath = leftDoor, duration = 1.0, hpr = VBase3(0, 0, 0), startHpr = VBase3(h, 0, 0), other = otherNP, blendType = 'easeInOut'), Func(doorFrameHoleLeft.hide), Func(leftDoor.hide)), Sequence(Wait(0.5), SoundInterval(self.closeSfx, node = leftDoor)), name = trackName)
            self.doorExitTrack.start(ts)
        


