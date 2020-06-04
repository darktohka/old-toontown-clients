# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\battle\BattleManagerAI.py
import DistributedBattleAI
from direct.directnotify import DirectNotifyGlobal

class BattleManagerAI:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('BattleManagerAI')

    def __init__(self, air):
        self.air = air
        self.cellId2battle = {}
        self.battleConstructor = DistributedBattleAI.DistributedBattleAI

    def cellHasBattle(self, cellId):
        return self.cellId2battle.has_key(cellId)

    def getBattle(self, cellId):
        if self.cellId2battle.has_key(cellId):
            return self.cellId2battle[cellId]
        return

    def newBattle(self, cellId, zoneId, pos, suit, toonId, finishCallback=None, maxSuits=4, interactivePropTrackBonus=-1):
        if self.cellId2battle.has_key(cellId):
            self.notify.info("A battle is already present in the suit's zone!")
            if not self.requestBattleAddSuit(cellId, suit):
                suit.flyAwayNow()
            battle = self.cellId2battle[cellId]
            battle.signupToon(toonId, pos[0], pos[1], pos[2])
        else:
            battle = self.battleConstructor(self.air, self, pos, suit, toonId, zoneId, finishCallback, maxSuits, interactivePropTrackBonus=interactivePropTrackBonus)
            battle.generateWithRequired(zoneId)
            battle.battleCellId = cellId
            self.cellId2battle[cellId] = battle
        return battle

    def requestBattleAddSuit(self, cellId, suit):
        return self.cellId2battle[cellId].suitRequestJoin(suit)

    def destroy(self, battle):
        cellId = battle.battleCellId
        self.notify.debug('BattleManager - destroying battle %d' % cellId)
        del self.cellId2battle[cellId]
        battle.requestDelete()