# File: C (Python 2.2)

from PurchaseBase import *
from toontown.toonbase import ToontownTimer
COUNT_UP_RATE = 0.14999999999999999
DELAY_BEFORE_COUNT_UP = 1.25
DELAY_AFTER_COUNT_UP = 1.75
COUNT_DOWN_RATE = 0.074999999999999997
DELAY_AFTER_COUNT_DOWN = 0.0
DELAY_AFTER_CELEBRATE = 3.0

class ClerkPurchase(PurchaseBase):
    activateMode = 'storePurchase'
    
    def __init__(self, toon, remain, doneEvent):
        PurchaseBase.__init__(self, toon, doneEvent)
        self.remain = remain

    
    def load(self):
        purchaseModels = loader.loadModel('phase_4/models/gui/gag_shop_purchase_gui')
        PurchaseBase.load(self, purchaseModels)
        self.backToPlayground = DirectButton(parent = self.frame, relief = None, scale = 1.04, pos = (0.66000000000000003, 0, -0.044999999999999998), image = (purchaseModels.find('**/PurchScrn_BTN_UP'), purchaseModels.find('**/PurchScrn_BTN_DN'), purchaseModels.find('**/PurchScrn_BTN_RLVR')), text = TTLocalizer.GagShopDoneShopping, text_fg = (0, 0.10000000000000001, 0.69999999999999996, 1), text_scale = 0.050000000000000003, text_pos = (0, 0.014999999999999999, 0), command = self._ClerkPurchase__handleBackToPlayground)
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(self.frame)
        self.timer.posInTopRightCorner()
        purchaseModels.removeNode()

    
    def unload(self):
        PurchaseBase.unload(self)
        del self.backToPlayground
        del self.timer
        return None

    
    def _ClerkPurchase__handleBackToPlayground(self):
        self.toon.inventory.reparentTo(hidden)
        self.toon.inventory.hide()
        self.handleDone(0)
        return None

    
    def _ClerkPurchase__timerExpired(self):
        self.handleDone(0)
        return None

    
    def enterPurchase(self):
        PurchaseBase.enterPurchase(self)
        self.backToPlayground.reparentTo(self.toon.inventory.storePurchaseFrame)
        self.pointDisplay.reparentTo(self.toon.inventory.storePurchaseFrame)
        self.statusLabel.reparentTo(self.toon.inventory.storePurchaseFrame)
        self.timer.countdown(self.remain, self._ClerkPurchase__timerExpired)
        return None

    
    def exitPurchase(self):
        PurchaseBase.exitPurchase(self)
        self.backToPlayground.reparentTo(self.frame)
        self.pointDisplay.reparentTo(self.frame)
        self.statusLabel.reparentTo(self.frame)
        self.ignore('purchaseStateChange')
        return None


