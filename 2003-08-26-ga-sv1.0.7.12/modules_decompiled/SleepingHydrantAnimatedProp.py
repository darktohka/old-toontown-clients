# File: S (Python 2.2)

import AnimatedProp
from IntervalGlobal import *
import Task
import math

class SleepingHydrantAnimatedProp(AnimatedProp.AnimatedProp):
    
    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        self.task = None

    
    def bobTask(self, task):
        self.node.setSz(1.0 + 0.080000000000000002 * math.sin(task.time))
        return Task.cont

    
    def enter(self):
        AnimatedProp.AnimatedProp.enter(self)
        self.task = taskMgr.add(self.bobTask, self.uniqueName('bobTask'))

    
    def exit(self):
        AnimatedProp.AnimatedProp.exit(self)
        if self.task:
            taskMgr.remove(self.task)
            self.task = None
        


