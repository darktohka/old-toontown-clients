# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\fsm\FourState.py
__all__ = [
 'FourState']
from direct.directnotify import DirectNotifyGlobal
import ClassicFSM, State
from direct.task import Task

class FourState:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FourState')

    def __init__(self, names, durations=[
 0, 1, None, 1, 1]):
        self.track = None
        self.stateTime = 0.0
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
        self.stateIndex = 0
        self.fsm = ClassicFSM.ClassicFSM('FourState', self.states.values(), names[0], names[0])
        self.fsm.enterInitialState()
        return

    def setTrack(self, track):
        if self.track is not None:
            self.track.pause()
            self.track = None
        if track is not None:
            track.start(self.stateTime)
            self.track = track
        return

    def enterStateN(self, stateIndex):
        self.stateIndex = stateIndex
        self.duration = self.durations[stateIndex] or 0.0

    def isOn(self):
        return self.stateIndex == 4

    def changedOnState(self, isOn):
        pass

    def enterState0(self):
        self.enterStateN(0)

    def exitState0(self):
        self.changedOnState(0)

    def enterState1(self):
        self.enterStateN(1)

    def exitState1(self):
        pass

    def enterState2(self):
        self.enterStateN(2)

    def exitState2(self):
        pass

    def enterState3(self):
        self.enterStateN(3)

    def exitState3(self):
        pass

    def enterState4(self):
        self.enterStateN(4)
        self.changedOnState(1)

    def exitState4(self):
        self.changedOnState(0)