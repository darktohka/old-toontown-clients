# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedGagBarrelAI.py
from toontown.toonbase.ToontownBattleGlobals import *
import DistributedBarrelBaseAI
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task

class DistributedGagBarrelAI(DistributedBarrelBaseAI.DistributedBarrelBaseAI):
    __module__ = __name__

    def __init__(self, level, entId):
        x = y = z = h = 0
        self.gagLevelMax = 0
        DistributedBarrelBaseAI.DistributedBarrelBaseAI.__init__(self, level, entId)

    def d_setGrab(self, avId):
        self.notify.debug('d_setGrab %s' % avId)
        self.sendUpdate('setGrab', [avId])
        av = self.air.doId2do.get(avId)
        if av:
            if not av.hasTrackAccess(self.getGagTrack()):
                return
            track = self.getGagTrack()
            level = self.getGagLevel()
            maxGags = av.getMaxCarry()
            av.inventory.calcTotalProps()
            numGags = av.inventory.totalProps
            numReward = min(self.getRewardPerGrab(), maxGags - numGags)
            while numReward > 0 and level >= 0:
                result = av.inventory.addItem(track, level)
                if result <= 0:
                    level -= 1
                else:
                    numReward -= 1

            av.d_setInventory(av.inventory.makeNetString())