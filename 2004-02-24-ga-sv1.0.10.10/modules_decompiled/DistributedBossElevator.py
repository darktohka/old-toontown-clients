# File: D (Python 2.2)

from PandaModules import *
from ClockDelta import *
from IntervalGlobal import *
from ElevatorConstants import *
from ElevatorUtils import *
import DistributedElevator
import DistributedElevatorExt
import ToontownGlobals
import DirectNotifyGlobal
import FSM
import State
import ZoneUtil
import Localizer
import ToontownDialog
import DelayDelete

class DistributedBossElevator(DistributedElevatorExt.DistributedElevatorExt):
    countdownTime = BOSS_ELEVATOR_COUNTDOWN_TIME
    
    def __init__(self, cr):
        DistributedElevatorExt.DistributedElevatorExt.__init__(self, cr)
        self.bigElevator = 1
        self.elevatorPoints = BigElevatorPoints
        self.openSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.mp3')
        self.finalOpenSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.mp3')
        self.closeSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.mp3')
        self.finalCloseSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.mp3')

    
    def disable(self):
        DistributedElevator.DistributedElevator.disable(self)

    
    def generate(self):
        DistributedElevatorExt.DistributedElevatorExt.generate(self)

    
    def delete(self):
        self.elevatorModel.removeNode()
        del self.elevatorModel
        DistributedElevatorExt.DistributedElevatorExt.delete(self)

    
    def setupElevator(self):
        self.elevatorModel = loader.loadModelCopy('phase_9/models/cogHQ/cogHQ_elevator')
        icon = self.elevatorModel.find('**/big_frame/')
        icon.hide()
        self.leftDoor = self.elevatorModel.find('**/left-door')
        self.rightDoor = self.elevatorModel.find('**/right-door')
        geom = toonbase.tcr.playGame.hood.loader.geom
        locator = geom.find('**/elevator_locator')
        self.elevatorModel.reparentTo(locator)
        self.elevatorModel.setH(180)
        DistributedElevator.DistributedElevator.setupElevator(self, big = 1)

    
    def getElevatorModel(self):
        return self.elevatorModel

    
    def gotBldg(self, buildingList):
        return DistributedElevator.DistributedElevator.gotBldg(self, buildingList)

    
    def getZoneId(self):
        return 0

    
    def _DistributedBossElevator__doorsClosed(self, zoneId):
        return None

    
    def setBossOfficeZone(self, zoneId):
        if self.localToonOnBoard:
            hoodId = ZoneUtil.getHoodId(zoneId)
            doneStatus = {
                'loader': 'cogHQLoader',
                'where': 'cogHQBossBattle',
                'how': 'movie',
                'zoneId': zoneId }
            self.cr.playGame.getPlace().elevator.signalDone(doneStatus)
        

    
    def rejectBoard(self, avId):
        self.rejectDialog = ToontownDialog.GlobalDialog(message = Localizer.BossElevatorRejectMessage, doneEvent = 'elevatorRejectAck', style = ToontownDialog.Acknowledge)
        self.rejectDialog.show()
        self.rejectDialog.delayDelete = DelayDelete.DelayDelete(self)
        toonbase.localToon.b_setAnimState('neutral', 1.0)
        toonbase.localToon.suit.loop('neutral')
        self.acceptOnce('elevatorRejectAck', self._DistributedBossElevator__handleRejectAck)

    
    def _DistributedBossElevator__handleRejectAck(self):
        doneStatus = self.rejectDialog.doneStatus
        if doneStatus != 'ok':
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))
        
        doneStatus = {
            'where': 'reject' }
        self.cr.playGame.getPlace().elevator.signalDone(doneStatus)
        self.rejectDialog.cleanup()
        del self.rejectDialog


