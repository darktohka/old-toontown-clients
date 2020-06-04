# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\parties\activityFSMs.py
from direct.directnotify import DirectNotifyGlobal
from BaseActivityFSM import BaseActivityFSM
from activityFSMMixins import IdleMixin
from activityFSMMixins import RulesMixin
from activityFSMMixins import ActiveMixin
from activityFSMMixins import DisabledMixin
from activityFSMMixins import ConclusionMixin
from activityFSMMixins import WaitForEnoughMixin
from activityFSMMixins import WaitToStartMixin
from activityFSMMixins import WaitClientsReadyMixin
from activityFSMMixins import WaitForServerMixin

class FireworksActivityFSM(BaseActivityFSM, IdleMixin, ActiveMixin, DisabledMixin):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FireworksActivityFSM')

    def __init__(self, activity):
        FireworksActivityFSM.notify.debug('__init__')
        BaseActivityFSM.__init__(self, activity)
        self.defaultTransitions = {'Idle': ['Active', 'Disabled'], 'Active': ['Disabled'], 'Disabled': []}


class CatchActivityFSM(BaseActivityFSM, IdleMixin, ActiveMixin, ConclusionMixin):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('CatchActivityFSM')

    def __init__(self, activity):
        CatchActivityFSM.notify.debug('__init__')
        BaseActivityFSM.__init__(self, activity)
        self.defaultTransitions = {'Idle': ['Active', 'Conclusion'], 'Active': ['Conclusion'], 'Conclusion': ['Idle']}


class TrampolineActivityFSM(BaseActivityFSM, IdleMixin, RulesMixin, ActiveMixin):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TrampolineActivityFSM')

    def __init__(self, activity):
        TrampolineActivityFSM.notify.debug('__init__')
        BaseActivityFSM.__init__(self, activity)
        self.defaultTransitions = {'Idle': ['Rules', 'Active'], 'Rules': ['Active', 'Idle'], 'Active': ['Idle']}


class DanceActivityFSM(BaseActivityFSM, IdleMixin, ActiveMixin, DisabledMixin):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DanceActivityFSM')

    def __init__(self, activity):
        DanceActivityFSM.notify.debug('__init__')
        BaseActivityFSM.__init__(self, activity)
        self.defaultTransitions = {'Active': ['Disabled'], 'Disabled': ['Active']}


class TeamActivityAIFSM(BaseActivityFSM, WaitForEnoughMixin, WaitToStartMixin, WaitClientsReadyMixin, ActiveMixin, ConclusionMixin):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TeamActivityAIFSM')

    def __init__(self, activity):
        BaseActivityFSM.__init__(self, activity)
        self.notify.debug('__init__')
        self.defaultTransitions = {'WaitForEnough': ['WaitToStart'], 'WaitToStart': ['WaitForEnough', 'WaitClientsReady'], 'WaitClientsReady': ['WaitForEnough', 'Active'], 'Active': ['WaitForEnough', 'Conclusion'], 'Conclusion': ['WaitForEnough']}


class TeamActivityFSM(BaseActivityFSM, WaitForEnoughMixin, WaitToStartMixin, RulesMixin, WaitForServerMixin, ActiveMixin, ConclusionMixin):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TeamActivityFSM')

    def __init__(self, activity):
        BaseActivityFSM.__init__(self, activity)
        self.defaultTransitions = {'WaitForEnough': ['WaitToStart'], 'WaitToStart': ['WaitForEnough', 'Rules'], 'Rules': ['WaitForServer', 'Active', 'WaitForEnough'], 'WaitForServer': ['Active', 'WaitForEnough'], 'Active': ['Conclusion', 'WaitForEnough'], 'Conclusion': ['WaitForEnough']}