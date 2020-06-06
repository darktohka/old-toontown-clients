# File: R (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from toontown.toonbase import ToontownBattleGlobals
import BattleBase
from direct.directnotify import DirectNotifyGlobal
import whrandom
import string
from toontown.quest import Quests
import copy
from toontown.suit import SuitDNA
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.toon import NPCToons
import math
from toontown.coghq import CogDisguiseGlobals
from toontown.shtiker import DisguisePage

class RewardPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('RewardPanel')
    
    def __init__(self, name):
        DirectFrame.__init__(self, relief = None, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (1.75, 1, 0.75), pos = (0, 0, 0.58699999999999997))
        self.initialiseoptions(RewardPanel)
        self.avNameLabel = DirectLabel(parent = self, relief = None, pos = (0, 0, 0.29999999999999999), text = name, text_scale = 0.080000000000000002)
        self.gagExpFrame = DirectFrame(parent = self, relief = None, pos = (-0.32000000000000001, 0, 0.23999999999999999))
        self.itemFrame = DirectFrame(parent = self, relief = None, text = TTLocalizer.RewardPanelItems, text_pos = (0, 0.20000000000000001), text_scale = 0.080000000000000002)
        self.cogPartFrame = DirectFrame(parent = self, relief = None, text = TTLocalizer.RewardPanelCogPart, text_pos = (0, 0.20000000000000001), text_scale = 0.080000000000000002)
        self.missedItemFrame = DirectFrame(parent = self, relief = None, text = TTLocalizer.RewardPanelMissedItems, text_pos = (0, 0.20000000000000001), text_scale = 0.080000000000000002)
        self.itemLabel = DirectLabel(parent = self.itemFrame, text = '', text_scale = 0.059999999999999998)
        self.cogPartLabel = DirectLabel(parent = self.cogPartFrame, text = '', text_scale = 0.059999999999999998)
        self.missedItemLabel = DirectLabel(parent = self.missedItemFrame, text = '', text_scale = 0.059999999999999998)
        self.questFrame = DirectFrame(parent = self, relief = None, text = TTLocalizer.RewardPanelToonTasks, text_pos = (0, 0.20000000000000001), text_scale = 0.059999999999999998)
        self.questLabelList = []
        for i in range(ToontownGlobals.MaxQuestCarryLimit):
            label = DirectLabel(parent = self.questFrame, relief = None, pos = (-0.84999999999999998, 0, -0.10000000000000001 * i), text = TTLocalizer.RewardPanelQuestLabel % i, text_scale = 0.050000000000000003, text_align = TextNode.ALeft)
            label.hide()
            self.questLabelList.append(label)
        
        self.newGagFrame = DirectFrame(parent = self, relief = None, pos = (0, 0, 0.23999999999999999), text = '', text_wordwrap = 14.4, text_pos = (0, -0.46000000000000002), text_scale = 0.059999999999999998)
        self.congratsLeft = DirectLabel(parent = self.newGagFrame, pos = (-0.20000000000000001, 0, -0.10000000000000001), text = '', text_pos = (0, 0), text_scale = 0.059999999999999998)
        self.congratsLeft.setHpr(0, 0, -30)
        self.congratsRight = DirectLabel(parent = self.newGagFrame, pos = (0.20000000000000001, 0, -0.10000000000000001), text = '', text_pos = (0, 0), text_scale = 0.059999999999999998)
        self.congratsRight.setHpr(0, 0, 30)
        self.promotionFrame = DirectFrame(parent = self, relief = None, pos = (0, 0, 0.23999999999999999), text = '', text_wordwrap = 14.4, text_pos = (0, -0.46000000000000002), text_scale = 0.059999999999999998)
        self.trackLabels = []
        self.trackIncLabels = []
        self.trackBars = []
        self.trackBarsOffset = 0
        self.meritLabels = []
        self.meritIncLabels = []
        self.meritBars = []
        for i in range(len(SuitDNA.suitDepts)):
            deptName = TextEncoder.upper(SuitDNA.suitDeptFullnames[SuitDNA.suitDepts[i]])
            self.meritLabels.append(DirectLabel(parent = self.gagExpFrame, relief = None, text = deptName, text_scale = 0.050000000000000003, text_align = TextNode.ARight, pos = (0.55000000000000004, 0, -0.089999999999999997 * i - 0.125), text_pos = (0, -0.02)))
            self.meritIncLabels.append(DirectLabel(parent = self.gagExpFrame, relief = None, text = '', text_scale = 0.050000000000000003, text_align = TextNode.ALeft, pos = (0.69999999999999996, 0, -0.089999999999999997 * i - 0.125), text_pos = (0, -0.02)))
            self.meritBars.append(DirectWaitBar(parent = self.gagExpFrame, relief = SUNKEN, frameSize = (-1, 1, -0.14999999999999999, 0.14999999999999999), borderWidth = (0.02, 0.02), scale = 0.25, frameColor = (DisguisePage.DeptColors[i][0] * 0.69999999999999996, DisguisePage.DeptColors[i][1] * 0.69999999999999996, DisguisePage.DeptColors[i][2] * 0.69999999999999996, 1), barColor = (DisguisePage.DeptColors[i][0], DisguisePage.DeptColors[i][1], DisguisePage.DeptColors[i][2], 1), text = '0/0 ' + TTLocalizer.RewardPanelMeritBarLabels[i], text_scale = 0.17999999999999999, text_fg = (0, 0, 0, 1), text_align = TextNode.ALeft, text_pos = (-0.84999999999999998, -0.050000000000000003), pos = (0.82499999999999996, 0, -0.089999999999999997 * i - 0.125)))
        
        for i in range(len(ToontownBattleGlobals.Tracks)):
            trackName = TextEncoder.upper(ToontownBattleGlobals.Tracks[i])
            self.trackLabels.append(DirectLabel(parent = self.gagExpFrame, relief = None, text = trackName, text_scale = 0.050000000000000003, text_align = TextNode.ARight, pos = (0.13, 0, -0.089999999999999997 * i), text_pos = (0, -0.02)))
            self.trackIncLabels.append(DirectLabel(parent = self.gagExpFrame, relief = None, text = '', text_scale = 0.050000000000000003, text_align = TextNode.ALeft, pos = (0.65000000000000002, 0, -0.089999999999999997 * i), text_pos = (0, -0.02)))
            self.trackBars.append(DirectWaitBar(parent = self.gagExpFrame, relief = SUNKEN, frameSize = (-1, 1, -0.14999999999999999, 0.14999999999999999), borderWidth = (0.02, 0.02), scale = 0.25, frameColor = (ToontownBattleGlobals.TrackColors[i][0] * 0.69999999999999996, ToontownBattleGlobals.TrackColors[i][1] * 0.69999999999999996, ToontownBattleGlobals.TrackColors[i][2] * 0.69999999999999996, 1), barColor = (ToontownBattleGlobals.TrackColors[i][0], ToontownBattleGlobals.TrackColors[i][1], ToontownBattleGlobals.TrackColors[i][2], 1), text = '0/0', text_scale = 0.17999999999999999, text_fg = (0, 0, 0, 1), text_align = TextNode.ACenter, text_pos = (0, -0.050000000000000003), pos = (0.40000000000000002, 0, -0.089999999999999997 * i)))
        
        return None

    
    def getNextExpValue(self, curSkill, trackIndex):
        retVal = ToontownBattleGlobals.MaxSkill
        for amount in ToontownBattleGlobals.Levels[trackIndex]:
            if curSkill < amount:
                retVal = amount
                return retVal
            
        
        return retVal

    
    def getNextMeritValue(self, curMerits, toon, dept):
        totalMerits = CogDisguiseGlobals.getTotalMerits(toon, dept)
        retVal = totalMerits
        if curMerits > totalMerits:
            retVal = amount
        
        return retVal

    
    def initItemFrame(self, toon):
        self.gagExpFrame.hide()
        self.newGagFrame.hide()
        self.promotionFrame.hide()
        self.questFrame.hide()
        self.itemFrame.show()
        self.cogPartFrame.hide()
        self.missedItemFrame.hide()

    
    def initMissedItemFrame(self, toon):
        self.gagExpFrame.hide()
        self.newGagFrame.hide()
        self.promotionFrame.hide()
        self.questFrame.hide()
        self.itemFrame.hide()
        self.cogPartFrame.hide()
        self.missedItemFrame.show()

    
    def initCogPartFrame(self, toon):
        self.gagExpFrame.hide()
        self.newGagFrame.hide()
        self.promotionFrame.hide()
        self.questFrame.hide()
        self.itemFrame.hide()
        self.cogPartFrame.show()
        self.cogPartLabel['text'] = ''
        self.missedItemFrame.hide()

    
    def initQuestFrame(self, toon, avQuests):
        self.gagExpFrame.hide()
        self.newGagFrame.hide()
        self.promotionFrame.hide()
        self.questFrame.show()
        self.itemFrame.hide()
        self.cogPartFrame.hide()
        self.missedItemFrame.hide()
        for i in range(ToontownGlobals.MaxQuestCarryLimit):
            questLabel = self.questLabelList[i]
            questLabel['text_fg'] = (0, 0, 0, 1)
            questLabel.hide()
        
        for i in range(len(avQuests)):
            questDesc = avQuests[i]
            (questId, npcId, toNpcId, rewardId, toonProgress) = questDesc
            quest = Quests.getQuest(questId)
            if quest:
                questString = quest.getString()
                progressString = quest.getProgressString(toon, questDesc)
                rewardString = quest.getRewardString(progressString)
                rewardString = Quests.fillInQuestNames(rewardString, toNpcId = toNpcId)
                completed = quest.getCompletionStatus(toon, questDesc) == Quests.COMPLETE
                questLabel = self.questLabelList[i]
                questLabel.show()
                if base.localAvatar.tutorialAck:
                    questLabel['text'] = rewardString
                    if completed:
                        questLabel['text_fg'] = (0, 0.29999999999999999, 0, 1)
                    
                else:
                    questLabel['text'] = questString + ' :'
            
        

    
    def initGagFrame(self, toon, expList, meritList):
        self.avNameLabel['text'] = toon.getName()
        self.gagExpFrame.show()
        self.newGagFrame.hide()
        self.promotionFrame.hide()
        self.questFrame.hide()
        self.itemFrame.hide()
        self.cogPartFrame.hide()
        self.missedItemFrame.hide()
        trackBarOffset = 0
        for i in range(len(SuitDNA.suitDepts)):
            meritBar = self.meritBars[i]
            meritLabel = self.meritLabels[i]
            totalMerits = CogDisguiseGlobals.getTotalMerits(toon, i)
            merits = meritList[i]
            self.meritIncLabels[i].hide()
            if CogDisguiseGlobals.isSuitComplete(toon.cogParts, i):
                if not (self.trackBarsOffset):
                    trackBarOffset = 0.46999999999999997
                    self.trackBarsOffset = 1
                
                meritBar.show()
                meritLabel.show()
                meritLabel.show()
                if totalMerits:
                    meritBar['range'] = totalMerits
                    meritBar['value'] = merits
                    if merits == totalMerits:
                        meritBar['text'] = TTLocalizer.RewardPanelMeritAlert
                    else:
                        meritBar['text'] = '%s/%s %s' % (merits, totalMerits, TTLocalizer.RewardPanelMeritBarLabels[i])
                else:
                    meritBar['range'] = 1
                    meritBar['value'] = 1
                    meritBar['text'] = TTLocalizer.RewardPanelMeritsMaxed
                self.resetMeritBarColor(i)
            else:
                meritBar.hide()
                meritLabel.hide()
        
        for i in range(len(expList)):
            curExp = expList[i]
            trackBar = self.trackBars[i]
            trackLabel = self.trackLabels[i]
            trackIncLabel = self.trackIncLabels[i]
            trackBar.setX(trackBar.getX() - trackBarOffset)
            trackLabel.setX(trackLabel.getX() - trackBarOffset)
            trackIncLabel.setX(trackIncLabel.getX() - trackBarOffset)
            trackIncLabel.hide()
            if toon.hasTrackAccess(i):
                trackBar.show()
                nextExp = self.getNextExpValue(curExp, i)
                trackBar['range'] = nextExp
                trackBar['value'] = curExp
                trackBar['text'] = '%s/%s' % (curExp, nextExp)
                self.resetBarColor(i)
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

    
    def incrementMerits(self, toon, dept, newValue, totalMerits):
        meritBar = self.meritBars[dept]
        oldValue = meritBar['value']
        if totalMerits:
            newValue = min(totalMerits, newValue)
            meritBar['range'] = totalMerits
            meritBar['value'] = newValue
            if newValue == totalMerits:
                meritBar['text'] = TTLocalizer.RewardPanelMeritAlert
                meritBar['barColor'] = (DisguisePage.DeptColors[dept][0], DisguisePage.DeptColors[dept][1], DisguisePage.DeptColors[dept][2], 1)
            else:
                meritBar['text'] = '%s/%s %s' % (newValue, totalMerits, TTLocalizer.RewardPanelMeritBarLabels[dept])
        
        return None

    
    def resetMeritBarColor(self, dept):
        self.meritBars[dept]['barColor'] = (DisguisePage.DeptColors[dept][0] * 0.80000000000000004, DisguisePage.DeptColors[dept][1] * 0.80000000000000004, DisguisePage.DeptColors[dept][2] * 0.80000000000000004, 1)

    
    def getRandomCongratsPair(self, toon):
        congratsStrings = TTLocalizer.RewardPanelCongratsStrings
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
        self.promotionFrame.hide()
        self.questFrame.hide()
        self.itemFrame.hide()
        self.missedItemFrame.hide()
        self.newGagFrame['text'] = TTLocalizer.RewardPanelNewGag % {
            'gagName': ToontownBattleGlobals.Tracks[track].capitalize(),
            'avName': toon.getName() }
        self.congratsLeft['text'] = ''
        self.congratsRight['text'] = ''
        gagOriginal = base.localAvatar.inventory.buttonLookup(track, level)
        self.newGagIcon = gagOriginal.copyTo(self.newGagFrame)
        self.newGagIcon.setPos(0, 0, -0.25)
        self.newGagIcon.setScale(1.5)
        return None

    
    def cleanupNewGag(self):
        self.newGagIcon.removeNode()
        self.newGagIcon = None
        self.gagExpFrame.show()
        self.newGagFrame.hide()
        self.promotionFrame.hide()
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

    
    def showTrackIncLabel(self, track, earnedSkill):
        self.trackIncLabels[track]['text'] = '+ ' + str(earnedSkill)
        self.trackIncLabels[track].show()

    
    def showMeritIncLabel(self, dept, earnedMerits):
        self.meritIncLabels[dept]['text'] = '+ ' + str(earnedMerits)
        self.meritIncLabels[dept].show()

    
    def getTrackIntervalList(self, toon, track, origSkill, earnedSkill):
        tickDelay = 0.16
        intervalList = []
        intervalList.append(Func(self.showTrackIncLabel, track, earnedSkill))
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

    
    def getMeritIntervalList(self, toon, dept, origMerits, earnedMerits):
        tickDelay = 0.080000000000000002
        intervalList = []
        totalMerits = CogDisguiseGlobals.getTotalMerits(toon, dept)
        neededMerits = 0
        if totalMerits and origMerits != totalMerits:
            neededMerits = totalMerits - origMerits
            intervalList.append(Func(self.showMeritIncLabel, dept, min(neededMerits, earnedMerits)))
        
        barTime = math.log(earnedMerits + 1)
        numTicks = int(math.ceil(barTime / tickDelay))
        for i in range(numTicks):
            t = (i + 1) / float(numTicks)
            newValue = int(origMerits + t * earnedMerits + 0.5)
            intervalList.append(Func(self.incrementMerits, toon, dept, newValue, totalMerits))
            intervalList.append(Wait(tickDelay))
        
        intervalList.append(Func(self.resetMeritBarColor, dept))
        intervalList.append(Wait(0.40000000000000002))
        if toon.cogLevels[dept] < ToontownGlobals.MaxCogSuitLevel:
            if neededMerits and toon.readyForPromotion(dept):
                intervalList.append(Wait(0.40000000000000002))
                intervalList += self.getPromotionIntervalList(toon, dept)
            
        
        return intervalList

    
    def promotion(self, toon, dept):
        self.gagExpFrame.hide()
        self.newGagFrame.hide()
        self.promotionFrame.show()
        self.questFrame.hide()
        self.itemFrame.hide()
        self.missedItemFrame.hide()
        name = SuitDNA.suitDepts[dept]
        self.promotionFrame['text'] = 'Ready for promotion in %s track!' % SuitDNA.suitDeptFullnames[name]
        icons = loader.loadModelOnce('phase_3/models/gui/cog_icons')
        if dept == 0:
            self.deptIcon = icons.find('**/CorpIcon').copyTo(self.promotionFrame)
        elif dept == 1:
            self.deptIcon = icons.find('**/LegalIcon').copyTo(self.promotionFrame)
        elif dept == 2:
            self.deptIcon = icons.find('**/MoneyIcon').copyTo(self.promotionFrame)
        elif dept == 3:
            self.deptIcon = icons.find('**/SalesIcon').copyTo(self.promotionFrame)
        
        icons.removeNode()
        self.deptIcon.setPos(0, 0, -0.22500000000000001)
        self.deptIcon.setScale(0.33000000000000002)
        return None

    
    def cleanupPromotion(self):
        self.deptIcon.removeNode()
        self.deptIcon = None
        self.gagExpFrame.show()
        self.newGagFrame.hide()
        self.promotionFrame.hide()
        self.questFrame.hide()
        self.itemFrame.hide()
        self.missedItemFrame.hide()

    
    def getPromotionIntervalList(self, toon, dept):
        finalDelay = 2.0
        intervalList = [
            Func(self.promotion, toon, dept),
            Wait(finalDelay),
            Func(self.cleanupPromotion)]
        return intervalList

    
    def getQuestIntervalList(self, toon, deathList, toonList):
        avQuests = copy.deepcopy(toon.quests)
        avId = toon.getDoId()
        tickDelay = 0.20000000000000001
        intervalList = []
        toonShortList = []
        for t in toonList:
            if t is not None:
                toonShortList.append(t)
            
        
        cogList = []
        for i in range(0, len(deathList), 4):
            cogIndex = deathList[i]
            cogLevel = deathList[i + 1]
            activeToonBits = deathList[i + 2]
            flags = deathList[i + 3]
            activeToonIds = []
            for j in range(8):
                if activeToonBits & 1 << j:
                    if toonList[j] is not None:
                        activeToonIds.append(toonList[j].getDoId())
                    
                
            
            isSkelecog = flags & ToontownBattleGlobals.DLF_SKELECOG
            isForeman = flags & ToontownBattleGlobals.DLF_FOREMAN
            isVP = flags & ToontownBattleGlobals.DLF_VP
            isCFO = flags & ToontownBattleGlobals.DLF_CFO
            isSupervisor = flags & ToontownBattleGlobals.DLF_SUPERVISOR
            if isVP or isCFO:
                cogType = None
                cogTrack = SuitDNA.suitDepts[cogIndex]
            else:
                cogType = SuitDNA.suitHeadTypes[cogIndex]
                cogTrack = SuitDNA.getSuitDept(cogType)
            cogList.append({
                'type': cogType,
                'level': cogLevel,
                'track': cogTrack,
                'isSkelecog': isSkelecog,
                'isForeman': isForeman,
                'isVP': isVP,
                'isCFO': isCFO,
                'isSupervisor': isSupervisor,
                'activeToons': activeToonIds })
        
        
        try:
            zoneId = base.cr.playGame.getPlace().getTaskZoneId()
        except:
            zoneId = 0

        for i in range(len(avQuests)):
            questDesc = avQuests[i]
            (questId, npcId, toNpcId, rewardId, toonProgress) = questDesc
            quest = Quests.getQuest(questId)
            if quest:
                questString = quest.getString()
                progressString = quest.getProgressString(toon, questDesc)
                questLabel = self.questLabelList[i]
                origCogs = questDesc[4]
                earnedCogs = 0
                for cogDict in cogList:
                    if cogDict['isVP']:
                        num = quest.doesVPCount(avId, cogDict, zoneId, toonShortList)
                    elif cogDict['isCFO']:
                        num = quest.doesCFOCount(avId, cogDict, zoneId, toonShortList)
                    else:
                        num = quest.doesCogCount(avId, cogDict, zoneId, toonShortList)
                    if num:
                        earnedCogs += num
                    
                
                if earnedCogs > 0 and hasattr(quest, 'getNumCogs'):
                    earnedCogs = min(earnedCogs, quest.getNumCogs() - questDesc[4])
                
                if earnedCogs > 0:
                    barTime = math.log(earnedCogs + 1)
                    numTicks = int(math.ceil(barTime / tickDelay))
                    for i in range(numTicks):
                        t = (i + 1) / float(numTicks)
                        newValue = int(origCogs + t * earnedCogs + 0.5)
                        questDesc[4] = newValue
                        progressString = quest.getProgressString(toon, questDesc)
                        str = '%s : %s' % (questString, progressString)
                        if quest.getCompletionStatus(toon, questDesc) == Quests.COMPLETE:
                            intervalList.append(Func(questLabel.setProp, 'text_fg', (0, 0.29999999999999999, 0, 1)))
                        
                        intervalList.append(Func(questLabel.setProp, 'text', str))
                        intervalList.append(Wait(tickDelay))
                    
                
            
        
        return intervalList

    
    def getItemIntervalList(self, toon, itemList):
        intervalList = []
        for itemId in itemList:
            itemName = Quests.getItemName(itemId)
            intervalList.append(Func(self.itemLabel.setProp, 'text', itemName))
            intervalList.append(Wait(1))
        
        return intervalList

    
    def getCogPartIntervalList(self, toon, cogPartList):
        itemName = CogDisguiseGlobals.getPartName(cogPartList)
        intervalList = []
        intervalList.append(Func(self.cogPartLabel.setProp, 'text', itemName))
        intervalList.append(Wait(1))
        return intervalList

    
    def getMissedItemIntervalList(self, toon, missedItemList):
        intervalList = []
        for itemId in missedItemList:
            itemName = Quests.getItemName(itemId)
            intervalList.append(Func(self.missedItemLabel.setProp, 'text', itemName))
            intervalList.append(Wait(1))
        
        return intervalList

    
    def getExpTrack(self, toon, origExp, earnedExp, deathList, itemList, missedItemList, origMeritList, meritList, partList, toonList):
        track = Sequence(Func(self.initGagFrame, toon, origExp, origMeritList), Wait(1.0))
        for trackIndex in range(len(earnedExp)):
            if earnedExp[trackIndex] > 0:
                track += self.getTrackIntervalList(toon, trackIndex, origExp[trackIndex], earnedExp[trackIndex])
            
        
        for dept in range(len(SuitDNA.suitDepts)):
            if meritList[dept]:
                track += self.getMeritIntervalList(toon, dept, origMeritList[dept], meritList[dept])
            
        
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
        
        self.notify.debug('partList = %s' % partList)
        newPart = 0
        for part in partList:
            if part != 0:
                newPart = 1
                break
            
        
        if newPart:
            partList = self.getCogPartIntervalList(toon, partList)
            if partList:
                track.append(Func(self.initCogPartFrame, toon))
                track.append(Wait(1.0))
                track += partList
                track.append(Wait(1.0))
            
        
        questList = self.getQuestIntervalList(toon, deathList, toonList)
        if questList:
            track.append(Func(self.initQuestFrame, toon, copy.deepcopy(toon.quests)))
            track.append(Wait(1.0))
            track += questList
            track.append(Wait(2.0))
        
        return track

    
    def testMovie(self, otherToons = []):
        track = Sequence()
        track.append(Func(self.show))
        expTrack = self.getExpTrack(base.localAvatar, [
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
            3,
            0,
            2,
            2,
            1,
            1,
            30,
            2,
            1,
            0], [], [], [
            0,
            0,
            0,
            0], [
            0,
            0,
            0,
            0], [], [
            base.localAvatar] + otherToons)
        track.append(expTrack)
        if len(track) > 0:
            track.append(Func(self.hide))
            track.append(Func(base.localAvatar.loop, 'neutral'))
            track.append(Func(base.localAvatar.startUpdateSmartCamera))
            track.start()
            base.localAvatar.loop('victory')
            base.localAvatar.stopUpdateSmartCamera()
            camera.setPosHpr(0, 8, base.localAvatar.getHeight() * 0.66000000000000003, 179, 15, 0)
        else:
            self.notify.debug('no experience, no movie.')
        return None


