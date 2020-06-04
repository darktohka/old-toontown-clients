# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedBarrelBaseAI.py
from direct.directnotify import DirectNotifyGlobal
from otp.level import DistributedEntityAI
from direct.task import Task
from toontown.coghq import BarrelBase

class DistributedBarrelBaseAI(DistributedEntityAI.DistributedEntityAI, BarrelBase.BarrelBase):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBarrelBaseAI')

    def __init__(self, level, entId):
        self.rewardPerGrabMax = 0
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)
        self.usedAvIds = []

    def delete(self):
        taskMgr.remove(self.taskName('resetGags'))
        del self.usedAvIds
        del self.pos
        DistributedEntityAI.DistributedEntityAI.delete(self)

    def requestGrab(self):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('requestGrab %s' % avId)
        if avId not in self.usedAvIds:
            self.usedAvIds.append(avId)
            self.d_setGrab(avId)
        else:
            self.sendUpdate('setReject')

    def d_setGrab(self, avId):
        self.sendUpdate('setGrab', [avId])