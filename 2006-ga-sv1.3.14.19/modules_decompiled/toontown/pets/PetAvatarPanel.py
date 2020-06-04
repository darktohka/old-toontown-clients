# File: P (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.directnotify.DirectNotifyGlobal import *
from direct.gui.DirectGui import *
from direct.showbase import PandaObject
from direct.task import Task
from direct.distributed import DistributedObject
from otp.avatar import Avatar, AvatarPanel
from toontown.toon import ToonHead
from toontown.toon import LaffMeter
from toontown.toon import ToonAvatarDetailPanel
from toontown.friends import FriendHandle
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.pets import Pet, PetConstants

class PetAvatarPanel(AvatarPanel.AvatarPanel):
    notify = directNotify.newCategory('PetAvatarPanel')
    
    def __init__(self, avatar):
        self.notify.debug('Init(): doId=%s' % avatar.doId)
        distPet = base.cr.doId2do.get(avatar.doId)
        if distPet:
            self.avatar = distPet
            self.petIsLocal = True
        else:
            self.avatar = avatar
            self.petIsLocal = False
        FriendsListPanel = FriendsListPanel
        import toontown.friends
        AvatarPanel.AvatarPanel.__init__(self, self.avatar, FriendsListPanel = FriendsListPanel)
        base.localAvatar.obscureFriendsListButton(1)
        base.panel = self
        gui = loader.loadModelOnce('phase_3.5/models/gui/PetControlPannel')
        guiScale = 0.11600000000000001
        guiPos = (1.1200000000000001, 0, 0.29999999999999999)
        self.frame = DirectFrame(image = gui, scale = guiScale, pos = guiPos, relief = None)
        disabledImageColor = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1)
        text0Color = Vec4(1, 1, 1, 1)
        text1Color = Vec4(0.5, 1, 0.5, 1)
        text2Color = Vec4(1, 1, 0.5, 1)
        text3Color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1)
        self.closeButton = DirectButton(parent = self.frame, image = (gui.find('**/CancelButtonUp'), gui.find('**/CancelButtonDown'), gui.find('**/CancelButtonRollover')), relief = None, command = self._PetAvatarPanel__handleClose)
        self.feedButton = DirectButton(parent = self.frame, image = (gui.find('**/ButtonFeedUp'), gui.find('**/ButtonFeedDown'), gui.find('**/ButtonFeedRollover'), gui.find('**/ButtonFeedUp')), geom = gui.find('**/PetControlFeedIcon'), image3_color = disabledImageColor, relief = None, text = TTLocalizer.PetPanelFeed, text_scale = TTLocalizer.PAPfeed, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_pos = (-0.5, 2.7999999999999998), text_align = TextNode.ALeft, command = self._PetAvatarPanel__handleFeed)
        if not (self.petIsLocal):
            self.feedButton['state'] = DISABLED
        else:
            self.feedButton['state'] = self.feedButtonState()
        self.callButton = DirectButton(parent = self.frame, image = (gui.find('**/ButtonGoToUp'), gui.find('**/ButtonGoToDown'), gui.find('**/ButtonGoToRollover'), gui.find('**/ButtonGoToUp')), geom = gui.find('**/PetControlGoToIcon'), image3_color = disabledImageColor, relief = None, text = TTLocalizer.PetPanelCall, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = TTLocalizer.PAPcall, text_pos = (-0.5, 1.3), text_align = TextNode.ALeft, command = self._PetAvatarPanel__handleCall)
        if not (self.petIsLocal):
            self.callButton['state'] = DISABLED
        
        self.scratchButton = DirectButton(parent = self.frame, image = (gui.find('**/ButtonScratchUp'), gui.find('**/ButtonScratchDown'), gui.find('**/ButtonScratchRollover'), gui.find('**/ButtonScratchUp')), geom = gui.find('**/PetControlScratchIcon'), image3_color = disabledImageColor, relief = None, text = TTLocalizer.PetPanelScratch, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = TTLocalizer.PAPscratch, text_pos = (-0.5, 2.0499999999999998), text_align = TextNode.ALeft, command = self._PetAvatarPanel__handleScratch)
        if not (self.petIsLocal):
            self.scratchButton['state'] = DISABLED
        
        self.ownerButton = DirectButton(parent = self.frame, image = (gui.find('**/PetControlToonButtonUp'), gui.find('**/PetControlToonButtonDown'), gui.find('**/PetControlToonButtonRollover')), geom = gui.find('**/PetControlToonIcon'), geom3_color = disabledImageColor, relief = None, image3_color = disabledImageColor, text = ('', TTLocalizer.PetPanelOwner, TTLocalizer.PetPanelOwner, ''), text_fg = text2Color, text_shadow = (0, 0, 0, 1), text_scale = TTLocalizer.PAPowner, text_pos = (0.29999999999999999, 1.1000000000000001), text_align = TextNode.ACenter, command = self._PetAvatarPanel__handleToOwner)
        if self.avatar.getOwnerId() == base.localAvatar.doId:
            self.ownerButton['state'] = DISABLED
        
        gui.removeNode()
        self._PetAvatarPanel__fillPetInfo(self.avatar)
        self.accept('petNameChanged', self._PetAvatarPanel__refreshPetInfo)
        self.accept('petStateUpdated', self._PetAvatarPanel__refreshPetInfo)
        self.frame.show()
        if self.petIsLocal:
            proxTask = Task.loop(Task.Task(self._PetAvatarPanel__checkPetProximity), Task.pause(0.5))
            taskMgr.add(proxTask, 'petpanel-proximity-check', priority = ToontownGlobals.PetPanelProximityPriority)
        
        if base.localAvatar.isLockedDown():
            self.disableInteractionButtons()
        
        self.listenForInteractionDone()
        messenger.send('petPanelDone')

    
    def _PetAvatarPanel__checkPetProximity(self, task = None):
        if base.localAvatar.isInWater():
            self.scratchButton['state'] = DISABLED
            self.feedButton['state'] = DISABLED
            self.callButton['state'] = DISABLED
        else:
            petPos = self.avatar.getPos()
            toonPos = base.localAvatar.getPos()
            diff = Vec3(petPos - toonPos)
            distance = diff.length()
            if distance > 20.0:
                self.scratchButton['state'] = DISABLED
                self.feedButton['state'] = DISABLED
            else:
                tooVert = abs(diff[2]) > 5.0
                if tooVert:
                    self.scratchButton['state'] = DISABLED
                else:
                    self.scratchButton['state'] = NORMAL
                self.feedButton['state'] = self.feedButtonState()
                self.callButton['state'] = NORMAL
        return Task.done

    
    def enableInteractionButtons(self):
        proxTask = Task.loop(Task.Task(self._PetAvatarPanel__checkPetProximity), Task.pause(0.5))
        taskMgr.add(proxTask, 'petpanel-proximity-check', priority = ToontownGlobals.PetPanelProximityPriority)
        self._PetAvatarPanel__checkPetProximity()

    
    def disableInteractionButtons(self):
        taskMgr.remove('petpanel-proximity-check')
        self.scratchButton['state'] = DISABLED
        self.feedButton['state'] = DISABLED
        self.callButton['state'] = DISABLED

    
    def listenForInteractionDone(self):
        self.accept('pet-interaction-done', self.enableInteractionButtons)

    
    def cancelListenForInteractionDone(self):
        self.ignore('pet-interaction-done')

    
    def feedButtonState(self):
        if base.localAvatar.getMoney() >= PetConstants.FEED_AMOUNT:
            return NORMAL
        else:
            return DISABLED

    
    def cleanup(self):
        self.notify.debug('cleanup(): doId=%s' % self.avatar.doId)
        if self.frame == None:
            return None
        
        self.cancelListenForInteractionDone()
        taskMgr.remove('petpanel-proximity-check')
        if hasattr(self, 'toonDetail'):
            del self.toonDetail
        
        self.frame.destroy()
        del self.frame
        self.frame = None
        self.petView.removeNode()
        del self.petView
        self.petModel.delete()
        del self.petModel
        base.localAvatar.obscureFriendsListButton(-1)
        self.ignore('petStateUpdated')
        self.ignore('petNameChanged')
        if self.avatar.bFake:
            self.avatar.disable()
            self.avatar.delete()
        
        AvatarPanel.AvatarPanel.cleanup(self)
        return None

    
    def disableAll(self):
        self.disableInteractionButtons()
        self.ownerButton['state'] = DISABLED
        self.closeButton['state'] = DISABLED

    
    def _PetAvatarPanel__handleToOwner(self):
        self.notify.debug('__handleToOwner(): doId=%s' % self.avatar.doId)
        handle = base.cr.identifyFriend(self.avatar.ownerId)
        if handle != None:
            self.cleanup()
            messenger.send('clickedNametag', [
                handle])
        else:
            self.disableAll()
            ToonDetail = ToonDetail
            import toontown.toon
            self.toonDetail = ToonDetail.ToonDetail(self.avatar.ownerId, self._PetAvatarPanel__ownerDetailsLoaded)

    
    def _PetAvatarPanel__ownerDetailsLoaded(self, avatar):
        self.notify.debug('__ownerDetailsLoaded(): doId=%s' % self.avatar.doId)
        self.cleanup()
        if avatar is not None:
            messenger.send('clickedNametag', [
                avatar])
        

    
    def _PetAvatarPanel__handleCall(self):
        self.notify.debug('__handleCall(): doId=%s' % self.avatar.doId)
        base.localAvatar.b_setPetMovie(self.avId, PetConstants.PET_MOVIE_CALL)
        base.panel.disableInteractionButtons()
        if self.avatar.trickIval is not None and self.avatar.trickIval.isPlaying():
            self.avatar.trickIval.finish()
        
        base.cr.playGame.getPlace().preserveFriendsList()
        base.cr.playGame.getPlace().fsm.request('pet')
        base.localAvatar.lock()

    
    def _PetAvatarPanel__handleFeed(self):
        self.notify.debug('__handleFeed(): doId=%s' % self.avatar.doId)
        base.localAvatar.b_setPetMovie(self.avId, PetConstants.PET_MOVIE_FEED)
        base.panel.disableInteractionButtons()
        if self.avatar.trickIval is not None and self.avatar.trickIval.isPlaying():
            self.avatar.trickIval.finish()
        
        base.cr.playGame.getPlace().preserveFriendsList()
        base.cr.playGame.getPlace().fsm.request('pet')
        base.localAvatar.lock()

    
    def _PetAvatarPanel__handleScratch(self):
        self.notify.debug('__handleScratch(): doId=%s' % self.avatar.doId)
        base.localAvatar.b_setPetMovie(self.avId, PetConstants.PET_MOVIE_SCRATCH)
        base.panel.disableInteractionButtons()
        if self.avatar.trickIval is not None and self.avatar.trickIval.isPlaying():
            self.avatar.trickIval.finish()
        
        base.cr.playGame.getPlace().preserveFriendsList()
        base.cr.playGame.getPlace().fsm.request('pet')
        base.localAvatar.lock()

    
    def _PetAvatarPanel__handleDisableAvatar(self):
        self.notify.debug('__handleDisableAvatar(): doId=%s' % self.avatar.doId)
        self.cleanup()
        AvatarPanel.currentAvatarPanel = None

    
    def _PetAvatarPanel__handleGenerateAvatar(self, avatar):
        return None

    
    def _PetAvatarPanel__handleClose(self):
        self.notify.debug('__handleClose(): doId=%s' % self.avatar.doId)
        self.cleanup()
        AvatarPanel.currentAvatarPanel = None
        if self.friendsListShown:
            self.FriendsListPanel.showFriendsList()
        

    
    def _PetAvatarPanel__fillPetInfo(self, avatar):
        self.notify.debug('__fillPetInfo(): doId=%s' % avatar.doId)
        self.petView = self.frame.attachNewNode('petView')
        self.petView.setPos(0, 0, 5.4000000000000004)
        self.petModel = Pet.Pet(forGui = 1)
        self.petModel.setDNA(avatar.getDNA())
        self.petModel.fitAndCenterHead(3.5750000000000002, forGui = 1)
        self.petModel.reparentTo(self.petView)
        self.petModel.enterNeutralHappy()
        self.petModel.startBlink()
        self.nameLabel = DirectLabel(parent = self.frame, pos = (0, 0, 5.2000000000000002), relief = None, text = avatar.getName(), text_font = avatar.getFont(), text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0), text_scale = 0.40000000000000002, text_wordwrap = 7.5, text_shadow = (1, 1, 1, 1))
        self.stateLabel = DirectLabel(parent = self.frame, pos = TTLocalizer.PAPstateLabelPos, relief = None, text = '', text_font = avatar.getFont(), text_fg = Vec4(0, 0, 0, 1), text_scale = TTLocalizer.PAPstateLabel, text_wordwrap = TTLocalizer.PAPstateLabelwordwrap, text_shadow = (1, 1, 1, 1))
        self._PetAvatarPanel__refreshPetInfo(avatar)

    
    def _PetAvatarPanel__refreshPetInfo(self, avatar):
        self.notify.debug('__refreshPetInfo(): doId=%s' % avatar.doId)
        if avatar.doId != self.avatar.doId:
            return None
        
        if not (self.petIsLocal):
            self.avatar.updateOfflineMood()
        
        mood = self.avatar.getDominantMood()
        self.stateLabel['text'] = TTLocalizer.PetMoodAdjectives[mood]
        self.nameLabel['text'] = avatar.getName()


