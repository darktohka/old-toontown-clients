# File: C (Python 2.2)

import DirectNotifyGlobal
import CatalogItem
import CatalogItemList
from CatalogFurnitureItem import CatalogFurnitureItem, nextAvailableBank, getAllBanks
from CatalogClothingItem import CatalogClothingItem, getAllClothes
from CatalogChatItem import CatalogChatItem, getChatRange
from CatalogEmoteItem import CatalogEmoteItem
from CatalogWallpaperItem import CatalogWallpaperItem, getWallpapers
from CatalogFlooringItem import CatalogFlooringItem, getFloorings
from CatalogMouldingItem import CatalogMouldingItem, getAllMouldings
from CatalogWainscotingItem import CatalogWainscotingItem, getAllWainscotings
from CatalogWindowItem import CatalogWindowItem
from CatalogPoleItem import nextAvailablePole, getAllPoles
import Actor
import Localizer
import ToontownGlobals
import types
import random
import time
from PandaModules import *
MetaItems = {
    100: getAllClothes(101, 102, 103, 104, 105, 106, 107, 108, 109, 109, 111, 115, 201, 202, 203, 204, 205, 206, 207, 208, 209, 209, 211, 215),
    300: getAllClothes(301, 302, 303, 304, 305, 308, 401, 403, 404, 405, 407, 451, 452, 453),
    2000: getChatRange(0, 1999),
    2010: getChatRange(2000, 2999),
    2020: getChatRange(3000, 3999),
    2900: getChatRange(10000, 10099),
    2910: getChatRange(11000, 11099),
    2920: getChatRange(12000, 12099),
    3000: getWallpapers(1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100),
    3010: getWallpapers(2200, 2300, 2400, 2500, 2600, 2700, 2800),
    3020: getWallpapers(2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600),
    3500: getAllWainscotings(1000, 1010),
    3510: getAllWainscotings(1020),
    3520: getAllWainscotings(1030),
    3530: getAllWainscotings(1040),
    4000: getFloorings(1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100),
    4010: getFloorings(1110, 1120, 1130),
    4020: getFloorings(1140, 1150, 1160, 1170, 1180, 1190),
    4500: getAllMouldings(1000, 1010),
    4510: getAllMouldings(1020, 1030, 1040),
    4520: getAllMouldings(1070) }
MonthlySchedule = ((10, 1, 10, 31, ((3, 2900), CatalogClothingItem(1001, 0), CatalogClothingItem(1002, 0), CatalogWallpaperItem(10100), CatalogWallpaperItem(10200), CatalogFurnitureItem(10000), CatalogFurnitureItem(10010))), (12, 1, 1, 1, ((3, 2910), CatalogClothingItem(1100, 0), CatalogClothingItem(1101, 0), CatalogClothingItem(1102, 0), CatalogClothingItem(1103, 0), CatalogWallpaperItem(11000), CatalogWallpaperItem(11100), CatalogWallpaperItem(11200), CatalogFlooringItem(10000), CatalogFlooringItem(10010))), (2, 1, 2, 14, ((3, 2920), CatalogClothingItem(1200, 0), CatalogClothingItem(1201, 0), CatalogClothingItem(1202, 0), CatalogClothingItem(1203, 0), CatalogClothingItem(1204, 0), CatalogClothingItem(1205, 0), CatalogWallpaperItem(12000), CatalogWallpaperItem(12100), CatalogWallpaperItem(12200), CatalogWallpaperItem(12300), CatalogWainscotingItem(1030, 0), CatalogWainscotingItem(1030, 1), CatalogMouldingItem(1060, 0), CatalogMouldingItem(1060, 1))))
WeeklySchedule = ((100, (5, 2000), 3000, 3500, 4000, 4500, CatalogEmoteItem(5), CatalogFurnitureItem(210, 0), CatalogFurnitureItem(220, 0)), (100, (5, 2000), CatalogFurnitureItem(1400), 3000, 3500, 4000, 4500, CatalogFurnitureItem(600), CatalogFurnitureItem(610), CatalogClothingItem(116, 0), CatalogClothingItem(216, 0)), (300, (5, 2000), CatalogFurnitureItem(1410), 3000, 3500, 4000, 4500, CatalogFurnitureItem(1100), CatalogFurnitureItem(1020), CatalogClothingItem(408, 0)), (100, (5, 2000), CatalogWindowItem(40), 3000, 3500, 4000, 4500, CatalogFurnitureItem(110), CatalogFurnitureItem(100), nextAvailablePole), (100, (5, 2000), CatalogFurnitureItem(1420), CatalogEmoteItem(9), 3000, 3500, 4000, 4500, CatalogFurnitureItem(700), CatalogFurnitureItem(710)), (300, (5, 2000), 3000, 3500, 4000, 4500, CatalogFurnitureItem(410), CatalogFurnitureItem(1000), nextAvailableBank, CatalogClothingItem(117, 0), CatalogClothingItem(217, 0)), (100, (5, 2000), CatalogFurnitureItem(1430), 3000, 3500, 4000, 4500, CatalogFurnitureItem(1510), CatalogFurnitureItem(1610)), (100, (5, 2000), CatalogWindowItem(70), 3000, 3500, 4000, 4500, CatalogFurnitureItem(1210), CatalogClothingItem(409, 0), nextAvailablePole), (300, (5, 2000), CatalogEmoteItem(13), 3000, 3500, 4000, 4500, CatalogFurnitureItem(1200), CatalogFurnitureItem(900)), (100, (5, 2000), 3000, 3500, 4000, 4500, CatalogFurnitureItem(910), CatalogFurnitureItem(1600), CatalogClothingItem(118, 0), CatalogClothingItem(218, 0)), (100, (5, 2000), 3000, 3500, 4000, 4500, CatalogFurnitureItem(800), CatalogFurnitureItem(1010), CatalogClothingItem(410, 0)), (300, (5, 2000), 3000, 3500, 4000, 4500, CatalogFurnitureItem(620), nextAvailableBank, nextAvailablePole), (300, (5, 2000), 3000, 3500, 4000, 4500, CatalogFurnitureItem(502), CatalogFurnitureItem(512), CatalogClothingItem(119, 0), CatalogClothingItem(219, 0)), (100, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(1110), CatalogFurnitureItem(630), CatalogFurnitureItem(1630), CatalogEmoteItem(11)), (100, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(230), CatalogFurnitureItem(920), CatalogFurnitureItem(1440)), (300, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(420), CatalogFurnitureItem(120), CatalogClothingItem(120, 0), CatalogClothingItem(220, 0), nextAvailablePole), (100, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(1700), CatalogFurnitureItem(640), CatalogWindowItem(50)), (100, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(1120), CatalogFurnitureItem(930), CatalogFurnitureItem(1500), CatalogEmoteItem(6)), (300, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(430), CatalogFurnitureItem(1620), CatalogFurnitureItem(1442), nextAvailableBank), (100, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(610), CatalogFurnitureItem(940), CatalogClothingItem(121, 0), CatalogClothingItem(221, 0), nextAvailablePole), (100, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(1710), CatalogFurnitureItem(1030), CatalogWindowItem(60)), (300, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(1130), CatalogFurnitureItem(130), CatalogEmoteItem(8)), (100, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(1530), CatalogFurnitureItem(1640), CatalogFurnitureItem(1441)), (100, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(300), CatalogFurnitureItem(1220), nextAvailablePole), (300, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(810), CatalogFurnitureItem(1230), CatalogFurnitureItem(1443), nextAvailableBank), (300, (2, 2000), (3, 2010), 3010, 3510, 4010, 4510, CatalogFurnitureItem(310), CatalogFurnitureItem(1520), CatalogFurnitureItem(1650), CatalogWindowItem(80), CatalogClothingItem(222, 0)), (100, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogFurnitureItem(1240), CatalogFurnitureItem(1661), CatalogEmoteItem(5)), (100, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogFurnitureItem(1800), CatalogFurnitureItem(240), CatalogFurnitureItem(1200)), (300, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogFurnitureItem(145), CatalogClothingItem(123, 0), CatalogClothingItem(224, 0), nextAvailablePole), (100, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogWindowItem(100), CatalogFurnitureItem(1810)), (100, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogFurnitureItem(650), CatalogFurnitureItem(1900)), (300, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogFurnitureItem(1725), nextAvailableBank), (100, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogWindowItem(90), CatalogClothingItem(124, 0), CatalogClothingItem(411, 0)), (100, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogFurnitureItem(140), CatalogFurnitureItem(1020), CatalogEmoteItem(13)), (300, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogFurnitureItem(950), CatalogFurnitureItem(1660), CatalogClothingItem(310, 0)), (100, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogFurnitureItem(660), CatalogFurnitureItem(1200)), (100, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogFurnitureItem(1910), nextAvailablePole, CatalogFurnitureItem(1000)), (300, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogFurnitureItem(1720), nextAvailableBank, CatalogEmoteItem(9)), (300, (1, 2000), (2, 2010), (3, 2020), 3020, 3530, 4020, 4520, CatalogWindowItem(110), CatalogClothingItem(311, 0)))

class CatalogGenerator:
    notify = DirectNotifyGlobal.directNotify.newCategory('CatalogGenerator')
    
    def __init__(self):
        self._CatalogGenerator__itemLists = { }

    
    def generateMonthlyCatalog(self, avatar, weekStart):
        dayNumber = int(weekStart / 24 * 60)
        itemLists = self._CatalogGenerator__getMonthlyItemLists(dayNumber, weekStart)
        monthlyCatalog = CatalogItemList.CatalogItemList()
        for list in itemLists:
            for item in list:
                monthlyCatalog += self._CatalogGenerator__selectItem(avatar, item, [])
            
        
        return monthlyCatalog

    
    def generateWeeklyCatalog(self, avatar, week):
        weeklyCatalog = CatalogItemList.CatalogItemList()
        self.notify.debug('Generating catalog for %s for week %s.' % (avatar.doId, week))
        if week >= 1 and week <= len(WeeklySchedule):
            for item in WeeklySchedule[week - 1]:
                weeklyCatalog += self._CatalogGenerator__selectItem(avatar, item, [])
            
        
        self.notify.debug('Generated catalog: %s' % weeklyCatalog)
        return weeklyCatalog

    
    def generateBackCatalog(self, avatar, week, previousWeek, weeklyCatalog):
        backCatalog = CatalogItemList.CatalogItemList()
        lastBackCatalog = avatar.backCatalog[:]
        thisWeek = min(len(WeeklySchedule), week - 1)
        lastWeek = min(len(WeeklySchedule), previousWeek)
        for week in range(thisWeek, lastWeek, -1):
            self.notify.debug('Adding items from week %s to back catalog' % week)
            for item in WeeklySchedule[week - 1]:
                for item in self._CatalogGenerator__selectItem(avatar, item, weeklyCatalog + backCatalog):
                    item.putInBackCatalog(backCatalog, lastBackCatalog)
                
            
        
        if previousWeek < week:
            self.notify.debug('Adding current items from week %s to back catalog' % previousWeek)
            for item in avatar.weeklyCatalog:
                item.putInBackCatalog(backCatalog, lastBackCatalog)
            
        
        backCatalog += lastBackCatalog
        for item in weeklyCatalog:
            while item in backCatalog:
                backCatalog.remove(item)
        
        return backCatalog

    
    def _CatalogGenerator__getMonthlyItemLists(self, dayNumber, weekStart):
        itemLists = self._CatalogGenerator__itemLists.get(dayNumber)
        if itemLists != None:
            return itemLists
        
        nowtuple = time.localtime(weekStart * 60)
        month = nowtuple[1]
        day = nowtuple[2]
        self.notify.debug('Generating seasonal itemLists for %s/%s.' % (month, day))
        itemLists = []
        for (startMM, startDD, endMM, endDD, list) in MonthlySchedule:
            if month > startMM and month == startMM:
                pass
            pastStart = day >= startDD
            if month < endMM and month == endMM:
                pass
            beforeEnd = day <= endDD
            if endMM < startMM:
                if pastStart or beforeEnd:
                    itemLists.append(list)
                
            elif pastStart and beforeEnd:
                itemLists.append(list)
            
        
        self._CatalogGenerator__itemLists[dayNumber] = itemLists
        return itemLists

    
    def _CatalogGenerator__selectItem(self, avatar, item, duplicateItems):
        chooseCount = 1
        if callable(item):
            item = item(avatar, duplicateItems)
        
        if isinstance(item, types.TupleType):
            (chooseCount, item) = item
        
        if isinstance(item, types.IntType):
            item = MetaItems[item]
        
        selection = []
        if isinstance(item, CatalogItem.CatalogItem):
            if not item.notOfferedTo(avatar):
                selection.append(item)
            
        elif item != None:
            list = item[:]
            for i in range(chooseCount):
                if len(list) == 0:
                    return selection
                
                item = self._CatalogGenerator__chooseFromList(avatar, list, duplicateItems)
                if item != None:
                    selection.append(item)
                
            
        
        return selection

    
    def _CatalogGenerator__chooseFromList(self, avatar, list, duplicateItems):
        index = random.randrange(len(list))
        item = list[index]
        del list[index]
        while item.notOfferedTo(avatar) and item.reachedPurchaseLimit(avatar) and item in duplicateItems and item in avatar.backCatalog or item in avatar.weeklyCatalog:
            if len(list) == 0:
                return None
            
            index = random.randrange(len(list))
            item = list[index]
            del list[index]
        return item

    
    def outputSchedule(self, filename):
        out = open(Filename(filename).toOsSpecific(), 'w')
        sched = self.generateScheduleDictionary()
        items = sched.keys()
        items.sort()
        for item in items:
            (weeklist, maybeWeeklist) = sched[item]
            color = self._CatalogGenerator__formatColor(item.getColor())
            seriesDict = { }
            self._CatalogGenerator__determineSeries(seriesDict, weeklist)
            self._CatalogGenerator__determineSeries(seriesDict, maybeWeeklist)
            seriesList = seriesDict.keys()
            seriesList.sort()
            series = str(seriesList)[1:-1]
            week = self._CatalogGenerator__formatWeeklist(weeklist)
            maybeWeek = self._CatalogGenerator__formatWeeklist(maybeWeeklist)
            line = '"%s"\t"%s"\t"%s"\t%s\t"%s"\t"%s"\t"%s"\t"%s"\t"%s"' % (item.output(store = 0), item.getTypeName(), item.getDisplayName(), item.getBasePrice(), item.getFilename(), color, series, week, maybeWeek)
            out.write(line + '\n')
        
        out.close()

    
    def _CatalogGenerator__formatColor(self, color):
        if color == None:
            return ''
        else:
            return '(%0.2f, %0.2f, %0.2f)' % (color[0], color[1], color[2])

    
    def _CatalogGenerator__determineSeries(self, seriesDict, weeklist):
        for week in weeklist:
            if isinstance(week, types.IntType):
                series = (week - 1) / ToontownGlobals.CatalogNumWeeksPerSeries + 1
                seriesDict[series] = None
            
        

    
    def _CatalogGenerator__formatWeeklist(self, weeklist):
        str = ''
        for week in weeklist:
            str += ', %s' % week
        
        return str[2:]

    
    def generateScheduleDictionary(self):
        sched = { }
        for index in range(len(WeeklySchedule)):
            week = index + 1
            self._CatalogGenerator__recordSchedule(sched, week, WeeklySchedule[index])
        
        for (startMM, startDD, endMM, endDD, list) in MonthlySchedule:
            string = '%02d/%02d - %02d/%02d' % (startMM, startDD, endMM, endDD)
            self._CatalogGenerator__recordSchedule(sched, string, list)
        
        return sched

    
    def _CatalogGenerator__recordSchedule(self, sched, weekCode, schedule):
        for item in schedule:
            if callable(item):
                if item == nextAvailablePole:
                    item = getAllPoles()
                elif item == nextAvailableBank:
                    item = getAllBanks()
                else:
                    self.notify.warning("Don't know how to interpret function " % repr(name))
                    item = None
            elif isinstance(item, types.TupleType):
                item = item[1]
            
            if isinstance(item, types.IntType):
                item = MetaItems[item]
            
            if isinstance(item, CatalogItem.CatalogItem):
                self._CatalogGenerator__recordScheduleItem(sched, weekCode, None, item)
            elif item != None:
                if item == MetaItems[3020] or item == MetaItems[3010]:
                    print '%s: %s' % (weekCode, item)
                
                for i in item:
                    self._CatalogGenerator__recordScheduleItem(sched, None, weekCode, i)
                
            
        

    
    def _CatalogGenerator__recordScheduleItem(self, sched, weekCode, maybeWeekCode, item):
        if not sched.has_key(item):
            sched[item] = [
                [],
                []]
        
        if item == CatalogWallpaperItem(2900) or item == CatalogWallpaperItem(2210):
            print '%s,%s: %s' % (item, maybeWeekCode, sched[item])
        
        if weekCode != None:
            sched[item][0].append(weekCode)
        
        if maybeWeekCode != None:
            sched[item][1].append(maybeWeekCode)
        


