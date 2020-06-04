# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\DistributedBoatAI.py
from otp.ai.AIBase import *
from toontown.toonbase.ToontownGlobals import *
from direct.distributed.ClockDelta import *
from direct.distributed import DistributedObjectAI
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task import Task

class DistributedBoatAI(DistributedObjectAI.DistributedObjectAI):
    __module__ = __name__

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.fsm = ClassicFSM.ClassicFSM('DistributedBoatAI', [
         State.State('off', self.enterOff, self.exitOff, [
          'DockedEast']),
         State.State('DockedEast', self.enterDockedEast, self.exitDockedEast, [
          'SailingWest']),
         State.State('SailingWest', self.enterSailingWest, self.exitSailingWest, [
          'DockedWest']),
         State.State('DockedWest', self.enterDockedWest, self.exitDockedWest, [
          'SailingEast']),
         State.State('SailingEast', self.enterSailingEast, self.exitSailingEast, [
          'DockedEast'])], 'off', 'off')
        self.fsm.enterInitialState()
        return

    def delete(self):
        self.fsm.request('off')
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def b_setState(self, state):
        self.sendUpdate('setState', [state, globalClockDelta.getRealNetworkTime()])
        self.fsm.request(state)

    def getState(self):
        return [
         self.fsm.getCurrentState().getName(), globalClockDelta.getRealNetworkTime()]

    def start(self):
        self.b_setState('DockedEast')
        return

    def enterOff(self):
        return

    def exitOff(self):
        return

    def enterDockedEast(self):
        taskMgr.doMethodLater(10.0, self.__departEast, 'depart-east')
        return

    def exitDockedEast(self):
        taskMgr.remove('depart-east')
        return

    def __departEast(self, task):
        self.b_setState('SailingWest')
        return Task.done

    def enterSailingWest(self):
        taskMgr.doMethodLater(20.0, self.__dockWest, 'dock-west')
        return

    def exitSailingWest(self):
        taskMgr.remove('dock-west')
        return

    def __dockWest(self, task):
        self.b_setState('DockedWest')
        return Task.done

    def enterDockedWest(self):
        taskMgr.doMethodLater(10.0, self.__departWest, 'depart-west')
        return

    def exitDockedWest(self):
        taskMgr.remove('depart-west')
        return

    def __departWest(self, task):
        self.b_setState('SailingEast')
        return Task.done

    def enterSailingEast(self):
        taskMgr.doMethodLater(20.0, self.__dockEast, 'dock-east')
        return

    def exitSailingEast(self):
        taskMgr.remove('dock-east')
        return

    def __dockEast(self, task):
        self.b_setState('DockedEast')
        return Task.done