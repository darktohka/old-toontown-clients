# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\LevelMgr.py
from direct.showbase.PythonUtil import Functor
import LevelMgrBase

class LevelMgr(LevelMgrBase.LevelMgrBase):
    __module__ = __name__

    def __init__(self, level, entId):
        LevelMgrBase.LevelMgrBase.__init__(self, level, entId)
        self.geom = loader.loadModel(self.modelFilename)
        if not self.geom:
            import pdb
            pdb.set_trace()
        self.zoneNums = []
        self.level.zoneNum2zoneId = {}
        self.level.zoneId2zoneNum = {}
        self.accept(self.level.getEntityOfTypeCreateEvent('zone'), self.handleZoneCreated)

    def destroy(self):
        del self.level.zoneIds
        del self.level.zoneId2zoneNum
        del self.level.zoneNum2zoneId
        self.geom.removeNode()
        del self.geom
        LevelMgrBase.LevelMgrBase.destroy(self)

    def handleZoneCreated(self, entId):
        zoneEnt = self.level.getEntity(entId)
        self.zoneNums.append(zoneEnt.entId)
        self.privAssignZoneIds()
        self.accept(self.level.getEntityDestroyEvent(entId), Functor(self.handleZoneDestroy, entId))

    def handleZoneDestroy(self, entId):
        zoneEnt = self.level.getEntity(entId)
        del self.level.zoneId2zoneNum[self.level.zoneNum2zoneId[zoneEnt.entId]]
        del self.level.zoneNum2zoneId[zoneEnt.entId]
        self.zoneNums.remove(zoneEnt.entId)
        self.privAssignZoneIds()

    def privAssignZoneIds(self):
        self.zoneNums.sort()
        for i in range(len(self.zoneNums)):
            zoneNum = self.zoneNums[i]
            zoneEnt = self.level.getEntity(zoneNum)
            zoneId = self.level.zoneIds[i]
            zoneEnt.setZoneId(zoneId)
            self.level.zoneNum2zoneId[zoneNum] = zoneId
            self.level.zoneId2zoneNum[zoneId] = zoneNum