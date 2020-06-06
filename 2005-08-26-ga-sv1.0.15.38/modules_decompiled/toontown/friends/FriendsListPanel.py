# File: F (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.gui.DirectGui import *
from direct.fsm import StateData
from toontown.toon import ToonAvatarPanel
from otp.friends import FriendSecret
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
FLPPets = 1
FLPOnline = 2
FLPAll = 3
FLPEnemies = 4
leftmostPanel = FLPPets
rightmostPanel = FLPAll
globalFriendsList = None

def showFriendsList():
    global globalFriendsList
    if globalFriendsList == None:
        globalFriendsList = FriendsListPanel()
    
    globalFriendsList.enter()


def hideFriendsList():
    if globalFriendsList != None:
        globalFriendsList.exit()
    


def showFriendsListTutorial():
    global globalFriendsList
    if globalFriendsList == None:
        globalFriendsList = FriendsListPanel()
    
    globalFriendsList.enter()
    globalFriendsList.closeCommand = globalFriendsList.close['command']
    globalFriendsList.close['command'] = None


def hideFriendsListTutorial():
    if globalFriendsList != None:
        if hasattr(globalFriendsList, 'closeCommand'):
            globalFriendsList.close['command'] = globalFriendsList.closeCommand
        
        globalFriendsList.exit()
    


def isFriendsListShown():
    if globalFriendsList != None:
        return globalFriendsList.isEntered
    
    return 0


def unloadFriendsList():
    global globalFriendsList
    if globalFriendsList != None:
        globalFriendsList.unload()
        globalFriendsList = None
    


class FriendsListPanel(DirectFrame, StateData.StateData):
    
    def __init__(self):
        DirectFrame.__init__(self, relief = None)
        self.initialiseoptions(FriendsListPanel)
        StateData.StateData.__init__(self, 'friends-list-done')
        self.friends = { }
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.90000000000000002, 1, 1)
        self.textDisabledColor = Vec4(0.40000000000000002, 0.80000000000000004, 0.40000000000000002, 1)
        self.panelType = FLPOnline

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.isLoaded = 1
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        auxGui = loader.loadModelOnce('phase_3.5/models/gui/avatar_panel_gui')
        self.title = DirectLabel(parent = self, relief = None, text = '', text_scale = 0.040000000000000001, text_fg = (0, 0.10000000000000001, 0.40000000000000002, 1), pos = (0.0070000000000000001, 0.0, 0.20000000000000001))
        background_image = gui.find('**/FriendsBox_Open')
        self['image'] = background_image
        self.setPos(1.1000000000000001, 0, 0.54000000000000004)
        self.scrollList = DirectScrolledList(parent = self, relief = None, incButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_pos = (0.0, 0.0, -0.316), incButton_image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), incButton_scale = (1.0, 1.0, -1.0), decButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_pos = (0.0, 0.0, 0.11700000000000001), decButton_image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), itemFrame_pos = (-0.17000000000000001, 0.0, 0.059999999999999998), itemFrame_relief = None, numItemsVisible = 8, items = [])
        clipper = PlaneNode('clipper')
        clipper.setPlane(Plane(Vec3(-1, 0, 0), Point3(0.20000000000000001, 0, 0)))
        self.scrollList.attachNewNode(clipper)
        cpa = ClipPlaneAttrib.make(ClipPlaneAttrib.OSet, clipper)
        self.scrollList.node().setAttrib(cpa)
        self.close = DirectButton(parent = self, relief = None, image = (auxGui.find('**/CloseBtn_UP'), auxGui.find('**/CloseBtn_DN'), auxGui.find('**/CloseBtn_Rllvr')), pos = (0.01, 0, -0.38), command = self._FriendsListPanel__close)
        self.left = DirectButton(parent = self, relief = None, image = (gui.find('**/Horiz_Arrow_UP'), gui.find('**/Horiz_Arrow_DN'), gui.find('**/Horiz_Arrow_Rllvr'), gui.find('**/Horiz_Arrow_UP')), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), pos = (-0.14999999999999999, 0.0, -0.38), scale = (-1.0, 1.0, 1.0), command = self._FriendsListPanel__left)
        self.right = DirectButton(parent = self, relief = None, image = (gui.find('**/Horiz_Arrow_UP'), gui.find('**/Horiz_Arrow_DN'), gui.find('**/Horiz_Arrow_Rllvr'), gui.find('**/Horiz_Arrow_UP')), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), pos = (0.17000000000000001, 0, -0.38), command = self._FriendsListPanel__right)
        self.newFriend = DirectButton(parent = self, relief = None, pos = (-0.14000000000000001, 0.0, 0.14000000000000001), image = (auxGui.find('**/Frnds_Btn_UP'), auxGui.find('**/Frnds_Btn_DN'), auxGui.find('**/Frnds_Btn_RLVR')), text = ('', TTLocalizer.FriendsListPanelNewFriend, TTLocalizer.FriendsListPanelNewFriend), text_scale = 0.044999999999999998, text_fg = (0, 0, 0, 1), text_bg = (1, 1, 1, 1), text_pos = (0.10000000000000001, -0.085000000000000006), textMayChange = 0, command = self._FriendsListPanel__newFriend)
        self.secrets = DirectButton(parent = self, relief = None, pos = (0.152, 0.0, 0.14000000000000001), image = (auxGui.find('**/ChtBx_ChtBtn_UP'), auxGui.find('**/ChtBx_ChtBtn_DN'), auxGui.find('**/ChtBx_ChtBtn_RLVR')), text = ('', TTLocalizer.FriendsListPanelSecrets, TTLocalizer.FriendsListPanelSecrets), text_scale = 0.044999999999999998, text_fg = (0, 0, 0, 1), text_bg = (1, 1, 1, 1), text_pos = (-0.040000000000000001, -0.085000000000000006), textMayChange = 0, command = self._FriendsListPanel__secrets)
        gui.removeNode()
        auxGui.removeNode()

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        self.isLoaded = 0
        self.exit()
        del self.title
        del self.scrollList
        del self.close
        del self.left
        del self.right
        del self.friends
        DirectFrame.destroy(self)

    
    def makeFriendButton(self, friendPair):
        (friendId, flags) = friendPair
        handle = base.cr.identifyFriend(friendId)
        if handle == None:
            base.cr.fillUpFriendsMap()
            return None
        
        friendName = handle.getName()
        colorCode = NametagGroup.CCNoChat
        if flags & ToontownGlobals.FriendChat:
            colorCode = NametagGroup.CCNormal
        
        fg = NametagGlobals.getNameFg(colorCode, PGButton.SInactive)
        return DirectButton(relief = None, text = friendName, text_scale = 0.040000000000000001, text_align = TextNode.ALeft, text_fg = fg, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, textMayChange = 0, command = self._FriendsListPanel__choseFriend, extraArgs = [
            friendId])

    
    def enter(self):
        if self.isEntered == 1:
            return None
        
        self.isEntered = 1
        if self.isLoaded == 0:
            self.load()
        
        base.localAvatar.obscureFriendsListButton(1)
        if ToonAvatarPanel.ToonAvatarPanel.currentAvatarPanel:
            ToonAvatarPanel.ToonAvatarPanel.currentAvatarPanel.cleanup()
            ToonAvatarPanel.ToonAvatarPanel.currentAvatarPanel = None
        
        self._FriendsListPanel__updateScrollList()
        self._FriendsListPanel__updateTitle()
        self._FriendsListPanel__updateArrows()
        self.show()
        self.accept('friendOnline', self._FriendsListPanel__friendOnline)
        self.accept('friendOffline', self._FriendsListPanel__friendOffline)
        self.accept('friendsListChanged', self._FriendsListPanel__friendsListChanged)
        self.accept('ignoreListChanged', self._FriendsListPanel__ignoreListChanged)
        self.accept('friendsMapComplete', self._FriendsListPanel__friendsListChanged)
        return None

    
    def exit(self):
        if self.isEntered == 0:
            return None
        
        self.isEntered = 0
        self.hide()
        base.cr.cleanPetsFromFriendsMap()
        self.ignore('friendOnline')
        self.ignore('friendOffline')
        self.ignore('friendsListChanged')
        self.ignore('ignoreListChanged')
        self.ignore('friendsMapComplete')
        base.localAvatar.obscureFriendsListButton(-1)
        messenger.send(self.doneEvent)
        return None

    
    def _FriendsListPanel__close(self):
        messenger.send('wakeup')
        self.exit()

    
    def _FriendsListPanel__left(self):
        messenger.send('wakeup')
        if self.panelType > leftmostPanel:
            self.panelType -= 1
        
        self._FriendsListPanel__updateScrollList()
        self._FriendsListPanel__updateTitle()
        self._FriendsListPanel__updateArrows()

    
    def _FriendsListPanel__right(self):
        messenger.send('wakeup')
        if self.panelType < rightmostPanel:
            self.panelType += 1
        
        self._FriendsListPanel__updateScrollList()
        self._FriendsListPanel__updateTitle()
        self._FriendsListPanel__updateArrows()

    
    def _FriendsListPanel__secrets(self):
        messenger.send('wakeup')
        FriendSecret.showFriendSecret()

    
    def _FriendsListPanel__newFriend(self):
        messenger.send('wakeup')
        messenger.send('friendAvatar', [
            None,
            None,
            None])

    
    def _FriendsListPanel__choseFriend(self, friendId):
        messenger.send('wakeup')
        handle = base.cr.identifyFriend(friendId)
        if handle != None:
            self.notify.info("Clicked on name in friend's list. doId = %s" % handle.doId)
            messenger.send('clickedNametag', [
                handle])
        

    
    def _FriendsListPanel__updateScrollList(self):
        if self.panelType == FLPOnline:
            newFriends = []
            if base.wantPets and base.localAvatar.hasPet():
                newFriends.append((base.localAvatar.getPetId(), 0))
            
            for friendPair in base.localAvatar.friendsList:
                if base.cr.isFriendOnline(friendPair[0]):
                    newFriends.append(friendPair)
                
            
        elif self.panelType == FLPAll:
            newFriends = []
            if base.wantPets and base.localAvatar.hasPet():
                newFriends.append((base.localAvatar.getPetId(), 0))
            
            newFriends += base.localAvatar.friendsList
        elif self.panelType == FLPPets:
            newFriends = []
            for (objId, obj) in base.cr.doId2do.items():
                DistributedPet = DistributedPet
                import toontown.pets
                if isinstance(obj, DistributedPet.DistributedPet):
                    friendPair = (objId, 0)
                    newFriends.append(friendPair)
                
            
        else:
            newFriends = []
            for ignored in base.localAvatar.ignoreList:
                newFriends.append((ignored, 0))
            
        for friendPair in self.friends.keys():
            if friendPair not in newFriends:
                friendButton = self.friends[friendPair]
                self.scrollList.removeItem(friendButton, refresh = 0)
                friendButton.destroy()
                del self.friends[friendPair]
            
        
        for friendPair in newFriends:
            if not self.friends.has_key(friendPair):
                friendButton = self.makeFriendButton(friendPair)
                if friendButton:
                    self.scrollList.addItem(friendButton, refresh = 0)
                    self.friends[friendPair] = friendButton
                
            
        
        self.scrollList.refresh()

    
    def _FriendsListPanel__updateTitle(self):
        if self.panelType == FLPOnline:
            self.title['text'] = TTLocalizer.FriendsListPanelOnlineFriends
        elif self.panelType == FLPAll:
            self.title['text'] = TTLocalizer.FriendsListPanelAllFriends
        elif self.panelType == FLPPets:
            self.title['text'] = TTLocalizer.FriendsListPanelPets
        else:
            self.title['text'] = TTLocalizer.FriendsListPanelIgnoredFriends
        self.title.resetFrameSize()

    
    def _FriendsListPanel__updateArrows(self):
        if self.panelType == leftmostPanel:
            self.left['state'] = 'inactive'
        else:
            self.left['state'] = 'normal'
        if self.panelType == rightmostPanel:
            self.right['state'] = 'inactive'
        else:
            self.right['state'] = 'normal'

    
    def _FriendsListPanel__friendOnline(self, doId):
        if self.panelType == FLPOnline:
            self._FriendsListPanel__updateScrollList()
        

    
    def _FriendsListPanel__friendOffline(self, doId):
        if self.panelType == FLPOnline:
            self._FriendsListPanel__updateScrollList()
        

    
    def _FriendsListPanel__friendsListChanged(self):
        if self.panelType != FLPEnemies:
            self._FriendsListPanel__updateScrollList()
        

    
    def _FriendsListPanel__ignoreListChanged(self):
        if self.panelType == FLPEnemies:
            self._FriendsListPanel__updateScrollList()
        


