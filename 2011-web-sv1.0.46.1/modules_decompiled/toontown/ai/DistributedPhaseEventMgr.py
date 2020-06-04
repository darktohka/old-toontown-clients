# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\ai\DistributedPhaseEventMgr.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
import datetime

class DistributedPhaseEventMgr(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPhaseEventMgr')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.holidayDates = []

    def setIsRunning(self, isRunning):
        self.isRunning = isRunning

    def setNumPhases(self, numPhases):
        self.numPhases = numPhases

    def setCurPhase(self, curPhase):
        self.curPhase = curPhase

    def getIsRunning(self):
        return self.isRunning

    def getNumPhases(self):
        return self.numPhases

    def getCurPhase(self):
        return self.curPhase

    def setDates(self, holidayDates):
        for holidayDate in holidayDates:
            self.holidayDates.append(datetime.datetime(holidayDate[0], holidayDate[1], holidayDate[2], holidayDate[3], holidayDate[4], holidayDate[5]))