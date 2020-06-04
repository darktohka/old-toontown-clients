# File: C (Python 2.2)

from DirectGui import *
from SpeedChatTypes import *
from SpeedChat import SpeedChat
import SpeedChatGlobals
import PandaObject
import FSM
import State
import Emote
import string
import Localizer
import ToontownGlobals
from OptionsPage import speedChatStyles
scStructure = [
    [
        Localizer.SCMenuHello,
        {
            100: 0 },
        {
            101: 0 },
        {
            102: 0 },
        {
            103: 0 },
        {
            104: 0 },
        {
            105: 0 },
        106,
        107,
        108,
        109],
    [
        Localizer.SCMenuBye,
        {
            200: 0 },
        {
            201: 0 },
        {
            202: 0 },
        203,
        204,
        205,
        206,
        207],
    [
        Localizer.SCMenuHappy,
        {
            300: 1 },
        {
            301: 1 },
        {
            302: 1 },
        303,
        {
            304: 1 },
        305,
        306,
        307,
        308,
        309,
        310,
        311,
        {
            312: 1 },
        {
            313: 1 },
        {
            314: 1 },
        315],
    [
        Localizer.SCMenuSad,
        {
            400: 2 },
        {
            401: 2 },
        {
            402: 2 },
        403,
        404,
        405,
        406,
        407,
        408,
        409,
        410],
    [
        Localizer.SCMenuFriendly,
        [
            Localizer.SCMenuFriendlyYou,
            600,
            601,
            602,
            603],
        [
            Localizer.SCMenuFriendlyILike,
            700,
            701,
            702,
            703,
            704,
            705],
        500,
        501,
        502,
        503,
        504,
        505,
        506,
        507,
        508,
        509,
        510,
        511,
        512,
        513,
        514],
    [
        Localizer.SCMenuSorry,
        800,
        801,
        802,
        803,
        804,
        805,
        806,
        807,
        808,
        {
            809: 5 },
        810],
    [
        Localizer.SCMenuStinky,
        {
            900: 3 },
        {
            901: 3 },
        {
            902: 3 },
        {
            903: 3 },
        904,
        {
            905: 3 },
        907],
    [
        Localizer.SCMenuPlaces,
        [
            Localizer.SCMenuPlacesLetsGo,
            1100,
            1101,
            1111,
            1102,
            1103,
            1104,
            1105,
            1106,
            1107,
            1108,
            1109,
            1110],
        1000,
        1001,
        1013,
        1002,
        1003,
        1004,
        1005,
        1006,
        1007,
        1008,
        1009,
        1010,
        1011,
        1012],
    [
        Localizer.SCMenuToontasks,
        [
            SCToontaskMenu,
            Localizer.SCMenuToontasksMyTasks],
        [
            Localizer.SCMenuToontasksYouShouldChoose,
            1300,
            1301,
            1302,
            1303,
            1304],
        1200,
        1201,
        1202,
        1203,
        1204,
        1205],
    [
        Localizer.SCMenuBattle,
        [
            Localizer.SCMenuBattleLetsUse,
            1500,
            1501,
            1502,
            1503,
            1504,
            1505,
            1506],
        1415,
        1400,
        1401,
        1402,
        1403,
        1404,
        1405,
        1406,
        1407,
        1408,
        1409,
        1410,
        1411,
        1412,
        1413,
        1414],
    [
        Localizer.SCMenuGagShop,
        1600,
        1601,
        1602,
        1603,
        1604,
        1605,
        1606],
    {
        1: 17 },
    {
        2: 18 },
    3]

class ChatInputSpeedChat(PandaObject.PandaObject):
    DefaultSCColorScheme = SCColorScheme()
    
    def __init__(self, chatMgr):
        self.chatMgr = chatMgr
        self.whisperAvatarId = None
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        self.emoteNoAccessPanel = DirectFrame(parent = hidden, relief = None, state = 'normal', text = Localizer.SCEmoteNoAccessMsg, frameSize = (-1, 1, -1, 1), geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (0.92000000000000004, 1, 0.59999999999999998), geom_pos = (0, 0, -0.080000000000000002), text_scale = 0.080000000000000002)
        DirectButton(parent = self.emoteNoAccessPanel, image = okButtonImage, relief = None, text = Localizer.SCEmoteNoAccessOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.20000000000000001), command = self.handleEmoteNoAccessDone)
        structure = []
        if toonbase.emotionsMenuEnabled:
            structure.append([
                SCEmoteMenu,
                Localizer.SCMenuEmotions])
        
        if toonbase.customMenuEnabled:
            structure.append([
                SCCustomMenu,
                Localizer.SCMenuCustom])
        
        structure += scStructure
        self.createSpeedChatObject(structure)
        
        def listenForSCEvent(eventBaseName, handler, self = self):
            eventName = self.speedChat.getEventName(eventBaseName)
            self.accept(eventName, handler)

        listenForSCEvent(SpeedChatGlobals.SCTerminalLinkedEmoteEvent, self.handleLinkedEmote)
        listenForSCEvent(SpeedChatGlobals.SCStaticTextMsgEvent, self.handleStaticTextMsg)
        listenForSCEvent(SpeedChatGlobals.SCCustomMsgEvent, self.handleCustomMsg)
        listenForSCEvent(SpeedChatGlobals.SCEmoteMsgEvent, self.handleEmoteMsg)
        listenForSCEvent(SpeedChatGlobals.SCEmoteNoAccessEvent, self.handleEmoteNoAccess)
        listenForSCEvent(SpeedChatGlobals.SCToontaskMsgEvent, self.handleToontaskMsg)
        listenForSCEvent('SpeedChatStyleChange', self.handleSpeedChatStyleChange)
        self.fsm = FSM.FSM('SpeedChat', [
            State.State('off', self.enterOff, self.exitOff, [
                'active']),
            State.State('active', self.enterActive, self.exitActive, [
                'off'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def delete(self):
        self.ignoreAll()
        self.emoteNoAccessPanel.destroy()
        del self.emoteNoAccessPanel
        self.speedChat.destroy()
        del self.speedChat

    
    def show(self, whisperAvatarId = None):
        self.whisperAvatarId = whisperAvatarId
        self.fsm.request('active')

    
    def hide(self):
        self.fsm.request('off')

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterActive(self):
        
        def handleCancel(self = self):
            self.chatMgr.fsm.request('mainMenu')

        self.accept('mouse1', handleCancel)
        
        def selectionMade(self = self):
            self.chatMgr.fsm.request('mainMenu')

        self.terminalSelectedEvent = self.speedChat.getEventName(SpeedChatGlobals.SCTerminalSelectedEvent)
        self.accept(self.terminalSelectedEvent, selectionMade)
        self.speedChat.reparentTo(aspect2d, FOREGROUND_SORT_INDEX)
        scZ = 0.95999999999999996
        self.speedChat.setPos(-1.05, 0, scZ)
        self.speedChat.setWhisperMode(self.whisperAvatarId != None)
        self.speedChat.enter()

    
    def exitActive(self):
        self.ignore('mouse1')
        self.ignore(self.terminalSelectedEvent)
        self.speedChat.exit()
        self.speedChat.reparentTo(hidden)
        self.emoteNoAccessPanel.reparentTo(hidden)

    
    def handleLinkedEmote(self, emoteId):
        if self.whisperAvatarId is None:
            lt = toonbase.localToon
            lt.b_setEmoteState(emoteId, animMultiplier = lt.animMultiplier)
        

    
    def handleStaticTextMsg(self, textId):
        if self.whisperAvatarId is None:
            self.chatMgr.sendSCChatMessage(textId)
        else:
            self.chatMgr.sendSCWhisperMessage(textId, self.whisperAvatarId)

    
    def handleCustomMsg(self, textId):
        if self.whisperAvatarId is None:
            self.chatMgr.sendSCCustomChatMessage(textId)
        else:
            self.chatMgr.sendSCCustomWhisperMessage(textId, self.whisperAvatarId)

    
    def handleEmoteMsg(self, emoteId):
        if self.whisperAvatarId is None:
            self.chatMgr.sendSCEmoteChatMessage(emoteId)
        else:
            self.chatMgr.sendSCEmoteWhisperMessage(emoteId, self.whisperAvatarId)

    
    def handleEmoteNoAccess(self):
        if self.whisperAvatarId is None:
            self.emoteNoAccessPanel.setPos(0, 0, 0)
        else:
            self.emoteNoAccessPanel.setPos(0.37, 0, 0)
        self.emoteNoAccessPanel.reparentTo(aspect2d)

    
    def handleEmoteNoAccessDone(self):
        self.emoteNoAccessPanel.reparentTo(hidden)

    
    def handleToontaskMsg(self, taskId, toNpcId, toonProgress, msgIndex):
        if self.whisperAvatarId is None:
            self.chatMgr.sendSCToontaskChatMessage(taskId, toNpcId, toonProgress, msgIndex)
        else:
            self.chatMgr.sendSCToontaskWhisperMessage(taskId, toNpcId, toonProgress, msgIndex, self.whisperAvatarId)

    
    def handleSpeedChatStyleChange(self):
        (nameKey, arrowColor, rolloverColor, frameColor) = speedChatStyles[toonbase.localToon.getSpeedChatStyleIndex()]
        newSCColorScheme = SCColorScheme(arrowColor = arrowColor, rolloverColor = rolloverColor, frameColor = frameColor)
        self.speedChat.setColorScheme(newSCColorScheme)

    
    def createSpeedChatObject(self, structure):
        if hasattr(self, 'speedChat'):
            self.speedChat.exit()
            self.speedChat.destroy()
            del self.speedChat
        
        self.speedChat = SpeedChat(structure = structure)
        self.speedChat.setScale(0.055)
        self.speedChat.setBin('gui-popup', 0)
        self.speedChat.setTopLevelOverlap(0.0)
        self.speedChat.setColorScheme(ChatInputSpeedChat.DefaultSCColorScheme)
        self.speedChat.finalizeAll()

    
    def addFactoryMenu(self):
        fMenu = SCFactoryMenu()
        fMenuHolder = SCMenuHolder(Localizer.SCMenuFactory, menu = fMenu)
        self.speedChat[2:2] = [
            fMenuHolder]

    
    def removeFactoryMenu(self):
        fMenu = self.speedChat[2]
        del self.speedChat[2]
        fMenu.destroy()

    
    def addCogMenu(self, indices):
        fMenu = SCCogMenu(indices)
        fMenuHolder = SCMenuHolder(Localizer.SCMenuCog, menu = fMenu)
        self.speedChat[2:2] = [
            fMenuHolder]

    
    def removeCogMenu(self):
        fMenu = self.speedChat[2]
        del self.speedChat[2]
        fMenu.destroy()


