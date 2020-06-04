# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\EntrancePoint.py
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal
import BasicEntities

class EntrancePoint(BasicEntities.NodePathEntity):
    __module__ = __name__

    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.rotator = self.attachNewNode('rotator')
        self.placer = self.rotator.attachNewNode('placer')
        self.initEntrancePoint()

    def destroy(self):
        self.destroyEntrancePoint()
        self.placer.removeNode()
        self.rotator.removeNode()
        del self.placer
        del self.rotator
        BasicEntities.NodePathEntity.destroy(self)

    def placeToon(self, toon, toonIndex, numToons):
        self.placer.setY(-self.radius)
        self.rotator.setH(-self.theta * (numToons - 1) * 0.5 + toonIndex * self.theta)
        toon.setPosHpr(self.placer, 0, 0, 0, 0, 0, 0)

    def initEntrancePoint(self):
        if self.entranceId >= 0:
            self.level.entranceId2entity[self.entranceId] = self

    def destroyEntrancePoint(self):
        if self.entranceId >= 0:
            if self.level.entranceId2entity.has_key(self.entranceId):
                del self.level.entranceId2entity[self.entranceId]

    if __dev__:

        def attribChanged(self, *args):
            BasicEntities.NodePathEntity.attribChanged(self, *args)
            self.destroyEntrancePoint()
            self.initEntrancePoint()