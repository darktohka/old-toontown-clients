# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\RingAction.py
from direct.directnotify import DirectNotifyGlobal
import RingTrack

class RingAction:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('RingAction')

    def __init__(self):
        pass

    def eval(self, t):
        return (0, 0)


class RingActionStaticPos(RingAction):
    __module__ = __name__

    def __init__(self, pos):
        RingAction.__init__(self)
        self.__pos = pos

    def eval(self, t):
        return self.__pos


class RingActionFunction(RingAction):
    __module__ = __name__

    def __init__(self, func, args):
        RingAction.__init__(self)
        self.__func = func
        self.__args = args

    def eval(self, t):
        return self.__func(t, *self.__args)


class RingActionRingTrack(RingAction):
    __module__ = __name__

    def __init__(self, ringTrack):
        RingAction.__init__(self)
        self.__track = ringTrack

    def eval(self, t):
        return self.__track.eval(t)