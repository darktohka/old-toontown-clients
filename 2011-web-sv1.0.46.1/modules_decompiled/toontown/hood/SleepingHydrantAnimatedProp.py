# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\hood\SleepingHydrantAnimatedProp.py
import AnimatedProp
from direct.interval.IntervalGlobal import *
from direct.task import Task
import math

class SleepingHydrantAnimatedProp(AnimatedProp.AnimatedProp):
    __module__ = __name__

    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        self.task = None
        return

    def bobTask(self, task):
        self.node.setSz(1.0 + 0.08 * math.sin(task.time))
        return Task.cont

    def enter(self):
        AnimatedProp.AnimatedProp.enter(self)
        self.task = taskMgr.add(self.bobTask, self.uniqueName('bobTask'))

    def exit(self):
        AnimatedProp.AnimatedProp.exit(self)
        if self.task:
            taskMgr.remove(self.task)
            self.task = None
        return