# File: F (Python 2.2)

from PandaModules import *
import FriendsListPanel
import FriendInviter
import FriendInvitee
import TeleportPanel
import FriendSecret
import AvatarPanel
import AvatarDetailPanel
import ToontownGlobals

class FriendsListManager:
    
    def __init__(self):
        self.avatarPanel = None
        return None

    
    def load(self):
        return None

    
    def unload(self):
        if self.avatarPanel:
            del self.avatarPanel
        
        FriendInviter.unloadFriendInviter()
        AvatarDetailPanel.unloadAvatarDetail()
        TeleportPanel.unloadTeleportPanel()
        return None

    
    def enter(self):
        self.accept('openFriendsList', self._FriendsListManager__openFriendsList)
        self.accept('clickedNametag', self._FriendsListManager__handleClickedNametag)
        toonbase.localToon.setFriendsListButtonActive(1)
        NametagGlobals.setMasterNametagsActive(1)
        self.accept('gotoAvatar', self._FriendsListManager__handleGotoAvatar)
        self.accept('friendAvatar', self._FriendsListManager__handleFriendAvatar)
        self.accept('avatarDetails', self._FriendsListManager__handleAvatarDetails)
        self.accept('friendInvitation', self._FriendsListManager__handleFriendInvitation)
        if toonbase.tcr.friendManager:
            toonbase.tcr.friendManager.setAvailable(1)
        
        return None

    
    def exit(self):
        self.ignore('openFriendsList')
        self.ignore('clickedNametag')
        toonbase.localToon.setFriendsListButtonActive(0)
        NametagGlobals.setMasterNametagsActive(0)
        if self.avatarPanel:
            self.avatarPanel.cleanup()
            self.avatarPanel = None
        
        self.ignore('gotoAvatar')
        self.ignore('friendAvatar')
        self.ignore('avatarDetails')
        FriendsListPanel.hideFriendsList()
        FriendSecret.hideFriendSecret()
        if toonbase.tcr.friendManager:
            toonbase.tcr.friendManager.setAvailable(0)
        
        self.ignore('friendInvitation')
        FriendInviter.hideFriendInviter()
        AvatarDetailPanel.hideAvatarDetail()
        TeleportPanel.hideTeleportPanel()
        return None

    
    def _FriendsListManager__openFriendsList(self):
        FriendsListPanel.showFriendsList()
        return None

    
    def _FriendsListManager__handleClickedNametag(self, avatar):
        self.avatarPanel = AvatarPanel.AvatarPanel(avatar)

    
    def _FriendsListManager__handleGotoAvatar(self, avId, avName, avDisableName):
        TeleportPanel.showTeleportPanel(avId, avName, avDisableName)
        return None

    
    def _FriendsListManager__handleFriendAvatar(self, avId, avName, avDisableName):
        FriendInviter.showFriendInviter(avId, avName, avDisableName)
        return None

    
    def _FriendsListManager__handleFriendInvitation(self, avId, avName, dna, context):
        FriendInvitee.FriendInvitee(avId, avName, dna, context)
        return None

    
    def _FriendsListManager__handleAvatarDetails(self, avId, avName):
        AvatarDetailPanel.showAvatarDetail(avId, avName)
        return None


