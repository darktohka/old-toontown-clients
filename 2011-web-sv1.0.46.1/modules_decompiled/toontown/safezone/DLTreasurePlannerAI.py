# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\DLTreasurePlannerAI.py
from toontown.toonbase.ToontownGlobals import *
import RegenTreasurePlannerAI, DistributedDLTreasureAI

class DLTreasurePlannerAI(RegenTreasurePlannerAI.RegenTreasurePlannerAI):
    __module__ = __name__

    def __init__(self, zoneId):
        self.healAmount = 12
        RegenTreasurePlannerAI.RegenTreasurePlannerAI.__init__(self, zoneId, DistributedDLTreasureAI.DistributedDLTreasureAI, 'DLTreasurePlanner', 20, 2)
        return

    def initSpawnPoints(self):
        self.spawnPoints = [
         (86, 69, -17.4), (34, -48, -16.4), (87, -70, -17.5), (-98, 99, 0.0), (51, 100, 0.0), (-45, -12, -15.0), (9, 8, -15.0), (-24, 64, -17.2), (-100, -99, 0.0), (21, -101, 0.0), (88, -17, -15.0), (32, 70, -17.4), (53, 35, -15.8), (2, -30, -15.5), (-40, -56, -16.8), (-28, 18, -15.0), (-34, -88, 0.0)]
        return self.spawnPoints