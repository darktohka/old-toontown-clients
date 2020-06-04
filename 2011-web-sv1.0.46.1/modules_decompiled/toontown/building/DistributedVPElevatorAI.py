# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedVPElevatorAI.py
from ElevatorConstants import *
import DistributedBossElevatorAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals

class DistributedVPElevatorAI(DistributedBossElevatorAI.DistributedBossElevatorAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedVPElevatorAI')

    def __init__(self, air, bldg, zone, antiShuffle=0, minLaff=0):
        DistributedBossElevatorAI.DistributedBossElevatorAI.__init__(self, air, bldg, zone, antiShuffle=antiShuffle, minLaff=minLaff)
        self.type = ELEVATOR_VP
        self.countdownTime = ElevatorData[self.type]['countdown']

    def checkBoard(self, av):
        dept = ToontownGlobals.cogHQZoneId2deptIndex(self.zone)
        boardingResult = 0
        if av.hp < self.minLaff:
            boardingResult = REJECT_MINLAFF
        if not av.readyForPromotion(dept):
            boardingResult = REJECT_PROMOTION
        if ToontownGlobals.SELLBOT_NERF_HOLIDAY in self.air.holidayManager.currentHolidays:
            boardingResult = 0
        return boardingResult