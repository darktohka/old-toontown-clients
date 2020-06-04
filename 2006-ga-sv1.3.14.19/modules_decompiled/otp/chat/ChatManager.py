# File: C (Python 2.2)

import string
import sys
from direct.showbase import PandaObject
from otp.otpbase import OTPGlobals
from direct.fsm import ClassicFSM
from direct.fsm import State
from otp.login import SecretFriendsInfoPanel
from otp.login import PrivacyPolicyPanel
from otp.otpbase import OTPLocalizer
from direct.directnotify import DirectNotifyGlobal
from otp.login import LeaveToPayDialog
from direct.gui.DirectGui import *
ChatEvent = 'ChatEvent'
NormalChatEvent = 'NormalChatEvent'
SCChatEvent = 'SCChatEvent'
SCCustomChatEvent = 'SCCustomChatEvent'
SCEmoteChatEvent = 'SCEmoteChatEvent'
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
    notify = DirectNotifyGlobal.directNotify.newCategory('ChatManager')
    execChat = base.config.GetBool('exec-chat', 0)
    
    def __init__(self, cr, localAvatar):
        self.cr = cr
        self.localAvatar = localAvatar
        self._ChatManager__scObscured = 0
        self._ChatManager__normalObscured = 0
        self.openChatWarning = None
        self.unpaidChatWarning = None
        self.teaser = None
        self.paidNoParentPassword = None
        self.noSecretChatAtAll = None
        self.noSecretChatWarning = None
        self.activateChat = None
        self.chatMoreInfo = None
        self.chatPrivacyPolicy = None
        self.secretChatActivated = None
        self.problemActivatingChat = None
        self.leaveToPayDialog = None
        self.fsm = ClassicFSM.ClassicFSM('chatManager', [
            State.State('off', self.enterOff, self.exitOff),
            State.State('mainMenu', self.enterMainMenu, self.exitMainMenu),
            State.State('speedChat', self.enterSpeedChat, self.exitSpeedChat),
            State.State('normalChat', self.enterNormalChat, self.exitNormalChat),
            State.State('whisper', self.enterWhisper, self.exitWhisper),
            State.State('whisperChat', self.enterWhisperChat, self.exitWhisperChat),
            State.State('whisperSpeedChat', self.enterWhisperSpeedChat, self.exitWhisperSpeedChat),
            State.State('openChatWarning', self.enterOpenChatWarning, self.exitOpenChatWarning),
            State.State('leaveToPayDialog', self.enterLeaveToPayDialog, self.exitLeaveToPayDialog),
            State.State('unpaidChatWarning', self.enterUnpaidChatWarning, self.exitUnpaidChatWarning),
            State.State('noSecretChatAtAll', self.enterNoSecretChatAtAll, self.exitNoSecretChatAtAll),
            State.State('noSecretChatWarning', self.enterNoSecretChatWarning, self.exitNoSecretChatWarning),
            State.State('otherDialog', self.enterOtherDialog, self.exitOtherDialog),
            State.State('activateChat', self.enterActivateChat, self.exitActivateChat),
            State.State('chatMoreInfo', self.enterChatMoreInfo, self.exitChatMoreInfo),
            State.State('chatPrivacyPolicy', self.enterChatPrivacyPolicy, self.exitChatPrivacyPolicy),
            State.State('secretChatActivated', self.enterSecretChatActivated, self.exitSecretChatActivated),
            State.State('problemActivatingChat', self.enterProblemActivatingChat, self.exitProblemActivatingChat)], 'off', 'off')
        self.fsm.enterInitialState()

    
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
        
        if self.teaser:
            self.teaser.cleanup()
            self.teaser.unload()
            self.teaser = None
        
        if self.noSecretChatAtAll:
            self.noSecretChatAtAll.destroy()
            self.noSecretChatAtAll = None
        
        if self.noSecretChatWarning:
            self.noSecretChatWarning.destroy()
            self.noSecretChatWarning = None
        
        if self.activateChat:
            self.activateChat.destroy()
            self.activateChat = None
        
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
        
        del self.localAvatar
        del self.cr

    
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

    
    def announceChat(self):
        messenger.send(ChatEvent)

    
    def announceSCChat(self):
        messenger.send(SCChatEvent)
        self.announceChat()

    
    def sendChatString(self, message):
        chatFlags = CFSpeech | CFTimeout
        if isThought(message):
            message = removeThoughtPrefix(message)
            chatFlags = CFThought
        
        messenger.send('chatUpdate', [
            message,
            chatFlags])
        messenger.send(NormalChatEvent)
        self.announceChat()

    
    def sendWhisperString(self, message, whisperAvatarId):
        messenger.send('whisperUpdate', [
            message,
            whisperAvatarId])

    
    def sendSCChatMessage(self, msgIndex):
        messenger.send('chatUpdateSC', [
            msgIndex])
        self.announceSCChat()

    
    def sendSCWhisperMessage(self, msgIndex, whisperAvatarId):
        messenger.send('whisperUpdateSC', [
            msgIndex,
            whisperAvatarId])

    
    def sendSCCustomChatMessage(self, msgIndex):
        messenger.send('chatUpdateSCCustom', [
            msgIndex])
        messenger.send(SCCustomChatEvent)
        self.announceSCChat()

    
    def sendSCCustomWhisperMessage(self, msgIndex, whisperAvatarId):
        messenger.send('whisperUpdateSCCustom', [
            msgIndex,
            whisperAvatarId])

    
    def sendSCEmoteChatMessage(self, emoteId):
        messenger.send('chatUpdateSCEmote', [
            emoteId])
        messenger.send(SCEmoteChatEvent)
        self.announceSCChat()

    
    def sendSCEmoteWhisperMessage(self, emoteId, whisperAvatarId):
        messenger.send('whisperUpdateSCEmote', [
            emoteId,
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
        
        if self.localAvatar.canChat() or self.cr.wantMagicWords:
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
        if self.cr.doId2do.has_key(avatarId):
            online = 1
        elif self.cr.isFriend(avatarId):
            online = self.cr.isFriendOnline(avatarId)
        
        understandable = 0
        av = self.cr.identifyAvatar(avatarId)
        if av != None:
            understandable = av.isUnderstandable()
        
        if understandable and online:
            self.whisperButton['state'] = 'normal'
        else:
            self.whisperButton['state'] = 'inactive'
        if online:
            self.whisperScButton['state'] = 'normal'
            self.whisperFrame['text'] = OTPLocalizer.ChatManagerWhisperToName % avatarName
        else:
            self.whisperScButton['state'] = 'inactive'
            self.whisperFrame['text'] = OTPLocalizer.ChatManagerWhisperOffline % avatarName
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
        self.notify.error('called enterOpenChatWarning() on parent class')

    
    def exitOpenChatWarning(self):
        self.notify.error('called exitOpenChatWarning() on parent class')

    
    def enterLeaveToPayDialog(self):
        if self.leaveToPayDialog == None:
            self.leaveToPayDialog = LeaveToPayDialog.LeaveToPayDialog(self.paidNoParentPassword)
            self.leaveToPayDialog.setCancel(self._ChatManager__handleLeaveToPayCancel)
        
        self.leaveToPayDialog.show()

    
    def exitLeaveToPayDialog(self):
        if self.leaveToPayDialog:
            self.leaveToPayDialog.destroy()
            self.leaveToPayDialog = None
        

    
    def enterUnpaidChatWarning(self):
        self.notify.error('called enterUnpaidChatWarning() on parent class')

    
    def exitUnpaidChatWarning(self):
        self.notify.error('called exitUnpaidChatWarning() on parent class')

    
    def enterNoSecretChatAtAll(self):
        self.notify.error('called enterNoSecretChatAtAll() on parent class')

    
    def exitNoSecretChatAtAll(self):
        self.notify.error('called exitNoSecretChatAtAll() on parent class')

    
    def enterNoSecretChatWarning(self):
        self.notify.error('called enterNoSecretChatWarning() on parent class')

    
    def exitNoSecretChatWarning(self):
        self.notify.error('called exitNoSecretChatWarning() on parent class')

    
    def enterActivateChat(self):
        self.notify.error('called enterActivateChat() on parent class')

    
    def exitActivateChat(self):
        self.notify.error('called exitActivateChat() on parent class')

    
    def enterOtherDialog(self):
        pass

    
    def exitOtherDialog(self):
        pass

    
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
        cleanupDialog('privacyPolicyDialog')
        self.chatPrivacyPolicy = None
        self.ignore('privacyPolicyDone')

    
    def enterSecretChatActivated(self):
        self.notify.error('called enterSecretChatActivated() on parent class')

    
    def exitSecretChatActivated(self):
        self.notify.error('called exitSecretChatActivated() on parent class')

    
    def enterProblemActivatingChat(self):
        self.notify.error('called enterProblemActivatingChat() on parent class')

    
    def exitProblemActivatingChat(self):
        self.notify.error('called exitProblemActivatingChat() on parent class')

    
    def _ChatManager__handleLeaveToPayCancel(self):
        self.fsm.request('mainMenu')

    
    def _ChatManager__secretFriendsInfoDone(self):
        self.fsm.request('activateChat')

    
    def _ChatManager__privacyPolicyDone(self):
        self.fsm.request('activateChat')


