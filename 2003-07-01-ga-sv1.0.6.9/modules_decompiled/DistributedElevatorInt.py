# File: D (Python 2.2)

from ShowBaseGlobal import *
from PandaObject import *
from ClockDelta import *
from IntervalGlobal import *
from ElevatorConstants import *
from ElevatorUtils import *
from ToontownGlobals import *
import DistributedObject
import DirectNotifyGlobal
import FSM
import State
import NodePath
import CollisionSphere
import CollisionNode
import ZoneUtil
import DelayDelete

class DistributedElevatorInt(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedElevatorInt')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.localToonOnBoard = 0
        self.openSfx = base.loadSfx('phase_5/audio/sfx/elevator_door_open.mp3')
        self.closeSfx = base.loadSfx('phase_5/audio/sfx/elevator_door_close.mp3')
        self.fsm = FSM.FSM('DistributedElevatorInt', [
            State.State('off', self.enterOff, self.exitOff, [
                'opening',
                'waitCountdown',
                'closing',
                'closed']),
            State.State('opening', self.enterOpening, self.exitOpening, [
                'waitCountdown']),
            State.State('waitCountdown', self.enterWaitCountdown, self.exitWaitCountdown, [
                'closing']),
            State.State('closing', self.enterClosing, self.exitClosing, [
                'closed']),
            State.State('closed', self.enterClosed, self.exitClosed, [
                'opening'])], 'off', 'off')
        self.fsm.enterInitialState()
        return None

    
    def generate(self):
        return None

    
    def setupElevator(self, suitInterior):
        self.elevatorModel = suitInterior.elevatorModelOut
        self.leftDoor = suitInterior.leftDoorOut
        self.rightDoor = suitInterior.rightDoorOut
        self.elevatorSphere = CollisionSphere.CollisionSphere(0, 5, 0, 5)
        self.elevatorSphere.setTangible(0)
        self.elevatorSphereNode = CollisionNode.CollisionNode(self.uniqueName('elevatorSphere'))
        self.elevatorSphereNode.setIntoCollideMask(WallBitmask)
        self.elevatorSphereNode.addSolid(self.elevatorSphere)
        self.elevatorSphereNodePath = self.elevatorModel.attachNewNode(self.elevatorSphereNode)
        self.elevatorSphereNodePath.hide()
        self.elevatorSphereNodePath.reparentTo(self.elevatorModel)
        self.elevatorSphereNodePath.stash()
        self.openDoors = getOpenInterval(self, self.leftDoor, self.rightDoor, self.openSfx)
        self.closeDoors = getCloseInterval(self, self.leftDoor, self.rightDoor, self.closeSfx)
        return None

    
    def disable(self):
        DistributedObject.DistributedObject.disable(self)
        self.fsm.request('off')
        return None

    
    def delete(self):
        self.elevatorSphereNodePath.removeNode()
        del self.elevatorSphere
        del self.elevatorSphereNode
        del self.elevatorSphereNodePath
        del self.suitInterior
        del self.elevatorModel
        del self.leftDoor
        del self.rightDoor
        del self.openDoors
        del self.closeDoors
        del self.fsm
        del self.openSfx
        del self.closeSfx
        DistributedObject.DistributedObject.delete(self)
        return None

    
    def setSuitInteriorDoId(self, suitInteriorDoId):
        self.suitInteriorDoId = suitInteriorDoId
        self.suitInterior = self.cr.doId2do[suitInteriorDoId]
        self.setupElevator(self.suitInterior)
        return None

    
    def setState(self, state, timestamp):
        self.fsm.request(state, [
            globalClockDelta.localElapsedTime(timestamp)])
        return None

    
    def handleEnterSphere(self, collEntry):
        self.notify.debug('Entering Elevator Sphere....')
        self.cr.playGame.getPlace().detectedElevatorCollision(self)
        if toonbase.localToon.hp > 0:
            toon = toonbase.localToon
            self.sendUpdate('requestBoard', [
                toon.getX(),
                toon.getY(),
                toon.getZ(),
                toon.getH(),
                toon.getP(),
                toon.getR()])
            return None
        

    
    def fillSlot0(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(0, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot1(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(1, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot2(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(2, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot3(self, avId, x, y, z, h, p, r, timestamp):
        self.fillSlot(3, avId, x, y, z, h, p, r, timestamp)

    
    def fillSlot(self, index, avId, x, y, z, h, p, r, timestamp):
        if avId == 0:
            pass
        1
        if avId == toonbase.localToon.getDoId():
            self.cr.playGame.getPlace().elevator.fsm.request('boarding', [
                self.elevatorModel])
            self.localToonOnBoard = 1
        
        if avId == toonbase.localToon.getDoId():
            self.cr.playGame.getPlace().elevator.fsm.request('boarded')
        
        if self.cr.doId2do.has_key(avId):
            toon = self.cr.doId2do[avId]
            toon.stopSmooth()
            toon.wrtReparentTo(self.elevatorModel)
            toon.setAnimState('run', 1.0)
            toon.headsUp(apply(Point3, ElevatorPoints[index]))
            track = Sequence(LerpPosInterval(toon, TOON_BOARD_ELEVATOR_TIME * 0.75, apply(Point3, ElevatorPoints[index])), LerpHprInterval(toon, TOON_BOARD_ELEVATOR_TIME * 0.25, Point3(180, 0, 0)), Func(toon.setAnimState, 'neutral', 1.0), name = toon.uniqueName('fillElevatorInt'), autoPause = 1)
            track.delayDelete = DelayDelete.DelayDelete(toon)
            track.start()
        else:
            self.notify.warning('toon: ' + str(avId) + " doesn't exist, and" + ' cannot board the elevator!')
        return None

    
    def emptySlot0(self, avId, bailFlag, timestamp):
        self.emptySlot(0, avId, timestamp)

    
    def emptySlot1(self, avId, bailFlag, timestamp):
        self.emptySlot(1, avId, timestamp)

    
    def emptySlot2(self, avId, bailFlag, timestamp):
        self.emptySlot(2, avId, timestamp)

    
    def emptySlot3(self, avId, bailFlag, timestamp):
        self.emptySlot(3, avId, timestamp)

    
    def notifyToonOffElevator(self, toon):
        toon.setAnimState('neutral', 1.0)
        if toon == toonbase.localToon:
            doneStatus = {
                'where': 'exit' }
            self.cr.playGame.getPlace().elevator.signalDone(doneStatus)
            self.localToonOnBoard = 0
        else:
            toon.startSmooth()
        return None

    
    def emptySlot(self, index, avId, timestamp):
        if avId == 0:
            pass
        1
        if self.cr.doId2do.has_key(avId):
            toon = self.cr.doId2do[avId]
            toon.wrtReparentTo(render)
            toon.stopSmooth()
            toon.setAnimState('run', 1.0)
            track = Sequence(LerpPosInterval(toon, TOON_EXIT_ELEVATOR_TIME, Point3(0, -5, 0), other = self.elevatorModel), Func(toon.animFSM.request, 'neutral'), Func(self.notifyToonOffElevator, toon), name = toon.uniqueName('emptyElevatorInt'), autoPause = 1)
            track.delayDelete = DelayDelete.DelayDelete(toon)
            track.start()
            if avId == toonbase.localToon.getDoId():
                messenger.send('exitElevator')
            
        else:
            self.notify.warning('toon: ' + str(avId) + " doesn't exist, and" + ' cannot exit the elevator!')
        return None

    
    def rejectBoard(self, avId):
        doneStatus = {
            'where': 'reject' }
        self.cr.playGame.getPlace().elevator.signalDone(doneStatus)
        return None

    
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

    
    def forceDoorsOpen(self):
        self.leftDoor.setPos(OPEN_POS_LEFT)
        self.rightDoor.setPos(OPEN_POS_RIGHT)

    
    def forceDoorsClosed(self):
        self.closeDoors.finish()
        self.leftDoor.setPos(CLOSED_POS_LEFT)
        self.rightDoor.setPos(CLOSED_POS_RIGHT)

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterOpening(self, ts):
        self.openDoors.start()
        return None

    
    def exitOpening(self):
        return None

    
    def enterWaitCountdown(self, ts):
        self.elevatorSphereNodePath.unstash()
        countdownTime = base.config.GetFloat('int-elevator-timeout', INTERIOR_ELEVATOR_COUNTDOWN_TIME)
        self.accept(self.uniqueName('enterelevatorSphere'), self.handleEnterSphere)
        self.accept('elevatorExitButton', self.handleExitButton)
        self.acceptOnce('localToonLeft', self._DistributedElevatorInt__handleTeleportOut)
        self.clockNode = TextNode('elevatorClock')
        self.clockNode.setFont(getSignFont())
        self.clockNode.setAlign(TextNode.ACenter)
        self.clockNode.setTextColor(0.5, 0.5, 0.5, 1)
        self.clockNode.setText(str(countdownTime))
        self.clock = self.elevatorModel.attachNewNode(self.clockNode)
        self.clock.setPosHprScale(0, 6.4000000000000004, 6.0, 0, 0, 0, 2.0, 2.0, 2.0)
        print ts
        if ts < countdownTime:
            self.countdown(countdownTime - ts)
        
        return None

    
    def _DistributedElevatorInt__handleTeleportOut(self):
        self.sendUpdate('requestBuildingExit', [])
        return None

    
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
        taskMgr.remove('elevatorTimerTask')
        return taskMgr.add(countdownTask, 'elevatorTimerTask')

    
    def handleExitButton(self):
        self.sendUpdate('requestExit')
        return None

    
    def exitWaitCountdown(self):
        self.elevatorSphereNodePath.stash()
        self.ignore(self.uniqueName('enterelevatorSphere'))
        self.ignore('elevatorExitButton')
        self.ignore('localToonLeft')
        taskMgr.remove('elevatorTimerTask')
        self.clock.removeNode()
        del self.clock
        del self.clockNode
        return None

    
    def enterClosing(self, ts):
        if self.localToonOnBoard:
            self.cr.playGame.getPlace().elevator.fsm.request('elevatorClosing')
        
        self.closeDoors.start(ts)
        return None

    
    def exitClosing(self):
        return None

    
    def _DistributedElevatorInt__doorsClosed(self):
        if self.localToonOnBoard:
            zoneId = self.suitInterior.getZoneId()
            hoodId = ZoneUtil.getHoodId(zoneId)
            doneStatus = {
                'loader': 'suitInterior',
                'where': 'suitInterior',
                'hoodId': hoodId,
                'zoneId': zoneId,
                'shardId': None }
            self.cr.playGame.getPlace().elevator.signalDone(doneStatus)
        

    
    def enterClosed(self, ts):
        self.forceDoorsClosed()
        self._DistributedElevatorInt__doorsClosed()
        return None

    
    def exitClosed(self):
        return None


