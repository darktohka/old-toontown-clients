# File: A (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.gui.DirectGui import *
from direct.showbase import PandaObject
import Avatar
from direct.distributed import DistributedObject

class AvatarPanel(PandaObject.PandaObject):
    currentAvatarPanel = None
    
    def __init__(self, avatar, FriendsListPanel = None):
        if AvatarPanel.currentAvatarPanel:
            AvatarPanel.currentAvatarPanel.cleanup()
        
        AvatarPanel.currentAvatarPanel = self
        self.friendsListShown = False
        self.FriendsListPanel = FriendsListPanel
        if FriendsListPanel:
            self.friendsListShown = FriendsListPanel.isFriendsListShown()
            FriendsListPanel.hideFriendsList()
        
        self.avatar = avatar
        self.avName = avatar.getName()
        if hasattr(avatar, 'uniqueName'):
            self.avId = avatar.doId
            self.avDisableName = avatar.uniqueName('disable')
            self.avGenerateName = avatar.uniqueName('generate')
            self.avHpChangeName = avatar.uniqueName('hpChange')
            if base.cr.doId2do.has_key(self.avId):
                self.avatar = base.cr.doId2do[self.avId]
            
        else:
            self.avDisableName = None
            self.avGenerateName = None
            self.avHpChangeName = None
            self.avId = None
        if self.avDisableName:
            self.accept(self.avDisableName, self._AvatarPanel__handleDisableAvatar)
        

    
    def cleanup(self):
        if AvatarPanel.currentAvatarPanel != self:
            return None
        
        if self.avDisableName:
            self.ignore(self.avDisableName)
        
        if self.avGenerateName:
            self.ignore(self.avGenerateName)
        
        if self.avHpChangeName:
            self.ignore(self.avHpChangeName)
        
        AvatarPanel.currentAvatarPanel = None
        return None

    
    def _AvatarPanel__handleClose(self):
        self.cleanup()
        AvatarPanel.currentAvatarPanel = None
        if self.friendsListShown:
            self.FriendsListPanel.showFriendsList()
        

    
    def _AvatarPanel__handleDisableAvatar(self):
        self.cleanup()
        AvatarPanel.currentAvatarPanel = None


