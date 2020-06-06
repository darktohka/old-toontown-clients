# File: R (Python 2.2)

from ShowBaseGlobal import *
from DirectGui import *
from IntervalGlobal import *
import ToontownBattleGlobals
import BattleBase
import DirectNotifyGlobal
import whrandom
import string
import Quests
import copy
import AvatarDNA
import ToontownGlobals
import Localizer
import NPCToons
import math

class RewardPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('RewardPanel')
    
    def __init__(self, name):
        DirectFrame.__init__(self, relief = None, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (1.5, 1, 0.75), pos = (0, 0, 0.58699999999999997))
        self.initialiseoptions(RewardPanel)
        self.avNameLabel = DirectLabel(parent = self, relief = None, pos = (0, 0, 0.29999999999999999), text = name, text_scale = 0.080000000000000002)
        self.gagExpFrame = DirectFrame(parent = self, relief = None, pos = (-0.32000000000000001, 0, 0.23999999999999999))
        self.itemFrame = DirectFrame(parent = self, relief = None, text = Localizer.RewardPanelItems, text_pos = (0, 0.20000000000000001), text_scale = 0.080000000000000002)
        self.missedItemFrame = DirectFrame(parent = self, relief = None, text = Localizer.RewardPanelMissedItems, text_pos = (0, 0.20000000000000001), text_scale = 0.080000000000000002)
        self.itemLabel = DirectLabel(parent = self.itemFrame, text = '', text_scale = 0.059999999999999998)
        self.missedItemLabel = DirectLabel(parent = self.missedItemFrame, text = '', text_scale = 0.059999999999999998)
        self.questFrame = DirectFrame(parent = self, relief = None, text = Localizer.RewardPanelToonTasks, text_pos = (0, 0.20000000000000001), text_scale = 0.080000000000000002)
        self.questLabelList = []
        for i in range(ToontownGlobals.MaxQuestCarryLimit):
            label = DirectLabel(parent = self.questFrame, relief = None, pos = (-0.69999999999999996, 0, -0.10000000000000001 * i), text = Localizer.RewardPanelQuestLabel % i, text_scale = 0.059999999999999998, text_align = TextNode.ALeft)
            label.hide()
            self.questLabelList.append(label)
        
        self.newGagFrame = DirectFrame(parent = self, relief = None, pos = (-0.32000000000000001, 0, 0.23999999999999999), text = '', text_wordwrap = 14.4, text_pos = (0, -0.46000000000000002), text_scale = 0.059999999999999998)
        self.congratsLeft = DirectLabel(parent = self.newGagFrame, pos = (-0.20000000000000001, 0, -0.10000000000000001), text = '', text_pos = (0, 0), text_scale = 0.059999999999999998)
        self.congratsLeft.setHpr(0, 0, 30)
        self.congratsRight = DirectLabel(parent = self.newGagFrame, pos = (0.20000000000000001, 0, -0.10000000000000001), text = '', text_pos = (0, 0), text_scale = 0.059999999999999998)
        self.congratsRight.setHpr(0, 0, -30)
        self.trackLabels = []
        self.trackIncLabels = []
        self.trackBars = []
        for i in range(len(ToontownBattleGlobals.Tracks)):
            trackName = ToontownBattleGlobals.Tracks[i].upper()
            self.trackLabels.append(DirectLabel(parent = self.gagExpFrame, relief = None, text = trackName, text_scale = 0.050000000000000003, text_align = TextNode.ARight, pos = (-0.10000000000000001, 0, -0.089999999999999997 * i), text_pos = (0, -0.02)))
            self.trackIncLabels.append(DirectLabel(parent = self.gagExpFrame, relief = None, text = '', text_scale = 0.050000000000000003, text_align = TextNode.ALeft, pos = (0.41999999999999998, 0, -0.089999999999999997 * i), text_pos = (0, -0.02)))
            self.trackBars.append(DirectWaitBar(parent = self.gagExpFrame, relief = SUNKEN, frameSize = (-1, 1, -0.14999999999999999, 0.14999999999999999), borderWidth = (0.02, 0.02), scale = 0.25, frameColor = (ToontownBattleGlobals.TrackColors[i][0] * 0.5, ToontownBattleGlobals.TrackColors[i][1] * 0.5, ToontownBattleGlobals.TrackColors[i][2] * 0.5, 1), barColor = (ToontownBattleGlobals.TrackColors[i][0] * 0.80000000000000004, ToontownBattleGlobals.TrackColors[i][1] * 0.80000000000000004, ToontownBattleGlobals.TrackColors[i][2] * 0.80000000000000004, 1), text = '0/0', text_scale = 0.17999999999999999, text_fg = (0, 0, 0, 1), text_align = TextNode.ACenter, text_pos = (0, -0.050000000000000003), pos = (0.16, 0, -0.089999999999999997 * i)))
        
        return None

    
    def getNextExpValue(self, curSkill, trackIndex):
        retVal = ToontownBattleGlobals.MaxSkill
        for amount in ToontownBattleGlobals.Levels[trackIndex]:
            if curSkill < amount:
                retVal = amount
                return retVal
            
        
        return retVal

    
    def initItemFrame(self, toon):
        self.gagExpFrame.hide()
        self.newGagFrame.hide()
        self.questFrame.hide()
        self.itemFrame.show()
        self.missedItemFrame.hide()

    
    def initMissedItemFrame(self, toon):
        self.gagExpFrame.hide()
        self.newGagFrame.hide()
        self.questFrame.hide()
        self.itemFrame.hide()
        self.missedItemFrame.show()

    
    def initQuestFrame(self, toon, avQuests):
        self.gagExpFrame.hide()
        self.newGagFrame.hide()
        self.questFrame.show()
        self.itemFrame.hide()
        self.missedItemFrame.hide()
        for i in range(ToontownGlobals.MaxQuestCarryLimit):
            questLabel = self.questLabelList[i]
            questLabel.hide()
        
        for i in range(len(avQuests)):
            questDesc = avQuests[i]
            (questId, npcId, toNpcId, rewardId, toonProgress) = questDesc
            quest = Quests.getQuest(questId)
            questString = quest.getString()
            progressString = quest.getProgressString(toon, questDesc)
            rewardString = quest.getRewardString(progressString)
            rewardString = Quests.fillInQuestNames(rewardString, toNpcId = toNpcId)
            completed = quest.getCompletionStatus(toon, questDesc) == Quests.COMPLETE
            questLabel = self.questLabelList[i]
            questLabel.show()
            questLabel['text'] = rewardString
            if completed:
                questLabel['text_fg'] = (0, 0.29999999999999999, 0, 1)
            
        

    
    def initGagFrame(self, toon, expList):
        self.avNameLabel['text'] = toon.getName()
        self.gagExpFrame.show()
        self.newGagFrame.hide()
        self.questFrame.hide()
        self.itemFrame.hide()
        self.missedItemFrame.hide()
        for i in range(len(expList)):
            curExp = expList[i]
            trackBar = self.trackBars[i]
            trackIncLabel = self.trackIncLabels[i]
            trackIncLabel.hide()
            if toon.hasTrackAccess(i):
                trackBar.show()
                nextExp = self.getNextExpValue(curExp, i)
                trackBar['range'] = nextExp
                trackBar['value'] = curExp
                trackBar['text'] = '%s/%s' % (curExp, nextExp)
                trackBar['barColor'] = (ToontownBattleGlobals.TrackColors[i][0] * 0.80000000000000004, ToontownBattleGlobals.TrackColors[i][1] * 0.80000000000000004, ToontownBattleGlobals.TrackColors[i][2] * 0.80000000000000004, 1)
            else:
                trackBar.hide()
        
        return None

    
    def incrementExp(self, track, newValue):
        trackBar = self.trackBars[track]
        oldValue = trackBar['value']
        newValue = min(ToontownBattleGlobals.MaxSkill, newValue)
        nextExp = self.getNextExpValue(newValue, track)
        trackBar['range'] = nextExp
        trackBar['value'] = newValue
        trackBar['text'] = '%s/%s' % (newValue, nextExp)
        trackBar['barColor'] = (ToontownBattleGlobals.TrackColors[track][0], ToontownBattleGlobals.TrackColors[track][1], ToontownBattleGlobals.TrackColors[track][2], 1)
        return None

    
    def resetBarColor(self, track):
        self.trackBars[track]['barColor'] = (ToontownBattleGlobals.TrackColors[track][0] * 0.80000000000000004, ToontownBattleGlobals.TrackColors[track][1] * 0.80000000000000004, ToontownBattleGlobals.TrackColors[track][2] * 0.80000000000000004, 1)

    
    def getRandomCongratsPair(self, toon):
        congratsStrings = Localizer.RewardPanelCongratsStrings
        numStrings = len(congratsStrings)
        indexList = range(numStrings)
        index1 = whrandom.choice(indexList)
        indexList.remove(index1)
        index2 = whrandom.choice(indexList)
        string1 = congratsStrings[index1]
        string2 = congratsStrings[index2]
        return (string1, string2)

    
    def newGag(self, toon, track, level):
        self.gagExpFrame.hide()
        self.newGagFrame.show()
        self.questFrame.hide()
        self.itemFrame.hide()
        self.missedItemFrame.hide()
        self.newGagFrame['text'] = Localizer.RewardPanelNewGag % {
            'gagName': ToontownBattleGlobals.Tracks[track].capitalize(),
            'avName': toon.getName() }
        self.congratsLeft['text'] = ''
        self.congratsRight['text'] = ''
        gagOriginal = toonbase.localToon.inventory.buttonLookup(track, level)
        self.newGagIcon = gagOriginal.copyTo(self.newGagFrame)
        self.newGagIcon.setPos(0, 0, -0.25)
        self.newGagIcon.setScale(1.5)
        return None

    
    def cleanupNewGag(self):
        self.newGagIcon.removeNode()
        self.newGagIcon = None
        self.gagExpFrame.show()
        self.newGagFrame.hide()
        self.questFrame.hide()
        self.itemFrame.hide()
        self.missedItemFrame.hide()

    
    def getNewGagIntervalList(self, toon, track, level):
        leftCongratsAnticipate = 1.0
        rightCongratsAnticipate = 1.0
        finalDelay = 1.5
        (leftString, rightString) = self.getRandomCongratsPair(toon)
        intervalList = [
            Func(self.newGag, toon, track, level),
            Wait(leftCongratsAnticipate),
            Func(self.congratsLeft.setProp, 'text', leftString),
            Wait(rightCongratsAnticipate),
            Func(self.congratsRight.setProp, 'text', rightString),
            Wait(finalDelay),
            Func(self.cleanupNewGag)]
        return intervalList

    
    def showIncLabel(self, track, earnedSkill):
        total = 0
        self.trackIncLabels[track]['text'] = '+ ' + str(earnedSkill)
        self.trackIncLabels[track].show()

    
    def getTrackIntervalList(self, toon, track, origSkill, earnedSkill):
        tickDelay = 0.16
        intervalList = []
        intervalList.append(Func(self.showIncLabel, track, earnedSkill))
        barTime = math.log(earnedSkill + 1)
        numTicks = int(math.ceil(barTime / tickDelay))
        for i in range(numTicks):
            t = (i + 1) / float(numTicks)
            newValue = int(origSkill + t * earnedSkill + 0.5)
            intervalList.append(Func(self.incrementExp, track, newValue))
            intervalList.append(Wait(tickDelay))
        
        intervalList.append(Func(self.resetBarColor, track))
        intervalList.append(Wait(0.40000000000000002))
        nextExpValue = self.getNextExpValue(origSkill, track)
        finalGagFlag = 0
        while origSkill + earnedSkill >= nextExpValue and origSkill < nextExpValue and not finalGagFlag:
            if nextExpValue != ToontownBattleGlobals.MaxSkill:
                intervalList += self.getNewGagIntervalList(toon, track, ToontownBattleGlobals.Levels[track].index(nextExpValue))
            
            newNextExpValue = self.getNextExpValue(nextExpValue, track)
            if newNextExpValue == nextExpValue:
                finalGagFlag = 1
            else:
                nextExpValue = newNextExpValue
        return intervalList

    
    def getItemIntervalList(self, toon, itemList):
        intervalList = []
        for itemId in itemList:
            itemName = Quests.getItemName(itemId)
            intervalList.append(Func(self.itemLabel.setProp, 'text', itemName))
            intervalList.append(Wait(1))
        
        return intervalList

    
    def getMissedItemIntervalList(self, toon, missedItemList):
        intervalList = []
        for itemId in missedItemList:
            itemName = Quests.getItemName(itemId)
            intervalList.append(Func(self.missedItemLabel.setProp, 'text', itemName))
            intervalList.append(Wait(1))
        
        return intervalList

    
    def getQuestIntervalList(self, toon, deathList, toonList = []):
        avQuests = copy.deepcopy(toon.quests)
        avId = toon.getDoId()
        changed = 0
        tickDelay = 0.5
        intervalList = []
        cogList = []
        for i in range(0, len(deathList), 2):
            cogIndex = deathList[i]
            cogLevel = deathList[i + 1]
            cogType = AvatarDNA.suitHeadTypes[cogIndex]
            cogTrack = AvatarDNA.getSuitDept(cogType)
            cogList.append({
                'type': cogType,
                'level': cogLevel,
                'track': cogTrack,
                'activeToons': [
                    avId] })
        
        
        try:
            zoneId = toonbase.tcr.playGame.getPlace().getZoneId()
        except:
            zoneId = 0

        for i in range(len(avQuests)):
            questDesc = avQuests[i]
            (questId, npcId, toNpcId, rewardId, toonProgress) = questDesc
            quest = Quests.getQuest(questId)
            questString = quest.getString()
            progressString = quest.getProgressString(toon, questDesc)
            questLabel = self.questLabelList[i]
            for cogDict in cogList:
                if quest.doesCogCount(avId, cogDict, zoneId, toonList):
                    questDesc[4] += 1
                    changed = 1
                    progressString = quest.getProgressString(toon, questDesc)
                    str = '%s : %s' % (questString, progressString)
                    if quest.getCompletionStatus(toon, questDesc) == Quests.COMPLETE:
                        intervalList.append(Func(questLabel.setProp, 'text_fg', (0, 0.29999999999999999, 0, 1)))
                    
                    intervalList.append(Func(questLabel.setProp, 'text', str))
                    intervalList.append(Wait(tickDelay))
                
            
        
        return intervalList

    
    def getExpTrack(self, toon, origExp, earnedExp, deathList, itemList, missedItemList, toonList):
        track = Sequence(Func(self.initGagFrame, toon, origExp), Wait(1.0))
        for trackIndex in range(len(earnedExp)):
            if earnedExp[trackIndex] > 0:
                track += self.getTrackIntervalList(toon, trackIndex, origExp[trackIndex], earnedExp[trackIndex])
            
        
        track.append(Wait(1.0))
        itemList = self.getItemIntervalList(toon, itemList)
        if itemList:
            track.append(Func(self.initItemFrame, toon))
            track.append(Wait(1.0))
            track += itemList
            track.append(Wait(1.0))
        
        missedItemList = self.getMissedItemIntervalList(toon, missedItemList)
        if missedItemList:
            track.append(Func(self.initMissedItemFrame, toon))
            track.append(Wait(1.0))
            track += missedItemList
            track.append(Wait(1.0))
        
        questList = self.getQuestIntervalList(toon, deathList, toonList)
        if questList:
            track.append(Func(self.initQuestFrame, toon, copy.deepcopy(toon.quests)))
            track.append(Wait(1.0))
            track += questList
            track.append(Wait(2.0))
        
        return track

    
    def testMovie(self):
        track = Sequence()
        track.append(Func(self.show))
        expTrack = self.getExpTrack(toonbase.localToon, [
            1999,
            0,
            20,
            30,
            10,
            0,
            60], [
            2,
            0,
            2,
            6,
            1,
            0,
            8], [
            3,
            1,
            2,
            2,
            30,
            2], [], [], [])
        track.append(expTrack)
        if len(track) > 0:
            track.append(Func(self.hide))
            track.append(Func(toonbase.localToon.loop, 'neutral'))
            track.append(Func(toonbase.localToon.startUpdateSmartCamera))
            track.play()
            toonbase.localToon.loop('victory')
            toonbase.localToon.stopUpdateSmartCamera()
            camera.setPosHpr(0, 8, toonbase.localToon.getHeight() * 0.66000000000000003, 179, 15, 0)
        else:
            self.notify.debug('no experience, no movie.')
        return None


