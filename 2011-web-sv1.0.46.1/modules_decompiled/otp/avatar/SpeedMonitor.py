# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\avatar\SpeedMonitor.py
from direct.showbase.PythonUtil import SerialNumGen
from direct.task import Task

class SpeedMonitor:
    __module__ = __name__
    notify = directNotify.newCategory('SpeedMonitor')
    SerialGen = SerialNumGen()
    TrackingPeriod = 30.0

    def __init__(self, name):
        self._name = name
        self._nodepaths = {}
        self._maxSpeeds = {}
        self._prevPosQueue = {}
        self._speedLimits = {}
        self._trackTask = taskMgr.add(self._trackSpeedsTask, 'speedMonitorTask-%s-%s' % (self._name, id(self)))

    def destroy(self):
        taskMgr.remove(self._trackTask)

    def _allocToken(self):
        return 'speedMonitorToken-%s-%s-%s' % (self._name, id(self), SpeedMonitor.SerialGen.next())

    def addNodepath(self, nodepath):
        token = self._allocToken()
        self._nodepaths[token] = nodepath
        self.resetMaxSpeed(token)
        return token

    def setSpeedLimit(self, token, limit, callback):
        self._speedLimits[token] = (
         limit, callback)

    def removeNodepath(self, token):
        del self._nodepaths[token]
        del self._maxSpeeds[token]
        del self._prevPosQueue[token]
        if token in self._speedLimits:
            self._speedLimits.pop(token)

    def getMaxSpeed(self, token):
        return self._maxSpeeds[token]

    def resetMaxSpeed(self, token):
        self._maxSpeeds[token] = 0.0
        nodepath = self._nodepaths[token]
        self._prevPosQueue[token] = [(nodepath.getPos(), globalClock.getFrameTime() - SpeedMonitor.TrackingPeriod, 0.0)]

    def _trackSpeedsTask(self, task=None):
        for (token, nodepath) in self._nodepaths.iteritems():
            curT = globalClock.getFrameTime()
            curPos = nodepath.getPos()
            while len(self._prevPosQueue[token]) > 1:
                (oldestPos, oldestT, oldestDistance) = self._prevPosQueue[token][1]
                if curT - oldestT > SpeedMonitor.TrackingPeriod:
                    self._prevPosQueue[token] = self._prevPosQueue[token][1:]
                else:
                    break

            storeCurPos = False
            if len(self._prevPosQueue[token]) == 0:
                storeCurPos = True
                curDistance = 0.0
            else:
                (prevPos, prevT, prevDistance) = self._prevPosQueue[token][(-1)]
                if curPos != prevPos:
                    storeCurPos = True
                    curDistance = (curPos - prevPos).length()
            if storeCurPos:
                self._prevPosQueue[token].append((curPos, curT, curDistance))
            if len(self._prevPosQueue[token]) > 1:
                (oldestPos, oldestT, oldestDistance) = self._prevPosQueue[token][0]
                (newestPos, newestT, newestDistance) = self._prevPosQueue[token][(-1)]
                tDelta = newestT - oldestT
                if tDelta >= SpeedMonitor.TrackingPeriod:
                    totalDistance = 0.0
                    for (pos, t, distance) in self._prevPosQueue[token][1:]:
                        totalDistance += distance

                    speed = totalDistance / tDelta
                    if speed > self._maxSpeeds[token]:
                        if self.notify.getDebug():
                            self.notify.debug('new max speed(%s): %s' % (nodepath, speed))
                        self._maxSpeeds[token] = speed
                        (limit, callback) = self._speedLimits[token]
                        if speed > limit:
                            self.notify.warning('%s over speed limit (%s, cur speed=%s)' % (nodepath, limit, speed))
                            callback(speed)

        return Task.cont