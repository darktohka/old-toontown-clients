# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\distributed\DistributedSmoothNodeBase.py
from ClockDelta import *
from direct.task import Task
from direct.showbase.PythonUtil import randFloat, Enum

class DummyTaskClass:
    __module__ = __name__

    def setDelay(self, blah):
        pass


DummyTask = DummyTaskClass()

class DistributedSmoothNodeBase:
    __module__ = __name__
    BroadcastTypes = Enum('FULL, XYH, XY')

    def __init__(self):
        self.__broadcastPeriod = None
        return

    def generate(self):
        self.cnode = CDistributedSmoothNodeBase()
        self.cnode.setClockDelta(globalClockDelta)
        self.d_broadcastPosHpr = None
        return

    def disable(self):
        del self.cnode
        self.stopPosHprBroadcast()

    def delete(self):
        pass

    def b_clearSmoothing(self):
        self.d_clearSmoothing()
        self.clearSmoothing()

    def d_clearSmoothing(self):
        self.sendUpdate('clearSmoothing', [0])

    def getPosHprBroadcastTaskName(self):
        return 'sendPosHpr-%s' % self.doId

    def setPosHprBroadcastPeriod(self, period):
        self.__broadcastPeriod = period

    def getPosHprBroadcastPeriod(self):
        return self.__broadcastPeriod

    def stopPosHprBroadcast(self):
        taskMgr.remove(self.getPosHprBroadcastTaskName())
        self.d_broadcastPosHpr = None
        return

    def posHprBroadcastStarted(self):
        return self.d_broadcastPosHpr != None

    def wantSmoothPosBroadcastTask(self):
        return True

    def startPosHprBroadcast(self, period=0.2, stagger=0, type=None):
        if self.cnode == None:
            self.initializeCnode()
        BT = DistributedSmoothNodeBase.BroadcastTypes
        if type is None:
            type = BT.FULL
        self.broadcastType = type
        broadcastFuncs = {BT.FULL: self.cnode.broadcastPosHprFull, BT.XYH: self.cnode.broadcastPosHprXyh, BT.XY: self.cnode.broadcastPosHprXy}
        self.d_broadcastPosHpr = broadcastFuncs[self.broadcastType]
        taskName = self.getPosHprBroadcastTaskName()
        self.cnode.initialize(self, self.dclass, self.doId)
        self.setPosHprBroadcastPeriod(period)
        self.b_clearSmoothing()
        self.cnode.sendEverything()
        taskMgr.remove(taskName)
        delay = 0.0
        if stagger:
            delay = randFloat(period)
        if self.wantSmoothPosBroadcastTask():
            taskMgr.doMethodLater(self.__broadcastPeriod + delay, self._posHprBroadcast, taskName)
        return

    def _posHprBroadcast(self, task=DummyTask):
        self.d_broadcastPosHpr()
        task.setDelay(self.__broadcastPeriod)
        return Task.again

    def sendCurrentPosition(self):
        if self.d_broadcastPosHpr is None:
            self.cnode.initialize(self, self.dclass, self.doId)
        self.cnode.sendEverything()
        return