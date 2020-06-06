# File: N (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
from toontown.battle import SuitBattleGlobals
from toontown.toonbase import TTLocalizer
import HolidayDecorator
from direct.interval.IntervalGlobal import *
decorationHolidays = [
    ToontownGlobals.WINTER_DECORATIONS]
promotionalSpeedChatHolidays = [
    ToontownGlobals.ELECTION_PROMOTION]

class NewsManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('NewsManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.population = 0
        self.invading = 0
        self.decorationHolidayId = ToontownGlobals.NO_HOLIDAY
        self.holidayDecorator = None
        self.holidayIdList = []
        base.cr.newsManager = self
        base.localAvatar.inventory.setInvasionCreditMultiplier(1)

    
    def delete(self):
        self.cr.newsManager = None
        if self.holidayDecorator:
            self.holidayDecorator.exit()
        
        DistributedObject.DistributedObject.delete(self)

    
    def setPopulation(self, population):
        self.population = population
        messenger.send('newPopulation', [
            population])

    
    def getPopulation(self):
        return population

    
    def setInvasionStatus(self, msgType, cogType, numRemaining, skeleton):
        self.notify.info('setInvasionStatus: msgType: %s cogType: %s, numRemaining: %s, skeleton: %s' % (msgType, cogType, numRemaining, skeleton))
        cogName = SuitBattleGlobals.SuitAttributes[cogType]['name']
        cogNameP = SuitBattleGlobals.SuitAttributes[cogType]['pluralname']
        if skeleton:
            cogName = TTLocalizer.Skeleton
            cogNameP = TTLocalizer.SkeletonP
        
        if msgType == ToontownGlobals.SuitInvasionBegin:
            msg1 = TTLocalizer.SuitInvasionBegin1
            msg2 = TTLocalizer.SuitInvasionBegin2 % cogNameP
            self.invading = 1
        elif msgType == ToontownGlobals.SuitInvasionUpdate:
            msg1 = TTLocalizer.SuitInvasionUpdate1 % numRemaining
            msg2 = TTLocalizer.SuitInvasionUpdate2 % cogNameP
            self.invading = 1
        elif msgType == ToontownGlobals.SuitInvasionEnd:
            msg1 = TTLocalizer.SuitInvasionEnd1 % cogName
            msg2 = TTLocalizer.SuitInvasionEnd2
            self.invading = 0
        elif msgType == ToontownGlobals.SuitInvasionBulletin:
            msg1 = TTLocalizer.SuitInvasionBulletin1
            msg2 = TTLocalizer.SuitInvasionBulletin2 % cogNameP
            self.invading = 1
        else:
            self.notify.warning('setInvasionStatus: invalid msgType: %s' % msgType)
            return None
        if self.invading:
            mult = ToontownBattleGlobals.getInvasionMultiplier()
        else:
            mult = 1
        base.localAvatar.inventory.setInvasionCreditMultiplier(mult)
        Sequence(Wait(1.0), Func(base.localAvatar.setSystemMessage, 0, msg1), Wait(5.0), Func(base.localAvatar.setSystemMessage, 0, msg2), name = 'newsManagerWait').start()
        return None

    
    def getInvading(self):
        return self.invading

    
    def startHoliday(self, holidayId):
        if holidayId not in self.holidayIdList:
            self.notify.info('setHolidayId: Starting Holiday %s' % holidayId)
            self.holidayIdList.append(holidayId)
            if holidayId in decorationHolidays:
                self.decorationHolidayId = holidayId
                if hasattr(base.cr.playGame, 'dnaStore') and hasattr(base.cr.playGame, 'hood') and hasattr(base.cr.playGame.hood, 'loader'):
                    self.holidayDecorator = HolidayDecorator.HolidayDecorator()
                    self.holidayDecorator.decorate()
                
            elif holidayId in promotionalSpeedChatHolidays:
                if hasattr(base, 'TTSCPromotionalMenu'):
                    base.TTSCPromotionalMenu.startHoliday(holidayId)
                
            
        

    
    def endHoliday(self, holidayId):
        if holidayId in self.holidayIdList:
            self.notify.info('setHolidayId: Ending Holiday %s' % holidayId)
            self.holidayIdList.remove(holidayId)
            if holidayId == self.decorationHolidayId:
                self.decorationHolidayId = ToontownGlobals.NO_HOLIDAY
                if hasattr(base.cr.playGame, 'dnaStore') and hasattr(base.cr.playGame, 'hood') and hasattr(base.cr.playGame.hood, 'loader'):
                    self.holidayDecorator = HolidayDecorator.HolidayDecorator()
                    self.holidayDecorator.undecorate()
                
            elif holidayId in promotionalSpeedChatHolidays:
                if hasattr(base, 'TTSCPromotionalMenu'):
                    base.TTSCPromotionalMenu.endHoliday(holidayId)
                
            
        

    
    def setHolidayIdList(self, holidayIdList):
        print 'setHolidayIdList: %s' % holidayIdList
        
        def isEnding(id):
            return id not in holidayIdList

        
        def isStarting(id):
            return id not in self.holidayIdList

        toEnd = filter(isEnding, self.holidayIdList)
        for endingHolidayId in toEnd:
            self.endHoliday(endingHolidayId)
        
        toStart = filter(isStarting, holidayIdList)
        for startingHolidayId in toStart:
            self.startHoliday(startingHolidayId)
        
        messenger.send('setHolidayIdList', [
            holidayIdList])

    
    def getDecorationHolidayId(self):
        return self.decorationHolidayId

    
    def getHolidayIdList(self):
        return self.holidayIdList

    
    def setBingoWin(self, zoneId):
        print 'Hello'
        base.localAvatar.setSystemMessage(0, 'Bingo congrats!')

    
    def setBingoStart(self):
        base.localAvatar.setSystemMessage(0, TTLocalizer.FishBingoStart)

    
    def setBingoEnd(self):
        base.localAvatar.setSystemMessage(0, TTLocalizer.FishBingoEnd)


