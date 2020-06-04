# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedMintElevatorExtAI.py
from otp.ai.AIBase import *
from toontown.toonbase import ToontownGlobals
from direct.distributed.ClockDelta import *
from toontown.building.ElevatorConstants import *
from toontown.building import DistributedElevatorExtAI
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task import Task
import CogDisguiseGlobals

class DistributedMintElevatorExtAI(DistributedElevatorExtAI.DistributedElevatorExtAI):
    __module__ = __name__

    def __init__(self, air, bldg, mintId, antiShuffle=0, minLaff=0):
        DistributedElevatorExtAI.DistributedElevatorExtAI.__init__(self, air, bldg, antiShuffle=antiShuffle, minLaff=minLaff)
        self.mintId = mintId
        self.cogDept = ToontownGlobals.cogHQZoneId2deptIndex(self.mintId)
        self.type = ELEVATOR_MINT
        self.countdownTime = ElevatorData[self.type]['countdown']

    def getMintId(self):
        return self.mintId

    def avIsOKToBoard(self, av):
        if not DistributedElevatorExtAI.DistributedElevatorExtAI.avIsOKToBoard(self, av):
            return False
        return True

    def elevatorClosed(self):
        numPlayers = self.countFullSeats()
        if numPlayers > 0:
            players = []
            for i in self.seats:
                if i not in [None, 0]:
                    players.append(i)

            mintZone = self.bldg.createMint(self.mintId, players)
            for seatIndex in range(len(self.seats)):
                avId = self.seats[seatIndex]
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setMintInteriorZone', [
                     mintZone])
                    self.clearFullNow(seatIndex)

        else:
            self.notify.warning('The elevator left, but was empty.')
        self.fsm.request('closed')
        return

    def enterClosed(self):
        DistributedElevatorExtAI.DistributedElevatorExtAI.enterClosed(self)
        self.fsm.request('opening')

    def sendAvatarsToDestination(self, avIdList):
        if len(avIdList) > 0:
            mintZone = self.bldg.createMint(self.mintId, avIdList)
            for avId in avIdList:
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setMintInteriorZoneForce', [
                     mintZone])