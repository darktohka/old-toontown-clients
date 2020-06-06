# File: Q (Python 2.2)

from PandaModules import *
import DirectNotifyGlobal
import Quests
import ToontownGlobals

class QuestRewardCounter:
    notify = directNotify.newCategory('QuestRewardCounter')
    
    def __init__(self):
        self.reset()

    
    def reset(self):
        self.maxHp = 15
        self.maxCarry = 20
        self.maxMoney = 40
        self.questCarryLimit = 1
        self.teleportAccess = []
        self.trackAccess = [
            0,
            0,
            0,
            0,
            1,
            1,
            0]
        self.trackProgressId = -1
        self.trackProgress = 0

    
    def addTeleportAccess(self, zoneId):
        if zoneId not in self.teleportAccess:
            self.teleportAccess.append(zoneId)
        

    
    def addTrackAccess(self, track):
        self.trackAccess[track] = 1

    
    def addTrackProgress(self, trackId, progressIndex):
        if self.trackProgressId != trackId:
            self.notify.warning('tried to update progress on a track toon is not training')
        
        self.trackProgress = self.trackProgress | 1 << progressIndex

    
    def getTrackProgress(self):
        return (self.trackProgressId, self.trackProgress)

    
    def clearTrackProgress(self):
        self.trackProgressId = -1
        self.trackProgress = 0

    
    def setFromAvatar(self, av):
        rewardIds = []
        for q in av.quests:
            (questId, fromNpcId, toNpcId, rewardId, toonProgress) = q
            if rewardId == Quests.NA:
                rewardId = Quests.getFinalRewardId(questId, fAll = 1)
            
            rewardIds.append(rewardId)
        
        self.notify.debug('Ignoring rewards: %s' % rewardIds)
        self.setRewardIndex(av.rewardTier, rewardIds, av.rewardHistory)

    
    def setRewardIndex(self, tier, rewardIds, rewardHistory):
        self.reset()
        for tierNum in range(tier):
            for rewardId in Quests.getRewardsInTier(tierNum):
                reward = Quests.getReward(rewardId)
                reward.countReward(self)
                self.notify.debug('Assigning reward %d' % rewardId)
            
        
        print 'rewardHistory: ', rewardHistory
        for rewardId in rewardHistory:
            if rewardId in Quests.getRewardsInTier(tier):
                if rewardIds.count(rewardId) != 0:
                    print 'before: ', rewardIds
                    rewardIds.remove(rewardId)
                    self.notify.debug('Ignoring reward %d' % rewardId)
                    print 'after: ', rewardIds
                else:
                    reward = Quests.getReward(rewardId)
                    reward.countReward(self)
                    self.notify.debug('Assigning reward %d' % rewardId)
            
        
        self.notify.debug('Remaining rewardIds %s' % rewardIds)
        self.maxHp = min(ToontownGlobals.MaxHpLimit, self.maxHp)

    
    def assignReward(self, rewardId, rewardIds):
        if rewardIds.count(rewardId) != 0:
            rewardIds.remove(rewardId)
            self.notify.debug('Ignoring reward %d' % rewardId)
        else:
            reward = Quests.getReward(rewardId)
            reward.countReward(self)
            self.notify.debug('Assigning reward %d' % rewardId)

    
    def fixAvatar(self, av):
        self.setFromAvatar(av)
        anyChanged = 0
        if self.maxHp != av.maxHp:
            self.notify.info('Changed avatar %d to have maxHp %d instead of %d' % (av.doId, self.maxHp, av.maxHp))
            av.b_setMaxHp(self.maxHp)
            anyChanged = 1
        
        if self.maxMoney != av.maxMoney:
            self.notify.info('Changed avatar %d to have maxMoney %d instead of %d' % (av.doId, self.maxMoney, av.maxMoney))
            av.b_setMaxMoney(self.maxMoney)
            anyChanged = 1
        
        if self.questCarryLimit != av.questCarryLimit:
            self.notify.info('Changed avatar %d to have questCarryLimit %d instead of %d' % (av.doId, self.questCarryLimit, av.questCarryLimit))
            av.b_setQuestCarryLimit(self.questCarryLimit)
            anyChanged = 1
        
        if self.teleportAccess != av.teleportZoneArray:
            self.notify.info('Changed avatar %d to have teleportAccess %s instead of %s' % (av.doId, self.teleportAccess, av.teleportZoneArray))
            av.b_setTeleportAccess(self.teleportAccess)
            anyChanged = 1
        
        return anyChanged


