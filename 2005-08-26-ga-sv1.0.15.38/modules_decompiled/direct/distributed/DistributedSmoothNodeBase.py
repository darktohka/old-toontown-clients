# File: D (Python 2.2)

from ClockDelta import *
from direct.task import Task
from direct.showbase.PythonUtil import randFloat, Enum

class DistributedSmoothNodeBase:
    BroadcastTypes = Enum('FULL, XYH')
    
    def __init__(self):
        self.cnode = CDistributedSmoothNodeBase()
        self.cnode.setClockDelta(globalClockDelta)

    
    def delete(self):
        self.stopPosHprBroadcast()

    
    def b_clearSmoothing(self):
        self.d_clearSmoothing()
        self.clearSmoothing()

    
    def d_clearSmoothing(self):
        self.sendUpdate('clearSmoothing', [
            0])

    
    def getPosHprBroadcastTaskName(self):
        return 'sendPosHpr-%s' % self.doId

    
    def setPosHprBroadcastPeriod(self, period):
        self._DistributedSmoothNodeBase__broadcastPeriod = period

    
    def stopPosHprBroadcast(self):
        taskMgr.remove(self.getPosHprBroadcastTaskName())
        self.d_broadcastPosHpr = None

    
    def startPosHprBroadcast(self, period = 0.20000000000000001, stagger = 0, type = None):
        if self.cnode == None:
            self.initializeCnode()
        
        BT = DistributedSmoothNodeBase.BroadcastTypes
        if type is None:
            type = BT.FULL
        
        self.broadcastType = type
        broadcastFuncs = {
            BT.FULL: self.cnode.broadcastPosHprFull,
            BT.XYH: self.cnode.broadcastPosHprXyh }
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
        
        taskMgr.doMethodLater(self._DistributedSmoothNodeBase__broadcastPeriod + delay, self._DistributedSmoothNodeBase__posHprBroadcast, taskName)

    
    def _DistributedSmoothNodeBase__posHprBroadcast(self, task):
        self.d_broadcastPosHpr()
        taskName = self.taskName('sendPosHpr')
        taskMgr.doMethodLater(self._DistributedSmoothNodeBase__broadcastPeriod, self._DistributedSmoothNodeBase__posHprBroadcast, taskName)
        return Task.done


