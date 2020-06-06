# File: E (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DirectGui import *
from IntervalGlobal import *
import PandaObject
import FSM
import State
import StateData
import DownloadForceAcknowledge
import Localizer

class Elevator(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, elevatorState, doneEvent, distElevator):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = FSM.FSM('Elevator', [
            State.State('start', self.enterStart, self.exitStart, [
                'elevatorDFA']),
            State.State('elevatorDFA', self.enterElevatorDFA, self.exitElevatorDFA, [
                'requestBoard',
                'final']),
            State.State('requestBoard', self.enterRequestBoard, self.exitRequestBoard, [
                'boarding']),
            State.State('boarding', self.enterBoarding, self.exitBoarding, [
                'boarded']),
            State.State('boarded', self.enterBoarded, self.exitBoarded, [
                'requestExit',
                'elevatorClosing',
                'final']),
            State.State('requestExit', self.enterRequestExit, self.exitRequestExit, [
                'exiting',
                'elevatorClosing']),
            State.State('elevatorClosing', self.enterElevatorClosing, self.exitElevatorClosing, [
                'final']),
            State.State('exiting', self.enterExiting, self.exitExiting, [
                'final']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.dfaDoneEvent = 'elevatorDfaDoneEvent'
        self.elevatorState = elevatorState
        self.distElevator = distElevator
        return None

    
    def load(self):
        self.elevatorState.addChild(self.fsm)
        self.buttonModels = loader.loadModelOnce('phase_3.5/models/gui/inventory_gui')
        self.upButton = self.buttonModels.find('**//InventoryButtonUp')
        self.downButton = self.buttonModels.find('**/InventoryButtonDown')
        self.rolloverButton = self.buttonModels.find('**/InventoryButtonRollover')
        return None

    
    def unload(self):
        self.elevatorState.removeChild(self.fsm)
        del self.fsm
        del self.elevatorState
        self.buttonModels.removeNode()
        del self.buttonModels
        del self.upButton
        del self.downButton
        del self.rolloverButton
        return None

    
    def enter(self):
        self.fsm.enterInitialState()
        self.fsm.request('elevatorDFA')
        return None

    
    def exit(self):
        self.ignoreAll()
        return None

    
    def signalDone(self, doneStatus):
        messenger.send(self.doneEvent, [
            doneStatus])

    
    def enterStart(self):
        return None

    
    def exitStart(self):
        return None

    
    def enterElevatorDFA(self):
        self.acceptOnce(self.dfaDoneEvent, self.enterDFACallback)
        self.dfa = DownloadForceAcknowledge.DownloadForceAcknowledge(self.dfaDoneEvent)
        self.dfa.enter(7)
        return None

    
    def enterDFACallback(self, DFAdoneStatus):
        self.dfa.exit()
        del self.dfa
        if DFAdoneStatus['mode'] == 'complete':
            self.fsm.request('requestBoard')
        elif DFAdoneStatus['mode'] == 'incomplete':
            elevatorDoneStatus = { }
            elevatorDoneStatus['where'] = 'reject'
            messenger.send(self.doneEvent, [
                elevatorDoneStatus])
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(DFAdoneStatus))
        return None

    
    def exitElevatorDFA(self):
        self.ignore(self.dfaDoneEvent)
        return None

    
    def enterRequestBoard(self):
        messenger.send(self.distElevator.uniqueName('enterElevatorOK'))
        return None

    
    def exitRequestBoard(self):
        return None

    
    def enterBoarding(self, nodePath):
        camera.wrtReparentTo(nodePath)
        self.cameraBoardTrack = Track([
            LerpPosHprInterval(camera, 1.5, Point3(0, -16, 5.5), Point3(0, 0, 0))])
        self.cameraBoardTrack.play()
        return None

    
    def exitBoarding(self):
        self.ignore('boardedElevator')
        return None

    
    def enterBoarded(self):
        self.enableExitButton()
        return None

    
    def exitBoarded(self):
        self.cameraBoardTrack.stop()
        self.disableExitButton()
        return None

    
    def enableExitButton(self):
        self.exitButton = DirectButton(relief = None, text = Localizer.ElevatorHopOff, text_fg = (0.90000000000000002, 0.90000000000000002, 0.90000000000000002, 1), text_pos = (0, -0.23000000000000001), text_scale = 0.80000000000000004, image = (self.upButton, self.downButton, self.rolloverButton), image_color = (0.5, 0.5, 0.5, 1), image_scale = (20, 1, 11), pos = (0, 0, 0.80000000000000004), scale = 0.14999999999999999, command = lambda self = self: self.fsm.request('requestExit'))
        return None

    
    def disableExitButton(self):
        self.exitButton.destroy()
        return None

    
    def enterRequestExit(self):
        messenger.send('elevatorExitButton')
        return None

    
    def exitRequestExit(self):
        return None

    
    def enterElevatorClosing(self):
        return None

    
    def exitElevatorClosing(self):
        return None

    
    def enterExiting(self):
        return None

    
    def exitExiting(self):
        return None

    
    def enterFinal(self):
        return None

    
    def exitFinal(self):
        return None


