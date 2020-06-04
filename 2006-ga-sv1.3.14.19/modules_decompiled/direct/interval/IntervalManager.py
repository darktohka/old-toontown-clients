# File: I (Python 2.2)

from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
from direct.showbase import EventManager
import Interval
import types
import fnmatch

class IntervalManager(CIntervalManager):
    
    def __init__(self, globalPtr = 0):
        if globalPtr:
            CIntervalManager.__init__(self, None)
            cObj = CIntervalManager.getGlobalPtr()
            self.this = cObj.this
            self.userManagesMemory = 0
        else:
            CIntervalManager.__init__(self)
        self.eventQueue = EventQueue()
        self.eventManager = EventManager.EventManager(self.eventQueue)
        self.setEventQueue(self.eventQueue)
        self.ivals = []
        self.removedIvals = { }

    
    def addInterval(self, interval):
        index = self.addCInterval(interval, 1)
        self._IntervalManager__storeInterval(interval, index)

    
    def removeInterval(self, interval):
        index = self.findCInterval(interval.getName())
        if index >= 0:
            self.removeCInterval(index)
            self.ivals[index] = None
            return 1
        
        return 0

    
    def getInterval(self, name):
        index = self.findCInterval(name)
        if index >= 0:
            return self.ivals[index]
        
        return None

    
    def finishIntervalsMatching(self, pattern):
        count = 0
        maxIndex = self.getMaxIndex()
        for index in range(maxIndex):
            ival = self.getCInterval(index)
            if ival and fnmatch.fnmatchcase(ival.getName(), pattern):
                count += 1
                if self.ivals[index]:
                    self.ivals[index].finish()
                else:
                    ival.finish()
            
        
        return count

    
    def step(self):
        CIntervalManager.step(self)
        self._IntervalManager__doPythonCallbacks()

    
    def interrupt(self):
        CIntervalManager.interrupt(self)
        self._IntervalManager__doPythonCallbacks()

    
    def _IntervalManager__doPythonCallbacks(self):
        index = self.getNextRemoval()
        while index >= 0:
            ival = self.ivals[index]
            self.ivals[index] = None
            ival.privPostEvent()
            index = self.getNextRemoval()
        index = self.getNextEvent()
        while index >= 0:
            self.ivals[index].privPostEvent()
            index = self.getNextEvent()
        self.eventManager.doEvents()

    
    def _IntervalManager__storeInterval(self, interval, index):
        while index >= len(self.ivals):
            self.ivals.append(None)
        self.ivals[index] = interval

    
    def __repr__(self):
        return self.__str__()


ivalMgr = IntervalManager(1)
