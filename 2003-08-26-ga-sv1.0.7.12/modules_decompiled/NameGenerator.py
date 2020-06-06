# File: N (Python 2.2)

from ShowBaseGlobal import *
import whrandom
import string
import copy
import ToontownGlobals
import Localizer
import os
import DirectNotifyGlobal

class NameGenerator:
    font = ToontownGlobals.getInterfaceFont()
    notify = DirectNotifyGlobal.directNotify.newCategory('NameGenerator')
    boyTitles = []
    girlTitles = []
    neutralTitles = []
    boyFirsts = []
    girlFirsts = []
    neutralFirsts = []
    capPrefixes = []
    lastPrefixes = []
    lastSuffixes = []
    
    def __init__(self):
        self.generateLists()
        return None

    
    def generateLists(self):
        self.boyTitles = []
        self.girlTitles = []
        self.neutralTitles = []
        self.boyFirsts = []
        self.girlFirsts = []
        self.neutralFirsts = []
        self.capPrefixes = []
        self.lastPrefixes = []
        self.lastSuffixes = []
        self.nameDictionary = { }
        searchPath = DSearchPath()
        searchPath.appendDirectory(Filename('phase_3/etc'))
        searchPath.appendDirectory(Filename.fromOsSpecific(os.path.expandvars('$TOONTOWN/src/configfiles')))
        filename = Filename(Localizer.NameShopNameMaster)
        if vfs:
            found = vfs.resolveFilename(filename, searchPath)
        else:
            found = filename.resolveFilename(searchPath)
        if not found:
            self.notify.error('NameGenerator: Error opening name list text file.')
        
        if vfs:
            input = StreamReader(vfs.openReadFile(filename), 1)
        else:
            input = open(filename.toOsSpecific(), 'r')
        currentLine = input.readline()
        while currentLine:
            if currentLine.lstrip()[0:1] != '#':
                a1 = currentLine.find('*')
                a2 = currentLine.find('*', a1 + 1)
                self.nameDictionary[int(currentLine[0:a1])] = (int(currentLine[a1 + 1:a2]), currentLine[a2 + 1:len(currentLine) - 1])
            
            currentLine = input.readline()
        masterList = [
            self.boyTitles,
            self.girlTitles,
            self.neutralTitles,
            self.boyFirsts,
            self.girlFirsts,
            self.neutralFirsts,
            self.capPrefixes,
            self.lastPrefixes,
            self.lastSuffixes]
        for tu in self.nameDictionary.values():
            masterList[tu[0]].append(tu[1])
        
        return 1

    
    def returnUniqueID(self, name, listnumber):
        newtu = [
            (),
            (),
            ()]
        if listnumber == 0:
            newtu[0] = (0, name)
            newtu[1] = (1, name)
            newtu[2] = (2, name)
        elif listnumber == 1:
            newtu[0] = (3, name)
            newtu[1] = (4, name)
            newtu[2] = (5, name)
        elif listnumber == 2:
            newtu[0] = (6, name)
            newtu[1] = (7, name)
        else:
            newtu[0] = (8, name)
        for tu in self.nameDictionary.items():
            for g in newtu:
                if tu[1] == g:
                    return tu[0]
                
            
        
        return -1

    
    def findWidestInList(self, font, nameList):
        maxWidth = 0
        maxName = ''
        for name in nameList:
            width = font.calcWidth(name)
            if width > maxWidth:
                maxWidth = font.calcWidth(name)
                maxName = name
            
        
        print maxName + ' ' + str(maxWidth)
        return maxName

    
    def findWidestName(self):
        longestBoyTitle = self.findWidestInList(self.font, self.boyTitles + self.neutralTitles)
        longestGirlTitle = self.findWidestInList(self.font, self.girlTitles + self.neutralTitles)
        longestBoyFirst = self.findWidestInList(self.font, self.boyFirsts + self.neutralFirsts)
        longestGirlFirst = self.findWidestInList(self.font, self.girlFirsts + self.neutralFirsts)
        longestLastPrefix = self.findWidestInList(self.font, self.lastPrefixes)
        longestLastSuffix = self.findWidestInList(self.font, self.lastSuffixes)
        longestBoyFront = self.findWidestInList(self.font, [
            longestBoyTitle,
            longestBoyFirst])
        longestGirlFront = self.findWidestInList(self.font, [
            longestGirlTitle,
            longestGirlFirst])
        longestBoyName = longestBoyTitle + ' ' + longestBoyFirst + ' ' + longestLastPrefix + longestLastSuffix
        longestGirlName = longestGirlTitle + ' ' + longestGirlFirst + ' ' + longestLastPrefix + longestLastSuffix
        longestName = self.findWidestInList(self.font, [
            longestBoyName,
            longestGirlName])
        return longestName

    
    def findWidestTitleFirst(self):
        longestBoyTitle = self.findWidestInList(self.font, self.boyTitles + self.neutralTitles)
        longestGirlTitle = self.findWidestInList(self.font, self.girlTitles + self.neutralTitles)
        longestBoyFirst = self.findWidestInList(self.font, self.boyFirsts + self.neutralFirsts)
        longestGirlFirst = self.findWidestInList(self.font, self.girlFirsts + self.neutralFirsts)
        longestBoyName = longestBoyTitle + ' ' + longestBoyFirst
        longestGirlName = longestGirlTitle + ' ' + longestGirlFirst
        longestName = self.findWidestInList(self.font, [
            longestBoyName,
            longestGirlName])

    
    def findWidestTitle(self):
        widestTitle = self.findWidestInList(self.font, self.neutralTitles + self.boyTitles + self.girlTitles)
        return widestTitle

    
    def findWidestFirstName(self):
        widestFirst = self.findWidestInList(self.font, self.neutralFirsts + self.boyFirsts + self.girlFirsts)
        return widestFirst

    
    def findWidestLastName(self):
        longestLastPrefix = self.findWidestInList(self.font, self.lastPrefixes)
        longestLastSuffix = self.findWidestInList(self.font, self.lastSuffixes)
        longestLastName = longestLastPrefix + longestLastSuffix
        return longestLastName

    
    def findWidestNameWord(self):
        widestWord = self.findWidestInList(self.font, [
            self.findWidestTitle(),
            self.findWidestFirstName(),
            self.findWidestLastName()])
        return widestWord

    
    def findWidestNameWidth(self):
        name = self.findWidestName()
        return self.font.calcWidth(name)

    
    def printWidestName(self):
        name = self.findWidestName()
        width = self.font.calcWidth(name)
        widthStr = str(width)
        print 'The widest name is: ' + name + ' (' + widthStr + ' units)'

    
    def printWidestLastName(self):
        name = self.findWidestLastName()
        width = self.font.calcWidth(name)
        widthStr = str(width)
        print 'The widest last name is: ' + name + ' (' + widthStr + ' units)'

    
    def randomName(self, boy = 0, girl = 0):
        if boy and girl:
            self.error("A name can't be both boy and girl!")
        
        if not boy and not girl:
            boy = whrandom.choice([
                0,
                1])
            girl = not boy
        
        uberFlag = whrandom.choice([
            'title-first',
            'title-last',
            'first',
            'last',
            'first-last',
            'title-first-last'])
        titleFlag = 0
        if uberFlag == 'title-first' and uberFlag == 'title-last' or uberFlag == 'title-first-last':
            titleFlag = 1
        
        firstFlag = 0
        if uberFlag == 'title-first' and uberFlag == 'first' and uberFlag == 'first-last' or uberFlag == 'title-first-last':
            firstFlag = 1
        
        lastFlag = 0
        if uberFlag == 'title-last' and uberFlag == 'last' and uberFlag == 'first-last' or uberFlag == 'title-first-last':
            lastFlag = 1
        
        retString = ''
        if titleFlag:
            titleList = self.neutralTitles[:]
            if boy:
                titleList += self.boyTitles
            elif girl:
                titleList += self.girlTitles
            else:
                self.error('Must be boy or girl.')
            retString += whrandom.choice(titleList) + ' '
        
        if firstFlag:
            firstList = self.neutralFirsts[:]
            if boy:
                firstList += self.boyFirsts
            elif girl:
                firstList += self.girlFirsts
            else:
                self.error('Must be boy or girl.')
            retString += whrandom.choice(firstList)
            if lastFlag:
                retString += ' '
            
        
        if lastFlag:
            lastPrefix = whrandom.choice(self.lastPrefixes)
            lastSuffix = whrandom.choice(self.lastSuffixes)
            if lastPrefix in self.capPrefixes:
                lastSuffix = lastSuffix.capitalize()
            
            retString += lastPrefix + lastSuffix
        
        return retString

    
    def randomNameMoreinfo(self, boy = 0, girl = 0):
        if boy and girl:
            self.error("A name can't be both boy and girl!")
        
        if not boy and not girl:
            boy = whrandom.choice([
                0,
                1])
            girl = not boy
        
        uberFlag = whrandom.choice([
            'title-first',
            'title-last',
            'first',
            'last',
            'first-last',
            'title-first-last'])
        titleFlag = 0
        if uberFlag == 'title-first' and uberFlag == 'title-last' or uberFlag == 'title-first-last':
            titleFlag = 1
        
        firstFlag = 0
        if uberFlag == 'title-first' and uberFlag == 'first' and uberFlag == 'first-last' or uberFlag == 'title-first-last':
            firstFlag = 1
        
        lastFlag = 0
        if uberFlag == 'title-last' and uberFlag == 'last' and uberFlag == 'first-last' or uberFlag == 'title-first-last':
            lastFlag = 1
        
        retString = ''
        uberReturn = [
            0,
            0,
            0,
            '',
            '',
            '',
            '']
        uberReturn[0] = titleFlag
        uberReturn[1] = firstFlag
        uberReturn[2] = lastFlag
        titleList = self.neutralTitles[:]
        if boy:
            titleList += self.boyTitles
        elif girl:
            titleList += self.girlTitles
        else:
            self.error('Must be boy or girl.')
        uberReturn[3] = whrandom.choice(titleList)
        firstList = self.neutralFirsts[:]
        if boy:
            firstList += self.boyFirsts
        elif girl:
            firstList += self.girlFirsts
        else:
            self.error('Must be boy or girl.')
        uberReturn[4] = whrandom.choice(firstList)
        lastPrefix = whrandom.choice(self.lastPrefixes)
        lastSuffix = whrandom.choice(self.lastSuffixes)
        if lastPrefix in self.capPrefixes:
            lastSuffix = lastSuffix.capitalize()
        
        uberReturn[5] = lastPrefix
        uberReturn[6] = lastSuffix
        if titleFlag:
            retString += uberReturn[3] + ' '
        
        if firstFlag:
            retString += uberReturn[4]
            if lastFlag:
                retString += ' '
            
        
        if lastFlag:
            retString += uberReturn[5] + uberReturn[6]
        
        uberReturn.append(retString)
        return uberReturn

    
    def printRandomNames(self, boy = 0, girl = 0, total = 1):
        i = 0
        origBoy = boy
        origGirl = girl
        while i < total:
            if not origBoy and not origGirl:
                boy = whrandom.choice([
                    0,
                    1])
                girl = not boy
            
            name = self.randomName(boy, girl)
            width = self.font.calcWidth(name)
            widthStr = str(width)
            if boy:
                print 'Boy: ' + name + ' (' + widthStr + ' units)'
            
            if girl:
                print 'Girl: ' + name + ' (' + widthStr + ' units)'
            
            i += 1

    
    def percentOver(self, limit = 9.0, samples = 1000):
        i = 0
        over = 0
        while i < samples:
            name = self.randomName()
            width = self.font.calcWidth(name)
            if width > limit:
                over += 1
            
            i += 1
        percent = (float(over) / float(samples)) * 100
        print 'Samples: ' + str(samples) + ' Over: ' + str(over) + ' Percent: ' + str(percent)

    
    def totalNames(self):
        firsts = len(self.boyFirsts) + len(self.girlFirsts) + len(self.neutralFirsts)
        print 'Total firsts: ' + str(firsts)
        lasts = len(self.lastPrefixes) * len(self.lastSuffixes)
        print 'Total lasts: ' + str(lasts)
        neutralTitleFirsts = len(self.neutralTitles) * len(self.neutralFirsts)
        boyTitleFirsts = len(self.boyTitles) * (len(self.neutralFirsts) + len(self.boyFirsts)) + len(self.neutralTitles) * len(self.boyFirsts)
        girlTitleFirsts = len(self.girlTitles) * (len(self.neutralFirsts) + len(self.girlFirsts)) + len(self.neutralTitles) * len(self.girlFirsts)
        totalTitleFirsts = neutralTitleFirsts + boyTitleFirsts + girlTitleFirsts
        print 'Total title firsts: ' + str(totalTitleFirsts)
        neutralTitleLasts = len(self.neutralTitles) * lasts
        boyTitleLasts = len(self.boyTitles) * lasts
        girlTitleLasts = len(self.girlTitles) * lasts
        totalTitleLasts = neutralTitleLasts + boyTitleFirsts + girlTitleLasts
        print 'Total title lasts: ' + str(totalTitleLasts)
        neutralFirstLasts = len(self.neutralFirsts) * lasts
        boyFirstLasts = len(self.boyFirsts) * lasts
        girlFirstLasts = len(self.girlFirsts) * lasts
        totalFirstLasts = neutralFirstLasts + boyFirstLasts + girlFirstLasts
        print 'Total first lasts: ' + str(totalFirstLasts)
        neutralTitleFirstLasts = neutralTitleFirsts * lasts
        boyTitleFirstLasts = boyTitleFirsts * lasts
        girlTitleFirstLasts = girlTitleFirsts * lasts
        totalTitleFirstLasts = neutralTitleFirstLasts + boyTitleFirstLasts + girlTitleFirstLasts
        print 'Total title first lasts: ' + str(totalTitleFirstLasts)
        totalNames = firsts + lasts + totalTitleFirsts + totalTitleLasts + totalFirstLasts + totalTitleFirstLasts
        print 'Total Names: ' + str(totalNames)


