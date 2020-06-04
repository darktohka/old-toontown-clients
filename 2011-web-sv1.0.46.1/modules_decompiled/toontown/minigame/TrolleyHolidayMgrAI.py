# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\TrolleyHolidayMgrAI.py
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.ai import HolidayBaseAI

class TrolleyHolidayMgrAI(HolidayBaseAI.HolidayBaseAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TrolleyHolidayMgrAI')
    PostName = 'TrolleyHoliday'
    StartStopMsg = 'TrolleyHolidayStartStop'

    def __init__(self, air, holidayId):
        HolidayBaseAI.HolidayBaseAI.__init__(self, air, holidayId)

    def start(self):
        bboard.post(TrolleyHolidayMgrAI.PostName, True)
        simbase.air.newsManager.trolleyHolidayStart()
        messenger.send(TrolleyHolidayMgrAI.StartStopMsg)

    def stop(self):
        bboard.remove(TrolleyHolidayMgrAI.PostName)
        simbase.air.newsManager.trolleyHolidayEnd()
        messenger.send(TrolleyHolidayMgrAI.StartStopMsg)