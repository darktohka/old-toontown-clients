# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\ZoneEntityBase.py
import Entity, LevelConstants

class ZoneEntityBase(Entity.Entity):
    __module__ = __name__

    def __init__(self, level, entId):
        Entity.Entity.__init__(self, level, entId)
        self.zoneId = None
        return

    def destroy(self):
        del self.zoneId
        Entity.Entity.destroy(self)

    def isUberZone(self):
        return self.entId == LevelConstants.UberZoneEntId

    def setZoneId(self, zoneId):
        self.zoneId = zoneId

    def getZoneId(self):
        return self.zoneId

    def getZoneNum(self):
        return self.entId