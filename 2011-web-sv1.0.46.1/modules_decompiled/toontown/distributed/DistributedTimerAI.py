# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\distributed\DistributedTimerAI.py
from direct.distributed import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
import time

class DistributedTimerAI(DistributedObjectAI.DistributedObjectAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTimerAI')

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.setStartTime(globalClockDelta.getRealNetworkTime(bits=32))

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)

    def setStartTime(self, time):
        self.startTime = time

    def getStartTime(self):
        return self.startTime