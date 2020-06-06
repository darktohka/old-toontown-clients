# File: F (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from toontown.battle import BattlePlace
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.toonbase import ToontownGlobals
from toontown.building import Elevator
from pandac.PandaModules import *

class FactoryExterior(BattlePlace.BattlePlace):
    notify = DirectNotifyGlobal.directNotify.newCategory('FactoryExterior')
    
    def __init__(self, loader, parentFSM, doneEvent):
        BattlePlace.BattlePlace.__init__(self, loader, doneEvent)
        self.parentFSM = parentFSM
        self.elevatorDoneEvent = 'elevatorDone'
        self.fsm = ClassicFSM.ClassicFSM('FactoryExterior', [
            State.State('start', self.enterStart, self.exitStart, [
                'walk',
                'tunnelIn',
                'teleportIn']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'stickerBook',
                'teleportOut',
                'tunnelOut',
                'DFA',
                'elevator',
                'WaitForBattle',
                'battle']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk',
                'DFA',
                'WaitForBattle',
                'battle']),
            State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, [
                'battle',
                'walk']),
            State.State('battle', self.enterBattle, self.exitBattle, [
                'walk',
                'teleportOut',
                'died']),
            State.State('DFA', self.enterDFA, self.exitDFA, [
                'DFAReject',
                'teleportOut',
                'tunnelOut']),
            State.State('DFAReject', self.enterDFAReject, self.exitDFAReject, [
                'walk']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk']),
            State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, [
                'teleportIn',
                'final',
                'WaitForBattle']),
            State.State('died', self.enterDied, self.exitDied, [
                'quietZone']),
            State.State('tunnelIn', self.enterTunnelIn, self.exitTunnelIn, [
                'walk']),
            State.State('tunnelOut', self.enterTunnelOut, self.exitTunnelOut, [
                'final']),
            State.State('elevator', self.enterElevator, self.exitElevator, [
                'walk']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')

    
    def load(self):
        self.parentFSM.getStateNamed('factoryExterior').addChild(self.fsm)
        BattlePlace.BattlePlace.load(self)

    
    def unload(self):
        self.parentFSM.getStateNamed('factoryExterior').removeChild(self.fsm)
        BattlePlace.BattlePlace.unload(self)

    
    def enter(self, requestStatus):
        self.zoneId = requestStatus['zoneId']
        BattlePlace.BattlePlace.enter(self)
        self.fsm.enterInitialState()
        base.playMusic(self.loader.music, looping = 1, volume = 0.80000000000000004)
        self.loader.geom.reparentTo(render)
        self.nodeList = [
            self.loader.geom]
        self.loader.hood.startSky()
        NametagGlobals.setMasterArrowsOn(1)
        self.tunnelOriginList = base.cr.hoodMgr.addLinkTunnelHooks(self, self.nodeList, self.zoneId)
        how = requestStatus['how']
        self.fsm.request(how, [
            requestStatus])

    
    def exit(self):
        self.loader.hood.stopSky()
        self.fsm.requestFinalState()
        self.loader.music.stop()
        for node in self.tunnelOriginList:
            node.removeNode()
        
        del self.tunnelOriginList
        del self.nodeList
        self.ignoreAll()
        BattlePlace.BattlePlace.exit(self)

    
    def enterTunnelOut(self, requestStatus):
        fromZoneId = self.zoneId - self.zoneId % 100
        tunnelName = base.cr.hoodMgr.makeLinkTunnelName(self.loader.hood.id, fromZoneId)
        requestStatus['tunnelName'] = tunnelName
        BattlePlace.BattlePlace.enterTunnelOut(self, requestStatus)

    
    def enterTeleportIn(self, requestStatus):
        base.localAvatar.setPosHpr(-34, -350, 0, -28, 0, 0)
        BattlePlace.BattlePlace.enterTeleportIn(self, requestStatus)

    
    def enterTeleportOut(self, requestStatus):
        BattlePlace.BattlePlace.enterTeleportOut(self, requestStatus, self._FactoryExterior__teleportOutDone)

    
    def _FactoryExterior__teleportOutDone(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        avId = requestStatus['avId']
        shardId = requestStatus['shardId']
        if hoodId == self.loader.hood.hoodId and zoneId == self.zoneId and shardId == None:
            self.fsm.request('teleportIn', [
                requestStatus])
        elif hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    
    def exitTeleportOut(self):
        BattlePlace.BattlePlace.exitTeleportOut(self)

    
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
        elif where == 'factoryInterior':
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
        else:
            self.notify.error('Unknown mode: ' + where + ' in handleElevatorDone')


