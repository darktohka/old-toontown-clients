# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from direct.showbase import PandaObject
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import types
from toontown.toon import NPCToons
from toontown.toon import NPCFriendPanel
from toontown.toonbase import ToontownBattleGlobals

class TownBattleSOSPanel(DirectFrame, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattleSOSPanel')
    
    def __init__(self, doneEvent):
        DirectFrame.__init__(self, relief = None)
        self.initialiseoptions(TownBattleSOSPanel)
        StateData.StateData.__init__(self, doneEvent)
        self.friends = { }
        self.NPCFriends = { }
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.90000000000000002, 1, 1)
        self.textDisabledColor = Vec4(0.40000000000000002, 0.80000000000000004, 0.40000000000000002, 1)
        self.bldg = 0
        self.chosenNPCToons = []

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.isLoaded = 1
        bgd = loader.loadModelOnce('phase_3.5/models/gui/frame')
        gui = loader.loadModelOnce('phase_3.5/models/gui/frame4names')
        scrollGui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        backGui = loader.loadModelOnce('phase_3.5/models/gui/battle_gui')
        self['image'] = bgd
        self['image_pos'] = (0.0, 0.10000000000000001, -0.080000000000000002)
        self.setScale(0.29999999999999999)
        self.title = DirectLabel(parent = self, relief = None, text = TTLocalizer.TownBattleSOSNoFriends, text_scale = 0.40000000000000002, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), pos = (0.0, 0.0, 1.45))
        self.NPCFriendPanel = NPCFriendPanel.NPCFriendPanel(parent = self, doneEvent = self.doneEvent)
        self.NPCFriendPanel.setPos(-0.75, 0, -0.14999999999999999)
        self.NPCFriendPanel.setScale(0.32500000000000001)
        self.NPCFriendsLabel = DirectLabel(parent = self, relief = None, text = TTLocalizer.TownBattleSOSNPCFriends, text_scale = 0.29999999999999999, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), pos = (-0.75, 0.0, -1.8500000000000001))
        self.scrollList = DirectScrolledList(parent = self, relief = None, image = gui.find('**/frame4names'), image_scale = (0.11, 1, 0.10000000000000001), text = TTLocalizer.FriendsListPanelOnlineFriends, text_scale = 0.040000000000000001, text_pos = (-0.02, 0.27500000000000002), text_fg = (0, 0, 0, 1), incButton_image = (scrollGui.find('**/FndsLst_ScrollUp'), scrollGui.find('**/FndsLst_ScrollDN'), scrollGui.find('**/FndsLst_ScrollUp_Rllvr'), scrollGui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_pos = (0.0, 0.0, -0.29999999999999999), incButton_image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), incButton_scale = (1.0, 1.0, -1.0), decButton_image = (scrollGui.find('**/FndsLst_ScrollUp'), scrollGui.find('**/FndsLst_ScrollDN'), scrollGui.find('**/FndsLst_ScrollUp_Rllvr'), scrollGui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_pos = (0.0, 0.0, 0.17499999999999999), decButton_image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), itemFrame_pos = (-0.17000000000000001, 0.0, 0.11), itemFrame_relief = None, numItemsVisible = 9, items = [], pos = (2.2999999999999998, 0.0, 0.025000000000000001), scale = 3.5)
        clipper = PlaneNode('clipper')
        clipper.setPlane(Plane(Vec3(-1, 0, 0), Point3(0.32000000000000001, 0, 0)))
        self.scrollList.component('itemFrame').attachNewNode(clipper)
        cpa = ClipPlaneAttrib.make(ClipPlaneAttrib.OSet, clipper)
        self.scrollList.component('itemFrame').node().setAttrib(cpa)
        self.close = DirectButton(parent = self, relief = None, image = (backGui.find('**/PckMn_BackBtn'), backGui.find('**/PckMn_BackBtn_Dn'), backGui.find('**/PckMn_BackBtn_Rlvr')), pos = (2.2000000000000002, 0.0, -1.6499999999999999), scale = 3, text = TTLocalizer.TownBattleSOSBack, text_scale = 0.050000000000000003, text_pos = (0.01, -0.012), text_fg = Vec4(0, 0, 0.80000000000000004, 1), command = self._TownBattleSOSPanel__close)
        gui.removeNode()
        scrollGui.removeNode()
        backGui.removeNode()
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
        del self.NPCFriends
        DirectFrame.destroy(self)

    
    def makeFriendButton(self, friendPair):
        (friendId, flags) = friendPair
        handle = base.cr.identifyFriend(friendId)
        if handle == None:
            base.cr.fillUpFriendsMap()
            return None
        
        friendName = handle.getName()
        fg = Vec4(0.0, 0.0, 0.0, 1.0)
        return DirectButton(relief = None, text = friendName, text_scale = 0.040000000000000001, text_align = TextNode.ALeft, text_fg = fg, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, command = self._TownBattleSOSPanel__choseFriend, extraArgs = [
            friendId])

    
    def makeNPCFriendButton(self, NPCFriendId, numCalls):
        if not TTLocalizer.NPCToonNames.has_key(NPCFriendId):
            return None
        
        friendName = TTLocalizer.NPCToonNames[NPCFriendId]
        friendName += ' %d' % numCalls
        fg = Vec4(0.0, 0.0, 0.0, 1.0)
        return DirectButton(relief = None, text = friendName, text_scale = 0.040000000000000001, text_align = TextNode.ALeft, text_fg = fg, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, command = self._TownBattleSOSPanel__choseNPCFriend, extraArgs = [
            NPCFriendId])

    
    def enter(self, canLure = 1, canTrap = 1):
        if self.isEntered == 1:
            return None
        
        self.isEntered = 1
        if self.isLoaded == 0:
            self.load()
        
        self.canLure = canLure
        self.canTrap = canTrap
        self.factoryToonIdList = None
        messenger.send('SOSPanelEnter', [
            self])
        self._TownBattleSOSPanel__updateScrollList()
        self._TownBattleSOSPanel__updateNPCFriendsPanel()
        self._TownBattleSOSPanel__updateTitleText()
        self.show()
        self.accept('friendOnline', self._TownBattleSOSPanel__friendOnline)
        self.accept('friendOffline', self._TownBattleSOSPanel__friendOffline)
        self.accept('friendsListChanged', self._TownBattleSOSPanel__friendsListChanged)
        self.accept('friendsMapComplete', self._TownBattleSOSPanel__friendsListChanged)

    
    def exit(self):
        if self.isEntered == 0:
            return None
        
        self.isEntered = 0
        self.hide()
        self.ignore('friendOnline')
        self.ignore('friendOffline')
        self.ignore('friendsListChanged')
        self.ignore('friendsMapComplete')
        messenger.send(self.doneEvent)

    
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

    
    def _TownBattleSOSPanel__choseNPCFriend(self, friendId):
        doneStatus = { }
        doneStatus['mode'] = 'NPCFriend'
        doneStatus['friend'] = friendId
        self.chosenNPCToons.append(friendId)
        messenger.send(self.doneEvent, [
            doneStatus])

    
    def setFactoryToonIdList(self, toonIdList):
        self.factoryToonIdList = toonIdList[:]

    
    def _TownBattleSOSPanel__updateScrollList(self):
        newFriends = []
        if not (self.bldg) or self.factoryToonIdList is not None:
            for friendPair in base.localAvatar.friendsList:
                if base.cr.isFriendOnline(friendPair[0]):
                    if self.factoryToonIdList is None or friendPair[0] in self.factoryToonIdList:
                        newFriends.append(friendPair)
                    
                
            
        
        for friendPair in self.friends.keys():
            if friendPair not in newFriends:
                friendButton = self.friends[friendPair]
                self.scrollList.removeItem(friendButton)
                if not friendButton.isEmpty():
                    friendButton.destroy()
                
                del self.friends[friendPair]
            
        
        for friendPair in newFriends:
            if not self.friends.has_key(friendPair):
                friendButton = self.makeFriendButton(friendPair)
                if friendButton:
                    self.scrollList.addItem(friendButton)
                    self.friends[friendPair] = friendButton
                
            
        

    
    def _TownBattleSOSPanel__updateNPCFriendsPanel(self):
        self.NPCFriends = { }
        for (friend, count) in base.localAvatar.NPCFriendsDict.items():
            track = NPCToons.getNPCTrack(friend)
            if track == ToontownBattleGlobals.LURE_TRACK and self.canLure == 0 and track == ToontownBattleGlobals.TRAP_TRACK and self.canTrap == 0:
                self.NPCFriends[friend] = 0
            else:
                self.NPCFriends[friend] = count
        
        self.NPCFriendPanel.update(self.NPCFriends, fCallable = 1)

    
    def _TownBattleSOSPanel__updateTitleText(self):
        if len(self.friends) == 0:
            pass
        isEmpty = len(self.NPCFriends) == 0
        if isEmpty:
            self.title['text'] = TTLocalizer.TownBattleSOSNoFriends
        else:
            self.title['text'] = TTLocalizer.TownBattleSOSWhichFriend

    
    def _TownBattleSOSPanel__friendOnline(self, doId):
        self._TownBattleSOSPanel__updateScrollList()
        self._TownBattleSOSPanel__updateTitleText()

    
    def _TownBattleSOSPanel__friendOffline(self, doId):
        self._TownBattleSOSPanel__updateScrollList()
        self._TownBattleSOSPanel__updateTitleText()

    
    def _TownBattleSOSPanel__friendsListChanged(self):
        self._TownBattleSOSPanel__updateScrollList()
        self._TownBattleSOSPanel__updateTitleText()


