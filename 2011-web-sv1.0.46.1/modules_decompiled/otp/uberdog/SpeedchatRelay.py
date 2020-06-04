# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\uberdog\SpeedchatRelay.py
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.otpbase import OTPGlobals
from otp.uberdog import SpeedchatRelayGlobals

class SpeedchatRelay(DistributedObjectGlobal):
    __module__ = __name__

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)

    def sendSpeedchat(self, receiverId, messageIndex):
        self.sendSpeedchatToRelay(receiverId, SpeedchatRelayGlobals.NORMAL, [messageIndex])

    def sendSpeedchatCustom(self, receiverId, messageIndex):
        self.sendSpeedchatToRelay(receiverId, SpeedchatRelayGlobals.CUSTOM, [messageIndex])

    def sendSpeedchatEmote(self, receiverId, messageIndex):
        self.sendSpeedchatToRelay(receiverId, SpeedchatRelayGlobals.EMOTE, [messageIndex])

    def sendSpeedchatToRelay(self, receiverId, speedchatType, parameters):
        self.sendUpdate('forwardSpeedchat', [receiverId, speedchatType, parameters, base.cr.accountDetailRecord.playerAccountId, base.cr.accountDetailRecord.playerName + ' RHFM', 0])