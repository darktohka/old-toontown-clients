# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedStomperPairAI.py
from otp.ai.AIBase import *
from direct.directnotify import DirectNotifyGlobal
from otp.level import DistributedEntityAI
import StomperGlobals
from direct.distributed import ClockDelta

class DistributedStomperPairAI(DistributedEntityAI.DistributedEntityAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStomperAI')

    def __init__(self, level, entId):
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)
        self.stompers = [None, None]
        self.hitPtsTaken = 3
        return

    def generate(self):
        DistributedEntityAI.DistributedEntityAI.generate(self)

    def delete(self):
        DistributedEntityAI.DistributedEntityAI.delete(self)

    def setChildren(self, doIds):
        for id in doIds:
            self.children = simbase.air.doId2do[id]

        self.sendUpdate('setChildren', [doIds])

    def setSquash(self):
        avId = self.air.getAvatarIdFromSender()
        av = simbase.air.doId2do.get(avId)
        if av:
            av.takeDamage(self.hitPtsTaken)