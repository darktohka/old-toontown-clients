# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from DistributedNPCToonBase import *
from toontown.minigame import ClerkPurchase
from toontown.shtiker.PurchaseManagerConstants import *
import NPCToons
from toontown.toonbase import TTLocalizer

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
        base.localAvatar.posCamera(0, 0)
        DistributedNPCToonBase.disable(self)

    
    def handleCollisionSphereEnter(self, collEntry):
        base.cr.playGame.getPlace().fsm.request('purchase')
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
        
        self.clearMat()
        self.startLookAround()
        self.detectAvatars()
        if self.isLocalToon:
            self.freeAvatar()
        
        return Task.done

    
    def setMovie(self, mode, npcId, avId, timestamp):
        timeStamp = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.remain = NPCToons.CLERK_COUNTDOWN_TIME - timeStamp
        self.isLocalToon = avId == base.localAvatar.doId
        if mode == NPCToons.PURCHASE_MOVIE_CLEAR:
            return None
        
        if mode == NPCToons.PURCHASE_MOVIE_TIMEOUT:
            taskMgr.remove(self.uniqueName('popupPurchaseGUI'))
            taskMgr.remove(self.uniqueName('lerpCamera'))
            if self.isLocalToon:
                self.ignore(self.purchaseDoneEvent)
            
            if self.purchase:
                self._DistributedNPCClerk__handlePurchaseDone()
            
            self.setChatAbsolute(TTLocalizer.STOREOWNER_TOOKTOOLONG, CFSpeech | CFTimeout)
            self.resetClerk()
        elif mode == NPCToons.PURCHASE_MOVIE_START:
            self.av = base.cr.doId2do.get(avId)
            if self.av is None:
                self.notify.warning('Avatar %d not found in doId' % avId)
                return None
            else:
                self.accept(self.av.uniqueName('disable'), self._DistributedNPCClerk__handleUnexpectedExit)
            self.setupAvatars(self.av)
            if self.isLocalToon:
                camera.wrtReparentTo(render)
                camera.lerpPosHpr(-5, 9, self.getHeight() - 0.5, -150, -2, 0, 1, other = self, blendType = 'easeOut', task = self.uniqueName('lerpCamera'))
            
            self.setChatAbsolute(TTLocalizer.STOREOWNER_GREETING, CFSpeech | CFTimeout)
            if self.isLocalToon:
                taskMgr.doMethodLater(1.0, self.popupPurchaseGUI, self.uniqueName('popupPurchaseGUI'))
            
        elif mode == NPCToons.PURCHASE_MOVIE_COMPLETE:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_GOODBYE, CFSpeech | CFTimeout)
            self.resetClerk()
        elif mode == NPCToons.PURCHASE_MOVIE_NO_MONEY:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_NEEDJELLYBEANS, CFSpeech | CFTimeout)
            self.resetClerk()
        
        return None

    
    def popupPurchaseGUI(self, task):
        self.setChatAbsolute('', CFSpeech)
        self.acceptOnce(self.purchaseDoneEvent, self._DistributedNPCClerk__handlePurchaseDone)
        self.purchase = ClerkPurchase.ClerkPurchase(base.localAvatar, self.remain, self.purchaseDoneEvent)
        self.purchase.load()
        self.purchase.enter()
        return Task.done

    
    def _DistributedNPCClerk__handlePurchaseDone(self):
        print 'handlepurchasedone'
        self.d_setInventory(base.localAvatar.inventory.makeNetString(), base.localAvatar.getMoney())
        print 'handlepurchasedone, set inventory'
        self.purchase.exit()
        self.purchase.unload()
        self.purchase = None

    
    def d_setInventory(self, invString, money):
        self.sendUpdate('setInventory', [
            invString,
            money])


