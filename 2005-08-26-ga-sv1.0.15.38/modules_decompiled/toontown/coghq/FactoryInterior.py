# File: F (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from toontown.battle import BattlePlace
from direct.fsm import ClassicFSM
from direct.fsm import State
from pandac.PandaModules import *
from toontown.toon import Toon
from toontown.toonbase import ToontownGlobals
from toontown.hood import ZoneUtil
from toontown.toonbase import TTLocalizer
from toontown.toontowngui import TTDialog
from toontown.toonbase import ToontownBattleGlobals

class FactoryInterior(BattlePlace.BattlePlace):
    notify = DirectNotifyGlobal.directNotify.newCategory('FactoryInterior')
    
    def __init__(self, loader, parentFSM, doneEvent):
        BattlePlace.BattlePlace.__init__(self, loader, doneEvent)
        self.parentFSM = parentFSM
        self.zoneId = ToontownGlobals.SellbotFactoryInt
        self.fsm = ClassicFSM.ClassicFSM('FactoryInterior', [
            State.State('start', self.enterStart, self.exitStart, [
                'walk',
                'teleportIn',
                'fallDown']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'push',
                'sit',
                'stickerBook',
                'WaitForBattle',
                'battle',
                'died',
                'teleportOut',
                'squished',
                'DFA',
                'fallDown']),
            State.State('sit', self.enterSit, self.exitSit, [
                'walk',
                'died',
                'teleportOut']),
            State.State('push', self.enterPush, self.exitPush, [
                'walk',
                'died',
                'teleportOut']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk',
                'battle',
                'DFA',
                'WaitForBattle',
                'died',
                'teleportOut']),
            State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, [
                'battle',
                'walk',
                'died',
                'teleportOut']),
            State.State('battle', self.enterBattle, self.exitBattle, [
                'walk',
                'teleportOut',
                'died']),
            State.State('fallDown', self.enterFallDown, self.exitFallDown, [
                'walk',
                'died',
                'teleportOut']),
            State.State('squished', self.enterSquished, self.exitSquished, [
                'walk',
                'died',
                'teleportOut']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk',
                'teleportOut',
                'quietZone',
                'died']),
            State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, [
                'teleportIn',
                'FLA',
                'quietZone',
                'WaitForBattle']),
            State.State('DFA', self.enterDFA, self.exitDFA, [
                'DFAReject',
                'teleportOut']),
            State.State('DFAReject', self.enterDFAReject, self.exitDFAReject, [
                'walkteleportOut']),
            State.State('died', self.enterDied, self.exitDied, [
                'teleportOut']),
            State.State('FLA', self.enterFLA, self.exitFLA, [
                'quietZone']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'teleportIn']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')

    
    def load(self):
        self.parentFSM.getStateNamed('factoryInterior').addChild(self.fsm)
        BattlePlace.BattlePlace.load(self)
        self.music = base.loadMusic('phase_9/audio/bgm/CHQ_FACT_bg.mid')

    
    def unload(self):
        self.parentFSM.getStateNamed('factoryInterior').removeChild(self.fsm)
        del self.music
        BattlePlace.BattlePlace.unload(self)

    
    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        base.transitions.fadeOut(t = 0)
        base.localAvatar.inventory.setRespectInvasions(0)
        
        def commence(self = self):
            NametagGlobals.setMasterArrowsOn(1)
            self.fsm.request(requestStatus['how'], [
                requestStatus])
            base.playMusic(self.music, looping = 1, volume = 0.80000000000000004)
            base.transitions.irisIn()

        if hasattr(base, 'factoryReady'):
            commence()
        else:
            self.acceptOnce('FactoryReady', commence)
        self.factoryDefeated = 0
        self.acceptOnce('FactoryWinEvent', self.handleFactoryWinEvent)
        if __debug__ and 0:
            self.accept('f10', lambda : messenger.send('FactoryWinEvent'))
        
        self.confrontedForeman = 0
        
        def handleConfrontedForeman(self = self):
            self.confrontedForeman = 1

        self.acceptOnce('localToonConfrontedForeman', handleConfrontedForeman)

    
    def exit(self):
        NametagGlobals.setMasterArrowsOn(0)
        if hasattr(base, 'factoryReady'):
            del base.factoryReady
        
        base.localAvatar.inventory.setRespectInvasions(1)
        self.fsm.requestFinalState()
        self.loader.music.stop()
        self.music.stop()
        self.ignoreAll()

    
    def enterWalk(self, teleportIn = 0):
        BattlePlace.BattlePlace.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    
    def enterPush(self):
        BattlePlace.BattlePlace.enterPush(self)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    
    def enterWaitForBattle(self):
        FactoryInterior.notify.info('enterWaitForBattle')
        BattlePlace.BattlePlace.enterWaitForBattle(self)
        if base.localAvatar.getParent() != render:
            base.localAvatar.wrtReparentTo(render)
            base.localAvatar.b_setParent(ToontownGlobals.SPRender)
        

    
    def exitWaitForBattle(self):
        FactoryInterior.notify.info('exitWaitForBattle')
        BattlePlace.BattlePlace.exitWaitForBattle(self)

    
    def enterBattle(self, event):
        FactoryInterior.notify.info('enterBattle')
        self.music.stop()
        BattlePlace.BattlePlace.enterBattle(self, event)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    
    def enterTownBattle(self, event):
        mult = ToontownBattleGlobals.getFactoryCreditMultiplier(self.zoneId)
        base.localAvatar.inventory.setBattleCreditMultiplier(mult)
        self.loader.townBattle.enter(event, self.fsm.getStateNamed('battle'), bldg = 1, creditMultiplier = mult)

    
    def exitBattle(self):
        FactoryInterior.notify.info('exitBattle')
        BattlePlace.BattlePlace.exitBattle(self)
        self.loader.music.stop()
        base.playMusic(self.music, looping = 1, volume = 0.80000000000000004)

    
    def enterStickerBook(self, page = None):
        BattlePlace.BattlePlace.enterStickerBook(self, page)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    
    def enterSit(self):
        BattlePlace.BattlePlace.enterSit(self)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    
    def enterZone(self, zoneId):
        pass

    
    def enterTeleportOut(self, requestStatus):
        FactoryInterior.notify.info('enterTeleportOut()')
        BattlePlace.BattlePlace.enterTeleportOut(self, requestStatus, self._FactoryInterior__teleportOutDone)

    
    def _FactoryInterior__processLeaveRequest(self, requestStatus):
        hoodId = requestStatus['hoodId']
        if hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    
    def _FactoryInterior__teleportOutDone(self, requestStatus):
        FactoryInterior.notify.info('__teleportOutDone()')
        messenger.send('leavingFactory')
        messenger.send('localToonLeft')
        if self.factoryDefeated and not (self.confrontedForeman):
            self.fsm.request('FLA', [
                requestStatus])
        else:
            self._FactoryInterior__processLeaveRequest(requestStatus)

    
    def exitTeleportOut(self):
        FactoryInterior.notify.info('exitTeleportOut()')
        BattlePlace.BattlePlace.exitTeleportOut(self)

    
    def handleFactoryWinEvent(self):
        FactoryInterior.notify.info('handleFactoryWinEvent')
        if base.cr.playGame.getPlace().fsm.getCurrentState().getName() == 'died':
            return None
        
        self.factoryDefeated = 1
        if 1:
            zoneId = ZoneUtil.getHoodId(self.zoneId)
        else:
            zoneId = ZoneUtil.getSafeZoneId(base.localAvatar.defaultZone)
        self.fsm.request('teleportOut', [
            {
                'loader': ZoneUtil.getLoaderName(zoneId),
                'where': ZoneUtil.getToonWhereName(zoneId),
                'how': 'teleportIn',
                'hoodId': zoneId,
                'zoneId': zoneId,
                'shardId': None,
                'avId': -1 }])

    
    def enterDied(self, requestStatus, callback = None):
        FactoryInterior.notify.info('enterDied')
        
        def diedDone(requestStatus, self = self, callback = callback):
            if callback is not None:
                callback()
            
            messenger.send('leavingFactory')
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

        BattlePlace.BattlePlace.enterDied(self, requestStatus, diedDone)

    
    def enterFLA(self, requestStatus):
        FactoryInterior.notify.info('enterFLA')
        self.flaDialog = TTDialog.TTGlobalDialog(message = TTLocalizer.ForcedLeaveFactoryAckMsg, doneEvent = 'FLADone', style = TTDialog.Acknowledge, fadeScreen = 1)
        
        def continueExit(self = self, requestStatus = requestStatus):
            self._FactoryInterior__processLeaveRequest(requestStatus)

        self.accept('FLADone', continueExit)
        self.flaDialog.show()

    
    def exitFLA(self):
        FactoryInterior.notify.info('exitFLA')
        if hasattr(self, 'flaDialog'):
            self.flaDialog.cleanup()
            del self.flaDialog
        


