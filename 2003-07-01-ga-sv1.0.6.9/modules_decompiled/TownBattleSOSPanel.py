# File: T (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from DirectGui import *
import PandaObject
import DirectNotifyGlobal
import StateData
import ToontownGlobals
import Localizer

class TownBattleSOSPanel(DirectFrame, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattleSOSPanel')
    
    def __init__(self, doneEvent):
        DirectFrame.__init__(self, relief = None)
        self.initialiseoptions(TownBattleSOSPanel)
        StateData.StateData.__init__(self, doneEvent)
        self.friends = { }
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.90000000000000002, 1, 1)
        self.textDisabledColor = Vec4(0.40000000000000002, 0.80000000000000004, 0.40000000000000002, 1)

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.isLoaded = 1
        bgd = loader.loadModelOnce('phase_3/models/gui/dialog_box_gui')
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        auxGui = loader.loadModelOnce('phase_3.5/models/gui/battle_gui')
        self['image'] = bgd
        self['image_scale'] = (0.80000000000000004, 1.0, 0.59999999999999998)
        self['image_pos'] = (0.0, 0.10000000000000001, -0.080000000000000002)
        self['image_color'] = Vec4(1.0, 0.20000000000000001, 0.20000000000000001, 1.0)
        self.title = DirectLabel(parent = self, relief = None, text = Localizer.TownBattleSOSNoFriends, text_scale = 0.059999999999999998, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_wordwrap = 5.0, pos = (-0.20000000000000001, 0.0, 0.059999999999999998))
        self.scrollList = DirectScrolledList(parent = self, relief = None, incButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_pos = (0.0, 0.0, -0.316), incButton_image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), incButton_scale = (1.0, 1.0, -1.0), decButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_pos = (0.0, 0.0, 0.11700000000000001), decButton_image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), itemFrame_pos = (-0.17000000000000001, 0.0, 0.044999999999999998), itemFrame_relief = None, numItemsVisible = 8, items = [], pos = (0.20000000000000001, 0.0, 0.02))
        clipper = PlaneNode('clipper')
        clipper.setPlane(Plane(Vec3(-1, 0, 0), Point3(0.20000000000000001, 0, 0)))
        self.scrollList.attachNewNode(clipper)
        cpa = ClipPlaneAttrib.make(ClipPlaneAttrib.OSet, clipper)
        self.scrollList.node().setAttrib(cpa)
        self.close = DirectButton(parent = self, relief = None, image = (auxGui.find('**/PckMn_BackBtn'), auxGui.find('**/PckMn_BackBtn_Dn'), auxGui.find('**/PckMn_BackBtn_Rlvr')), pos = (-0.20000000000000001, 0.0, -0.25), scale = 1.05, text = Localizer.TownBattleSOSBack, text_scale = 0.050000000000000003, text_pos = (0.01, -0.012), text_fg = Vec4(0, 0, 0.80000000000000004, 1), command = self._TownBattleSOSPanel__close)
        gui.removeNode()
        auxGui.removeNode()
        bgd.removeNode()
        self.hide()

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        self.isLoaded = 0
        self.exit()
        del self.title
        del self.scrollList
        del self.close
        del self.friends
        DirectFrame.destroy(self)

    
    def makeFriendButton(self, friendPair):
        (friendId, flags) = friendPair
        handle = toonbase.tcr.identifyFriend(friendId)
        if handle == None:
            toonbase.tcr.fillUpFriendsMap()
            return None
        
        friendName = handle.getName()
        fg = Vec4(0.0, 0.0, 0.0, 1.0)
        return DirectButton(relief = None, text = friendName, text_scale = 0.040000000000000001, text_align = TextNode.ALeft, text_fg = fg, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, command = self._TownBattleSOSPanel__choseFriend, extraArgs = [
            friendId])

    
    def enter(self):
        if self.isEntered == 1:
            return None
        
        self.isEntered = 1
        if self.isLoaded == 0:
            self.load()
        
        toonbase.localToon.obscureFriendsListButton(1)
        self._TownBattleSOSPanel__updateScrollList()
        self.show()
        self.accept('friendOnline', self._TownBattleSOSPanel__friendOnline)
        self.accept('friendOffline', self._TownBattleSOSPanel__friendOffline)
        self.accept('friendsListChanged', self._TownBattleSOSPanel__friendsListChanged)
        self.accept('friendsMapComplete', self._TownBattleSOSPanel__friendsListChanged)
        return None

    
    def exit(self):
        if self.isEntered == 0:
            return None
        
        self.isEntered = 0
        self.hide()
        self.ignore('friendOnline')
        self.ignore('friendOffline')
        self.ignore('friendsListChanged')
        self.ignore('friendsMapComplete')
        toonbase.localToon.obscureFriendsListButton(-1)
        messenger.send(self.doneEvent)
        return None

    
    def _TownBattleSOSPanel__close(self):
        doneStatus = { }
        doneStatus['mode'] = 'Back'
        messenger.send(self.doneEvent, [
            doneStatus])

    
    def _TownBattleSOSPanel__choseFriend(self, friendId):
        doneStatus = { }
        doneStatus['mode'] = 'Friend'
        doneStatus['friend'] = friendId
        messenger.send(self.doneEvent, [
            doneStatus])

    
    def _TownBattleSOSPanel__updateScrollList(self):
        wasEmpty = len(self.friends) == 0
        newFriends = []
        for friendPair in toonbase.localToon.friendsList:
            if toonbase.tcr.isFriendOnline(friendPair[0]):
                newFriends.append(friendPair)
            
        
        for friendPair in self.friends.keys():
            if friendPair not in newFriends:
                friendButton = self.friends[friendPair]
                self.scrollList.removeItem(friendButton)
                friendButton.destroy()
                del self.friends[friendPair]
            
        
        for friendPair in newFriends:
            if friendPair not in self.friends.keys():
                friendButton = self.makeFriendButton(friendPair)
                if friendButton:
                    self.scrollList.addItem(friendButton)
                    self.friends[friendPair] = friendButton
                
            
        
        isEmpty = len(self.friends) == 0
        if wasEmpty != isEmpty:
            if isEmpty:
                self.title['text'] = Localizer.TownBattleSOSNoFriends
            else:
                self.title['text'] = Localizer.TownBattleSOSWhichFriend
        
        return None

    
    def _TownBattleSOSPanel__friendOnline(self, doId):
        self._TownBattleSOSPanel__updateScrollList()

    
    def _TownBattleSOSPanel__friendOffline(self, doId):
        self._TownBattleSOSPanel__updateScrollList()

    
    def _TownBattleSOSPanel__friendsListChanged(self):
        self._TownBattleSOSPanel__updateScrollList()


