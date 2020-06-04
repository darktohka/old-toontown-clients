# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\DistCogdoCraneCogAI.py
from direct.distributed.ClockDelta import globalClockDelta
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistCogdoCraneCogAI(DistributedObjectAI):
    __module__ = __name__

    def __init__(self, air, game, dna, entranceId, spawnTime):
        DistributedObjectAI.__init__(self, air)
        self._gameId = game.doId
        self._dna = dna
        self._entranceId = entranceId
        self._spawnTime = spawnTime

    def getGameId(self):
        return self._gameId

    def getDNAString(self):
        return self._dna.makeNetString()

    def getSpawnInfo(self):
        return (
         self._entranceId, globalClockDelta.localToNetworkTime(self._spawnTime))