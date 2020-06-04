# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\task\FrameProfiler.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.fsm.StatePush import FunctionCall
from direct.showbase.PythonUtil import formatTimeExact, normalDistrib
from direct.task import Task

class FrameProfiler:
    __module__ = __name__
    notify = directNotify.newCategory('FrameProfiler')
    Minute = 60
    Hour = 60 * Minute
    Day = 24 * Hour

    def __init__(self):
        Hour = FrameProfiler.Hour
        self._period = 2 * FrameProfiler.Minute
        if config.GetBool('frequent-frame-profiles', 0):
            self._period = 1 * FrameProfiler.Minute
        self._jitterMagnitude = self._period * 0.75
        self._logSchedule = [
         1 * FrameProfiler.Hour, 4 * FrameProfiler.Hour, 12 * FrameProfiler.Hour, 1 * FrameProfiler.Day]
        if config.GetBool('frequent-frame-profiles', 0):
            self._logSchedule = [
             1 * FrameProfiler.Minute, 4 * FrameProfiler.Minute, 12 * FrameProfiler.Minute, 24 * FrameProfiler.Minute]
        for t in self._logSchedule:
            pass

        for i in xrange(len(self._logSchedule)):
            e = self._logSchedule[i]
            for j in xrange(i, len(self._logSchedule)):
                pass

        self._enableFC = FunctionCall(self._setEnabled, taskMgr.getProfileFramesSV())
        self._enableFC.pushCurrentState()

    def destroy(self):
        self._enableFC.set(False)
        self._enableFC.destroy()

    def _setEnabled(self, enabled):
        if enabled:
            self.notify.info('frame profiler started')
            self._startTime = globalClock.getFrameTime()
            self._profileCounter = 0
            self._jitter = None
            self._period2aggregateProfile = {}
            self._id2session = {}
            self._id2task = {}
            self._task = taskMgr.doMethodLater(self._period, self._scheduleNextProfileDoLater, 'FrameProfilerStart-%s' % serialNum())
        else:
            self._task.remove()
            del self._task
            for session in self._period2aggregateProfile.itervalues:
                session.release()

            del self._period2aggregateProfile
            for task in self._id2task.itervalues():
                task.remove()

            del self._id2task
            for session in self._id2session.itervalues():
                session.release()

            del self._id2session
            self.notify.info('frame profiler stopped')
        return

    def _scheduleNextProfileDoLater(self, task):
        self._scheduleNextProfile()
        return task.done

    def _scheduleNextProfile(self):
        self._profileCounter += 1
        self._timeElapsed = self._profileCounter * self._period
        time = self._startTime + self._timeElapsed
        jitter = self._jitter
        if jitter is None:
            jitter = normalDistrib(-self._jitterMagnitude, self._jitterMagnitude)
            time += jitter
        else:
            time -= jitter
            jitter = None
        self._jitter = jitter
        sessionId = serialNum()
        session = taskMgr.getProfileSession('FrameProfile-%s' % sessionId)
        self._id2session[sessionId] = session
        taskMgr.profileFrames(num=1, session=session, callback=Functor(self._analyzeResults, sessionId))
        delay = max(time - globalClock.getFrameTime(), 0.0)
        self._task = taskMgr.doMethodLater(delay, self._scheduleNextProfileDoLater, 'FrameProfiler-%s' % serialNum())
        return

    def _analyzeResults(self, sessionId):
        self._id2task[sessionId] = taskMgr.add(Functor(self._doAnalysis, sessionId), 'FrameProfilerAnalysis-%s' % sessionId)

    def _doAnalysis(self, sessionId, task):
        if hasattr(task, '_generator'):
            gen = task._generator
        else:
            gen = self._doAnalysisGen(sessionId)
            task._generator = gen
        result = gen.next()
        if result == Task.done:
            del task._generator
        return result

    def _doAnalysisGen(self, sessionId):
        p2ap = self._period2aggregateProfile
        self._id2task.pop(sessionId)
        session = self._id2session.pop(sessionId)
        if session.profileSucceeded():
            period = self._logSchedule[0]
            if period not in self._period2aggregateProfile:
                p2ap[period] = session.getReference()
            else:
                p2ap[period].aggregate(session)
        else:
            self.notify.warning('frame profile did not succeed')
        session.release()
        session = None
        counter = 0
        for pi in xrange(len(self._logSchedule)):
            period = self._logSchedule[pi]
            if self._timeElapsed % period == 0:
                if period in p2ap:
                    if counter >= 3:
                        counter = 0
                        yield Task.cont
                    self.notify.info('aggregate profile of sampled frames over last %s\n%s' % (formatTimeExact(period), p2ap[period].getResults()))
                    counter += 1
                    nextIndex = pi + 1
                    if nextIndex >= len(self._logSchedule):
                        nextPeriod = period * 2
                        self._logSchedule.append(nextPeriod)
                    else:
                        nextPeriod = self._logSchedule[nextIndex]
                    if nextPeriod not in p2ap:
                        p2ap[nextPeriod] = p2ap[period].getReference()
                    else:
                        p2ap[nextPeriod].aggregate(p2ap[period])
                    p2ap[period].release()
                    del p2ap[period]
            else:
                break

        yield Task.done
        return