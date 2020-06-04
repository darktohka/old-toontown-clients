# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\login\TTDateObject.py
import DateObject

class TTDateObject(DateObject.DateObject):
    __module__ = __name__

    def __init__(self, accountServerDate):
        self.accountServerDate = accountServerDate

    def getYear(self):
        return self.accountServerDate.getYear()

    def getMonth(self):
        return self.accountServerDate.getMonth()

    def getDay(self):
        return self.accountServerDate.getDay()

    def getDetailedAge(self, dobMonth, dobYear, dobDay=None, curMonth=None, curYear=None, curDay=None):
        return DateObject.DateObject.getDetailedAge(self, dobMonth, dobYear, dobDay, curMonth=self.getMonth(), curYear=self.getYear(), curDay=self.getDay())

    def getAge(self, dobMonth, dobYear, dobDay=None, curMonth=None, curYear=None, curDay=None):
        return TTDateObject.getDetailedAge(self, dobMonth, dobYear, dobDay=dobDay, curMonth=curMonth, curYear=curYear, curDay=curDay)[0]