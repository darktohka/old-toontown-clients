# File: Q (Python 2.2)

import ToontownBattleGlobals
import ToontownGlobals
import SuitBattleGlobals
import random
import NPCToons
import copy
import string
import ZoneUtil
import DirectNotifyGlobal
import Localizer
import PythonUtil
import time
import types
notify = DirectNotifyGlobal.directNotify.newCategory('Quests')
notify.setDebug(1)
ItemDict = Localizer.QuestsItemDict
CompleteString = Localizer.QuestsCompleteString
NotChosenString = Localizer.QuestsNotChosenString
DefaultGreeting = Localizer.QuestsDefaultGreeting
DefaultIncomplete = Localizer.QuestsDefaultIncomplete
DefaultIncompleteProgress = Localizer.QuestsDefaultIncompleteProgress
DefaultIncompleteWrongNPC = Localizer.QuestsDefaultIncompleteWrongNPC
DefaultComplete = Localizer.QuestsDefaultComplete
DefaultLeaving = Localizer.QuestsDefaultLeaving
DefaultReject = Localizer.QuestsDefaultReject
DefaultTierNotDone = Localizer.QuestsDefaultTierNotDone
DefaultQuest = Localizer.QuestsDefaultQuest
DefaultVisitQuestDialog = Localizer.QuestsDefaultVisitQuestDialog
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
Any = 1
OBSOLETE = 'OBSOLETE'
Anywhere = 1
NA = 2
Same = 3
AnyFish = 4
ToonTailor = 999
ToonHQ = 1000
QuestDictTierIndex = 0
QuestDictStartIndex = 1
QuestDictDescIndex = 2
QuestDictFromNpcIndex = 3
QuestDictToNpcIndex = 4
QuestDictRewardIndex = 5
QuestDictNextQuestIndex = 6
QuestDictDialogIndex = 7
VeryEasy = 100
Easy = 75
Medium = 50
Hard = 25
VeryHard = 20
TT_TIER = 0
DD_TIER = 4
DG_TIER = 7
MM_TIER = 8
BR_TIER = 11
DL_TIER = 14
ELDER_TIER = 18
LOOPING_FINAL_TIER = ELDER_TIER
VISIT_QUEST_ID = 1000
QuestRandGen = random.Random()

def seedRandomGen(npcId, avId, tier, rewardHistory):
    QuestRandGen.seed(npcId * 100 + avId + tier + len(rewardHistory))


def seededRandomChoice(seq):
    return QuestRandGen.choice(seq)


def getCompleteStatusWithNpc(questComplete, toNpcId, npc):
    if questComplete:
        if npc:
            if npcMatches(toNpcId, npc):
                return COMPLETE
            else:
                return INCOMPLETE_WRONG_NPC
        else:
            return COMPLETE
    elif npc:
        if npcMatches(toNpcId, npc):
            return INCOMPLETE_PROGRESS
        else:
            return INCOMPLETE
    else:
        return INCOMPLETE


def npcMatches(toNpcId, npc):
    if not toNpcId == npc.getNpcId() and toNpcId == Any:
        if toNpcId == ToonHQ and npc.getHq() and toNpcId == ToonTailor:
            pass
    return npc.getTailor()


class Quest:
    _cogTracks = [
        Any,
        'c',
        'l',
        'm',
        's']
    
    def check(self, cond, msg):
        pass

    
    def checkLocation(self, location):
        locations = [
            Anywhere] + Localizer.GlobalStreetNames.keys()
        self.check(location in locations, 'invalid location: %s' % location)

    
    def checkNumCogs(self, num):
        self.check(1, 'invalid number of cogs: %s' % num)

    
    def checkNewbieLevel(self, level):
        self.check(1, 'invalid newbie level: %s' % level)

    
    def checkCogType(self, type):
        types = [
            Any] + SuitBattleGlobals.SuitAttributes.keys()
        self.check(type in types, 'invalid cog type: %s' % type)

    
    def checkCogTrack(self, track):
        self.check(track in self._cogTracks, 'invalid cog track: %s' % track)

    
    def checkCogLevel(self, level):
        self.check(1, 'invalid cog level: %s' % level)

    
    def checkNumBuildings(self, num):
        self.check(1, 'invalid num buildings: %s' % num)

    
    def checkBuildingTrack(self, track):
        self.check(track in self._cogTracks, 'invalid building track: %s' % track)

    
    def checkBuildingFloors(self, floors):
        if floors >= 1:
            pass
        self.check(floors <= 5, 'invalid num floors: %s' % floors)

    
    def checkNumGags(self, num):
        self.check(1, 'invalid num gags: %s' % num)

    
    def checkGagTrack(self, track):
        if track >= ToontownBattleGlobals.MIN_TRACK_INDEX:
            pass
        self.check(track <= ToontownBattleGlobals.MAX_TRACK_INDEX, 'invalid gag track: %s' % track)

    
    def checkGagItem(self, item):
        if item >= ToontownBattleGlobals.MIN_LEVEL_INDEX:
            pass
        self.check(item <= ToontownBattleGlobals.MAX_LEVEL_INDEX, 'invalid gag item: %s' % item)

    
    def checkDeliveryItem(self, item):
        self.check(item in ItemDict.keys(), 'invalid delivery item: %s' % item)

    
    def checkNumItems(self, num):
        self.check(1, 'invalid num items: %s' % num)

    
    def checkRecoveryItem(self, item):
        self.check(item in ItemDict.keys(), 'invalid recovery item: %s' % item)

    
    def checkPercentChance(self, chance):
        if chance > 0:
            pass
        self.check(chance <= 100, 'invalid percent chance: %s' % chance)

    
    def checkRecoveryItemHolderAndType(self, holder, holderType = 'type'):
        holderTypes = [
            'type',
            'level',
            'track']
        self.check(holderType in holderTypes, 'invalid recovery item holderType: %s' % holderType)
        if holderType == 'type':
            holders = [
                Any,
                AnyFish] + SuitBattleGlobals.SuitAttributes.keys()
            self.check(holder in holders, 'invalid recovery item holder: %s for holderType: %s' % (holder, holderType))
        elif holderType == 'level':
            pass
        elif holderType == 'track':
            self.check(holder in self._cogTracks, 'invalid recovery item holder: %s for holderType: %s' % (holder, holderType))
        

    
    def checkTrackChoice(self, option):
        if option >= ToontownBattleGlobals.MIN_TRACK_INDEX:
            pass
        self.check(option <= ToontownBattleGlobals.MAX_TRACK_INDEX, 'invalid track option: %s' % option)

    
    def checkNumFriends(self, num):
        self.check(1, 'invalid number of friends: %s' % num)

    
    def checkNumMinigames(self, num):
        self.check(1, 'invalid number of minigames: %s' % num)

    
    def filterFunc(avatar):
        return 1

    filterFunc = staticmethod(filterFunc)
    
    def __init__(self, id, quest):
        self.id = id
        self.quest = quest

    
    def getId(self):
        return self.id

    
    def getType(self):
        return self.__class__

    
    def getObjectiveStrings(self):
        return [
            '']

    
    def getString(self):
        return self.getObjectiveStrings()[0]

    
    def getRewardString(self, progressString):
        return self.getString() + ' : ' + progressString

    
    def getChooseString(self):
        return self.getString()

    
    def getPosterString(self):
        return self.getString()

    
    def getHeadlineString(self):
        return self.getString()

    
    def getDefaultQuestDialog(self):
        return self.getString() + '.'

    
    def getNumQuestItems(self):
        return -1

    
    def addArticle(self, num, oString):
        if len(oString) == 0:
            return oString
        
        if num == 1:
            return oString
        else:
            return '%d %s' % (num, oString)

    
    def __repr__(self):
        return 'Quest type: %s id: %s params: %s' % (self.__class__.__name__, self.id, self.quest[0:])

    
    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return 0

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        notify.error('Pure virtual - please overrride me')
        return None



class LocationBasedQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkLocation(self.quest[0])

    
    def getLocation(self):
        return self.quest[0]

    
    def getLocationName(self):
        loc = self.getLocation()
        if loc == Anywhere:
            locName = ''
        elif loc in ToontownGlobals.Hoods:
            locName = Localizer.QuestPosterLocationIn + ToontownGlobals.hoodNameMap[loc][1]
        elif loc in ToontownGlobals.StreetBranchZones:
            locName = Localizer.QuestPosterLocationOn + ToontownGlobals.StreetNames[loc][1]
        
        return locName

    
    def isLocationMatch(self, zoneId):
        loc = self.getLocation()
        if loc is Anywhere:
            return 1
        
        if ZoneUtil.isPlayground(loc):
            if loc == ZoneUtil.getHoodId(zoneId):
                return 1
            else:
                return 0
        elif loc == ZoneUtil.getBranchZone(zoneId):
            return 1
        elif loc == zoneId:
            return 1
        else:
            return 0

    
    def getChooseString(self):
        return self.getString() + self.getLocationName()

    
    def getPosterString(self):
        return self.getString() + self.getLocationName()

    
    def getDefaultQuestDialog(self):
        return self.getString() + self.getLocationName() + '.'



class CogQuest(LocationBasedQuest):
    
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        if self.__class__ == CogQuest:
            self.checkNumCogs(self.quest[1])
            self.checkCogType(self.quest[2])
        

    
    def getCogType(self):
        return self.quest[2]

    
    def getNumQuestItems(self):
        return self.getNumCogs()

    
    def getNumCogs(self):
        return self.quest[1]

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        questComplete = toonProgress >= self.getNumCogs()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return Localizer.QuestsCogQuestProgress % {
                'progress': questDesc[4],
                'numCogs': self.getNumCogs() }

    
    def getObjectiveStrings(self):
        numCogs = self.getNumCogs()
        cogType = self.getCogType()
        if numCogs == 1:
            if cogType == Any:
                text = Localizer.ACog
            else:
                text = SuitBattleGlobals.SuitAttributes[cogType]['singularname']
        elif cogType == Any:
            cogName = Localizer.Cogs
        else:
            cogName = SuitBattleGlobals.SuitAttributes[cogType]['pluralname']
        text = '%s %s' % (numCogs, cogName)
        return (text,)

    
    def getString(self):
        return Localizer.QuestsCogQuestDefeat % self.getObjectiveStrings()[0]

    
    def getQTStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskQTStrings(toNpcId)
        
        numCogs = self.getNumCogs()
        cogType = self.getCogType()
        if numCogs == 1:
            if cogType == Any:
                cogName = Localizer.ACog
            else:
                cogName = SuitBattleGlobals.SuitAttributes[cogType]['singularname']
            text = Localizer.QuestsCogQuestQTStringS
        elif cogType == Any:
            cogName = Localizer.Cogs
        else:
            cogName = SuitBattleGlobals.SuitAttributes[cogType]['pluralname']
        text = Localizer.QuestsCogQuestQTStringP
        cogLoc = self.getLocationName()
        return text % {
            'cogName': cogName,
            'cogLoc': cogLoc }

    
    def getHeadlineString(self):
        return Localizer.QuestsCogQuestHeadline

    
    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogType = self.getCogType()
        if (questCogType is Any or questCogType is cogDict['type']) and avId in cogDict['activeToons']:
            pass
        return self.isLocationMatch(zoneId)



class CogNewbieQuest(CogQuest):
    
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCogs(self.quest[1])
        self.checkCogType(self.quest[2])
        self.checkNewbieLevel(self.quest[3])

    
    def getNewbieLevel(self):
        return self.quest[3]

    
    def getString(self):
        return Localizer.QuestsCogNewbieQuestObjective % (self.getNewbieLevel(), self.getObjectiveStrings()[0])

    
    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogType = self.getCogType()
        newbieHp = self.getNewbieLevel()
        num = 0
        for av in avList:
            if av.getDoId() != avId and av.getMaxHp() <= newbieHp:
                num += 1
            
        
        if (questCogType is Any or questCogType is cogDict['type']) and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId):
            return num
        else:
            return 0



class CogTrackQuest(CogQuest):
    trackCodes = [
        'c',
        'l',
        'm',
        's']
    trackNamesS = [
        Localizer.BossbotS,
        Localizer.LawbotS,
        Localizer.CashbotS,
        Localizer.SellbotS]
    trackNamesP = [
        Localizer.BossbotP,
        Localizer.LawbotP,
        Localizer.CashbotP,
        Localizer.SellbotP]
    
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCogs(self.quest[1])
        self.checkCogTrack(self.quest[2])

    
    def getCogTrack(self):
        return self.quest[2]

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return Localizer.QuestsCogTrackQuestProgress % {
                'progress': questDesc[4],
                'numCogs': self.getNumCogs() }

    
    def getObjectiveStrings(self):
        numCogs = self.getNumCogs()
        track = self.trackCodes.index(self.getCogTrack())
        if numCogs == 1:
            text = self.trackNamesS[track]
        else:
            text = '%s %s' % (numCogs, self.trackNamesP[track])
        return (text,)

    
    def getString(self):
        return Localizer.QuestsCogTrackQuestDefeat % self.getObjectiveStrings()[0]

    
    def getQTStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskQTStrings(toNpcId)
        
        numCogs = self.getNumCogs()
        track = self.trackCodes.index(self.getCogTrack())
        if numCogs == 1:
            cogText = self.trackNamesS[track]
        else:
            cogText = self.trackNamesP[track]
        cogLocName = self.getLocationName()
        return Localizer.QuestsCogTrackQuestQTString % {
            'cogText': cogText,
            'cogLoc': cogLocName }

    
    def getHeadlineString(self):
        return Localizer.QuestsCogTrackQuestHeadline

    
    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogTrack = self.getCogTrack()
        if questCogTrack == cogDict['track'] and avId in cogDict['activeToons']:
            pass
        return self.isLocationMatch(zoneId)



class CogLevelQuest(CogQuest):
    
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCogs(self.quest[1])
        self.checkCogLevel(self.quest[2])

    
    def getCogLevel(self):
        return self.quest[2]

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return Localizer.QuestsCogLevelQuestProgress % {
                'progress': questDesc[4],
                'numCogs': self.getNumCogs() }

    
    def getObjectiveStrings(self):
        count = self.getNumCogs()
        level = self.getCogLevel()
        if count == 1:
            text = Localizer.QuestsCogLevelQuestDesc
        else:
            text = Localizer.QuestsCogLevelQuestDescC
        return (text % {
            'count': count,
            'level': level },)

    
    def getString(self):
        return Localizer.QuestsCogLevelQuestDefeat % self.getObjectiveStrings()[0]

    
    def getQTStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskQTStrings(toNpcId)
        
        count = self.getNumCogs()
        level = self.getCogLevel()
        if count == 1:
            text = Localizer.QuestsCogLevelQuestDesc
        else:
            text = Localizer.QuestsCogLevelQuestDescI
        objective = text % {
            'level': level }
        location = self.getLocationName()
        return Localizer.QuestsCogLevelQuestQTString % {
            'objective': objective,
            'location': location }

    
    def getHeadlineString(self):
        return Localizer.QuestsCogLevelQuestHeadline

    
    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogLevel = self.getCogLevel()
        if questCogLevel <= cogDict['level'] and avId in cogDict['activeToons']:
            pass
        return self.isLocationMatch(zoneId)



class BuildingQuest(CogQuest):
    trackCodes = [
        'c',
        'l',
        'm',
        's']
    trackNames = [
        Localizer.Bossbot,
        Localizer.Lawbot,
        Localizer.Cashbot,
        Localizer.Sellbot]
    
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumBuildings(self.quest[1])
        self.checkBuildingTrack(self.quest[2])
        self.checkBuildingFloors(self.quest[3])

    
    def getNumFloors(self):
        return self.quest[3]

    
    def getBuildingTrack(self):
        return self.quest[2]

    
    def getNumQuestItems(self):
        return self.getNumBuildings()

    
    def getNumBuildings(self):
        return self.quest[1]

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        questComplete = toonProgress >= self.getNumBuildings()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumBuildings() == 1:
            return ''
        else:
            return Localizer.QuestsBuildingQuestProgressString % {
                'progress': questDesc[4],
                'num': self.getNumBuildings() }

    
    def getObjectiveStrings(self):
        count = self.getNumBuildings()
        floors = Localizer.QuestsBuildingQuestFloorNumbers[self.getNumFloors() - 1]
        buildingTrack = self.getBuildingTrack()
        if buildingTrack == Any:
            type = Localizer.Cog
        else:
            type = self.trackNames[self.trackCodes.index(buildingTrack)]
        if count == 1:
            if floors == '':
                text = Localizer.QuestsBuildingQuestDesc
            else:
                text = Localizer.QuestsBuildingQuestDescF
        elif floors == '':
            text = Localizer.QuestsBuildingQuestDescC
        else:
            text = Localizer.QuestsBuildingQuestDescCF
        return (text % {
            'count': count,
            'floors': floors,
            'type': type },)

    
    def getString(self):
        return Localizer.QuestsBuildingQuestString % self.getObjectiveStrings()[0]

    
    def getQTStrings(self, toNpcId, progress):
        if progress >= self.getNumBuildings():
            return getFinishToonTaskQTStrings(toNpcId)
        
        count = self.getNumBuildings()
        floors = Localizer.QuestsBuildingQuestFloorNumbers[self.getNumFloors() - 1]
        buildingTrack = self.getBuildingTrack()
        if buildingTrack == Any:
            type = Localizer.Cog
        else:
            type = self.trackNames[self.trackCodes.index(buildingTrack)]
        if count == 1:
            if floors == '':
                text = Localizer.QuestsBuildingQuestDesc
            else:
                text = Localizer.QuestsBuildingQuestDescF
        elif floors == '':
            text = Localizer.QuestsBuildingQuestDescI
        else:
            text = Localizer.QuestsBuildingQuestDescIF
        objective = text % {
            'floors': floors,
            'type': type }
        location = self.getLocationName()
        return Localizer.QuestsBuildingQuestQTString % {
            'objective': objective,
            'location': location }

    
    def getHeadlineString(self):
        return Localizer.QuestsBuildingQuestHeadline

    
    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return 0

    
    def doesBuildingCount(self, avId, avList):
        return 1



class BuildingNewbieQuest(BuildingQuest):
    
    def __init__(self, id, quest):
        BuildingQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[4])

    
    def getNewbieLevel(self):
        return self.quest[4]

    
    def getString(self):
        return Localizer.QuestsCogNewbieQuestObjective % (self.getNewbieLevel(), self.getObjectiveStrings()[0])

    
    def getHeadlineString(self):
        return Localizer.QuestsNewbieQuestHeadline

    
    def doesBuildingCount(self, avId, avList):
        newbieHp = self.getNewbieLevel()
        num = 0
        for av in avList:
            if av.getDoId() != avId and av.getMaxHp() <= newbieHp:
                num += 1
            
        
        return num



class DeliverGagQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkNumGags(self.quest[0])
        self.checkGagTrack(self.quest[1])
        self.checkGagItem(self.quest[2])

    
    def getGagType(self):
        return (self.quest[1], self.quest[2])

    
    def getNumQuestItems(self):
        return self.getNumGags()

    
    def getNumGags(self):
        return self.quest[0]

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        gag = self.getGagType()
        num = self.getNumGags()
        track = gag[0]
        level = gag[1]
        if npc and av.inventory:
            pass
        questComplete = av.inventory.numItem(track, level) >= num
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumGags() == 1:
            return ''
        else:
            return Localizer.QuestsDeliverGagQuestProgress % {
                'progress': questDesc[4],
                'numGags': self.getNumGags() }

    
    def getObjectiveStrings(self):
        (track, item) = self.getGagType()
        num = self.getNumGags()
        if num == 1:
            text = ToontownBattleGlobals.AvPropStringsSingular[track][item]
        else:
            gagName = ToontownBattleGlobals.AvPropStringsPlural[track][item]
            text = '%d %s' % (num, gagName)
        return (text,)

    
    def getString(self):
        return Localizer.QuestsDeliverGagQuestString % self.getObjectiveStrings()[0]

    
    def getRewardString(self, progress):
        return Localizer.QuestsDeliverGagQuestStringLong % self.getObjectiveStrings()[0]

    
    def getDefaultQuestDialog(self):
        return Localizer.QuestsDeliverGagQuestStringLong % self.getObjectiveStrings()[0]

    
    def getQTStrings(self, toNpcId, progress):
        if progress >= self.getNumGags():
            return getFinishToonTaskQTStrings(toNpcId)
        
        (track, item) = self.getGagType()
        num = self.getNumGags()
        if num == 1:
            text = Localizer.QuestsDeliverGagQuestToQTStringS
            gagName = ToontownBattleGlobals.AvPropStringsSingular[track][item]
        else:
            text = Localizer.QuestsDeliverGagQuestToQTStringP
            gagName = ToontownBattleGlobals.AvPropStringsPlural[track][item]
        return [
            text % {
                'gagName': gagName },
            Localizer.QuestsDeliverGagQuestQTString] + getVisitQTStrings(toNpcId)

    
    def getHeadlineString(self):
        return Localizer.QuestsDeliverGagQuestHeadline



class DeliverItemQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkDeliveryItem(self.quest[0])

    
    def getItem(self):
        return self.quest[0]

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    
    def getProgressString(self, avatar, questDesc):
        return Localizer.QuestsDeliverItemQuestProgress

    
    def getObjectiveStrings(self):
        iDict = ItemDict[self.getItem()]
        article = iDict[2]
        itemName = iDict[0]
        return [
            article + itemName]

    
    def getString(self):
        return Localizer.QuestsDeliverItemQuestString % self.getObjectiveStrings()[0]

    
    def getRewardString(self, progress):
        return Localizer.QuestsDeliverItemQuestStringLong % self.getObjectiveStrings()[0]

    
    def getDefaultQuestDialog(self):
        return Localizer.QuestsDeliverItemQuestStringLong % self.getObjectiveStrings()[0]

    
    def getQTStrings(self, toNpcId, progress):
        iDict = ItemDict[self.getItem()]
        article = iDict[2]
        itemName = iDict[0]
        return [
            Localizer.QuestsDeliverItemQuestQTString % {
                'article': article,
                'itemName': itemName }] + getVisitQTStrings(toNpcId)

    
    def getHeadlineString(self):
        return Localizer.QuestsDeliverItemQuestHeadline



class VisitQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    
    def getProgressString(self, avatar, questDesc):
        return Localizer.QuestsVisitQuestProgress

    
    def getObjectiveStrings(self):
        return [
            '']

    
    def getString(self):
        return Localizer.QuestsVisitQuestStringShort

    
    def getChooseString(self):
        return Localizer.QuestsVisitQuestStringLong

    
    def getRewardString(self, progress):
        return Localizer.QuestsVisitQuestStringLong

    
    def getDefaultQuestDialog(self):
        return random.choice(DefaultVisitQuestDialog)

    
    def getQTStrings(self, toNpcId, progress):
        return getVisitQTStrings(toNpcId)

    
    def getHeadlineString(self):
        return Localizer.QuestsVisitQuestHeadline



class RecoverItemQuest(LocationBasedQuest):
    
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumItems(self.quest[1])
        self.checkRecoveryItem(self.quest[2])
        self.checkPercentChance(self.quest[3])
        if len(self.quest) > 5:
            self.checkRecoveryItemHolderAndType(self.quest[4], self.quest[5])
        else:
            self.checkRecoveryItemHolderAndType(self.quest[4])

    
    def getNumQuestItems(self):
        return self.getNumItems()

    
    def getNumItems(self):
        return self.quest[1]

    
    def getItem(self):
        return self.quest[2]

    
    def getPercentChance(self):
        return self.quest[3]

    
    def getHolder(self):
        return self.quest[4]

    
    def getHolderType(self):
        if len(self.quest) == 5:
            return 'type'
        else:
            return self.quest[5]

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        questComplete = toonProgress >= self.getNumItems()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumItems() == 1:
            return ''
        else:
            return Localizer.QuestsRecoverItemQuestProgress % {
                'progress': questDesc[4],
                'numItems': self.getNumItems() }

    
    def getObjectiveStrings(self):
        holder = self.getHolder()
        holderType = self.getHolderType()
        if holder == Any:
            holderName = Localizer.TheCogs
        elif holder == AnyFish:
            holderName = Localizer.AFish
        elif holderType == 'type':
            holderName = SuitBattleGlobals.SuitAttributes[holder]['pluralname']
        elif holderType == 'level':
            holderName = '%s %d+ %s' % (Localizer.Level, holder, Localizer.Cogs)
        elif holderType == 'track':
            if holder == 'c':
                holderName = Localizer.BossbotP
            elif holder == 's':
                holderName = Localizer.SellbotP
            elif holder == 'm':
                holderName = Localizer.CashbotP
            elif holder == 'l':
                holderName = Localizer.LawbotP
            
        
        item = self.getItem()
        num = self.getNumItems()
        if num == 1:
            itemName = ItemDict[item][2] + ItemDict[item][0]
        else:
            itemName = '%d ' % num + ItemDict[item][1]
        return [
            itemName,
            holderName]

    
    def getString(self):
        return Localizer.QuestsRecoverItemQuestString % {
            'item': self.getObjectiveStrings()[0],
            'holder': self.getObjectiveStrings()[1] }

    
    def getQTStrings(self, toNpcId, progress):
        item = self.getItem()
        num = self.getNumItems()
        if progress >= self.getNumItems():
            if num == 1:
                itemName = 'this ' + ItemDict[item][0]
            else:
                itemName = 'these ' + ItemDict[item][1]
            if toNpcId == ToonHQ:
                strings = [
                    Localizer.QuestsRecoverItemQuestReturnToHQQTString % itemName,
                    Localizer.QuestsRecoverItemQuestGoToHQQTString]
            elif toNpcId:
                (npcName, hoodName, buildingName, streetName) = getNpcInfo(toNpcId)
                strings = [
                    Localizer.QuestsRecoverItemQuestReturnToQTString % {
                        'item': itemName,
                        'npcName': npcName }]
                if streetName == 'Playground':
                    strings.append(Localizer.QuestsRecoverItemQuestGoToPlaygroundQTString % hoodName)
                else:
                    strings.append(Localizer.QuestsRecoverItemQuestGoToStreetQTString % {
                        'street': streetName,
                        'hood': hoodName })
                strings.extend([
                    Localizer.QuestsRecoverItemQuestVisitBuildingQTString % buildingName,
                    Localizer.QuestsRecoverItemQuestWhereIsBuildingQTString % buildingName])
            
            return strings
        
        holder = self.getHolder()
        holderType = self.getHolderType()
        locName = self.getLocationName()
        if holder == Any:
            holderName = Localizer.TheCogs
        elif holder == AnyFish:
            holderName = Localizer.TheFish
        elif holderType == 'type':
            holderName = SuitBattleGlobals.SuitAttributes[holder]['pluralname']
        elif holderType == 'level':
            holderName = '%s %d+ %s' % (Localizer.Level, holder, Localizer.Cogs)
        elif holderType == 'track':
            if holder == 'c':
                holderName = Localizer.BossbotP
            elif holder == 's':
                holderName = Localizer.SellbotP
            elif holder == 'm':
                holderName = Localizer.CashbotP
            elif holder == 'l':
                holderName = Localizer.LawbotP
            
        
        if num == 1:
            itemName = 'a ' + ItemDict[item][0]
        else:
            itemName = 'some ' + ItemDict[item][1]
        return Localizer.QuestsRecoverItemQuestRecoverFromQTString % {
            'item': itemName,
            'holder': holderName,
            'loc': locName }

    
    def getHeadlineString(self):
        return Localizer.QuestsRecoverItemQuestHeadline



class TrackChoiceQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkTrackChoice(self.quest[0])
        self.checkTrackChoice(self.quest[1])

    
    def getChoices(self):
        return (self.quest[0], self.quest[1])

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return NotChosenString

    
    def getObjectiveStrings(self):
        (trackA, trackB) = self.getChoices()
        trackAName = ToontownBattleGlobals.Tracks[trackA].capitalize()
        trackBName = ToontownBattleGlobals.Tracks[trackB].capitalize()
        return [
            trackAName,
            trackBName]

    
    def getString(self):
        return Localizer.QuestsTrackChoiceQuestString % {
            'trackA': self.getObjectiveStrings()[0],
            'trackB': self.getObjectiveStrings()[1] }

    
    def getQTStrings(self, toNpcId, progress):
        (trackA, trackB) = self.getChoices()
        trackAName = ToontownBattleGlobals.Tracks[trackA].capitalize()
        trackBName = ToontownBattleGlobals.Tracks[trackB].capitalize()
        return [
            Localizer.QuestsTrackChoiceQuestQTString % {
                'trackA': trackAName,
                'trackB': trackBName },
            Localizer.QuestsTrackChoiceQuestMaybeQTString % trackAName,
            Localizer.QuestsTrackChoiceQuestMaybeQTString % trackBName] + getVisitQTStrings(toNpcId)

    
    def getHeadlineString(self):
        return Localizer.QuestsTrackChoiceQuestHeadline



class FriendQuest(Quest):
    
    def filterFunc(avatar):
        if len(avatar.getFriendsList()) == 0:
            return 1
        else:
            return 0

    filterFunc = staticmethod(filterFunc)
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        if not toonProgress >= 1:
            pass
        questComplete = len(av.getFriendsList()) > 0
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ''

    
    def getString(self):
        return Localizer.QuestsFriendQuestString

    
    def getQTStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskQTStrings(toNpcId)
        
        return Localizer.QuestsFriendQuestQTString

    
    def getHeadlineString(self):
        return Localizer.QuestsFriendQuestHeadline

    
    def getObjectiveStrings(self):
        return [
            Localizer.QuestsFriendQuestString]

    
    def doesFriendCount(self, av, otherAv):
        return 1



class FriendNewbieQuest(FriendQuest):
    
    def filterFunc(avatar):
        return 1

    filterFunc = staticmethod(filterFunc)
    
    def __init__(self, id, quest):
        FriendQuest.__init__(self, id, quest)
        self.checkNumFriends(self.quest[0])
        self.checkNewbieLevel(self.quest[1])

    
    def getNumQuestItems(self):
        return self.getNumFriends()

    
    def getNumFriends(self):
        return self.quest[0]

    
    def getNewbieLevel(self):
        return self.quest[1]

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        questComplete = toonProgress >= self.getNumFriends()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumFriends() == 1:
            return ''
        else:
            return Localizer.QuestsFriendNewbieQuestProgress % {
                'progress': questDesc[4],
                'numFriends': self.getNumFriends() }

    
    def getString(self):
        return Localizer.QuestsFriendNewbieQuestObjective % (self.getNumFriends(), self.getNewbieLevel())

    
    def getObjectiveStrings(self):
        return [
            Localizer.QuestsFriendNewbieQuestString % (self.getNumFriends(), self.getNewbieLevel())]

    
    def doesFriendCount(self, av, otherAv):
        if otherAv != None and otherAv.getMaxHp() <= self.getNewbieLevel():
            return 1
        
        return 0



class TrolleyQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        questComplete = toonProgress >= 1
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ''

    
    def getString(self):
        return Localizer.QuestsFriendQuestString

    
    def getQTStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskQTStrings(toNpcId)
        
        return Localizer.QuestsTrolleyQuestQTString

    
    def getHeadlineString(self):
        return Localizer.QuestsTrolleyQuestHeadline

    
    def getObjectiveStrings(self):
        return [
            Localizer.QuestsTrolleyQuestString]



class MinigameNewbieQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkNumMinigames(self.quest[0])
        self.checkNewbieLevel(self.quest[1])

    
    def getNumQuestItems(self):
        return self.getNumMinigames()

    
    def getNumMinigames(self):
        return self.quest[0]

    
    def getNewbieLevel(self):
        return self.quest[1]

    
    def getCompletionStatus(self, av, questDesc, npc = None):
        (questId, fromNpcId, toNpcId, rewardId, toonProgress) = questDesc
        questComplete = toonProgress >= self.getNumMinigames()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumMinigames() == 1:
            return ''
        else:
            return Localizer.QuestsMinigameNewbieQuestProgress % {
                'progress': questDesc[4],
                'numMinigames': self.getNumMinigames() }

    
    def getString(self):
        return Localizer.QuestsMinigameNewbieQuestObjective % (self.getNumMinigames(), self.getNewbieLevel())

    
    def getObjectiveStrings(self):
        return [
            Localizer.QuestsMinigameNewbieQuestString % self.getNumMinigames()]

    
    def getHeadlineString(self):
        return Localizer.QuestsNewbieQuestHeadline

    
    def getQTStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskQTStrings(toNpcId)
        
        return Localizer.QuestsTrolleyQuestQTString

    
    def doesMinigameCount(self, av, avList):
        newbieHp = self.getNewbieLevel()
        points = 0
        for toon in avList:
            if toon != av and toon.getMaxHp() <= newbieHp:
                points += 1
            
        
        return points


DefaultDialog = {
    GREETING: DefaultGreeting,
    QUEST: DefaultQuest,
    INCOMPLETE: DefaultIncomplete,
    INCOMPLETE_PROGRESS: DefaultIncompleteProgress,
    INCOMPLETE_WRONG_NPC: DefaultIncompleteWrongNPC,
    COMPLETE: DefaultComplete,
    LEAVING: DefaultLeaving }

def getQuestFromNpcId(id):
    return QuestDict.get(id)[QuestDictFromNpcIndex]


def getQuestToNpcId(id):
    return QuestDict.get(id)[QuestDictToNpcIndex]


def getQuestDialog(id):
    return QuestDict.get(id)[QuestDictDialogIndex]


def getQuestReward(id, av):
    baseRewardId = QuestDict.get(id)[QuestDictRewardIndex]
    return transformReward(baseRewardId, av)

QuestDict = {
    101: (TT_TIER, 1, (CogQuest, Anywhere, 1, 'f'), Any, ToonHQ, NA, 110, DefaultDialog),
    110: (TT_TIER, 0, (TrolleyQuest,), Any, ToonHQ, NA, (120, 130, 140), DefaultDialog),
    120: (TT_TIER, 0, (DeliverItemQuest, 5), ToonHQ, 2002, NA, 121, DefaultDialog),
    121: (TT_TIER, 0, (RecoverItemQuest, ToontownGlobals.ToontownCentral, 1, 2, VeryEasy, Any, 'type'), 2002, 2002, NA, 150, DefaultDialog),
    130: (TT_TIER, 0, (DeliverItemQuest, 6), ToonHQ, 2003, NA, 131, DefaultDialog),
    131: (TT_TIER, 0, (RecoverItemQuest, ToontownGlobals.ToontownCentral, 1, 3, VeryEasy, Any, 'type'), 2003, 2003, NA, 150, DefaultDialog),
    140: (TT_TIER, 0, (DeliverItemQuest, 4), ToonHQ, 2005, NA, 141, DefaultDialog),
    141: (TT_TIER, 0, (RecoverItemQuest, ToontownGlobals.ToontownCentral, 1, 1, VeryEasy, Any, 'type'), 2005, 2005, NA, 150, DefaultDialog),
    150: (TT_TIER, 0, (FriendQuest,), Same, Same, NA, (160, 161, 162, 163), DefaultDialog),
    160: (TT_TIER, 0, (CogTrackQuest, ToontownGlobals.ToontownCentral, 3, 'c'), Same, ToonHQ, 100, NA, Localizer.QuestDialogDict[160]),
    161: (TT_TIER, 0, (CogTrackQuest, ToontownGlobals.ToontownCentral, 3, 'l'), Same, ToonHQ, 100, NA, Localizer.QuestDialogDict[161]),
    162: (TT_TIER, 0, (CogTrackQuest, ToontownGlobals.ToontownCentral, 3, 'm'), Same, ToonHQ, 100, NA, Localizer.QuestDialogDict[162]),
    163: (TT_TIER, 0, (CogTrackQuest, ToontownGlobals.ToontownCentral, 3, 's'), Same, ToonHQ, 100, NA, Localizer.QuestDialogDict[163]),
    164: (TT_TIER + 1, 1, (VisitQuest,), Any, 2001, NA, 165, Localizer.QuestDialogDict[164]),
    165: (TT_TIER + 1, 1, (CogQuest, Anywhere, 4, Any), 2001, Same, NA, (166, 167, 168, 169), Localizer.QuestDialogDict[165]),
    166: (TT_TIER + 1, 0, (CogTrackQuest, Anywhere, 4, 'c'), Same, Same, NA, (170, 171, 172), Localizer.QuestDialogDict[166]),
    167: (TT_TIER + 1, 0, (CogTrackQuest, Anywhere, 4, 'l'), Same, Same, NA, (170, 171, 172), Localizer.QuestDialogDict[167]),
    168: (TT_TIER + 1, 0, (CogTrackQuest, Anywhere, 4, 's'), Same, Same, NA, (170, 171, 172), Localizer.QuestDialogDict[168]),
    169: (TT_TIER + 1, 0, (CogTrackQuest, Anywhere, 4, 'm'), Same, Same, NA, (170, 171, 172), Localizer.QuestDialogDict[169]),
    170: (TT_TIER + 1, 0, (VisitQuest,), Same, 2005, NA, 400, Localizer.QuestDialogDict[170]),
    171: (TT_TIER + 1, 0, (VisitQuest,), Same, 2311, NA, 400, Localizer.QuestDialogDict[171]),
    172: (TT_TIER + 1, 0, (VisitQuest,), Same, 2119, NA, 400, Localizer.QuestDialogDict[172]),
    400: (TT_TIER + 1, 0, (TrackChoiceQuest, ToontownBattleGlobals.SOUND_TRACK, ToontownBattleGlobals.HEAL_TRACK), Same, Same, 400, NA, Localizer.QuestDialogDict[400]),
    1001: (TT_TIER + 2, 1, (CogQuest, ToontownGlobals.ToontownCentral, 3, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    1002: (TT_TIER + 2, 1, (CogQuest, ToontownGlobals.ToontownCentral, 4, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    1003: (TT_TIER + 2, 1, (CogQuest, ToontownGlobals.ToontownCentral, 5, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    1004: (TT_TIER + 2, 1, (CogQuest, ToontownGlobals.ToontownCentral, 6, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    1005: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'f'), Any, ToonHQ, Any, NA, DefaultDialog),
    1006: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'p'), Any, ToonHQ, Any, NA, DefaultDialog),
    1007: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'bf'), Any, ToonHQ, Any, NA, DefaultDialog),
    1008: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'b'), Any, ToonHQ, Any, NA, DefaultDialog),
    1009: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'sc'), Any, ToonHQ, Any, NA, DefaultDialog),
    1010: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'pp'), Any, ToonHQ, Any, NA, DefaultDialog),
    1011: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'cc'), Any, ToonHQ, Any, NA, DefaultDialog),
    1012: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'tm'), Any, ToonHQ, Any, NA, DefaultDialog),
    1013: (TT_TIER + 2, 1, (CogQuest, Anywhere, 4, 'f'), Any, ToonHQ, Any, NA, DefaultDialog),
    1014: (TT_TIER + 2, 1, (CogQuest, Anywhere, 4, 'p'), Any, ToonHQ, Any, NA, DefaultDialog),
    1015: (TT_TIER + 2, 1, (CogQuest, Anywhere, 4, 'bf'), Any, ToonHQ, Any, NA, DefaultDialog),
    1016: (TT_TIER + 2, 1, (CogQuest, Anywhere, 4, 'b'), Any, ToonHQ, Any, NA, DefaultDialog),
    1017: (TT_TIER + 2, 1, (CogQuest, Anywhere, 1, 'ym'), Any, ToonHQ, Any, NA, DefaultDialog),
    1018: (TT_TIER + 2, 1, (CogQuest, Anywhere, 1, 'nd'), Any, ToonHQ, Any, NA, DefaultDialog),
    1019: (TT_TIER + 2, 1, (CogQuest, Anywhere, 1, 'tw'), Any, ToonHQ, Any, NA, DefaultDialog),
    1020: (TT_TIER + 2, 1, (CogQuest, Anywhere, 1, 'dt'), Any, ToonHQ, Any, NA, DefaultDialog),
    1021: (TT_TIER + 2, 1, (CogLevelQuest, ToontownGlobals.ToontownCentral, 2, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    1022: (TT_TIER + 2, 1, (CogLevelQuest, ToontownGlobals.ToontownCentral, 6, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    1023: (TT_TIER + 2, 1, (CogLevelQuest, ToontownGlobals.ToontownCentral, 3, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    1024: (TT_TIER + 2, 1, (CogLevelQuest, ToontownGlobals.ToontownCentral, 4, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    1025: (TT_TIER + 2, 1, (CogLevelQuest, ToontownGlobals.ToontownCentral, 4, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    1026: (TT_TIER + 2, 1, (CogLevelQuest, ToontownGlobals.ToontownCentral, 6, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    1027: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 2, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    1028: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 2, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    1029: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 2, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    1030: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 2, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    1031: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 3, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    1032: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 3, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    1033: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 3, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    1034: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 3, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    1035: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 5, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    1036: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 5, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    1037: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 5, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    1038: (TT_TIER + 2, 1, (CogTrackQuest, ToontownGlobals.ToontownCentral, 5, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    1039: (TT_TIER + 2, 1, (VisitQuest,), Any, 2135, NA, (1041, 1042, 1043), Localizer.QuestDialogDict[1039]),
    1040: (TT_TIER + 2, 1, (VisitQuest,), Any, 2207, NA, (1041, 1042, 1043), Localizer.QuestDialogDict[1040]),
    1041: (TT_TIER + 2, 0, (VisitQuest,), Same, 2211, NA, 1044, Localizer.QuestDialogDict[1041]),
    1042: (TT_TIER + 2, 0, (VisitQuest,), Same, 2209, NA, 1044, Localizer.QuestDialogDict[1042]),
    1043: (TT_TIER + 2, 0, (VisitQuest,), Same, 2210, NA, 1044, Localizer.QuestDialogDict[1043]),
    1044: (TT_TIER + 2, 0, (RecoverItemQuest, Anywhere, 4, 7, VeryEasy, Any, 'type'), Same, Same, NA, 1045, Localizer.QuestDialogDict[1044]),
    1045: (TT_TIER + 2, 0, (DeliverItemQuest, 8), Same, ToonHQ, 300, NA, Localizer.QuestDialogDict[1045]),
    1046: (TT_TIER + 2, 1, (VisitQuest,), Any, 2127, NA, 1047, Localizer.QuestDialogDict[1046]),
    1047: (TT_TIER + 2, 1, (RecoverItemQuest, Anywhere, 5, 9, VeryEasy, 'm', 'track'), 2127, Same, NA, 1048, Localizer.QuestDialogDict[1047]),
    1048: (TT_TIER + 2, 0, (DeliverItemQuest, 9), Same, 2131, NA, 1049, Localizer.QuestDialogDict[1048]),
    1049: (TT_TIER + 2, 0, (RecoverItemQuest, Anywhere, 10, 2007, VeryEasy, 3, 'level'), Same, Same, NA, 1053, Localizer.QuestDialogDict[1049]),
    1053: (TT_TIER + 2, 0, (DeliverItemQuest, 9), Same, 2127, 700, NA, Localizer.QuestDialogDict[1053]),
    1054: (TT_TIER + 2, 1, (VisitQuest,), Any, 2128, NA, 1055, Localizer.QuestDialogDict[1054]),
    1055: (TT_TIER + 2, 1, (RecoverItemQuest, Anywhere, 4, 10, Easy, AnyFish), 2128, Same, NA, 1056, Localizer.QuestDialogDict[1055]),
    1056: (TT_TIER + 2, 0, (VisitQuest,), Same, 2213, NA, 1057, Localizer.QuestDialogDict[1056]),
    1057: (TT_TIER + 2, 0, (CogLevelQuest, ToontownGlobals.ToontownCentral, 6, 3), Same, Same, NA, 1058, Localizer.QuestDialogDict[1057]),
    1058: (TT_TIER + 2, 0, (DeliverItemQuest, 11), Same, 2128, 200, NA, Localizer.QuestDialogDict[1058]),
    1059: (TT_TIER + 2, 1, (VisitQuest,), Any, 2302, NA, 1060, Localizer.QuestDialogDict[1059]),
    1060: (TT_TIER + 2, 1, (RecoverItemQuest, Anywhere, 1, 12, Medium, AnyFish), 2302, Same, NA, 1062, Localizer.QuestDialogDict[1060]),
    1061: (TT_TIER + 2, 0, (CogQuest, ToontownGlobals.ToontownCentral, 6, 'p'), Same, Same, 101, NA, Localizer.QuestDialogDict[1061]),
    1062: (TT_TIER + 2, 0, (CogQuest, ToontownGlobals.ToontownCentral, 6, 'b'), Same, Same, 101, NA, Localizer.QuestDialogDict[1062]),
    900: (TT_TIER + 3, 1, (VisitQuest,), Any, 2201, NA, 1063, Localizer.QuestDialogDict[900]),
    1063: (TT_TIER + 3, 1, (RecoverItemQuest, Anywhere, 1, 13, Medium, 3, 'level'), 2201, Same, NA, 1067, Localizer.QuestDialogDict[1063]),
    1067: (TT_TIER + 3, 0, (DeliverItemQuest, 13), Same, 2112, NA, 1068, Localizer.QuestDialogDict[1067]),
    1068: (TT_TIER + 3, 0, (CogQuest, ToontownGlobals.ToontownCentral, 10, Any), Same, Same, NA, (1069, 1070, 1071), Localizer.QuestDialogDict[1068]),
    1069: (TT_TIER + 3, 0, (RecoverItemQuest, Anywhere, 1, 13, Medium, 'm', 'track'), Same, Same, NA, 1072, Localizer.QuestDialogDict[1069]),
    1070: (TT_TIER + 3, 0, (RecoverItemQuest, Anywhere, 1, 13, Medium, 's', 'track'), Same, Same, NA, 1072, Localizer.QuestDialogDict[1070]),
    1071: (TT_TIER + 3, 0, (RecoverItemQuest, Anywhere, 1, 13, Medium, 'c', 'track'), Same, Same, NA, 1072, Localizer.QuestDialogDict[1071]),
    1072: (TT_TIER + 3, 0, (DeliverItemQuest, 13), Same, 2301, NA, 1073, Localizer.QuestDialogDict[1072]),
    1073: (TT_TIER + 3, 0, (VisitQuest,), Any, 2201, NA, 1074, Localizer.QuestDialogDict[1073]),
    1074: (TT_TIER + 3, 0, (RecoverItemQuest, Anywhere, 1, 13, Hard, Any), Same, Same, NA, 1075, Localizer.QuestDialogDict[1074]),
    1075: (TT_TIER + 3, 0, (DeliverItemQuest, 13), Same, 2301, 900, NA, Localizer.QuestDialogDict[1075]),
    1076: (TT_TIER + 2, 1, (VisitQuest,), Any, 2217, NA, 1077, Localizer.QuestDialogDict[1076]),
    1077: (TT_TIER + 2, 1, (RecoverItemQuest, Anywhere, 1, 14, Medium, Any), 2217, Same, NA, 1078, Localizer.QuestDialogDict[1077]),
    1078: (TT_TIER + 2, 0, (DeliverItemQuest, 14), Same, 2302, NA, 1079, Localizer.QuestDialogDict[1078]),
    1079: (TT_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 15, Easy, 'f'), Same, 2217, NA, 1080, Localizer.QuestDialogDict[1079]),
    1092: (TT_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 15, Easy, 'sc'), Same, 2217, NA, 1080, Localizer.QuestDialogDict[1092]),
    1080: (TT_TIER + 2, 0, (RecoverItemQuest, Anywhere, 4, 15, Easy, AnyFish), Same, Same, 500, NA, Localizer.QuestDialogDict[1080]),
    1081: (TT_TIER + 2, 1, (VisitQuest,), Any, 2208, NA, 1082, Localizer.QuestDialogDict[1081]),
    1082: (TT_TIER + 2, 1, (RecoverItemQuest, Anywhere, 1, 16, Medium, 's', 'track'), 2208, Same, NA, 1083, Localizer.QuestDialogDict[1082]),
    1083: (TT_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 17, Medium, 'l', 'track'), Same, Same, NA, 1084, Localizer.QuestDialogDict[1083]),
    1084: (TT_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 18, Medium, 'm', 'track'), Same, Same, 102, NA, Localizer.QuestDialogDict[1084]),
    1085: (TT_TIER + 2, 1, (VisitQuest,), Any, 2003, NA, 1086, Localizer.QuestDialogDict[1085]),
    1086: (TT_TIER + 2, 1, (RecoverItemQuest, Anywhere, 5, 2007, Easy, 2, 'level'), 2003, Same, NA, 1089, Localizer.QuestDialogDict[1086]),
    1089: (TT_TIER + 2, 0, (DeliverItemQuest, 19), Same, ToonHQ, 100, NA, Localizer.QuestDialogDict[1089]),
    1090: (TT_TIER + 2, 1, (VisitQuest,), Any, 2119, NA, 1091, Localizer.QuestDialogDict[1090]),
    1091: (TT_TIER + 2, 1, (CogLevelQuest, ToontownGlobals.ToontownCentral, 8, 2), 2119, ToonHQ, 101, NA, Localizer.QuestDialogDict[1091]),
    1100: (TT_TIER + 2, 1, (CogQuest, ToontownGlobals.ToontownCentral, 10, Any), Any, ToonHQ, NA, 1101, DefaultDialog),
    1101: (TT_TIER + 2, 0, (DeliverItemQuest, 1000), Any, 2004, 1000, NA, DefaultDialog),
    1102: (TT_TIER + 2, 1, (CogLevelQuest, ToontownGlobals.ToontownCentral, 8, 3), Any, ToonHQ, NA, 1103, DefaultDialog),
    1103: (TT_TIER + 2, 0, (DeliverItemQuest, 1000), Any, 2004, 1000, NA, DefaultDialog),
    1105: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'f'), Any, ToonHQ, Any, NA, DefaultDialog),
    1106: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'p'), Any, ToonHQ, Any, NA, DefaultDialog),
    1107: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'bf'), Any, ToonHQ, Any, NA, DefaultDialog),
    1108: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'b'), Any, ToonHQ, Any, NA, DefaultDialog),
    1109: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'sc'), Any, ToonHQ, Any, NA, DefaultDialog),
    1110: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'pp'), Any, ToonHQ, Any, NA, DefaultDialog),
    1111: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'cc'), Any, ToonHQ, Any, NA, DefaultDialog),
    1112: (TT_TIER + 2, 1, (CogQuest, Anywhere, 2, 'tm'), Any, ToonHQ, Any, NA, DefaultDialog),
    401: (DD_TIER, 1, (TrackChoiceQuest, ToontownBattleGlobals.DROP_TRACK, ToontownBattleGlobals.LURE_TRACK), Any, ToonHQ, 400, NA, Localizer.QuestDialogDict[401]),
    2001: (DD_TIER, 1, (CogQuest, Anywhere, 3, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2002: (DD_TIER, 1, (CogQuest, Anywhere, 4, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2003: (DD_TIER, 1, (CogQuest, Anywhere, 5, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2004: (DD_TIER, 1, (CogQuest, Anywhere, 6, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2005: (DD_TIER, 1, (CogQuest, Anywhere, 7, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2006: (DD_TIER, 1, (CogQuest, Anywhere, 8, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2007: (DD_TIER, 1, (CogQuest, Anywhere, 9, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2008: (DD_TIER, 1, (CogQuest, Anywhere, 10, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2009: (DD_TIER, 1, (CogQuest, Anywhere, 12, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2010: (DD_TIER, 1, (CogLevelQuest, Anywhere, 2, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    2011: (DD_TIER, 1, (CogLevelQuest, Anywhere, 3, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    2012: (DD_TIER, 1, (CogLevelQuest, Anywhere, 2, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    2013: (DD_TIER, 1, (CogLevelQuest, Anywhere, 4, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    2014: (DD_TIER, 1, (CogLevelQuest, Anywhere, 4, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    2015: (DD_TIER, 1, (CogLevelQuest, Anywhere, 5, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    2816: (DD_TIER, 1, (CogLevelQuest, Anywhere, 4, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    2817: (DD_TIER, 1, (CogLevelQuest, Anywhere, 5, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    2818: (DD_TIER, 1, (CogLevelQuest, Anywhere, 6, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    2819: (DD_TIER, 1, (CogLevelQuest, Anywhere, 7, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    2020: (DD_TIER, 1, (CogQuest, Anywhere, 10, Any), Any, ToonHQ, NA, 2021, DefaultDialog),
    2021: (DD_TIER, 0, (DeliverItemQuest, 1000), Any, 1007, 1000, NA, DefaultDialog),
    2101: (DD_TIER + 1, 1, (CogQuest, ToontownGlobals.DonaldsDock, 3, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2102: (DD_TIER + 1, 1, (CogQuest, ToontownGlobals.DonaldsDock, 4, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2103: (DD_TIER + 1, 1, (CogQuest, ToontownGlobals.DonaldsDock, 5, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2104: (DD_TIER + 1, 1, (CogQuest, Anywhere, 6, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2105: (DD_TIER + 1, 1, (CogQuest, Anywhere, 7, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2106: (DD_TIER + 1, 1, (CogQuest, Anywhere, 8, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2107: (DD_TIER + 1, 1, (CogQuest, Anywhere, 6, 'f'), Any, ToonHQ, Any, NA, DefaultDialog),
    2108: (DD_TIER + 1, 1, (CogQuest, Anywhere, 4, 'p'), Any, ToonHQ, Any, NA, DefaultDialog),
    2109: (DD_TIER + 1, 1, (CogQuest, Anywhere, 4, 'ym'), Any, ToonHQ, Any, NA, DefaultDialog),
    2110: (DD_TIER + 1, 1, (CogQuest, Anywhere, 3, 'mm'), Any, ToonHQ, Any, NA, DefaultDialog),
    2111: (DD_TIER + 1, 1, (CogQuest, Anywhere, 2, 'ds'), Any, ToonHQ, Any, NA, DefaultDialog),
    2112: (DD_TIER + 1, 1, (CogQuest, Anywhere, 1, 'hh'), Any, ToonHQ, Any, NA, DefaultDialog),
    2113: (DD_TIER + 1, 1, (CogQuest, Anywhere, 6, 'cc'), Any, ToonHQ, Any, NA, DefaultDialog),
    2114: (DD_TIER + 1, 1, (CogQuest, Anywhere, 4, 'tm'), Any, ToonHQ, Any, NA, DefaultDialog),
    2115: (DD_TIER + 1, 1, (CogQuest, Anywhere, 4, 'nd'), Any, ToonHQ, Any, NA, DefaultDialog),
    2116: (DD_TIER + 1, 1, (CogQuest, Anywhere, 3, 'gh'), Any, ToonHQ, Any, NA, DefaultDialog),
    2117: (DD_TIER + 1, 1, (CogQuest, Anywhere, 2, 'ms'), Any, ToonHQ, Any, NA, DefaultDialog),
    2118: (DD_TIER + 1, 1, (CogQuest, Anywhere, 1, 'tf'), Any, ToonHQ, Any, NA, DefaultDialog),
    2119: (DD_TIER + 1, 1, (CogQuest, Anywhere, 6, 'sc'), Any, ToonHQ, Any, NA, DefaultDialog),
    2120: (DD_TIER + 1, 1, (CogQuest, Anywhere, 4, 'pp'), Any, ToonHQ, Any, NA, DefaultDialog),
    2121: (DD_TIER + 1, 1, (CogQuest, Anywhere, 4, 'tw'), Any, ToonHQ, Any, NA, DefaultDialog),
    2122: (DD_TIER + 1, 1, (CogQuest, Anywhere, 3, 'bc'), Any, ToonHQ, Any, NA, DefaultDialog),
    2123: (DD_TIER + 1, 1, (CogQuest, Anywhere, 2, 'nc'), Any, ToonHQ, Any, NA, DefaultDialog),
    2124: (DD_TIER + 1, 1, (CogQuest, Anywhere, 1, 'mb'), Any, ToonHQ, Any, NA, DefaultDialog),
    2125: (DD_TIER + 1, 1, (CogQuest, Anywhere, 6, 'bf'), Any, ToonHQ, Any, NA, DefaultDialog),
    2126: (DD_TIER + 1, 1, (CogQuest, Anywhere, 4, 'b'), Any, ToonHQ, Any, NA, DefaultDialog),
    2127: (DD_TIER + 1, 1, (CogQuest, Anywhere, 4, 'dt'), Any, ToonHQ, Any, NA, DefaultDialog),
    2128: (DD_TIER + 1, 1, (CogQuest, Anywhere, 3, 'ac'), Any, ToonHQ, Any, NA, DefaultDialog),
    2129: (DD_TIER + 1, 1, (CogQuest, Anywhere, 2, 'bs'), Any, ToonHQ, Any, NA, DefaultDialog),
    2130: (DD_TIER + 1, 1, (CogQuest, Anywhere, 1, 'sd'), Any, ToonHQ, Any, NA, DefaultDialog),
    2131: (DD_TIER + 1, 1, (CogLevelQuest, ToontownGlobals.DonaldsDock, 2, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    2132: (DD_TIER + 1, 1, (CogLevelQuest, ToontownGlobals.DonaldsDock, 3, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    2133: (DD_TIER + 1, 1, (CogLevelQuest, ToontownGlobals.DonaldsDock, 2, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    2134: (DD_TIER + 1, 1, (CogLevelQuest, ToontownGlobals.DonaldsDock, 4, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    2135: (DD_TIER + 1, 1, (CogLevelQuest, ToontownGlobals.DonaldsDock, 4, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    2136: (DD_TIER + 1, 1, (CogLevelQuest, ToontownGlobals.DonaldsDock, 5, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    2137: (DD_TIER + 1, 1, (CogLevelQuest, ToontownGlobals.DonaldsDock, 4, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    2138: (DD_TIER + 1, 1, (CogLevelQuest, ToontownGlobals.DonaldsDock, 6, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    2139: (DD_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.DonaldsDock, 3, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    2140: (DD_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.DonaldsDock, 3, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    2141: (DD_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.DonaldsDock, 3, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    2142: (DD_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.DonaldsDock, 3, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    2143: (DD_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.DonaldsDock, 5, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    2144: (DD_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.DonaldsDock, 5, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    2145: (DD_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.DonaldsDock, 5, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    2146: (DD_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.DonaldsDock, 5, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    2147: (DD_TIER + 1, 1, (CogTrackQuest, Anywhere, 7, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    2148: (DD_TIER + 1, 1, (CogTrackQuest, Anywhere, 7, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    2149: (DD_TIER + 1, 1, (CogTrackQuest, Anywhere, 7, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    2150: (DD_TIER + 1, 1, (CogTrackQuest, Anywhere, 7, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    2151: (DD_TIER + 1, 1, (BuildingQuest, Anywhere, 1, Any, 1), Any, ToonHQ, Any, NA, DefaultDialog),
    2152: (DD_TIER + 1, 1, (BuildingQuest, Anywhere, 1, Any, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    2153: (DD_TIER + 1, 1, (BuildingQuest, Anywhere, 2, Any, 1), Any, ToonHQ, Any, NA, DefaultDialog),
    2154: (DD_TIER + 1, 1, (BuildingQuest, Anywhere, 2, Any, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    2155: (DD_TIER + 1, 1, (BuildingQuest, Anywhere, 1, 'm', 1), Any, ToonHQ, Any, NA, DefaultDialog),
    2156: (DD_TIER + 1, 1, (BuildingQuest, Anywhere, 1, 's', 1), Any, ToonHQ, Any, NA, DefaultDialog),
    2157: (DD_TIER + 1, 1, (BuildingQuest, Anywhere, 1, 'c', 1), Any, ToonHQ, Any, NA, DefaultDialog),
    2158: (DD_TIER + 1, 1, (BuildingQuest, Anywhere, 1, 'l', 1), Any, ToonHQ, Any, NA, DefaultDialog),
    2159: (DD_TIER + 1, 1, (DeliverGagQuest, 2, ToontownBattleGlobals.THROW_TRACK, 1), Any, Any, Any, NA, DefaultDialog),
    2160: (DD_TIER + 1, 1, (DeliverGagQuest, 1, ToontownBattleGlobals.SQUIRT_TRACK, 1), Any, Any, Any, NA, DefaultDialog),
    2161: (DD_TIER + 1, 1, (DeliverGagQuest, 1, ToontownBattleGlobals.SQUIRT_TRACK, 2), Any, Any, Any, NA, DefaultDialog),
    2162: (DD_TIER + 1, 1, (DeliverGagQuest, 2, ToontownBattleGlobals.THROW_TRACK, 2), Any, Any, Any, NA, DefaultDialog),
    2201: (DD_TIER + 1, 1, (VisitQuest,), Any, 1101, NA, 2202, Localizer.QuestDialogDict[2201]),
    2202: (DD_TIER + 1, 1, (RecoverItemQuest, Anywhere, 1, 2001, Medium, 'pp'), 1101, Same, 101, NA, Localizer.QuestDialogDict[2202]),
    2203: (DD_TIER + 1, 1, (VisitQuest,), Any, 1102, NA, 2204, Localizer.QuestDialogDict[2203]),
    2204: (DD_TIER + 1, 1, (DeliverItemQuest, 2002), 1102, 1104, NA, 2205, Localizer.QuestDialogDict[2204]),
    2205: (DD_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 2003, Medium, 'f'), Same, Same, NA, 2206, Localizer.QuestDialogDict[2205]),
    2206: (DD_TIER + 1, 0, (DeliverItemQuest, 2004), Same, 1102, 201, NA, Localizer.QuestDialogDict[2206]),
    2207: (DD_TIER + 1, 1, (VisitQuest,), Any, 1201, NA, 2208, Localizer.QuestDialogDict[2207]),
    2208: (DD_TIER + 1, 1, (RecoverItemQuest, Anywhere, 1, 2005, Easy, 'bs'), 1201, Same, 701, NA, Localizer.QuestDialogDict[2208]),
    2209: (DD_TIER + 1, 1, (VisitQuest,), Any, 1302, NA, 2210, Localizer.QuestDialogDict[2209]),
    2210: (DD_TIER + 1, 1, (VisitQuest,), 1302, 1301, NA, 2211, Localizer.QuestDialogDict[2210]),
    2211: (DD_TIER + 1, 0, (CogQuest, ToontownGlobals.DonaldsDock, 5, 'mm'), Same, Same, NA, 2212, Localizer.QuestDialogDict[2211]),
    2212: (DD_TIER + 1, 0, (DeliverItemQuest, 2006), Same, 1302, NA, 2213, Localizer.QuestDialogDict[2212]),
    2213: (DD_TIER + 1, 0, (VisitQuest,), Same, 1202, NA, 2214, Localizer.QuestDialogDict[2213]),
    2214: (DD_TIER + 1, 0, (RecoverItemQuest, ToontownGlobals.DonaldsDock, 3, 2007, Hard, Any), Same, Same, NA, 2215, Localizer.QuestDialogDict[2214]),
    2215: (DD_TIER + 1, 0, (DeliverItemQuest, 2008), Same, 1302, 301, NA, Localizer.QuestDialogDict[2215]),
    2500: (DD_TIER + 1, 1, (CogQuest, ToontownGlobals.DonaldsDock, 15, Any), Any, ToonHQ, NA, 2501, DefaultDialog),
    2501: (DD_TIER + 1, 0, (DeliverItemQuest, 1000), Any, 1007, 1000, NA, DefaultDialog),
    2801: (DD_TIER + 2, 1, (CogQuest, Anywhere, 3, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2802: (DD_TIER + 2, 1, (CogQuest, Anywhere, 4, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2803: (DD_TIER + 2, 1, (CogQuest, Anywhere, 5, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2804: (DD_TIER + 2, 1, (CogQuest, Anywhere, 6, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2805: (DD_TIER + 2, 1, (CogQuest, Anywhere, 7, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2806: (DD_TIER + 2, 1, (CogQuest, Anywhere, 8, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2807: (DD_TIER + 2, 1, (CogQuest, Anywhere, 9, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2808: (DD_TIER + 2, 1, (CogQuest, Anywhere, 10, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2809: (DD_TIER + 2, 1, (CogQuest, Anywhere, 12, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    2810: (DD_TIER + 2, 1, (CogLevelQuest, Anywhere, 2, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    2811: (DD_TIER + 2, 1, (CogLevelQuest, Anywhere, 3, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    2812: (DD_TIER + 2, 1, (CogLevelQuest, Anywhere, 2, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    2813: (DD_TIER + 2, 1, (CogLevelQuest, Anywhere, 4, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    2814: (DD_TIER + 2, 1, (CogLevelQuest, Anywhere, 4, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    2815: (DD_TIER + 2, 1, (CogLevelQuest, Anywhere, 5, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    2816: (DD_TIER + 2, 1, (CogLevelQuest, Anywhere, 4, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    2817: (DD_TIER + 2, 1, (CogLevelQuest, Anywhere, 5, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    2818: (DD_TIER + 2, 1, (CogLevelQuest, Anywhere, 6, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    2819: (DD_TIER + 2, 1, (CogLevelQuest, Anywhere, 7, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    2820: (DD_TIER + 2, 1, (CogQuest, Anywhere, 20, Any), Any, ToonHQ, NA, 2821, DefaultDialog),
    2821: (DD_TIER + 2, 0, (DeliverItemQuest, 1000), Any, 1007, 1000, NA, DefaultDialog),
    901: (DD_TIER + 2, 1, (VisitQuest,), Any, 1203, NA, 2902, Localizer.QuestDialogDict[901]),
    2902: (DD_TIER + 2, 1, (VisitQuest,), 1203, 1303, NA, 2903, Localizer.QuestDialogDict[2902]),
    2903: (DD_TIER + 2, 0, (DeliverItemQuest, 2009), Same, 1106, NA, 2904, Localizer.QuestDialogDict[2903]),
    2904: (DD_TIER + 2, 0, (DeliverItemQuest, 2010), Same, 1203, NA, 2905, Localizer.QuestDialogDict[2904]),
    2905: (DD_TIER + 2, 0, (VisitQuest, 2009), Same, 1105, NA, 2906, Localizer.QuestDialogDict[2905]),
    2906: (DD_TIER + 2, 0, (DeliverGagQuest, 3, ToontownBattleGlobals.SQUIRT_TRACK, 2), Same, Same, NA, 2907, Localizer.QuestDialogDict[2906]),
    2907: (DD_TIER + 2, 0, (DeliverItemQuest, 2011), Same, 1203, NA, (2910, 2915, 2920), Localizer.QuestDialogDict[2907]),
    2910: (DD_TIER + 2, 0, (VisitQuest,), Same, 1107, NA, 2911, Localizer.QuestDialog_2910),
    2911: (DD_TIER + 2, 0, (CogTrackQuest, ToontownGlobals.DonaldsDock, 4, 'm'), Same, Same, NA, 2925, Localizer.QuestDialogDict[2911]),
    2915: (DD_TIER + 2, 0, (VisitQuest,), Same, 1204, NA, 2916, Localizer.QuestDialog_2910),
    2916: (DD_TIER + 2, 0, (CogTrackQuest, ToontownGlobals.DonaldsDock, 2, 's'), Same, Same, NA, 2925, Localizer.QuestDialogDict[2916]),
    2920: (DD_TIER + 2, 0, (VisitQuest,), Same, 1204, NA, 2921, Localizer.QuestDialog_2910),
    2921: (DD_TIER + 2, 0, (CogTrackQuest, ToontownGlobals.DonaldsDock, 6, 'c'), Same, Same, NA, 2925, Localizer.QuestDialogDict[2921]),
    2925: (DD_TIER + 2, 0, (DeliverItemQuest, 2012), Same, 1203, NA, 2926, Localizer.QuestDialogDict[2925]),
    2926: (DD_TIER + 2, 0, (BuildingQuest, ToontownGlobals.DonaldsDock, 1, Any, 2), Same, Same, 900, NA, Localizer.QuestDialogDict[2926]),
    3101: (DG_TIER, 1, (CogQuest, ToontownGlobals.DaisyGardens, 8, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    3102: (DG_TIER, 1, (CogQuest, ToontownGlobals.DaisyGardens, 10, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    3103: (DG_TIER, 1, (CogQuest, ToontownGlobals.DaisyGardens, 12, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    3104: (DG_TIER, 1, (CogQuest, Anywhere, 14, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    3105: (DG_TIER, 1, (CogQuest, Anywhere, 16, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    3106: (DG_TIER, 1, (CogQuest, Anywhere, 18, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    3107: (DG_TIER, 1, (CogQuest, Anywhere, 10, 'f'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3108: (DG_TIER, 1, (CogQuest, Anywhere, 8, 'p'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3109: (DG_TIER, 1, (CogQuest, Anywhere, 8, 'ym'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3110: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'mm'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3111: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'ds'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3112: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'hh'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3113: (DG_TIER, 1, (CogQuest, Anywhere, 10, 'cc'), Any, ToonHQ, Any, NA, DefaultDialog),
    3114: (DG_TIER, 1, (CogQuest, Anywhere, 8, 'tm'), Any, ToonHQ, Any, NA, DefaultDialog),
    3115: (DG_TIER, 1, (CogQuest, Anywhere, 8, 'nd'), Any, ToonHQ, Any, NA, DefaultDialog),
    3116: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'gh'), Any, ToonHQ, Any, NA, DefaultDialog),
    3117: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'ms'), Any, ToonHQ, Any, NA, DefaultDialog),
    3118: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'tf'), Any, ToonHQ, Any, NA, DefaultDialog),
    3119: (DG_TIER, 1, (CogQuest, Anywhere, 10, 'sc'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3120: (DG_TIER, 1, (CogQuest, Anywhere, 8, 'pp'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3121: (DG_TIER, 1, (CogQuest, Anywhere, 8, 'tw'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3122: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'bc'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3123: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'nc'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3124: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'mb'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3125: (DG_TIER, 1, (CogQuest, Anywhere, 10, 'bf'), Any, ToonHQ, Any, NA, DefaultDialog),
    3126: (DG_TIER, 1, (CogQuest, Anywhere, 8, 'b'), Any, ToonHQ, Any, NA, DefaultDialog),
    3127: (DG_TIER, 1, (CogQuest, Anywhere, 8, 'dt'), Any, ToonHQ, Any, NA, DefaultDialog),
    3128: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'ac'), Any, ToonHQ, Any, NA, DefaultDialog),
    3129: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'bs'), Any, ToonHQ, Any, NA, DefaultDialog),
    3130: (DG_TIER, 1, (CogQuest, Anywhere, 6, 'sd'), Any, ToonHQ, Any, NA, DefaultDialog),
    3131: (DG_TIER, 1, (CogLevelQuest, Anywhere, 10, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    3132: (DG_TIER, 1, (CogLevelQuest, Anywhere, 15, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    3133: (DG_TIER, 1, (CogLevelQuest, Anywhere, 8, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    3134: (DG_TIER, 1, (CogLevelQuest, Anywhere, 12, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    3135: (DG_TIER, 1, (CogLevelQuest, Anywhere, 4, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    3136: (DG_TIER, 1, (CogLevelQuest, Anywhere, 6, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    3137: (DG_TIER, 1, (CogLevelQuest, Anywhere, 8, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    3138: (DG_TIER, 1, (CogLevelQuest, Anywhere, 12, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    3139: (DG_TIER, 1, (CogTrackQuest, ToontownGlobals.DaisyGardens, 6, 'm'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3140: (DG_TIER, 1, (CogTrackQuest, ToontownGlobals.DaisyGardens, 6, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    3141: (DG_TIER, 1, (CogTrackQuest, ToontownGlobals.DaisyGardens, 6, 'c'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3142: (DG_TIER, 1, (CogTrackQuest, ToontownGlobals.DaisyGardens, 6, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    3143: (DG_TIER, 1, (CogTrackQuest, ToontownGlobals.DaisyGardens, 10, 'm'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3144: (DG_TIER, 1, (CogTrackQuest, ToontownGlobals.DaisyGardens, 10, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    3145: (DG_TIER, 1, (CogTrackQuest, ToontownGlobals.DaisyGardens, 10, 'c'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3146: (DG_TIER, 1, (CogTrackQuest, ToontownGlobals.DaisyGardens, 10, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    3147: (DG_TIER, 1, (CogTrackQuest, Anywhere, 14, 'm'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3148: (DG_TIER, 1, (CogTrackQuest, Anywhere, 14, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    3149: (DG_TIER, 1, (CogTrackQuest, Anywhere, 14, 'c'), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3150: (DG_TIER, 1, (CogTrackQuest, Anywhere, 14, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    3151: (DG_TIER, 1, (BuildingQuest, Anywhere, 1, Any, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    3152: (DG_TIER, 1, (BuildingQuest, Anywhere, 2, Any, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    3153: (DG_TIER, 1, (BuildingQuest, Anywhere, 3, Any, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    3154: (DG_TIER, 1, (BuildingQuest, Anywhere, 4, Any, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    3155: (DG_TIER, 1, (BuildingQuest, Anywhere, 2, 'm', 2), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3156: (DG_TIER, 1, (BuildingQuest, Anywhere, 2, 's', 2), Any, ToonHQ, Any, NA, DefaultDialog),
    3157: (DG_TIER, 1, (BuildingQuest, Anywhere, 2, 'c', 2), Any, ToonHQ, OBSOLETE, NA, DefaultDialog),
    3158: (DG_TIER, 1, (BuildingQuest, Anywhere, 2, 'l', 2), Any, ToonHQ, Any, NA, DefaultDialog),
    3200: (DG_TIER, 1, (VisitQuest,), Any, 5101, NA, 3201, Localizer.QuestDialogDict[3200]),
    3201: (DG_TIER, 1, (DeliverItemQuest, 5001), 5101, 5206, NA, 3203, Localizer.QuestDialogDict[3201]),
    3203: (DG_TIER, 0, (RecoverItemQuest, ToontownGlobals.DaisyGardens, 1, 5002, VeryHard, Any), Same, Same, 100, NA, Localizer.QuestDialogDict[3203]),
    3204: (DG_TIER, 1, (VisitQuest,), Any, 5106, NA, 3205, Localizer.QuestDialogDict[3204]),
    3205: (DG_TIER, 1, (RecoverItemQuest, Anywhere, 1, 5003, Medium, 'b'), 5106, Same, 100, NA, Localizer.QuestDialogDict[3205]),
    3206: (DG_TIER, 1, (VisitQuest,), Any, 5107, NA, 3207, Localizer.QuestDialogDict[3206]),
    3207: (DG_TIER, 1, (RecoverItemQuest, ToontownGlobals.DaisyGardens, 10, 5004, VeryEasy, 'dt'), 5107, Same, 101, NA, Localizer.QuestDialogDict[3207]),
    3208: (DG_TIER, 1, (CogQuest, ToontownGlobals.DaisyGardens, 10, 'cc'), Any, ToonHQ, NA, 3209, Localizer.QuestDialogDict[3208]),
    3209: (DG_TIER, 0, (CogQuest, ToontownGlobals.DaisyGardens, 10, 'tm'), Same, Same, 202, NA, Localizer.QuestDialogDict[3209]),
    3247: (DG_TIER, 1, (CogQuest, ToontownGlobals.DaisyGardens, 20, 'b'), Any, ToonHQ, 202, NA, Localizer.QuestDialogDict[3247]),
    3210: (DG_TIER, 1, (DeliverGagQuest, 10, ToontownBattleGlobals.SQUIRT_TRACK, 0), Any, 5207, NA, 3211, Localizer.QuestDialogDict[3210]),
    3211: (DG_TIER, 0, (CogQuest, 5200, 20, Any), Same, Same, 100, NA, Localizer.QuestDialogDict[3211]),
    3212: (DG_TIER, 1, (VisitQuest,), Any, 5208, NA, 3213, Localizer.QuestDialogDict[3212]),
    3213: (DG_TIER, 1, (RecoverItemQuest, ToontownGlobals.DaisyGardens, 1, 5005, VeryHard, Any), 5208, Same, NA, 3214, Localizer.QuestDialogDict[3213]),
    3214: (DG_TIER, 0, (RecoverItemQuest, ToontownGlobals.DaisyGardens, 1, 5006, VeryHard, Any), Same, Same, NA, 3215, Localizer.QuestDialogDict[3214]),
    3215: (DG_TIER, 0, (RecoverItemQuest, ToontownGlobals.DaisyGardens, 1, 5007, VeryHard, Any), Same, Same, NA, 3216, Localizer.QuestDialogDict[3215]),
    3216: (DG_TIER, 0, (RecoverItemQuest, ToontownGlobals.DaisyGardens, 1, 5008, VeryHard, Any), Same, Same, 202, NA, Localizer.QuestDialogDict[3216]),
    3217: (DG_TIER, 1, (RecoverItemQuest, Anywhere, 1, 5010, VeryEasy, 'nd'), ToonHQ, ToonHQ, NA, 3218, Localizer.QuestDialogDict[3217]),
    3218: (DG_TIER, 0, (RecoverItemQuest, Anywhere, 1, 5010, VeryHard, 'gh'), Same, Same, NA, 3219, Localizer.QuestDialogDict[3218]),
    3219: (DG_TIER, 0, (RecoverItemQuest, Anywhere, 1, 5010, Easy, 'ms'), Same, Same, 101, NA, Localizer.QuestDialogDict[3219]),
    3244: (DG_TIER, 1, (RecoverItemQuest, Anywhere, 1, 5010, VeryEasy, 'ac'), ToonHQ, ToonHQ, NA, 3245, Localizer.QuestDialogDict[3244]),
    3245: (DG_TIER, 0, (RecoverItemQuest, Anywhere, 1, 5010, VeryHard, 'bs'), Same, Same, NA, 3246, Localizer.QuestDialogDict[3245]),
    3246: (DG_TIER, 0, (RecoverItemQuest, Anywhere, 1, 5010, VeryHard, 'sd'), Same, Same, 101, NA, Localizer.QuestDialogDict[3246]),
    3220: (DG_TIER, 1, (VisitQuest,), Any, 5207, NA, 3221, Localizer.QuestDialogDict[3220]),
    3221: (DG_TIER, 1, (CogQuest, ToontownGlobals.DaisyGardens, 20, Any), 5207, Same, 100, NA, Localizer.QuestDialogDict[3221]),
    3222: (DG_TIER, 1, (BuildingQuest, Anywhere, 2, Any, 1), ToonHQ, ToonHQ, NA, 3223, Localizer.QuestDialogDict[3222]),
    3223: (DG_TIER, 0, (BuildingQuest, Anywhere, 2, Any, 2), Same, Same, NA, 3224, Localizer.QuestDialogDict[3223]),
    3224: (DG_TIER, 0, (BuildingQuest, Anywhere, 2, Any, 3), Same, Same, 501, NA, Localizer.QuestDialogDict[3224]),
    3225: (DG_TIER, 1, (VisitQuest,), Any, 5108, NA, (3226, 3227, 3228, 3229, 3230, 3231, 3232, 3233, 3234), Localizer.QuestDialogDict[3225]),
    3226: (DG_TIER, 1, (DeliverItemQuest, 5011), 5108, 5201, NA, 3235, Localizer.QuestDialog_3225),
    3227: (DG_TIER, 1, (DeliverItemQuest, 5011), 5108, 5203, NA, 3235, Localizer.QuestDialog_3225),
    3228: (DG_TIER, 1, (DeliverItemQuest, 5011), 5108, 5204, NA, 3235, Localizer.QuestDialog_3225),
    3229: (DG_TIER, 1, (DeliverItemQuest, 5011), 5108, 5205, NA, 3235, Localizer.QuestDialog_3225),
    3230: (DG_TIER, 1, (DeliverItemQuest, 5011), 5108, 5102, NA, 3235, Localizer.QuestDialog_3225),
    3231: (DG_TIER, 1, (DeliverItemQuest, 5011), 5108, 5103, NA, 3235, Localizer.QuestDialog_3225),
    3232: (DG_TIER, 1, (DeliverItemQuest, 5011), 5108, 5104, NA, 3235, Localizer.QuestDialog_3225),
    3233: (DG_TIER, 1, (DeliverItemQuest, 5011), 5108, 5105, NA, 3235, Localizer.QuestDialog_3225),
    3234: (DG_TIER, 1, (DeliverItemQuest, 5011), 5108, 5207, NA, 3235, Localizer.QuestDialog_3225),
    3235: (DG_TIER, 0, (CogQuest, ToontownGlobals.DaisyGardens, 10, Any), Same, 5108, 100, NA, Localizer.QuestDialogDict[3235]),
    3236: (DG_TIER, 1, (BuildingQuest, Anywhere, 3, 'l', 2), Any, ToonHQ, NA, 3237, Localizer.QuestDialogDict[3236]),
    3237: (DG_TIER, 0, (BuildingQuest, Anywhere, 3, 's', 2), Same, Same, 702, NA, Localizer.QuestDialogDict[3237]),
    3238: (DG_TIER, 1, (RecoverItemQuest, Anywhere, 1, 2, VeryEasy, 'm'), Any, ToonHQ, NA, 3239, Localizer.QuestDialogDict[3238]),
    3239: (DG_TIER, 0, (RecoverItemQuest, Anywhere, 1, 5012, Hard, 'm'), Same, Same, 302, NA, Localizer.QuestDialogDict[3239]),
    3242: (DG_TIER, 1, (RecoverItemQuest, Anywhere, 1, 2, VeryEasy, 'le'), Any, ToonHQ, NA, 3243, Localizer.QuestDialogDict[3242]),
    3243: (DG_TIER, 0, (RecoverItemQuest, Anywhere, 1, 5012, Hard, 'le'), Same, Same, 302, NA, Localizer.QuestDialogDict[3243]),
    3240: (DG_TIER, 1, (RecoverItemQuest, Anywhere, 1, 5009, Hard, 'le'), Any, 5103, 102, NA, Localizer.QuestDialogDict[3240]),
    3241: (DG_TIER, 1, (BuildingQuest, Anywhere, 5, Any, 3), Any, ToonHQ, 102, NA, Localizer.QuestDialogDict[3241]),
    3500: (DG_TIER, 1, (CogQuest, ToontownGlobals.DaisyGardens, 25, Any), Any, ToonHQ, NA, 3501, DefaultDialog),
    3501: (DG_TIER, 0, (DeliverItemQuest, 1000), Any, 5007, 1000, NA, DefaultDialog),
    4001: (MM_TIER, 1, (TrackChoiceQuest, ToontownBattleGlobals.TRAP_TRACK, ToontownBattleGlobals.HEAL_TRACK), Any, ToonHQ, 400, NA, Localizer.QuestDialogDict[4001]),
    4002: (MM_TIER, 1, (TrackChoiceQuest, ToontownBattleGlobals.TRAP_TRACK, ToontownBattleGlobals.SOUND_TRACK), Any, ToonHQ, 400, NA, Localizer.QuestDialogDict[4002]),
    4010: (MM_TIER, 1, (CogQuest, Anywhere, 16, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4011: (MM_TIER, 1, (CogQuest, Anywhere, 18, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4012: (MM_TIER, 1, (CogQuest, Anywhere, 20, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4013: (MM_TIER, 1, (CogQuest, Anywhere, 22, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4014: (MM_TIER, 1, (CogQuest, Anywhere, 24, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4015: (MM_TIER, 1, (CogQuest, Anywhere, 26, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4016: (MM_TIER, 1, (CogQuest, Anywhere, 28, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4017: (MM_TIER, 1, (CogQuest, Anywhere, 30, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4018: (MM_TIER, 1, (CogQuest, Anywhere, 32, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4019: (MM_TIER, 1, (CogQuest, Anywhere, 34, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4020: (MM_TIER, 1, (CogLevelQuest, Anywhere, 20, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4021: (MM_TIER, 1, (CogLevelQuest, Anywhere, 25, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4022: (MM_TIER, 1, (CogLevelQuest, Anywhere, 16, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    4023: (MM_TIER, 1, (CogLevelQuest, Anywhere, 20, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    4024: (MM_TIER, 1, (CogLevelQuest, Anywhere, 10, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    4025: (MM_TIER, 1, (CogLevelQuest, Anywhere, 20, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    4026: (MM_TIER, 1, (CogLevelQuest, Anywhere, 16, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    4027: (MM_TIER, 1, (CogLevelQuest, Anywhere, 18, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    4028: (MM_TIER, 1, (CogLevelQuest, Anywhere, 20, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    4029: (MM_TIER, 1, (CogLevelQuest, Anywhere, 24, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    4030: (MM_TIER, 1, (CogQuest, Anywhere, 45, Any), Any, ToonHQ, NA, 4031, DefaultDialog),
    4031: (MM_TIER, 0, (DeliverItemQuest, 1000), Any, 4008, 1000, NA, DefaultDialog),
    4101: (MM_TIER + 1, 1, (CogQuest, ToontownGlobals.MinniesMelodyland, 16, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4102: (MM_TIER + 1, 1, (CogQuest, ToontownGlobals.MinniesMelodyland, 18, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4103: (MM_TIER + 1, 1, (CogQuest, ToontownGlobals.MinniesMelodyland, 20, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4104: (MM_TIER + 1, 1, (CogQuest, ToontownGlobals.MinniesMelodyland, 24, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4105: (MM_TIER + 1, 1, (CogQuest, Anywhere, 28, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4106: (MM_TIER + 1, 1, (CogQuest, Anywhere, 32, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4107: (MM_TIER + 1, 1, (CogQuest, Anywhere, 20, 'f'), Any, ToonHQ, Any, NA, DefaultDialog),
    4108: (MM_TIER + 1, 1, (CogQuest, Anywhere, 16, 'p'), Any, ToonHQ, Any, NA, DefaultDialog),
    4109: (MM_TIER + 1, 1, (CogQuest, Anywhere, 16, 'ym'), Any, ToonHQ, Any, NA, DefaultDialog),
    4110: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'mm'), Any, ToonHQ, Any, NA, DefaultDialog),
    4111: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'ds'), Any, ToonHQ, Any, NA, DefaultDialog),
    4112: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'hh'), Any, ToonHQ, Any, NA, DefaultDialog),
    4113: (MM_TIER + 1, 1, (CogQuest, Anywhere, 20, 'cc'), Any, ToonHQ, Any, NA, DefaultDialog),
    4114: (MM_TIER + 1, 1, (CogQuest, Anywhere, 16, 'tm'), Any, ToonHQ, Any, NA, DefaultDialog),
    4115: (MM_TIER + 1, 1, (CogQuest, Anywhere, 16, 'nd'), Any, ToonHQ, Any, NA, DefaultDialog),
    4116: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'gh'), Any, ToonHQ, Any, NA, DefaultDialog),
    4117: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'ms'), None, ToonHQ, Any, NA, DefaultDialog),
    4118: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'tf'), None, ToonHQ, Any, NA, DefaultDialog),
    4119: (MM_TIER + 1, 1, (CogQuest, Anywhere, 20, 'sc'), Any, ToonHQ, Any, NA, DefaultDialog),
    4120: (MM_TIER + 1, 1, (CogQuest, Anywhere, 16, 'pp'), Any, ToonHQ, Any, NA, DefaultDialog),
    4121: (MM_TIER + 1, 1, (CogQuest, Anywhere, 16, 'tw'), Any, ToonHQ, Any, NA, DefaultDialog),
    4122: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'bc'), Any, ToonHQ, Any, NA, DefaultDialog),
    4123: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'nc'), Any, ToonHQ, Any, NA, DefaultDialog),
    4124: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'mb'), Any, ToonHQ, Any, NA, DefaultDialog),
    4125: (MM_TIER + 1, 1, (CogQuest, Anywhere, 20, 'bf'), Any, ToonHQ, Any, NA, DefaultDialog),
    4126: (MM_TIER + 1, 1, (CogQuest, Anywhere, 16, 'b'), Any, ToonHQ, Any, NA, DefaultDialog),
    4127: (MM_TIER + 1, 1, (CogQuest, Anywhere, 16, 'dt'), Any, ToonHQ, Any, NA, DefaultDialog),
    4128: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'ac'), Any, ToonHQ, Any, NA, DefaultDialog),
    4129: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'bs'), Any, ToonHQ, Any, NA, DefaultDialog),
    4130: (MM_TIER + 1, 1, (CogQuest, Anywhere, 12, 'sd'), Any, ToonHQ, Any, NA, DefaultDialog),
    4131: (MM_TIER + 1, 1, (CogLevelQuest, Anywhere, 20, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4132: (MM_TIER + 1, 1, (CogLevelQuest, Anywhere, 25, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4133: (MM_TIER + 1, 1, (CogLevelQuest, Anywhere, 16, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    4134: (MM_TIER + 1, 1, (CogLevelQuest, Anywhere, 20, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    4135: (MM_TIER + 1, 1, (CogLevelQuest, Anywhere, 10, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    4136: (MM_TIER + 1, 1, (CogLevelQuest, Anywhere, 20, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    4137: (MM_TIER + 1, 1, (CogLevelQuest, Anywhere, 16, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    4138: (MM_TIER + 1, 1, (CogLevelQuest, Anywhere, 24, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    4139: (MM_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.MinniesMelodyland, 15, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    4140: (MM_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.MinniesMelodyland, 15, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    4141: (MM_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.MinniesMelodyland, 15, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    4142: (MM_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.MinniesMelodyland, 15, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    4143: (MM_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.MinniesMelodyland, 24, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    4144: (MM_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.MinniesMelodyland, 24, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    4145: (MM_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.MinniesMelodyland, 24, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    4146: (MM_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.MinniesMelodyland, 24, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    4147: (MM_TIER + 1, 1, (CogTrackQuest, Anywhere, 30, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    4148: (MM_TIER + 1, 1, (CogTrackQuest, Anywhere, 30, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    4149: (MM_TIER + 1, 1, (CogTrackQuest, Anywhere, 30, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    4150: (MM_TIER + 1, 1, (CogTrackQuest, Anywhere, 30, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    4151: (MM_TIER + 1, 1, (BuildingQuest, Anywhere, 1, Any, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4152: (MM_TIER + 1, 1, (BuildingQuest, Anywhere, 2, Any, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4153: (MM_TIER + 1, 1, (BuildingQuest, Anywhere, 3, Any, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4154: (MM_TIER + 1, 1, (BuildingQuest, Anywhere, 4, Any, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4155: (MM_TIER + 1, 1, (BuildingQuest, Anywhere, 3, 'm', 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4156: (MM_TIER + 1, 1, (BuildingQuest, Anywhere, 3, 's', 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4157: (MM_TIER + 1, 1, (BuildingQuest, Anywhere, 3, 'c', 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4158: (MM_TIER + 1, 1, (BuildingQuest, Anywhere, 3, 'l', 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4200: (MM_TIER + 1, 1, (VisitQuest,), Any, 4101, NA, 4201, Localizer.QuestDialogDict[4200]),
    4201: (MM_TIER + 1, 1, (VisitQuest,), 4101, 4201, NA, 4202, Localizer.QuestDialogDict[4201]),
    4202: (MM_TIER + 1, 0, (DeliverItemQuest, 4001), Same, 4101, NA, 4203, Localizer.QuestDialogDict[4202]),
    4203: (MM_TIER + 1, 0, (VisitQuest,), Same, 4301, NA, 4204, Localizer.QuestDialogDict[4203]),
    4204: (MM_TIER + 1, 0, (CogQuest, ToontownGlobals.MinniesMelodyland, 10, Any), Same, Same, NA, 4205, Localizer.QuestDialogDict[4204]),
    4205: (MM_TIER + 1, 0, (DeliverItemQuest, 4002), Same, 4101, NA, 4206, Localizer.QuestDialogDict[4205]),
    4206: (MM_TIER + 1, 0, (VisitQuest,), Same, 4102, NA, 4207, Localizer.QuestDialogDict[4206]),
    4207: (MM_TIER + 1, 0, (VisitQuest,), Same, 4108, NA, 4208, Localizer.QuestDialogDict[4207]),
    4208: (MM_TIER + 1, 0, (DeliverGagQuest, 1, ToontownBattleGlobals.THROW_TRACK, 4), Same, Same, NA, 4209, Localizer.QuestDialogDict[4208]),
    4209: (MM_TIER + 1, 0, (DeliverItemQuest, 4003), Same, 4102, NA, 4210, Localizer.QuestDialogDict[4209]),
    4210: (MM_TIER + 1, 0, (DeliverItemQuest, 4004), Same, 4101, 203, NA, Localizer.QuestDialogDict[4210]),
    4211: (MM_TIER + 1, 1, (VisitQuest,), ToonHQ, 4103, NA, 4212, Localizer.QuestDialogDict[4211]),
    4212: (MM_TIER + 1, 1, (CogQuest, ToontownGlobals.MinniesMelodyland, 10, 'nc'), 4103, Same, NA, 4213, Localizer.QuestDialogDict[4212]),
    4213: (MM_TIER + 1, 0, (CogTrackQuest, ToontownGlobals.MinniesMelodyland, 20, 'm'), Same, Same, NA, 4214, Localizer.QuestDialogDict[4213]),
    4214: (MM_TIER + 1, 0, (BuildingQuest, Anywhere, 1, 'm', Any), Same, Same, 303, NA, Localizer.QuestDialogDict[4214]),
    4215: (MM_TIER + 1, 1, (VisitQuest,), Any, 4302, NA, 4216, Localizer.QuestDialogDict[4215]),
    4216: (MM_TIER + 1, 1, (RecoverItemQuest, Anywhere, 1, 4005, VeryHard, 'gh'), 4302, Same, NA, 4217, Localizer.QuestDialogDict[4216]),
    4217: (MM_TIER + 1, 0, (DeliverItemQuest, 4005), Same, 4203, NA, 4218, Localizer.QuestDialogDict[4217]),
    4218: (MM_TIER + 1, 0, (VisitQuest,), Any, 4302, NA, 4219, Localizer.QuestDialogDict[4218]),
    4219: (MM_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 4006, VeryHard, 'gh'), Same, Same, NA, 4220, Localizer.QuestDialogDict[4219]),
    4220: (MM_TIER + 1, 0, (DeliverItemQuest, 4006), Same, 4308, NA, 4221, Localizer.QuestDialogDict[4220]),
    4221: (MM_TIER + 1, 0, (VisitQuest,), Any, 4302, NA, 4222, Localizer.QuestDialogDict[4221]),
    4222: (MM_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 4007, VeryHard, 'gh'), Same, Same, NA, 4223, Localizer.QuestDialogDict[4222]),
    4223: (MM_TIER + 1, 0, (DeliverItemQuest, 4007), Same, 4202, NA, 4224, Localizer.QuestDialogDict[4223]),
    4224: (MM_TIER + 1, 0, (VisitQuest,), Any, 4302, 703, NA, Localizer.QuestDialogDict[4224]),
    4500: (MM_TIER + 1, 1, (CogQuest, ToontownGlobals.MinniesMelodyland, 40, Any), Any, ToonHQ, NA, 4501, DefaultDialog),
    4501: (MM_TIER + 1, 0, (DeliverItemQuest, 1000), Any, 4008, 1000, NA, DefaultDialog),
    902: (MM_TIER + 2, 1, (VisitQuest,), Any, 4303, NA, 4903, Localizer.QuestDialogDict[902]),
    4903: (MM_TIER + 2, 1, (DeliverItemQuest, 4008), 4303, 4109, NA, 4904, Localizer.QuestDialogDict[4903]),
    4904: (MM_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 4009, VeryHard, AnyFish), Same, Same, NA, 4905, Localizer.QuestDialogDict[4904]),
    4905: (MM_TIER + 2, 0, (BuildingQuest, Anywhere, 1, Any, 1), Same, Same, NA, 4906, Localizer.QuestDialogDict[4905]),
    4906: (MM_TIER + 2, 0, (DeliverItemQuest, 4010), Same, 4303, NA, 4907, Localizer.QuestDialogDict[4906]),
    4907: (MM_TIER + 2, 0, (VisitQuest,), Same, 4208, NA, 4908, Localizer.QuestDialogDict[4907]),
    4908: (MM_TIER + 2, 0, (BuildingQuest, Anywhere, 1, Any, 2), Same, Same, NA, 4909, Localizer.QuestDialogDict[4908]),
    4909: (MM_TIER + 2, 0, (BuildingQuest, Anywhere, 1, Any, 3), Same, Same, NA, 4910, Localizer.QuestDialogDict[4909]),
    4910: (MM_TIER + 2, 0, (DeliverItemQuest, 4011), Same, 4303, 900, NA, Localizer.QuestDialogDict[4910]),
    4810: (MM_TIER + 2, 1, (CogQuest, Anywhere, 16, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4811: (MM_TIER + 2, 1, (CogQuest, Anywhere, 18, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4812: (MM_TIER + 2, 1, (CogQuest, Anywhere, 20, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4813: (MM_TIER + 2, 1, (CogQuest, Anywhere, 22, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4814: (MM_TIER + 2, 1, (CogQuest, Anywhere, 24, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4815: (MM_TIER + 2, 1, (CogQuest, Anywhere, 26, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4816: (MM_TIER + 2, 1, (CogQuest, Anywhere, 28, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4817: (MM_TIER + 2, 1, (CogQuest, Anywhere, 30, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4818: (MM_TIER + 2, 1, (CogQuest, Anywhere, 32, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4819: (MM_TIER + 2, 1, (CogQuest, Anywhere, 34, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    4820: (MM_TIER + 2, 1, (CogLevelQuest, Anywhere, 20, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4821: (MM_TIER + 2, 1, (CogLevelQuest, Anywhere, 25, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    4822: (MM_TIER + 2, 1, (CogLevelQuest, Anywhere, 16, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    4823: (MM_TIER + 2, 1, (CogLevelQuest, Anywhere, 20, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    4824: (MM_TIER + 2, 1, (CogLevelQuest, Anywhere, 10, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    4825: (MM_TIER + 2, 1, (CogLevelQuest, Anywhere, 20, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    4826: (MM_TIER + 2, 1, (CogLevelQuest, Anywhere, 16, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    4827: (MM_TIER + 2, 1, (CogLevelQuest, Anywhere, 18, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    4828: (MM_TIER + 2, 1, (CogLevelQuest, Anywhere, 20, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    4829: (MM_TIER + 2, 1, (CogLevelQuest, Anywhere, 24, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    4830: (MM_TIER + 2, 1, (CogQuest, Anywhere, 45, Any), Any, ToonHQ, NA, 4831, DefaultDialog),
    4831: (MM_TIER + 2, 0, (DeliverItemQuest, 1000), Any, 4008, 1000, NA, DefaultDialog),
    5247: (BR_TIER, 1, (VisitQuest,), Any, 3112, NA, 5248, Localizer.QuestDialogDict[5247]),
    5248: (BR_TIER, 1, (CogLevelQuest, Anywhere, 10, 8), 3112, Same, NA, 5249, Localizer.QuestDialogDict[5248]),
    5249: (BR_TIER, 0, (RecoverItemQuest, Anywhere, 3, 3018, VeryHard, AnyFish), Same, Same, NA, (5250, 5258, 5259, 5260), Localizer.QuestDialogDict[5249]),
    5250: (BR_TIER, 0, (BuildingQuest, Anywhere, 2, 'l', 4), Same, Same, NA, (5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008), Localizer.QuestDialogDict[5250]),
    5258: (BR_TIER, 0, (BuildingQuest, Anywhere, 2, 'c', 4), Same, Same, NA, (5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008), Localizer.QuestDialogDict[5258]),
    5259: (BR_TIER, 0, (BuildingQuest, Anywhere, 2, 'm', 4), Same, Same, NA, (5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008), Localizer.QuestDialogDict[5259]),
    5260: (BR_TIER, 0, (BuildingQuest, Anywhere, 2, 's', 4), Same, Same, NA, (5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008), Localizer.QuestDialogDict[5260]),
    5001: (BR_TIER, 0, (TrackChoiceQuest, ToontownBattleGlobals.SOUND_TRACK, ToontownBattleGlobals.DROP_TRACK), Same, Same, 400, NA, Localizer.TheBrrrghTrackQuestDict),
    5002: (BR_TIER, 0, (TrackChoiceQuest, ToontownBattleGlobals.SOUND_TRACK, ToontownBattleGlobals.LURE_TRACK), Same, Same, 400, NA, Localizer.TheBrrrghTrackQuestDict),
    5003: (BR_TIER, 0, (TrackChoiceQuest, ToontownBattleGlobals.HEAL_TRACK, ToontownBattleGlobals.DROP_TRACK), Same, Same, 400, NA, Localizer.TheBrrrghTrackQuestDict),
    5004: (BR_TIER, 0, (TrackChoiceQuest, ToontownBattleGlobals.HEAL_TRACK, ToontownBattleGlobals.LURE_TRACK), Same, Same, 400, NA, Localizer.TheBrrrghTrackQuestDict),
    5005: (BR_TIER, 0, (TrackChoiceQuest, ToontownBattleGlobals.TRAP_TRACK, ToontownBattleGlobals.SOUND_TRACK), Same, Same, 400, NA, Localizer.TheBrrrghTrackQuestDict),
    5006: (BR_TIER, 0, (TrackChoiceQuest, ToontownBattleGlobals.TRAP_TRACK, ToontownBattleGlobals.HEAL_TRACK), Same, Same, 400, NA, Localizer.TheBrrrghTrackQuestDict),
    5007: (BR_TIER, 0, (TrackChoiceQuest, ToontownBattleGlobals.TRAP_TRACK, ToontownBattleGlobals.DROP_TRACK), Same, Same, 400, NA, Localizer.TheBrrrghTrackQuestDict),
    5008: (BR_TIER, 0, (TrackChoiceQuest, ToontownBattleGlobals.TRAP_TRACK, ToontownBattleGlobals.LURE_TRACK), Same, Same, 400, NA, Localizer.TheBrrrghTrackQuestDict),
    5020: (BR_TIER, 1, (CogQuest, Anywhere, 36, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5021: (BR_TIER, 1, (CogQuest, Anywhere, 38, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5022: (BR_TIER, 1, (CogQuest, Anywhere, 40, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5023: (BR_TIER, 1, (CogQuest, Anywhere, 42, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5024: (BR_TIER, 1, (CogQuest, Anywhere, 44, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5025: (BR_TIER, 1, (CogQuest, Anywhere, 46, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5026: (BR_TIER, 1, (CogQuest, Anywhere, 48, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5027: (BR_TIER, 1, (CogQuest, Anywhere, 50, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5028: (BR_TIER, 1, (CogQuest, Anywhere, 52, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5029: (BR_TIER, 1, (CogQuest, Anywhere, 54, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5030: (BR_TIER, 1, (CogLevelQuest, Anywhere, 25, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    5031: (BR_TIER, 1, (CogLevelQuest, Anywhere, 30, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    5032: (BR_TIER, 1, (CogLevelQuest, Anywhere, 35, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    5033: (BR_TIER, 1, (CogLevelQuest, Anywhere, 6, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    5034: (BR_TIER, 1, (CogLevelQuest, Anywhere, 10, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    5035: (BR_TIER, 1, (CogLevelQuest, Anywhere, 20, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    5036: (BR_TIER, 1, (CogLevelQuest, Anywhere, 2, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    5037: (BR_TIER, 1, (CogLevelQuest, Anywhere, 8, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    5038: (BR_TIER, 1, (CogLevelQuest, Anywhere, 10, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    5039: (BR_TIER, 1, (CogLevelQuest, Anywhere, 12, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    5040: (BR_TIER, 1, (CogQuest, ToontownGlobals.TheBrrrgh, 75, Any), Any, ToonHQ, NA, 5041, DefaultDialog),
    5041: (BR_TIER, 0, (DeliverItemQuest, 1000), Any, 3008, 1000, NA, DefaultDialog),
    5101: (BR_TIER + 1, 1, (CogQuest, ToontownGlobals.TheBrrrgh, 36, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5102: (BR_TIER + 1, 1, (CogQuest, ToontownGlobals.TheBrrrgh, 40, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5103: (BR_TIER + 1, 1, (CogQuest, ToontownGlobals.TheBrrrgh, 42, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5104: (BR_TIER + 1, 1, (CogQuest, Anywhere, 45, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5105: (BR_TIER + 1, 1, (CogQuest, Anywhere, 50, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5106: (BR_TIER + 1, 1, (CogQuest, Anywhere, 55, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5107: (BR_TIER + 1, 1, (CogQuest, Anywhere, 25, 'p'), Any, ToonHQ, Any, NA, DefaultDialog),
    5108: (BR_TIER + 1, 1, (CogQuest, Anywhere, 20, 'ym'), Any, ToonHQ, Any, NA, DefaultDialog),
    5109: (BR_TIER + 1, 1, (CogQuest, Anywhere, 20, 'mm'), Any, ToonHQ, Any, NA, DefaultDialog),
    5110: (BR_TIER + 1, 1, (CogQuest, Anywhere, 15, 'ds'), Any, ToonHQ, Any, NA, DefaultDialog),
    5111: (BR_TIER + 1, 1, (CogQuest, Anywhere, 15, 'hh'), Any, ToonHQ, Any, NA, DefaultDialog),
    5112: (BR_TIER + 1, 1, (CogQuest, Anywhere, 8, 'cr'), Any, ToonHQ, Any, NA, DefaultDialog),
    5113: (BR_TIER + 1, 1, (CogQuest, Anywhere, 25, 'tm'), Any, ToonHQ, Any, NA, DefaultDialog),
    5114: (BR_TIER + 1, 1, (CogQuest, Anywhere, 20, 'nd'), Any, ToonHQ, Any, NA, DefaultDialog),
    5115: (BR_TIER + 1, 1, (CogQuest, Anywhere, 20, 'gh'), Any, ToonHQ, Any, NA, DefaultDialog),
    5116: (BR_TIER + 1, 1, (CogQuest, Anywhere, 15, 'ms'), Any, ToonHQ, Any, NA, DefaultDialog),
    5117: (BR_TIER + 1, 1, (CogQuest, Anywhere, 15, 'tf'), Any, ToonHQ, Any, NA, DefaultDialog),
    5118: (BR_TIER + 1, 1, (CogQuest, Anywhere, 8, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    5119: (BR_TIER + 1, 1, (CogQuest, Anywhere, 25, 'pp'), Any, ToonHQ, Any, NA, DefaultDialog),
    5120: (BR_TIER + 1, 1, (CogQuest, Anywhere, 20, 'tw'), Any, ToonHQ, Any, NA, DefaultDialog),
    5121: (BR_TIER + 1, 1, (CogQuest, Anywhere, 20, 'bc'), Any, ToonHQ, Any, NA, DefaultDialog),
    5122: (BR_TIER + 1, 1, (CogQuest, Anywhere, 15, 'nc'), Any, ToonHQ, Any, NA, DefaultDialog),
    5123: (BR_TIER + 1, 1, (CogQuest, Anywhere, 15, 'mb'), Any, ToonHQ, Any, NA, DefaultDialog),
    5124: (BR_TIER + 1, 1, (CogQuest, Anywhere, 8, 'ls'), Any, ToonHQ, Any, NA, DefaultDialog),
    5125: (BR_TIER + 1, 1, (CogQuest, Anywhere, 25, 'b'), Any, ToonHQ, Any, NA, DefaultDialog),
    5126: (BR_TIER + 1, 1, (CogQuest, Anywhere, 20, 'dt'), Any, ToonHQ, Any, NA, DefaultDialog),
    5127: (BR_TIER + 1, 1, (CogQuest, Anywhere, 20, 'ac'), Any, ToonHQ, Any, NA, DefaultDialog),
    5128: (BR_TIER + 1, 1, (CogQuest, Anywhere, 15, 'bs'), Any, ToonHQ, Any, NA, DefaultDialog),
    5129: (BR_TIER + 1, 1, (CogQuest, Anywhere, 15, 'sd'), Any, ToonHQ, Any, NA, DefaultDialog),
    5130: (BR_TIER + 1, 1, (CogQuest, Anywhere, 8, 'le'), Any, ToonHQ, Any, NA, DefaultDialog),
    5131: (BR_TIER + 1, 1, (CogLevelQuest, Anywhere, 25, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    5132: (BR_TIER + 1, 1, (CogLevelQuest, Anywhere, 30, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    5133: (BR_TIER + 1, 1, (CogLevelQuest, Anywhere, 35, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    5134: (BR_TIER + 1, 1, (CogLevelQuest, Anywhere, 6, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    5135: (BR_TIER + 1, 1, (CogLevelQuest, Anywhere, 10, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    5136: (BR_TIER + 1, 1, (CogLevelQuest, Anywhere, 20, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    5137: (BR_TIER + 1, 1, (CogLevelQuest, Anywhere, 2, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    5138: (BR_TIER + 1, 1, (CogLevelQuest, Anywhere, 8, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    5139: (BR_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 32, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    5140: (BR_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 32, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    5141: (BR_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 32, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    5142: (BR_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 32, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    5143: (BR_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 40, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    5144: (BR_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 40, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    5145: (BR_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 40, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    5146: (BR_TIER + 1, 1, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 40, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    5147: (BR_TIER + 1, 1, (CogTrackQuest, Anywhere, 45, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    5148: (BR_TIER + 1, 1, (CogTrackQuest, Anywhere, 45, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    5149: (BR_TIER + 1, 1, (CogTrackQuest, Anywhere, 45, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    5150: (BR_TIER + 1, 1, (CogTrackQuest, Anywhere, 45, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    5151: (BR_TIER + 1, 1, (BuildingQuest, Anywhere, 8, Any, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    5152: (BR_TIER + 1, 1, (BuildingQuest, Anywhere, 2, Any, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    5153: (BR_TIER + 1, 1, (BuildingQuest, Anywhere, 5, Any, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    5154: (BR_TIER + 1, 1, (BuildingQuest, Anywhere, 6, Any, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    5155: (BR_TIER + 1, 1, (BuildingQuest, Anywhere, 2, 'm', 4), Any, ToonHQ, Any, NA, DefaultDialog),
    5156: (BR_TIER + 1, 1, (BuildingQuest, Anywhere, 2, 's', 4), Any, ToonHQ, Any, NA, DefaultDialog),
    5157: (BR_TIER + 1, 1, (BuildingQuest, Anywhere, 2, 'c', 4), Any, ToonHQ, Any, NA, DefaultDialog),
    5158: (BR_TIER + 1, 1, (BuildingQuest, Anywhere, 2, 'l', 4), Any, ToonHQ, Any, NA, DefaultDialog),
    5200: (BR_TIER + 1, 1, (VisitQuest,), Any, 3110, NA, (5201, 5261, 5262, 5263), Localizer.QuestDialogDict[5200]),
    5201: (BR_TIER + 1, 1, (RecoverItemQuest, Anywhere, 1, 3001, VeryHard, 'hh'), 3110, Same, 100, NA, Localizer.QuestDialogDict[5201]),
    5261: (BR_TIER + 1, 1, (RecoverItemQuest, Anywhere, 1, 3001, VeryHard, 'tf'), 3110, Same, 100, NA, Localizer.QuestDialogDict[5261]),
    5262: (BR_TIER + 1, 1, (RecoverItemQuest, Anywhere, 1, 3001, VeryHard, 'mb'), 3110, Same, 100, NA, Localizer.QuestDialogDict[5262]),
    5263: (BR_TIER + 1, 1, (RecoverItemQuest, Anywhere, 1, 3001, VeryHard, 'sd'), 3110, Same, 100, NA, Localizer.QuestDialogDict[5263]),
    5202: (BR_TIER + 1, 1, (VisitQuest,), Any, 3108, NA, 5203, Localizer.QuestDialogDict[5202]),
    5203: (BR_TIER + 1, 1, (RecoverItemQuest, ToontownGlobals.TheBrrrgh, 1, 3002, VeryHard, Any), 3108, Same, NA, 5204, Localizer.QuestDialogDict[5203]),
    5204: (BR_TIER + 1, 0, (VisitQuest,), Same, 3205, NA, 5205, Localizer.QuestDialogDict[5204]),
    5205: (BR_TIER + 1, 0, (RecoverItemQuest, ToontownGlobals.TheBrrrgh, 3, 3003, Hard, AnyFish), Same, Same, NA, 5206, Localizer.QuestDialogDict[5205]),
    5206: (BR_TIER + 1, 0, (VisitQuest,), Same, 3210, NA, 5207, Localizer.QuestDialogDict[5206]),
    5207: (BR_TIER + 1, 0, (BuildingQuest, Anywhere, 5, Any, 4), Same, Same, NA, 5208, Localizer.QuestDialogDict[5207]),
    5208: (BR_TIER + 1, 0, (VisitQuest,), Same, 3114, NA, 5209, Localizer.QuestDialogDict[5208]),
    5209: (BR_TIER + 1, 0, (CogLevelQuest, Anywhere, 20, 7), Same, Same, 204, NA, Localizer.QuestDialogDict[5209]),
    5210: (BR_TIER + 1, 1, (VisitQuest,), Any, 3206, NA, (5211, 5264, 5265, 5266), Localizer.QuestDialogDict[5210]),
    5211: (BR_TIER + 1, 1, (RecoverItemQuest, ToontownGlobals.TheBrrrgh, 1, 3004, Medium, 'le'), 3206, Same, NA, 5212, Localizer.QuestDialogDict[5211]),
    5264: (BR_TIER + 1, 1, (RecoverItemQuest, ToontownGlobals.TheBrrrgh, 1, 3004, Hard, 'ls'), 3206, Same, NA, 5212, Localizer.QuestDialogDict[5264]),
    5265: (BR_TIER + 1, 1, (RecoverItemQuest, ToontownGlobals.TheBrrrgh, 1, 3004, Hard, 'm'), 3206, Same, NA, 5212, Localizer.QuestDialogDict[5265]),
    5266: (BR_TIER + 1, 1, (RecoverItemQuest, ToontownGlobals.TheBrrrgh, 1, 3004, Hard, 'cr'), 3206, Same, NA, 5212, Localizer.QuestDialogDict[5266]),
    5212: (BR_TIER + 1, 0, (DeliverItemQuest, 3004), Same, 3111, NA, 5213, Localizer.QuestDialogDict[5212]),
    5213: (BR_TIER + 1, 0, (RecoverItemQuest, ToontownGlobals.TheBrrrgh, 10, 3005, Hard, Any), Same, Same, NA, 5214, Localizer.QuestDialogDict[5213]),
    5214: (BR_TIER + 1, 0, (VisitQuest,), Same, 3119, NA, 5215, Localizer.QuestDialogDict[5214]),
    5215: (BR_TIER + 1, 0, (CogLevelQuest, Anywhere, 10, 8), Same, Same, NA, 5216, Localizer.QuestDialogDict[5215]),
    5216: (BR_TIER + 1, 0, (DeliverItemQuest, 3006), Same, 3206, 704, NA, Localizer.QuestDialogDict[5216]),
    5217: (BR_TIER + 1, 1, (VisitQuest,), Any, 3113, NA, 5218, Localizer.QuestDialogDict[5217]),
    5218: (BR_TIER + 1, 1, (CogQuest, Anywhere, 10, 'm'), 3113, Same, NA, 5219, Localizer.QuestDialogDict[5218]),
    5219: (BR_TIER + 1, 0, (CogQuest, Anywhere, 10, 'cr'), Same, Same, NA, 5220, Localizer.QuestDialogDict[5219]),
    5220: (BR_TIER + 1, 0, (CogQuest, Anywhere, 10, 'ls'), Same, Same, NA, 5221, Localizer.QuestDialogDict[5220]),
    5221: (BR_TIER + 1, 0, (VisitQuest,), Same, 3211, NA, 5222, Localizer.QuestDialogDict[5221]),
    5222: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 2, 3007, Hard, AnyFish), Same, Same, NA, 5223, Localizer.QuestDialogDict[5222]),
    5223: (BR_TIER + 1, 0, (DeliverItemQuest, 3008), Same, 3113, NA, 5224, Localizer.QuestDialogDict[5223]),
    5224: (BR_TIER + 1, 0, (CogQuest, Anywhere, 5, 'le'), Same, Same, 502, NA, Localizer.QuestDialogDict[5224]),
    5225: (BR_TIER + 1, 1, (VisitQuest,), Any, 3106, NA, 5226, Localizer.QuestDialogDict[5225]),
    5226: (BR_TIER + 1, 1, (BuildingQuest, Anywhere, 3, 'm', 4), 3106, Same, NA, 5227, Localizer.QuestDialogDict[5226]),
    5227: (BR_TIER + 1, 0, (VisitQuest,), Same, 3208, NA, 5228, Localizer.QuestDialogDict[5227]),
    5228: (BR_TIER + 1, 0, (DeliverItemQuest, 3009), Same, 3207, NA, (5229, 5267, 5268, 5269), Localizer.QuestDialogDict[5228]),
    5229: (BR_TIER + 1, 0, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 8, 'm'), Same, Same, NA, 5230, Localizer.QuestDialogDict[5229]),
    5267: (BR_TIER + 1, 0, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 8, 's'), Same, Same, NA, 5230, Localizer.QuestDialogDict[5267]),
    5268: (BR_TIER + 1, 0, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 8, 'l'), Same, Same, NA, 5230, Localizer.QuestDialogDict[5268]),
    5269: (BR_TIER + 1, 0, (CogTrackQuest, ToontownGlobals.TheBrrrgh, 8, 'c'), Same, Same, NA, (5230, 5270, 5271, 5272), Localizer.QuestDialogDict[5269]),
    5230: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3010, Hard, 'rb'), Same, Same, NA, 5231, Localizer.QuestDialogDict[5230]),
    5270: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3010, Hard, 'tbc'), Same, Same, NA, 5231, Localizer.QuestDialogDict[5270]),
    5271: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3010, Hard, 'mh'), Same, Same, NA, 5231, Localizer.QuestDialogDict[5271]),
    5272: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3010, Medium, 'bw'), Same, Same, NA, 5231, Localizer.QuestDialogDict[5272]),
    5231: (BR_TIER + 1, 0, (DeliverItemQuest, 3010), Same, 3208, NA, 5232, Localizer.QuestDialogDict[5231]),
    5232: (BR_TIER + 1, 0, (VisitQuest,), Same, 3106, NA, 5233, Localizer.QuestDialogDict[5232]),
    5233: (BR_TIER + 1, 0, (DeliverItemQuest, 3011), Same, 3208, 304, NA, Localizer.QuestDialogDict[5233]),
    903: (BR_TIER + 2, 1, (VisitQuest,), Any, 3112, NA, (5234, 5278), Localizer.QuestDialogDict[903]),
    5234: (BR_TIER + 2, 1, (RecoverItemQuest, Anywhere, 6, 3012, Medium, 'tbc'), 3112, Same, NA, (5235, 5279), Localizer.QuestDialogDict[5234]),
    5278: (BR_TIER + 2, 1, (RecoverItemQuest, Anywhere, 6, 3022, Medium, 'mh'), 3112, Same, NA, (5235, 5279), Localizer.QuestDialogDict[5278]),
    5235: (BR_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 3013, Hard, 'rb'), Same, Same, NA, 5236, Localizer.QuestDialogDict[5235]),
    5279: (BR_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 3013, Medium, 'bw'), Same, Same, NA, 5236, Localizer.QuestDialogDict[5279]),
    5236: (BR_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 3014, VeryHard, AnyFish), Same, Same, NA, 5237, Localizer.QuestDialogDict[5236]),
    5237: (BR_TIER + 2, 0, (VisitQuest,), Same, 3128, NA, (5238, 5280), Localizer.QuestDialogDict[5237]),
    5238: (BR_TIER + 2, 0, (RecoverItemQuest, Anywhere, 10, 3015, VeryEasy, 'mh'), Same, Same, NA, 5239, Localizer.QuestDialogDict[5238]),
    5280: (BR_TIER + 2, 0, (RecoverItemQuest, Anywhere, 10, 3015, VeryEasy, 'tbc'), Same, Same, NA, 5239, Localizer.QuestDialogDict[5280]),
    5239: (BR_TIER + 2, 0, (DeliverItemQuest, 3015), Same, 3112, NA, (5240, 5281), Localizer.QuestDialogDict[5239]),
    5240: (BR_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 3016, Hard, 'bw'), Same, Same, NA, 5241, Localizer.QuestDialogDict[5240]),
    5281: (BR_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 3023, Hard, 'mh'), Same, Same, NA, 5241, Localizer.QuestDialogDict[5281]),
    5241: (BR_TIER + 2, 0, (BuildingQuest, Anywhere, 20, Any, 4), Same, Same, NA, 5242, Localizer.QuestDialogDict[5241]),
    5242: (BR_TIER + 2, 0, (RecoverItemQuest, Anywhere, 1, 3014, VeryHard, AnyFish), Same, Same, 900, NA, Localizer.QuestDialogDict[5242]),
    5243: (BR_TIER + 1, 1, (VisitQuest,), Any, 3217, NA, 5244, Localizer.QuestDialogDict[5243]),
    5244: (BR_TIER + 1, 1, (RecoverItemQuest, Anywhere, 1, 2007, VeryHard, 'mm'), 3217, Same, NA, 5245, Localizer.QuestDialogDict[5244]),
    5245: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3017, Hard, AnyFish), Same, Same, NA, 5246, Localizer.QuestDialogDict[5245]),
    5246: (BR_TIER + 1, 0, (BuildingQuest, ToontownGlobals.TheBrrrgh, 5, Any, 1), Same, Same, 101, NA, Localizer.QuestDialogDict[5246]),
    5251: (BR_TIER + 1, 1, (VisitQuest,), Any, 3134, NA, 5252, Localizer.QuestDialogDict[5251]),
    5252: (BR_TIER + 1, 1, (RecoverItemQuest, Anywhere, 1, 3019, VeryHard, Any), 3134, Same, NA, (5253, 5273, 5274, 5275), Localizer.QuestDialogDict[5252]),
    5253: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3020, VeryHard, 'cr'), Same, Same, NA, (5254, 5282, 5283, 5284), Localizer.QuestDialogDict[5253]),
    5273: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3020, VeryHard, 'm'), Same, Same, NA, (5254, 5282, 5283, 5284), Localizer.QuestDialogDict[5273]),
    5274: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3020, VeryHard, 'ls'), Same, Same, NA, (5254, 5282, 5283, 5284), Localizer.QuestDialogDict[5274]),
    5275: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3020, Hard, 'le'), Same, Same, NA, (5254, 5282, 5283, 5284), Localizer.QuestDialogDict[5275]),
    5254: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3021, VeryHard, 'mh'), Same, Same, 102, NA, Localizer.QuestDialogDict[5254]),
    5282: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3021, VeryHard, 'tbc'), Same, Same, 102, NA, Localizer.QuestDialogDict[5282]),
    5283: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3021, VeryHard, 'rb'), Same, Same, 102, NA, Localizer.QuestDialogDict[5283]),
    5284: (BR_TIER + 1, 0, (RecoverItemQuest, Anywhere, 1, 3021, Hard, 'bw'), Same, Same, 102, NA, Localizer.QuestDialogDict[5284]),
    5255: (BR_TIER + 1, 1, (VisitQuest,), Any, 3228, NA, (5256, 5276), Localizer.QuestDialogDict[5255]),
    5256: (BR_TIER + 1, 1, (CogTrackQuest, Anywhere, 45, 'c'), 3228, Same, NA, (5257, 5277), Localizer.QuestDialogDict[5256]),
    5276: (BR_TIER + 1, 1, (CogTrackQuest, Anywhere, 40, 'l'), 3228, Same, NA, (5257, 5277), Localizer.QuestDialogDict[5276]),
    5257: (BR_TIER + 1, 0, (CogTrackQuest, Anywhere, 45, 's'), Same, Same, 100, NA, Localizer.QuestDialogDict[5257]),
    5277: (BR_TIER + 1, 0, (CogTrackQuest, Anywhere, 45, 'm'), Same, Same, 100, NA, Localizer.QuestDialogDict[5277]),
    5500: (BR_TIER + 1, 1, (CogQuest, ToontownGlobals.TheBrrrgh, 75, Any), Any, ToonHQ, NA, 5501, DefaultDialog),
    5501: (BR_TIER + 1, 0, (DeliverItemQuest, 1000), Any, 3008, 1000, NA, DefaultDialog),
    5320: (BR_TIER + 2, 1, (CogQuest, Anywhere, 36, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5321: (BR_TIER + 2, 1, (CogQuest, Anywhere, 38, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5322: (BR_TIER + 2, 1, (CogQuest, Anywhere, 40, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5323: (BR_TIER + 2, 1, (CogQuest, Anywhere, 42, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5324: (BR_TIER + 2, 1, (CogQuest, Anywhere, 44, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5325: (BR_TIER + 2, 1, (CogQuest, Anywhere, 46, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5326: (BR_TIER + 2, 1, (CogQuest, Anywhere, 48, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5327: (BR_TIER + 2, 1, (CogQuest, Anywhere, 53, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5328: (BR_TIER + 2, 1, (CogQuest, Anywhere, 52, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5329: (BR_TIER + 2, 1, (CogQuest, Anywhere, 54, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    5330: (BR_TIER + 2, 1, (CogLevelQuest, Anywhere, 25, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    5331: (BR_TIER + 2, 1, (CogLevelQuest, Anywhere, 30, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    5332: (BR_TIER + 2, 1, (CogLevelQuest, Anywhere, 35, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    5333: (BR_TIER + 2, 1, (CogLevelQuest, Anywhere, 6, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    5334: (BR_TIER + 2, 1, (CogLevelQuest, Anywhere, 10, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    5335: (BR_TIER + 2, 1, (CogLevelQuest, Anywhere, 20, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    5336: (BR_TIER + 2, 1, (CogLevelQuest, Anywhere, 2, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    5337: (BR_TIER + 2, 1, (CogLevelQuest, Anywhere, 8, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    5338: (BR_TIER + 2, 1, (CogLevelQuest, Anywhere, 10, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    5339: (BR_TIER + 2, 1, (CogLevelQuest, Anywhere, 12, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    5340: (BR_TIER + 2, 1, (CogQuest, ToontownGlobals.TheBrrrgh, 75, Any), Any, ToonHQ, NA, 5341, DefaultDialog),
    5341: (BR_TIER + 2, 0, (DeliverItemQuest, 1000), Any, 3008, 1000, NA, DefaultDialog),
    6101: (DL_TIER, 1, (CogQuest, ToontownGlobals.DonaldsDreamland, 60, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    6102: (DL_TIER, 1, (CogQuest, ToontownGlobals.DonaldsDreamland, 65, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    6103: (DL_TIER, 1, (CogQuest, ToontownGlobals.DonaldsDreamland, 70, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    6104: (DL_TIER, 1, (CogQuest, Anywhere, 80, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    6105: (DL_TIER, 1, (CogQuest, Anywhere, 90, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    6106: (DL_TIER, 1, (CogQuest, Anywhere, 100, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    6107: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'ym'), Any, ToonHQ, Any, NA, DefaultDialog),
    6108: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'mm'), Any, ToonHQ, Any, NA, DefaultDialog),
    6109: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'ds'), Any, ToonHQ, Any, NA, DefaultDialog),
    6110: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'hh'), Any, ToonHQ, Any, NA, DefaultDialog),
    6111: (DL_TIER, 1, (CogQuest, Anywhere, 15, 'cr'), Any, ToonHQ, Any, NA, DefaultDialog),
    6112: (DL_TIER, 1, (CogQuest, Anywhere, 8, 'tbc'), Any, ToonHQ, Any, NA, DefaultDialog),
    6113: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'nd'), Any, ToonHQ, Any, NA, DefaultDialog),
    6114: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'gh'), Any, ToonHQ, Any, NA, DefaultDialog),
    6115: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'ms'), Any, ToonHQ, Any, NA, DefaultDialog),
    6116: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'tf'), Any, ToonHQ, Any, NA, DefaultDialog),
    6117: (DL_TIER, 1, (CogQuest, Anywhere, 15, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    6118: (DL_TIER, 1, (CogQuest, Anywhere, 8, 'mh'), Any, ToonHQ, Any, NA, DefaultDialog),
    6119: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'tw'), Any, ToonHQ, Any, NA, DefaultDialog),
    6120: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'bc'), Any, ToonHQ, Any, NA, DefaultDialog),
    6121: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'nc'), Any, ToonHQ, Any, NA, DefaultDialog),
    6122: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'mb'), Any, ToonHQ, Any, NA, DefaultDialog),
    6123: (DL_TIER, 1, (CogQuest, Anywhere, 15, 'ls'), Any, ToonHQ, Any, NA, DefaultDialog),
    6124: (DL_TIER, 1, (CogQuest, Anywhere, 8, 'rb'), Any, ToonHQ, Any, NA, DefaultDialog),
    6125: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'dt'), Any, ToonHQ, Any, NA, DefaultDialog),
    6126: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'ac'), Any, ToonHQ, Any, NA, DefaultDialog),
    6127: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'bs'), Any, ToonHQ, Any, NA, DefaultDialog),
    6128: (DL_TIER, 1, (CogQuest, Anywhere, 25, 'sd'), Any, ToonHQ, Any, NA, DefaultDialog),
    6129: (DL_TIER, 1, (CogQuest, Anywhere, 15, 'le'), Any, ToonHQ, Any, NA, DefaultDialog),
    6130: (DL_TIER, 1, (CogQuest, Anywhere, 8, 'bw'), Any, ToonHQ, Any, NA, DefaultDialog),
    6131: (DL_TIER, 1, (CogLevelQuest, Anywhere, 50, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    6132: (DL_TIER, 1, (CogLevelQuest, Anywhere, 40, 6), Any, ToonHQ, Any, NA, DefaultDialog),
    6133: (DL_TIER, 1, (CogLevelQuest, Anywhere, 35, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    6134: (DL_TIER, 1, (CogLevelQuest, Anywhere, 30, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    6135: (DL_TIER, 1, (CogLevelQuest, Anywhere, 25, 9), Any, ToonHQ, Any, NA, DefaultDialog),
    6136: (DL_TIER, 1, (CogLevelQuest, Anywhere, 20, 9), Any, ToonHQ, Any, NA, DefaultDialog),
    6137: (DL_TIER, 1, (CogLevelQuest, Anywhere, 15, 9), Any, ToonHQ, Any, NA, DefaultDialog),
    6138: (DL_TIER, 1, (CogLevelQuest, Anywhere, 10, 10), Any, ToonHQ, Any, NA, DefaultDialog),
    6139: (DL_TIER, 1, (CogTrackQuest, ToontownGlobals.DonaldsDreamland, 50, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    6140: (DL_TIER, 1, (CogTrackQuest, ToontownGlobals.DonaldsDreamland, 50, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    6141: (DL_TIER, 1, (CogTrackQuest, ToontownGlobals.DonaldsDreamland, 50, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    6142: (DL_TIER, 1, (CogTrackQuest, ToontownGlobals.DonaldsDreamland, 50, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    6143: (DL_TIER, 1, (CogTrackQuest, ToontownGlobals.DonaldsDreamland, 55, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    6144: (DL_TIER, 1, (CogTrackQuest, ToontownGlobals.DonaldsDreamland, 55, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    6145: (DL_TIER, 1, (CogTrackQuest, ToontownGlobals.DonaldsDreamland, 55, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    6146: (DL_TIER, 1, (CogTrackQuest, ToontownGlobals.DonaldsDreamland, 55, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    6147: (DL_TIER, 1, (CogTrackQuest, Anywhere, 70, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    6148: (DL_TIER, 1, (CogTrackQuest, Anywhere, 70, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    6149: (DL_TIER, 1, (CogTrackQuest, Anywhere, 70, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    6150: (DL_TIER, 1, (CogTrackQuest, Anywhere, 70, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    6151: (DL_TIER, 1, (BuildingQuest, Anywhere, 10, Any, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    6152: (DL_TIER, 1, (BuildingQuest, Anywhere, 6, Any, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    6153: (DL_TIER, 1, (BuildingQuest, Anywhere, 8, Any, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    6154: (DL_TIER, 1, (BuildingQuest, Anywhere, 6, Any, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    6155: (DL_TIER, 1, (BuildingQuest, Anywhere, 2, 'm', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    6156: (DL_TIER, 1, (BuildingQuest, Anywhere, 2, 's', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    6157: (DL_TIER, 1, (BuildingQuest, Anywhere, 2, 'c', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    6158: (DL_TIER, 1, (BuildingQuest, Anywhere, 2, 'l', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    7101: (DL_TIER + 1, 1, (CogQuest, Anywhere, 120, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    7102: (DL_TIER + 1, 1, (CogQuest, Anywhere, 130, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    7103: (DL_TIER + 1, 1, (CogQuest, Anywhere, 140, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    7104: (DL_TIER + 1, 1, (CogQuest, Anywhere, 160, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    7105: (DL_TIER + 1, 1, (CogQuest, Anywhere, 180, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    7106: (DL_TIER + 1, 1, (CogQuest, Anywhere, 200, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    7107: (DL_TIER + 1, 1, (CogQuest, Anywhere, 70, 'ym'), Any, ToonHQ, Any, NA, DefaultDialog),
    7108: (DL_TIER + 1, 1, (CogQuest, Anywhere, 60, 'mm'), Any, ToonHQ, Any, NA, DefaultDialog),
    7109: (DL_TIER + 1, 1, (CogQuest, Anywhere, 50, 'ds'), Any, ToonHQ, Any, NA, DefaultDialog),
    7110: (DL_TIER + 1, 1, (CogQuest, Anywhere, 50, 'hh'), Any, ToonHQ, Any, NA, DefaultDialog),
    7111: (DL_TIER + 1, 1, (CogQuest, Anywhere, 30, 'cr'), Any, ToonHQ, Any, NA, DefaultDialog),
    7112: (DL_TIER + 1, 1, (CogQuest, Anywhere, 20, 'tbc'), Any, ToonHQ, Any, NA, DefaultDialog),
    7113: (DL_TIER + 1, 1, (CogQuest, Anywhere, 70, 'nd'), Any, ToonHQ, Any, NA, DefaultDialog),
    7114: (DL_TIER + 1, 1, (CogQuest, Anywhere, 60, 'gh'), Any, ToonHQ, Any, NA, DefaultDialog),
    7115: (DL_TIER + 1, 1, (CogQuest, Anywhere, 50, 'ms'), Any, ToonHQ, Any, NA, DefaultDialog),
    7116: (DL_TIER + 1, 1, (CogQuest, Anywhere, 50, 'tf'), Any, ToonHQ, Any, NA, DefaultDialog),
    7117: (DL_TIER + 1, 1, (CogQuest, Anywhere, 30, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    7118: (DL_TIER + 1, 1, (CogQuest, Anywhere, 20, 'mh'), Any, ToonHQ, Any, NA, DefaultDialog),
    7119: (DL_TIER + 1, 1, (CogQuest, Anywhere, 70, 'tw'), Any, ToonHQ, Any, NA, DefaultDialog),
    7120: (DL_TIER + 1, 1, (CogQuest, Anywhere, 60, 'bc'), Any, ToonHQ, Any, NA, DefaultDialog),
    7121: (DL_TIER + 1, 1, (CogQuest, Anywhere, 50, 'nc'), Any, ToonHQ, Any, NA, DefaultDialog),
    7122: (DL_TIER + 1, 1, (CogQuest, Anywhere, 50, 'mb'), Any, ToonHQ, Any, NA, DefaultDialog),
    7123: (DL_TIER + 1, 1, (CogQuest, Anywhere, 30, 'ls'), Any, ToonHQ, Any, NA, DefaultDialog),
    7124: (DL_TIER + 1, 1, (CogQuest, Anywhere, 20, 'rb'), Any, ToonHQ, Any, NA, DefaultDialog),
    7125: (DL_TIER + 1, 1, (CogQuest, Anywhere, 70, 'dt'), Any, ToonHQ, Any, NA, DefaultDialog),
    7126: (DL_TIER + 1, 1, (CogQuest, Anywhere, 60, 'ac'), Any, ToonHQ, Any, NA, DefaultDialog),
    7127: (DL_TIER + 1, 1, (CogQuest, Anywhere, 50, 'bs'), Any, ToonHQ, Any, NA, DefaultDialog),
    7128: (DL_TIER + 1, 1, (CogQuest, Anywhere, 50, 'sd'), Any, ToonHQ, Any, NA, DefaultDialog),
    7129: (DL_TIER + 1, 1, (CogQuest, Anywhere, 30, 'le'), Any, ToonHQ, Any, NA, DefaultDialog),
    7130: (DL_TIER + 1, 1, (CogQuest, Anywhere, 20, 'bw'), Any, ToonHQ, Any, NA, DefaultDialog),
    7131: (DL_TIER + 1, 1, (CogLevelQuest, Anywhere, 100, 7), Any, ToonHQ, Any, NA, DefaultDialog),
    7132: (DL_TIER + 1, 1, (CogLevelQuest, Anywhere, 80, 8), Any, ToonHQ, Any, NA, DefaultDialog),
    7133: (DL_TIER + 1, 1, (CogLevelQuest, Anywhere, 60, 9), Any, ToonHQ, Any, NA, DefaultDialog),
    7134: (DL_TIER + 1, 1, (CogLevelQuest, Anywhere, 70, 9), Any, ToonHQ, Any, NA, DefaultDialog),
    7135: (DL_TIER + 1, 1, (CogLevelQuest, Anywhere, 40, 10), Any, ToonHQ, Any, NA, DefaultDialog),
    7136: (DL_TIER + 1, 1, (CogLevelQuest, Anywhere, 50, 10), Any, ToonHQ, Any, NA, DefaultDialog),
    7137: (DL_TIER + 1, 1, (CogLevelQuest, Anywhere, 20, 11), Any, ToonHQ, Any, NA, DefaultDialog),
    7138: (DL_TIER + 1, 1, (CogLevelQuest, Anywhere, 30, 11), Any, ToonHQ, Any, NA, DefaultDialog),
    7139: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 100, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    7140: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 100, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    7141: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 100, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    7142: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 100, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    7143: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 120, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    7144: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 120, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    7145: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 120, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    7146: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 120, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    7147: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 140, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    7148: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 140, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    7149: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 140, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    7150: (DL_TIER + 1, 1, (CogTrackQuest, Anywhere, 140, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    7151: (DL_TIER + 1, 1, (BuildingQuest, Anywhere, 20, Any, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    7152: (DL_TIER + 1, 1, (BuildingQuest, Anywhere, 10, Any, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    7153: (DL_TIER + 1, 1, (BuildingQuest, Anywhere, 10, Any, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    7154: (DL_TIER + 1, 1, (BuildingQuest, Anywhere, 10, Any, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    7155: (DL_TIER + 1, 1, (BuildingQuest, Anywhere, 5, 'm', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    7156: (DL_TIER + 1, 1, (BuildingQuest, Anywhere, 5, 's', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    7157: (DL_TIER + 1, 1, (BuildingQuest, Anywhere, 5, 'c', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    7158: (DL_TIER + 1, 1, (BuildingQuest, Anywhere, 5, 'l', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    7500: (DL_TIER + 1, 1, (CogQuest, ToontownGlobals.DonaldsDreamland, 100, Any), Any, ToonHQ, NA, 7501, DefaultDialog),
    7501: (DL_TIER + 1, 0, (DeliverItemQuest, 1000), Any, 9010, 1000, NA, DefaultDialog),
    8101: (DL_TIER + 2, 1, (CogQuest, Anywhere, 240, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    8102: (DL_TIER + 2, 1, (CogQuest, Anywhere, 260, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    8103: (DL_TIER + 2, 1, (CogQuest, Anywhere, 280, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    8104: (DL_TIER + 2, 1, (CogQuest, Anywhere, 320, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    8105: (DL_TIER + 2, 1, (CogQuest, Anywhere, 360, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    8106: (DL_TIER + 2, 1, (CogQuest, Anywhere, 400, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    8107: (DL_TIER + 2, 1, (CogQuest, Anywhere, 140, 'ym'), Any, ToonHQ, Any, NA, DefaultDialog),
    8108: (DL_TIER + 2, 1, (CogQuest, Anywhere, 120, 'mm'), Any, ToonHQ, Any, NA, DefaultDialog),
    8109: (DL_TIER + 2, 1, (CogQuest, Anywhere, 100, 'ds'), Any, ToonHQ, Any, NA, DefaultDialog),
    8110: (DL_TIER + 2, 1, (CogQuest, Anywhere, 100, 'hh'), Any, ToonHQ, Any, NA, DefaultDialog),
    8111: (DL_TIER + 2, 1, (CogQuest, Anywhere, 60, 'cr'), Any, ToonHQ, Any, NA, DefaultDialog),
    8112: (DL_TIER + 2, 1, (CogQuest, Anywhere, 40, 'tbc'), Any, ToonHQ, Any, NA, DefaultDialog),
    8113: (DL_TIER + 2, 1, (CogQuest, Anywhere, 140, 'nd'), Any, ToonHQ, Any, NA, DefaultDialog),
    8114: (DL_TIER + 2, 1, (CogQuest, Anywhere, 120, 'gh'), Any, ToonHQ, Any, NA, DefaultDialog),
    8115: (DL_TIER + 2, 1, (CogQuest, Anywhere, 100, 'ms'), Any, ToonHQ, Any, NA, DefaultDialog),
    8116: (DL_TIER + 2, 1, (CogQuest, Anywhere, 100, 'tf'), Any, ToonHQ, Any, NA, DefaultDialog),
    8117: (DL_TIER + 2, 1, (CogQuest, Anywhere, 60, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    8118: (DL_TIER + 2, 1, (CogQuest, Anywhere, 40, 'mh'), Any, ToonHQ, Any, NA, DefaultDialog),
    8119: (DL_TIER + 2, 1, (CogQuest, Anywhere, 140, 'tw'), Any, ToonHQ, Any, NA, DefaultDialog),
    8120: (DL_TIER + 2, 1, (CogQuest, Anywhere, 120, 'bc'), Any, ToonHQ, Any, NA, DefaultDialog),
    8121: (DL_TIER + 2, 1, (CogQuest, Anywhere, 100, 'nc'), Any, ToonHQ, Any, NA, DefaultDialog),
    8122: (DL_TIER + 2, 1, (CogQuest, Anywhere, 100, 'mb'), Any, ToonHQ, Any, NA, DefaultDialog),
    8123: (DL_TIER + 2, 1, (CogQuest, Anywhere, 60, 'ls'), Any, ToonHQ, Any, NA, DefaultDialog),
    8124: (DL_TIER + 2, 1, (CogQuest, Anywhere, 40, 'rb'), Any, ToonHQ, Any, NA, DefaultDialog),
    8125: (DL_TIER + 2, 1, (CogQuest, Anywhere, 140, 'dt'), Any, ToonHQ, Any, NA, DefaultDialog),
    8126: (DL_TIER + 2, 1, (CogQuest, Anywhere, 120, 'ac'), Any, ToonHQ, Any, NA, DefaultDialog),
    8127: (DL_TIER + 2, 1, (CogQuest, Anywhere, 100, 'bs'), Any, ToonHQ, Any, NA, DefaultDialog),
    8128: (DL_TIER + 2, 1, (CogQuest, Anywhere, 100, 'sd'), Any, ToonHQ, Any, NA, DefaultDialog),
    8129: (DL_TIER + 2, 1, (CogQuest, Anywhere, 60, 'le'), Any, ToonHQ, Any, NA, DefaultDialog),
    8130: (DL_TIER + 2, 1, (CogQuest, Anywhere, 40, 'bw'), Any, ToonHQ, Any, NA, DefaultDialog),
    8131: (DL_TIER + 2, 1, (CogLevelQuest, Anywhere, 160, 9), Any, ToonHQ, Any, NA, DefaultDialog),
    8132: (DL_TIER + 2, 1, (CogLevelQuest, Anywhere, 200, 9), Any, ToonHQ, Any, NA, DefaultDialog),
    8133: (DL_TIER + 2, 1, (CogLevelQuest, Anywhere, 120, 10), Any, ToonHQ, Any, NA, DefaultDialog),
    8134: (DL_TIER + 2, 1, (CogLevelQuest, Anywhere, 140, 10), Any, ToonHQ, Any, NA, DefaultDialog),
    8135: (DL_TIER + 2, 1, (CogLevelQuest, Anywhere, 80, 11), Any, ToonHQ, Any, NA, DefaultDialog),
    8136: (DL_TIER + 2, 1, (CogLevelQuest, Anywhere, 100, 11), Any, ToonHQ, Any, NA, DefaultDialog),
    8137: (DL_TIER + 2, 1, (CogLevelQuest, Anywhere, 40, 12), Any, ToonHQ, Any, NA, DefaultDialog),
    8138: (DL_TIER + 2, 1, (CogLevelQuest, Anywhere, 60, 12), Any, ToonHQ, Any, NA, DefaultDialog),
    8139: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 200, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    8140: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 200, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    8141: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 200, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    8142: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 200, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    8143: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 250, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    8144: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 250, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    8145: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 250, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    8146: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 250, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    8147: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 300, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    8148: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 300, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    8149: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 300, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    8150: (DL_TIER + 2, 1, (CogTrackQuest, Anywhere, 300, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    8151: (DL_TIER + 2, 1, (BuildingQuest, Anywhere, 40, Any, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    8152: (DL_TIER + 2, 1, (BuildingQuest, Anywhere, 20, Any, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    8153: (DL_TIER + 2, 1, (BuildingQuest, Anywhere, 20, Any, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    8154: (DL_TIER + 2, 1, (BuildingQuest, Anywhere, 20, Any, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    8155: (DL_TIER + 2, 1, (BuildingQuest, Anywhere, 10, 'm', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    8156: (DL_TIER + 2, 1, (BuildingQuest, Anywhere, 10, 's', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    8157: (DL_TIER + 2, 1, (BuildingQuest, Anywhere, 10, 'c', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    8158: (DL_TIER + 2, 1, (BuildingQuest, Anywhere, 10, 'l', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    9101: (DL_TIER + 3, 1, (CogQuest, Anywhere, 500, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    9102: (DL_TIER + 3, 1, (CogQuest, Anywhere, 600, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    9103: (DL_TIER + 3, 1, (CogQuest, Anywhere, 700, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    9104: (DL_TIER + 3, 1, (CogQuest, Anywhere, 800, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    9105: (DL_TIER + 3, 1, (CogQuest, Anywhere, 900, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    9106: (DL_TIER + 3, 1, (CogQuest, Anywhere, 1000, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    9107: (DL_TIER + 3, 1, (CogQuest, Anywhere, 300, 'ym'), Any, ToonHQ, Any, NA, DefaultDialog),
    9108: (DL_TIER + 3, 1, (CogQuest, Anywhere, 250, 'mm'), Any, ToonHQ, Any, NA, DefaultDialog),
    9109: (DL_TIER + 3, 1, (CogQuest, Anywhere, 200, 'ds'), Any, ToonHQ, Any, NA, DefaultDialog),
    9110: (DL_TIER + 3, 1, (CogQuest, Anywhere, 200, 'hh'), Any, ToonHQ, Any, NA, DefaultDialog),
    9111: (DL_TIER + 3, 1, (CogQuest, Anywhere, 120, 'cr'), Any, ToonHQ, Any, NA, DefaultDialog),
    9112: (DL_TIER + 3, 1, (CogQuest, Anywhere, 80, 'tbc'), Any, ToonHQ, Any, NA, DefaultDialog),
    9113: (DL_TIER + 3, 1, (CogQuest, Anywhere, 280, 'nd'), Any, ToonHQ, Any, NA, DefaultDialog),
    9114: (DL_TIER + 3, 1, (CogQuest, Anywhere, 240, 'gh'), Any, ToonHQ, Any, NA, DefaultDialog),
    9115: (DL_TIER + 3, 1, (CogQuest, Anywhere, 200, 'ms'), Any, ToonHQ, Any, NA, DefaultDialog),
    9116: (DL_TIER + 3, 1, (CogQuest, Anywhere, 200, 'tf'), Any, ToonHQ, Any, NA, DefaultDialog),
    9117: (DL_TIER + 3, 1, (CogQuest, Anywhere, 120, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    9118: (DL_TIER + 3, 1, (CogQuest, Anywhere, 80, 'mh'), Any, ToonHQ, Any, NA, DefaultDialog),
    9119: (DL_TIER + 3, 1, (CogQuest, Anywhere, 280, 'tw'), Any, ToonHQ, Any, NA, DefaultDialog),
    9120: (DL_TIER + 3, 1, (CogQuest, Anywhere, 240, 'bc'), Any, ToonHQ, Any, NA, DefaultDialog),
    9121: (DL_TIER + 3, 1, (CogQuest, Anywhere, 200, 'nc'), Any, ToonHQ, Any, NA, DefaultDialog),
    9122: (DL_TIER + 3, 1, (CogQuest, Anywhere, 200, 'mb'), Any, ToonHQ, Any, NA, DefaultDialog),
    9123: (DL_TIER + 3, 1, (CogQuest, Anywhere, 120, 'ls'), Any, ToonHQ, Any, NA, DefaultDialog),
    9124: (DL_TIER + 3, 1, (CogQuest, Anywhere, 80, 'rb'), Any, ToonHQ, Any, NA, DefaultDialog),
    9125: (DL_TIER + 3, 1, (CogQuest, Anywhere, 280, 'dt'), Any, ToonHQ, Any, NA, DefaultDialog),
    9126: (DL_TIER + 3, 1, (CogQuest, Anywhere, 240, 'ac'), Any, ToonHQ, Any, NA, DefaultDialog),
    9127: (DL_TIER + 3, 1, (CogQuest, Anywhere, 200, 'bs'), Any, ToonHQ, Any, NA, DefaultDialog),
    9128: (DL_TIER + 3, 1, (CogQuest, Anywhere, 200, 'sd'), Any, ToonHQ, Any, NA, DefaultDialog),
    9129: (DL_TIER + 3, 1, (CogQuest, Anywhere, 120, 'le'), Any, ToonHQ, Any, NA, DefaultDialog),
    9130: (DL_TIER + 3, 1, (CogQuest, Anywhere, 80, 'bw'), Any, ToonHQ, Any, NA, DefaultDialog),
    9131: (DL_TIER + 3, 1, (CogLevelQuest, Anywhere, 320, 9), Any, ToonHQ, Any, NA, DefaultDialog),
    9132: (DL_TIER + 3, 1, (CogLevelQuest, Anywhere, 400, 9), Any, ToonHQ, Any, NA, DefaultDialog),
    9133: (DL_TIER + 3, 1, (CogLevelQuest, Anywhere, 240, 10), Any, ToonHQ, Any, NA, DefaultDialog),
    9134: (DL_TIER + 3, 1, (CogLevelQuest, Anywhere, 280, 10), Any, ToonHQ, Any, NA, DefaultDialog),
    9135: (DL_TIER + 3, 1, (CogLevelQuest, Anywhere, 160, 11), Any, ToonHQ, Any, NA, DefaultDialog),
    9136: (DL_TIER + 3, 1, (CogLevelQuest, Anywhere, 200, 11), Any, ToonHQ, Any, NA, DefaultDialog),
    9137: (DL_TIER + 3, 1, (CogLevelQuest, Anywhere, 80, 12), Any, ToonHQ, Any, NA, DefaultDialog),
    9138: (DL_TIER + 3, 1, (CogLevelQuest, Anywhere, 120, 12), Any, ToonHQ, Any, NA, DefaultDialog),
    9139: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 400, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    9140: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 400, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    9141: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 400, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    9142: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 400, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    9143: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 500, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    9144: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 500, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    9145: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 500, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    9146: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 500, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    9147: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 600, 'm'), Any, ToonHQ, Any, NA, DefaultDialog),
    9148: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 600, 's'), Any, ToonHQ, Any, NA, DefaultDialog),
    9149: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 600, 'c'), Any, ToonHQ, Any, NA, DefaultDialog),
    9150: (DL_TIER + 3, 1, (CogTrackQuest, Anywhere, 600, 'l'), Any, ToonHQ, Any, NA, DefaultDialog),
    9151: (DL_TIER + 3, 1, (BuildingQuest, Anywhere, 400, Any, 2), Any, ToonHQ, Any, NA, DefaultDialog),
    9152: (DL_TIER + 3, 1, (BuildingQuest, Anywhere, 200, Any, 3), Any, ToonHQ, Any, NA, DefaultDialog),
    9153: (DL_TIER + 3, 1, (BuildingQuest, Anywhere, 200, Any, 4), Any, ToonHQ, Any, NA, DefaultDialog),
    9154: (DL_TIER + 3, 1, (BuildingQuest, Anywhere, 200, Any, 5), Any, ToonHQ, Any, NA, DefaultDialog),
    9155: (DL_TIER + 3, 1, (BuildingQuest, Anywhere, 100, 'm', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    9156: (DL_TIER + 3, 1, (BuildingQuest, Anywhere, 100, 's', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    9157: (DL_TIER + 3, 1, (BuildingQuest, Anywhere, 100, 'c', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    9158: (DL_TIER + 3, 1, (BuildingQuest, Anywhere, 100, 'l', 5), Any, ToonHQ, Any, NA, DefaultDialog),
    9500: (DL_TIER + 3, 1, (CogQuest, ToontownGlobals.DonaldsDreamland, 1000, Any), Any, ToonHQ, NA, 9501, DefaultDialog),
    9501: (DL_TIER + 3, 0, (DeliverItemQuest, 1000), Any, 2004, 1000, NA, DefaultDialog),
    10001: (ELDER_TIER, 1, (CogNewbieQuest, Anywhere, 1, Any, 20), Any, ToonHQ, Any, NA, DefaultDialog),
    10002: (ELDER_TIER, 1, (BuildingNewbieQuest, Anywhere, 1, Any, 1, 20), Any, ToonHQ, Any, NA, DefaultDialog),
    10100: (ELDER_TIER, 1, (CogQuest, Anywhere, 500, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    10101: (ELDER_TIER, 1, (CogQuest, Anywhere, 600, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    10102: (ELDER_TIER, 1, (CogQuest, Anywhere, 700, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    10103: (ELDER_TIER, 1, (CogQuest, Anywhere, 800, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    10104: (ELDER_TIER, 1, (CogQuest, Anywhere, 900, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    10105: (ELDER_TIER, 1, (CogQuest, Anywhere, 1000, Any), Any, ToonHQ, Any, NA, DefaultDialog),
    10200: (ELDER_TIER, 1, (CogQuest, ToontownGlobals.DonaldsDreamland, 1000, Any), Any, ToonHQ, NA, 10201, DefaultDialog),
    10201: (ELDER_TIER, 0, (DeliverItemQuest, 1000), Any, ToonTailor, 1000, NA, DefaultDialog) }
Tier2QuestsDict = { }
for (questId, questDesc) in QuestDict.items():
    if questDesc[QuestDictStartIndex]:
        tier = questDesc[QuestDictTierIndex]
        if Tier2QuestsDict.has_key(tier):
            Tier2QuestsDict[tier].append(questId)
        else:
            Tier2QuestsDict[tier] = [
                questId]
    

Quest2RewardDict = { }
Tier2Reward2QuestsDict = { }
Quest2RemainingStepsDict = { }

def findFinalRewardId(questId):
    finalRewardId = Quest2RewardDict.get(questId)
    if finalRewardId:
        remainingSteps = Quest2RemainingStepsDict.get(questId)
    else:
        
        try:
            questDesc = QuestDict[questId]
        except KeyError:
            print 'findFinalRewardId: Quest ID: %d not found' % questId
            return -1

        nextQuestId = questDesc[QuestDictNextQuestIndex]
        if nextQuestId == NA:
            finalRewardId = questDesc[QuestDictRewardIndex]
            remainingSteps = 1
        elif type(nextQuestId) == type(()):
            (finalRewardId, remainingSteps) = findFinalRewardId(nextQuestId[0])
            for id in nextQuestId[1:]:
                findFinalRewardId(id)
            
        else:
            (finalRewardId, remainingSteps) = findFinalRewardId(nextQuestId)
        remainingSteps += 1
        if finalRewardId != OBSOLETE:
            if questDesc[QuestDictStartIndex]:
                tier = questDesc[QuestDictTierIndex]
                tier2RewardDict = Tier2Reward2QuestsDict.setdefault(tier, { })
                questList = tier2RewardDict.setdefault(finalRewardId, [])
                questList.append(questId)
            
        else:
            finalRewardId = None
        Quest2RewardDict[questId] = finalRewardId
        Quest2RemainingStepsDict[questId] = remainingSteps
    return (finalRewardId, remainingSteps)

for questId in QuestDict.keys():
    findFinalRewardId(questId)


def getStartingQuests(tier = None):
    startingQuests = []
    for questId in QuestDict.keys():
        if isStartingQuest(questId):
            if tier is None:
                startingQuests.append(questId)
            elif questId in Tier2QuestsDict[tier]:
                startingQuests.append(questId)
            
        
    
    startingQuests.sort()
    return startingQuests


def getFinalRewardId(questId, fAll = 0):
    if fAll or isStartingQuest(questId):
        return Quest2RewardDict.get(questId)
    else:
        return None


def isStartingQuest(questId):
    
    try:
        return QuestDict[questId][QuestDictStartIndex]
    except KeyError:
        return None



def getNumChoices(tier):
    if tier in (0,):
        return 0
    
    if tier in (1,):
        return 2
    else:
        return 3


def getAvatarRewardId(av, questId):
    for quest in av.quests:
        if questId == quest[0]:
            return quest[3]
        
    
    notify.warning('getAvatarRewardId(): quest not found on avatar')
    return None


def getNextQuest(id, currentNpc, av):
    nextQuest = QuestDict[id][QuestDictNextQuestIndex]
    if nextQuest == NA:
        return (NA, NA)
    elif type(nextQuest) == type(()):
        nextReward = QuestDict[nextQuest[0]][QuestDictRewardIndex]
        (nextNextQuest, nextNextToNpcId) = getNextQuest(nextQuest[0], currentNpc, av)
        if nextReward == 400 and nextNextQuest == NA:
            nextQuest = chooseTrackChoiceQuest(av.getRewardTier(), av)
        else:
            nextQuest = random.choice(nextQuest)
    
    if not getQuestClass(nextQuest).filterFunc(av):
        return getNextQuest(nextQuest, currentNpc, av)
    
    nextToNpcId = getQuestToNpcId(nextQuest)
    if nextToNpcId == Any:
        nextToNpcId = 2004
    elif nextToNpcId == Same:
        if currentNpc.getHq():
            nextToNpcId = ToonHQ
        else:
            nextToNpcId = currentNpc.getNpcId()
    elif nextToNpcId == ToonHQ:
        nextToNpcId = ToonHQ
    
    return (nextQuest, nextToNpcId)


def filterQuests(entireQuestPool, currentNpc, av):
    notify.debug('filterQuests: entireQuestPool: %s' % entireQuestPool)
    continue
    validQuestPool = []([ (questId, 1) for questId in entireQuestPool ])
    if isLoopingFinalTier(av.getRewardTier()):
        history = map(lambda questDesc: questDesc[0], av.quests)
    else:
        history = av.getQuestHistory()
    notify.debug('filterQuests: av quest history: %s' % history)
    currentQuests = av.quests
    for questId in entireQuestPool:
        if questId in history:
            notify.debug('filterQuests: Removed %s because in history' % questId)
            validQuestPool[questId] = 0
            continue
        
        potentialFromNpc = getQuestFromNpcId(questId)
        if potentialFromNpc != Any and currentNpc.getNpcId() != potentialFromNpc:
            notify.debug('filterQuests: Removed %s because potentialFromNpc is not currentNpc' % questId)
            validQuestPool[questId] = 0
            continue
        
        potentialToNpc = getQuestToNpcId(questId)
        if currentNpc.getNpcId() == potentialToNpc:
            notify.debug('filterQuests: Removed %s because potentialToNpc is currentNpc' % questId)
            validQuestPool[questId] = 0
            continue
        
        if not getQuestClass(questId).filterFunc(av):
            notify.debug('filterQuests: Removed %s because of filterFunc' % questId)
            validQuestPool[questId] = 0
            continue
        
        for quest in currentQuests:
            fromNpcId = quest[1]
            toNpcId = quest[2]
            if potentialToNpc == toNpcId and toNpcId != ToonHQ:
                validQuestPool[questId] = 0
                notify.debug('filterQuests: Removed %s because npc involved' % questId)
                break
            
        
    
    finalQuestPool = filter(lambda key: validQuestPool[key], validQuestPool.keys())
    notify.debug('filterQuests: finalQuestPool: %s' % finalQuestPool)
    return finalQuestPool


def chooseTrackChoiceQuest(tier, av, fixed = 0):
    
    def fixAndCallAgain():
        if not fixed and av.fixTrackAccess():
            notify.warning('av %s trackAccess fixed: %s' % (av.getDoId(), trackAccess))
            return chooseTrackChoiceQuest(tier, av, fixed = 1)
        else:
            return None

    bestQuest = None
    trackAccess = av.getTrackAccess()
    if tier == MM_TIER:
        if trackAccess[ToontownBattleGlobals.HEAL_TRACK] == 1:
            bestQuest = 4002
        elif trackAccess[ToontownBattleGlobals.SOUND_TRACK] == 1:
            bestQuest = 4001
        else:
            notify.warning('av %s has bogus trackAccess: %s' % (av.getDoId(), trackAccess))
            return fixAndCallAgain()
    elif tier == BR_TIER:
        if trackAccess[ToontownBattleGlobals.TRAP_TRACK] == 1:
            if trackAccess[ToontownBattleGlobals.SOUND_TRACK] == 1:
                if trackAccess[ToontownBattleGlobals.DROP_TRACK] == 1:
                    bestQuest = 5004
                elif trackAccess[ToontownBattleGlobals.LURE_TRACK] == 1:
                    bestQuest = 5003
                else:
                    notify.warning('av %s has bogus trackAccess: %s' % (av.getDoId(), trackAccess))
                    return fixAndCallAgain()
            elif trackAccess[ToontownBattleGlobals.HEAL_TRACK] == 1:
                if trackAccess[ToontownBattleGlobals.DROP_TRACK] == 1:
                    bestQuest = 5002
                elif trackAccess[ToontownBattleGlobals.LURE_TRACK] == 1:
                    bestQuest = 5001
                else:
                    notify.warning('av %s has bogus trackAccess: %s' % (av.getDoId(), trackAccess))
                    return fixAndCallAgain()
            
        elif trackAccess[ToontownBattleGlobals.SOUND_TRACK] == 0:
            bestQuest = 5005
        elif trackAccess[ToontownBattleGlobals.HEAL_TRACK] == 0:
            bestQuest = 5006
        elif trackAccess[ToontownBattleGlobals.DROP_TRACK] == 0:
            bestQuest = 5007
        elif trackAccess[ToontownBattleGlobals.LURE_TRACK] == 0:
            bestQuest = 5008
        else:
            notify.warning('av %s has bogus trackAccess: %s' % (av.getDoId(), trackAccess))
            return fixAndCallAgain()
    else:
        notify.debug('questPool for reward 400 had no dynamic choice, tier: %s' % tier)
        bestQuest = seededRandomChoice(Tier2Reward2QuestsDict[tier][400])
    notify.debug('chooseTrackChoiceQuest: avId: %s trackAccess: %s tier: %s bestQuest: %s' % (av.getDoId(), trackAccess, tier, bestQuest))
    return bestQuest


def chooseMatchingQuest(tier, validQuestPool, rewardId, npc, av):
    questsMatchingReward = Tier2Reward2QuestsDict[tier].get(rewardId, [])
    notify.debug('questsMatchingReward: %s tier: %s = %s' % (rewardId, tier, questsMatchingReward))
    if rewardId == 400 and QuestDict[questsMatchingReward[0]][QuestDictNextQuestIndex] == NA:
        bestQuest = chooseTrackChoiceQuest(tier, av)
        notify.debug('single part track choice quest: %s tier: %s avId: %s trackAccess: %s bestQuest: %s' % (rewardId, tier, av.getDoId(), av.getTrackAccess(), bestQuest))
    else:
        validQuestsMatchingReward = PythonUtil.intersection(questsMatchingReward, validQuestPool)
        notify.debug('validQuestsMatchingReward: %s tier: %s = %s' % (rewardId, tier, validQuestsMatchingReward))
        if validQuestsMatchingReward:
            bestQuest = seededRandomChoice(validQuestsMatchingReward)
        else:
            questsMatchingReward = Tier2Reward2QuestsDict[tier].get(Any, [])
            notify.debug('questsMatchingReward: Any tier: %s = %s' % (tier, questsMatchingReward))
            if not questsMatchingReward:
                notify.warning('chooseMatchingQuests, no questsMatchingReward')
                return None
            
            validQuestsMatchingReward = PythonUtil.intersection(questsMatchingReward, validQuestPool)
            if not validQuestsMatchingReward:
                notify.warning('chooseMatchingQuests, no validQuestsMatchingReward')
                return None
            
            notify.debug('validQuestsMatchingReward: Any tier: %s = %s' % (tier, validQuestsMatchingReward))
            bestQuest = seededRandomChoice(validQuestsMatchingReward)
    return bestQuest


def transformReward(baseRewardId, av):
    if baseRewardId == 900:
        (trackId, progress) = av.getTrackProgress()
        if trackId == -1:
            notify.warning('transformReward: asked to transform 900 but av is not training')
            actualRewardId = baseRewardId
        else:
            actualRewardId = 900 + 1 + trackId
        return actualRewardId
    elif baseRewardId > 800 and baseRewardId < 900:
        (trackId, progress) = av.getTrackProgress()
        if trackId < 0:
            notify.warning('transformReward: av: %s is training a track with none chosen!' % av.getDoId())
            return 601
        else:
            actualRewardId = baseRewardId + 200 + trackId * 100
            return actualRewardId
    else:
        return baseRewardId


def chooseBestQuests(tier, currentNpc, av):
    if isLoopingFinalTier(tier):
        rewardHistory = map(lambda questDesc: questDesc[3], av.quests)
    else:
        rewardHistory = av.getRewardHistory()[1]
    seedRandomGen(currentNpc.getNpcId(), av.getDoId(), tier, rewardHistory)
    numChoices = getNumChoices(tier)
    rewards = getNextRewards(numChoices, tier, av)
    if not rewards:
        return []
    
    possibleQuests = []
    possibleRewards = list(rewards)
    if Any not in possibleRewards:
        possibleRewards.append(Any)
    
    for rewardId in possibleRewards:
        possibleQuests.extend(Tier2Reward2QuestsDict[tier].get(rewardId, []))
    
    validQuestPool = filterQuests(possibleQuests, currentNpc, av)
    if not validQuestPool:
        return []
    
    if numChoices == 0:
        numChoices = 1
    
    bestQuests = []
    for i in range(numChoices):
        if len(validQuestPool) == 0:
            break
        
        if len(rewards) == 0:
            break
        
        rewardId = rewards.pop(0)
        bestQuestId = chooseMatchingQuest(tier, validQuestPool, rewardId, currentNpc, av)
        if bestQuestId is None:
            continue
        
        validQuestPool.remove(bestQuestId)
        bestQuestToNpcId = getQuestToNpcId(bestQuestId)
        if bestQuestToNpcId == Any:
            bestQuestToNpcId = 2003
        elif bestQuestToNpcId == Same:
            if currentNpc.getHq():
                bestQuestToNpcId = ToonHQ
            else:
                bestQuestToNpcId = currentNpc.getNpcId()
        elif bestQuestToNpcId == ToonHQ:
            bestQuestToNpcId = ToonHQ
        
        bestQuests.append([
            bestQuestId,
            rewardId,
            bestQuestToNpcId])
    
    for quest in bestQuests:
        quest[1] = transformReward(quest[1], av)
    
    return bestQuests


def questExists(id):
    return QuestDict.has_key(id)


def getQuest(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        questDesc = questEntry[QuestDictDescIndex]
        questClass = questDesc[0]
        return questClass(id, questDesc[1:])
    else:
        return None


def getQuestClass(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        return questEntry[QuestDictDescIndex][0]
    else:
        return None


def getVisitQTStrings(npcId):
    if npcId == ToonHQ:
        strings = [
            'I need to see an HQ Officer.',
            'I need to go to a Toon HQ.']
    elif npcId == ToonTailor:
        strings = [
            'I need to see a Tailor.']
    elif npcId:
        (npcName, hoodName, buildingName, streetName) = getNpcInfo(npcId)
        strings = [
            'I need to see %s.' % npcName]
        if streetName == 'Playground':
            strings.append('I need to go to %s Playground.' % hoodName)
        else:
            strings.append('I need to go to %s in %s.' % (streetName, hoodName))
        strings.extend([
            'I need to visit %s.' % buildingName,
            'Where is %s?' % buildingName])
    
    return strings


def getFinishToonTaskQTStrings(npcId):
    return [
        'I need to finish a ToonTask.'] + getVisitQTStrings(npcId)


def chooseQuestDialog(id, status):
    questDialog = getQuestDialog(id).get(status)
    if questDialog == None:
        if status == QUEST:
            quest = getQuest(id)
            questDialog = quest.getDefaultQuestDialog()
        else:
            questDialog = DefaultDialog[status]
    
    if type(questDialog) == type(()):
        return random.choice(questDialog)
    else:
        return questDialog


def chooseQuestDialogReject():
    return random.choice(DefaultReject)


def chooseQuestDialogTierNotDone():
    return random.choice(DefaultTierNotDone)


def getNpcInfo(npcId):
    npcName = NPCToons.getNPCName(npcId)
    npcZone = NPCToons.getNPCZone(npcId)
    hoodId = ZoneUtil.getHoodId(npcZone)
    hoodName = toonbase.tcr.hoodMgr.getFullnameFromId(hoodId)
    buildingName = NPCToons.getBuildingTitle(npcZone)
    branchId = ZoneUtil.getBranchZone(npcZone)
    streetName = ToontownGlobals.StreetNames[branchId][1]
    return (npcName, hoodName, buildingName, streetName)


def getNpcLocationDialog(fromNpcId, toNpcId):
    if not toNpcId:
        return (None, None, None)
    
    fromNpcZone = None
    fromBranchId = None
    if fromNpcId:
        fromNpcZone = NPCToons.getNPCZone(fromNpcId)
        fromBranchId = ZoneUtil.getBranchZone(fromNpcZone)
    
    toNpcZone = NPCToons.getNPCZone(toNpcId)
    toBranchId = ZoneUtil.getBranchZone(toNpcZone)
    (toNpcName, toHoodName, toBuildingName, toStreetName) = getNpcInfo(toNpcId)
    if fromBranchId == toBranchId:
        if toStreetName == 'Playground':
            streetDesc = Localizer.QuestsStreetLocationThisPlayground
        else:
            streetDesc = Localizer.QuestsStreetLocationThisStreet
    elif toStreetName == 'Playground':
        streetDesc = Localizer.QuestsStreetLocationNamedPlayground % toHoodName
    else:
        streetDesc = Localizer.QuestsStreetLocationNamedStreet % (toStreetName, toHoodName)
    paragraph = Localizer.QuestsLocationParagraph % {
        'building': Localizer.QuestsLocationBuilding % toNpcName,
        'buildingName': toBuildingName,
        'buildingVerb': Localizer.QuestsLocationBuildingVerb,
        'street': streetDesc }
    return (paragraph, toBuildingName, streetDesc)


def fillInQuestNames(text, avName = None, fromNpcId = None, toNpcId = None):
    text = copy.deepcopy(text)
    if avName != None:
        text = string.replace(text, '_avName_', avName)
    
    if toNpcId:
        if toNpcId == ToonHQ:
            toNpcName = Localizer.QuestsHQOfficerFillin
            where = Localizer.QuestsHQWhereFillin
            buildingName = Localizer.QuestsHQBuildingNameFillin
            streetDesc = Localizer.QuestsHQLocationNameFillin
        elif toNpcId == ToonTailor:
            toNpcName = Localizer.QuestsTailorFillin
            where = Localizer.QuestsTailorWhereFillin
            buildingName = Localizer.QuestsTailorBuildingNameFillin
            streetDesc = Localizer.QuestsTailorLocationNameFillin
        else:
            toNpcName = str(NPCToons.getNPCName(toNpcId))
            (where, buildingName, streetDesc) = getNpcLocationDialog(fromNpcId, toNpcId)
        text = string.replace(text, '_toNpcName_', toNpcName)
        text = string.replace(text, '_where_', where)
        text = string.replace(text, '_buildingName_', buildingName)
        text = string.replace(text, '_streetDesc_', streetDesc)
    
    return text


def getVisitingQuest():
    return VisitQuest(VISIT_QUEST_ID)


class Reward:
    
    def __init__(self, id, reward):
        self.id = id
        self.reward = reward

    
    def getId(self):
        return self.id

    
    def getType(self):
        return self.__class__

    
    def getAmount(self):
        return None

    
    def sendRewardAI(self, av):
        raise 'not implemented'

    
    def countReward(self, qrc):
        raise 'not implemented'

    
    def getString(self):
        return 'undefined'

    
    def getPosterString(self):
        return 'base class'



class MaxHpReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getAmount(self):
        return self.reward[0]

    
    def sendRewardAI(self, av):
        maxHp = av.getMaxHp()
        maxHp = min(ToontownGlobals.MaxHpLimit, maxHp + self.getAmount())
        av.b_setMaxHp(maxHp)
        av.b_setHp(maxHp)

    
    def countReward(self, qrc):
        qrc.maxHp += self.getAmount()

    
    def getString(self):
        return Localizer.QuestsMaxHpReward % self.getAmount()

    
    def getPosterString(self):
        return Localizer.QuestsMaxHpRewardPoster % self.getAmount()



class MoneyReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getAmount(self):
        return self.reward[0]

    
    def sendRewardAI(self, av):
        money = av.getMoney()
        maxMoney = av.getMaxMoney()
        money = money + self.getAmount()
        av.setTotalMoney(money)

    
    def countReward(self, qrc):
        qrc.money += self.getAmount()

    
    def getString(self):
        amt = self.getAmount()
        if amt == 1:
            return Localizer.QuestsMoneyRewardSingular
        else:
            return Localizer.QuestsMoneyRewardPlural % amt

    
    def getPosterString(self):
        amt = self.getAmount()
        if amt == 1:
            return Localizer.QuestsMoneyRewardPosterSingular
        else:
            return Localizer.QuestsMoneyRewardPosterPlural % amt



class MaxMoneyReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getAmount(self):
        return self.reward[0]

    
    def sendRewardAI(self, av):
        av.b_setMaxMoney(self.getAmount())

    
    def countReward(self, qrc):
        qrc.maxMoney = self.getAmount()

    
    def getString(self):
        amt = self.getAmount()
        if amt == 1:
            return Localizer.QuestsMaxMoneyRewardSingular
        else:
            return Localizer.QuestsMaxMoneyRewardPlural % amt

    
    def getPosterString(self):
        amt = self.getAmount()
        if amt == 1:
            return Localizer.QuestsMaxMoneyRewardPosterSingular
        else:
            return Localizer.QuestsMaxMoneyRewardPosterPlural % amt



class MaxGagCarryReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getAmount(self):
        return self.reward[0]

    
    def getName(self):
        return self.reward[1]

    
    def sendRewardAI(self, av):
        av.b_setMaxCarry(self.getAmount())

    
    def countReward(self, qrc):
        qrc.maxCarry = self.getAmount()

    
    def getString(self):
        name = self.getName()
        amt = self.getAmount()
        return Localizer.QuestsMaxGagCarryReward % {
            'name': name,
            'num': amt }

    
    def getPosterString(self):
        name = self.getName()
        amt = self.getAmount()
        return Localizer.QuestsMaxGagCarryRewardPoster % {
            'name': name,
            'num': amt }



class MaxQuestCarryReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getAmount(self):
        return self.reward[0]

    
    def sendRewardAI(self, av):
        av.b_setQuestCarryLimit(self.getAmount())

    
    def countReward(self, qrc):
        qrc.questCarryLimit = self.getAmount()

    
    def getString(self):
        amt = self.getAmount()
        return Localizer.QuestsMaxQuestCarryReward % amt

    
    def getPosterString(self):
        amt = self.getAmount()
        return Localizer.QuestsMaxQuestCarryRewardPoster % amt



class TeleportReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getZone(self):
        return self.reward[0]

    
    def sendRewardAI(self, av):
        av.addTeleportAccess(self.getZone())

    
    def countReward(self, qrc):
        qrc.addTeleportAccess(self.getZone())

    
    def getString(self):
        hoodName = ToontownGlobals.hoodNameMap[self.getZone()][1]
        return Localizer.QuestsTeleportReward % hoodName

    
    def getPosterString(self):
        hoodName = ToontownGlobals.hoodNameMap[self.getZone()][1]
        return Localizer.QuestsTeleportRewardPoster % hoodName


TrackTrainingQuotas = {
    ToontownBattleGlobals.HEAL_TRACK: 15,
    ToontownBattleGlobals.TRAP_TRACK: 15,
    ToontownBattleGlobals.LURE_TRACK: 15,
    ToontownBattleGlobals.SOUND_TRACK: 15,
    ToontownBattleGlobals.THROW_TRACK: 15,
    ToontownBattleGlobals.SQUIRT_TRACK: 15,
    ToontownBattleGlobals.DROP_TRACK: 15 }

class TrackTrainingReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        
        return track

    
    def sendRewardAI(self, av):
        av.b_setTrackProgress(self.getTrack(), 0)

    
    def countReward(self, qrc):
        qrc.trackProgressId = self.getTrack()
        qrc.trackProgress = 0

    
    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return Localizer.QuestsTrackTrainingReward % trackName

    
    def getPosterString(self):
        return Localizer.QuestsTrackTrainingRewardPoster



class TrackProgressReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        
        return track

    
    def getProgressIndex(self):
        return self.reward[1]

    
    def sendRewardAI(self, av):
        av.addTrackProgress(self.getTrack(), self.getProgressIndex())

    
    def countReward(self, qrc):
        qrc.addTrackProgress(self.getTrack(), self.getProgressIndex())

    
    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return Localizer.QuestsTrackProgressReward % {
            'frameNum': self.getProgressIndex(),
            'trackName': trackName }

    
    def getPosterString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return Localizer.QuestsTrackProgressRewardPoster % {
            'trackName': trackName,
            'frameNum': self.getProgressIndex() }



class TrackCompleteReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        
        return track

    
    def sendRewardAI(self, av):
        av.addTrackAccess(self.getTrack())
        av.clearTrackProgress()

    
    def countReward(self, qrc):
        qrc.addTrackAccess(self.getTrack())
        qrc.clearTrackProgress()

    
    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return Localizer.QuestsTrackCompleteReward % trackName

    
    def getPosterString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return Localizer.QuestsTrackCompleteRewardPoster % trackName



class ClothingTicketReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def sendRewardAI(self, av):
        return None

    
    def countReward(self, qrc):
        return None

    
    def getString(self):
        return Localizer.QuestsClothingTicketReward

    
    def getPosterString(self):
        return Localizer.QuestsClothingTicketRewardPoster



class CheesyEffectReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getEffect(self):
        return self.reward[0]

    
    def getHoodId(self):
        return self.reward[1]

    
    def getDurationMinutes(self):
        return self.reward[2]

    
    def sendRewardAI(self, av):
        expireTime = int(time.time() / 60 + 0.5) + self.getDurationMinutes()
        av.b_setCheesyEffect(self.getEffect(), self.getHoodId(), expireTime)

    
    def countReward(self, qrc):
        pass

    
    def getString(self):
        effect = self.getEffect()
        hoodId = self.getHoodId()
        duration = self.getDurationMinutes()
        string = Localizer.CheesyEffectMinutes
        if duration > 90:
            duration = int((duration + 30) / 60)
            string = Localizer.CheesyEffectHours
            if duration > 36:
                duration = int((duration + 12) / 24)
                string = Localizer.CheesyEffectDays
            
        
        desc = Localizer.CheesyEffectDescriptions[effect][1]
        if hoodId == 0:
            whileStr = ''
        elif hoodId == 1:
            whileStr = Localizer.CheesyEffectExceptIn % Localizer.ToontownCentral[1]
        else:
            hoodName = toonbase.tcr.hoodMgr.getFullnameFromId(hoodId)
            whileStr = Localizer.CheesyEffectWhileYouAreIn % hoodName
        if duration:
            return string % {
                'time': duration,
                'effectName': desc,
                'whileIn': whileStr }
        else:
            return Localizer.CheesyEffectIndefinite % {
                'effectName': desc,
                'whileIn': whileStr }

    
    def getPosterString(self):
        effect = self.getEffect()
        desc = Localizer.CheesyEffectDescriptions[effect][0]
        return Localizer.QuestsCheesyEffectRewardPoster % desc



def getRewardClass(id):
    reward = RewardDict.get(id)
    if reward:
        return reward[0]
    else:
        return None


def getReward(id):
    reward = RewardDict.get(id)
    if reward:
        rewardClass = reward[0]
        return rewardClass(id, reward[1:])
    else:
        return None


def getNextRewards(numChoices, tier, av):
    rewardTier = list(getRewardsInTier(tier))
    optRewards = list(getOptionalRewardsInTier(tier))
    if isLoopingFinalTier(tier):
        rewardHistory = map(lambda questDesc: questDesc[3], av.quests)
    else:
        rewardHistory = av.getRewardHistory()[1]
    for rewardId in rewardHistory:
        if rewardId in rewardTier:
            rewardTier.remove(rewardId)
        elif rewardId in optRewards:
            optRewards.remove(rewardId)
        elif rewardId in (901, 902, 903, 904, 905, 906, 907):
            genericRewardId = 900
            if genericRewardId in rewardTier:
                rewardTier.remove(genericRewardId)
            
        elif rewardId > 1000 and rewardId < 1699:
            index = rewardId % 100
            genericRewardId = 800 + index
            if genericRewardId in rewardTier:
                rewardTier.remove(genericRewardId)
            
        
    
    if numChoices == 0:
        if len(rewardTier) == 0:
            return []
        else:
            return [
                rewardTier[0]]
    
    rewardPool = rewardTier[:numChoices]
    for i in range(len(rewardPool), numChoices * 2):
        if optRewards:
            optionalReward = seededRandomChoice(optRewards)
            optRewards.remove(optionalReward)
            rewardPool.append(optionalReward)
        else:
            break
    
    notify.debug('getNextRewards: starting reward pool: %s' % rewardPool)
    if len(rewardPool) == 0:
        return []
    
    finalRewardPool = [
        rewardPool.pop(0)]
    for i in range(numChoices - 1):
        if len(rewardPool) == 0:
            break
        
        selectedReward = seededRandomChoice(rewardPool)
        rewardPool.remove(selectedReward)
        finalRewardPool.append(selectedReward)
    
    return finalRewardPool

RewardDict = {
    100: (MaxHpReward, 1),
    101: (MaxHpReward, 2),
    102: (MaxHpReward, 3),
    103: (MaxHpReward, 4),
    104: (MaxHpReward, 5),
    105: (MaxHpReward, 6),
    106: (MaxHpReward, 7),
    107: (MaxHpReward, 8),
    108: (MaxHpReward, 9),
    109: (MaxHpReward, 10),
    200: (MaxGagCarryReward, 25, Localizer.QuestsMediumPouch),
    201: (MaxGagCarryReward, 30, Localizer.QuestsLargePouch),
    202: (MaxGagCarryReward, 35, Localizer.QuestsSmallBag),
    203: (MaxGagCarryReward, 40, Localizer.QuestsMediumBag),
    204: (MaxGagCarryReward, 50, Localizer.QuestsLargeBag),
    205: (MaxGagCarryReward, 60, Localizer.QuestsSmallBackpack),
    206: (MaxGagCarryReward, 70, Localizer.QuestsMediumBackpack),
    207: (MaxGagCarryReward, 80, Localizer.QuestsLargeBackpack),
    300: (TeleportReward, ToontownGlobals.ToontownCentral),
    301: (TeleportReward, ToontownGlobals.DonaldsDock),
    302: (TeleportReward, ToontownGlobals.DaisyGardens),
    303: (TeleportReward, ToontownGlobals.MinniesMelodyland),
    304: (TeleportReward, ToontownGlobals.TheBrrrgh),
    305: (TeleportReward, ToontownGlobals.DonaldsDreamland),
    400: (TrackTrainingReward, None),
    401: (TrackTrainingReward, ToontownBattleGlobals.HEAL_TRACK),
    402: (TrackTrainingReward, ToontownBattleGlobals.TRAP_TRACK),
    403: (TrackTrainingReward, ToontownBattleGlobals.LURE_TRACK),
    404: (TrackTrainingReward, ToontownBattleGlobals.SOUND_TRACK),
    405: (TrackTrainingReward, ToontownBattleGlobals.THROW_TRACK),
    406: (TrackTrainingReward, ToontownBattleGlobals.SQUIRT_TRACK),
    407: (TrackTrainingReward, ToontownBattleGlobals.DROP_TRACK),
    500: (MaxQuestCarryReward, 2),
    501: (MaxQuestCarryReward, 3),
    502: (MaxQuestCarryReward, 4),
    600: (MoneyReward, 5),
    601: (MoneyReward, 10),
    602: (MoneyReward, 20),
    603: (MoneyReward, 30),
    604: (MoneyReward, 50),
    605: (MoneyReward, 75),
    606: (MoneyReward, 100),
    607: (MoneyReward, 100),
    608: (MoneyReward, 120),
    609: (MoneyReward, 200),
    700: (MaxMoneyReward, 50),
    701: (MaxMoneyReward, 60),
    702: (MaxMoneyReward, 80),
    703: (MaxMoneyReward, 100),
    704: (MaxMoneyReward, 120),
    705: (MaxMoneyReward, 150),
    706: (MaxMoneyReward, 200),
    707: (MaxMoneyReward, 250),
    801: (TrackProgressReward, None, 1),
    802: (TrackProgressReward, None, 2),
    803: (TrackProgressReward, None, 3),
    804: (TrackProgressReward, None, 4),
    805: (TrackProgressReward, None, 5),
    806: (TrackProgressReward, None, 6),
    807: (TrackProgressReward, None, 7),
    808: (TrackProgressReward, None, 8),
    809: (TrackProgressReward, None, 9),
    810: (TrackProgressReward, None, 10),
    811: (TrackProgressReward, None, 11),
    812: (TrackProgressReward, None, 12),
    813: (TrackProgressReward, None, 13),
    814: (TrackProgressReward, None, 14),
    815: (TrackProgressReward, None, 15),
    1000: (ClothingTicketReward,),
    1001: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 1),
    1002: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 2),
    1003: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 3),
    1004: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 4),
    1005: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 5),
    1006: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 6),
    1007: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 7),
    1008: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 8),
    1009: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 9),
    1010: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 10),
    1011: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 11),
    1012: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 12),
    1013: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 13),
    1014: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 14),
    1015: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 15),
    1101: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 1),
    1102: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 2),
    1103: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 3),
    1104: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 4),
    1105: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 5),
    1106: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 6),
    1107: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 7),
    1108: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 8),
    1109: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 9),
    1110: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 10),
    1111: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 11),
    1112: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 12),
    1113: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 13),
    1114: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 14),
    1115: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 15),
    1201: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 1),
    1202: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 2),
    1203: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 3),
    1204: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 4),
    1205: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 5),
    1206: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 6),
    1207: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 7),
    1208: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 8),
    1209: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 9),
    1210: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 10),
    1211: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 11),
    1212: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 12),
    1213: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 13),
    1214: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 14),
    1215: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 15),
    1301: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 1),
    1302: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 2),
    1303: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 3),
    1304: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 4),
    1305: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 5),
    1306: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 6),
    1307: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 7),
    1308: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 8),
    1309: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 9),
    1310: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 10),
    1311: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 11),
    1312: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 12),
    1313: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 13),
    1314: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 14),
    1315: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 15),
    1601: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 1),
    1602: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 2),
    1603: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 3),
    1604: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 4),
    1605: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 5),
    1606: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 6),
    1607: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 7),
    1608: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 8),
    1609: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 9),
    1610: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 10),
    1611: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 11),
    1612: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 12),
    1613: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 13),
    1614: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 14),
    1615: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 15),
    900: (TrackCompleteReward, None),
    901: (TrackCompleteReward, ToontownBattleGlobals.HEAL_TRACK),
    902: (TrackCompleteReward, ToontownBattleGlobals.TRAP_TRACK),
    903: (TrackCompleteReward, ToontownBattleGlobals.LURE_TRACK),
    904: (TrackCompleteReward, ToontownBattleGlobals.SOUND_TRACK),
    905: (TrackCompleteReward, ToontownBattleGlobals.THROW_TRACK),
    906: (TrackCompleteReward, ToontownBattleGlobals.SQUIRT_TRACK),
    907: (TrackCompleteReward, ToontownBattleGlobals.DROP_TRACK),
    2205: (CheesyEffectReward, ToontownGlobals.CEBigToon, 2000, 10),
    2206: (CheesyEffectReward, ToontownGlobals.CESmallToon, 2000, 10),
    2101: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1000, 10),
    2102: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1000, 10),
    2105: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 20),
    2106: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 20),
    2501: (CheesyEffectReward, ToontownGlobals.CEBigHead, 5000, 60),
    2502: (CheesyEffectReward, ToontownGlobals.CESmallHead, 5000, 60),
    2503: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 5000, 20),
    2504: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 5000, 20),
    2505: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 60),
    2506: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 60),
    2401: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 120),
    2402: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 120),
    2403: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 4000, 60),
    2404: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 4000, 60),
    2405: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 120),
    2406: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 120),
    2407: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 4000, 30),
    2408: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 4000, 30),
    2409: (CheesyEffectReward, ToontownGlobals.CETransparent, 4000, 30),
    2410: (CheesyEffectReward, ToontownGlobals.CENoColor, 4000, 30),
    2301: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 360),
    2302: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 360),
    2303: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 1, 360),
    2304: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 1, 360),
    2305: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 1440),
    2306: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 1440),
    2307: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 3000, 240),
    2308: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 3000, 240),
    2309: (CheesyEffectReward, ToontownGlobals.CETransparent, 1, 120),
    2310: (CheesyEffectReward, ToontownGlobals.CENoColor, 1, 120),
    2311: (CheesyEffectReward, ToontownGlobals.CEInvisible, 3000, 120),
    2900: (CheesyEffectReward, ToontownGlobals.CENormal, 0, 0),
    2901: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 1440),
    2902: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 1440),
    2903: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 1, 1440),
    2904: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 1, 1440),
    2905: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 1440),
    2906: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 1440),
    2907: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 1, 1440),
    2908: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 1, 1440),
    2909: (CheesyEffectReward, ToontownGlobals.CETransparent, 1, 1440),
    2910: (CheesyEffectReward, ToontownGlobals.CENoColor, 1, 1440),
    2911: (CheesyEffectReward, ToontownGlobals.CEInvisible, 1, 1440),
    2920: (CheesyEffectReward, ToontownGlobals.CENormal, 0, 0),
    2921: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 2880),
    2922: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 2880),
    2923: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 1, 2880),
    2924: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 1, 2880),
    2925: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 2880),
    2926: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 2880),
    2927: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 1, 2880),
    2928: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 1, 2880),
    2929: (CheesyEffectReward, ToontownGlobals.CETransparent, 1, 2880),
    2930: (CheesyEffectReward, ToontownGlobals.CENoColor, 1, 2880),
    2931: (CheesyEffectReward, ToontownGlobals.CEInvisible, 1, 2880),
    2940: (CheesyEffectReward, ToontownGlobals.CENormal, 0, 0),
    2941: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 10080),
    2942: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 10080),
    2943: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 1, 10080),
    2944: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 1, 10080),
    2945: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 10080),
    2946: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 10080),
    2947: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 1, 10080),
    2948: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 1, 10080),
    2949: (CheesyEffectReward, ToontownGlobals.CETransparent, 1, 10080),
    2950: (CheesyEffectReward, ToontownGlobals.CENoColor, 1, 10080),
    2951: (CheesyEffectReward, ToontownGlobals.CEInvisible, 1, 10080),
    2960: (CheesyEffectReward, ToontownGlobals.CENormal, 0, 0),
    2961: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 43200),
    2962: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 43200),
    2963: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 1, 43200),
    2964: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 1, 43200),
    2965: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 43200),
    2966: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 43200),
    2967: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 1, 43200),
    2968: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 1, 43200),
    2969: (CheesyEffectReward, ToontownGlobals.CETransparent, 1, 43200),
    2970: (CheesyEffectReward, ToontownGlobals.CENoColor, 1, 43200),
    2971: (CheesyEffectReward, ToontownGlobals.CEInvisible, 1, 43200) }

def getNumTiers():
    return len(RequiredRewardTrackDict) - 1


def isLoopingFinalTier(tier):
    return tier == LOOPING_FINAL_TIER


def getRewardsInTier(tier):
    return RequiredRewardTrackDict.get(tier, [])


def getNumRewardsInTier(tier):
    return len(RequiredRewardTrackDict.get(tier, []))


def rewardTierExists(tier):
    return RequiredRewardTrackDict.has_key(tier)


def getOptionalRewardsInTier(tier):
    return OptionalRewardTrackDict.get(tier, [])


def getRewardIdFromTrackId(trackId):
    return 401 + trackId

RequiredRewardTrackDict = {
    TT_TIER: (100,),
    TT_TIER + 1: (400,),
    TT_TIER + 2: (100, 801, 200, 802, 803, 101, 804, 805, 102, 806, 807, 100, 808, 809, 101, 810, 811, 500, 812, 813, 700, 814, 815, 300),
    TT_TIER + 3: (900,),
    DD_TIER: (400,),
    DD_TIER + 1: (100, 801, 802, 201, 803, 804, 101, 805, 806, 102, 807, 808, 100, 809, 810, 101, 811, 812, 701, 813, 814, 815, 301),
    DD_TIER + 2: (900,),
    DG_TIER: (100, 202, 101, 102, 100, 101, 501, 702, 302),
    MM_TIER: (400,),
    MM_TIER + 1: (100, 801, 802, 203, 803, 804, 101, 805, 806, 102, 807, 808, 100, 809, 810, 101, 811, 812, 703, 813, 814, 815, 303),
    MM_TIER + 2: (900,),
    BR_TIER: (400,),
    BR_TIER + 1: (100, 801, 802, 704, 803, 804, 101, 805, 806, 502, 807, 808, 102, 809, 810, 204, 811, 812, 100, 813, 814, 101, 815, 304),
    BR_TIER + 2: (900,),
    DL_TIER: (100, 205, 101, 102, 705, 103, 305),
    DL_TIER + 1: (100, 206, 101, 102, 706, 103),
    DL_TIER + 2: (100, 101, 102, 103),
    DL_TIER + 3: (100, 101, 102, 102, 707, 207) }
OptionalRewardTrackDict = {
    TT_TIER: (),
    TT_TIER + 1: (),
    TT_TIER + 2: (1000, 601, 601, 602, 602, 2205, 2206, 2205, 2206),
    TT_TIER + 3: (),
    DD_TIER: (1000, 602, 602, 603, 603, 2101, 2102, 2105, 2106),
    DD_TIER + 1: (1000, 602, 602, 603, 603, 2101, 2102, 2105, 2106),
    DD_TIER + 2: (1000, 602, 602, 603, 603, 2101, 2102, 2105, 2106),
    DG_TIER: (1000, 603, 603, 604, 604, 2501, 2502, 2503, 2504, 2505, 2506),
    MM_TIER: (1000, 604, 604, 605, 605, 2403, 2404, 2405, 2406, 2407, 2408, 2409),
    MM_TIER + 1: (1000, 604, 604, 605, 605, 2403, 2404, 2405, 2406, 2407, 2408, 2409),
    MM_TIER + 2: (1000, 604, 604, 605, 605, 2403, 2404, 2405, 2406, 2407, 2408, 2409),
    BR_TIER: (1000, 606, 606, 607, 607, 2305, 2306, 2307, 2308, 2309, 2310, 2311),
    BR_TIER + 1: (1000, 606, 606, 607, 607, 2305, 2306, 2307, 2308, 2309, 2310, 2311),
    BR_TIER + 2: (1000, 606, 606, 607, 607, 2305, 2306, 2307, 2308, 2309, 2310, 2311),
    DL_TIER: (607, 607, 608, 608, 2901, 2902, 2907, 2908, 2909, 2910, 2911),
    DL_TIER + 1: (1000, 607, 607, 608, 608, 2923, 2924, 2927, 2928, 2929, 2930, 2931),
    DL_TIER + 2: (608, 608, 609, 609, 2941, 2942, 2943, 2944, 2947, 2948, 2949, 2950, 2951),
    DL_TIER + 3: (1000, 609, 609, 2961, 2962, 2963, 2964, 2965, 2966, 2967, 2968, 2969, 2970, 2971) }

def isRewardOptional(tier, rewardId):
    if OptionalRewardTrackDict.has_key(tier):
        pass
    return rewardId in OptionalRewardTrackDict[tier]


def getItemName(itemId):
    return ItemDict[itemId][0]


def getPluralItemName(itemId):
    return ItemDict[itemId][1]


def avatarWorkingOnRequiredRewards(av):
    tier = av.getRewardTier()
    rewardList = list(getRewardsInTier(tier))
    for i in range(len(rewardList)):
        actualRewardId = transformReward(rewardList[i], av)
        rewardList[i] = actualRewardId
    
    for questDesc in av.quests:
        questId = questDesc[0]
        rewardId = questDesc[3]
        if rewardId in rewardList:
            return 1
        elif rewardId == NA:
            rewardId = transformReward(getFinalRewardId(questId, fAll = 1), av)
            if rewardId in rewardList:
                return 1
            
        
    
    return 0


def avatarHasAllRequiredRewards(av, tier):
    rewardHistory = av.getRewardHistory()[1]
    rewardList = getRewardsInTier(tier)
    notify.debug('avatarHasAllRequiredRewards: history: %s, tier: %s' % (rewardHistory, rewardList))
    for rewardId in rewardList:
        if rewardId == 900:
            found = 0
            for actualRewardId in (901, 902, 903, 904, 905, 906, 907):
                if actualRewardId in rewardHistory:
                    found = 1
                
            
            if not found:
                notify.debug('avatarHasAllRequiredRewards: rewardId 900 not found')
                return 0
            
        else:
            actualRewardId = transformReward(rewardId, av)
            if actualRewardId not in rewardHistory:
                notify.debug('avatarHasAllRequiredRewards: rewardId %s not found' % actualRewardId)
                return 0
            
    
    return 1


def nextQuestList(nextQuest):
    if nextQuest == NA:
        return None
    
    seqTypes = (types.ListType, types.TupleType)
    if type(nextQuest) in seqTypes:
        return nextQuest
    else:
        return (nextQuest,)


def checkReward(questId, forked = 0):
    quest = QuestDict[questId]
    reward = quest[5]
    nextQuests = nextQuestList(quest[6])
    if nextQuests is None:
        validRewards = RewardDict.keys() + [
            Any,
            OBSOLETE]
        if reward is OBSOLETE:
            print 'warning: quest %s is obsolete' % questId
        
        return reward
    elif not forked:
        pass
    forked = len(nextQuests) > 1
    firstReward = checkReward(nextQuests[0], forked)
    for qId in nextQuests[1:]:
        thisReward = checkReward(qId, forked)
    
    return firstReward


def assertAllQuestsValid():
    print 'checking quests...'
    for questId in QuestDict.keys():
        
        try:
            quest = getQuest(questId)
        except AssertionError:
            e = None
            err = 'invalid quest: %s' % questId
            print err
            raise 

    
    for questId in QuestDict.keys():
        quest = QuestDict[questId]
        (tier, start, questDesc, fromNpc, toNpc, reward, nextQuest, dialog) = quest
        if start:
            checkReward(questId)
        
    

