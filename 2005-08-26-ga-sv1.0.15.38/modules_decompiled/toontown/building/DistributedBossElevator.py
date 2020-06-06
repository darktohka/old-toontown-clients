# File: D (Python 2.2)

from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from ElevatorConstants import *
from ElevatorUtils import *
import DistributedElevator
import DistributedElevatorExt
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.hood import ZoneUtil
from toontown.toonbase import TTLocalizer
from toontown.toontowngui import TTDialog
from direct.distributed import DelayDelete

class DistributedBossElevator(DistributedElevatorExt.DistributedElevatorExt):
    
    def __init__(self, cr):
        DistributedElevatorExt.DistributedElevatorExt.__init__(self, cr)
        self.elevatorPoints = BigElevatorPoints
        self.openSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.mp3')
        self.finalOpenSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.mp3')
        self.closeSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.mp3')
        self.finalCloseSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.mp3')
        self.type = ELEVATOR_VP
        self.countdownTime = ElevatorData[self.type]['countdown']

    
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
        geom = base.cr.playGame.hood.loader.geom
        locator = geom.find('**/elevator_locator')
        self.elevatorModel.reparentTo(locator)
        self.elevatorModel.setH(180)
        DistributedElevator.DistributedElevator.setupElevator(self)

    
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
            hoodId = self.cr.playGame.hood.hoodId
            doneStatus = {
                'loader': 'cogHQLoader',
                'where': 'cogHQBossBattle',
                'how': 'movie',
                'zoneId': zoneId,
                'hoodId': hoodId }
            self.cr.playGame.getPlace().elevator.signalDone(doneStatus)
        

    
    def rejectBoard(self, avId):
        self.rejectDialog = TTDialog.TTGlobalDialog(message = TTLocalizer.BossElevatorRejectMessage, doneEvent = 'elevatorRejectAck', style = TTDialog.Acknowledge)
        self.rejectDialog.show()
        self.rejectDialog.delayDelete = DelayDelete.DelayDelete(self)
        base.localAvatar.b_setAnimState('neutral', 1.0)
        base.localAvatar.suit.loop('neutral')
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


