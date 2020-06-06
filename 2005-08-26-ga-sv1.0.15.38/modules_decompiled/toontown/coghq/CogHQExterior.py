# File: C (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from toontown.battle import BattlePlace
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import *

class CogHQExterior(BattlePlace.BattlePlace):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogHQExterior')
    
    def __init__(self, loader, parentFSM, doneEvent):
        BattlePlace.BattlePlace.__init__(self, loader, doneEvent)
        self.parentFSM = parentFSM
        self.fsm = ClassicFSM.ClassicFSM('CogHQExterior', [
            State.State('start', self.enterStart, self.exitStart, [
                'walk',
                'tunnelIn',
                'teleportIn',
                'doorIn']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'stickerBook',
                'teleportOut',
                'tunnelOut',
                'DFA',
                'doorOut',
                'died',
                'WaitForBattle',
                'battle',
                'squished']),
            State.State('doorIn', self.enterDoorIn, self.exitDoorIn, [
                'walk']),
            State.State('doorOut', self.enterDoorOut, self.exitDoorOut, [
                'walk']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk',
                'DFA',
                'WaitForBattle',
                'battle',
                'tunnelOut',
                'doorOut',
                'squished',
                'died']),
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
            State.State('squished', self.enterSquished, self.exitSquished, [
                'walk',
                'died',
                'teleportOut']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk',
                'WaitForBattle',
                'battle']),
            State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, [
                'teleportIn',
                'final',
                'WaitForBattle']),
            State.State('died', self.enterDied, self.exitDied, [
                'quietZone']),
            State.State('tunnelIn', self.enterTunnelIn, self.exitTunnelIn, [
                'walk',
                'WaitForBattle',
                'battle']),
            State.State('tunnelOut', self.enterTunnelOut, self.exitTunnelOut, [
                'final']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')

    
    def load(self):
        self.parentFSM.getStateNamed('cogHQExterior').addChild(self.fsm)
        BattlePlace.BattlePlace.load(self)

    
    def unload(self):
        self.parentFSM.getStateNamed('cogHQExterior').removeChild(self.fsm)
        del self.fsm
        BattlePlace.BattlePlace.unload(self)

    
    def enter(self, requestStatus):
        self.zoneId = requestStatus['zoneId']
        BattlePlace.BattlePlace.enter(self)
        self.fsm.enterInitialState()
        base.playMusic(self.loader.music, looping = 1, volume = 0.80000000000000004)
        self.loader.geom.reparentTo(render)
        self.nodeList = [
            self.loader.geom]
        self.accept('doorDoneEvent', self.handleDoorDoneEvent)
        self.accept('DistributedDoor_doorTrigger', self.handleDoorTrigger)
        NametagGlobals.setMasterArrowsOn(1)
        self.tunnelOriginList = base.cr.hoodMgr.addLinkTunnelHooks(self, self.nodeList, self.zoneId)
        how = requestStatus['how']
        self.fsm.request(how, [
            requestStatus])

    
    def exit(self):
        self.fsm.requestFinalState()
        self.loader.music.stop()
        for node in self.tunnelOriginList:
            node.removeNode()
        
        del self.tunnelOriginList
        if self.loader.geom:
            self.loader.geom.reparentTo(hidden)
        
        self.ignoreAll()
        BattlePlace.BattlePlace.exit(self)

    
    def enterTunnelOut(self, requestStatus):
        fromZoneId = self.zoneId - self.zoneId % 100
        tunnelName = base.cr.hoodMgr.makeLinkTunnelName(self.loader.hood.id, fromZoneId)
        requestStatus['tunnelName'] = tunnelName
        BattlePlace.BattlePlace.enterTunnelOut(self, requestStatus)

    
    def enterTeleportIn(self, requestStatus):
        (x, y, z, h, p, r) = base.cr.hoodMgr.getPlaygroundCenterFromId(self.loader.hood.id)
        base.localAvatar.setPosHpr(render, x, y, z, h, p, r)
        BattlePlace.BattlePlace.enterTeleportIn(self, requestStatus)

    
    def enterTeleportOut(self, requestStatus):
        if requestStatus.has_key('battle'):
            self._CogHQExterior__teleportOutDone(requestStatus)
        else:
            BattlePlace.BattlePlace.enterTeleportOut(self, requestStatus, self._CogHQExterior__teleportOutDone)

    
    def _CogHQExterior__teleportOutDone(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        avId = requestStatus['avId']
        shardId = requestStatus['shardId']
        if hoodId == self.loader.hood.hoodId and zoneId == self.loader.hood.hoodId and shardId == None:
            self.fsm.request('teleportIn', [
                requestStatus])
        elif hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    
    def exitTeleportOut(self):
        BattlePlace.BattlePlace.exitTeleportOut(self)

    
    def enterSquished(self):
        base.localAvatar.laffMeter.start()
        base.localAvatar.b_setAnimState('Squish')
        taskMgr.doMethodLater(2.0, self.handleSquishDone, base.localAvatar.uniqueName('finishSquishTask'))

    
    def handleSquishDone(self, extraArgs = []):
        base.cr.playGame.getPlace().setState('walk')

    
    def exitSquished(self):
        taskMgr.remove(base.localAvatar.uniqueName('finishSquishTask'))
        base.localAvatar.laffMeter.stop()


