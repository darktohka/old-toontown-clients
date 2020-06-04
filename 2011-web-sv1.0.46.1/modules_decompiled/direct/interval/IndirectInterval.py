# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\interval\IndirectInterval.py
__all__ = [
 'IndirectInterval']
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
import Interval
from direct.showbase import LerpBlendHelpers

class IndirectInterval(Interval.Interval):
    __module__ = __name__
    indirectIntervalNum = 1
    notify = directNotify.newCategory('IndirectInterval')

    def __init__(self, interval, startT=0, endT=None, playRate=1, duration=None, blendType='noBlend', name=None):
        self.interval = interval
        self.startAtStart = startT == 0
        self.endAtEnd = endT == None or endT == interval.getDuration()
        if endT == None:
            endT = interval.getDuration()
        if duration == None:
            duration = abs(endT - startT) / playRate
        if name == None:
            name = 'IndirectInterval-%d' % IndirectInterval.indirectIntervalNum
            IndirectInterval.indirectIntervalNum += 1
        self.startT = startT
        self.endT = endT
        self.deltaT = endT - startT
        self.blendType = LerpBlendHelpers.getBlend(blendType)
        Interval.Interval.__init__(self, name, duration)
        return

    def __calcT(self, t):
        return self.startT + self.deltaT * self.blendType(t / self.duration)

    def privInitialize(self, t):
        state = self.interval.getState()
        if state == CInterval.SInitial or state == CInterval.SFinal:
            self.interval.privInitialize(self.__calcT(t))
        else:
            self.interval.privStep(self.__calcT(t))
        self.currT = t
        self.state = CInterval.SStarted
        self.interval.privPostEvent()

    def privInstant(self):
        state = self.interval.getState()
        if (state == CInterval.SInitial or state == CInterval.SFinal) and self.endAtEnd:
            self.interval.privInstant()
            self.currT = self.getDuration()
            self.interval.privPostEvent()
            self.intervalDone()
        else:
            if state == CInterval.SInitial or state == CInterval.SFinal:
                self.interval.privInitialize(self.startT)
            else:
                self.interval.privStep(self.startT)
            self.privFinalize()

    def privStep(self, t):
        self.interval.privStep(self.__calcT(t))
        self.currT = t
        self.state = CInterval.SStarted
        self.interval.privPostEvent()

    def privFinalize(self):
        if self.endAtEnd:
            self.interval.privFinalize()
        else:
            self.interval.privStep(self.endT)
            self.interval.privInterrupt()
        self.currT = self.getDuration()
        self.state = CInterval.SFinal
        self.interval.privPostEvent()
        self.intervalDone()

    def privReverseInitialize(self, t):
        state = self.interval.getState()
        if state == CInterval.SInitial or state == CInterval.SFinal:
            self.interval.privReverseInitialize(self.__calcT(t))
        else:
            self.interval.privStep(self.__calcT(t))
        self.currT = t
        self.state = CInterval.SStarted
        self.interval.privPostEvent()

    def privReverseInstant(self):
        state = self.interval.getState()
        if (state == CInterval.SInitial or state == CInterval.SFinal) and self.startAtStart:
            self.interval.privReverseInstant()
            self.currT = 0
            self.interval.privPostEvent()
        else:
            if state == CInterval.SInitial or state == CInterval.SFinal:
                self.interval.privReverseInitialize(self.endT)
            else:
                self.interval.privStep(self.endT)
            self.privReverseFinalize()

    def privReverseFinalize(self):
        if self.startAtStart:
            self.interval.privReverseFinalize()
        else:
            self.interval.privStep(self.endT)
            self.interval.privInterrupt()
        self.currT = 0
        self.state = CInterval.SInitial
        self.interval.privPostEvent()

    def privInterrupt(self):
        self.interval.privInterrupt()
        self.interval.privPostEvent()