# File: I (Python 2.2)

from direct.showbase.DirectObject import *
from pandac.PandaModules import *
from direct.task import Task
from direct.showbase import PythonUtil
import math

class Interval(DirectObject):
    notify = directNotify.newCategory('Interval')
    playbackCounter = 0
    
    def __init__(self, name, duration, openEnded = 1):
        self.name = name
        self.duration = max(duration, 0.0)
        self.state = CInterval.SInitial
        self.currT = 0.0
        self.doneEvent = None
        self.setTHooks = []
        self._Interval__startT = 0
        self._Interval__startTAtStart = 1
        self._Interval__endT = duration
        self._Interval__endTAtEnd = 1
        self._Interval__playRate = 1.0
        self._Interval__doLoop = 0
        self._Interval__loopCount = 0
        self.openEnded = openEnded

    
    def getName(self):
        return self.name

    
    def getDuration(self):
        return self.duration

    
    def getOpenEnded(self):
        return self.openEnded

    
    def setLoop(self, loop = 1):
        self._Interval__doLoop = loop

    
    def getLoop(self):
        return self._Interval__doLoop

    
    def getState(self):
        return self.state

    
    def isStopped(self):
        if not self.getState() == CInterval.SInitial:
            pass
        return self.getState() == CInterval.SFinal

    
    def setT(self, t):
        state = self.getState()
        if state == CInterval.SInitial:
            self.privInitialize(t)
            if self.isPlaying():
                self.setupResume()
            else:
                self.privInterrupt()
        elif state == CInterval.SStarted:
            self.privInterrupt()
            self.privStep(t)
            self.setupResume()
        elif state == CInterval.SPaused:
            self.privStep(t)
            self.privInterrupt()
        elif state == CInterval.SFinal:
            self.privReverseInitialize(t)
            if self.isPlaying():
                self.setupResume()
            else:
                self.privInterrupt()
        else:
            self.notify.error('Invalid state: %s' % state)
        self.privPostEvent()

    
    def getT(self):
        return self.currT

    
    def start(self, startT = 0.0, endT = -1.0, playRate = 1.0):
        self.setupPlay(startT, endT, playRate, 0)
        self._Interval__spawnTask()

    
    def loop(self, startT = 0.0, endT = -1.0, playRate = 1.0):
        self.setupPlay(startT, endT, playRate, 1)
        self._Interval__spawnTask()

    
    def pause(self):
        if self.getState() == CInterval.SStarted:
            self.privInterrupt()
        
        self.privPostEvent()
        self._Interval__removeTask()
        return self.getT()

    
    def resume(self, startT = None):
        if startT != None:
            self.setT(startT)
        
        self.setupResume()
        if not self.isPlaying():
            self._Interval__spawnTask()
        

    
    def resumeUntil(self, endT):
        duration = self.getDuration()
        if endT < 0 or endT >= duration:
            self._Interval__endT = duration
            self._Interval__endTAtEnd = 1
        else:
            self._Interval__endT = endT
            self._Interval__endTAtEnd = 0
        self.setupResume()
        if not self.isPlaying():
            self._Interval__spawnTask()
        

    
    def finish(self):
        state = self.getState()
        if state == CInterval.SInitial:
            self.privInstant()
        elif state != CInterval.SFinal:
            self.privFinalize()
        
        self.privPostEvent()
        self._Interval__removeTask()

    
    def isPlaying(self):
        return taskMgr.hasTaskNamed(self.getName() + '-play')

    
    def setDoneEvent(self, event):
        self.doneEvent = event

    
    def getDoneEvent(self):
        return self.doneEvent

    
    def privDoEvent(self, t, event):
        if event == CInterval.ETStep:
            self.privStep(t)
        elif event == CInterval.ETFinalize:
            self.privFinalize()
        elif event == CInterval.ETInterrupt:
            self.privInterrupt()
        elif event == CInterval.ETInstant:
            self.privInstant()
        elif event == CInterval.ETInitialize:
            self.privInitialize(t)
        elif event == CInterval.ETReverseFinalize:
            self.privReverseFinalize()
        elif event == CInterval.ETReverseInstant:
            self.privReverseInstant()
        elif event == CInterval.ETReverseInitialize:
            self.privReverseInitialize(t)
        else:
            self.notify.error('Invalid event type: %s' % event)

    
    def privInitialize(self, t):
        self.state = CInterval.SStarted
        self.privStep(t)

    
    def privInstant(self):
        self.state = CInterval.SStarted
        self.privStep(self.getDuration())
        self.state = CInterval.SFinal
        self.intervalDone()

    
    def privStep(self, t):
        self.state = CInterval.SStarted
        self.currT = t

    
    def privFinalize(self):
        self.privStep(self.getDuration())
        self.state = CInterval.SFinal
        self.intervalDone()

    
    def privReverseInitialize(self, t):
        self.state = CInterval.SStarted
        self.privStep(t)

    
    def privReverseInstant(self):
        self.state = CInterval.SStarted
        self.privStep(self.getDuration())
        self.state = CInterval.SInitial

    
    def privReverseFinalize(self):
        self.privStep(0)
        self.state = CInterval.SInitial

    
    def privInterrupt(self):
        self.state = CInterval.SPaused

    
    def intervalDone(self):
        if self.doneEvent:
            messenger.send(self.doneEvent)
        

    
    def setupPlay(self, startT, endT, playRate, doLoop):
        duration = self.getDuration()
        if startT <= 0:
            self._Interval__startT = 0
            self._Interval__startTAtStart = 1
        elif startT > duration:
            self._Interval__startT = duration
            self._Interval__startTAtStart = 0
        else:
            self._Interval__startT = startT
            self._Interval__startTAtStart = 0
        if endT < 0 or endT >= duration:
            self._Interval__endT = duration
            self._Interval__endTAtEnd = 1
        else:
            self._Interval__endT = endT
            self._Interval__endTAtEnd = 0
        self._Interval__clockStart = globalClock.getFrameTime()
        self._Interval__playRate = playRate
        self._Interval__doLoop = doLoop
        self._Interval__loopCount = 0

    
    def setupResume(self):
        now = globalClock.getFrameTime()
        if self._Interval__playRate > 0:
            self._Interval__clockStart = now - (self.getT() - self._Interval__startT) / self._Interval__playRate
        elif self._Interval__playRate < 0:
            self._Interval__clockStart = now - (self.getT() - self._Interval__endT) / self._Interval__playRate
        
        self._Interval__loopCount = 0

    
    def stepPlay(self):
        now = globalClock.getFrameTime()
        if self._Interval__playRate >= 0:
            t = (now - self._Interval__clockStart) * self._Interval__playRate + self._Interval__startT
            if self._Interval__endTAtEnd:
                self._Interval__endT = self.getDuration()
            
            if t < self._Interval__endT:
                if self.isStopped():
                    self.privInitialize(t)
                else:
                    self.privStep(t)
            elif self._Interval__endTAtEnd:
                if self.isStopped():
                    if self.getOpenEnded() or self._Interval__loopCount != 0:
                        self.privInstant()
                    
                else:
                    self.privFinalize()
            elif self.isStopped():
                self.privInitialize(self._Interval__endT)
            else:
                self.privStep(self._Interval__endT)
            if self._Interval__endT == self._Interval__startT:
                self._Interval__loopCount += 1
            else:
                timePerLoop = (self._Interval__endT - self._Interval__startT) / self._Interval__playRate
                numLoops = math.floor((now - self._Interval__clockStart) / timePerLoop)
                self._Interval__loopCount += numLoops
                self._Interval__clockStart += numLoops * timePerLoop
        
        if not self._Interval__loopCount == 0:
            pass
        shouldContinue = self._Interval__doLoop
        if not shouldContinue and self.getState() == CInterval.SStarted:
            self.privInterrupt()
        
        return shouldContinue

    
    def __repr__(self, indent = 0):
        space = ''
        for l in range(indent):
            space = space + ' '
        
        return space + self.name + ' dur: %.2f' % self.duration

    
    def play(self, *args, **kw):
        self.notify.error('using deprecated Interval.play() interface')
        self.start(*args, **args)

    
    def stop(self):
        self.notify.error('using deprecated Interval.stop() interface')
        self.finish()

    
    def setFinalT(self):
        self.notify.error('using deprecated Interval.setFinalT() interface')
        self.finish()

    
    def privPostEvent(self):
        t = self.getT()
        if hasattr(self, 'setTHooks'):
            for func in self.setTHooks:
                func(t)
            
        

    
    def _Interval__spawnTask(self):
        Task = Task
        import direct.task
        self._Interval__removeTask()
        taskName = self.getName() + '-play'
        task = Task.Task(self._Interval__playTask)
        task.interval = self
        taskMgr.add(task, taskName)

    
    def _Interval__removeTask(self):
        taskName = self.getName() + '-play'
        oldTasks = taskMgr.getTasksNamed(taskName)
        for task in oldTasks:
            if hasattr(task, 'interval'):
                task.interval.privInterrupt()
                taskMgr.remove(task)
            
        

    
    def _Interval__playTask(self, task):
        Task = Task
        import direct.task
        again = self.stepPlay()
        self.privPostEvent()
        if again:
            return Task.cont
        else:
            return Task.done

    
    def popupControls(self, tl = None):
        TkGlobal = TkGlobal
        import direct.showbase
        import math
        Toplevel = Toplevel
        Frame = Frame
        Button = Button
        LEFT = LEFT
        X = X
        import Tkinter
        import Pmw
        EntryScale = EntryScale
        import direct.tkwidgets
        if tl == None:
            tl = Toplevel()
            tl.title('Interval Controls')
        
        outerFrame = Frame(tl)
        
        def entryScaleCommand(t, s = self):
            s.setT(t)
            s.pause()

        self.es = EntryScale.EntryScale(outerFrame, text = self.getName(), min = 0, max = math.floor(self.getDuration() * 100) / 100, command = entryScaleCommand)
        es = EntryScale.EntryScale(outerFrame, text = self.getName(), min = 0, max = math.floor(self.getDuration() * 100) / 100, command = entryScaleCommand)
        es.set(self.getT(), fCommand = 0)
        es.pack(expand = 1, fill = X)
        bf = Frame(outerFrame)
        
        def toStart(s = self, es = es):
            s.pause()
            s.setT(0.0)
            s.pause()

        
        def toEnd(s = self):
            s.pause()
            s.setT(s.getDuration())
            s.pause()

        jumpToStart = Button(bf, text = '<<', command = toStart)
        
        def doPlay(s = self, es = es):
            s.resume(es.get())

        stop = Button(bf, text = 'Stop', command = lambda s = self: s.pause())
        play = Button(bf, text = 'Play', command = doPlay)
        jumpToEnd = Button(bf, text = '>>', command = toEnd)
        jumpToStart.pack(side = LEFT, expand = 1, fill = X)
        play.pack(side = LEFT, expand = 1, fill = X)
        stop.pack(side = LEFT, expand = 1, fill = X)
        jumpToEnd.pack(side = LEFT, expand = 1, fill = X)
        bf.pack(expand = 1, fill = X)
        outerFrame.pack(expand = 1, fill = X)
        
        def update(t, es = es):
            es.set(t, fCommand = 0)

        if not hasattr(self, 'setTHooks'):
            self.setTHooks = []
        
        self.setTHooks.append(update)
        
        def onDestroy(e, s = self, u = update):
            if u in s.setTHooks:
                s.setTHooks.remove(u)
            

        tl.bind('<Destroy>', onDestroy)


