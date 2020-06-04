# File: F (Python 2.2)

import DirectNotifyGlobal
import BattlePlace
import FSM
import State
from PandaModules import *
import Toon
import ToontownGlobals
import ZoneUtil
import Localizer
import ToontownDialog

class FactoryInterior(BattlePlace.BattlePlace):
    notify = DirectNotifyGlobal.directNotify.newCategory('FactoryInterior')
    
    def __init__(self, loader, parentFSM, doneEvent):
        BattlePlace.BattlePlace.__init__(self, loader, doneEvent)
        self.parentFSM = parentFSM
        self.zoneId = ToontownGlobals.SellbotFactoryInt
        self.fsm = FSM.FSM('FactoryInterior', [
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
        toonbase.localToon.inventory.setRespectInvasions(0)
        
        def commence(self = self):
            NametagGlobals.setMasterArrowsOn(1)
            self.fsm.request(requestStatus['how'], [
                requestStatus])
            base.playMusic(self.music, looping = 1, volume = 0.80000000000000004)
            base.transitions.irisIn()

        if hasattr(toonbase, 'factoryReady'):
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
        if hasattr(toonbase, 'factoryReady'):
            del toonbase.factoryReady
        
        toonbase.localToon.inventory.setRespectInvasions(1)
        self.fsm.requestFinalState()
        self.loader.music.stop()
        self.music.stop()
        self.ignoreAll()

    
    def enterWalk(self, teleportIn = 0):
        BattlePlace.BattlePlace.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
    def enterPush(self):
        BattlePlace.BattlePlace.enterPush(self)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
    def enterWaitForBattle(self):
        FactoryInterior.notify.info('enterWaitForBattle')
        BattlePlace.BattlePlace.enterWaitForBattle(self)
        if toonbase.localToon.getParent() != render:
            toonbase.localToon.wrtReparentTo(render)
            toonbase.localToon.b_setParent(ToontownGlobals.SPRender)
        

    
    def exitWaitForBattle(self):
        FactoryInterior.notify.info('exitWaitForBattle')
        BattlePlace.BattlePlace.exitWaitForBattle(self)

    
    def enterBattle(self, event):
        FactoryInterior.notify.info('enterBattle')
        self.music.stop()
        BattlePlace.BattlePlace.enterBattle(self, event)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
    def exitBattle(self):
        FactoryInterior.notify.info('exitBattle')
        BattlePlace.BattlePlace.exitBattle(self)
        self.loader.music.stop()
        base.playMusic(self.music, looping = 1, volume = 0.80000000000000004)

    
    def enterStickerBook(self, page = None):
        BattlePlace.BattlePlace.enterStickerBook(self, page)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
    def enterSit(self):
        BattlePlace.BattlePlace.enterSit(self)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
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

    
    def enterFallDown(self, extraArgs = []):
        toonbase.localToon.laffMeter.start()
        toonbase.localToon.b_setAnimState('FallDown', callback = self.handleFallDownDone, extraArgs = extraArgs)

    
    def handleFallDownDone(self):
        toonbase.tcr.playGame.getPlace().setState('walk')

    
    def exitFallDown(self):
        toonbase.localToon.laffMeter.stop()

    
    def enterSquished(self):
        toonbase.localToon.laffMeter.start()
        toonbase.localToon.b_setAnimState('Squish')
        taskMgr.doMethodLater(2.0, self.handleSquishDone, toonbase.localToon.uniqueName('finishSquishTask'))

    
    def handleSquishDone(self, extraArgs = []):
        toonbase.tcr.playGame.getPlace().setState('walk')

    
    def exitSquished(self):
        taskMgr.remove(toonbase.localToon.uniqueName('finishSquishTask'))
        toonbase.localToon.laffMeter.stop()

    
    def handleFactoryWinEvent(self):
        FactoryInterior.notify.info('handleFactoryWinEvent')
        if toonbase.tcr.playGame.getPlace().fsm.getCurrentState().getName() == 'died':
            return None
        
        self.factoryDefeated = 1
        if 1:
            zoneId = ZoneUtil.getHoodId(self.zoneId)
        else:
            zoneId = ZoneUtil.getSafeZoneId(toonbase.localToon.defaultZone)
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
        self.flaDialog = ToontownDialog.GlobalDialog(message = Localizer.ForcedLeaveFactoryAckMsg, doneEvent = 'FLADone', style = ToontownDialog.Acknowledge, fadeScreen = 1)
        
        def continueExit(self = self, requestStatus = requestStatus):
            self._FactoryInterior__processLeaveRequest(requestStatus)

        self.accept('FLADone', continueExit)
        self.flaDialog.show()

    
    def exitFLA(self):
        FactoryInterior.notify.info('exitFLA')
        if hasattr(self, 'flaDialog'):
            self.flaDialog.cleanup()
            del self.flaDialog
        


