# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\TaskThreaded.py
__all__ = [
 'TaskThreaded', 'TaskThread']
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task

class TaskThreaded:
    __module__ = __name__
    notify = directNotify.newCategory('TaskThreaded')
    _Serial = SerialNumGen()

    def __init__(self, name, threaded=True, timeslice=None, callback=None):
        self.__name = name
        self.__threaded = threaded
        if timeslice is None:
            timeslice = 0.01
        self.__timeslice = timeslice
        self.__taskNames = set()
        self._taskStartTime = None
        self.__threads = set()
        self._callback = callback
        return

    def finished(self):
        if self._callback:
            self._callback()

    def destroy(self):
        for taskName in self.__taskNames:
            taskMgr.remove(taskName)

        del self.__taskNames
        for thread in self.__threads:
            thread.tearDown()
            thread._destroy()

        del self.__threads
        del self._callback
        self.ignoreAll()

    def getTimeslice(self):
        return self.___timeslice

    def setTimeslice(self, timeslice):
        self.__timeslice = timeslice

    def scheduleCallback(self, callback):
        if not self.__threaded:
            callback()
        else:
            taskName = '%s-ThreadedTask-%s' % (self.__name, TaskThreaded._Serial.next())
            self.__taskNames.add(taskName)
            taskMgr.add(Functor(self.__doCallback, callback, taskName), taskName)

    def scheduleThread(self, thread):
        thread._init(self)
        thread.setUp()
        if thread.isFinished():
            thread._destroy()
        elif not self.__threaded:
            while not thread.isFinished():
                thread.run()

            thread._destroy()
        else:
            self.__threads.add(thread)
            taskName = '%s-ThreadedTask-%s-%s' % (self.__name, thread.__class__.__name__, TaskThreaded._Serial.next())
            self.__taskNames.add(taskName)
            self.__threads.add(thread)
            taskMgr.add(Functor(self._doThreadCallback, thread, taskName), taskName)

    def _doCallback(self, callback, taskName, task):
        self.__taskNames.remove(taskName)
        self._taskStartTime = globalClock.getRealTime()
        callback()
        self._taskStartTime = None
        return Task.done

    def _doThreadCallback(self, thread, taskName, task):
        self._taskStartTime = globalClock.getRealTime()
        thread.run()
        self._taskStartTime = None
        if thread.isFinished():
            thread._destroy()
            self.__taskNames.remove(taskName)
            self.__threads.remove(thread)
            return Task.done
        else:
            return Task.cont
        return

    def taskTimeLeft(self):
        if self._taskStartTime is None:
            return True
        return globalClock.getRealTime() - self._taskStartTime < self.__timeslice


class TaskThread:
    __module__ = __name__

    def setUp(self):
        pass

    def run(self):
        pass

    def tearDown(self):
        pass

    def done(self):
        pass

    def finished(self):
        self.tearDown()
        self._finished = True
        self.done()

    def isFinished(self):
        return self._finished

    def timeLeft(self):
        return self.parent.taskTimeLeft()

    def _init(self, parent):
        self.parent = parent
        self._finished = False

    def _destroy(self):
        del self.parent
        del self._finished