# File: F (Python 2.2)

from pandac.PandaModules import *
import FriendsListPanel
import FriendInviter
import FriendInvitee
from direct.directnotify import DirectNotifyGlobal
from toontown.toon import ToonTeleportPanel
from otp.friends import FriendSecret
from toontown.pets import PetAvatarPanel
from toontown.toon import ToonAvatarPanel
from toontown.suit import SuitAvatarPanel
from toontown.toon import ToonDNA
from toontown.toon import ToonAvatarDetailPanel
from toontown.toonbase import ToontownGlobals
from toontown.toon import Toon
import FriendHandle

class FriendsListManager:
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendsListManager')
    
    def __init__(self):
        self.avatarPanel = None
        self._preserveFriendsList = False
        self._entered = False

    
    def load(self):
        pass

    
    def unload(self):
        self.exitFLM()
        if self.avatarPanel:
            del self.avatarPanel
        
        FriendInviter.unloadFriendInviter()
        ToonAvatarDetailPanel.unloadAvatarDetail()
        ToonTeleportPanel.unloadTeleportPanel()

    
    def enterFLM(self):
        self.notify.info('FriendsListManager: enterFLM()')
        if self._preserveFriendsList:
            self._preserveFriendsList = 0
            return None
        
        self._entered = True
        self.accept('openFriendsList', self._FriendsListManager__openFriendsList)
        self.accept('clickedNametag', self._FriendsListManager__handleClickedNametag)
        base.localAvatar.setFriendsListButtonActive(1)
        NametagGlobals.setMasterNametagsActive(1)
        self.accept('gotoAvatar', self._FriendsListManager__handleGotoAvatar)
        self.accept('friendAvatar', self._FriendsListManager__handleFriendAvatar)
        self.accept('avatarDetails', self._FriendsListManager__handleAvatarDetails)
        self.accept('friendInvitation', self._FriendsListManager__handleFriendInvitation)
        if base.cr.friendManager:
            base.cr.friendManager.setAvailable(1)
        

    
    def exitFLM(self):
        self.notify.info('FriendsListManager: exitFLM()')
        if self._preserveFriendsList:
            return None
        
        if not (self._entered):
            return None
        
        self._entered = False
        self.ignore('openFriendsList')
        self.ignore('clickedNametag')
        base.localAvatar.setFriendsListButtonActive(0)
        NametagGlobals.setMasterNametagsActive(0)
        if self.avatarPanel:
            self.avatarPanel.cleanup()
            self.avatarPanel = None
        
        self.ignore('gotoAvatar')
        self.ignore('friendAvatar')
        self.ignore('avatarDetails')
        FriendsListPanel.hideFriendsList()
        FriendSecret.hideFriendSecret()
        if base.cr.friendManager:
            base.cr.friendManager.setAvailable(0)
        
        self.ignore('friendInvitation')
        FriendInviter.hideFriendInviter()
        ToonAvatarDetailPanel.hideAvatarDetail()
        ToonTeleportPanel.hideTeleportPanel()

    
    def _FriendsListManager__openFriendsList(self):
        FriendsListPanel.showFriendsList()

    
    def _FriendsListManager__handleClickedNametag(self, avatar):
        self.notify.info('__handleClickedNametag. doId = %s' % avatar.doId)
        if avatar.isPet():
            self.avatarPanel = PetAvatarPanel.PetAvatarPanel(avatar)
        elif isinstance(avatar, Toon.Toon) or isinstance(avatar, FriendHandle.FriendHandle):
            self.avatarPanel = ToonAvatarPanel.ToonAvatarPanel(avatar)
        else:
            self.avatarPanel = SuitAvatarPanel.SuitAvatarPanel(avatar)

    
    def _FriendsListManager__handleGotoAvatar(self, avId, avName, avDisableName):
        ToonTeleportPanel.showTeleportPanel(avId, avName, avDisableName)

    
    def _FriendsListManager__handleFriendAvatar(self, avId, avName, avDisableName):
        FriendInviter.showFriendInviter(avId, avName, avDisableName)

    
    def _FriendsListManager__handleFriendInvitation(self, avId, avName, inviterDna, context):
        dna = ToonDNA.ToonDNA()
        dna.makeFromNetString(inviterDna)
        FriendInvitee.FriendInvitee(avId, avName, dna, context)

    
    def _FriendsListManager__handleAvatarDetails(self, avId, avName):
        ToonAvatarDetailPanel.showAvatarDetail(avId, avName)

    
    def preserveFriendsList(self):
        self.notify.info('Preserving Friends List')
        self._preserveFriendsList = True


