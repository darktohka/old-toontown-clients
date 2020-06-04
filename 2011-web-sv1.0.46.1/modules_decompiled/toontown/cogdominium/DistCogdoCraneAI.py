# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\DistCogdoCraneAI.py
from pandac.PandaModules import *
from direct.distributed import DistributedObjectAI
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from direct.fsm import FSM

class DistCogdoCraneAI(DistributedObjectAI.DistributedObjectAI, FSM.FSM):
    __module__ = __name__

    def __init__(self, air, craneGame, index):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        FSM.FSM.__init__(self, 'DistCogdoCraneAI')
        self.craneGame = craneGame
        self.index = index
        self.avId = 0
        self.objectId = 0

    def getCraneGameId(self):
        return self.craneGame.doId

    def getIndex(self):
        return self.index

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)
        self.request('Free')

    def d_setState(self, state, avId):
        self.sendUpdate('setState', [state, avId])

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterControlled(self, avId):
        self.avId = avId
        self.d_setState('C', avId)

    def exitControlled(self):
        if self.objectId:
            obj = self.air.doId2do[self.objectId]
            obj.request('Dropped', self.avId, self.doId)

    def enterFree(self):
        self.avId = 0
        self.d_setState('F', 0)

    def exitFree(self):
        pass