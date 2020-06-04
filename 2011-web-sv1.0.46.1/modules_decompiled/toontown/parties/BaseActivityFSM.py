# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\parties\BaseActivityFSM.py
from direct.fsm.FSM import FSM
from direct.directnotify import DirectNotifyGlobal

class BaseActivityFSM(FSM):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('BaseActivityFSM')

    def __init__(self, activity):
        FSM.__init__(self, self.__class__.__name__)
        self.activity = activity
        self.defaultTransitions = None
        return