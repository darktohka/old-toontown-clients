# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedElevatorMarkerAI.py
from otp.ai.AIBase import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import ClockDelta
from direct.task import Task
from otp.level import DistributedEntityAI
from otp.level import BasicEntities
from direct.directnotify import DirectNotifyGlobal

class DistributedElevatorMarkerAI(DistributedEntityAI.DistributedEntityAI, NodePath, BasicEntities.NodePathAttribs):
    __module__ = __name__

    def __init__(self, level, entId):
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)
        node = hidden.attachNewNode('DistributedElevatorMarkerAI')
        NodePath.__init__(self, node)

    def generate(self):
        DistributedEntityAI.DistributedEntityAI.generate(self)
        self.setPos(self.pos)
        self.setHpr(self.hpr)

    def delete(self):
        self.ignoreAll()
        DistributedEntityAI.DistributedEntityAI.delete(self)

    def destroy(self):
        self.notify.info('destroy entity(elevatorMaker) %s' % self.entId)
        DistributedEntityAI.DistributedEntityAI.destroy(self)