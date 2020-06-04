# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedMazeAI.py
from otp.level import DistributedEntityAI
import DistributedBarrelBaseAI
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta
from direct.task import Task

class DistributedMazeAI(DistributedEntityAI.DistributedEntityAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMazeAI')

    def __init__(self, level, entId):
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)
        self.roomDoId = level.doId
        self.GameDuration = 60.0
        self.DamageOnFailure = 20
        self.finishedList = []

    def delete(self):
        self.removeAllTasks()
        DistributedEntityAI.DistributedEntityAI.delete(self)

    def announceGenerate(self):
        DistributedEntityAI.DistributedEntityAI.announceGenerate(self)
        self.mazeEndTimeTaskName = self.uniqueName('mazeEndTime')

    def getRoomDoId(self):
        return self.roomDoId

    def setClientTriggered(self):
        if not hasattr(self, 'gameStartTime'):
            self.gameStartTime = globalClock.getRealTime()
            self.b_setGameStart(globalClockDelta.localToNetworkTime(self.gameStartTime))

    def b_setGameStart(self, timestamp):
        self.d_setGameStart(timestamp)
        self.setGameStart(timestamp)

    def d_setGameStart(self, timestamp):
        self.notify.debug('BASE: Sending setGameStart')
        self.sendUpdate('setGameStart', [timestamp])

    def setGameStart(self, timestamp):
        self.notify.debug('BASE: setGameStart')
        self.GameDuration = 35.0 + self.numSections * 15.0
        self.prepareForGameStartOrRestart()

    def prepareForGameStartOrRestart(self):
        self.doMethodLater(self.GameDuration, self.gameEndingTimeHit, self.mazeEndTimeTaskName)

    def setFinishedMaze(self):
        senderId = self.air.getAvatarIdFromSender()
        if senderId not in self.finishedList:
            toon = simbase.air.doId2do.get(senderId)
            if toon:
                if len(self.finishedList) < 1:
                    toon.toonUp(200.0)
                else:
                    toon.toonUp(20.0)
                lastToon = 0
                if hasattr(self, 'level'):
                    numToons = len(self.level.presentAvIds)
                    if numToons == len(self.finishedList) + 1:
                        lastToon = 1
                self.sendUpdate('toonFinished', [senderId, len(self.finishedList), lastToon])
            self.finishedList.append(senderId)

    def gameEndingTimeHit(self, task):
        roomId = self.getLevelDoId()
        room = simbase.air.doId2do.get(roomId)
        if room:
            playerIds = room.presentAvIds
            for avId in playerIds:
                av = simbase.air.doId2do.get(avId)
                if av and avId not in self.finishedList:
                    self.finishedList.append(avId)

        self.sendUpdate('setGameOver', [])

    def damageMe(self):
        senderId = self.air.getAvatarIdFromSender()
        av = simbase.air.doId2do.get(senderId)
        roomId = self.getLevelDoId()
        room = simbase.air.doId2do.get(roomId)
        if room:
            playerIds = room.presentAvIds
            if av and senderId in playerIds:
                av.takeDamage(self.DamageOnFailure, quietly=0)
                room.sendUpdate('forceOuch', [self.DamageOnFailure])