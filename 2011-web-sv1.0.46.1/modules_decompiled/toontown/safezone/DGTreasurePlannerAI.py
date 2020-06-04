# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\DGTreasurePlannerAI.py
from toontown.toonbase.ToontownGlobals import *
import RegenTreasurePlannerAI, DistributedDGTreasureAI

class DGTreasurePlannerAI(RegenTreasurePlannerAI.RegenTreasurePlannerAI):
    __module__ = __name__

    def __init__(self, zoneId):
        self.healAmount = 10
        RegenTreasurePlannerAI.RegenTreasurePlannerAI.__init__(self, zoneId, DistributedDGTreasureAI.DistributedDGTreasureAI, 'DGTreasurePlanner', 15, 2)
        return

    def initSpawnPoints(self):
        self.spawnPoints = [
         (-49, 156, 0.0), (-59, 50, 0.0), (19, 16, 0.0), (76, 38, 1.1), (102, 121, 0.0), (69, 123, 0.0), (49, 105, 0.0), (24, 156, 0.0), (-27, 127, 0.0), (-56, 105, 0.0), (-40, 113, 0.0), (25, 114, 0.0), (-6, 84, 0.0), (19, 96, 0.0), (0, 114, 0.0), (-78, 157, 10.0), (-33.4, 218.2, 10.0), (57, 205, 10.0), (32, 77, 0.0), (-102, 101, 0.0)]
        return self.spawnPoints