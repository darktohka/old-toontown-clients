# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from DistributedNPCToonBase import *
from direct.gui.DirectGui import *
import NPCToons
from toontown.toonbase import TTLocalizer
from toontown.pets import PetshopGUI

class DistributedNPCPetclerk(DistributedNPCToonBase):
    
    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.isLocalToon = 0
        self.av = None
        self.button = None
        self.popupInfo = None
        self.petshopGui = None
        self.petSeeds = None
        self.waitingForPetSeeds = False

    
    def disable(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupPetshopGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        if self.petshopGui:
            self.petshopGui.destroy()
            self.petshopGui = None
        
        self.av = None
        if self.isLocalToon:
            base.localAvatar.posCamera(0, 0)
        
        DistributedNPCToonBase.disable(self)

    
    def generate(self):
        DistributedNPCToonBase.generate(self)
        self.eventDict = { }
        self.eventDict['guiDone'] = 'guiDone'
        self.eventDict['petAdopted'] = 'petAdopted'
        self.eventDict['petReturned'] = 'petReturned'
        self.eventDict['fishSold'] = 'fishSold'

    
    def getCollSphereRadius(self):
        return 4.0

    
    def handleCollisionSphereEnter(self, collEntry):
        base.cr.playGame.getPlace().fsm.request('purchase')
        self.sendUpdate('avatarEnter', [])

    
    def _DistributedNPCPetclerk__handleUnexpectedExit(self):
        self.notify.warning('unexpected exit')
        self.av = None

    
    def resetPetshopClerk(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupPetshopGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        if self.petshopGui:
            self.petshopGui.destroy()
            self.petshopGui = None
        
        self.show()
        self.startLookAround()
        self.detectAvatars()
        self.clearMat()
        if self.isLocalToon:
            self.freeAvatar()
        
        self.petSeeds = None
        self.waitingForPetSeeds = False
        return Task.done

    
    def ignoreEventDict(self):
        for event in self.eventDict.values():
            self.ignore(event)
        

    
    def setPetSeeds(self, petSeeds):
        self.petSeeds = petSeeds
        if self.waitingForPetSeeds:
            self.waitingForPetSeeds = False
            self.popupPetshopGUI(None)
        

    
    def setMovie(self, mode, npcId, avId, extraArgs, timestamp):
        timeStamp = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.remain = NPCToons.CLERK_COUNTDOWN_TIME - timeStamp
        self.npcId = npcId
        self.isLocalToon = avId == base.localAvatar.doId
        if mode == NPCToons.SELL_MOVIE_CLEAR:
            return None
        
        if mode == NPCToons.SELL_MOVIE_TIMEOUT:
            taskMgr.remove(self.uniqueName('lerpCamera'))
            if self.isLocalToon:
                self.ignoreEventDict()
                if self.popupInfo:
                    self.popupInfo.reparentTo(hidden)
                
                if self.petshopGui:
                    self.petshopGui.destroy()
                    self.petshopGui = None
                
            
            self.setChatAbsolute(TTLocalizer.STOREOWNER_TOOKTOOLONG, CFSpeech | CFTimeout)
            self.resetPetshopClerk()
        elif mode == NPCToons.SELL_MOVIE_START:
            self.av = base.cr.doId2do.get(avId)
            if self.av is None:
                self.notify.warning('Avatar %d not found in doId' % avId)
                return None
            else:
                self.accept(self.av.uniqueName('disable'), self._DistributedNPCPetclerk__handleUnexpectedExit)
            self.setupAvatars(self.av)
            if self.isLocalToon:
                camera.wrtReparentTo(render)
                camera.lerpPosHpr(-5, 9, base.localAvatar.getHeight() - 0.5, -150, -2, 0, 1, other = self, blendType = 'easeOut', task = self.uniqueName('lerpCamera'))
            
            if self.isLocalToon:
                taskMgr.doMethodLater(1.0, self.popupPetshopGUI, self.uniqueName('popupPetshopGUI'))
            
        elif mode == NPCToons.SELL_MOVIE_COMPLETE:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_THANKSFISH_PETSHOP, CFSpeech | CFTimeout)
            self.resetPetshopClerk()
        elif mode == NPCToons.SELL_MOVIE_PETRETURNED:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_PETRETURNED, CFSpeech | CFTimeout)
            self.resetPetshopClerk()
        elif mode == NPCToons.SELL_MOVIE_PETADOPTED:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_PETADOPTED, CFSpeech | CFTimeout)
            self.resetPetshopClerk()
        elif mode == NPCToons.SELL_MOVIE_PETCANCELED:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_PETCANCELED, CFSpeech | CFTimeout)
            self.resetPetshopClerk()
        elif mode == NPCToons.SELL_MOVIE_TROPHY:
            self.av = base.cr.doId2do.get(avId)
            if self.av is None:
                self.notify.warning('Avatar %d not found in doId' % avId)
                return None
            else:
                (numFish, totalNumFish) = extraArgs
                self.setChatAbsolute(TTLocalizer.STOREOWNER_TROPHY % (numFish, totalNumFish), CFSpeech | CFTimeout)
            self.resetPetshopClerk()
        elif mode == NPCToons.SELL_MOVIE_NOFISH:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_NOFISH, CFSpeech | CFTimeout)
            self.resetPetshopClerk()
        elif mode == NPCToons.SELL_MOVIE_NO_MONEY:
            self.notify.warning('SELL_MOVIE_NO_MONEY should not be called')
            self.resetPetshopClerk()
        
        return None

    
    def _DistributedNPCPetclerk__handlePetAdopted(self, whichPet, nameIndex):
        base.cr.removePetFromFriendsMap()
        self.ignore(self.eventDict['petAdopted'])
        self.sendUpdate('petAdopted', [
            whichPet,
            nameIndex])

    
    def _DistributedNPCPetclerk__handlePetReturned(self):
        base.cr.removePetFromFriendsMap()
        self.ignore(self.eventDict['petReturned'])
        self.sendUpdate('petReturned')

    
    def _DistributedNPCPetclerk__handleFishSold(self):
        self.ignore(self.eventDict['fishSold'])
        self.sendUpdate('fishSold')

    
    def _DistributedNPCPetclerk__handleGUIDone(self, bTimedOut = False):
        self.ignore(self.eventDict['guiDone'])
        self.petshopGui.destroy()
        self.petshopGui = None
        if not bTimedOut:
            self.sendUpdate('transactionDone')
        

    
    def popupPetshopGUI(self, task):
        if not (self.petSeeds):
            self.waitingForPetSeeds = True
            return None
        
        print 'popupPetshopGui'
        self.setChatAbsolute('', CFSpeech)
        self.acceptOnce(self.eventDict['guiDone'], self._DistributedNPCPetclerk__handleGUIDone)
        self.acceptOnce(self.eventDict['petAdopted'], self._DistributedNPCPetclerk__handlePetAdopted)
        self.acceptOnce(self.eventDict['petReturned'], self._DistributedNPCPetclerk__handlePetReturned)
        self.acceptOnce(self.eventDict['fishSold'], self._DistributedNPCPetclerk__handleFishSold)
        self.petshopGui = PetshopGUI.PetshopGUI(self.eventDict, self.petSeeds)


