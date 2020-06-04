# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\DropScheduler.py


class DropScheduler:
    __module__ = __name__

    def __init__(self, gameDuration, firstDropDelay, dropPeriod, maxDropDuration, fasterDropDelay, fasterDropPeriodMult, startTime=None):
        self.gameDuration = gameDuration
        self.firstDropDelay = firstDropDelay
        self._dropPeriod = dropPeriod
        self.maxDropDuration = maxDropDuration
        self.fasterDropDelay = fasterDropDelay
        self.fasterDropPeriodMult = fasterDropPeriodMult
        if startTime is None:
            startTime = 0
        self._startTime = startTime
        self.curT = self._startTime + self.firstDropDelay
        return

    def getT(self):
        return self.curT

    def getDuration(self):
        return self.gameDuration

    def getDropPeriod(self):
        delay = self._dropPeriod
        if self.curT - self._startTime >= self.fasterDropDelay:
            delay *= self.fasterDropPeriodMult
        return delay

    def doneDropping(self, continuous=None):
        landTime = self.getT() - self._startTime + self.maxDropDuration
        if continuous is None:
            continuous = False
        else:
            continuous = True
        if continuous:
            maxTime = self.gameDuration + self.maxDropDuration
        else:
            maxTime = self.gameDuration + self.getDropPeriod()
        return landTime >= maxTime

    def skipPercent(self, percent):
        numSkips = 0
        while True:
            prevT = self.curT
            self.stepT()
            if self.curT >= percent * self.gameDuration:
                self.curT = prevT
                break
            else:
                numSkips += 1

        return numSkips

    def stepT(self):
        self.curT += self.getDropPeriod()


class ThreePhaseDropScheduler(DropScheduler):
    __module__ = __name__

    def __init__(self, gameDuration, firstDropDelay, dropPeriod, maxDropDuration, slowerDropPeriodMult, normalDropDelay, fasterDropDelay, fasterDropPeriodMult, startTime=None):
        self._slowerDropPeriodMult = slowerDropPeriodMult
        self._normalDropDelay = normalDropDelay
        DropScheduler.__init__(self, gameDuration, firstDropDelay, dropPeriod, maxDropDuration, fasterDropDelay, fasterDropPeriodMult, startTime)

    def getDropPeriod(self):
        delay = self._dropPeriod
        if self.curT - self._startTime < self._normalDropDelay:
            delay *= self._slowerDropPeriodMult
        elif self.curT - self._startTime >= self.fasterDropDelay:
            delay *= self.fasterDropPeriodMult
        return delay