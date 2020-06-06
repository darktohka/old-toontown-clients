# File: T (Python 2.2)

from direct.gui.DirectGui import *
from otp.speedchat.SpeedChatTypes import *
from toontown.speedchat.TTSpeedChatTypes import *
from otp.speedchat.SpeedChat import SpeedChat
from otp.speedchat import SpeedChatGlobals
from toontown.speedchat import TTSpeedChatGlobals
from direct.showbase import PandaObject
from direct.fsm import ClassicFSM
from direct.fsm import State
import string
from otp.otpbase import OTPLocalizer
from otp.otpbase import OTPGlobals
from toontown.shtiker.OptionsPage import speedChatStyles
scStructure = [
    [
        OTPLocalizer.SCMenuHello,
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
        OTPLocalizer.SCMenuBye,
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
        208,
        209,
        207],
    [
        OTPLocalizer.SCMenuHappy,
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
        OTPLocalizer.SCMenuSad,
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
        OTPLocalizer.SCMenuFriendly,
        [
            OTPLocalizer.SCMenuFriendlyYou,
            600,
            601,
            602,
            603],
        [
            OTPLocalizer.SCMenuFriendlyILike,
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
        515,
        511,
        512,
        513,
        514],
    [
        OTPLocalizer.SCMenuSorry,
        801,
        800,
        802,
        803,
        804,
        811,
        812,
        813,
        805,
        806,
        807,
        808,
        {
            809: 5 },
        810],
    [
        OTPLocalizer.SCMenuStinky,
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
        OTPLocalizer.SCMenuPlaces,
        [
            OTPLocalizer.SCMenuPlacesPlayground,
            1100,
            1101,
            1105,
            1106,
            1107,
            1108,
            1109,
            1110,
            1116],
        [
            OTPLocalizer.SCMenuPlacesCogs,
            1102,
            1103,
            1104,
            1113,
            1114,
            1115,
            1118,
            1119,
            1120],
        [
            OTPLocalizer.SCMenuPlacesEstate,
            1111,
            1112,
            1013,
            1117],
        [
            OTPLocalizer.SCMenuPlacesWait,
            1015,
            1007,
            1008,
            1010,
            1011,
            1014],
        1000,
        1001,
        1002,
        1003,
        1004,
        1005,
        1006,
        1009,
        1012],
    [
        OTPLocalizer.SCMenuToontasks,
        [
            TTSCToontaskMenu,
            OTPLocalizer.SCMenuToontasksMyTasks],
        [
            OTPLocalizer.SCMenuToontasksYouShouldChoose,
            1300,
            1301,
            1302,
            1303,
            1304],
        1200,
        1201,
        1202,
        1208,
        1203,
        1209,
        1204,
        1205,
        1206,
        1207],
    [
        OTPLocalizer.SCMenuBattle,
        [
            OTPLocalizer.SCMenuBattleGags,
            1500,
            1501,
            1502,
            1503,
            1504,
            1505,
            1506,
            1401,
            1402,
            1413],
        [
            OTPLocalizer.SCMenuBattleTaunts,
            1403,
            1406,
            1520,
            1521,
            1522,
            1523,
            1524,
            1525,
            1526,
            1407,
            1408],
        [
            OTPLocalizer.SCMenuBattleStrategy,
            1414,
            1550,
            1551,
            1552,
            1415,
            1553,
            1554,
            1555,
            1556,
            1557,
            1558,
            1559],
        1400,
        1416,
        1404,
        1405,
        1409,
        1410,
        1411,
        1412],
    [
        OTPLocalizer.SCMenuGagShop,
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
if hasattr(base, 'wantPets') and base.wantPets:
    scPetMenuStructure = [
        [
            OTPLocalizer.SCMenuPets,
            [
                TTSCPetTrickMenu,
                OTPLocalizer.SCMenuPetTricks],
            21000,
            21001,
            21002,
            21003,
            21004,
            21005]]

cfoMenuStructure = [
    [
        OTPLocalizer.SCMenuCFOBattleCranes,
        2100,
        2101,
        2102,
        2103,
        2104,
        2105,
        2106,
        2107,
        2108,
        2109,
        2110],
    [
        OTPLocalizer.SCMenuCFOBattleGoons,
        2120,
        2121,
        2122,
        2123,
        2124,
        2125,
        2126],
    2130,
    2131,
    2132,
    2133,
    1410]

class TTChatInputSpeedChat(PandaObject.PandaObject):
    DefaultSCColorScheme = SCColorScheme()
    
    def __init__(self, chatMgr):
        self.chatMgr = chatMgr
        self.whisperAvatarId = None
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        self.emoteNoAccessPanel = DirectFrame(parent = hidden, relief = None, state = 'normal', text = OTPLocalizer.SCEmoteNoAccessMsg, frameSize = (-1, 1, -1, 1), geom = getDefaultDialogGeom(), geom_color = OTPGlobals.GlobalDialogColor, geom_scale = (0.92000000000000004, 1, 0.59999999999999998), geom_pos = (0, 0, -0.080000000000000002), text_scale = 0.080000000000000002)
        DirectButton(parent = self.emoteNoAccessPanel, image = okButtonImage, relief = None, text = OTPLocalizer.SCEmoteNoAccessOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.20000000000000001), command = self.handleEmoteNoAccessDone)
        self.createSpeedChat()
        self.factoryMenu = None
        self.cogMenu = None
        self.cfoMenu = None
        
        def listenForSCEvent(eventBaseName, handler, self = self):
            eventName = self.speedChat.getEventName(eventBaseName)
            self.accept(eventName, handler)

        listenForSCEvent(SpeedChatGlobals.SCTerminalLinkedEmoteEvent, self.handleLinkedEmote)
        listenForSCEvent(SpeedChatGlobals.SCStaticTextMsgEvent, self.handleStaticTextMsg)
        listenForSCEvent(SpeedChatGlobals.SCCustomMsgEvent, self.handleCustomMsg)
        listenForSCEvent(SpeedChatGlobals.SCEmoteMsgEvent, self.handleEmoteMsg)
        listenForSCEvent(SpeedChatGlobals.SCEmoteNoAccessEvent, self.handleEmoteNoAccess)
        listenForSCEvent(TTSpeedChatGlobals.TTSCToontaskMsgEvent, self.handleToontaskMsg)
        listenForSCEvent(TTSpeedChatGlobals.TTSCResistanceMsgEvent, self.handleResistanceMsg)
        listenForSCEvent('SpeedChatStyleChange', self.handleSpeedChatStyleChange)
        self.fsm = ClassicFSM.ClassicFSM('SpeedChat', [
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
        del self.fsm
        del self.chatMgr

    
    def show(self, whisperAvatarId = None):
        self.whisperAvatarId = whisperAvatarId
        self.fsm.request('active')

    
    def hide(self):
        self.fsm.request('off')

    
    def createSpeedChat(self):
        structure = []
        if launcher and not launcher.isTestServer() or __dev__:
            structure.append([
                TTSCPromotionalMenu,
                'PROMOTIONAL'])
        
        structure.append([
            SCEmoteMenu,
            OTPLocalizer.SCMenuEmotions])
        structure.append([
            SCCustomMenu,
            OTPLocalizer.SCMenuCustom])
        structure.append([
            TTSCResistanceMenu,
            OTPLocalizer.SCMenuResistance])
        if hasattr(base, 'wantPets') and base.wantPets:
            structure += scPetMenuStructure
        
        structure += scStructure
        self.createSpeedChatObject(structure)

    
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
        self.speedChat.reparentTo(aspect2dp, FOREGROUND_SORT_INDEX)
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
            lt = base.localAvatar
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

    
    def handleResistanceMsg(self, textId):
        self.chatMgr.sendSCResistanceChatMessage(textId)

    
    def handleSpeedChatStyleChange(self):
        (nameKey, arrowColor, rolloverColor, frameColor) = speedChatStyles[base.localAvatar.getSpeedChatStyleIndex()]
        newSCColorScheme = SCColorScheme(arrowColor = arrowColor, rolloverColor = rolloverColor, frameColor = frameColor)
        self.speedChat.setColorScheme(newSCColorScheme)

    
    def createSpeedChatObject(self, structure):
        if hasattr(self, 'speedChat'):
            self.speedChat.exit()
            self.speedChat.destroy()
            del self.speedChat
        
        self.speedChat = SpeedChat(structure = structure, backgroundModelName = 'phase_3/models/gui/ChatPanel', guiModelName = 'phase_3.5/models/gui/speedChatGui')
        self.speedChat.setScale(0.055)
        self.speedChat.setBin('gui-popup', 0)
        self.speedChat.setTopLevelOverlap(0.0)
        self.speedChat.setColorScheme(self.DefaultSCColorScheme)
        self.speedChat.finalizeAll()

    
    def addFactoryMenu(self):
        if self.factoryMenu == None:
            menu = TTSCFactoryMenu()
            self.factoryMenu = SCMenuHolder(OTPLocalizer.SCMenuFactory, menu = menu)
            self.speedChat[2:2] = [
                self.factoryMenu]
        

    
    def removeFactoryMenu(self):
        if self.factoryMenu:
            i = self.speedChat.index(self.factoryMenu)
            del self.speedChat[i]
            self.factoryMenu.destroy()
            self.factoryMenu = None
        

    
    def addCogMenu(self, indices):
        if self.cogMenu == None:
            menu = TTSCCogMenu(indices)
            self.cogMenu = SCMenuHolder(OTPLocalizer.SCMenuCog, menu = menu)
            self.speedChat[2:2] = [
                self.cogMenu]
        

    
    def removeCogMenu(self):
        if self.cogMenu:
            i = self.speedChat.index(self.cogMenu)
            del self.speedChat[i]
            self.cogMenu.destroy()
            self.cogMenu = None
        

    
    def addCFOMenu(self):
        if self.cfoMenu == None:
            menu = SCMenu()
            menu.rebuildFromStructure(cfoMenuStructure)
            self.cfoMenu = SCMenuHolder(OTPLocalizer.SCMenuCFOBattle, menu = menu)
            self.speedChat[2:2] = [
                self.cfoMenu]
        

    
    def removeCFOMenu(self):
        if self.cfoMenu:
            i = self.speedChat.index(self.cfoMenu)
            del self.speedChat[i]
            self.cfoMenu.destroy()
            self.cfoMenu = None
        


