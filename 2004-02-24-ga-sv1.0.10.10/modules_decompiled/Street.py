# File: S (Python 2.2)

from ShowBaseGlobal import *
from BattleProps import *
from BattleSounds import *
from ToontownMsgTypes import *
from DirectGui import cleanupDialog
import DirectNotifyGlobal
import Place
import BattlePlace
import PandaObject
import StateData
import FSM
import State
import Task
import BattleParticles
import Elevator
import ZoneUtil
import ToontownGlobals
import HouseGlobals
import Localizer
from IntervalGlobal import *
visualizeZones = base.config.GetBool('visualize-zones', 0)

class Street(BattlePlace.BattlePlace):
    notify = DirectNotifyGlobal.directNotify.newCategory('Street')
    
    def __init__(self, loader, parentFSM, doneEvent):
        BattlePlace.BattlePlace.__init__(self, loader, doneEvent)
        self.fsm = FSM.FSM('Street', [
            State.State('start', self.enterStart, self.exitStart, [
                'walk',
                'tunnelIn',
                'doorIn',
                'teleportIn',
                'elevatorIn']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'push',
                'sit',
                'stickerBook',
                'WaitForBattle',
                'battle',
                'DFA',
                'doorOut',
                'elevator',
                'tunnelIn',
                'tunnelOut',
                'teleportOut',
                'quest',
                'phone',
                'fishing']),
            State.State('sit', self.enterSit, self.exitSit, [
                'walk']),
            State.State('push', self.enterPush, self.exitPush, [
                'walk']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk',
                'battle',
                'DFA',
                'WaitForBattle']),
            State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, [
                'battle',
                'walk']),
            State.State('battle', self.enterBattle, self.exitBattle, [
                'walk',
                'teleportOut',
                'died']),
            State.State('doorIn', self.enterDoorIn, self.exitDoorIn, [
                'walk']),
            State.State('doorOut', self.enterDoorOut, self.exitDoorOut, [
                'walk']),
            State.State('elevatorIn', self.enterElevatorIn, self.exitElevatorIn, [
                'walk']),
            State.State('elevator', self.enterElevator, self.exitElevator, [
                'walk']),
            State.State('DFA', self.enterDFA, self.exitDFA, [
                'DFAReject',
                'teleportOut',
                'tunnelOut']),
            State.State('DFAReject', self.enterDFAReject, self.exitDFAReject, [
                'walk']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk',
                'teleportOut',
                'quietZone',
                'WaitForBattle',
                'battle']),
            State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, [
                'teleportIn',
                'quietZone',
                'WaitForBattle']),
            State.State('died', self.enterDied, self.exitDied, [
                'quietZone']),
            State.State('tunnelIn', self.enterTunnelIn, self.exitTunnelIn, [
                'walk']),
            State.State('tunnelOut', self.enterTunnelOut, self.exitTunnelOut, [
                'final']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'teleportIn']),
            State.State('quest', self.enterQuest, self.exitQuest, [
                'walk']),
            State.State('phone', self.enterPhone, self.exitPhone, [
                'walk']),
            State.State('fishing', self.enterFishing, self.exitFishing, [
                'walk']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.parentFSM = parentFSM
        self.tunnelOriginList = []
        self.elevatorDoneEvent = 'elevatorDone'

    
    def enter(self, requestStatus, visibilityFlag = 1, arrowsOn = 1):
        self.fsm.enterInitialState()
        base.playMusic(self.loader.music, looping = 1, volume = 0.80000000000000004)
        self.loader.geom.reparentTo(render)
        if visibilityFlag:
            self.visibilityOn()
        
        toonbase.localToon.setGeom(self.loader.geom)
        toonbase.localToon.setOnLevelGround(1)
        NametagGlobals.setMasterArrowsOn(arrowsOn)
        self.loader.hood.startSky()
        self.accept('doorDoneEvent', self.handleDoorDoneEvent)
        self.accept('DistributedDoor_doorTrigger', self.handleDoorTrigger)
        self.enterZone(requestStatus['zoneId'])
        self.tunnelOriginList = toonbase.tcr.hoodMgr.addLinkTunnelHooks(self, self.loader.nodeList, self.zoneId)
        self.fsm.request(requestStatus['how'], [
            requestStatus])

    
    def exit(self, visibilityFlag = 1):
        if visibilityFlag:
            self.visibilityOff()
        
        self.loader.geom.reparentTo(hidden)
        for node in self.tunnelOriginList:
            node.removeNode()
        
        del self.tunnelOriginList
        NametagGlobals.setMasterArrowsOn(0)
        self.loader.hood.stopSky()
        self.loader.music.stop()
        toonbase.localToon.setGeom(render)
        toonbase.localToon.setOnLevelGround(0)

    
    def load(self):
        BattlePlace.BattlePlace.load(self)
        self.parentFSM.getStateNamed('street').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('street').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.enterZone(None)
        cleanupDialog('globalDialog')
        self.ignoreAll()
        BattlePlace.BattlePlace.unload(self)

    
    def enterElevatorIn(self, requestStatus):
        bldg = toonbase.tcr.doId2do.get(requestStatus['bldgDoId'])
        messenger.send('insideVictorElevator')

    
    def exitElevatorIn(self):
        pass

    
    def enterElevator(self, distElevator):
        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm.getStateNamed('elevator'), self.elevatorDoneEvent, distElevator)
        self.elevator.load()
        self.elevator.enter()
        return None

    
    def exitElevator(self):
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        del self.elevator
        return None

    
    def detectedElevatorCollision(self, distElevator):
        self.fsm.request('elevator', [
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
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
        else:
            self.notify.error('Unknown mode: ' + where + ' in handleElevatorDone')

    
    def enterTunnelIn(self, requestStatus):
        self.enterZone(requestStatus['zoneId'])
        BattlePlace.BattlePlace.enterTunnelIn(self, requestStatus)

    
    def enterTeleportIn(self, requestStatus):
        avId = requestStatus['avId']
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        if avId != -1:
            if not toonbase.tcr.doId2do.has_key(avId):
                handle = toonbase.tcr.identifyFriend(avId)
                requestStatus = {
                    'how': 'teleportIn',
                    'hoodId': hoodId,
                    'zoneId': hoodId,
                    'shardId': None,
                    'loader': 'safeZoneLoader',
                    'where': 'playground',
                    'avId': avId }
                self.fsm.request('final')
                self._Street__teleportOutDone(requestStatus)
                return None
            
        
        self.enterZone(zoneId)
        BattlePlace.BattlePlace.enterTeleportIn(self, requestStatus)
        return None

    
    def enterTeleportOut(self, requestStatus):
        if requestStatus.has_key('battle'):
            self._Street__teleportOutDone(requestStatus)
        else:
            BattlePlace.BattlePlace.enterTeleportOut(self, requestStatus, self._Street__teleportOutDone)

    
    def _Street__teleportOutDone(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        shardId = requestStatus['shardId']
        if hoodId == self.loader.hood.id and shardId == None:
            if zoneId == self.zoneId:
                self.fsm.request('teleportIn', [
                    requestStatus])
            elif requestStatus['where'] == 'street' and ZoneUtil.getBranchZone(zoneId) == self.loader.branchZone:
                self.fsm.request('quietZone', [
                    requestStatus])
            else:
                self.doneStatus = requestStatus
                messenger.send(self.doneEvent)
        elif hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    
    def exitTeleportOut(self):
        BattlePlace.BattlePlace.exitTeleportOut(self)

    
    def goHomeFailed(self, task):
        self.notifyUserGoHomeFailed()
        self.ignore('setLocalEstateZone')
        self.doneStatus['avId'] = -1
        self.doneStatus['zoneId'] = self.getZoneId()
        self.fsm.request('teleportIn', [
            self.doneStatus])
        return Task.done

    
    def renameFloorPolys(self, nodeList):
        for i in nodeList:
            collNodePaths = i.findAllMatches('**/+CollisionNode')
            numCollNodePaths = collNodePaths.getNumPaths()
            visGroupName = i.node().getName()
            for j in range(numCollNodePaths):
                collNodePath = collNodePaths.getPath(j)
                bitMask = collNodePath.node().getIntoCollideMask()
                if bitMask.getBit(1):
                    collNodePath.node().setName(visGroupName)
                
            
        

    
    def hideAllVisibles(self):
        for i in self.loader.nodeList:
            i.stash()
        

    
    def showAllVisibles(self):
        for i in self.loader.nodeList:
            i.unstash()
        

    
    def visibilityOn(self):
        self.hideAllVisibles()
        self.accept('on-floor', self.enterZone)

    
    def visibilityOff(self):
        self.ignore('on-floor')
        self.showAllVisibles()

    
    def doEnterZone(self, newZoneId):
        if self.zoneId != None:
            for i in self.loader.nodeDict[self.zoneId]:
                if newZoneId:
                    if i not in self.loader.nodeDict[newZoneId]:
                        self.loader.fadeOutDict[i].start()
                        self.loader.exitAnimatedProps(i)
                    
                else:
                    i.stash()
                    self.loader.exitAnimatedProps(i)
            
        
        if newZoneId != None:
            for i in self.loader.nodeDict[newZoneId]:
                if self.zoneId:
                    if i not in self.loader.nodeDict[self.zoneId]:
                        self.loader.fadeInDict[i].start()
                        self.loader.enterAnimatedProps(i)
                    
                elif self.loader.fadeOutDict[i].isPlaying():
                    self.loader.fadeOutDict[i].finish()
                
                if self.loader.fadeInDict[i].isPlaying():
                    self.loader.fadeInDict[i].finish()
                
                self.loader.enterAnimatedProps(i)
                i.unstash()
            
        
        if newZoneId != self.zoneId:
            if visualizeZones:
                if self.zoneId != None:
                    self.loader.zoneDict[self.zoneId].clearColor()
                
                if newZoneId != None:
                    self.loader.zoneDict[newZoneId].setColor(0, 0, 1, 1, 100)
                
            
            if newZoneId != None:
                toonbase.tcr.sendSetZoneMsg(newZoneId)
                self.notify.debug('Entering Zone %d' % newZoneId)
            
            self.zoneId = newZoneId
        


