# File: D (Python 2.2)

from ShowBaseGlobal import *
from DistributedNPCToonBase import *
import ClerkPurchase
from PurchaseManagerConstants import *
import NPCToons
import Localizer

class DistributedNPCClerk(DistributedNPCToonBase):
    
    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.purchase = None
        self.isLocalToon = 0
        self.av = None
        self.purchaseDoneEvent = 'purchaseDone'

    
    def disable(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupPurchaseGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        if self.purchase:
            self.purchase.exit()
            self.purchase.unload()
            self.purchase = None
        
        self.av = None
        toonbase.localToon.posCamera(0, 0)
        DistributedNPCToonBase.disable(self)

    
    def handleCollisionSphereEnter(self, collEntry):
        toonbase.tcr.playGame.getPlace().fsm.request('purchase', [
            self])
        self.sendUpdate('avatarEnter', [])

    
    def _DistributedNPCClerk__handleUnexpectedExit(self):
        self.notify.warning('unexpected exit')
        self.av = None

    
    def resetClerk(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupPurchaseGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        if self.purchase:
            self.purchase.exit()
            self.purchase.unload()
            self.purchase = None
        
        if self.isLocalToon:
            self.freeAvatar()
        
        self.startLookAround()
        self.detectAvatars()
        self.clearMat()
        return Task.done

    
    def setMovie(self, mode, npcId, avId, timestamp):
        timeStamp = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.remain = NPCToons.CLERK_COUNTDOWN_TIME - timeStamp
        self.isLocalToon = avId == toonbase.localToon.doId
        if mode == NPCToons.PURCHASE_MOVIE_CLEAR:
            return None
        
        if mode == NPCToons.PURCHASE_MOVIE_TIMEOUT:
            taskMgr.remove(self.uniqueName('popupPurchaseGUI'))
            taskMgr.remove(self.uniqueName('lerpCamera'))
            if self.isLocalToon:
                self.ignore(self.purchaseDoneEvent)
            
            if self.purchase:
                self._DistributedNPCClerk__handlePurchaseDone()
            
            self.setChatAbsolute(Localizer.STOREOWNER_TOOKTOOLONG, CFSpeech | CFTimeout)
            self.resetClerk()
        elif mode == NPCToons.PURCHASE_MOVIE_START:
            self.av = toonbase.tcr.doId2do.get(avId)
            if self.av is None:
                self.notify.warning('Avatar %d not found in doId' % avId)
                return None
            else:
                self.accept(self.av.uniqueName('disable'), self._DistributedNPCClerk__handleUnexpectedExit)
            self.setupAvatars(self.av)
            if self.isLocalToon:
                camera.wrtReparentTo(render)
                camera.lerpPosHpr(-5, 9, self.getHeight() - 0.5, -150, -2, 0, 1, other = self, blendType = 'easeOut', task = self.uniqueName('lerpCamera'))
            
            self.setChatAbsolute(Localizer.STOREOWNER_GREETING, CFSpeech | CFTimeout)
            if self.isLocalToon:
                taskMgr.doMethodLater(1.0, self.popupPurchaseGUI, self.uniqueName('popupPurchaseGUI'))
            
        elif mode == NPCToons.PURCHASE_MOVIE_COMPLETE:
            self.setChatAbsolute(Localizer.STOREOWNER_GOODBYE, CFSpeech | CFTimeout)
            self.resetClerk()
        elif mode == NPCToons.PURCHASE_MOVIE_NO_MONEY:
            self.setChatAbsolute(Localizer.STOREOWNER_NEEDJELLYBEANS, CFSpeech | CFTimeout)
            self.resetClerk()
        
        return None

    
    def popupPurchaseGUI(self, task):
        self.setChatAbsolute('', CFSpeech)
        self.acceptOnce(self.purchaseDoneEvent, self._DistributedNPCClerk__handlePurchaseDone)
        self.purchase = ClerkPurchase.ClerkPurchase(toonbase.localToon, self.remain, self.purchaseDoneEvent)
        self.purchase.load()
        self.purchase.enter()
        return Task.done

    
    def _DistributedNPCClerk__handlePurchaseDone(self):
        print 'handlepurchasedone'
        self.d_setInventory(toonbase.localToon.inventory.makeNetString(), toonbase.localToon.getMoney())
        print 'handlepurchasedone, set inventory'
        self.purchase.exit()
        self.purchase.unload()
        self.purchase = None

    
    def d_setInventory(self, invString, money):
        self.sendUpdate('setInventory', [
            invString,
            money])


