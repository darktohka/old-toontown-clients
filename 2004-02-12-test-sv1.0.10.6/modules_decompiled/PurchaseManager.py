# File: P (Python 2.2)

from ShowBaseGlobal import *
from PurchaseManagerConstants import *
from ClockDelta import *
import DistributedObject
import DirectNotifyGlobal

class PurchaseManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('PurchaseManager')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.playAgain = 0

    
    def disable(self):
        self.ignoreAll()

    
    def setPlayerIds(self, *playerIds):
        self.playerIds = playerIds

    
    def setMinigamePoints(self, *mpArray):
        self.mpArray = mpArray

    
    def setPlayerMoney(self, *moneyArray):
        self.moneyArray = moneyArray

    
    def setPlayerStates(self, *stateArray):
        self.notify.debug('setPlayerStates: %s' % (stateArray,))
        self.playerStates = stateArray
        messenger.send('purchaseStateChange', [
            self.playerStates])

    
    def setCountdown(self, timestamp):
        et = globalClockDelta.localElapsedTime(timestamp)
        remain = PURCHASE_COUNTDOWN_TIME - et
        self.acceptOnce('purchasePlayAgain', self.playAgainHandler)
        self.acceptOnce('purchaseBackToToontown', self.backToToontownHandler)
        self.acceptOnce('purchaseTimeout', self.setPurchaseExit)
        toonbase.tcr.playGame.hood.fsm.request('purchase', [
            self.mpArray,
            self.moneyArray,
            self.playerIds,
            self.playerStates,
            remain])

    
    def playAgainHandler(self):
        self.d_requestPlayAgain()

    
    def backToToontownHandler(self):
        self.notify.debug('requesting exit to toontown...')
        self.d_requestExit()
        self.playAgain = 0
        self.setPurchaseExit()

    
    def d_requestExit(self):
        self.sendUpdate('requestExit', [])

    
    def d_requestPlayAgain(self):
        self.notify.debug('requesting play again...')
        self.sendUpdate('requestPlayAgain', [])
        self.playAgain = 1

    
    def d_setInventory(self, invString, money):
        self.sendUpdate('setInventory', [
            invString,
            money])

    
    def setPurchaseExit(self):
        self.d_setInventory(toonbase.localToon.inventory.makeNetString(), toonbase.localToon.getMoney())
        messenger.send('purchaseOver', [
            self.playAgain])


