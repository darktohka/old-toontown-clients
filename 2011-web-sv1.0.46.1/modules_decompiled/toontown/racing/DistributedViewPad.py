# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\racing\DistributedViewPad.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from direct.task import Task
from pandac.PandaModules import *
from toontown.racing.DistributedKartPad import DistributedKartPad
from toontown.racing.KartShopGlobals import KartGlobals
if __debug__:
    import pdb

class DistributedViewPad(DistributedKartPad):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedViewPad')
    id = 0

    def __init__(self, cr):
        DistributedKartPad.__init__(self, cr)
        self.id = DistributedViewPad.id
        DistributedViewPad.id += 1

    def setLastEntered(self, timeStamp):
        self.timeStamp = timeStamp

    def getTimestamp(self, avId):
        return self.timeStamp

    def addStartingBlock(self, block):
        block.cameraPos = Point3(0, 23, 7)
        block.cameraHpr = Point3(180, -10, 0)
        DistributedKartPad.addStartingBlock(self, block)