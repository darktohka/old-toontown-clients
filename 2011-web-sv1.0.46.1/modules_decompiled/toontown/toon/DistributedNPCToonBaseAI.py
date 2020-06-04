# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\toon\DistributedNPCToonBaseAI.py
from otp.ai.AIBaseGlobal import *
from pandac.PandaModules import *
import DistributedToonAI
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.distributed import ClockDelta
from toontown.toonbase import ToontownGlobals
import NPCToons
from direct.task import Task
from toontown.quest import Quests

class DistributedNPCToonBaseAI(DistributedToonAI.DistributedToonAI):
    __module__ = __name__

    def __init__(self, air, npcId, questCallback=None):
        DistributedToonAI.DistributedToonAI.__init__(self, air)
        self.air = air
        self.npcId = npcId
        self.busy = 0
        self.questCallback = questCallback
        self.givesQuests = 1

    def delete(self):
        taskMgr.remove(self.uniqueName('clearMovie'))
        DistributedToonAI.DistributedToonAI.delete(self)

    def _doPlayerEnter(self):
        pass

    def _doPlayerExit(self):
        pass

    def _announceArrival(self):
        pass

    def isPlayerControlled(self):
        return False

    def getHq(self):
        return 0

    def getTailor(self):
        return 0

    def getGivesQuests(self):
        return self.givesQuests

    def avatarEnter(self):
        pass

    def isBusy(self):
        return self.busy > 0

    def getNpcId(self):
        return self.npcId

    def freeAvatar(self, avId):
        self.sendUpdateToAvatarId(avId, 'freeAvatar', [])

    def setPositionIndex(self, posIndex):
        self.posIndex = posIndex

    def getPositionIndex(self):
        return self.posIndex