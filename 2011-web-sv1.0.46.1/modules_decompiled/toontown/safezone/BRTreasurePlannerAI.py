# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\BRTreasurePlannerAI.py
from toontown.toonbase.ToontownGlobals import *
import RegenTreasurePlannerAI, DistributedBRTreasureAI

class BRTreasurePlannerAI(RegenTreasurePlannerAI.RegenTreasurePlannerAI):
    __module__ = __name__

    def __init__(self, zoneId):
        self.healAmount = 12
        RegenTreasurePlannerAI.RegenTreasurePlannerAI.__init__(self, zoneId, DistributedBRTreasureAI.DistributedBRTreasureAI, 'BRTreasurePlanner', 20, 2)
        return

    def initSpawnPoints(self):
        self.spawnPoints = [
         (-108, 46, 6.2), (-111, 74, 6.2), (-126, 81, 6.2), (-74, -75, 3.0), (-136, -51, 3.0), (-20, 35, 6.2), (-55, 109, 6.2), (58, -57, 6.2), (-42, -134, 6.2), (-68, -148, 6.2), (-1, -62, 6.2), (25, 2, 6.2), (-133, 53, 6.2), (-99, 86, 6.2), (30, 63, 6.2), (-147, 3, 6.2), (-135, -102, 6.2), (35, -98, 6.2)]
        return self.spawnPoints