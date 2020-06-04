# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedGagshopInteriorAI.py
from direct.distributed import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedGagshopInteriorAI(DistributedObjectAI.DistributedObjectAI):
    __module__ = __name__

    def __init__(self, block, air, zoneId):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.block = block
        self.zoneId = zoneId

    def getZoneIdAndBlock(self):
        r = [
         self.zoneId, self.block]
        return r