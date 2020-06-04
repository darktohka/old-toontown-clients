# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedDoorEntityBase.py


def stubFunction(*args):
    pass


class LockBase:
    __module__ = __name__
    stateNames = ['off', 'locking', 'locked', 'unlocking', 'unlocked']
    stateDurations = [None, 3.5, None, 4.0, None]


class DistributedDoorEntityBase:
    __module__ = __name__
    stateNames = ['off', 'opening', 'open', 'closing', 'closed']
    stateDurations = [None, 5.0, 1.0, 6.0, None]