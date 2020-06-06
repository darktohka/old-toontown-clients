# File: D (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from ClockDelta import *
from IntervalGlobal import *
import ToontownGlobals
import DirectNotifyGlobal
import DistributedAvatar
import Avatar
import Toon
import DistributedSmoothNode
import DistributedObject
import FSM
import ZoneUtil
import DelayDelete
import PythonUtil
import CatalogItemList
import CatalogItem
from Emote import *
from OptionsPage import speedChatStyles

class DistributedToon(DistributedAvatar.DistributedAvatar, Toon.Toon, DistributedSmoothNode.DistributedSmoothNode):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToon')
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedToon_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)
            Toon.Toon.__init__(self)
            DistributedSmoothNode.DistributedSmoothNode.__init__(self, cr)
            self.safeZonesVisited = []
            self.teleportCheat = base.config.GetBool('teleport-all', 0)
            self.friendsList = []
            self.oldFriendsList = None
            self.timeFriendsListChanged = None
            self.ignoreList = []
            self.earnedExperience = None
            self.track = None
            self.maxCarry = 0
            self.savedCheesyEffect = CENormal
            self.savedCheesyHoodId = 0
            self.savedCheesyExpireTime = 0
            self.customMessages = []
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


    
    def disable(self):
        self.animFSM.request('off')
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
        
        if self.tunnelTrack:
            self.tunnelTrack.finish()
            self.tunnelTrack = None
        
        DistributedAvatar.DistributedAvatar.disable(self)

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedToon_deleted = 1
            del self.safeZonesVisited
            DistributedAvatar.DistributedAvatar.delete(self)
            Toon.Toon.delete(self)


    
    def generate(self):
        DistributedAvatar.DistributedAvatar.generate(self)
        self.startBlink()
        self.startSmooth()

    
    def playDialogue(self, *args):
        Toon.Toon.playDialogue(self, *args)

    
    def setDefaultShard(self, shard):
        self.defaultShard = shard
        self.notify.debug('setting default shard to %s' % shard)

    
    def setDefaultZone(self, zoneId):
        hoodPhase = toonbase.tcr.hoodMgr.getPhaseFromHood(zoneId)
        if launcher and not launcher.getPhaseComplete(hoodPhase):
            self.notify.debug('default zone %s not downloaded yet. Reverting to ToontownCentral.' % zoneId)
            self.defaultZone = ToontownCentral
        else:
            self.notify.debug('setting default zone to %s' % zoneId)
            self.defaultZone = zoneId

    
    def setShtickerBook(self, string):
        self.notify.debug('setting Shticker Book to %s' % string)

    
    def getFriendsList(self):
        return self.friendsList

    
    def setFriendsList(self, friendsList):
        self.oldFriendsList = self.friendsList
        self.friendsList = friendsList
        self.timeFriendsListChanged = globalClock.getFrameTime()
        self.notify.debug('setting friends list to %s' % self.friendsList)
        messenger.send('friendsListChanged')
        Avatar.reconsiderAllUnderstandable()

    
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

    
    def isClosetFull(self, extraClothes = 0):
        numClothes = len(self.clothesTopsList) / 4 + len(self.clothesBottomsList) / 2
        return numClothes + extraClothes >= self.maxClothes

    
    def setInterface(self, string):
        self.notify.debug('setting interface to %s' % string)

    
    def setZonesVisited(self, hoods):
        self.safeZonesVisited = hoods
        self.notify.debug('setting safe zone list to %s' % self.safeZonesVisited)

    
    def setHoodsVisited(self, hoods):
        self.hoodsVisited = hoods
        self.notify.debug('setting hood list to %s' % self.hoodsVisited)

    
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
        self.notify.debug('DistributedToon.handleTunnelIn')
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
        self.notify.debug('DistributedToon.handleTunnelOut')
        tunnelOrigin = render.attachNewNode('tunnelOrigin')
        tunnelOrigin.setPosHpr(x, y, z, h, 0, 0)
        self.tunnelTrack = Sequence(Func(self.stopSmooth), self.getTunnelOutToonTrack(startX, startY, tunnelOrigin), Func(self.reparentTo, hidden), Func(tunnelOrigin.removeNode))
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
        

    
    def b_setAnimState(self, animName, animMultiplier, callback = None, extraArgs = []):
        self.setAnimState(animName, animMultiplier, None, None, callback, extraArgs)
        self.d_setAnimState(animName, animMultiplier, None, extraArgs)

    
    def d_setAnimState(self, animName, animMultiplier, timestamp = None, extraArgs = []):
        timestamp = globalClockDelta.getFrameNetworkTime()
        self.sendUpdate('setAnimState', [
            animName,
            animMultiplier,
            timestamp])

    
    def setAnimState(self, animName, animMultiplier, timestamp = None, animType = None, callback = None, extraArgs = []):
        if timestamp == None:
            ts = 0.0
        else:
            ts = globalClockDelta.localElapsedTime(timestamp)
        self.animFSM.request(animName, [
            animMultiplier,
            ts,
            callback,
            extraArgs])

    
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
        if timestamp == None:
            ts = 0.0
        else:
            ts = globalClockDelta.localElapsedTime(timestamp)
        callback = None
        extraArgs = []
        extraArgs.insert(0, animIndex)
        self.doEmote(animIndex, animMultiplier, ts, callback, extraArgs)

    
    def setCogStatus(self, cogStatusList):
        self.notify.debug('setting cogs to %s' % cogStatusList)
        self.cogs = cogStatusList
        if hasattr(self, 'suitPage'):
            self.suitPage.updatePage()
        

    
    def setCogCount(self, cogCountList):
        self.notify.debug('setting cogCount to %s' % cogCountList)
        self.cogCounts = cogCountList
        if hasattr(self, 'suitPage'):
            self.suitPage.updatePage()
        

    
    def setCogRadar(self, radar):
        self.notify.debug('setting cog radar to: %s' % radar)
        self.cogRadar = radar
        if hasattr(self, 'suitPage'):
            self.suitPage.updateCogRadarButtons(radar)
        

    
    def setBuildingRadar(self, radar):
        self.notify.debug('setting building radar to: %s' % radar)
        self.buildingRadar = radar
        if hasattr(self, 'suitPage'):
            self.suitPage.updateBuildingRadarButtons(radar)
        

    
    def setFishes(self, fishList):
        self.notify.debug('setting fish to %s' % fishList)
        self.fishes = fishList
        if hasattr(self, 'fishPage'):
            self.fishPage.updatePage()
        

    
    def setQuests(self, flattenedQuests):
        self.notify.debug('setting quests to %s' % flattenedQuests)
        questList = []
        questLen = 5
        for i in range(0, len(flattenedQuests), questLen):
            questList.append(flattenedQuests[i:i + questLen])
        
        self.quests = questList
        if self == toonbase.localToon:
            messenger.send('questsChanged')
        

    
    def setQuestCarryLimit(self, limit):
        self.notify.debug('setting questCarryLimit to %s' % limit)
        self.questCarryLimit = limit
        if self == toonbase.localToon:
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
        if self == toonbase.localToon:
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
                currentHoodId = toonbase.tcr.playGame.hood.id
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
            
            if self.activeState == DistributedObject.ESGenerated:
                self.reconsiderCheesyEffect(lerpTime = 0.5)
            else:
                self.reconsiderCheesyEffect()
            self.showNametag2d()
            self.showNametag3d()
            if hasattr(self, 'collNode'):
                if self.ghostMode:
                    self.collNode.setCollideMask(ToontownGlobals.GhostBitmask)
                else:
                    self.collNode.setCollideMask(ToontownGlobals.WallBitmask)
            
            if self.isLocal():
                if self.ghostMode:
                    self.enableGhostMode()
                else:
                    self.disableGhostMode()
            
        

    
    def setCustomMessages(self, customMessages):
        self.customMessages = customMessages
        if self.isLocal():
            messenger.send('customMessagesChanged')
        

    
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
        
        if self.isLocal():
            if mailboxNotify != self.mailboxNotify and mailboxNotify == ToontownGlobals.NewItems:
                self.setSystemMessage(Localizer.Clarabelle, Localizer.NewDeliveryNotify)
            
            if catalogNotify != self.catalogNotify and catalogNotify == ToontownGlobals.NewItems:
                self.setSystemMessage(Localizer.Clarabelle, Localizer.NewCatalogNotify)
            
        
        self.catalogNotify = catalogNotify
        self.mailboxNotify = mailboxNotify

    
    def setDeliverySchedule(self, onOrder):
        self.onOrder = CatalogItemList.CatalogItemList(onOrder, store = CatalogItem.Customization | CatalogItem.DeliveryDate)
        if self == toonbase.localToon:
            nextTime = self.onOrder.getNextDeliveryDate()
            if nextTime != None:
                serverTime = time.time() + self.cr.getServerDelta()
                duration = nextTime * 60 - serverTime
                self.notify.info('next delivery in %s.' % PythonUtil.formatElapsedSeconds(duration))
            
        

    
    def setMailboxContents(self, mailboxContents):
        self.mailboxContents = CatalogItemList.CatalogItemList(mailboxContents, store = CatalogItem.Customization)

    
    def playSplashEffect(self, x, y, z):
        import Splash
        if self.splash == None:
            self.splash = Splash.Splash(render)
        
        self.splash.setPos(x, y, z)
        self.splash.setScale(2)
        self.splash.play()
        place = toonbase.tcr.playGame.getPlace()
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
        self.notify.debug('setting track %s progress to %s' % (trackId, progress))
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
        self.notify.debug('setting quest history to %s' % questList)
        self.questHistory = questList

    
    def getQuestHistory(self):
        return self.questHistory

    
    def setRewardHistory(self, rewardTier, rewardList):
        self.notify.debug('setting reward history to %s' % rewardList)
        self.rewardTier = rewardTier
        self.rewardHistory = rewardList

    
    def getRewardHistory(self):
        return (self.rewardTier, self.rewardHistory)

    
    def smoothPosition(self):
        DistributedSmoothNode.DistributedSmoothNode.smoothPosition(self)
        self.setSpeed(self.smoother.getSmoothForwardVelocity(), self.smoother.getSmoothRotationalVelocity())

    
    def d_setParent(self, parentToken):
        DistributedSmoothNode.DistributedSmoothNode.d_setParent(self, parentToken)

    
    def setEmoteAccess(self, bits):
        self.notify.debug('setting Emote access to %s' % bits)
        self.emoteAccess = bits
        if self == toonbase.localToon:
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


