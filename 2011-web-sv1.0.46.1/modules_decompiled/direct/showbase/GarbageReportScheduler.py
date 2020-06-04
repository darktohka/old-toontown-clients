# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\GarbageReportScheduler.py
from direct.showbase.GarbageReport import GarbageReport

class GarbageReportScheduler:
    __module__ = __name__

    def __init__(self, waitBetween=None, waitScale=None):
        if waitBetween is None:
            waitBetween = 30 * 60
        if waitScale is None:
            waitScale = 1.5
        self._waitBetween = waitBetween
        self._waitScale = waitScale
        self._taskName = 'startScheduledGarbageReport-%s' % serialNum()
        self._garbageReport = None
        self._scheduleNextGarbageReport()
        return

    def getTaskName(self):
        return self._taskName

    def _scheduleNextGarbageReport(self, garbageReport=None):
        if garbageReport:
            self._garbageReport = None
        taskMgr.doMethodLater(self._waitBetween, self._runGarbageReport, self._taskName)
        self._waitBetween = self._waitBetween * self._waitScale
        return

    def _runGarbageReport(self, task):
        self._garbageReport = GarbageReport('ScheduledGarbageReport', threaded=True, doneCallback=self._scheduleNextGarbageReport, autoDestroy=True, priority=GarbageReport.Priorities.Normal * 3)
        return task.done