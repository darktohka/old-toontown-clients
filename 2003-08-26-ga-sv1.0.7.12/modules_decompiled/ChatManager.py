# File: C (Python 2.2)

import Task
import string
import sys
import PandaObject
import ToontownGlobals
import LeaveToPayDialog
import FSM
import State
import MagicWordManager
import SecretFriendsInfoPanel
import PrivacyPolicyPanel
import Localizer
from DirectGui import *
from ChatInputNormal import ChatInputNormal
from ChatInputSpeedChat import ChatInputSpeedChat
ChatEvent = 'ChatEvent'
NormalChatEvent = 'NormalChatEvent'
SCChatEvent = 'SCChatEvent'
SCCustomChatEvent = 'SCCustomChatEvent'
SCEmoteChatEvent = 'SCEmoteChatEvent'
SCToontaskChatEvent = 'SCToontaskChatEvent'
OnScreen = 0
OffScreen = 1
Thought = 2
ThoughtPrefix = '.'

def isThought(message):
    if len(message) == 0:
        return 0
    elif string.find(message, ThoughtPrefix, 0, len(ThoughtPrefix)) >= 0:
        return 1
    else:
        return 0


def removeThoughtPrefix(message):
    if isThought(message):
        return message[len(ThoughtPrefix):]
    else:
        return message


class ChatManager(PandaObject.PandaObject):
    execChat = base.config.GetBool('exec-chat', 0)
    
    def __init__(self):
        self._ChatManager__scObscured = 0
        self._ChatManager__normalObscured = 0
        gui = loader.loadModelOnce('phase_3.5/models/gui/chat_input_gui')
        self.normalButton = DirectButton(image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (-1.2646999999999999, 0, 0.92800000000000005), scale = 1.179, relief = None, image_color = Vec4(1, 1, 1, 1), text = ('', Localizer.ChatManagerChat, Localizer.ChatManagerChat), text_align = TextNode.ALeft, text_scale = 0.059999999999999998, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (-0.052499999999999998, -0.089999999999999997), textMayChange = 0, sortOrder = FOREGROUND_SORT_INDEX, command = self._ChatManager__normalButtonPressed)
        self.normalButton.hide()
        self.openScSfx = loader.loadSfx('phase_3.5/audio/sfx/GUI_quicktalker.mp3')
        self.openScSfx.setVolume(0.59999999999999998)
        self.scButton = DirectButton(image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (-1.129, 0, 0.92800000000000005), scale = 1.179, relief = None, image_color = Vec4(0.75, 1, 0.59999999999999998, 1), text = ('', Localizer.GlobalSpeedChatName, Localizer.GlobalSpeedChatName), text_scale = 0.059999999999999998, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, sortOrder = FOREGROUND_SORT_INDEX, command = self._ChatManager__scButtonPressed, clickSound = self.openScSfx)
        self.scButton.hide()
        self.whisperFrame = DirectFrame(relief = None, image = getDefaultDialogGeom(), image_scale = (0.45000000000000001, 0.45000000000000001, 0.45000000000000001), image_color = ToontownGlobals.GlobalDialogColor, pos = (-0.40000000000000002, 0, 0.754), text = Localizer.ChatManagerWhisperTo, text_wordwrap = 7.0, text_scale = 0.059999999999999998, text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0.14000000000000001), textMayChange = 1, sortOrder = FOREGROUND_SORT_INDEX)
        self.whisperFrame.hide()
        self.whisperButton = DirectButton(parent = self.whisperFrame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (-0.125, 0, -0.10000000000000001), scale = 1.179, relief = None, image_color = Vec4(1, 1, 1, 1), text = ('', Localizer.ChatManagerChat, Localizer.ChatManagerChat, ''), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, command = self._ChatManager__whisperButtonPressed)
        self.whisperScButton = DirectButton(parent = self.whisperFrame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (0.0, 0, -0.10000000000000001), scale = 1.179, relief = None, image_color = Vec4(0.75, 1, 0.59999999999999998, 1), text = ('', Localizer.GlobalSpeedChatName, Localizer.GlobalSpeedChatName, ''), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, command = self._ChatManager__whisperScButtonPressed)
        self.whisperCancelButton = DirectButton(parent = self.whisperFrame, image = (gui.find('**/CloseBtn_UP'), gui.find('**/CloseBtn_DN'), gui.find('**/CloseBtn_Rllvr')), pos = (0.125, 0, -0.10000000000000001), scale = 1.179, relief = None, text = ('', Localizer.ChatManagerCancel, Localizer.ChatManagerCancel), text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, command = self._ChatManager__whisperCancelPressed)
        gui.removeNode()
        self.openChatWarning = None
        self.unpaidChatWarning = None
        self.noSecretChatAtAll = None
        self.noSecretChatWarning = None
        self.activateChat = None
        self.leaveToPayDialog = None
        self.chatMoreInfo = None
        self.chatPrivacyPolicy = None
        self.secretChatActivated = None
        self.problemActivatingChat = None
        self.fsm = FSM.FSM('chatManager', [
            State.State('off', self.enterOff, self.exitOff),
            State.State('mainMenu', self.enterMainMenu, self.exitMainMenu),
            State.State('speedChat', self.enterSpeedChat, self.exitSpeedChat),
            State.State('normalChat', self.enterNormalChat, self.exitNormalChat),
            State.State('whisper', self.enterWhisper, self.exitWhisper),
            State.State('whisperChat', self.enterWhisperChat, self.exitWhisperChat),
            State.State('whisperSpeedChat', self.enterWhisperSpeedChat, self.exitWhisperSpeedChat),
            State.State('openChatWarning', self.enterOpenChatWarning, self.exitOpenChatWarning),
            State.State('unpaidChatWarning', self.enterUnpaidChatWarning, self.exitUnpaidChatWarning),
            State.State('noSecretChatAtAll', self.enterNoSecretChatAtAll, self.exitNoSecretChatAtAll),
            State.State('noSecretChatWarning', self.enterNoSecretChatWarning, self.exitNoSecretChatWarning),
            State.State('activateChat', self.enterActivateChat, self.exitActivateChat),
            State.State('leaveToPayDialog', self.enterLeaveToPayDialog, self.exitLeaveToPayDialog),
            State.State('chatMoreInfo', self.enterChatMoreInfo, self.exitChatMoreInfo),
            State.State('chatPrivacyPolicy', self.enterChatPrivacyPolicy, self.exitChatPrivacyPolicy),
            State.State('secretChatActivated', self.enterSecretChatActivated, self.exitSecretChatActivated),
            State.State('problemActivatingChat', self.enterProblemActivatingChat, self.exitProblemActivatingChat)], 'off', 'off')
        self.fsm.enterInitialState()
        self.chatInputNormal = ChatInputNormal(self)
        self.chatInputSpeedChat = ChatInputSpeedChat(self)

    
    def delete(self):
        self.ignoreAll()
        del self.fsm
        self.chatInputNormal.delete()
        del self.chatInputNormal
        self.chatInputSpeedChat.delete()
        del self.chatInputSpeedChat
        if self.openChatWarning:
            self.openChatWarning.destroy()
            self.openChatWarning = None
        
        if self.unpaidChatWarning:
            self.payButton = None
            self.unpaidChatWarning.destroy()
            self.unpaidChatWarning = None
        
        if self.noSecretChatAtAll:
            self.noSecretChatAtAll.destroy()
            self.noSecretChatAtAll = None
        
        if self.noSecretChatWarning:
            self.noSecretChatWarning.destroy()
            self.noSecretChatWarning = None
        
        if self.activateChat:
            self.activateChat.destroy()
            self.activateChat = None
        
        if self.leaveToPayDialog:
            self.leaveToPayDialog.destroy()
            self.leaveToPayDialog = None
        
        if self.chatMoreInfo:
            self.chatMoreInfo.destroy()
            self.chatMoreInfo = None
        
        if self.chatPrivacyPolicy:
            self.chatPrivacyPolicy.destroy()
            self.chatPrivacyPolicy = None
        
        if self.secretChatActivated:
            self.secretChatActivated.destroy()
            self.secretChatActivated = None
        
        if self.problemActivatingChat:
            self.problemActivatingChat.destroy()
            self.problemActivatingChat = None
        
        loader.unloadModel('phase_3.5/models/gui/chat_input_gui')
        self.normalButton.destroy()
        del self.normalButton
        self.scButton.destroy()
        del self.scButton
        del self.openScSfx
        self.whisperFrame.destroy()
        del self.whisperFrame
        del self.whisperButton
        del self.whisperScButton
        del self.whisperCancelButton

    
    def obscure(self, normal, sc):
        self._ChatManager__scObscured = sc
        if self._ChatManager__scObscured:
            self.scButton.hide()
        
        self._ChatManager__normalObscured = normal
        if self._ChatManager__normalObscured:
            self.normalButton.hide()
        

    
    def isObscured(self):
        return (self._ChatManager__normalObscured, self._ChatManager__scObscured)

    
    def stop(self):
        self.fsm.request('off')
        self.ignoreAll()

    
    def start(self):
        self.fsm.request('mainMenu')

    
    def _ChatManager__announceChat(self):
        messenger.send(ChatEvent)

    
    def _ChatManager__announceSCChat(self):
        messenger.send(SCChatEvent)
        self._ChatManager__announceChat()

    
    def sendChatString(self, message):
        chatFlags = CFSpeech | CFTimeout
        if isThought(message):
            message = removeThoughtPrefix(message)
            chatFlags = CFThought
        
        messenger.send('chatUpdate', [
            message,
            chatFlags])
        messenger.send(NormalChatEvent)
        self._ChatManager__announceChat()

    
    def sendWhisperString(self, message, whisperAvatarId):
        messenger.send('whisperUpdate', [
            message,
            whisperAvatarId])

    
    def sendSCChatMessage(self, msgIndex):
        messenger.send('chatUpdateSC', [
            msgIndex])
        self._ChatManager__announceSCChat()

    
    def sendSCWhisperMessage(self, msgIndex, whisperAvatarId):
        messenger.send('whisperUpdateSC', [
            msgIndex,
            whisperAvatarId])

    
    def sendSCCustomChatMessage(self, msgIndex):
        messenger.send('chatUpdateSCCustom', [
            msgIndex])
        messenger.send(SCCustomChatEvent)
        self._ChatManager__announceSCChat()

    
    def sendSCCustomWhisperMessage(self, msgIndex, whisperAvatarId):
        messenger.send('whisperUpdateSCCustom', [
            msgIndex,
            whisperAvatarId])

    
    def sendSCEmoteChatMessage(self, emoteId):
        messenger.send('chatUpdateSCEmote', [
            emoteId])
        messenger.send(SCEmoteChatEvent)
        self._ChatManager__announceSCChat()

    
    def sendSCEmoteWhisperMessage(self, emoteId, whisperAvatarId):
        messenger.send('whisperUpdateSCEmote', [
            emoteId,
            whisperAvatarId])

    
    def sendSCToontaskChatMessage(self, taskId, toNpcId, toonProgress, msgIndex):
        messenger.send('chatUpdateSCToontask', [
            taskId,
            toNpcId,
            toonProgress,
            msgIndex])
        messenger.send(SCToontaskChatEvent)
        self._ChatManager__announceSCChat()

    
    def sendSCToontaskWhisperMessage(self, taskId, toNpcId, toonProgress, msgIndex, whisperAvatarId):
        messenger.send('whisperUpdateSCToontask', [
            taskId,
            toNpcId,
            toonProgress,
            msgIndex,
            whisperAvatarId])

    
    def enterOff(self):
        self.scButton.hide()
        self.normalButton.hide()
        self.ignoreAll()

    
    def exitOff(self):
        pass

    
    def enterMainMenu(self):
        if not (self._ChatManager__scObscured):
            self.scButton.show()
        
        if not (self._ChatManager__normalObscured):
            self.normalButton.show()
        
        if toonbase.localToon.canChat() or MagicWordManager.MagicWordManager.wantMagicWords:
            self.chatInputNormal.chatEntry['backgroundFocus'] = 1
            self.acceptOnce('enterNormalChat', self.fsm.request, [
                'normalChat'])
        

    
    def exitMainMenu(self):
        self.scButton.hide()
        self.normalButton.hide()
        self.ignore('enterNormalChat')
        self.chatInputNormal.chatEntry['backgroundFocus'] = 0

    
    def whisperTo(self, avatarName, avatarId):
        self.fsm.request('whisper', [
            avatarName,
            avatarId])

    
    def noWhisper(self):
        self.fsm.request('mainMenu')

    
    def enterWhisper(self, avatarName, avatarId):
        self.whisperScButton['extraArgs'] = [
            avatarId]
        self.whisperButton['extraArgs'] = [
            avatarName,
            avatarId]
        online = 0
        if toonbase.tcr.doId2do.has_key(avatarId):
            online = 1
        elif toonbase.tcr.isFriend(avatarId):
            online = toonbase.tcr.isFriendOnline(avatarId)
        
        understandable = 0
        av = toonbase.tcr.identifyAvatar(avatarId)
        if av != None:
            understandable = av.isUnderstandable()
        
        if understandable and online:
            self.whisperButton['state'] = 'normal'
        else:
            self.whisperButton['state'] = 'inactive'
        if online:
            self.whisperScButton['state'] = 'normal'
            self.whisperFrame['text'] = Localizer.ChatManagerWhisperToName % avatarName
        else:
            self.whisperScButton['state'] = 'inactive'
            self.whisperFrame['text'] = Localizer.ChatManagerWhisperOffline % avatarName
        self.whisperFrame.show()
        if understandable and online:
            self.chatInputNormal.chatEntry['backgroundFocus'] = 1
            self.acceptOnce('enterNormalChat', self.fsm.request, [
                'whisperChat',
                [
                    avatarName,
                    avatarId]])
        

    
    def exitWhisper(self):
        self.whisperFrame.hide()
        self.ignore('enterNormalChat')
        self.chatInputNormal.chatEntry['backgroundFocus'] = 0

    
    def enterWhisperSpeedChat(self, avatarId):
        self.whisperFrame.show()
        self.chatInputNormal.chatEntry['backgroundFocus'] = 0
        self.chatInputSpeedChat.show(avatarId)

    
    def exitWhisperSpeedChat(self):
        self.whisperFrame.hide()
        self.chatInputSpeedChat.hide()

    
    def enterWhisperChat(self, avatarName, avatarId):
        self.chatInputNormal.show(avatarName, avatarId)

    
    def exitWhisperChat(self):
        self.chatInputNormal.hide()

    
    def enterSpeedChat(self):
        messenger.send('enterSpeedChat')
        if not (self._ChatManager__scObscured):
            self.scButton.show()
        
        if not (self._ChatManager__normalObscured):
            self.normalButton.show()
        
        self.chatInputNormal.chatEntry['backgroundFocus'] = 0
        self.chatInputSpeedChat.show()

    
    def exitSpeedChat(self):
        self.scButton.hide()
        self.normalButton.hide()
        self.chatInputSpeedChat.hide()

    
    def enterNormalChat(self):
        self.chatInputNormal.show()

    
    def exitNormalChat(self):
        self.chatInputNormal.hide()

    
    def enterOpenChatWarning(self):
        if self.openChatWarning == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            buttonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.openChatWarning = DirectFrame(pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.90000000000000002), text = Localizer.OpenChatWarning, text_wordwrap = 19, text_scale = 0.059999999999999998, text_pos = (0.0, 0.28000000000000003), textMayChange = 0)
            DirectButton(self.openChatWarning, image = buttonImage, relief = None, text = Localizer.OpenChatWarningOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.28000000000000003), command = self._ChatManager__handleOpenChatWarningOK)
            buttons.removeNode()
        
        self.openChatWarning.show()
        if not (self._ChatManager__scObscured):
            self.scButton.show()
        

    
    def exitOpenChatWarning(self):
        self.openChatWarning.hide()
        self.scButton.hide()

    
    def enterUnpaidChatWarning(self):
        if self.unpaidChatWarning == None:
            guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
            buttonImage = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
            self.unpaidChatWarning = DirectFrame(pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.69999999999999996), text = Localizer.UnpaidChatWarning, text_wordwrap = 18, text_scale = 0.059999999999999998, text_pos = (0.0, 0.23000000000000001), textMayChange = 0)
            self.payButton = DirectButton(self.unpaidChatWarning, image = buttonImage, relief = None, text = Localizer.UnpaidChatWarningPay, image_scale = (1.75, 1, 1.1499999999999999), text_scale = 0.059999999999999998, text_pos = (0, -0.02), textMayChange = 0, pos = (0.0, 0.0, -0.080000000000000002), command = self._ChatManager__handleUnpaidChatWarningPay)
            DirectButton(self.unpaidChatWarning, image = buttonImage, relief = None, text = Localizer.UnpaidChatWarningContinue, textMayChange = 0, image_scale = (1.75, 1, 1.1499999999999999), text_scale = 0.059999999999999998, text_pos = (0, -0.02), pos = (0.0, 0.0, -0.23000000000000001), command = self._ChatManager__handleUnpaidChatWarningContinue)
            guiButton.removeNode()
        
        if toonbase.localToon.inTutorial:
            self.payButton.hide()
        else:
            self.payButton.show()
        self.unpaidChatWarning.show()
        if not (self._ChatManager__scObscured):
            self.scButton.show()
        

    
    def exitUnpaidChatWarning(self):
        self.unpaidChatWarning.hide()
        self.scButton.hide()

    
    def enterNoSecretChatAtAll(self):
        if self.noSecretChatAtAll == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.noSecretChatAtAll = DirectFrame(pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.3999999999999999, 1.0, 1.0), text = Localizer.NoSecretChatAtAll, text_wordwrap = 20, textMayChange = 0, text_scale = 0.059999999999999998, text_pos = (0, 0.25))
            DirectLabel(parent = self.noSecretChatAtAll, relief = None, pos = (0, 0, 0.34999999999999998), text = Localizer.NoSecretChatAtAllTitle, textMayChange = 0, text_scale = 0.080000000000000002)
            DirectButton(self.noSecretChatAtAll, image = okButtonImage, relief = None, text = Localizer.NoSecretChatAtAllOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.34999999999999998), command = self._ChatManager__handleNoSecretChatAtAllOK)
            buttons.removeNode()
        
        self.noSecretChatAtAll.show()

    
    def exitNoSecretChatAtAll(self):
        self.noSecretChatAtAll.hide()

    
    def enterNoSecretChatWarning(self):
        if self.noSecretChatWarning == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            if toonbase.tcr.productName != 'Terra-DMC':
                okPos = (-0.22, 0.0, -0.34999999999999998)
                textPos = (0, 0.25)
                okCommand = self._ChatManager__handleNoSecretChatWarningOK
            else:
                self.passwordEntry = None
                okPos = (0, 0, -0.34999999999999998)
                textPos = (0, 0.125)
                okCommand = self._ChatManager__handleNoSecretChatWarningCancel
            self.noSecretChatWarning = DirectFrame(pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.3999999999999999, 1.0, 1.0), text = Localizer.NoSecretChatWarning, text_wordwrap = 20, text_scale = 0.055, text_pos = textPos, textMayChange = 1)
            DirectButton(self.noSecretChatWarning, image = okButtonImage, relief = None, text = Localizer.NoSecretChatWarningOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = okPos, command = okCommand)
            DirectLabel(parent = self.noSecretChatWarning, relief = None, pos = (0, 0, 0.34999999999999998), text = Localizer.NoSecretChatWarningTitle, textMayChange = 0, text_scale = 0.080000000000000002)
            if toonbase.tcr.productName != 'Terra-DMC':
                self.passwordLabel = DirectLabel(parent = self.noSecretChatWarning, relief = None, pos = (-0.070000000000000007, 0.0, -0.20000000000000001), text = Localizer.ParentPassword, text_scale = 0.059999999999999998, text_align = TextNode.ARight, textMayChange = 0)
                self.passwordEntry = DirectEntry(parent = self.noSecretChatWarning, relief = None, image = nameBalloon, image1_color = (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1.0), scale = 0.064000000000000001, pos = (0.0, 0.0, -0.20000000000000001), width = ToontownGlobals.maxLoginWidth, numLines = 1, focus = 1, cursorKeys = 1, obscured = 1, command = self._ChatManager__handleNoSecretChatWarningOK)
                DirectButton(self.noSecretChatWarning, image = cancelButtonImage, relief = None, text = Localizer.NoSecretChatWarningCancel, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 1, pos = (0.20000000000000001, 0.0, -0.34999999999999998), command = self._ChatManager__handleNoSecretChatWarningCancel)
            
            buttons.removeNode()
            nameBalloon.removeNode()
        else:
            self.noSecretChatWarning['text'] = Localizer.NoSecretChatWarning
            if self.passwordEntry:
                self.passwordEntry['focus'] = 1
                self.passwordEntry.enterText('')
            
        self.noSecretChatWarning.show()

    
    def exitNoSecretChatWarning(self):
        self.noSecretChatWarning.hide()

    
    def enterActivateChat(self):
        if self.activateChat == None:
            guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            moreButtonImage = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
            self.activateChat = DirectFrame(pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.8, 1.0, 1.3), text = Localizer.ActivateChat, text_align = TextNode.ALeft, text_wordwrap = 28, text_scale = 0.059999999999999998, text_pos = (-0.81999999999999995, 0.5), textMayChange = 0)
            DirectButton(self.activateChat, image = moreButtonImage, image_scale = (1.25, 1.0, 1.0), relief = None, text = Localizer.ActivateChatMoreInfo, text_scale = 0.059999999999999998, text_pos = (0, -0.02), textMayChange = 0, pos = (0.0, 0.0, 0.29999999999999999), command = self._ChatManager__handleActivateChatMoreInfo)
            DirectButton(self.activateChat, image = okButtonImage, relief = None, text = Localizer.ActivateChatYes, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (-0.5, 0.0, -0.5), command = self._ChatManager__handleActivateChatYes)
            DirectButton(self.activateChat, image = cancelButtonImage, relief = None, text = Localizer.ActivateChatNo, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.5, 0.0, -0.5), command = self._ChatManager__handleActivateChatNo)
            DirectButton(self.activateChat, image = moreButtonImage, image_scale = (1.75, 1.0, 1.0), relief = None, text = Localizer.ActivateChatPrivacyPolicy, text_scale = 0.059999999999999998, text_pos = (0, -0.02), textMayChange = 0, pos = (0.0, 0.0, -0.5), command = self._ChatManager__handleActivateChatPrivacyPolicy)
            guiButton.removeNode()
            buttons.removeNode()
        
        self.activateChat.show()

    
    def exitActivateChat(self):
        self.activateChat.hide()

    
    def enterChatMoreInfo(self):
        if self.chatMoreInfo == None:
            self.chatMoreInfo = SecretFriendsInfoPanel.SecretFriendsInfoPanel('secretFriendsInfoDone')
        
        self.chatMoreInfo.show()
        self.accept('secretFriendsInfoDone', self._ChatManager__secretFriendsInfoDone)

    
    def exitChatMoreInfo(self):
        self.chatMoreInfo.hide()
        self.ignore('secretFriendsInfoDone')

    
    def enterChatPrivacyPolicy(self):
        if self.chatPrivacyPolicy == None:
            self.chatPrivacyPolicy = PrivacyPolicyPanel.PrivacyPolicyPanel('privacyPolicyDone')
        
        self.chatPrivacyPolicy.show()
        self.accept('privacyPolicyDone', self._ChatManager__privacyPolicyDone)

    
    def exitChatPrivacyPolicy(self):
        self.chatPrivacyPolicy.hide()
        self.ignore('privacyPolicyDone')

    
    def enterSecretChatActivated(self):
        if self.secretChatActivated == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            buttonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.secretChatActivated = DirectFrame(pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.80000000000000004), text = Localizer.SecretChatActivated, text_align = TextNode.ALeft, text_wordwrap = 17.5, text_scale = 0.059999999999999998, text_pos = (-0.5, 0.25), textMayChange = 0)
            DirectButton(self.secretChatActivated, image = buttonImage, relief = None, text = Localizer.SecretChatActivatedOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.22), command = self._ChatManager__handleSecretChatActivatedOK)
            buttons.removeNode()
        
        self.secretChatActivated.show()

    
    def exitSecretChatActivated(self):
        self.secretChatActivated.hide()

    
    def enterProblemActivatingChat(self):
        if self.problemActivatingChat == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            buttonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.problemActivatingChat = DirectFrame(pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.90000000000000002), text = '', text_align = TextNode.ALeft, text_wordwrap = 18, text_scale = 0.059999999999999998, text_pos = (-0.5, 0.28000000000000003), textMayChange = 1)
            DirectButton(self.problemActivatingChat, image = buttonImage, relief = None, text = Localizer.ProblemActivatingChatOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.28000000000000003), command = self._ChatManager__handleProblemActivatingChatOK)
            buttons.removeNode()
        
        self.problemActivatingChat.show()

    
    def exitProblemActivatingChat(self):
        self.problemActivatingChat.hide()

    
    def enterLeaveToPayDialog(self):
        if self.leaveToPayDialog == None:
            self.leaveToPayDialog = LeaveToPayDialog.LeaveToPayDialog()
            self.leaveToPayDialog.setCancel(self._ChatManager__handleLeaveToPayCancel)
        
        self.leaveToPayDialog.show()

    
    def exitLeaveToPayDialog(self):
        if self.leaveToPayDialog:
            self.leaveToPayDialog.destroy()
            self.leaveToPayDialog = None
        

    
    def _ChatManager__normalButtonPressed(self):
        if not toonbase.tcr.isPaid():
            self.fsm.request('unpaidChatWarning')
        elif not toonbase.tcr.allowSecretChat():
            tt = toonbase.tcr.loginInterface
            if tt.supportsParentPassword():
                self.fsm.request('noSecretChatWarning')
            else:
                self.fsm.request('noSecretChatAtAll')
        elif not toonbase.localToon.canChat():
            self.fsm.request('openChatWarning')
        else:
            self.fsm.request('normalChat')

    
    def _ChatManager__scButtonPressed(self):
        self.fsm.request('speedChat')

    
    def _ChatManager__whisperButtonPressed(self, avatarName, avatarId):
        self.fsm.request('whisperChat', [
            avatarName,
            avatarId])

    
    def _ChatManager__whisperScButtonPressed(self, avatarId):
        self.fsm.request('whisperSpeedChat', [
            avatarId])

    
    def _ChatManager__whisperCancelPressed(self):
        self.fsm.request('mainMenu')

    
    def _ChatManager__handleOpenChatWarningOK(self):
        self.fsm.request('mainMenu')

    
    def _ChatManager__handleUnpaidChatWarningContinue(self):
        self.fsm.request('mainMenu')

    
    def _ChatManager__handleUnpaidChatWarningPay(self):
        if toonbase.tcr.isWebPlayToken():
            self.fsm.request('leaveToPayDialog')
        else:
            self.fsm.request('mainMenu')
            toonbase.localToon.b_setAnimState('TeleportOut', 1, self._ChatManager__handleBookExitTeleport)

    
    def _ChatManager__handleBookExitTeleport(self):
        toonbase.tcr.loginFSM.request('memberAgreement')

    
    def _ChatManager__handleNoSecretChatAtAllOK(self):
        self.fsm.request('mainMenu')

    
    def _ChatManager__handleNoSecretChatWarningOK(self, *args):
        password = self.passwordEntry.get()
        tt = toonbase.tcr.loginInterface
        (okflag, message) = tt.authenticateParentPassword(toonbase.tcr.userName, toonbase.tcr.password, password)
        if okflag:
            self.fsm.request('activateChat')
        elif message:
            self.fsm.request('problemActivatingChat')
            self.problemActivatingChat['text'] = Localizer.ProblemActivatingChat % message
        else:
            self.noSecretChatWarning['text'] = Localizer.NoSecretChatWarningWrongPassword
            self.passwordEntry['focus'] = 1
            self.passwordEntry.enterText('')

    
    def _ChatManager__handleNoSecretChatWarningCancel(self):
        self.fsm.request('mainMenu')

    
    def _ChatManager__handleActivateChatYes(self):
        password = self.passwordEntry.get()
        tt = toonbase.tcr.loginInterface
        (okflag, message) = tt.enableSecretFriends(toonbase.tcr.userName, toonbase.tcr.password, password)
        if okflag:
            tt.resendPlayToken()
            toonbase.tcr.secretChatAllowed = 1
            self.fsm.request('secretChatActivated')
        elif message == None:
            message = 'Parent Password was invalid.'
        
        self.fsm.request('problemActivatingChat')
        self.problemActivatingChat['text'] = Localizer.ProblemActivatingChat % message

    
    def _ChatManager__handleActivateChatMoreInfo(self):
        self.fsm.request('chatMoreInfo')

    
    def _ChatManager__handleActivateChatPrivacyPolicy(self):
        self.fsm.request('chatPrivacyPolicy')

    
    def _ChatManager__handleActivateChatNo(self):
        self.fsm.request('mainMenu')

    
    def _ChatManager__handleLeaveToPayCancel(self):
        self.fsm.request('mainMenu')

    
    def _ChatManager__secretFriendsInfoDone(self):
        self.fsm.request('activateChat')

    
    def _ChatManager__privacyPolicyDone(self):
        self.fsm.request('activateChat')

    
    def _ChatManager__handleSecretChatActivatedOK(self):
        self.fsm.request('mainMenu')

    
    def _ChatManager__handleProblemActivatingChatOK(self):
        self.fsm.request('mainMenu')


