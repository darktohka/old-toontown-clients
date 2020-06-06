# File: C (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from direct.fsm import State
from toontown.building import Elevator
from toontown.coghq import CogHQExterior
from toontown.safezone import Train

class CashbotHQExterior(CogHQExterior.CogHQExterior):
    notify = DirectNotifyGlobal.directNotify.newCategory('CashbotHQExterior')
    TrackZ = -67
    TrainTracks = [
        {
            'start': Point3(-1000, -54.450000000000003, TrackZ),
            'end': Point3(2200, -54.450000000000003, TrackZ) },
        {
            'start': Point3(1800, -133.44999999999999, TrackZ),
            'end': Point3(-1200, -133.44999999999999, TrackZ) },
        {
            'start': Point3(-1000, -212.44999999999999, TrackZ),
            'end': Point3(2200, -212.44999999999999, TrackZ) },
        {
            'start': Point3(1800, -291.44999999999999, TrackZ),
            'end': Point3(-1200, -291.44999999999999, TrackZ) }]
    
    def __init__(self, loader, parentFSM, doneEvent):
        CogHQExterior.CogHQExterior.__init__(self, loader, parentFSM, doneEvent)
        self.elevatorDoneEvent = 'elevatorDone'
        self.trains = None
        self.fsm.addState(State.State('elevator', self.enterElevator, self.exitElevator, [
            'walk']))
        state = self.fsm.getStateNamed('walk')
        state.addTransition('elevator')

    
    def load(self):
        CogHQExterior.CogHQExterior.load(self)
        if not (self.trains):
            self.trains = []
            for track in self.TrainTracks:
                train = Train.Train(track['start'], track['end'], self.TrainTracks.index(track), len(self.TrainTracks))
                self.trains.append(train)
            
        

    
    def unload(self):
        CogHQExterior.CogHQExterior.unload(self)
        for train in self.trains:
            train.delete()
        
        self.trains = None

    
    def enter(self, requestStatus):
        CogHQExterior.CogHQExterior.enter(self, requestStatus)
        for train in self.trains:
            train.show()
        

    
    def exit(self):
        CogHQExterior.CogHQExterior.exit(self)
        for train in self.trains:
            train.hide()
        

    
    def enterElevator(self, distElevator):
        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm.getStateNamed('elevator'), self.elevatorDoneEvent, distElevator)
        self.elevator.load()
        self.elevator.enter()

    
    def exitElevator(self):
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        del self.elevator

    
    def detectedElevatorCollision(self, distElevator):
        self.fsm.request('elevator', [
            distElevator])

    
    def handleElevatorDone(self, doneStatus):
        self.notify.debug('handling elevator done event')
        where = doneStatus['where']
        if where == 'reject':
            self.fsm.request('walk')
        elif where == 'exit':
            self.fsm.request('walk')
        elif where == 'mintInterior':
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
        else:
            self.notify.error('Unknown mode: ' + where + ' in handleElevatorDone')


