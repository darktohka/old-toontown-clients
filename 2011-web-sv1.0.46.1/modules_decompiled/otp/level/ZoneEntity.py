# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\ZoneEntity.py
import ZoneEntityBase, BasicEntities

class ZoneEntity(ZoneEntityBase.ZoneEntityBase, BasicEntities.NodePathAttribs):
    __module__ = __name__

    def __init__(self, level, entId):
        ZoneEntityBase.ZoneEntityBase.__init__(self, level, entId)
        self.nodePath = self.level.getZoneNode(self.entId)
        if self.nodePath is None:
            if __dev__:
                self.level.reportModelSpecSyncError('unknown zoneNum %s; zone was removed from model?' % self.entId)
            else:
                self.notify.error('zone %s not found in level model' % self.entId)
        BasicEntities.NodePathAttribs.initNodePathAttribs(self, doReparent=0)
        self.visibleZoneNums = {}
        self.incrementRefCounts(self.visibility)
        return

    def destroy(self):
        BasicEntities.NodePathAttribs.destroy(self)
        ZoneEntityBase.ZoneEntityBase.destroy(self)

    def getNodePath(self):
        return self.nodePath

    def getVisibleZoneNums(self):
        return self.visibleZoneNums.keys()

    def incrementRefCounts(self, zoneNumList):
        for zoneNum in zoneNumList:
            self.visibleZoneNums.setdefault(zoneNum, 0)
            self.visibleZoneNums[zoneNum] += 1

    def decrementRefCounts(self, zoneNumList):
        for zoneNum in zoneNumList:
            self.visibleZoneNums[zoneNum] -= 1
            if self.visibleZoneNums[zoneNum] == 0:
                del self.visibleZoneNums[zoneNum]

    if __dev__:

        def setVisibility(self, visibility):
            self.decrementRefCounts(self.visibility)
            self.visibility = visibility
            self.incrementRefCounts(self.visibility)
            self.level.handleVisChange()