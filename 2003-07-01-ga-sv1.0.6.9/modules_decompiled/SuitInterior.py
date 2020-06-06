# File: S (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
import DirectNotifyGlobal
import Place
import PandaObject
import StateData
import FSM
import State
import TownBattle
import Suit
import Elevator
import ToontownGlobals
import ToontownBattleGlobals

class SuitInterior(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitInterior')
    
    def __init__(self, loader, parentFSM, doneEvent):
        Place.Place.__init__(self, loader, doneEvent)
        self.fsm = FSM.FSM('SuitInterior', [
            State.State('entrance', self.enterEntrance, self.exitEntrance, [
                'battle',
                'walk']),
            State.State('Elevator', self.enterElevator, self.exitElevator, [
                'battle',
                'walk']),
            State.State('battle', self.enterBattle, self.exitBattle, [
                'walk']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'stickerBook',
                'teleportOut',
                'Elevator',
                'DFA']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk',
                'DFA']),
            State.State('DFA', self.enterDFA, self.exitDFA, [
                'DFAReject',
                'teleportOut']),
            State.State('DFAReject', self.enterDFAReject, self.exitDFAReject, [
                'walk']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk']),
            State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, [
                'teleportIn']),
            State.State('elevatorOut', self.enterElevatorOut, self.exitElevatorOut, [])], 'entrance', 'elevatorOut')
        self.parentFSM = parentFSM
        self.elevatorDoneEvent = 'elevatorDoneSI'
        self._SuitInterior__zoneId = 0
        self.currentFloor = 0

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        self._SuitInterior__zoneId = requestStatus['zoneId']
        self.accept('DSIDoneEvent', self.handleDSIDoneEvent)

    
    def exit(self):
        self.ignoreAll()

    
    def load(self):
        Place.Place.load(self)
        self.parentFSM.getStateNamed('suitInterior').addChild(self.fsm)
        self.townBattle = TownBattle.TownBattle('town-battle-done')
        self.townBattle.load()
        for i in range(1, 3):
            Suit.loadSuits(i)
        

    
    def unload(self):
        Place.Place.unload(self)
        self.parentFSM.getStateNamed('suitInterior').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        self.townBattle.unload()
        self.townBattle.cleanup()
        del self.townBattle
        for i in range(1, 3):
            Suit.unloadSuits(i)
        

    
    def setState(self, state, battleEvent = None):
        if battleEvent:
            self.fsm.request(state, [
                battleEvent])
        else:
            self.fsm.request(state)

    
    def getZoneId(self):
        return self._SuitInterior__zoneId

    
    def enterZone(self, zoneId):
        pass

    
    def isPeriodTimerEffective(self):
        return 0

    
    def handleDSIDoneEvent(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    
    def enterEntrance(self):
        return None

    
    def exitEntrance(self):
        return None

    
    def enterElevator(self, distElevator):
        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm.getStateNamed('Elevator'), self.elevatorDoneEvent, distElevator)
        self.elevator.load()
        self.elevator.enter()
        return None
        return None

    
    def exitElevator(self):
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        del self.elevator
        return None

    
    def detectedElevatorCollision(self, distElevator):
        self.fsm.request('Elevator', [
            distElevator])
        return None

    
    def handleElevatorDone(self, doneStatus):
        self.notify.debug('handling elevator done event')
        where = doneStatus['where']
        if where == 'reject':
            self.fsm.request('walk')
        elif where == 'exit':
            self.fsm.request('walk')
        elif where == 'suitInterior':
            pass
        else:
            self.notify.error('Unknown mode: ' + +' in handleElevatorDone')

    
    def enterBattle(self, event):
        mult = ToontownBattleGlobals.getCreditMultiplier(self.currentFloor)
        self.townBattle.enter(event, self.fsm.getStateNamed('battle'), bldg = 1, creditMultiplier = mult)
        toonbase.localToon.b_setAnimState('off', 1)

    
    def exitBattle(self):
        self.townBattle.exit()

    
    def enterWalk(self, teleportIn = 0):
        Place.Place.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
    def enterStickerBook(self, page = None):
        Place.Place.enterStickerBook(self, page)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
    def enterTeleportIn(self, requestStatus):
        toonbase.localToon.setPosHpr(2.5, 11.5, ToontownGlobals.FloorOffset, 45.0, 0.0, 0.0)
        Place.Place.enterTeleportIn(self, requestStatus)

    
    def enterTeleportOut(self, requestStatus):
        Place.Place.enterTeleportOut(self, requestStatus, self._SuitInterior__teleportOutDone)

    
    def _SuitInterior__teleportOutDone(self, requestStatus):
        hoodId = requestStatus['hoodId']
        if hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            messenger.send('localToonLeft')
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    
    def exitTeleportOut(self):
        return None

    
    def goHomeFailed(self, task):
        self.notifyUserGoHomeFailed()
        self.ignore('setLocalEstateZone')
        self.doneStatus['avId'] = -1
        self.doneStatus['zoneId'] = self.getZoneId()
        self.fsm.request('teleportIn', [
            self.doneStatus])
        return Task.done

    
    def enterElevatorOut(self):
        return None

    
    def _SuitInterior__elevatorOutDone(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    
    def exitElevatorOut(self):
        return None


