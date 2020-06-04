# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\distributed\DistributedTimer.py
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
import time

class DistributedTimer(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTimer')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        base.cr.DTimer = self

    def delete(self):
        DistributedObject.DistributedObject.delete(self)
        base.cr.DTimer = None
        return

    def setStartTime(self, time):
        self.startTime = time
        print 'TIMER startTime %s' % time

    def getStartTime(self):
        return self.startTime

    def getTime(self):
        elapsedTime = globalClockDelta.localElapsedTime(self.startTime, bits=32)
        return elapsedTime