# File: D (Python 2.2)

from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from ElevatorConstants import *
from ElevatorUtils import *
from direct.showbase import PythonUtil
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.distributed import DistributedObject
from direct.fsm import State
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from direct.task import Task
from direct.distributed import DelayDelete
from toontown.hood import ZoneUtil

class DistributedElevator(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedElevator')
    notify.setDebug(1)
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.bldgRequest = None
        self.toonRequests = { }
        self.deferredSlots = []
        self.localToonOnBoard = 0
        self.boardedAvIds = { }
        self.openSfx = base.loadSfx('phase_5/audio/sfx/elevator_door_open.mp3')
        self.finalOpenSfx = None
        self.closeSfx = base.loadSfx('phase_5/audio/sfx/elevator_door_close.mp3')
        self.finalCloseSfx = None
        self.elevatorPoints = ElevatorPoints
        self.type = ELEVATOR_NORMAL
        self.countdownTime = ElevatorData[self.type]['countdown']
        self.fsm = ClassicFSM.ClassicFSM('DistributedElevator', [
            State.State('off', self.enterOff, self.exitOff, [
                'opening',
                'waitEmpty',
                'waitCountdown',
                'closing',
                'closed']),
            State.State('opening', self.enterOpening, self.exitOpening, [
                'waitEmpty',
                'waitCountdown']),
            State.State('waitEmpty', self.enterWaitEmpty, self.exitWaitEmpty, [
                'waitCountdown']),
            State.State('waitCountdown', self.enterWaitCountdown, self.exitWaitCountdown, [
                'waitEmpty',
                'closing']),
            State.State('closing', self.enterClosing, self.exitClosing, [
                'closed',
                'waitEmpty']),
            State.State('closed', self.enterClosed, self.exitClosed, [
                'opening'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.isSetup = 0
        self._DistributedElevator__preSetupState = None
        self.bigElevator = 0
        base.elevator = self

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def setupElevator(self):
        collisionRadius = ElevatorData[self.type]['collRadius']
        self.elevatorSphere = CollisionSphere(0, 5, 0, collisionRadius)
        self.elevatorSphere.setTangible(0)
        self.elevatorSphereNode = CollisionNode(self.uniqueName('elevatorSphere'))
        self.elevatorSphereNode.setIntoCollideMask(ToontownGlobals.WallBitmask)
        self.elevatorSphereNode.addSolid(self.elevatorSphere)
        self.elevatorSphereNodePath = self.getElevatorModel().attachNewNode(self.elevatorSphereNode)
        self.elevatorSphereNodePath.hide()
        self.elevatorSphereNodePath.reparentTo(self.getElevatorModel())
        self.elevatorSphereNodePath.stash()
        self.boardedAvIds = { }
        self.openDoors = getOpenInterval(self, self.leftDoor, self.rightDoor, self.openSfx, self.finalOpenSfx, self.type)
        self.closeDoors = getCloseInterval(self, self.leftDoor, self.rightDoor, self.closeSfx, self.finalCloseSfx, self.type)
        self.closeDoors = Sequence(self.closeDoors, Func(self.onDoorCloseFinish))
        self.finishSetup()

    
    def finishSetup(self):
        self.isSetup = 1
        if self._DistributedElevator__preSetupState:
            self.fsm.request(self._DistributedElevator__preSetupState, [
                0])
            self._DistributedElevator__preSetupState = None
        
        for slot in self.deferredSlots:
            self.fillSlot(*slot)
        
        self.deferredSlots = []

    
    def disable(self):
        if self.bldgRequest:
            self.cr.relatedObjectMgr.abortRequest(self.bldgRequest)
            self.bldgRequest = None
        
        for request in self.toonRequests.values():
            self.cr.relatedObjectMgr.abortRequest(request)
        
        self.toonRequests = { }
        self.openDoors.pause()
        self.closeDoors.pause()
        self.fsm.request('off')
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        if self.isSetup:
            self.elevatorSphereNodePath.removeNode()
            del self.elevatorSphereNodePath
            del self.elevatorSphereNode
            del self.elevatorSphere
            del self.bldg
            del self.leftDoor
            del self.rightDoor
            del self.openDoors
            del self.closeDoors
        
        del self.fsm
        del self.openSfx
        del self.closeSfx
        self.isSetup = 0
        DistributedObject.DistributedObject.delete(self)

    
    def setBldgDoId(self, bldgDoId):
        self.bldgDoId = bldgDoId
        self.bldgRequest = self.cr.relatedObjectMgr.requestObjects([
            bldgDoId], allCallback = self.gotBldg, timeout = 2)

    
    def gotBldg(self, buildingList):
        self.bldgRequest = None
        self.bldg = buildingList[0]
        if not (self.bldg):
            self.notify.error('setBldgDoId: elevator %d cannot find bldg %d!' % (self.doId, self.bldgDoId))
            return None
        
        self.setupElevator()

    
    def gotToon(self, index, avId, x, y, z, h, p, r, timestamp, toonList):
        del self.toonRequests[avId]
        self.fillSlot(index, avId, x, y, z, h, p, r, timestamp)

    
    def setState(self, state, timestamp):
        if self.isSetup:
            self.fsm.request(state, [
                globalClockDelta.localElapsedTime(timestamp)])
        else:
            self._DistributedElevator__preSetupState = state

    
    def fillSlot0(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(0, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot1(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(1, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot2(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(2, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot3(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(3, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot4(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(4, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot5(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(5, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot6(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(6, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot7(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(7, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot(self, index, avId, x, y, z, h, p, r, timestamp):
        if avId == 0:
            pass
        1
        if not self.cr.doId2do.has_key(avId):
            func = PythonUtil.Functor(self.gotToon, index, avId, x, y, z, h, p, r, timestamp)
            self.toonRequests[avId] = self.cr.relatedObjectMgr.requestObjects([
                avId], allCallback = func)
        elif not (self.isSetup):
            self.deferredSlots.append((index, avId, x, y, z, h, p, r, timestamp))
        elif avId == base.localAvatar.getDoId():
            self.localToonOnBoard = 1
            elevator = self.getPlaceElevator()
            elevator.fsm.request('boarding', [
                self.getElevatorModel()])
            elevator.fsm.request('boarded')
        
        toon = self.cr.doId2do[avId]
        toon.stopSmooth()
        toon.setZ(self.getElevatorModel(), self.elevatorPoints[index][2])
        toon.setShadowHeight(0)
        if toon.isDisguised:
            toon.suit.loop('walk')
            animFunc = Func(toon.suit.loop, 'neutral')
        else:
            toon.setAnimState('run', 1.0)
            animFunc = Func(toon.setAnimState, 'neutral', 1.0)
        toon.headsUp(self.getElevatorModel(), apply(Point3, self.elevatorPoints[index]))
        track = Sequence(LerpPosInterval(toon, TOON_BOARD_ELEVATOR_TIME * 0.75, apply(Point3, self.elevatorPoints[index]), other = self.getElevatorModel()), LerpHprInterval(toon, TOON_BOARD_ELEVATOR_TIME * 0.25, Point3(180, 0, 0), other = self.getElevatorModel()), animFunc, name = toon.uniqueName('fillElevator'), autoPause = 1)
        track.delayDelete = DelayDelete.DelayDelete(toon)
        track.start()
        self.boardedAvIds[avId] = None

    
    def emptySlot0(self, avId, bailFlag, timestamp):
        self.emptySlot(0, avId, bailFlag, timestamp)

    
    def emptySlot1(self, avId, bailFlag, timestamp):
        self.emptySlot(1, avId, bailFlag, timestamp)

    
    def emptySlot2(self, avId, bailFlag, timestamp):
        self.emptySlot(2, avId, bailFlag, timestamp)

    
    def emptySlot3(self, avId, bailFlag, timestamp):
        self.emptySlot(3, avId, bailFlag, timestamp)

    
    def emptySlot4(self, avId, bailFlag, timestamp):
        self.emptySlot(4, avId, bailFlag, timestamp)

    
    def emptySlot5(self, avId, bailFlag, timestamp):
        self.emptySlot(5, avId, bailFlag, timestamp)

    
    def emptySlot6(self, avId, bailFlag, timestamp):
        self.emptySlot(6, avId, bailFlag, timestamp)

    
    def emptySlot7(self, avId, bailFlag, timestamp):
        self.emptySlot(7, avId, bailFlag, timestamp)

    
    def notifyToonOffElevator(self, toon):
        toon.setAnimState('neutral', 1.0)
        if toon == base.localAvatar:
            doneStatus = {
                'where': 'exit' }
            elevator = self.getPlaceElevator()
            elevator.signalDone(doneStatus)
            self.localToonOnBoard = 0
        else:
            toon.startSmooth()
        return None

    
    def emptySlot(self, index, avId, bailFlag, timestamp):
        if avId == 0:
            pass
        1
        if not (self.isSetup):
            newSlots = []
            for slot in self.deferredSlots:
                if slot[0] != index:
                    newSlots.append(slot)
                
            
            self.deferredSlots = newSlots
        elif self.cr.doId2do.has_key(avId):
            if bailFlag == 1 and hasattr(self, 'clockNode'):
                if timestamp < self.countdownTime and timestamp >= 0:
                    self.countdown(self.countdownTime - timestamp)
                else:
                    self.countdown(self.countdownTime)
            
            toon = self.cr.doId2do[avId]
            toon.stopSmooth()
            if toon.isDisguised:
                toon.suit.loop('walk')
                animFunc = Func(toon.suit.loop, 'neutral')
            else:
                toon.setAnimState('run', 1.0)
                animFunc = Func(toon.setAnimState, 'neutral', 1.0)
            track = Sequence(LerpPosInterval(toon, TOON_EXIT_ELEVATOR_TIME, Point3(0, -5, 0), other = self.getElevatorModel()), animFunc, Func(self.notifyToonOffElevator, toon), name = toon.uniqueName('emptyElevator'), autoPause = 1)
            track.delayDelete = DelayDelete.DelayDelete(toon)
            track.start()
            if avId == base.localAvatar.getDoId():
                messenger.send('exitElevator')
            
            if avId in self.boardedAvIds:
                del self.boardedAvIds[avId]
            
        else:
            self.notify.warning('toon: ' + str(avId) + " doesn't exist, and" + ' cannot exit the elevator!')

    
    def handleEnterSphere(self, collEntry):
        self.notify.debug('Entering Elevator Sphere....')
        if base.localAvatar.hp > 0:
            self.cr.playGame.getPlace().detectedElevatorCollision(self)
            toon = base.localAvatar
            self.sendUpdate('requestBoard', [
                toon.getX(),
                toon.getY(),
                toon.getZ(),
                toon.getH(),
                toon.getP(),
                toon.getR()])
        

    
    def rejectBoard(self, avId):
        doneStatus = {
            'where': 'reject' }
        elevator = self.getPlaceElevator()
        elevator.signalDone(doneStatus)

    
    def timerTask(self, task):
        countdownTime = int(task.duration - task.time)
        timeStr = str(countdownTime)
        if self.clockNode.getText() != timeStr:
            self.clockNode.setText(timeStr)
        
        if task.time >= task.duration:
            return Task.done
        else:
            return Task.cont

    
    def countdown(self, duration):
        countdownTask = Task.Task(self.timerTask)
        countdownTask.duration = duration
        taskMgr.remove(self.uniqueName('elevatorTimerTask'))
        return taskMgr.add(countdownTask, self.uniqueName('elevatorTimerTask'))

    
    def handleExitButton(self):
        self.sendUpdate('requestExit')

    
    def enterWaitCountdown(self, ts):
        self.elevatorSphereNodePath.unstash()
        self.accept(self.uniqueName('enterelevatorSphere'), self.handleEnterSphere)
        self.accept('elevatorExitButton', self.handleExitButton)
        return None

    
    def exitWaitCountdown(self):
        self.elevatorSphereNodePath.stash()
        self.ignore(self.uniqueName('enterelevatorSphere'))
        self.ignore('elevatorExitButton')
        self.ignore('localToonLeft')
        taskMgr.remove(self.uniqueName('elevatorTimerTask'))
        self.clock.removeNode()
        del self.clock
        del self.clockNode

    
    def enterClosing(self, ts):
        if self.localToonOnBoard:
            elevator = self.getPlaceElevator()
            elevator.fsm.request('elevatorClosing')
        
        self.closeDoors.start(ts)

    
    def exitClosing(self):
        return None

    
    def onDoorCloseFinish(self):
        for avId in self.boardedAvIds.keys():
            av = self.cr.doId2do.get(avId)
            if av is not None:
                if av.getParent().compareTo(self.getElevatorModel()) == 0:
                    av.detachNode()
                
            
        
        self.boardedAvIds = { }

    
    def enterClosed(self, ts):
        self.forceDoorsClosed()
        self._DistributedElevator__doorsClosed(self.getZoneId())
        return None

    
    def exitClosed(self):
        return None

    
    def forceDoorsOpen(self):
        openDoors(self.leftDoor, self.rightDoor)

    
    def forceDoorsClosed(self):
        self.closeDoors.finish()
        closeDoors(self.leftDoor, self.rightDoor)

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterWaitEmpty(self, ts):
        return None

    
    def exitWaitEmpty(self):
        return None

    
    def enterOpening(self, ts):
        self.openDoors.start(ts)
        return None

    
    def exitOpening(self):
        return None

    
    def startCountdownClock(self, countdownTime, ts):
        self.clockNode = TextNode('elevatorClock')
        self.clockNode.setFont(ToontownGlobals.getSignFont())
        self.clockNode.setAlign(TextNode.ACenter)
        self.clockNode.setTextColor(0.5, 0.5, 0.5, 1)
        self.clockNode.setText(str(int(countdownTime)))
        self.clock = self.getElevatorModel().attachNewNode(self.clockNode)
        self.clock.setPosHprScale(0, 4.4000000000000004, 6.0, 0, 0, 0, 2.0, 2.0, 2.0)
        if ts < countdownTime:
            self.countdown(countdownTime - ts)
        

    
    def _DistributedElevator__doorsClosed(self, zoneId):
        if self.localToonOnBoard:
            hoodId = ZoneUtil.getHoodId(zoneId)
            doneStatus = {
                'loader': 'suitInterior',
                'where': 'suitInterior',
                'hoodId': hoodId,
                'zoneId': zoneId,
                'shardId': None }
            elevator = self.getPlaceElevator()
            elevator.signalDone(doneStatus)
        

    
    def getElevatorModel(self):
        self.notify.error('getElevatorModel: pure virtual -- inheritors must override')

    
    def getPlaceElevator(self):
        place = self.cr.playGame.getPlace()
        if not hasattr(place, 'elevator'):
            self.notify.warning("Place was in state '%s' instead of Elevator." % place.fsm.getCurrentState().getName())
            place.detectedElevatorCollision(self)
        
        return place.elevator


