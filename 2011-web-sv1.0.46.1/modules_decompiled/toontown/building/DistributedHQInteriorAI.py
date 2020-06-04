# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedHQInteriorAI.py
from direct.distributed import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
import cPickle

class DistributedHQInteriorAI(DistributedObjectAI.DistributedObjectAI):
    __module__ = __name__

    def __init__(self, block, air, zoneId):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.block = block
        self.zoneId = zoneId
        self.tutorial = 0
        self.isDirty = False
        self.accept('leaderboardChanged', self.leaderboardChanged)
        self.accept('leaderboardFlush', self.leaderboardFlush)

    def delete(self):
        self.ignore('leaderboardChanged')
        self.ignore('leaderboardFlush')
        self.ignore('setLeaderBoard')
        self.ignore('AIStarted')
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def getZoneIdAndBlock(self):
        r = [
         self.zoneId, self.block]
        return r

    def leaderboardChanged(self):
        self.isDirty = True

    def leaderboardFlush(self):
        if self.isDirty:
            self.sendNewLeaderBoard()

    def sendNewLeaderBoard(self):
        if self.air:
            self.isDirty = False
            self.sendUpdate('setLeaderBoard', [cPickle.dumps(self.air.trophyMgr.getLeaderInfo(), 1)])

    def getLeaderBoard(self):
        return cPickle.dumps(self.air.trophyMgr.getLeaderInfo(), 1)

    def getTutorial(self):
        return self.tutorial

    def setTutorial(self, flag):
        if self.tutorial != flag:
            self.tutorial = flag
            self.sendUpdate('setTutorial', [self.tutorial])