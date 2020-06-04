# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\battle\DistributedBattleWaitersAI.py
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import DistributedBattleFinalAI

class DistributedBattleWaitersAI(DistributedBattleFinalAI.DistributedBattleFinalAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBattleWaitersAI')

    def __init__(self, air, bossCog, roundCallback, finishCallback, battleSide):
        DistributedBattleFinalAI.DistributedBattleFinalAI.__init__(self, air, bossCog, roundCallback, finishCallback, battleSide)

    def startBattle(self, toonIds, suits):
        self.joinableFsm.request('Joinable')
        for toonId in toonIds:
            if self.addToon(toonId):
                self.activeToons.append(toonId)

        self.d_setMembers()
        for suit in suits:
            self.pendingSuits.append(suit)

        self.d_setMembers()
        self.needAdjust = 1
        self.b_setState('ReservesJoining')