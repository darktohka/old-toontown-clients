# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\uberdog\ScavengerHuntDataStore.py
from direct.directnotify import DirectNotifyGlobal
from toontown.uberdog.DataStore import *

class ScavengerHuntDataStore(DataStore):
    __module__ = __name__
    QueryTypes = DataStore.addQueryTypes(['GetGoals', 'AddGoal'])
    notify = DirectNotifyGlobal.directNotify.newCategory('ScavengerHuntDataStore')

    def __init__(self, filepath):
        DataStore.__init__(self, filepath)

    def handleQuery(self, query):
        (qId, qData) = query
        if qId == self.QueryTypes['GetGoals']:
            (avId, goal) = qData
            goals = self.__getGoalsForAvatarId(avId)
            return (
             qId, (avId, goal, goals))
        elif qId == self.QueryTypes['AddGoal']:
            (avId, goal) = qData
            self.__addGoalToAvatarId(avId, goal)
            return (
             qId, (avId,))
        return

    def __addGoalToAvatarId(self, avId, goal):
        if self.wantAnyDbm:
            pAvId = cPickle.dumps(avId)
            pGoal = cPickle.dumps(goal)
            pData = self.data.get(pAvId, None)
            if pData is not None:
                data = cPickle.loads(pData)
            else:
                data = set()
            data.add(goal)
            pData = cPickle.dumps(data)
            self.data[pAvId] = pData
        else:
            self.data.setdefault(avId, set())
            self.data[avId].add(goal)
        self.incrementWriteCount()
        return

    def __getGoalsForAvatarId(self, avId):
        if self.wantAnyDbm:
            pAvId = cPickle.dumps(avId)
            pData = self.data.get(pAvId, None)
            if pData is not None:
                data = list(cPickle.loads(pData))
            else:
                data = []
            return data
        else:
            return list(self.data.get(avId, []))
        return