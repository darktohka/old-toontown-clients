# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\LevelMgrAI.py
from direct.showbase.PythonUtil import Functor
import LevelMgrBase

class LevelMgrAI(LevelMgrBase.LevelMgrBase):
    __module__ = __name__

    def __init__(self, level, entId):
        LevelMgrBase.LevelMgrBase.__init__(self, level, entId)
        self.level.zoneNum2zoneId = {}
        self.level.zoneIds = []
        self.accept(self.level.getEntityOfTypeCreateEvent('zone'), self.handleZoneCreated)

    def destroy(self):
        del self.level.zoneIds
        del self.level.zoneNum2zoneId
        LevelMgrBase.LevelMgrBase.destroy(self)

    def handleZoneCreated(self, entId):
        zoneEnt = self.level.getEntity(entId)
        self.level.zoneNum2zoneId[zoneEnt.entId] = zoneEnt.getZoneId()
        self.privCreateSortedZoneIdList()
        self.accept(self.level.getEntityDestroyEvent(entId), Functor(self.handleZoneDestroy, entId))

    def handleZoneDestroy(self, entId):
        zoneEnt = self.level.getEntity(entId)
        del self.level.zoneNum2zoneId[zoneEnt.entId]
        self.privCreateSortedZoneIdList()

    def privCreateSortedZoneIdList(self):
        zoneNums = self.level.zoneNum2zoneId.keys()
        zoneNums.sort()
        self.level.zoneIds = []
        for zoneNum in zoneNums:
            self.level.zoneIds.append(self.level.zoneNum2zoneId[zoneNum])