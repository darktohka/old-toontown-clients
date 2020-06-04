# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\MMTreasurePlannerAI.py
from toontown.toonbase.ToontownGlobals import *
import RegenTreasurePlannerAI, DistributedMMTreasureAI

class MMTreasurePlannerAI(RegenTreasurePlannerAI.RegenTreasurePlannerAI):
    __module__ = __name__

    def __init__(self, zoneId):
        self.healAmount = 10
        RegenTreasurePlannerAI.RegenTreasurePlannerAI.__init__(self, zoneId, DistributedMMTreasureAI.DistributedMMTreasureAI, 'MMTreasurePlanner', 20, 2)
        return

    def initSpawnPoints(self):
        self.spawnPoints = [
         (118, -39, 3.3), (118, 1, 3.3), (112, -22, 0.8), (108, -74, -4.5), (110, -65, -4.5), (102, 23.5, -4.5), (60, -115, 6.5), (-5, -115, 6.5), (-64, -77, 6.5), (-77, -44, 6.5), (-76, 3, 6.5), (44, 76, 6.5), (136, -96, -13.5), (85, -6.7, -13.5), (60, -95, -14.5), (72, 60, -13.5), (-55, -23, -14.5), (-21, 47, -14.5), (-24, -75, -14.5)]
        return self.spawnPoints