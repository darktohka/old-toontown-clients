# File: D (Python 2.2)

from ShowBaseGlobal import *
from DistributedNPCToonBase import *
from DirectGui import *
import NPCToons
import Localizer
import FishSellGUI

class DistributedNPCFisherman(DistributedNPCToonBase):
    
    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.isLocalToon = 0
        self.av = None
        self.button = None
        self.popupInfo = None
        self.fishGui = None

    
    def disable(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupFishGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        
        if self.fishGui:
            self.fishGui.destroy()
            self.fishGui = None
        
        self.av = None
        toonbase.localToon.posCamera(0, 0)
        DistributedNPCToonBase.disable(self)

    
    def generate(self):
        DistributedNPCToonBase.generate(self)
        self.fishGuiDoneEvent = 'fishGuiDone'

    
    def announceGenerate(self):
        self.setAnimState('neutral', 1.05, None, None)
        npcOrigin = self.cr.playGame.hood.loader.geom.find('**/npc_fisherman_origin_' + `self.posIndex`)
        if not npcOrigin.isEmpty():
            self.reparentTo(npcOrigin)
            self.clearMat()
        else:
            self.notify.warning('announceGenerate: Could not find npc_fisherman_origin_' + str(self.posIndex))
        DistributedObject.DistributedObject.announceGenerate(self)

    
    def getCollSphereRadius(self):
        return 1.5

    
    def handleCollisionSphereEnter(self, collEntry):
        toonbase.tcr.playGame.getPlace().fsm.request('purchase')
        self.sendUpdate('avatarEnter', [])

    
    def _DistributedNPCFisherman__handleUnexpectedExit(self):
        self.notify.warning('unexpected exit')
        self.av = None

    
    def setupAvatars(self, av):
        self.ignoreAvatars()
        av.stopLookAround()
        av.lerpLookAt(Point3(-0.5, 4, 0), time = 0.5)
        self.stopLookAround()
        self.lerpLookAt(Point3(av.getPos(self)), time = 0.5)

    
    def resetFisherman(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupFishGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        if self.fishGui:
            self.fishGui.destroy()
            self.fishGui = None
        
        self.show()
        self.startLookAround()
        self.detectAvatars()
        self.clearMat()
        if self.isLocalToon:
            self.freeAvatar()
        
        return Task.done

    
    def setMovie(self, mode, npcId, avId, extraArgs, timestamp):
        timeStamp = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.remain = NPCToons.CLERK_COUNTDOWN_TIME - timeStamp
        self.npcId = npcId
        self.isLocalToon = avId == toonbase.localToon.doId
        if mode == NPCToons.SELL_MOVIE_CLEAR:
            return None
        
        if mode == NPCToons.SELL_MOVIE_TIMEOUT:
            taskMgr.remove(self.uniqueName('lerpCamera'))
            if self.isLocalToon:
                self.ignore(self.fishGuiDoneEvent)
                if self.popupInfo:
                    self.popupInfo.reparentTo(hidden)
                
                if self.fishGui:
                    self.fishGui.destroy()
                    self.fishGui = None
                
            
            self.setChatAbsolute(Localizer.STOREOWNER_TOOKTOOLONG, CFSpeech | CFTimeout)
            self.resetFisherman()
        elif mode == NPCToons.SELL_MOVIE_START:
            self.av = toonbase.tcr.doId2do.get(avId)
            if self.av is None:
                self.notify.warning('Avatar %d not found in doId' % avId)
                return None
            else:
                self.accept(self.av.uniqueName('disable'), self._DistributedNPCFisherman__handleUnexpectedExit)
            self.setupAvatars(self.av)
            if self.isLocalToon:
                camera.wrtReparentTo(render)
                camera.lerpPosHpr(-5, 9, toonbase.localToon.getHeight() - 0.5, -150, -2, 0, 1, other = self, blendType = 'easeOut', task = self.uniqueName('lerpCamera'))
            
            if self.isLocalToon:
                taskMgr.doMethodLater(1.0, self.popupFishGUI, self.uniqueName('popupFishGUI'))
            
        elif mode == NPCToons.SELL_MOVIE_COMPLETE:
            self.setChatAbsolute(Localizer.STOREOWNER_THANKSFISH, CFSpeech | CFTimeout)
            self.resetFisherman()
        elif mode == NPCToons.SELL_MOVIE_TROPHY:
            self.av = toonbase.tcr.doId2do.get(avId)
            if self.av is None:
                self.notify.warning('Avatar %d not found in doId' % avId)
                return None
            else:
                (numFish, totalNumFish) = extraArgs
                self.setChatAbsolute(Localizer.STOREOWNER_TROPHY % (numFish, totalNumFish), CFSpeech | CFTimeout)
            self.resetFisherman()
        elif mode == NPCToons.SELL_MOVIE_NOFISH:
            self.setChatAbsolute(Localizer.STOREOWNER_NOFISH, CFSpeech | CFTimeout)
            self.resetFisherman()
        elif mode == NPCToons.SELL_MOVIE_NO_MONEY:
            self.notify.warning('SELL_MOVIE_NO_MONEY should not be called')
            self.resetFisherman()
        
        return None

    
    def _DistributedNPCFisherman__handleSaleDone(self, sell):
        self.ignore(self.fishGuiDoneEvent)
        self.sendUpdate('completeSale', [
            sell])
        self.fishGui.destroy()
        self.fishGui = None

    
    def popupFishGUI(self, task):
        print 'popupFishGui'
        self.setChatAbsolute('', CFSpeech)
        self.acceptOnce(self.fishGuiDoneEvent, self._DistributedNPCFisherman__handleSaleDone)
        self.fishGui = FishSellGUI.FishSellGUI(self.fishGuiDoneEvent)


