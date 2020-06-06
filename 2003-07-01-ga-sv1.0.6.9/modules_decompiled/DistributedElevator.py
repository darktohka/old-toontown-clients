# File: D (Python 2.2)

from ShowBaseGlobal import *
from ClockDelta import *
import DirectNotifyGlobal
import FSM
import DistributedObject

class DistributedElevator(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.fsm = FSM.FSM('DistributedElevator', [
            State.State('off', self.enterOff, self.exitOff, [
                'closing',
                'closed',
                'opening',
                'open']),
            State.State('closing', self.enterClosing, self.exitClosing, [
                'closed']),
            State.State('closed', self.enterClosed, self.exitClosed, [
                'opening']),
            State.State('opening', self.enterOpening, self.exitOpening, [
                'open']),
            State.State('open', self.enterOpen, self.exitOpen, [
                'closing'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.skipClosedDoor = 1

    
    def disable(self):
        self.fsm.request('off')
        del self.building
        self.ignore('enterdoor_trigger_' + self.block, self.doorTrigger)
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    
    def setBlock(self, block):
        self.block = block
        self.accept('enterdoor_trigger_' + self.block, self.doorTrigger)

    
    def setState(self, state, timestamp):
        self.fsm.request(state, [
            globalClockDelta.localElapsedTime(timestamp)])

    
    def _DistributedElevator__getBuilding(self):
        if not self.__dict__.has_key('building'):
            self.building = self.cr.playGame.hood.loader.geom.find('**/tb' + self.block + ':*_DNARoot')
        
        return self.building

    
    def doorTrigger(self, args):
        print '\n\n', self.block, ': DistributedElevator.doorTrigger()', args, '\n\n'

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterClosing(self, ts):
        building = self._DistributedElevator__getBuilding()
        complexDoor = building.find('complexDoor')

    
    def exitClosing(self):
        pass

    
    def enterClosed(self, ts):
        if self.skipClosedDoor:
            self.skipClosedDoor = 0
            return None
        
        building = self._DistributedElevator__getBuilding()
        simpleDoor = building.find('simpleDoor')
        if not simpleDoor.isEmpty():
            simpleDoor.unstash()
        
        complexDoor = building.find('complexDoor')
        if not complexDoor.isEmpty():
            complexDoor.stash()
        

    
    def exitClosed(self):
        pass

    
    def enterOpening(self, ts):
        self.skipClosedDoor = 0
        building = self._DistributedElevator__getBuilding()
        complexDoor = building.find('complexDoor')
        if not complexDoor.isEmpty():
            complexDoor.unstash()
        
        simpleDoor = building.find('simpleDoor')
        if not simpleDoor.isEmpty():
            simpleDoor.stash()
        

    
    def exitOpening(self):
        pass

    
    def enterOpen(self, ts):
        pass

    
    def exitOpen(self):
        pass


