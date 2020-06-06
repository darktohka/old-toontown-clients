# File: T (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from ToontownGlobals import *
from ToontownMsgTypes import *
import DirectNotifyGlobal
import FSM
import State
import Purchase
import DistributedAvatar
import Hood
import SuitInterior

class ToonHood(Hood.Hood):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonHood')
    
    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.suitInteriorDoneEvent = 'suitInteriorDone'
        self.minigameDoneEvent = 'minigameDone'
        self.townLoaderClass = None
        self.fsm = FSM.FSM('Hood', [
            State.State('start', self.enterStart, self.exitStart, [
                'townLoader',
                'safeZoneLoader']),
            State.State('townLoader', self.enterTownLoader, self.exitTownLoader, [
                'quietZone',
                'safeZoneLoader',
                'suitInterior']),
            State.State('safeZoneLoader', self.enterSafeZoneLoader, self.exitSafeZoneLoader, [
                'quietZone',
                'suitInterior',
                'townLoader',
                'minigame']),
            State.State('purchase', self.enterPurchase, self.exitPurchase, [
                'quietZone',
                'minigame',
                'safeZoneLoader']),
            State.State('suitInterior', self.enterSuitInterior, self.exitSuitInterior, [
                'quietZone',
                'townLoader',
                'safeZoneLoader']),
            State.State('minigame', self.enterMinigame, self.exitMinigame, [
                'purchase']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'safeZoneLoader',
                'townLoader',
                'suitInterior',
                'minigame']),
            State.State('final', self.enterFinal, self.exitFinal, [])], 'start', 'final')
        self.fsm.enterInitialState()

    
    def load(self):
        Hood.Hood.load(self)

    
    def unload(self):
        del self.safeZoneLoaderClass
        del self.townLoaderClass
        Hood.Hood.unload(self)

    
    def enterTownLoader(self, requestStatus):
        self.accept(self.loaderDoneEvent, self.handleTownLoaderDone)
        self.loader.enter(requestStatus)
        self.spawnTitleText(requestStatus['zoneId'])

    
    def exitTownLoader(self):
        taskMgr.remove('titleText')
        self.hideTitleText()
        self.ignore(self.loaderDoneEvent)
        self.loader.exit()
        self.loader.unload()
        del self.loader

    
    def handleTownLoaderDone(self):
        doneStatus = self.loader.getDoneStatus()
        if self.isSameHood(doneStatus):
            self.fsm.request('quietZone', [
                doneStatus])
        else:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)

    
    def enterPurchase(self, pointsAwarded, playerMoney, playerIds, playerStates, remain):
        messenger.send('enterSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 0
        toonbase.localToon.laffMeter.start()
        self.purchaseDoneEvent = 'purchaseDone'
        self.accept(self.purchaseDoneEvent, self.handlePurchaseDone)
        self.purchase = Purchase.Purchase(toonbase.localToon, pointsAwarded, playerMoney, playerIds, playerStates, remain, self.purchaseDoneEvent)
        self.purchase.load()
        self.purchase.enter()

    
    def exitPurchase(self):
        messenger.send('exitSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 1
        toonbase.localToon.laffMeter.stop()
        self.ignore(self.purchaseDoneEvent)
        self.purchase.exit()
        self.purchase.unload()
        del self.purchase

    
    def handlePurchaseDone(self):
        doneStatus = self.purchase.getDoneStatus()
        if doneStatus['where'] == 'playground':
            self.fsm.request('quietZone', [
                {
                    'loader': 'safeZoneLoader',
                    'where': 'playground',
                    'how': 'teleportIn',
                    'hoodId': self.hoodId,
                    'zoneId': self.hoodId,
                    'shardId': None,
                    'avId': -1 }])
        elif doneStatus['loader'] == 'minigame':
            self.fsm.request('minigame')
        else:
            self.notify.error('handlePurchaseDone: unknown mode')

    
    def enterSuitInterior(self, requestStatus = None):
        self.placeDoneEvent = 'suit-interior-done'
        self.acceptOnce(self.placeDoneEvent, self.handleSuitInteriorDone)
        self.place = SuitInterior.SuitInterior(self, self.fsm, self.placeDoneEvent)
        self.place.load()
        self.place.enter(requestStatus)
        toonbase.tcr.playGame.setPlace(self.place)

    
    def exitSuitInterior(self):
        self.ignore(self.placeDoneEvent)
        del self.placeDoneEvent
        self.place.exit()
        self.place.unload()
        self.place = None
        toonbase.tcr.playGame.setPlace(self.place)

    
    def handleSuitInteriorDone(self):
        doneStatus = self.place.getDoneStatus()
        if self.isSameHood(doneStatus):
            self.fsm.request('quietZone', [
                doneStatus])
        else:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)

    
    def enterMinigame(self, ignoredParameter = None):
        messenger.send('enterSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 0
        toonbase.localToon.laffMeter.start()
        toonbase.tcr.forbidCheesyEffects(1)
        self.acceptOnce(self.minigameDoneEvent, self.handleMinigameDone)
        return None

    
    def exitMinigame(self):
        messenger.send('exitSafeZone')
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 1
        toonbase.localToon.laffMeter.stop()
        toonbase.tcr.forbidCheesyEffects(0)
        self.ignore(self.minigameDoneEvent)
        minigameState = self.fsm.getStateNamed('minigame')
        for childFSM in minigameState.getChildren():
            minigameState.removeChild(childFSM)
        

    
    def handleMinigameDone(self):
        return None


