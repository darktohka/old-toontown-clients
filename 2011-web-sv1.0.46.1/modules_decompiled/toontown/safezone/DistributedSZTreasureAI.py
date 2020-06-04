# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\DistributedSZTreasureAI.py
import DistributedTreasureAI
from toontown.toonbase import ToontownGlobals

class DistributedSZTreasureAI(DistributedTreasureAI.DistributedTreasureAI):
    __module__ = __name__

    def __init__(self, air, treasurePlanner, x, y, z):
        DistributedTreasureAI.DistributedTreasureAI.__init__(self, air, treasurePlanner, x, y, z)
        self.healAmount = treasurePlanner.healAmount

    def validAvatar(self, av):
        return av.hp >= -1 and av.hp < av.maxHp

    def d_setGrab(self, avId):
        DistributedTreasureAI.DistributedTreasureAI.d_setGrab(self, avId)
        if self.air.doId2do.has_key(avId):
            av = self.air.doId2do[avId]
            if self.validAvatar(av):
                if av.hp == -1:
                    av.hp = 0
                if simbase.air.holidayManager.currentHolidays.has_key(ToontownGlobals.VALENTINES_DAY):
                    av.toonUp(self.healAmount * 2)
                else:
                    av.toonUp(self.healAmount)