# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedAnimBuildingAI.py
from direct.directnotify import DirectNotifyGlobal
from toontown.building import DistributedBuildingAI
from toontown.building import DistributedAnimDoorAI
from toontown.building import DoorTypes

class DistributedAnimBuildingAI(DistributedBuildingAI.DistributedBuildingAI):
    __module__ = __name__

    def __init__(self, air, blockNumber, zoneId, trophyMgr):
        DistributedBuildingAI.DistributedBuildingAI.__init__(self, air, blockNumber, zoneId, trophyMgr)

    def createExteriorDoor(self):
        result = DistributedAnimDoorAI.DistributedAnimDoorAI(self.air, self.block, DoorTypes.EXT_ANIM_STANDARD)
        return result