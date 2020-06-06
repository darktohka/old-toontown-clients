# File: D (Python 2.2)

from pandac.PandaModules import *
from otp.chat import ChatGarbler
import string
from direct.task import Task
from otp.otpbase import OTPLocalizer
from otp.speedchat import SCDecoders
from direct.showbase import PythonUtil
from otp.avatar import DistributedAvatar
import time
from otp.avatar import Avatar

class DistributedPlayer(DistributedAvatar.DistributedAvatar):
    TeleportFailureTimeout = 60.0
    chatGarbler = ChatGarbler.ChatGarbler()
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedPlayer_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)
            self._DistributedPlayer__teleportAvailable = 0
            self.inventory = None
            self.experience = None
            self.friendsList = []
            self.oldFriendsList = None
            self.timeFriendsListChanged = None
            self.ignoreList = []
            self.lastFailedTeleportMessage = { }


    
    def disable(self):
        DistributedAvatar.DistributedAvatar.disable(self)

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedPlayer_deleted = 1
            del self.experience
            if self.inventory:
                self.inventory.unload()
            
            del self.inventory
            DistributedAvatar.DistributedAvatar.delete(self)


    
    def generate(self):
        DistributedAvatar.DistributedAvatar.generate(self)

    
    def setAccountName(self, accountName):
        self.accountName = accountName

    
    def whisperTo(self, chatString, sendToId):
        messenger.send('wakeup')
        self.sendUpdate('setWhisperFrom', [
            self.doId,
            chatString], sendToId)

    
    def setWhisperFrom(self, fromId, chatString):
        if fromId == 0:
            return None
        
        if fromId == self.doId:
            return None
        
        sender = base.cr.identifyAvatar(fromId)
        if sender == None:
            return None
        
        if fromId in self.ignoreList:
            sender.d_setWhisperIgnored(self.doId)
            return None
        
        if base.localAvatar.garbleChat and not sender.isUnderstandable():
            chatString = self.chatGarbler.garble(self, chatString)
        
        self.displayWhisper(fromId, chatString, WhisperPopup.WTNormal)
        return None

    
    def setSystemMessage(self, aboutId, chatString, whisperType = WhisperPopup.WTSystem):
        self.displayWhisper(aboutId, chatString, whisperType)
        return None

    
    def displayWhisper(self, fromId, chatString, whisperType):
        print 'Whisper type %s from %s: %s' % (whisperType, fromId, chatString)

    
    def whisperSCTo(self, msgIndex, sendToId):
        messenger.send('wakeup')
        self.sendUpdate('setWhisperSCFrom', [
            self.doId,
            msgIndex], sendToId)

    
    def setWhisperSCFrom(self, fromId, msgIndex):
        sender = base.cr.identifyAvatar(fromId)
        if sender == None:
            return None
        
        if fromId in self.ignoreList:
            sender.d_setWhisperIgnored(self.doId)
            return None
        
        chatString = SCDecoders.decodeSCStaticTextMsg(msgIndex)
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTQuickTalker)
        

    
    def whisperSCCustomTo(self, msgIndex, sendToId):
        messenger.send('wakeup')
        self.sendUpdate('setWhisperSCCustomFrom', [
            self.doId,
            msgIndex], sendToId)

    
    def setWhisperSCCustomFrom(self, fromId, msgIndex):
        sender = base.cr.identifyAvatar(fromId)
        if sender == None:
            return None
        
        if fromId in self.ignoreList:
            sender.d_setWhisperIgnored(self.doId)
            return None
        
        chatString = SCDecoders.decodeSCCustomMsg(msgIndex)
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTQuickTalker)
        

    
    def whisperSCEmoteTo(self, emoteId, sendToId):
        messenger.send('wakeup')
        self.sendUpdate('setWhisperSCEmoteFrom', [
            self.doId,
            emoteId], sendToId)

    
    def setWhisperSCEmoteFrom(self, fromId, emoteId):
        sender = base.cr.identifyAvatar(fromId)
        if sender == None:
            return None
        
        if fromId in self.ignoreList:
            sender.d_setWhisperIgnored(self.doId)
            return None
        
        chatString = SCDecoders.decodeSCEmoteWhisperMsg(emoteId, sender.getName())
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTEmote)
        

    
    def d_setWhisperIgnored(self, fromId):
        self.sendUpdate('setWhisperIgnored', [
            fromId])

    
    def setWhisperIgnored(self, fromId):
        if fromId in self.ignoreList:
            return None
        
        sender = base.cr.identifyAvatar(fromId)
        if sender == None:
            return None
        
        chatString = OTPLocalizer.WhisperIgnored % sender.getName()
        self.displayWhisper(0, chatString, WhisperPopup.WTSystem)

    
    def b_setChat(self, chatString, chatFlags):
        if self.cr.wantMagicWords and len(chatString) > 0 and chatString[0] == '~':
            messenger.send('magicWord', [
                chatString])
        else:
            messenger.send('wakeup')
            self.setChatAbsolute(chatString, chatFlags)
            self.d_setChat(chatString, chatFlags)
        return None

    
    def d_setChat(self, chatString, chatFlags):
        self.sendUpdate('setChat', [
            chatString,
            chatFlags])

    
    def setChat(self, chatString, chatFlags):
        if self.doId in base.localAvatar.ignoreList:
            return None
        
        if base.localAvatar.garbleChat and not self.isUnderstandable():
            chatString = self.chatGarbler.garble(self, chatString)
        
        chatFlags &= ~(CFQuicktalker | CFPageButton | CFQuitButton)
        if chatFlags & CFThought:
            chatFlags &= ~(CFSpeech | CFTimeout)
        else:
            chatFlags |= CFSpeech | CFTimeout
        self.setChatAbsolute(chatString, chatFlags)

    
    def b_setSC(self, msgIndex):
        self.setSC(msgIndex)
        self.d_setSC(msgIndex)

    
    def d_setSC(self, msgIndex):
        messenger.send('wakeup')
        self.sendUpdate('setSC', [
            msgIndex])

    
    def setSC(self, msgIndex):
        if self.doId in base.localAvatar.ignoreList:
            return None
        
        chatString = SCDecoders.decodeSCStaticTextMsg(msgIndex)
        if chatString:
            self.setChatAbsolute(chatString, CFSpeech | CFQuicktalker | CFTimeout)
        

    
    def b_setSCCustom(self, msgIndex):
        self.setSCCustom(msgIndex)
        self.d_setSCCustom(msgIndex)

    
    def d_setSCCustom(self, msgIndex):
        messenger.send('wakeup')
        self.sendUpdate('setSCCustom', [
            msgIndex])

    
    def setSCCustom(self, msgIndex):
        if self.doId in base.localAvatar.ignoreList:
            return None
        
        chatString = SCDecoders.decodeSCCustomMsg(msgIndex)
        if chatString:
            self.setChatAbsolute(chatString, CFSpeech | CFQuicktalker | CFTimeout)
        

    
    def b_setSCEmote(self, emoteId):
        self.b_setEmoteState(emoteId, animMultiplier = self.animMultiplier)

    
    def d_friendsNotify(self, avId, status):
        self.sendUpdate('friendsNotify', [
            avId,
            status])

    
    def friendsNotify(self, avId, status):
        avatar = base.cr.identifyFriend(avId)
        if avatar != None:
            if status == 1:
                self.setSystemMessage(avId, OTPLocalizer.WhisperNoLongerFriend % avatar.getName())
            elif status == 2:
                self.setSystemMessage(avId, OTPLocalizer.WhisperNowSpecialFriend % avatar.getName())
            
        

    
    def d_teleportQuery(self, requesterId, sendToId = None):
        self.sendUpdate('teleportQuery', [
            requesterId], sendToId)

    
    def teleportQuery(self, requesterId):
        avatar = base.cr.identifyAvatar(requesterId)
        if avatar != None:
            if requesterId in self.ignoreList:
                self.d_teleportResponse(self.doId, 2, 0, 0, 0, sendToId = requesterId)
                return None
            
            if self._DistributedPlayer__teleportAvailable and not (self.ghostMode):
                self.setSystemMessage(requesterId, OTPLocalizer.WhisperComingToVisit % avatar.getName())
                messenger.send('teleportQuery', [
                    avatar,
                    self])
                return None
            
            if self.failedTeleportMessageOk(requesterId):
                self.setSystemMessage(requesterId, OTPLocalizer.WhisperFailedVisit % avatar.getName())
            
        
        self.d_teleportResponse(self.doId, 0, 0, 0, 0, sendToId = requesterId)

    
    def failedTeleportMessageOk(self, fromId):
        now = globalClock.getFrameTime()
        lastTime = self.lastFailedTeleportMessage.get(fromId, None)
        if lastTime != None:
            elapsed = now - lastTime
            if elapsed < self.TeleportFailureTimeout:
                return 0
            
        
        self.lastFailedTeleportMessage[fromId] = now
        return 1

    
    def d_teleportResponse(self, avId, available, shardId, hoodId, zoneId, sendToId = None):
        self.sendUpdate('teleportResponse', [
            avId,
            available,
            shardId,
            hoodId,
            zoneId], sendToId)

    
    def teleportResponse(self, avId, available, shardId, hoodId, zoneId):
        messenger.send('teleportResponse', [
            avId,
            available,
            shardId,
            hoodId,
            zoneId])

    
    def d_teleportGiveup(self, requesterId, sendToId = None):
        self.sendUpdate('teleportGiveup', [
            requesterId], sendToId)

    
    def teleportGiveup(self, requesterId):
        avatar = base.cr.identifyAvatar(requesterId)
        if avatar != None:
            self.setSystemMessage(requesterId, OTPLocalizer.WhisperGiveupVisit % avatar.getName())
        

    
    def b_teleportGreeting(self, avId):
        self.d_teleportGreeting(avId)
        self.teleportGreeting(avId)

    
    def d_teleportGreeting(self, avId):
        self.sendUpdate('teleportGreeting', [
            avId])

    
    def teleportGreeting(self, avId):
        if base.cr.doId2do.has_key(avId):
            avatar = base.cr.doId2do[avId]
            self.setChatAbsolute(OTPLocalizer.TeleportGreeting % avatar.getName(), CFSpeech | CFTimeout)
        

    
    def setTeleportAvailable(self, available):
        self._DistributedPlayer__teleportAvailable = available

    
    def getTeleportAvailable(self):
        return self._DistributedPlayer__teleportAvailable

    
    def getFriendsList(self):
        return self.friendsList

    
    def setFriendsList(self, friendsList):
        self.oldFriendsList = self.friendsList
        self.friendsList = friendsList
        self.timeFriendsListChanged = globalClock.getFrameTime()
        messenger.send('friendsListChanged')
        Avatar.reconsiderAllUnderstandable()


