# File: D (Python 2.2)

from PandaModules import *
from ClockDelta import *
from IntervalGlobal import *
from ElevatorConstants import *
from ElevatorUtils import *
import DistributedElevatorExt
import DistributedElevator
import ToontownGlobals
import FSM
import State
import ZoneUtil
import Localizer

class DistributedFactoryElevatorExt(DistributedElevatorExt.DistributedElevatorExt):
    
    def __init__(self, cr):
        DistributedElevatorExt.DistributedElevatorExt.__init__(self, cr)

    
    def generate(self):
        DistributedElevatorExt.DistributedElevatorExt.generate(self)

    
    def delete(self):
        self.elevatorModel.removeNode()
        del self.elevatorModel
        DistributedElevatorExt.DistributedElevatorExt.delete(self)

    
    def setEntranceId(self, entranceId):
        self.entranceId = entranceId
        if self.entranceId == 0:
            self.elevatorModel.setPosHpr(62.740000000000002, -85.310000000000002, 0.0, 2.0, 0.0, 0.0)
        elif self.entranceId == 1:
            self.elevatorModel.setPosHpr(-162.25, 26.43, 0.0, 269.0, 0.0, 0.0)
        else:
            self.notify.error('Invalid entranceId: %s' % entranceId)

    
    def setupElevator(self):
        self.elevatorModel = loader.loadModelCopy('phase_5/models/modules/elevator')
        self.elevatorModel.reparentTo(render)
        self.elevatorModel.setScale(1.05)
        self.leftDoor = self.elevatorModel.find('**/left-door')
        self.rightDoor = self.elevatorModel.find('**/right-door')
        self.elevatorModel.find('**/light_panel').removeNode()
        self.elevatorModel.find('**/light_panel_frame').removeNode()
        DistributedElevator.DistributedElevator.setupElevator(self)

    
    def getElevatorModel(self):
        return self.elevatorModel

    
    def setBldgDoId(self, bldgDoId):
        self.bldg = None
        self.setupElevator()

    
    def getZoneId(self):
        return 0

    
    def _DistributedFactoryElevatorExt__doorsClosed(self, zoneId):
        return None

    
    def setFactoryInteriorZone(self, zoneId):
        if self.localToonOnBoard:
            hoodId = ZoneUtil.getHoodId(zoneId)
            doneStatus = {
                'loader': 'cogHQLoader',
                'where': 'factoryInterior',
                'how': 'teleportIn',
                'zoneId': zoneId }
            self.cr.playGame.getPlace().elevator.signalDone(doneStatus)
        


