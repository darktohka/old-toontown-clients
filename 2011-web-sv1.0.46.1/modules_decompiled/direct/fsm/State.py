# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\fsm\State.py
__all__ = [
 'State']
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject
import types

class State(DirectObject):
    __module__ = __name__
    notify = directNotify.newCategory('State')
    Any = 'ANY'

    def __init__(self, name, enterFunc=None, exitFunc=None, transitions=Any, inspectorPos=[]):
        self.__name = name
        self.__enterFunc = enterFunc
        self.__exitFunc = exitFunc
        self.__transitions = transitions
        self.__FSMList = []

    def getName(self):
        return self.__name

    def setName(self, stateName):
        self.__name = stateName

    def getEnterFunc(self):
        return self.__enterFunc

    def setEnterFunc(self, stateEnterFunc):
        self.__enterFunc = stateEnterFunc

    def getExitFunc(self):
        return self.__exitFunc

    def setExitFunc(self, stateExitFunc):
        self.__exitFunc = stateExitFunc

    def transitionsToAny(self):
        return self.__transitions is State.Any

    def getTransitions(self):
        if self.transitionsToAny():
            return []
        return self.__transitions

    def isTransitionDefined(self, otherState):
        if self.transitionsToAny():
            return 1
        if type(otherState) != type(''):
            otherState = otherState.getName()
        return otherState in self.__transitions

    def setTransitions(self, stateTransitions):
        self.__transitions = stateTransitions

    def addTransition(self, transition):
        if not self.transitionsToAny():
            self.__transitions.append(transition)
        else:
            State.notify.warning('attempted to add transition %s to state that transitions to any state')

    def getChildren(self):
        return self.__FSMList

    def setChildren(self, FSMList):
        self.__FSMList = FSMList

    def addChild(self, ClassicFSM):
        self.__FSMList.append(ClassicFSM)

    def removeChild(self, ClassicFSM):
        if ClassicFSM in self.__FSMList:
            self.__FSMList.remove(ClassicFSM)

    def hasChildren(self):
        return len(self.__FSMList) > 0

    def __enterChildren(self, argList):
        for fsm in self.__FSMList:
            if fsm.getCurrentState():
                fsm.conditional_request(fsm.getInitialState().getName())
            else:
                fsm.enterInitialState()

    def __exitChildren(self, argList):
        for fsm in self.__FSMList:
            fsm.request(fsm.getFinalState().getName())

    def enter(self, argList=[]):
        self.__enterChildren(argList)
        if self.__enterFunc != None:
            apply(self.__enterFunc, argList)
        return

    def exit(self, argList=[]):
        self.__exitChildren(argList)
        if self.__exitFunc != None:
            apply(self.__exitFunc, argList)
        return

    def __str__(self):
        return 'State: name = %s, enter = %s, exit = %s, trans = %s, children = %s' % (self.__name, self.__enterFunc, self.__exitFunc, self.__transitions, self.__FSMList)