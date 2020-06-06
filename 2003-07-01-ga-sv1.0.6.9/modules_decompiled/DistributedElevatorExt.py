# File: D (Python 2.2)

from ShowBaseGlobal import *
from PandaObject import *
from ClockDelta import *
from IntervalGlobal import *
from ElevatorConstants import *
from ElevatorUtils import *
import ToontownGlobals
import DistributedObject
import DirectNotifyGlobal
import FSM
import State
import CollisionSphere
import CollisionNode
import ZoneUtil
import DelayDelete

class DistributedElevatorExt(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedElevatorExt')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.countdownTask = None
        self.localToonOnBoard = 0
        self.openSfx = base.loadSfx('phase_5/audio/sfx/elevator_door_open.mp3')
        self.closeSfx = base.loadSfx('phase_5/audio/sfx/elevator_door_close.mp3')
        self.nametag = None
        self.fsm = FSM.FSM('DistributedElevatorExt', [
            State.State('off', self.enterOff, self.exitOff, [
                'opening',
                'waitEmpty',
                'waitCountdown',
                'closing',
                'closed']),
            State.State('opening', self.enterOpening, self.exitOpening, [
                'waitEmpty']),
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
        self.currentFloor = -1
        self.isSetup = 0
        return None

    
    def generate(self):
        return None

    
    def setupElevator(self, bldg):
        if self.isSetup:
            self.elevatorSphereNodePath.removeNode()
        
        self.bldg = bldg
        self.elevatorSphere = CollisionSphere.CollisionSphere(0, 5, 0, 5)
        self.elevatorSphere.setTangible(0)
        self.elevatorSphereNode = CollisionNode.CollisionNode(self.uniqueName('elevatorSphere'))
        self.elevatorSphereNode.setIntoCollideMask(ToontownGlobals.WallBitmask)
        self.elevatorSphereNode.addSolid(self.elevatorSphere)
        self.elevatorSphereNodePath = self.bldg.getElevatorNodePath().attachNewNode(self.elevatorSphereNode)
        self.elevatorSphereNodePath.hide()
        self.elevatorSphereNodePath.reparentTo(self.bldg.getElevatorNodePath())
        self.elevatorSphereNodePath.stash()
        self.openDoors = getOpenInterval(self, self.bldg.leftDoor, self.bldg.rightDoor, self.openSfx)
        self.closeDoors = getCloseInterval(self, self.bldg.leftDoor, self.bldg.rightDoor, self.closeSfx)
        self.isSetup = 1
        self.setupNametag()
        return None

    
    def disable(self):
        self.clearNametag()
        self.fsm.request('off')
        DistributedObject.DistributedObject.disable(self)
        return None

    
    def delete(self):
        if self.isSetup:
            self.elevatorSphereNodePath.removeNode()
            del self.elevatorSphereNodePath
            del self.elevatorSphereNode
            del self.elevatorSphere
            del self.bldg
            del self.openDoors
            del self.closeDoors
            del self.fsm
        
        del self.countdownTask
        del self.openSfx
        del self.closeSfx
        DistributedObject.DistributedObject.delete(self)
        self.isSetup = 0
        return None

    
    def setupNametag(self):
        if self.nametag == None:
            self.nametag = NametagGroup()
            self.nametag.setFont(ToontownGlobals.getSignFont())
            self.nametag.setContents(Nametag.CName)
            self.nametag.setColorCode(NametagGroup.CCSuitBuilding)
            self.nametag.setActive(0)
            self.nametag.setAvatar(self.bldg.getElevatorNodePath())
            name = self.cr.playGame.dnaStore.getTitleFromBlockNumber(self.bldg.block)
            if name:
                name += ', Inc.'
            else:
                name = 'COGS, Inc.'
            self.nametag.setName(name)
            self.nametag.manage(toonbase.marginManager)
        

    
    def clearNametag(self):
        if self.nametag != None:
            self.nametag.unmanage(toonbase.marginManager)
            self.nametag.setAvatar(NodePath())
            self.nametag = None
        

    
    def setBldgDoId(self, bldgDoId):
        self.bldgDoId = bldgDoId
        self.bldg = self.cr.doId2do[bldgDoId]
        if self.bldg.getSuitDoorOrigin():
            self.bossLevel = self.bldg.getBossLevel()
            self.setupElevator(self.bldg)
        else:
            self.notify.warning('Cannot create elevator %d for toon bldg %d!' % (self.doId, bldgDoId))
        return None

    
    def setFloor(self, floorNumber):
        if self.currentFloor >= 0:
            self.bldg.floorIndicator[self.currentFloor].setColor(LIGHT_OFF_COLOR)
        
        if floorNumber >= 0:
            self.bldg.floorIndicator[floorNumber].setColor(LIGHT_ON_COLOR)
        
        self.currentFloor = floorNumber

    
    def setState(self, state, timestamp):
        if self.isSetup:
            self.fsm.request(state, [
                globalClockDelta.localElapsedTime(timestamp)])
        
        return None

    
    def handleEnterSphere(self, collEntry):
        self.notify.debug('Entering Elevator Sphere....')
        self.cr.playGame.getPlace().detectedElevatorCollision(self)
        return None

    
    def handleEnterElevator(self):
        if toonbase.localToon.hp > 0:
            toon = toonbase.localToon
            self.sendUpdate('requestBoard', [
                toon.getX(),
                toon.getY(),
                toon.getZ(),
                toon.getH(),
                toon.getP(),
                toon.getR()])
        else:
            self.notify.warning('Tried to board elevator with hp: %d' % toonbase.localToon.hp)
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
                self.bldg.getElevatorNodePath()])
            self.localToonOnBoard = 1
        
        if avId == toonbase.localToon.getDoId():
            self.cr.playGame.getPlace().elevator.fsm.request('boarded')
        
        if self.cr.doId2do.has_key(avId):
            toon = self.cr.doId2do[avId]
            toon.stopSmooth()
            toon.wrtReparentTo(self.bldg.getElevatorNodePath())
            toon.setAnimState('run', 1.0)
            toon.headsUp(apply(Point3, ElevatorPoints[index]))
            track = Sequence(LerpPosInterval(toon, TOON_BOARD_ELEVATOR_TIME * 0.75, apply(Point3, ElevatorPoints[index])), LerpHprInterval(toon, TOON_BOARD_ELEVATOR_TIME * 0.25, Point3(180, 0, 0)), Func(toon.setAnimState, 'neutral', 1.0), name = toon.uniqueName('fillElevatorExt'), autoPause = 1)
            track.delayDelete = DelayDelete.DelayDelete(toon)
            track.start()
        else:
            self.notify.warning('toon: ' + str(avId) + " doesn't exist, and" + ' cannot board the elevator!')
        return None

    
    def emptySlot0(self, avId, bailFlag, timestamp):
        self.emptySlot(0, avId, bailFlag, timestamp)

    
    def emptySlot1(self, avId, bailFlag, timestamp):
        self.emptySlot(1, avId, bailFlag, timestamp)

    
    def emptySlot2(self, avId, bailFlag, timestamp):
        self.emptySlot(2, avId, bailFlag, timestamp)

    
    def emptySlot3(self, avId, bailFlag, timestamp):
        self.emptySlot(3, avId, bailFlag, timestamp)

    
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

    
    def emptySlot(self, index, avId, bailFlag, timestamp):
        if avId == 0:
            pass
        1
        if self.cr.doId2do.has_key(avId):
            if bailFlag == 1 and hasattr(self, 'clockNode'):
                if timestamp < ELEVATOR_COUNTDOWN_TIME and timestamp >= 0:
                    self.countdown(ELEVATOR_COUNTDOWN_TIME - timestamp)
                else:
                    self.countdown(ELEVATOR_COUNTDOWN_TIME)
            
            toon = self.cr.doId2do[avId]
            toon.wrtReparentTo(render)
            toon.stopSmooth()
            toon.setAnimState('run', 1.0)
            track = Sequence(LerpPosInterval(toon, TOON_EXIT_ELEVATOR_TIME, Point3(0, -5, 0), other = self.bldg.getElevatorNodePath()), Func(self.notifyToonOffElevator, toon), name = toon.uniqueName('emptyElevatorExt'), autoPause = 1)
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

    
    def forceDoorsOpen(self):
        self.bldg.leftDoor.setPos(OPEN_POS_LEFT)
        self.bldg.rightDoor.setPos(OPEN_POS_RIGHT)

    
    def forceDoorsClosed(self):
        self.closeDoors.finish()
        self.bldg.leftDoor.setPos(CLOSED_POS_LEFT)
        self.bldg.rightDoor.setPos(CLOSED_POS_RIGHT)

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterOpening(self, ts):
        self.openDoors.start(ts)
        return None

    
    def exitOpening(self):
        return None

    
    def enterWaitEmpty(self, ts):
        self.elevatorSphereNodePath.unstash()
        self.forceDoorsOpen()
        self.accept(self.uniqueName('enterelevatorSphere'), self.handleEnterSphere)
        self.accept(self.uniqueName('enterElevatorOK'), self.handleEnterElevator)
        return None

    
    def exitWaitEmpty(self):
        self.elevatorSphereNodePath.stash()
        self.ignore(self.uniqueName('enterelevatorSphere'))
        self.ignore(self.uniqueName('enterElevatorOK'))
        return None

    
    def enterWaitCountdown(self, ts):
        self.elevatorSphereNodePath.unstash()
        self.forceDoorsOpen()
        self.accept(self.uniqueName('enterelevatorSphere'), self.handleEnterSphere)
        self.accept(self.uniqueName('enterElevatorOK'), self.handleEnterElevator)
        self.accept('elevatorExitButton', self.handleExitButton)
        self.clockNode = TextNode('elevatorClock')
        self.clockNode.setFont(ToontownGlobals.getSignFont())
        self.clockNode.setAlign(TextNode.ACenter)
        self.clockNode.setTextColor(0.5, 0.5, 0.5, 1)
        self.clockNode.setText(str(ELEVATOR_COUNTDOWN_TIME))
        self.clock = self.bldg.getElevatorNodePath().attachNewNode(self.clockNode)
        self.clock.setPosHprScale(0, 6.4000000000000004, 6.0, 0, 0, 0, 2.0, 2.0, 2.0)
        if ts < ELEVATOR_COUNTDOWN_TIME:
            self.countdown(ELEVATOR_COUNTDOWN_TIME - ts)
        
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
        self.countdownTask = Task.Task(self.timerTask)
        self.countdownTask.duration = duration
        taskMgr.remove(self.uniqueName('elevatorTimerTask'))
        return taskMgr.add(self.countdownTask, self.uniqueName('elevatorTimerTask'))

    
    def handleExitButton(self):
        self.sendUpdate('requestExit')
        return None

    
    def exitWaitCountdown(self):
        self.elevatorSphereNodePath.stash()
        self.ignore(self.uniqueName('enterelevatorSphere'))
        self.ignore(self.uniqueName('enterElevatorOK'))
        self.ignore('elevatorExitButton')
        taskMgr.remove(self.uniqueName('elevatorTimerTask'))
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

    
    def _DistributedElevatorExt__doorsClosed(self):
        if self.localToonOnBoard:
            zoneId = self.bldg.interiorZoneId
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
        self._DistributedElevatorExt__doorsClosed()
        return None

    
    def exitClosed(self):
        return None


