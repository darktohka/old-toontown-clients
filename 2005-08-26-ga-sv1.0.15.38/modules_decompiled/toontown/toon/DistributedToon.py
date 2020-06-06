# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from otp.avatar import DistributedPlayer
from otp.avatar import Avatar, DistributedAvatar
import Toon
from direct.distributed import DistributedSmoothNode
from direct.distributed import DistributedObject
from direct.fsm import ClassicFSM
from toontown.hood import ZoneUtil
from direct.distributed import DelayDelete
from direct.showbase import PythonUtil
from toontown.catalog import CatalogItemList
from toontown.catalog import CatalogItem
import TTEmote
from toontown.shtiker.OptionsPage import speedChatStyles
from toontown.fishing import FishCollection
from toontown.fishing import FishTank
from toontown.suit import SuitDNA
from toontown.coghq import CogDisguiseGlobals
from toontown.toonbase import TTLocalizer
import Experience
import InventoryNew
from toontown.speedchat import TTSCDecoders
from toontown.chat import ToonChatGarbler
from toontown.chat import ResistanceChat
from direct.distributed.MsgTypes import *

class DistributedToon(DistributedPlayer.DistributedPlayer, Toon.Toon, DistributedSmoothNode.DistributedSmoothNode):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToon')
    chatGarbler = ToonChatGarbler.ToonChatGarbler()
    
    def __init__(self, cr, bFake = False):
        
        try:
            return None
        except:
            self.DistributedToon_initialized = 1

        DistributedPlayer.DistributedPlayer.__init__(self, cr)
        Toon.Toon.__init__(self)
        DistributedSmoothNode.DistributedSmoothNode.__init__(self, cr)
        self.bFake = bFake
        self.trophyScore = 0
        self.trophyStar = None
        self.trophyStarSpeed = 0
        self.safeZonesVisited = []
        self.NPCFriendsDict = { }
        self.earnedExperience = None
        self.track = None
        self.maxCarry = 0
        self.disguisePageFlag = 0
        self.disguisePage = None
        self.sosPage = None
        self.cogTypes = [
            0,
            0,
            0,
            0]
        self.cogLevels = [
            0,
            0,
            0,
            0]
        self.cogParts = [
            0,
            0,
            0,
            0]
        self.cogMerits = [
            0,
            0,
            0,
            0]
        self.savedCheesyEffect = CENormal
        self.savedCheesyHoodId = 0
        self.savedCheesyExpireTime = 0
        if hasattr(base, 'wantPets') and base.wantPets:
            self.petTrickPhrases = []
            self.petDNA = None
        
        self.customMessages = []
        self.resistanceMessages = []
        self.catalogNotify = ToontownGlobals.NoItems
        self.mailboxNotify = ToontownGlobals.NoItems
        self.catalogScheduleCurrentWeek = 0
        self.catalogScheduleNextTime = 0
        self.monthlyCatalog = CatalogItemList.CatalogItemList()
        self.weeklyCatalog = CatalogItemList.CatalogItemList()
        self.backCatalog = CatalogItemList.CatalogItemList()
        self.onOrder = CatalogItemList.CatalogItemList(store = CatalogItem.Customization | CatalogItem.DeliveryDate)
        self.mailboxContents = CatalogItemList.CatalogItemList(store = CatalogItem.Customization)
        self.splash = None
        self.tossTrack = None
        self.pieTracks = { }
        self.splatTracks = { }
        self.lastTossedPie = 0
        self.clothesTopsList = []
        self.clothesBottomsList = []
        self.tunnelTrack = None
        self.tunnelPivotPos = [
            -14,
            -6,
            0]
        self.tunnelCenterOffset = 9.0
        self.tunnelCenterInfluence = 0.59999999999999998
        self.pivotAngle = 90 + 45
        self.posIndex = 0
        self.houseId = 0
        self.money = 0
        self.bankMoney = 0
        self.maxMoney = 0
        self.maxBankMoney = 0
        self.bPetTutorialDone = False
        self.bFishBingoTutorialDone = False
        self.bFishBingoMarkTutorialDone = False

    
    def disable(self):
        self.stopAnimations()
        self.clearCheesyEffect()
        self.stopBlink()
        self.stopSmooth()
        self.stopLookAroundNow()
        self.setGhostMode(0)
        if self.track != None:
            self.track.finish()
            self.track = None
        
        if self.splash != None:
            self.splash.destroy()
            self.splash = None
        
        if self.emote != None:
            self.emote.finish()
            self.emote = None
        
        self.cleanupPies()
        if self.tunnelTrack:
            self.tunnelTrack.finish()
            self.tunnelTrack = None
        
        self.setTrophyScore(0)
        DistributedPlayer.DistributedPlayer.disable(self)

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedToon_deleted = 1
            del self.safeZonesVisited
            DistributedPlayer.DistributedPlayer.delete(self)
            Toon.Toon.delete(self)


    
    def generate(self):
        DistributedPlayer.DistributedPlayer.generate(self)
        self.startBlink()
        self.startSmooth()

    
    def setDNAString(self, dnaString):
        Toon.Toon.setDNAString(self, dnaString)

    
    def setDNA(self, dna):
        Toon.Toon.setDNA(self, dna)

    
    def setExperience(self, experience):
        self.experience = Experience.Experience(experience)
        if self.inventory:
            self.inventory.updateGUI()
        

    
    def setInventory(self, inventoryNetString):
        if not (self.inventory):
            self.inventory = InventoryNew.InventoryNew(self, inventoryNetString)
        
        self.inventory.updateInvString(inventoryNetString)

    
    def setLastHood(self, lastHood):
        self.lastHood = lastHood

    
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
        if self.doId in base.localAvatar.ignoreList:
            return None
        
        chatString = TTSCDecoders.decodeTTSCToontaskMsg(taskId, toNpcId, toonProgress, msgIndex)
        if chatString:
            self.setChatAbsolute(chatString, CFSpeech | CFQuicktalker | CFTimeout)
        

    
    def d_reqSCResistance(self, msgIndex):
        messenger.send('wakeup')
        nearbyPlayers = self.getNearbyPlayers(ResistanceChat.EFFECT_RADIUS)
        self.sendUpdate('reqSCResistance', [
            msgIndex,
            nearbyPlayers])

    
    def getNearbyPlayers(self, radius, includeSelf = True):
        nearbyToons = []
        toonIds = self.cr.getObjectsOfExactClass(DistributedToon)
        for (toonId, toon) in toonIds.items():
            if toon is not self:
                dist = toon.getDistance(self)
                if dist < radius:
                    nearbyToons.append(toonId)
                
            
        
        if includeSelf:
            nearbyToons.append(self.doId)
        
        return nearbyToons

    
    def setSCResistance(self, msgIndex, nearbyToons = []):
        chatString = TTSCDecoders.decodeTTSCResistanceMsg(msgIndex)
        if chatString:
            self.setChatAbsolute(chatString, CFSpeech | CFTimeout)
        
        ResistanceChat.doEffect(msgIndex, self, nearbyToons)

    
    def d_battleSOS(self, requesterId, sendToId = None):
        self.sendUpdate('battleSOS', [
            requesterId], sendToId)

    
    def battleSOS(self, requesterId):
        avatar = base.cr.identifyAvatar(requesterId)
        if avatar != None:
            self.setSystemMessage(requesterId, TTLocalizer.MovieSOSWhisperHelp % avatar.getName(), whisperType = WhisperPopup.WTBattleSOS)
        

    
    def getDialogueArray(self, *args):
        return Toon.Toon.getDialogueArray(self, *args)

    
    def setDefaultShard(self, shard):
        self.defaultShard = shard

    
    def setDefaultZone(self, zoneId):
        hoodPhase = base.cr.hoodMgr.getPhaseFromHood(zoneId)
        if launcher and not launcher.getPhaseComplete(hoodPhase):
            self.defaultZone = ToontownCentral
        else:
            self.defaultZone = zoneId

    
    def setShtickerBook(self, string):
        pass

    
    def whisperSCToontaskTo(self, taskId, toNpcId, toonProgress, msgIndex, sendToId):
        messenger.send('wakeup')
        self.sendUpdate('setWhisperSCToontaskFrom', [
            self.doId,
            taskId,
            toNpcId,
            toonProgress,
            msgIndex], sendToId)

    
    def setWhisperSCToontaskFrom(self, fromId, taskId, toNpcId, toonProgress, msgIndex):
        sender = base.cr.identifyAvatar(fromId)
        if sender == None:
            return None
        
        if fromId in self.ignoreList:
            sender.d_setWhisperIgnored(self.doId)
            return None
        
        chatString = TTSCDecoders.decodeTTSCToontaskMsg(taskId, toNpcId, toonProgress, msgIndex)
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTQuickTalker)
        

    
    def setMaxNPCFriends(self, max):
        self.maxNPCFriends = max

    
    def getMaxNPCFriends(self):
        return self.maxNPCFriends

    
    def getNPCFriendsDict(self):
        return self.NPCFriendsDict

    
    def setNPCFriendsDict(self, NPCFriendsList):
        NPCFriendsDict = { }
        for friendPair in NPCFriendsList:
            NPCFriendsDict[friendPair[0]] = friendPair[1]
        
        self.NPCFriendsDict = NPCFriendsDict

    
    def setMaxClothes(self, max):
        self.maxClothes = max

    
    def getMaxClothes(self):
        return self.maxClothes

    
    def getClothesTopsList(self):
        return self.clothesTopsList

    
    def setClothesTopsList(self, clothesList):
        self.clothesTopsList = clothesList

    
    def getClothesBottomsList(self):
        return self.clothesBottomsList

    
    def setClothesBottomsList(self, clothesList):
        self.clothesBottomsList = clothesList

    
    def catalogGenClothes(self, avId):
        if avId == self.doId:
            self.generateToonClothes()
            self.loop('neutral')
        

    
    def isClosetFull(self, extraClothes = 0):
        numClothes = len(self.clothesTopsList) / 4 + len(self.clothesBottomsList) / 2
        return numClothes + extraClothes >= self.maxClothes

    
    def setMaxHp(self, hitPoints):
        DistributedPlayer.DistributedPlayer.setMaxHp(self, hitPoints)
        if self.inventory:
            self.inventory.updateGUI()
        

    
    def died(self):
        messenger.send(self.uniqueName('died'))
        if self.isLocal():
            target_sz = ZoneUtil.getSafeZoneId(self.defaultZone)
            place = self.cr.playGame.getPlace()
            if place and place.fsm:
                place.fsm.request('died', [
                    {
                        'loader': ZoneUtil.getLoaderName(target_sz),
                        'where': ZoneUtil.getWhereName(target_sz, 1),
                        'how': 'teleportIn',
                        'hoodId': target_sz,
                        'zoneId': target_sz,
                        'shardId': None,
                        'avId': -1,
                        'battle': 1 }])
            
        

    
    def setInterface(self, string):
        pass

    
    def setZonesVisited(self, hoods):
        self.safeZonesVisited = hoods

    
    def setHoodsVisited(self, hoods):
        self.hoodsVisited = hoods
        if ToontownGlobals.SellbotHQ in hoods or ToontownGlobals.CashbotHQ in hoods:
            self.setDisguisePageFlag(1)
        

    
    def wrtReparentTo(self, parent):
        DistributedSmoothNode.DistributedSmoothNode.wrtReparentTo(self, parent)

    
    def setTutorialAck(self, tutorialAck):
        self.tutorialAck = tutorialAck

    
    def setEarnedExperience(self, earnedExp):
        self.earnedExperience = earnedExp

    
    def b_setTunnelIn(self, endX, tunnelOrigin):
        timestamp = globalClockDelta.getFrameNetworkTime()
        pos = tunnelOrigin.getPos(render)
        h = tunnelOrigin.getH(render)
        self.setTunnelIn(timestamp, endX, pos[0], pos[1], pos[2], h)
        self.d_setTunnelIn(timestamp, endX, pos[0], pos[1], pos[2], h)

    
    def d_setTunnelIn(self, timestamp, endX, x, y, z, h):
        self.sendUpdate('setTunnelIn', [
            timestamp,
            endX,
            x,
            y,
            z,
            h])

    
    def setTunnelIn(self, timestamp, endX, x, y, z, h):
        t = globalClockDelta.networkToLocalTime(timestamp)
        self.handleTunnelIn(t, endX, x, y, z, h)

    
    def getTunnelInToonTrack(self, endX, tunnelOrigin):
        pivotNode = tunnelOrigin.attachNewNode(self.uniqueName('pivotNode'))
        pivotNode.setPos(*self.tunnelPivotPos)
        pivotNode.setHpr(0, 0, 0)
        pivotY = pivotNode.getY(tunnelOrigin)
        endY = 5.0
        straightLerpDur = abs(endY - pivotY) / ToonForwardSpeed
        pivotDur = 2.0
        pivotLerpDur = pivotDur * (90.0 / self.pivotAngle)
        self.reparentTo(pivotNode)
        self.setPos(0, 0, 0)
        self.setX(tunnelOrigin, endX)
        targetX = self.getX()
        self.setX(self.tunnelCenterOffset + (targetX - self.tunnelCenterOffset) * (1.0 - self.tunnelCenterInfluence))
        self.setHpr(tunnelOrigin, 0, 0, 0)
        pivotNode.setH(-(self.pivotAngle))
        return Sequence(Wait(0.80000000000000004), Parallel(LerpHprInterval(pivotNode, pivotDur, hpr = Point3(0, 0, 0), name = self.uniqueName('tunnelInPivot')), Sequence(Wait(pivotDur - pivotLerpDur), LerpPosInterval(self, pivotLerpDur, pos = Point3(targetX, 0, 0), name = self.uniqueName('tunnelInPivotLerpPos')))), Func(self.wrtReparentTo, render), Func(pivotNode.removeNode), LerpPosInterval(self, straightLerpDur, pos = Point3(endX, endY, 0.10000000000000001), other = tunnelOrigin, name = self.uniqueName('tunnelInStraightLerp')))

    
    def handleTunnelIn(self, startTime, endX, x, y, z, h):
        self.stopSmooth()
        tunnelOrigin = render.attachNewNode('tunnelOrigin')
        tunnelOrigin.setPosHpr(x, y, z, h, 0, 0)
        self.tunnelTrack = Sequence(self.getTunnelInToonTrack(endX, tunnelOrigin), Func(tunnelOrigin.removeNode), Func(self.startSmooth))
        tOffset = globalClock.getFrameTime() - startTime + self.smoother.getDelay()
        if tOffset < 0.0:
            self.tunnelTrack = Sequence(Wait(-tOffset), self.tunnelTrack)
            self.tunnelTrack.start()
        else:
            self.tunnelTrack.start(tOffset)

    
    def b_setTunnelOut(self, startX, startY, tunnelOrigin):
        timestamp = globalClockDelta.getFrameNetworkTime()
        pos = tunnelOrigin.getPos(render)
        h = tunnelOrigin.getH(render)
        self.setTunnelOut(timestamp, startX, startY, pos[0], pos[1], pos[2], h)
        self.d_setTunnelOut(timestamp, startX, startY, pos[0], pos[1], pos[2], h)

    
    def d_setTunnelOut(self, timestamp, startX, startY, x, y, z, h):
        self.sendUpdate('setTunnelOut', [
            timestamp,
            startX,
            startY,
            x,
            y,
            z,
            h])

    
    def setTunnelOut(self, timestamp, startX, startY, x, y, z, h):
        t = globalClockDelta.networkToLocalTime(timestamp)
        self.handleTunnelOut(t, startX, startY, x, y, z, h)

    
    def getTunnelOutToonTrack(self, startX, startY, tunnelOrigin):
        startPos = self.getPos(tunnelOrigin)
        startHpr = self.getHpr(tunnelOrigin)
        reducedAvH = fitDestAngle2Src(startHpr[0], 180)
        pivotNode = tunnelOrigin.attachNewNode(self.uniqueName('pivotNode'))
        pivotNode.setPos(*self.tunnelPivotPos)
        pivotNode.setHpr(0, 0, 0)
        pivotY = pivotNode.getY(tunnelOrigin)
        straightLerpDur = abs(startY - pivotY) / ToonForwardSpeed
        pivotDur = 2.0
        pivotLerpDur = pivotDur * (90.0 / self.pivotAngle)
        
        def getTargetPos(self = self):
            pos = self.getPos()
            return Point3(self.tunnelCenterOffset + (pos[0] - self.tunnelCenterOffset) * (1.0 - self.tunnelCenterInfluence), pos[1], pos[2])

        return Sequence(Parallel(LerpPosInterval(self, straightLerpDur, pos = Point3(startX, pivotY, 0.10000000000000001), startPos = startPos, other = tunnelOrigin, name = self.uniqueName('tunnelOutStraightLerp')), LerpHprInterval(self, straightLerpDur * 0.80000000000000004, hpr = Point3(reducedAvH, 0, 0), startHpr = startHpr, other = tunnelOrigin, name = self.uniqueName('tunnelOutStraightLerpHpr'))), Func(self.wrtReparentTo, pivotNode), Parallel(LerpHprInterval(pivotNode, pivotDur, hpr = Point3(-(self.pivotAngle), 0, 0), name = self.uniqueName('tunnelOutPivot')), LerpPosInterval(self, pivotLerpDur, pos = getTargetPos, name = self.uniqueName('tunnelOutPivotLerpPos'))), Func(self.wrtReparentTo, render), Func(pivotNode.removeNode))

    
    def handleTunnelOut(self, startTime, startX, startY, x, y, z, h):
        tunnelOrigin = render.attachNewNode('tunnelOrigin')
        tunnelOrigin.setPosHpr(x, y, z, h, 0, 0)
        self.tunnelTrack = Sequence(Func(self.stopSmooth), self.getTunnelOutToonTrack(startX, startY, tunnelOrigin), Func(self.detachNode), Func(tunnelOrigin.removeNode))
        tOffset = globalClock.getFrameTime() - startTime + self.smoother.getDelay()
        if tOffset < 0.0:
            self.tunnelTrack = Sequence(Wait(-tOffset), self.tunnelTrack)
            self.tunnelTrack.start()
        else:
            self.tunnelTrack.start(tOffset)

    
    def enterTeleportOut(self, *args, **kw):
        Toon.Toon.enterTeleportOut(self, *args, **args)
        if self.track:
            self.track.delayDelete = DelayDelete.DelayDelete(self)
        

    
    def b_setAnimState(self, animName, animMultiplier = 1.0, callback = None, extraArgs = []):
        self.d_setAnimState(animName, animMultiplier, None, extraArgs)
        self.setAnimState(animName, animMultiplier, None, None, callback, extraArgs)

    
    def d_setAnimState(self, animName, animMultiplier = 1.0, timestamp = None, extraArgs = []):
        timestamp = globalClockDelta.getFrameNetworkTime()
        self.sendUpdate('setAnimState', [
            animName,
            animMultiplier,
            timestamp])

    
    def setAnimState(self, animName, animMultiplier = 1.0, timestamp = None, animType = None, callback = None, extraArgs = []):
        if timestamp == None:
            ts = 0.0
        else:
            ts = globalClockDelta.localElapsedTime(timestamp)
        self.animFSM.request(animName, [
            animMultiplier,
            ts,
            callback,
            extraArgs])
        self.cleanupPieInHand()

    
    def b_setEmoteState(self, animIndex, animMultiplier):
        self.setEmoteState(animIndex, animMultiplier)
        self.d_setEmoteState(animIndex, animMultiplier)

    
    def d_setEmoteState(self, animIndex, animMultiplier):
        timestamp = globalClockDelta.getFrameNetworkTime()
        self.sendUpdate('setEmoteState', [
            animIndex,
            animMultiplier,
            timestamp])

    
    def setEmoteState(self, animIndex, animMultiplier, timestamp = None):
        if animIndex == TTEmote.EmoteClear:
            return None
        
        if timestamp == None:
            ts = 0.0
        else:
            ts = globalClockDelta.localElapsedTime(timestamp)
        callback = None
        extraArgs = []
        extraArgs.insert(0, animIndex)
        self.doEmote(animIndex, animMultiplier, ts, callback, extraArgs)

    
    def setCogStatus(self, cogStatusList):
        self.cogs = cogStatusList

    
    def setCogCount(self, cogCountList):
        self.cogCounts = cogCountList
        if hasattr(self, 'suitPage'):
            self.suitPage.updatePage()
        

    
    def setCogRadar(self, radar):
        self.cogRadar = radar
        if hasattr(self, 'suitPage'):
            self.suitPage.updateCogRadarButtons(radar)
        

    
    def setBuildingRadar(self, radar):
        self.buildingRadar = radar
        if hasattr(self, 'suitPage'):
            self.suitPage.updateBuildingRadarButtons(radar)
        

    
    def setCogTypes(self, types):
        self.cogTypes = types
        if self.disguisePage:
            self.disguisePage.updatePage()
        

    
    def setCogLevels(self, levels):
        self.cogLevels = levels
        if self.disguisePage:
            self.disguisePage.updatePage()
        

    
    def getCogLevels(self):
        return self.cogLevels

    
    def setCogParts(self, parts):
        self.cogParts = parts
        if self.disguisePage:
            self.disguisePage.updatePage()
        

    
    def getCogParts(self):
        return self.cogParts

    
    def setCogMerits(self, merits):
        self.cogMerits = merits
        if self.disguisePage:
            self.disguisePage.updatePage()
        

    
    def readyForPromotion(self, dept):
        merits = base.localAvatar.cogMerits[dept]
        totalMerits = CogDisguiseGlobals.getTotalMerits(self, dept)
        if merits >= totalMerits:
            return 1
        else:
            return 0

    
    def setCogIndex(self, index):
        self.cogIndex = index
        if self.cogIndex == -1:
            if self.isDisguised:
                self.takeOffSuit()
            
        else:
            cogIndex = self.cogTypes[index] + SuitDNA.suitsPerDept * index
            cog = SuitDNA.suitHeadTypes[cogIndex]
            self.putOnSuit(cog)

    
    def isCog(self):
        if self.cogIndex == -1:
            return 0
        else:
            return 1

    
    def setDisguisePageFlag(self, flag):
        if flag and hasattr(self, 'book'):
            self.loadDisguisePages()
        
        self.disguisePageFlag = flag

    
    def setFishCollection(self, genusList, speciesList, weightList):
        self.fishCollection = FishCollection.FishCollection()
        self.fishCollection.makeFromNetLists(genusList, speciesList, weightList)

    
    def getFishCollection(self):
        return self.fishCollection

    
    def setMaxFishTank(self, maxTank):
        self.maxFishTank = maxTank

    
    def getMaxFishTank(self):
        return self.maxFishTank

    
    def setFishTank(self, genusList, speciesList, weightList):
        self.fishTank = FishTank.FishTank()
        self.fishTank.makeFromNetLists(genusList, speciesList, weightList)

    
    def getFishTank(self):
        return self.fishTank

    
    def isFishTankFull(self):
        return len(self.fishTank) >= self.maxFishTank

    
    def setFishingRod(self, rodId):
        self.fishingRod = rodId

    
    def getFishingRod(self):
        return self.fishingRod

    
    def setFishingTrophies(self, trophyList):
        self.fishingTrophies = trophyList

    
    def getFishingTrophies(self):
        return self.fishingTrophies

    
    def setQuests(self, flattenedQuests):
        questList = []
        questLen = 5
        for i in range(0, len(flattenedQuests), questLen):
            questList.append(flattenedQuests[i:i + questLen])
        
        self.quests = questList
        if self == base.localAvatar:
            messenger.send('questsChanged')
        

    
    def setQuestCarryLimit(self, limit):
        self.questCarryLimit = limit
        if self == base.localAvatar:
            messenger.send('questsChanged')
        

    
    def getQuestCarryLimit(self):
        return self.questCarryLimit

    
    def setMaxCarry(self, maxCarry):
        self.maxCarry = maxCarry
        if self.inventory:
            self.inventory.updateGUI()
        

    
    def getMaxCarry(self):
        return self.maxCarry

    
    def setCheesyEffect(self, effect, hoodId, expireTime):
        self.savedCheesyEffect = effect
        self.savedCheesyHoodId = hoodId
        self.savedCheesyExpireTime = expireTime
        if self == base.localAvatar:
            self.notify.info('setCheesyEffect(%s, %s, %s)' % (effect, hoodId, expireTime))
            if effect != ToontownGlobals.CENormal:
                serverTime = time.time() + self.cr.getServerDelta()
                duration = expireTime * 60 - serverTime
                if duration < 0:
                    self.notify.info('effect should have expired %s ago.' % PythonUtil.formatElapsedSeconds(-duration))
                else:
                    self.notify.info('effect will expire in %s.' % PythonUtil.formatElapsedSeconds(duration))
            
        
        if self.activeState == DistributedObject.ESGenerated:
            self.reconsiderCheesyEffect(lerpTime = 0.5)
        else:
            self.reconsiderCheesyEffect()

    
    def reconsiderCheesyEffect(self, lerpTime = 0):
        effect = self.savedCheesyEffect
        hoodId = self.savedCheesyHoodId
        if not self.cr.areCheesyEffectsAllowed():
            effect = CENormal
        
        if hoodId != 0:
            
            try:
                currentHoodId = base.cr.playGame.hood.id
            except:
                currentHoodId = None

            if hoodId == 1:
                if currentHoodId == ToontownGlobals.ToontownCentral:
                    effect = CENormal
                
            elif currentHoodId != None and currentHoodId != hoodId:
                effect = CENormal
            
        
        if self.ghostMode:
            effect = CEGhost
        
        self.applyCheesyEffect(effect, lerpTime = lerpTime)

    
    def setGhostMode(self, flag):
        if self.ghostMode != flag:
            self.ghostMode = flag
            if not hasattr(self, 'cr'):
                return None
            
            if self.activeState <= DistributedObject.ESDisabled:
                self.notify.debug('not applying cheesy effect to disabled Toon')
            elif self.activeState == DistributedObject.ESGenerating:
                self.reconsiderCheesyEffect()
            elif self.activeState == DistributedObject.ESGenerated:
                self.reconsiderCheesyEffect(lerpTime = 0.5)
            else:
                self.notify.warning('unknown activeState: %s' % self.activeState)
            self.showNametag2d()
            self.showNametag3d()
            if hasattr(self, 'collNode'):
                if self.ghostMode:
                    self.collNode.setCollideMask(ToontownGlobals.GhostBitmask)
                else:
                    self.collNode.setCollideMask(ToontownGlobals.WallBitmask | ToontownGlobals.PieBitmask)
            
            if self.isLocal():
                if self.ghostMode:
                    self.useGhostControls()
                else:
                    self.useWalkControls()
            
        

    if hasattr(base, 'wantPets') and base.wantPets:
        
        def setPetTrickPhrases(self, petTricks):
            self.petTrickPhrases = petTricks
            if self.isLocal():
                messenger.send('petTrickPhrasesChanged')
            

    
    
    def setCustomMessages(self, customMessages):
        self.customMessages = customMessages
        if self.isLocal():
            messenger.send('customMessagesChanged')
        

    
    def setResistanceMessages(self, resistanceMessages):
        self.resistanceMessages = resistanceMessages
        if self.isLocal():
            messenger.send('resistanceMessagesChanged')
        

    
    def getResistanceMessageCharges(self, textId):
        msgs = self.resistanceMessages
        for i in range(len(msgs)):
            if msgs[i][0] == textId:
                return msgs[i][1]
            
        
        return 0

    
    def setCatalogSchedule(self, currentWeek, nextTime):
        self.catalogScheduleCurrentWeek = currentWeek
        self.catalogScheduleNextTime = nextTime
        if self.isLocal():
            self.notify.info('setCatalogSchedule(%s, %s)' % (currentWeek, nextTime))
            if nextTime:
                serverTime = time.time() + self.cr.getServerDelta()
                duration = nextTime * 60 - serverTime
                self.notify.info('next catalog in %s.' % PythonUtil.formatElapsedSeconds(duration))
            
        

    
    def setCatalog(self, monthlyCatalog, weeklyCatalog, backCatalog):
        self.monthlyCatalog = CatalogItemList.CatalogItemList(monthlyCatalog)
        self.weeklyCatalog = CatalogItemList.CatalogItemList(weeklyCatalog)
        self.backCatalog = CatalogItemList.CatalogItemList(backCatalog)
        if self.catalogNotify == ToontownGlobals.NewItems:
            self.catalogNotify = ToontownGlobals.OldItems
        

    
    def setCatalogNotify(self, catalogNotify, mailboxNotify):
        if len(self.weeklyCatalog) + len(self.monthlyCatalog) == 0:
            catalogNotify = ToontownGlobals.NoItems
        
        if len(self.mailboxContents) == 0:
            mailboxNotify = ToontownGlobals.NoItems
        
        self.catalogNotify = catalogNotify
        self.mailboxNotify = mailboxNotify
        if self.isLocal():
            self.gotCatalogNotify = 1
            self.refreshOnscreenButtons()
        

    
    def setDeliverySchedule(self, onOrder):
        self.onOrder = CatalogItemList.CatalogItemList(onOrder, store = CatalogItem.Customization | CatalogItem.DeliveryDate)
        if self == base.localAvatar:
            nextTime = self.onOrder.getNextDeliveryDate()
            if nextTime != None:
                serverTime = time.time() + self.cr.getServerDelta()
                duration = nextTime * 60 - serverTime
                self.notify.info('next delivery in %s.' % PythonUtil.formatElapsedSeconds(duration))
            
        

    
    def setMailboxContents(self, mailboxContents):
        self.mailboxContents = CatalogItemList.CatalogItemList(mailboxContents, store = CatalogItem.Customization)

    
    def playSplashEffect(self, x, y, z):
        Splash = Splash
        import toontown.effects
        if self.splash == None:
            self.splash = Splash.Splash(render)
        
        self.splash.setPos(x, y, z)
        self.splash.setScale(2)
        self.splash.play()
        place = base.cr.playGame.getPlace()
        base.playSfx(place.loader.submergeSound, node = self)

    
    def d_playSplashEffect(self, x, y, z):
        self.sendUpdate('playSplashEffect', [
            x,
            y,
            z])

    
    def setTrackAccess(self, trackArray):
        self.trackArray = trackArray
        if self.inventory:
            self.inventory.updateGUI()
        

    
    def getTrackAccess(self):
        return self.trackArray

    
    def hasTrackAccess(self, track):
        return self.trackArray[track]

    
    def setTrackProgress(self, trackId, progress):
        self.trackProgressId = trackId
        self.trackProgress = progress
        if hasattr(self, 'trackPage'):
            self.trackPage.updatePage()
        

    
    def getTrackProgress(self):
        return [
            self.trackProgressId,
            self.trackProgress]

    
    def getTrackProgressAsArray(self, maxLength = 15):
        shifts = map(operator.rshift, maxLength * [
            self.trackProgress], range(maxLength - 1, -1, -1))
        digits = map(operator.mod, shifts, maxLength * [
            2])
        digits.reverse()
        return digits

    
    def setTeleportAccess(self, teleportZoneArray):
        self.teleportZoneArray = teleportZoneArray

    
    def getTeleportAccess(self):
        return self.teleportZoneArray

    
    def hasTeleportAccess(self, zoneId):
        return zoneId in self.teleportZoneArray

    
    def setQuestHistory(self, questList):
        self.questHistory = questList

    
    def getQuestHistory(self):
        return self.questHistory

    
    def setRewardHistory(self, rewardTier, rewardList):
        self.rewardTier = rewardTier
        self.rewardHistory = rewardList

    
    def getRewardHistory(self):
        return (self.rewardTier, self.rewardHistory)

    
    def doSmoothTask(self, task):
        self.smoother.computeAndApplySmoothMat(self)
        self.setSpeed(self.smoother.getSmoothForwardVelocity(), self.smoother.getSmoothRotationalVelocity())
        return Task.cont

    
    def d_setParent(self, parentToken):
        DistributedSmoothNode.DistributedSmoothNode.d_setParent(self, parentToken)

    
    def setEmoteAccess(self, bits):
        self.emoteAccess = bits
        if self == base.localAvatar:
            messenger.send('emotesChanged')
        

    
    def b_setHouseId(self, id):
        self.setHouseId(id)
        self.d_setHouseId(id)

    
    def d_setHouseId(self, id):
        self.sendUpdate('setHouseId', [
            id])

    
    def setHouseId(self, id):
        self.houseId = id

    
    def getHouseId(self):
        return self.houseId

    
    def setPosIndex(self, index):
        self.posIndex = index

    
    def getPosIndex(self):
        return self.posIndex

    
    def b_setSpeedChatStyleIndex(self, index):
        self.setSpeedChatStyleIndex(index)
        self.d_setSpeedChatStyleIndex(index)
        return None

    
    def d_setSpeedChatStyleIndex(self, index):
        self.sendUpdate('setSpeedChatStyleIndex', [
            index])

    
    def setSpeedChatStyleIndex(self, index):
        self.speedChatStyleIndex = index
        (nameKey, arrowColor, rolloverColor, frameColor) = speedChatStyles[index]
        self.nametag.setQtColor(VBase4(frameColor[0], frameColor[1], frameColor[2], 1))
        if self.isLocal():
            messenger.send('SpeedChatStyleChange', [])
        

    
    def getSpeedChatStyleIndex(self):
        return self.speedChatStyleIndex

    
    def setMaxMoney(self, maxMoney):
        self.maxMoney = maxMoney

    
    def getMaxMoney(self):
        return self.maxMoney

    
    def setMoney(self, money):
        if money != self.money:
            self.money = money
            messenger.send(self.uniqueName('moneyChange'), [
                self.money])
        

    
    def getMoney(self):
        return self.money

    
    def setMaxBankMoney(self, maxMoney):
        self.maxBankMoney = maxMoney

    
    def getMaxBankMoney(self):
        return self.maxBankMoney

    
    def setBankMoney(self, money):
        self.bankMoney = money
        messenger.send(self.uniqueName('bankMoneyChange'), [
            self.bankMoney])

    
    def getBankMoney(self):
        return self.bankMoney

    
    def getTotalMoney(self):
        return self.getBankMoney() + self.getMoney()

    
    def presentPie(self, x, y, z, h, p, r, timestamp32):
        if self.numPies <= 0:
            return None
        
        if launcher and not launcher.getPhaseComplete(5):
            return None
        
        lastTossTrack = Sequence()
        if self.tossTrack:
            lastTossTrack = self.tossTrack
            tossTrack = None
        
        ts = globalClockDelta.localElapsedTime(timestamp32, bits = 32)
        ts -= SmoothMover.getDelay()
        ival = self.getPresentPieInterval(x, y, z, h, p, r)
        if ts > 0:
            startTime = ts
            lastTossTrack.finish()
        else:
            ival = Sequence(Wait(-ts), ival)
            lastTossTrack.finish()
            startTime = 0
        ival = Sequence(ival)
        ival.start(startTime)
        self.tossTrack = ival

    
    def tossPie(self, x, y, z, h, p, r, sequence, power, timestamp32):
        if self.numPies <= 0:
            return None
        
        if self.numPies != ToontownGlobals.FullPies:
            self.setNumPies(self.numPies - 1)
        
        self.lastTossedPie = globalClock.getFrameTime()
        if launcher and not launcher.getPhaseComplete(5):
            return None
        
        lastTossTrack = Sequence()
        if self.tossTrack:
            lastTossTrack = self.tossTrack
            tossTrack = None
        
        lastPieTrack = Sequence()
        if self.pieTracks.has_key(sequence):
            lastPieTrack = self.pieTracks[sequence]
            del self.pieTracks[sequence]
        
        ts = globalClockDelta.localElapsedTime(timestamp32, bits = 32)
        ts -= SmoothMover.getDelay()
        (toss, pie, flyPie) = self.getTossPieInterval(x, y, z, h, p, r, power)
        if ts > 0:
            startTime = ts
            lastTossTrack.finish()
            lastPieTrack.finish()
        else:
            toss = Sequence(Wait(-ts), toss)
            pie = Sequence(Wait(-ts), pie)
            lastTossTrack.finish()
            lastPieTrack.finish()
            startTime = 0
        self.tossTrack = toss
        toss.start(startTime)
        pie = Sequence(pie, Func(self.pieFinishedFlying, sequence))
        self.pieTracks[sequence] = pie
        pie.start(startTime)

    
    def pieFinishedFlying(self, sequence):
        if self.pieTracks.has_key(sequence):
            del self.pieTracks[sequence]
        

    
    def pieFinishedSplatting(self, sequence):
        if self.splatTracks.has_key(sequence):
            del self.splatTracks[sequence]
        

    
    def pieSplat(self, x, y, z, sequence, pieCode, timestamp32):
        if self.isLocal():
            return None
        
        elapsed = globalClock.getFrameTime() - self.lastTossedPie
        if elapsed > 30:
            return None
        
        if launcher and not launcher.getPhaseComplete(5):
            return None
        
        lastPieTrack = Sequence()
        if self.pieTracks.has_key(sequence):
            lastPieTrack = self.pieTracks[sequence]
            del self.pieTracks[sequence]
        
        if self.splatTracks.has_key(sequence):
            lastSplatTrack = self.splatTracks[sequence]
            del self.splatTracks[sequence]
            lastSplatTrack.finish()
        
        ts = globalClockDelta.localElapsedTime(timestamp32, bits = 32)
        ts -= SmoothMover.getDelay()
        splat = self.getPieSplatInterval(x, y, z, pieCode)
        splat = Sequence(Func(messenger.send, 'pieSplat', [
            self,
            pieCode]), splat)
        if ts > 0:
            startTime = ts
            lastPieTrack.finish()
        else:
            splat = Sequence(Wait(-ts), splat)
            startTime = 0
        splat = Sequence(splat, Func(self.pieFinishedSplatting, sequence))
        self.splatTracks[sequence] = splat
        splat.start(startTime)

    
    def cleanupPies(self):
        for track in self.pieTracks.values():
            track.finish()
        
        self.pieTracks = { }
        for track in self.splatTracks.values():
            track.finish()
        
        self.splatTracks = { }
        self.cleanupPieInHand()

    
    def cleanupPieInHand(self):
        if self.tossTrack:
            self.tossTrack.finish()
            self.tossTrack = None
        
        self.cleanupPieModel()

    
    def setNumPies(self, numPies):
        self.numPies = numPies
        if self.isLocal():
            self.updatePieButton()
            if numPies == 0:
                self.interruptPie()
            
        

    
    def setPieType(self, pieType):
        self.pieType = pieType
        if self.isLocal():
            self.updatePieButton()
        

    
    def setTrophyScore(self, score):
        self.trophyScore = score
        if self.trophyStar != None:
            self.trophyStar.removeNode()
            self.trophyStar = None
        
        if self.trophyStarSpeed != 0:
            taskMgr.remove(self.uniqueName('starSpin'))
            self.trophyStarSpeed = 0
        
        if self.trophyScore >= ToontownGlobals.TrophyStarLevels[4]:
            self.trophyStar = loader.loadModelCopy('phase_3.5/models/gui/name_star')
            self.trophyStar.reparentTo(self.nametag.getNameIcon())
            self.trophyStar.setScale(2)
            self.trophyStar.setZ(2)
            self.trophyStar.setColor(ToontownGlobals.TrophyStarColors[4])
            self.trophyStarSpeed = 15
            if self.trophyScore >= ToontownGlobals.TrophyStarLevels[5]:
                taskMgr.add(self._DistributedToon__starSpin, self.uniqueName('starSpin'))
            
        elif self.trophyScore >= ToontownGlobals.TrophyStarLevels[2]:
            self.trophyStar = loader.loadModelCopy('phase_3.5/models/gui/name_star')
            self.trophyStar.reparentTo(self.nametag.getNameIcon())
            self.trophyStar.setScale(1.5)
            self.trophyStar.setZ(1.6000000000000001)
            self.trophyStar.setColor(ToontownGlobals.TrophyStarColors[2])
            self.trophyStarSpeed = 10
            if self.trophyScore >= ToontownGlobals.TrophyStarLevels[3]:
                taskMgr.add(self._DistributedToon__starSpin, self.uniqueName('starSpin'))
            
        elif self.trophyScore >= ToontownGlobals.TrophyStarLevels[0]:
            self.trophyStar = loader.loadModelCopy('phase_3.5/models/gui/name_star')
            self.trophyStar.reparentTo(self.nametag.getNameIcon())
            self.trophyStar.setScale(1.5)
            self.trophyStar.setZ(1.6000000000000001)
            self.trophyStar.setColor(ToontownGlobals.TrophyStarColors[0])
            self.trophyStarSpeed = 8
            if self.trophyScore >= ToontownGlobals.TrophyStarLevels[1]:
                taskMgr.add(self._DistributedToon__starSpin, self.uniqueName('starSpin'))
            
        

    
    def _DistributedToon__starSpin(self, task):
        now = globalClock.getFrameTime()
        r = now * self.trophyStarSpeed % 360.0
        self.trophyStar.setR(r)
        return Task.cont

    
    def getZoneId(self):
        return base.cr.playGame.getPlace().getZoneId()

    
    def getRequestID(self):
        return CLIENT_GET_AVATAR_DETAILS

    
    def announceBingo(self):
        self.setChatAbsolute(TTLocalizer.FishBingoBingo, CFSpeech | CFTimeout)

    
    def squish(self, damage):
        if self == base.localAvatar:
            base.cr.playGame.getPlace().fsm.request('squished')
            self.stunToon()
            self.setZ(self.getZ(render) + 0.025000000000000001)
        

    
    def d_squish(self, damage):
        self.sendUpdate('squish', [
            damage])

    
    def b_squish(self, damage):
        if not (self.isStunned):
            self.squish(damage)
            self.d_squish(damage)
            self.playDialogueForString('!')
        

    if hasattr(base, 'wantPets') and base.wantPets:
        
        def setPetId(self, petId):
            self.petId = petId
            if petId == 0:
                self.petDNA = None
            elif self.isLocal():
                base.cr.addPetToFriendsMap()
            

        
        def getPetId(self):
            return self.petId

        
        def getPetId(self):
            return self.petId

        
        def hasPet(self):
            return self.petId != 0

        
        def b_setPetTutorialDone(self, bDone):
            self.d_setPetTutorialDone(bDone)
            self.setPetTutorialDone(bDone)

        
        def d_setPetTutorialDone(self, bDone):
            self.sendUpdate('setPetTutorialDone', [
                bDone])

        
        def setPetTutorialDone(self, bDone):
            self.bPetTutorialDone = bDone

        
        def b_setFishBingoTutorialDone(self, bDone):
            self.d_setFishBingoTutorialDone(bDone)
            self.setFishBingoTutorialDone(bDone)

        
        def d_setFishBingoTutorialDone(self, bDone):
            self.sendUpdate('setFishBingoTutorialDone', [
                bDone])

        
        def setFishBingoTutorialDone(self, bDone):
            self.bFishBingoTutorialDone = bDone

        
        def b_setFishBingoMarkTutorialDone(self, bDone):
            self.d_setFishBingoMarkTutorialDone(bDone)
            self.setFishBingoMarkTutorialDone(bDone)

        
        def d_setFishBingoMarkTutorialDone(self, bDone):
            self.sendUpdate('setFishBingoMarkTutorialDone', [
                bDone])

        
        def setFishBingoMarkTutorialDone(self, bDone):
            self.bFishBingoMarkTutorialDone = bDone

        
        def b_setPetMovie(self, petId, flag):
            self.d_setPetMovie(petId, flag)
            self.setPetMovie(petId, flag)

        
        def d_setPetMovie(self, petId, flag):
            self.sendUpdate('setPetMovie', [
                petId,
                flag])

        
        def setPetMovie(self, petId, flag):
            pass

        
        def lookupPetDNA(self):
            if self.petId and not (self.petDNA):
                PetDetail = PetDetail
                import toontown.pets
                PetDetail.PetDetail(self.petId, self._DistributedToon__petDetailsLoaded)
            

        
        def _DistributedToon__petDetailsLoaded(self, pet):
            self.petDNA = pet.style

    

