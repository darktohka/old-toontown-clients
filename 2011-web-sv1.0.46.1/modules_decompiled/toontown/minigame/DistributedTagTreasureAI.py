# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\DistributedTagTreasureAI.py
from toontown.safezone import DistributedTreasureAI
from direct.distributed.ClockDelta import *

class DistributedTagTreasureAI(DistributedTreasureAI.DistributedTreasureAI):
    __module__ = __name__

    def __init__(self, air, treasurePlanner, x, y, z):
        DistributedTreasureAI.DistributedTreasureAI.__init__(self, air, treasurePlanner, x, y, z)