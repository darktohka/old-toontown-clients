# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedStomperPair.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
import math, StomperGlobals
from direct.directnotify import DirectNotifyGlobal
from otp.level import BasicEntities

class DistributedStomperPair(BasicEntities.DistributedNodePathEntity):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStomperPair')

    def __init__(self, cr):
        BasicEntities.DistributedNodePathEntity.__init__(self, cr)
        self.children = None
        return

    def delete(self):
        BasicEntities.DistributedNodePathEntity.delete(self)
        self.ignoreAll()

    def generateInit(self):
        self.notify.debug('generateInit')
        BasicEntities.DistributedNodePathEntity.generateInit(self)

    def generate(self):
        self.notify.debug('generate')
        BasicEntities.DistributedNodePathEntity.generate(self)

    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        BasicEntities.DistributedNodePathEntity.announceGenerate(self)
        self.listenForChildren()

    def listenForChildren(self):
        if self.stomperIds:
            for entId in self.stomperIds:
                self.accept(self.getUniqueName('crushMsg', entId), self.checkSquashedToon)

    def checkSquashedToon(self):
        tPos = base.localAvatar.getPos(self)
        print 'tpos = %s' % tPos
        yRange = 3.0
        xRange = 3.0
        if tPos[1] < yRange and tPos[1] > -yRange and tPos[0] < xRange and tPos[0] > -xRange:
            self.level.b_setOuch(3)