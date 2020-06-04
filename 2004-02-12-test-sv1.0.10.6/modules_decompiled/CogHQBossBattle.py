# File: C (Python 2.2)

from PandaModules import *
from IntervalGlobal import *
import DirectNotifyGlobal
import Place
import FSM
import State
import ToontownGlobals
import ToontownBattleGlobals
import BattlePlace
import DistributedBossCog
import Suit
import math

class CogHQBossBattle(BattlePlace.BattlePlace):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogHQBossBattle')
    
    def __init__(self, loader, parentFSM, doneEvent):
        BattlePlace.BattlePlace.__init__(self, loader, doneEvent)
        self.parentFSM = parentFSM
        self.fsm = FSM.FSM('CogHQBossBattle', [
            State.State('start', self.enterStart, self.exitStart, [
                'walk',
                'tunnelIn',
                'teleportIn',
                'movie']),
            State.State('battle', self.enterBattle, self.exitBattle, [
                'walk',
                'died',
                'movie']),
            State.State('finalBattle', self.enterFinalBattle, self.exitFinalBattle, [
                'walk',
                'stickerBook',
                'teleportOut',
                'died',
                'tunnelOut',
                'DFA',
                'battle',
                'movie',
                'ouch',
                'WaitForBattle']),
            State.State('movie', self.enterMovie, self.exitMovie, [
                'walk',
                'battle',
                'finalBattle',
                'died',
                'teleportOut']),
            State.State('ouch', self.enterOuch, self.exitOuch, [
                'walk',
                'battle',
                'finalBattle',
                'died']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'stickerBook',
                'teleportOut',
                'died',
                'tunnelOut',
                'DFA',
                'battle',
                'movie',
                'ouch',
                'finalBattle',
                'WaitForBattle']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk',
                'DFA',
                'WaitForBattle']),
            State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, [
                'battle',
                'walk',
                'movie']),
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
                'final']),
            State.State('tunnelIn', self.enterTunnelIn, self.exitTunnelIn, [
                'walk']),
            State.State('tunnelOut', self.enterTunnelOut, self.exitTunnelOut, [
                'final']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')

    
    def load(self):
        BattlePlace.BattlePlace.load(self)
        self.parentFSM.getStateNamed('cogHQBossBattle').addChild(self.fsm)
        self.townBattle = self.loader.townBattle
        for i in range(1, 3):
            Suit.loadSuits(i)
        

    
    def unload(self):
        BattlePlace.BattlePlace.unload(self)
        self.parentFSM.getStateNamed('cogHQBossBattle').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.ignoreAll()
        for i in range(1, 3):
            Suit.unloadSuits(i)
        

    
    def enter(self, requestStatus):
        self.zoneId = requestStatus['zoneId']
        BattlePlace.BattlePlace.enter(self)
        self.fsm.enterInitialState()
        self._CogHQBossBattle__setupHighSky()
        NametagGlobals.setMasterArrowsOn(1)
        toonbase.localToon.inventory.setRespectInvasions(0)
        if DistributedBossCog.OneBossCog:
            DistributedBossCog.OneBossCog.d_avatarEnter()
        
        self.fsm.request(requestStatus['how'], [
            requestStatus])

    
    def exit(self):
        self.fsm.requestFinalState()
        self._CogHQBossBattle__cleanupHighSky()
        toonbase.localToon.inventory.setRespectInvasions(1)
        if DistributedBossCog.OneBossCog:
            DistributedBossCog.OneBossCog.d_avatarExit()
        
        BattlePlace.BattlePlace.exit(self)

    
    def _CogHQBossBattle__setupHighSky(self):
        self.loader.hood.startSky()
        sky = self.loader.hood.sky
        sky.setH(150)
        sky.setZ(-100)

    
    def _CogHQBossBattle__cleanupHighSky(self):
        self.loader.hood.stopSky()
        sky = self.loader.hood.sky
        sky.setH(0)
        sky.setZ(0)

    
    def enterBattle(self, event):
        mult = 1
        if DistributedBossCog.OneBossCog:
            mult = ToontownBattleGlobals.getBossBattleCreditMultiplier(DistributedBossCog.OneBossCog.battleNumber)
        
        self.townBattle.enter(event, self.fsm.getStateNamed('battle'), bldg = 1, creditMultiplier = mult)
        toonbase.localToon.b_setAnimState('off', 1)
        toonbase.localToon.setTeleportAvailable(0)

    
    def exitBattle(self):
        self.townBattle.exit()

    
    def enterFinalBattle(self):
        self.walkStateData.enter()
        self.walkStateData.fsm.request('walking')
        toonbase.localToon.setTeleportAvailable(0)
        toonbase.localToon.setTeleportAllowed(0)
        toonbase.localToon.book.hideButton()
        self.ignore(ToontownGlobals.StickerBookHotkey)
        self.ignore('enterStickerBook')
        self.ignore(ToontownGlobals.OptionsPageHotkey)

    
    def exitFinalBattle(self):
        self.walkStateData.exit()
        toonbase.localToon.setTeleportAllowed(1)

    
    def enterMovie(self, requestStatus = None):
        toonbase.localToon.setTeleportAvailable(0)

    
    def exitMovie(self):
        pass

    
    def enterOuch(self):
        toonbase.localToon.setTeleportAvailable(0)
        toonbase.localToon.laffMeter.start()

    
    def exitOuch(self):
        toonbase.localToon.laffMeter.stop()

    
    def enterWalk(self, teleportIn = 0):
        BattlePlace.BattlePlace.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
    def enterStickerBook(self, page = None):
        BattlePlace.BattlePlace.enterStickerBook(self, page)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
    def enterSit(self):
        BattlePlace.BattlePlace.enterSit(self)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
    def enterTeleportIn(self, requestStatus):
        toonbase.localToon.reparentTo(hidden)
        toonbase.localToon.setPosHpr(0, 95, 18, 180, 0, 0)
        BattlePlace.BattlePlace.enterTeleportIn(self, requestStatus)

    
    def enterTeleportOut(self, requestStatus):
        BattlePlace.BattlePlace.enterTeleportOut(self, requestStatus, self._CogHQBossBattle__teleportOutDone)

    
    def _CogHQBossBattle__teleportOutDone(self, requestStatus):
        hoodId = requestStatus['hoodId']
        if hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)


