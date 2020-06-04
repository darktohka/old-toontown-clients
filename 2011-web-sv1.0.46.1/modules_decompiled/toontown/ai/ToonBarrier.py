# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\ai\ToonBarrier.py
from otp.ai.AIBase import *
from direct.task import Task
from direct.showbase import DirectObject
import random

class ToonBarrier(DirectObject.DirectObject):
    __module__ = __name__
    notify = directNotify.newCategory('ToonBarrier')

    def __init__(self, name, uniqueName, avIdList, timeout, clearedFunc=None, timeoutFunc=None, doneFunc=None):
        self.name = name
        self.uniqueName = uniqueName + '-Barrier'
        self.avIdList = avIdList[:]
        self.pendingToons = self.avIdList[:]
        self.timeout = timeout
        self.clearedFunc = clearedFunc
        self.timeoutFunc = timeoutFunc
        self.doneFunc = doneFunc
        if len(self.pendingToons) == 0:
            self.notify.debug('%s: barrier with empty list' % self.uniqueName)
            self.active = 0
            if self.clearedFunc:
                self.clearedFunc()
            if self.doneFunc:
                self.doneFunc(self.avIdList)
            return
        self.taskName = self.uniqueName + '-Timeout'
        origTaskName = self.taskName
        while taskMgr.hasTaskNamed(self.taskName):
            self.taskName = origTaskName + '-' + str(random.randint(0, 10000))

        taskMgr.doMethodLater(self.timeout, self.__timerExpired, self.taskName)
        for avId in self.avIdList:
            event = simbase.air.getAvatarExitEvent(avId)
            self.acceptOnce(event, self.__handleUnexpectedExit, extraArgs=[avId])

        self.notify.debug('%s: expecting responses from %s within %s seconds' % (self.uniqueName, self.avIdList, self.timeout))
        self.active = 1

    def cleanup(self):
        if self.active:
            taskMgr.remove(self.taskName)
            self.active = 0
        self.ignoreAll()

    def clear(self, avId):
        if avId not in self.pendingToons:
            self.notify.warning('%s: tried to clear %s, who was not listed.' % (self.uniqueName, avId))
            return
        self.notify.debug('%s: clearing avatar %s' % (self.uniqueName, avId))
        self.pendingToons.remove(avId)
        if len(self.pendingToons) == 0:
            self.notify.debug('%s: barrier cleared by %s' % (self.uniqueName, self.avIdList))
            self.cleanup()
            if self.clearedFunc:
                self.clearedFunc()
            if self.doneFunc:
                self.doneFunc(self.avIdList)

    def isActive(self):
        return self.active

    def getPendingToons(self):
        return self.pendingToons[:]

    def __timerExpired(self, task):
        self.notify.warning('%s: timeout expired; responses not received from %s' % (self.uniqueName, self.pendingToons))
        self.cleanup()
        if self.timeoutFunc:
            self.timeoutFunc(self.pendingToons[:])
        if self.doneFunc:
            clearedAvIds = self.avIdList[:]
            for avId in self.pendingToons:
                clearedAvIds.remove(avId)

            self.doneFunc(clearedAvIds)
        return Task.done

    def __handleUnexpectedExit(self, avId):
        if avId not in self.avIdList:
            return
        self.avIdList.remove(avId)
        if avId in self.pendingToons:
            self.clear(avId)