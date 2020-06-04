# File: D (Python 2.2)

from PandaObject import *
import DistributedNode
import DistributedActor
import ToontownGlobals
import Avatar
import AvatarDNA
import ChatGarbler
import ChatManager
import string
import Task
import InventoryNew
import Experience
import Localizer
import SCDecoders
import PythonUtil
import time

class DistributedAvatar(DistributedActor.DistributedActor, Avatar.Avatar):
    LaffNumberGenerator = TextNode('LaffNumberGenerator')
    LaffNumberGenerator.freeze()
    LaffNumbersEnabled = 1
    TeleportFailureTimeout = 60.0
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedAvatar_initialized = 1
            Avatar.Avatar.__init__(self)
            DistributedActor.DistributedActor.__init__(self, cr)
            self._DistributedAvatar__chatGarbler = ChatGarbler.ChatGarbler()
            self._DistributedAvatar__teleportAvailable = 0
            self.laffNumber = None
            self.inventory = None
            self.experience = None
            self.hp = None
            self.maxHp = None
            self.lastFailedTeleportMessage = { }


    
    def disable(self):
        self.reparentTo(hidden)
        self.removeActive()
        self.disableBodyCollisions()
        self.hideLaffNumber()
        self.hp = None
        DistributedActor.DistributedActor.disable(self)

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedAvatar_deleted = 1
            del self.experience
            if self.inventory:
                self.inventory.unload()
            
            del self.inventory
            del self._DistributedAvatar__chatGarbler
            DistributedActor.DistributedActor.delete(self)
            Avatar.Avatar.delete(self)


    
    def generate(self):
        DistributedActor.DistributedActor.generate(self)
        if not self.isLocal():
            self.addActive()
            self.initializeBodyCollisions('distAvatarCollNode-' + str(self.doId))
            self.considerUnderstandable()
        
        self.setParent(ToontownGlobals.SPHidden)
        self.setTag('avatarDoId', str(self.doId))

    
    def do_setParent(self, parentToken):
        if not self.isDisabled():
            if parentToken == ToontownGlobals.SPHidden:
                self.nametag2dDist &= ~(Nametag.CName)
            else:
                self.nametag2dDist |= Nametag.CName
            self.nametag.getNametag2d().setContents(self.nametag2dContents & self.nametag2dDist)
            DistributedActor.DistributedActor.do_setParent(self, parentToken)
        

    
    def setHp(self, hitPoints, checkDied = 1):
        if self.hp != None:
            oldHp = max(self.hp, 0)
            newHp = max(hitPoints, 0)
            hpDisplayDelta = newHp - oldHp
            self.showLaffNumber(hpDisplayDelta)
        
        if hitPoints is not None and self.hp > 0:
            pass
        justRanOutOfHp = not hitPoints
        self.hp = hitPoints
        
        try:
            if self.hp != None and self.maxHp != None:
                messenger.send(self.uniqueName('hpChange'), [
                    self.hp,
                    self.maxHp])
            
            if oldHp <= 0 and newHp > 0:
                messenger.send(self.uniqueName('positiveHP'))
        except:
            pass

        if checkDied and justRanOutOfHp:
            self.died()
        

    
    def died(self):
        pass

    
    def getHp(self):
        return self.hp

    
    def setMaxHp(self, hitPoints):
        self.maxHp = hitPoints
        
        try:
            if self.hp != None and self.maxHp != None:
                messenger.send(self.uniqueName('hpChange'), [
                    self.hp,
                    self.maxHp])
        except AttributeError:
            pass

        if self.inventory:
            self.inventory.updateGUI()
        

    
    def getMaxHp(self):
        return self.maxHp

    
    def setExperience(self, experience):
        self.experience = Experience.Experience(experience)
        if self.inventory:
            self.inventory.updateGUI()
        

    
    def setInventory(self, inventoryNetString):
        if not (self.inventory):
            self.inventory = InventoryNew.InventoryNew(self, inventoryNetString)
        
        self.inventory.updateInvString(inventoryNetString)

    
    def setAccountName(self, accountName):
        self.accountName = accountName

    
    def setLastHood(self, lastHood):
        self.lastHood = lastHood

    
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
        
        sender = toonbase.tcr.identifyAvatar(fromId)
        if sender == None:
            return None
        
        if fromId in self.ignoreList:
            sender.d_setWhisperIgnored(self.doId)
            return None
        
        if toonbase.localToon.garbleChat and not sender.isUnderstandable():
            chatString = self._DistributedAvatar__chatGarbler.garble(self, chatString)
        
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
        sender = toonbase.tcr.identifyAvatar(fromId)
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
        sender = toonbase.tcr.identifyAvatar(fromId)
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
        sender = toonbase.tcr.identifyAvatar(fromId)
        if sender == None:
            return None
        
        if fromId in self.ignoreList:
            sender.d_setWhisperIgnored(self.doId)
            return None
        
        chatString = SCDecoders.decodeSCEmoteWhisperMsg(emoteId, sender.getName())
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTEmote)
        

    
    def whisperSCToontaskTo(self, taskId, toNpcId, toonProgress, msgIndex, sendToId):
        messenger.send('wakeup')
        self.sendUpdate('setWhisperSCToontaskFrom', [
            self.doId,
            taskId,
            toNpcId,
            toonProgress,
            msgIndex], sendToId)

    
    def setWhisperSCToontaskFrom(self, fromId, taskId, toNpcId, toonProgress, msgIndex):
        sender = toonbase.tcr.identifyAvatar(fromId)
        if sender == None:
            return None
        
        if fromId in self.ignoreList:
            sender.d_setWhisperIgnored(self.doId)
            return None
        
        chatString = SCDecoders.decodeSCToontaskMsg(taskId, toNpcId, toonProgress, msgIndex)
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTQuickTalker)
        

    
    def d_setWhisperIgnored(self, fromId):
        self.sendUpdate('setWhisperIgnored', [
            fromId])

    
    def setWhisperIgnored(self, fromId):
        if fromId in self.ignoreList:
            return None
        
        sender = toonbase.tcr.identifyAvatar(fromId)
        if sender == None:
            return None
        
        chatString = Localizer.WhisperIgnored % sender.getName()
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
        if self.doId in toonbase.localToon.ignoreList:
            return None
        
        if toonbase.localToon.garbleChat and not self.isUnderstandable():
            chatString = self._DistributedAvatar__chatGarbler.garble(self, chatString)
        
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
        if self.doId in toonbase.localToon.ignoreList:
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
        if self.doId in toonbase.localToon.ignoreList:
            return None
        
        chatString = SCDecoders.decodeSCCustomMsg(msgIndex)
        if chatString:
            self.setChatAbsolute(chatString, CFSpeech | CFQuicktalker | CFTimeout)
        

    
    def b_setSCEmote(self, emoteId):
        self.b_setEmoteState(emoteId, animMultiplier = self.animMultiplier)

    
    def b_setSCToontask(self, taskId, toNpcId, toonProgress, msgIndex):
        self.setSCToontask(taskId, toNpcId, toonProgress, msgIndex)
        self.d_setSCToontask(taskId, toNpcId, toonProgress, msgIndex)
        return None

    
    def d_setSCToontask(self, taskId, toNpcId, toonProgress, msgIndex):
        messenger.send('wakeup')
        self.sendUpdate('setSCToontask', [
            taskId,
            toNpcId,
            toonProgress,
            msgIndex])

    
    def setSCToontask(self, taskId, toNpcId, toonProgress, msgIndex):
        if self.doId in toonbase.localToon.ignoreList:
            return None
        
        chatString = SCDecoders.decodeSCToontaskMsg(taskId, toNpcId, toonProgress, msgIndex)
        if chatString:
            self.setChatAbsolute(chatString, CFSpeech | CFQuicktalker | CFTimeout)
        

    
    def d_friendsNotify(self, avId, status):
        self.sendUpdate('friendsNotify', [
            avId,
            status])

    
    def friendsNotify(self, avId, status):
        avatar = toonbase.tcr.identifyFriend(avId)
        if avatar != None:
            if status == 1:
                self.setSystemMessage(avId, Localizer.WhisperNoLongerFriend % avatar.getName())
            elif status == 2:
                self.setSystemMessage(avId, Localizer.WhisperNowSpecialFriend % avatar.getName())
            
        

    
    def d_battleSOS(self, requesterId, sendToId = None):
        self.sendUpdate('battleSOS', [
            requesterId], sendToId)

    
    def battleSOS(self, requesterId):
        avatar = toonbase.tcr.identifyAvatar(requesterId)
        if avatar != None:
            self.setSystemMessage(requesterId, Localizer.MovieSOSWhisperHelp % avatar.getName(), whisperType = WhisperPopup.WTBattleSOS)
        

    
    def d_teleportQuery(self, requesterId, sendToId = None):
        self.sendUpdate('teleportQuery', [
            requesterId], sendToId)

    
    def teleportQuery(self, requesterId):
        avatar = toonbase.tcr.identifyAvatar(requesterId)
        if avatar != None:
            if requesterId in self.ignoreList:
                self.d_teleportResponse(self.doId, 2, 0, 0, 0, sendToId = requesterId)
                return None
            
            if self._DistributedAvatar__teleportAvailable and not (self.ghostMode):
                self.setSystemMessage(requesterId, Localizer.WhisperComingToVisit % avatar.getName())
                messenger.send('teleportQuery', [
                    avatar,
                    self])
                return None
            
            if self.failedTeleportMessageOk(requesterId):
                self.setSystemMessage(requesterId, Localizer.WhisperFailedVisit % avatar.getName())
            
        
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
        avatar = toonbase.tcr.identifyAvatar(requesterId)
        if avatar != None:
            self.setSystemMessage(requesterId, Localizer.WhisperGiveupVisit % avatar.getName())
        

    
    def b_teleportGreeting(self, avId):
        self.d_teleportGreeting(avId)
        self.teleportGreeting(avId)

    
    def d_teleportGreeting(self, avId):
        self.sendUpdate('teleportGreeting', [
            avId])

    
    def teleportGreeting(self, avId):
        if toonbase.tcr.doId2do.has_key(avId):
            avatar = toonbase.tcr.doId2do[avId]
            self.setChatAbsolute(Localizer.TeleportGreeting % avatar.getName(), CFSpeech | CFTimeout)
        

    
    def setTeleportAvailable(self, available):
        self._DistributedAvatar__teleportAvailable = available

    
    def getTeleportAvailable(self):
        return self._DistributedAvatar__teleportAvailable

    
    def getName(self):
        return Avatar.Avatar.getName(self)

    
    def setName(self, name):
        
        try:
            self.node().setName('%s-%d' % (name, self.doId))
            self.gotName = 1
        except:
            pass

        return Avatar.Avatar.setName(self, name)

    
    def showLaffNumber(self, number, bonus = 0):
        if self.LaffNumbersEnabled and not (self.ghostMode):
            if number != 0:
                if self.laffNumber:
                    self.hideLaffNumber()
                
                self.LaffNumberGenerator.setFont(ToontownGlobals.getSignFont())
                if number < 0:
                    self.LaffNumberGenerator.setText(str(number))
                else:
                    self.LaffNumberGenerator.setText('+' + str(number))
                self.LaffNumberGenerator.clearShadow()
                self.LaffNumberGenerator.setAlign(TextNode.ACenter)
                if bonus == 1:
                    r = 1.0
                    g = 1.0
                    b = 0
                    a = 1
                elif bonus == 2:
                    r = 1.0
                    g = 0.5
                    b = 0
                    a = 1
                elif number < 0:
                    r = 0.90000000000000002
                    g = 0
                    b = 0
                    a = 1
                else:
                    r = 0
                    g = 0.90000000000000002
                    b = 0
                    a = 1
                self.LaffNumberGenerator.setTextColor(r, g, b, a)
                self.laffNumberNode = self.LaffNumberGenerator.generate()
                self.laffNumber = self.attachNewNode(self.laffNumberNode)
                self.laffNumber.setBillboardPointEye()
                self.laffNumber.setBin('fixed', 100)
                self.laffNumber.setPos(0, 0, self.height / 2)
                seq = Task.sequence(self.laffNumber.lerpPos(Point3(0, 0, self.height + 1.5), 1.0, blendType = 'easeOut'), Task.pause(0.84999999999999998), self.laffNumber.lerpColor(Vec4(r, g, b, a), Vec4(r, g, b, 0), 0.10000000000000001), Task.Task(self.hideLaffNumberTask))
                taskMgr.add(seq, self.uniqueName('laffNumber'))
            
        

    
    def showLaffString(self, text, duration = 0.84999999999999998, scale = 0.69999999999999996):
        if self.LaffNumbersEnabled and not (self.ghostMode):
            if text != '':
                if self.laffNumber:
                    self.hideLaffNumber()
                
                self.LaffNumberGenerator.setFont(ToontownGlobals.getSignFont())
                self.LaffNumberGenerator.setText(text)
                self.LaffNumberGenerator.clearShadow()
                self.LaffNumberGenerator.setAlign(TextNode.ACenter)
                r = 1.0
                a = 1.0
                g = 0.0
                b = 0.0
                self.LaffNumberGenerator.setTextColor(r, g, b, a)
                self.laffNumberNode = self.LaffNumberGenerator.generate()
                self.laffNumber = self.attachNewNode(self.laffNumberNode)
                self.laffNumber.setScale(scale)
                self.laffNumber.setBillboardAxis()
                self.laffNumber.setPos(0, 0, self.height / 2)
                seq = Task.sequence(self.laffNumber.lerpPos(Point3(0, 0, self.height + 1.5), 1.0, blendType = 'easeOut'), Task.pause(duration), self.laffNumber.lerpColor(Vec4(r, g, b, a), Vec4(r, g, b, 0), 0.10000000000000001), Task.Task(self.hideLaffNumberTask))
                taskMgr.add(seq, self.uniqueName('laffNumber'))
            
        

    
    def hideLaffNumberTask(self, task):
        self.hideLaffNumber()
        return Task.done

    
    def hideLaffNumber(self):
        if self.laffNumber:
            taskMgr.remove(self.uniqueName('laffNumber'))
            self.laffNumber.removeNode()
            self.laffNumber = None
        

    
    def getStareAtNodeAndOffset(self):
        return (self, Point3(0, 0, self.height))


