# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedToonHallInteriorAI.py
from DistributedToonInteriorAI import *
from toontown.toonbase import ToontownGlobals

class DistributedToonHallInteriorAI(DistributedToonInteriorAI):
    __module__ = __name__

    def __init__(self, block, air, zoneId, building):
        DistributedToonInteriorAI.__init__(self, block, air, zoneId, building)
        self.accept('ToonEnteredZone', self.logToonEntered)
        self.accept('ToonLeftZone', self.logToonLeft)

    def logToonEntered(self, avId, zoneId):
        result = self.getCurPhase()
        if result == -1:
            phase = 'not available'
        else:
            phase = str(result)
        self.air.writeServerEvent('sillyMeter', avId, 'enter|%s' % phase)

    def logToonLeft(self, avId, zoneId):
        result = self.getCurPhase()
        if result == -1:
            phase = 'not available'
        else:
            phase = str(result)
        self.air.writeServerEvent('sillyMeter', avId, 'exit|%s' % phase)

    def getCurPhase(self):
        result = -1
        enoughInfoToRun = False
        if ToontownGlobals.SILLYMETER_HOLIDAY in simbase.air.holidayManager.currentHolidays and simbase.air.holidayManager.currentHolidays[ToontownGlobals.SILLYMETER_HOLIDAY] != None and simbase.air.holidayManager.currentHolidays[ToontownGlobals.SILLYMETER_HOLIDAY].getRunningState():
            if hasattr(simbase.air, 'SillyMeterMgr'):
                enoughInfoToRun = True
            else:
                self.notify.debug('simbase.air does not have SillyMeterMgr')
        else:
            self.notify.debug('holiday is not running')
        self.notify.debug('enoughInfoToRun = %s' % enoughInfoToRun)
        if enoughInfoToRun and simbase.air.SillyMeterMgr.getIsRunning():
            result = simbase.air.SillyMeterMgr.getCurPhase()
        return result

    def delete(self):
        self.ignoreAll()
        DistributedToonInteriorAI.delete(self)