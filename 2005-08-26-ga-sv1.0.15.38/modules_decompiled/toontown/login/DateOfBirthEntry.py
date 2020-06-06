# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase.DirectObject import *
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer

class DateOfBirthEntry(DirectFrame):
    
    def __init__(self, showDay = 1, firstYear = 1900, defaultAge = 10, curYear = None, monthHandler = None, yearHandler = None, dayHandler = None, dateObject = None, parent = aspect2d, **kw):
        if dateObject:
            self.dateObject = dateObject
        else:
            self.dateObject = base.cr.dateObject
        self.showDay = showDay
        self.firstYear = firstYear
        self.defaultAge = defaultAge
        self.setMonthHandler(None)
        self.setYearHandler(None)
        self.setDayHandler(None)
        optiondefs = { }
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent, relief = None)
        self.initialiseoptions(DateOfBirthEntry)
        gui = loader.loadModel('phase_3/models/gui/month_year_gui')
        bS = 14
        normalColor = (0.90000000000000002, 0.59999999999999998, 0.10000000000000001, 1)
        downColor = (0.20000000000000001, 0.59999999999999998, 1, 1)
        overColor = (1, 1, 0, 1)
        disabledColor = (0.5, 0.5, 0.5, 1)
        incButtonPos = (1.75, 0, -0.10000000000000001)
        decButtonPos = (1.75, 0, 0.59999999999999998)
        itemFrameScale = 0.80000000000000004
        imagePos = (0.5, 0, 0.25)
        imageScale = 12
        w = 4
        posTable = ((-0.75, 0, 0), (-0.75 + w, 0, 0), (-0.75 + w * 2, 0, 0))
        self.months = TTLocalizer.DateOfBirthEntryMonths
        self.monthControl = DirectScrolledList(parent = self, relief = None, items = self.months, image = gui.find('**/month-yearPanel'), image_scale = imageScale, image_pos = imagePos, incButton_image = gui.find('**/smallVerticalArrow'), incButton_relief = None, incButton_scale = (bS, bS, -bS), incButton_pos = incButtonPos, incButton_image0_color = normalColor, incButton_image1_color = downColor, incButton_image2_color = overColor, incButton_image3_color = disabledColor, decButton_image = gui.find('**/smallVerticalArrow'), decButton_relief = None, decButton_scale = (bS, bS, bS), decButton_pos = decButtonPos, decButton_image0_color = normalColor, decButton_image1_color = downColor, decButton_image2_color = overColor, decButton_image3_color = disabledColor, pos = posTable[0], itemFrame_pos = (0, 0, 0), itemFrame_scale = itemFrameScale, itemFrame_relief = None)
        self.days = range(1, 31 + 1)
        strDays = map(str, self.days)
        self.dayControl = DirectScrolledList(parent = self, relief = None, items = strDays, image = gui.find('**/month-yearPanel'), image_scale = imageScale, image_pos = imagePos, incButton_image = gui.find('**/smallVerticalArrow'), incButton_relief = None, incButton_scale = (bS, bS, bS), incButton_pos = decButtonPos, incButton_image0_color = normalColor, incButton_image1_color = downColor, incButton_image2_color = overColor, incButton_image3_color = disabledColor, decButton_image = gui.find('**/smallVerticalArrow'), decButton_relief = None, decButton_scale = (bS, bS, -bS), decButton_pos = incButtonPos, decButton_image0_color = normalColor, decButton_image1_color = downColor, decButton_image2_color = overColor, decButton_image3_color = disabledColor, pos = posTable[1], itemFrame_pos = (0, 0, 0), itemFrame_scale = itemFrameScale, itemFrame_relief = None)
        self.lastChosenDay = self.getDay()
        if curYear == None:
            curYear = self.dateObject.getYear()
        
        self.years = range(self.firstYear, curYear + 1)
        self.years.reverse()
        strYears = map(str, self.years)
        self.yearControl = DirectScrolledList(parent = self, items = strYears, relief = None, image = gui.find('**/month-yearPanel'), image_scale = imageScale, image_pos = imagePos, incButton_image = gui.find('**/smallVerticalArrow'), incButton_relief = None, incButton_scale = (bS, bS, -bS), incButton_pos = incButtonPos, incButton_image0_color = normalColor, incButton_image1_color = downColor, incButton_image2_color = overColor, incButton_image3_color = disabledColor, decButton_image = gui.find('**/smallVerticalArrow'), decButton_relief = None, decButton_scale = (bS, bS, bS), decButton_pos = decButtonPos, decButton_image0_color = normalColor, decButton_image1_color = downColor, decButton_image2_color = overColor, decButton_image3_color = disabledColor, pos = posTable[2], itemFrame_pos = (0, 0, 0), itemFrame_scale = itemFrameScale, itemFrame_relief = None)
        self.setYear(curYear - self.defaultAge)
        if not (self.showDay):
            self.dayControl.hide()
            self.yearControl.setPos(posTable[1])
        
        self.monthControl['command'] = self._DateOfBirthEntry__handleMonth
        self.yearControl['command'] = self._DateOfBirthEntry__handleYear
        self.dayControl['command'] = self._DateOfBirthEntry__handleDay
        self.setMonthHandler(monthHandler)
        self.setYearHandler(yearHandler)
        self.setDayHandler(dayHandler)
        gui.removeNode()

    
    def destroy(self):
        del self.monthHandler
        del self.dayHandler
        del self.yearHandler
        DirectFrame.destroy(self)

    
    def getMonth(self):
        month = self.monthControl.getSelectedText()
        return self.months.index(month) + 1

    
    def getDay(self):
        return int(self.dayControl.getSelectedText())

    
    def getYear(self):
        return int(self.yearControl.getSelectedText())

    
    def setMonth(self, month):
        if month in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12]:
            self.monthControl.scrollTo(month - 1)
        else:
            print 'month not found in list: %s' % month
            self.monthControl.scrollTo(0)
        self._DateOfBirthEntry__updateDaysInMonth()

    
    def setDay(self, day):
        if day in self.days:
            self.dayControl.scrollTo(self.days.index(day))
        else:
            print 'day not found in list: %s' % day
            self.dayControl.scrollTo(0)

    
    def setYear(self, year):
        if year in self.years:
            self.yearControl.scrollTo(self.years.index(year))
        else:
            print 'year not found in list: %s' % year
            self.yearControl.scrollTo(0)
        self._DateOfBirthEntry__updateDaysInMonth()

    
    def getAge(self):
        return self.dateObject.getAge(self.getMonth(), self.getYear())

    
    def setMonthHandler(self, handler):
        self.monthHandler = handler

    
    def setDayHandler(self, handler):
        self.dayHandler = handler

    
    def setYearHandler(self, handler):
        self.yearHandler = handler

    
    def _DateOfBirthEntry__handleMonth(self):
        self._DateOfBirthEntry__updateDaysInMonth()
        if self.monthHandler:
            self.monthHandler(self.getMonth())
        

    
    def _DateOfBirthEntry__handleDay(self):
        self.lastChosenDay = self.getDay()
        if self.dayHandler:
            self.dayHandler(self.getDay())
        

    
    def _DateOfBirthEntry__handleYear(self):
        self._DateOfBirthEntry__updateDaysInMonth()
        if self.yearHandler:
            self.yearHandler(self.getYear())
        

    
    def _DateOfBirthEntry__updateDaysInMonth(self):
        lastChosenDay = self.lastChosenDay
        oldNumDays = len(self.days)
        numDays = self.dateObject.getNumDaysInMonth(month = self.getMonth(), year = self.getYear())
        self.days = range(1, numDays + 1)
        self._DateOfBirthEntry__updateDayControlLength(oldNumDays, numDays)
        day = lastChosenDay
        if not (day in self.days):
            day = self.days[-1]
        
        self.setDay(day)
        self.lastChosenDay = lastChosenDay

    
    def _DateOfBirthEntry__updateDayControlLength(self, oldDays, newDays):
        if oldDays > newDays:
            for day in range(oldDays, newDays, -1):
                self.dayControl.removeItem(self.dayControl['items'][day - 1])
            
        elif oldDays < newDays:
            for day in range(oldDays + 1, newDays + 1):
                self.dayControl.addItem(str(day))
            
        


