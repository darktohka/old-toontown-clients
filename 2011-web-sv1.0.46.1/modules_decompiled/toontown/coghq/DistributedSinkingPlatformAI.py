# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedSinkingPlatformAI.py
from otp.ai.AIBase import *
from direct.directnotify import DirectNotifyGlobal
from otp.level import DistributedEntityAI
import SinkingPlatformGlobals

class DistributedSinkingPlatformAI(DistributedEntityAI.DistributedEntityAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSinkingPlatformAI')

    def __init__(self, levelDoId, entId):
        DistributedEntityAI.DistributedEntityAI.__init__(self, levelDoId, entId)
        self.numStanding = 0

    def setOnOff(self, on, timestamp):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('setOnOff %s' % on)
        if on:
            self.numStanding += 1
        else:
            self.numStanding -= 1
        self.notify.debug('numStanding = %s' % self.numStanding)
        if self.numStanding > 0:
            self.sendUpdate('setSinkMode', [avId, SinkingPlatformGlobals.SINKING, timestamp])
        else:
            self.sendUpdate('setSinkMode', [avId, SinkingPlatformGlobals.RISING, timestamp])