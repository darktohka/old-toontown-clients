# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\TTTreasurePlannerAI.py
from toontown.toonbase.ToontownGlobals import *
import RegenTreasurePlannerAI, DistributedTTTreasureAI

class TTTreasurePlannerAI(RegenTreasurePlannerAI.RegenTreasurePlannerAI):
    __module__ = __name__

    def __init__(self, zoneId):
        self.healAmount = 3
        RegenTreasurePlannerAI.RegenTreasurePlannerAI.__init__(self, zoneId, DistributedTTTreasureAI.DistributedTTTreasureAI, 'TTTreasurePlanner', 20, 5)

    def initSpawnPoints(self):
        self.spawnPoints = [
         (
          -59.9, -6.9, 0.84), (-90.6, -3.0, -0.75), (27.1, -93.5, 2.5), (94.2, 33.5, 4), (35.4, 43.1, 4), (67.1, 105.5, 2.5), (-99.15, -87.3407, 0.52499), (1.60586, -119.492, 3.025), (43.2026, -76.287, 3.025), (129.137, -61.9039, 2.525), (92.99, -158.399, 3.025), (111.749, -8.59927, 4.57466), (41.999, -30.2923, 4.025), (31.0649, -43.9149, 4.025), (10.0156, 105.218, 2.525), (46.9667, 169.143, 3.025), (100.68, 93.9896, 2.525), (129.285, 58.6107, 2.525), (-28.6272, 85.9833, 0.525), (-114.613, 86.1727, 0.525), (-132.528, 31.255, 0.025)]
        return self.spawnPoints