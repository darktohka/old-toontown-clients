# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\DistributedButterflyAI.py
from otp.ai.AIBase import *
from toontown.toonbase.ToontownGlobals import *
from direct.distributed.ClockDelta import *
from direct.distributed import DistributedObjectAI
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task import Task
import ButterflyGlobals, random

class DistributedButterflyAI(DistributedObjectAI.DistributedObjectAI):
    __module__ = __name__

    def __init__(self, air, playground, area, ownerId):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.playground = playground
        self.area = area
        self.ownerId = ownerId
        self.fsm = ClassicFSM.ClassicFSM('DistributedButterfliesAI', [
         State.State('off', self.enterOff, self.exitOff, [
          'Flying', 'Landed']),
         State.State('Flying', self.enterFlying, self.exitFlying, [
          'Landed']),
         State.State('Landed', self.enterLanded, self.exitLanded, [
          'Flying'])], 'off', 'off')
        self.fsm.enterInitialState()
        (self.curPos, self.curIndex, self.destPos, self.destIndex, self.time) = ButterflyGlobals.getFirstRoute(self.playground, self.area, self.ownerId)
        return

    def delete(self):
        try:
            self.butterfly_deleted
        except:
            self.butterfly_deleted = 1
            ButterflyGlobals.recycleIndex(self.curIndex, self.playground, self.area, self.ownerId)
            ButterflyGlobals.recycleIndex(self.destIndex, self.playground, self.area, self.ownerId)
            self.fsm.request('off')
            del self.fsm
            DistributedObjectAI.DistributedObjectAI.delete(self)

    def d_setState(self, stateIndex, curIndex, destIndex, time):
        self.sendUpdate('setState', [stateIndex, curIndex, destIndex, time, globalClockDelta.getRealNetworkTime()])

    def getArea(self):
        return [
         self.playground, self.area]

    def getState(self):
        return [
         self.stateIndex, self.curIndex, self.destIndex, self.time, globalClockDelta.getRealNetworkTime()]

    def start(self):
        self.fsm.request('Flying')

    def avatarEnter(self):
        if self.fsm.getCurrentState().getName() == 'Landed':
            self.__ready()
        return

    def enterOff(self):
        self.stateIndex = ButterflyGlobals.OFF
        return

    def exitOff(self):
        return

    def enterFlying(self):
        self.stateIndex = ButterflyGlobals.FLYING
        ButterflyGlobals.recycleIndex(self.curIndex, self.playground, self.area, self.ownerId)
        self.d_setState(ButterflyGlobals.FLYING, self.curIndex, self.destIndex, self.time)
        taskMgr.doMethodLater(self.time, self.__handleArrival, self.uniqueName('butter-flying'))
        return

    def exitFlying(self):
        taskMgr.remove(self.uniqueName('butter-flying'))
        return

    def __handleArrival(self, task):
        self.curPos = self.destPos
        self.curIndex = self.destIndex
        self.fsm.request('Landed')
        return Task.done

    def enterLanded(self):
        self.stateIndex = ButterflyGlobals.LANDED
        self.time = random.random() * ButterflyGlobals.MAX_LANDED_TIME
        self.d_setState(ButterflyGlobals.LANDED, self.curIndex, self.destIndex, self.time)
        taskMgr.doMethodLater(self.time, self.__ready, self.uniqueName('butter-ready'))
        return

    def exitLanded(self):
        taskMgr.remove(self.uniqueName('butter-ready'))
        return

    def __ready(self, task=None):
        (self.destPos, self.destIndex, self.time) = ButterflyGlobals.getNextPos(self.curPos, self.playground, self.area, self.ownerId)
        self.fsm.request('Flying')
        return Task.done