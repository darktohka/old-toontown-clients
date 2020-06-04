# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\ai\DistributedSillyMeterMgr.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from toontown.ai import DistributedPhaseEventMgr
import time

class DistributedSillyMeterMgr(DistributedPhaseEventMgr.DistributedPhaseEventMgr):
    __module__ = __name__
    neverDisable = 1
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSillyMeterMgr')

    def __init__(self, cr):
        DistributedPhaseEventMgr.DistributedPhaseEventMgr.__init__(self, cr)
        cr.SillyMeterMgr = self

    def announceGenerate(self):
        DistributedPhaseEventMgr.DistributedPhaseEventMgr.announceGenerate(self)
        messenger.send('SillyMeterIsRunning', [self.isRunning])

    def delete(self):
        self.notify.debug('deleting SillyMetermgr')
        messenger.send('SillyMeterIsRunning', [False])
        DistributedPhaseEventMgr.DistributedPhaseEventMgr.delete(self)
        if hasattr(self.cr, 'SillyMeterMgr'):
            del self.cr.SillyMeterMgr

    def setCurPhase(self, newPhase):
        DistributedPhaseEventMgr.DistributedPhaseEventMgr.setCurPhase(self, newPhase)
        messenger.send('SillyMeterPhase', [newPhase])

    def setIsRunning(self, isRunning):
        DistributedPhaseEventMgr.DistributedPhaseEventMgr.setIsRunning(self, isRunning)
        messenger.send('SillyMeterIsRunning', [isRunning])

    def getCurPhaseDuration(self):
        if len(self.holidayDates) > 0:
            startHolidayDate = self.holidayDates[self.curPhase]
            if self.curPhase + 1 >= len(self.holidayDates):
                self.notify.error('No end date for phase %' % self.curPhase)
                return -1
            else:
                endHolidayDate = self.holidayDates[(self.curPhase + 1)]
            startHolidayTime = time.mktime(startHolidayDate.timetuple())
            endHolidayTime = time.mktime(endHolidayDate.timetuple())
            holidayDuration = endHolidayTime - startHolidayTime
            if holidayDuration < 0:
                self.notify.error('Duration not set for phase %' % self.curPhase)
                return -1
            else:
                return holidayDuration
        else:
            self.notify.warning('Phase dates not yet known')
            return -1

    def getCurPhaseStartDate(self):
        if len(self.holidayDates) > 0:
            return self.holidayDates[self.curPhase]