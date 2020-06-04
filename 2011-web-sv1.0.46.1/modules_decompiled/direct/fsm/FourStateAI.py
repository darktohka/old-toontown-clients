# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\fsm\FourStateAI.py
__all__ = [
 'FourStateAI']
from direct.directnotify import DirectNotifyGlobal
import ClassicFSM, State
from direct.task import Task

class FourStateAI:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FourStateAI')

    def __init__(self, names, durations=[
 0, 1, None, 1, 1]):
        self.doLaterTask = None
        self.stateIndex = 0
        self.names = names
        self.durations = durations
        self.states = {0: State.State(names[0], self.enterState0, self.exitState0, [
             names[1], names[2], names[3], names[4]]), 
           1: State.State(names[1], self.enterState1, self.exitState1, [
             names[2], names[3]]), 
           2: State.State(names[2], self.enterState2, self.exitState2, [
             names[3]]), 
           3: State.State(names[3], self.enterState3, self.exitState3, [
             names[4], names[1]]), 
           4: State.State(names[4], self.enterState4, self.exitState4, [
             names[1]])}
        self.fsm = ClassicFSM.ClassicFSM('FourState', self.states.values(), names[0], names[0])
        self.fsm.enterInitialState()
        return

    def delete(self):
        if self.doLaterTask is not None:
            self.doLaterTask.remove()
            del self.doLaterTask
        del self.states
        del self.fsm
        return

    def getState(self):
        return [
         self.stateIndex]

    def sendState(self):
        self.sendUpdate('setState', self.getState())

    def setIsOn(self, isOn):
        if isOn:
            if self.stateIndex != 4:
                self.fsm.request(self.states[3])
        elif self.stateIndex != 2:
            self.fsm.request(self.states[1])

    def isOn(self):
        return self.stateIndex == 4

    def changedOnState(self, isOn):
        pass

    def switchToNextStateTask(self, task):
        self.fsm.request(self.states[self.nextStateIndex])
        return Task.done

    def distributeStateChange(self):
        self.sendState()

    def enterStateN(self, stateIndex, nextStateIndex):
        self.stateIndex = stateIndex
        self.nextStateIndex = nextStateIndex
        self.distributeStateChange()
        if self.durations[stateIndex] is not None:
            self.doLaterTask = taskMgr.doMethodLater(self.durations[stateIndex], self.switchToNextStateTask, 'enterStateN-timer-%s' % id(self))
        return

    def exitStateN(self):
        if self.doLaterTask:
            taskMgr.remove(self.doLaterTask)
            self.doLaterTask = None
        return

    def enterState0(self):
        self.enterStateN(0, 0)

    def exitState0(self):
        pass

    def enterState1(self):
        self.enterStateN(1, 2)

    def exitState1(self):
        self.exitStateN()

    def enterState2(self):
        self.enterStateN(2, 3)

    def exitState2(self):
        self.exitStateN()

    def enterState3(self):
        self.enterStateN(3, 4)

    def exitState3(self):
        self.exitStateN()

    def enterState4(self):
        self.enterStateN(4, 1)
        self.changedOnState(1)

    def exitState4(self):
        self.exitStateN()
        self.changedOnState(0)