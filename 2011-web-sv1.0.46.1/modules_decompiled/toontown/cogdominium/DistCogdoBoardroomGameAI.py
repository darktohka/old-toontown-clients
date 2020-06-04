# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\DistCogdoBoardroomGameAI.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from toontown.cogdominium.CogdoBoardroomGameBase import CogdoBoardroomGameBase
from toontown.cogdominium.DistCogdoLevelGameAI import DistCogdoLevelGameAI
from toontown.cogdominium import CogdoBoardroomGameConsts as Consts

class DistCogdoBoardroomGameAI(CogdoBoardroomGameBase, DistCogdoLevelGameAI):
    __module__ = __name__
    notify = directNotify.newCategory('DistCogdoBoardroomGameAI')

    def __init__(self, air, interior):
        DistCogdoLevelGameAI.__init__(self, air, interior)

    def enterGame(self):
        DistCogdoLevelGameAI.enterGame(self)
        self._gameDoneEvent = taskMgr.doMethodLater(Consts.GameDuration.get(), self._gameDoneDL, self.uniqueName('boardroomGameDone'))

    def exitGame(self):
        taskMgr.remove(self._gameDoneEvent)
        self._gameDoneEvent = None
        return

    def _gameDoneDL(self, task):
        self._handleGameFinished()
        return task.done

    def enterFinish(self):
        DistCogdoLevelGameAI.enterFinish(self)
        self._finishDoneEvent = taskMgr.doMethodLater(Consts.FinishDuration.get(), self._finishDoneDL, self.uniqueName('boardroomFinishDone'))

    def exitFinish(self):
        taskMgr.remove(self._finishDoneEvent)
        self._finishDoneEvent = None
        return

    def _finishDoneDL(self, task):
        self.announceGameDone()
        return task.done