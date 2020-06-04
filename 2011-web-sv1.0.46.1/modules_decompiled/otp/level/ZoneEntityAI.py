# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\ZoneEntityAI.py
import ZoneEntityBase

class ZoneEntityAI(ZoneEntityBase.ZoneEntityBase):
    __module__ = __name__

    def __init__(self, level, entId):
        ZoneEntityBase.ZoneEntityBase.__init__(self, level, entId)
        self.setZoneId(self.level.air.allocateZone())

    def destroy(self):
        if not self.isUberZone():
            self.level.air.deallocateZone(self.getZoneId())
        ZoneEntityBase.ZoneEntityBase.destroy(self)