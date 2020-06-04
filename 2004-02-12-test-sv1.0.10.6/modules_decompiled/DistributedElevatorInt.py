# File: D (Python 2.2)

from PandaModules import *
from ClockDelta import *
from IntervalGlobal import *
from ElevatorConstants import *
from ElevatorUtils import *
import DistributedElevator
import ToontownGlobals
import DirectNotifyGlobal
import FSM
import State
import ZoneUtil
import Localizer

class DistributedElevatorInt(DistributedElevator.DistributedElevator):
    countdownTime = base.config.GetFloat('int-elevator-timeout', INTERIOR_ELEVATOR_COUNTDOWN_TIME)
    
    def __init__(self, cr):
        DistributedElevator.DistributedElevator.__init__(self, cr)

    
    def setupElevator(self):
        self.leftDoor = self.bldg.leftDoorOut
        self.rightDoor = self.bldg.rightDoorOut
        DistributedElevator.DistributedElevator.setupElevator(self)

    
    def forcedExit(self, avId):
        target_sz = toonbase.localToon.defaultZone
        toonbase.tcr.playGame.getPlace().fsm.request('teleportOut', [
            {
                'loader': ZoneUtil.getLoaderName(target_sz),
                'where': ZoneUtil.getWhereName(target_sz, 1),
                'how': 'teleportIn',
                'hoodId': target_sz,
                'zoneId': target_sz,
                'shardId': None,
                'avId': -1 }])

    
    def enterWaitCountdown(self, ts):
        DistributedElevator.DistributedElevator.enterWaitCountdown(self, ts)
        self.acceptOnce('localToonLeft', self._DistributedElevatorInt__handleTeleportOut)
        self.startCountdownClock(self.countdownTime, ts)

    
    def _DistributedElevatorInt__handleTeleportOut(self):
        self.sendUpdate('requestBuildingExit', [])

    
    def exitWaitCountdown(self):
        self.ignore('localToonLeft')
        DistributedElevator.DistributedElevator.exitWaitCountdown(self)

    
    def getZoneId(self):
        return self.bldg.getZoneId()

    
    def getElevatorModel(self):
        return self.bldg.elevatorModelOut


