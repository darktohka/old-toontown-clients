# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\OZTreasurePlannerAI.py
from toontown.toonbase.ToontownGlobals import *
import RegenTreasurePlannerAI, DistributedOZTreasureAI

class OZTreasurePlannerAI(RegenTreasurePlannerAI.RegenTreasurePlannerAI):
    __module__ = __name__

    def __init__(self, zoneId):
        self.healAmount = 3
        RegenTreasurePlannerAI.RegenTreasurePlannerAI.__init__(self, zoneId, DistributedOZTreasureAI.DistributedOZTreasureAI, 'OZTreasurePlanner', 20, 5)

    def initSpawnPoints(self):
        self.spawnPoints = [
         (-156.9, -118.9, 0.025), (-35.6, 86.0, 1.25), (116.8, 10.8, 0.104), (-35, 145.7, 0.025), (-198.8, -45.1, 0.025), (-47.1, -25.5, 0.809), (59.15, 34.8, 1.767), (-81.02, -72.2, 0.026), (-167.9, 124.5, 0.025), (-226.7, -27.6, 0.025), (-16.0, -108.9, 0.025), (18.0, 58.5, 5.919), (91.4, 127.8, 0.025), (-86.5, -75.9, 0.025), (-48.751, -32.3, 1.143)]
        return self.spawnPoints