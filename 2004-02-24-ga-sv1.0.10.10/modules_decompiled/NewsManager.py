# File: N (Python 2.2)

from ShowBaseGlobal import *
import DistributedObject
import DirectNotifyGlobal
import ToontownGlobals
import ToontownBattleGlobals
import SuitBattleGlobals
import Localizer
import HolidayDecorator
from IntervalGlobal import *
decorationHolidays = [
    ToontownGlobals.WINTER_DECORATIONS]

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
        toonbase.tcr.newsManager = self
        toonbase.localToon.inventory.setInvasionCreditMultiplier(1)

    
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

    
    def setInvasionStatus(self, msgType, cogType, numRemaining):
        self.notify.info('setInvasionStatus: msgType: %s cogType: %s, numRemaining: %s' % (msgType, cogType, numRemaining))
        cogName = SuitBattleGlobals.SuitAttributes[cogType]['name']
        cogNameP = SuitBattleGlobals.SuitAttributes[cogType]['pluralname']
        if msgType == ToontownGlobals.SuitInvasionBegin:
            msg1 = Localizer.SuitInvasionBegin1
            msg2 = Localizer.SuitInvasionBegin2 % cogNameP
            self.invading = 1
        elif msgType == ToontownGlobals.SuitInvasionUpdate:
            msg1 = Localizer.SuitInvasionUpdate1 % numRemaining
            msg2 = Localizer.SuitInvasionUpdate2 % cogNameP
            self.invading = 1
        elif msgType == ToontownGlobals.SuitInvasionEnd:
            msg1 = Localizer.SuitInvasionEnd1 % cogName
            msg2 = Localizer.SuitInvasionEnd2
            self.invading = 0
        elif msgType == ToontownGlobals.SuitInvasionBulletin:
            msg1 = Localizer.SuitInvasionBulletin1
            msg2 = Localizer.SuitInvasionBulletin2 % cogNameP
            self.invading = 1
        else:
            self.notify.warning('setInvasionStatus: invalid msgType: %s' % msgType)
            return None
        if self.invading:
            mult = ToontownBattleGlobals.getInvasionMultiplier()
        else:
            mult = 1
        toonbase.localToon.inventory.setInvasionCreditMultiplier(mult)
        Sequence(Wait(1.0), Func(toonbase.localToon.setSystemMessage, 0, msg1), Wait(5.0), Func(toonbase.localToon.setSystemMessage, 0, msg2), name = 'newsManagerWait').start()
        return None

    
    def getInvading(self):
        return self.invading

    
    def startHoliday(self, holidayId):
        if holidayId not in self.holidayIdList:
            self.notify.info('setHolidayId: Starting Holiday %s' % holidayId)
            self.holidayIdList.append(holidayId)
            if holidayId in decorationHolidays:
                self.decorationHolidayId = holidayId
                if hasattr(toonbase.tcr.playGame, 'dnaStore') and hasattr(toonbase.tcr.playGame, 'hood') and hasattr(toonbase.tcr.playGame.hood, 'loader'):
                    self.holidayDecorator = HolidayDecorator.HolidayDecorator()
                    self.holidayDecorator.decorate()
                
            
        

    
    def endHoliday(self, holidayId):
        if holidayId in self.holidayIdList:
            self.notify.info('setHolidayId: Ending Holiday %s' % holidayId)
            self.holidayIdList.remove(holidayId)
            if holidayId == self.decorationHolidayId:
                self.decorationHolidayId = ToontownGlobals.NO_HOLIDAY
                if hasattr(toonbase.tcr.playGame, 'dnaStore') and hasattr(toonbase.tcr.playGame, 'hood') and hasattr(toonbase.tcr.playGame.hood, 'loader'):
                    self.holidayDecorator = HolidayDecorator.HolidayDecorator()
                    self.holidayDecorator.undecorate()
                
            
        

    
    def setHolidayIdList(self, holidayIdList):
        
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


