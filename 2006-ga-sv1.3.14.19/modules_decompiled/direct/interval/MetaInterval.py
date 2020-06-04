# File: M (Python 2.2)

from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
from IntervalManager import ivalMgr
import Interval
from direct.task import Task
import types
PREVIOUS_END = CMetaInterval.RSPreviousEnd
PREVIOUS_START = CMetaInterval.RSPreviousBegin
TRACK_START = CMetaInterval.RSLevelBegin

class MetaInterval(CMetaInterval):
    notify = directNotify.newCategory('MetaInterval')
    SequenceNum = 1
    
    def __init__(self, *ivals, **kw):
        name = None
        if kw.has_key('name'):
            name = kw['name']
            del kw['name']
        
        autoPause = 0
        autoFinish = 0
        if kw.has_key('autoPause'):
            autoPause = kw['autoPause']
            del kw['autoPause']
        
        if kw.has_key('autoFinish'):
            autoFinish = kw['autoFinish']
            del kw['autoFinish']
        
        self.phonyDuration = -1
        if kw.has_key('duration'):
            self.phonyDuration = kw['duration']
            del kw['duration']
        
        if kw:
            self.notify.error('Unexpected keyword parameters: %s' % kw.keys())
        
        self.ivals = ivals
        self._MetaInterval__ivalsDirty = 1
        if name == None:
            name = '%s-%d' % (self.__class__.__name__, self.SequenceNum)
            MetaInterval.SequenceNum += 1
        
        CMetaInterval.__init__(self, name)
        self._MetaInterval__manager = ivalMgr
        self.setAutoPause(autoPause)
        self.setAutoFinish(autoFinish)
        self.pythonIvals = []

    
    def append(self, ival):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        self.ivals.append(ival)
        self._MetaInterval__ivalsDirty = 1

    
    def extend(self, ivals):
        self += ivals

    
    def count(self, ival):
        return self.ivals.count(ival)

    
    def index(self, ival):
        return self.ivals.index(ival)

    
    def insert(self, index, ival):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        self.ivals.insert(index, ival)
        self._MetaInterval__ivalsDirty = 1

    
    def pop(self, index = None):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        self._MetaInterval__ivalsDirty = 1
        if index == None:
            return self.ivals.pop()
        else:
            return self.ivals.pop(index)

    
    def remove(self, ival):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        self.ivals.remove(ival)
        self._MetaInterval__ivalsDirty = 1

    
    def reverse(self):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        self.ivals.reverse()
        self._MetaInterval__ivalsDirty = 1

    
    def sort(self, cmpfunc = None):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        self._MetaInterval__ivalsDirty = 1
        if cmpfunc == None:
            self.ivals.sort()
        else:
            self.ivals.sort(cmpfunc)

    
    def __len__(self):
        return len(self.ivals)

    
    def __getitem__(self, index):
        return self.ivals[index]

    
    def __setitem__(self, index, value):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        self.ivals[index] = value
        self._MetaInterval__ivalsDirty = 1

    
    def __delitem__(self, index):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        del self.ivals[index]
        self._MetaInterval__ivalsDirty = 1

    
    def __getslice__(self, i, j):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        return self.__class__(self.ivals[i:j])

    
    def __setslice__(self, i, j, s):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        self.ivals[i:j] = s
        self._MetaInterval__ivalsDirty = 1

    
    def __delslice__(self, i, j):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        del self.ivals[i:j]
        self._MetaInterval__ivalsDirty = 1

    
    def __iadd__(self, other):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        
        if isinstance(other, MetaInterval):
            ivals = other.ivals
        else:
            ivals = list(other)
        self.ivals += ivals
        self._MetaInterval__ivalsDirty = 1
        return self

    
    def __add__(self, other):
        copy = self[:]
        copy += other
        return copy

    
    def addSequence(self, list, name, relTime, relTo, duration):
        self.pushLevel(name, relTime, relTo)
        for ival in list:
            self.addInterval(ival, 0.0, PREVIOUS_END)
        
        self.popLevel(duration)

    
    def addParallel(self, list, name, relTime, relTo, duration):
        self.pushLevel(name, relTime, relTo)
        for ival in list:
            self.addInterval(ival, 0.0, TRACK_START)
        
        self.popLevel(duration)

    
    def addParallelEndTogether(self, list, name, relTime, relTo, duration):
        maxDuration = 0
        for ival in list:
            maxDuration = max(maxDuration, ival.getDuration())
        
        self.pushLevel(name, relTime, relTo)
        for ival in list:
            self.addInterval(ival, maxDuration - ival.getDuration(), TRACK_START)
        
        self.popLevel(duration)

    
    def addTrack(self, list, name, relTime, relTo, duration):
        self.pushLevel(name, relTime, relTo)
        for tuple in list:
            if isinstance(tuple, types.TupleType) or isinstance(tuple, types.ListType):
                relTime = tuple[0]
                ival = tuple[1]
                if len(tuple) >= 3:
                    relTo = tuple[2]
                else:
                    relTo = TRACK_START
                self.addInterval(ival, relTime, relTo)
            else:
                self.notify.error('Not a tuple in Track: %s' % (tuple,))
        
        self.popLevel(duration)

    
    def addInterval(self, ival, relTime, relTo):
        if isinstance(ival, CInterval):
            if getattr(ival, 'inPython', 0):
                index = len(self.pythonIvals)
                self.pythonIvals.append(ival)
                self.addExtIndex(index, ival.getName(), ival.getDuration(), ival.getOpenEnded(), relTime, relTo)
            elif isinstance(ival, MetaInterval):
                ival.applyIvals(self, relTime, relTo)
            else:
                self.addCInterval(ival, relTime, relTo)
        elif isinstance(ival, Interval.Interval):
            index = len(self.pythonIvals)
            self.pythonIvals.append(ival)
            self.addExtIndex(index, ival.getName(), ival.getDuration(), ival.getOpenEnded(), relTime, relTo)
        else:
            self.notify.error('Not an Interval: %s' % (ival,))

    
    def setManager(self, manager):
        self._MetaInterval__manager = manager
        CMetaInterval.setManager(self, manager)

    
    def getManager(self):
        return self._MetaInterval__manager

    
    def setT(self, t):
        self._MetaInterval__updateIvals()
        CMetaInterval.setT(self, t)

    
    def start(self, startT = 0.0, endT = -1.0, playRate = 1.0):
        self._MetaInterval__updateIvals()
        self.setupPlay(startT, endT, playRate, 0)
        self._MetaInterval__manager.addInterval(self)

    
    def loop(self, startT = 0.0, endT = -1.0, playRate = 1.0):
        self._MetaInterval__updateIvals()
        self.setupPlay(startT, endT, playRate, 1)
        self._MetaInterval__manager.addInterval(self)

    
    def pause(self):
        if self.getState() == CInterval.SStarted:
            self.privInterrupt()
        
        self._MetaInterval__manager.removeInterval(self)
        self.privPostEvent()
        return self.getT()

    
    def resume(self, startT = None):
        self._MetaInterval__updateIvals()
        if startT != None:
            self.setT(startT)
        
        self.setupResume()
        self._MetaInterval__manager.addInterval(self)

    
    def resumeUntil(self, endT):
        self._MetaInterval__updateIvals()
        self.setupResumeUntil(endT)
        self._MetaInterval__manager.addInterval(self)

    
    def finish(self):
        self._MetaInterval__updateIvals()
        state = self.getState()
        if state == CInterval.SInitial:
            self.privInstant()
        elif state != CInterval.SFinal:
            self.privFinalize()
        
        self._MetaInterval__manager.removeInterval(self)
        self.privPostEvent()

    
    def validateComponent(self, component):
        if not isinstance(component, CInterval):
            pass
        return isinstance(component, Interval.Interval)

    
    def validateComponents(self, components):
        for component in components:
            if not self.validateComponent(component):
                return 0
            
        
        return 1

    
    def _MetaInterval__updateIvals(self):
        if self._MetaInterval__ivalsDirty:
            self.clearIntervals()
            self.applyIvals(self, 0, TRACK_START)
            self._MetaInterval__ivalsDirty = 0
        

    
    def clearIntervals(self):
        CMetaInterval.clearIntervals(self)
        self.inPython = 0

    
    def applyIvals(self, meta, relTime, relTo):
        if len(self.ivals) == 0:
            pass
        1
        if len(self.ivals) == 1:
            meta.addInterval(self.ivals[0], relTime, relTo)
        else:
            self.notify.error('Cannot build list from MetaInterval directly.')

    
    def _MetaInterval__doPythonCallbacks(self):
        ival = None
        
        try:
            while self.isEventReady():
                index = self.getEventIndex()
                t = self.getEventT()
                eventType = self.getEventType()
                self.popEvent()
                ival = self.pythonIvals[index]
                ival.privDoEvent(t, eventType)
                ival.privPostEvent()
                ival = None
        except:
            if ival != None:
                print 'Exception occurred while processing %s of %s:' % (ival.getName(), self.getName())
            else:
                print 'Exception occurred while processing %s:' % self.getName()
            print self
            raise 


    
    def privDoEvent(self, t, event):
        self._MetaInterval__updateIvals()
        CMetaInterval.privDoEvent(self, t, event)

    
    def privPostEvent(self):
        self._MetaInterval__doPythonCallbacks()
        CMetaInterval.privPostEvent(self)

    
    def setIntervalStartTime(self, *args, **kw):
        self._MetaInterval__updateIvals()
        self.inPython = 1
        return CMetaInterval.setIntervalStartTime(self, *args, **args)

    
    def getIntervalStartTime(self, *args, **kw):
        self._MetaInterval__updateIvals()
        return CMetaInterval.getIntervalStartTime(self, *args, **args)

    
    def getDuration(self):
        self._MetaInterval__updateIvals()
        return CMetaInterval.getDuration(self)

    
    def __repr__(self, *args, **kw):
        self._MetaInterval__updateIvals()
        return CMetaInterval.__repr__(self, *args, **args)

    
    def __str__(self, *args, **kw):
        self._MetaInterval__updateIvals()
        return CMetaInterval.__str__(self, *args, **args)

    
    def timeline(self, out = None):
        self._MetaInterval__updateIvals()
        if out == None:
            out = ostream
        
        CMetaInterval.timeline(self, out)



class Sequence(MetaInterval):
    
    def applyIvals(self, meta, relTime, relTo):
        meta.addSequence(self.ivals, self.getName(), relTime, relTo, self.phonyDuration)



class Parallel(MetaInterval):
    
    def applyIvals(self, meta, relTime, relTo):
        meta.addParallel(self.ivals, self.getName(), relTime, relTo, self.phonyDuration)



class ParallelEndTogether(MetaInterval):
    
    def applyIvals(self, meta, relTime, relTo):
        meta.addParallelEndTogether(self.ivals, self.getName(), relTime, relTo, self.phonyDuration)



class Track(MetaInterval):
    
    def applyIvals(self, meta, relTime, relTo):
        meta.addTrack(self.ivals, self.getName(), relTime, relTo, self.phonyDuration)

    
    def validateComponent(self, tuple):
        if not isinstance(tuple, types.TupleType):
            pass
        if not isinstance(tuple, types.ListType):
            return 0
        
        relTime = tuple[0]
        ival = tuple[1]
        if len(tuple) >= 3:
            relTo = tuple[2]
        else:
            relTo = TRACK_START
        if not isinstance(relTime, types.FloatType):
            pass
        if not isinstance(relTime, types.IntType):
            return 0
        
        if not MetaInterval.validateComponent(self, ival):
            return 0
        
        if relTo != PREVIOUS_END and relTo != PREVIOUS_START and relTo != TRACK_START:
            return 0
        
        return 1


