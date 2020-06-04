# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\TagTreasurePlannerAI.py
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase.ToontownGlobals import *
from toontown.safezone import RegenTreasurePlannerAI
import DistributedTagTreasureAI

class TagTreasurePlannerAI(RegenTreasurePlannerAI.RegenTreasurePlannerAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TagTreasurePlannerAI')

    def __init__(self, zoneId, callback):
        self.numPlayers = 0
        RegenTreasurePlannerAI.RegenTreasurePlannerAI.__init__(self, zoneId, DistributedTagTreasureAI.DistributedTagTreasureAI, 'TagTreasurePlanner-' + str(zoneId), 3, 4, callback)
        return

    def initSpawnPoints(self):
        self.spawnPoints = [
         (0, 0, 0.1), (5, 20, 0.1), (0, 40, 0.1), (-5, -20, 0.1), (0, -40, 0.1), (20, 0, 0.1), (40, 5, 0.1), (-20, -5, 0.1), (-40, 0, 0.1), (22, 20, 0.1), (-20, 22, 0.1), (20, -20, 0.1), (-25, -20, 0.1), (20, 40, 0.1), (20, -44, 0.1), (-24, 40, 0.1), (-20, -40, 0.1)]
        return self.spawnPoints