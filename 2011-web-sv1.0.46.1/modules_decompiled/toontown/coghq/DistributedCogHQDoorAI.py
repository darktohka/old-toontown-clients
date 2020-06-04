# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedCogHQDoorAI.py
from otp.ai.AIBaseGlobal import *
from direct.distributed.ClockDelta import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from toontown.building import DistributedDoorAI
from direct.fsm import State
from toontown.toonbase import ToontownGlobals
import CogDisguiseGlobals
from toontown.building import FADoorCodes
from toontown.building import DoorTypes
from toontown.toonbase import ToontownAccessAI

class DistributedCogHQDoorAI(DistributedDoorAI.DistributedDoorAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCogHQDoorAI')

    def __init__(self, air, blockNumber, doorType, destinationZone, doorIndex=0, lockValue=FADoorCodes.SB_DISGUISE_INCOMPLETE, swing=3):
        DistributedDoorAI.DistributedDoorAI.__init__(self, air, blockNumber, doorType, doorIndex, lockValue, swing)
        self.destinationZone = destinationZone

    def requestEnter(self):
        avatarID = self.air.getAvatarIdFromSender()
        allowed = 0
        dept = ToontownGlobals.cogHQZoneId2deptIndex(self.destinationZone)
        av = self.air.doId2do.get(avatarID)
        if av:
            if self.doorType == DoorTypes.EXT_COGHQ:
                if self.isLockedDoor():
                    parts = av.getCogParts()
                    if CogDisguiseGlobals.isSuitComplete(parts, dept):
                        allowed = 1
                    else:
                        allowed = 0
                else:
                    allowed = 1
            if not ToontownAccessAI.canAccess(avatarID, self.zoneId, 'DistributedCogHQDoorAI.requestEnter'):
                allowed = 0
            allowed or self.sendReject(avatarID, self.isLockedDoor())
        else:
            self.enqueueAvatarIdEnter(avatarID)
            self.sendUpdateToAvatarId(avatarID, 'setOtherZoneIdAndDoId', [
             self.destinationZone, self.otherDoor.getDoId()])

    def requestExit(self):
        avatarID = self.air.getAvatarIdFromSender()
        if self.avatarsWhoAreEntering.has_key(avatarID):
            del self.avatarsWhoAreEntering[avatarID]
        if not self.avatarsWhoAreExiting.has_key(avatarID):
            dept = ToontownGlobals.cogHQZoneId2deptIndex(self.destinationZone)
            self.avatarsWhoAreExiting[avatarID] = 1
            self.sendUpdate('avatarExit', [avatarID])
            self.openDoor(self.exitDoorFSM)
            if self.lockedDoor:
                av = self.air.doId2do[avatarID]
                if self.doorType == DoorTypes.EXT_COGHQ:
                    av.b_setCogIndex(-1)
                else:
                    av.b_setCogIndex(dept)