# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedLawbotBossGavelAI.py
from direct.directnotify import DirectNotifyGlobal
from pandac.PandaModules import *
from direct.distributed import DistributedObjectAI
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from direct.fsm import FSM

class DistributedLawbotBossGavelAI(DistributedObjectAI.DistributedObjectAI, FSM.FSM):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLawbotBossGavelAI')

    def __init__(self, air, boss, index):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        FSM.FSM.__init__(self, 'DistributedLawbotBossGavelAI')
        self.boss = boss
        self.index = index
        cn = CollisionNode('controls')
        cs = CollisionSphere(0, -6, 0, 6)
        cn.addSolid(cs)
        self.goonShield = NodePath(cn)
        self.goonShield.setPosHpr(*ToontownGlobals.LawbotBossGavelPosHprs[self.index])
        self.avId = 0
        self.objectId = 0

    def getBossCogId(self):
        return self.boss.doId

    def getIndex(self):
        return self.index

    def setState(self, state):
        self.request(state)

    def d_setState(self, state):
        newState = state
        if state == 'On':
            newState = 'N'
        elif state == 'Off':
            newState = 'F'
        self.sendUpdate('setState', [newState])

    def b_setState(self, state):
        self.request(state)
        self.d_setState(state)

    def turnOn(self):
        self.b_setState('On')

    def requestControl(self):
        avId = self.air.getAvatarIdFromSender()
        if avId in self.boss.involvedToons and self.avId == 0:
            craneId = self.__getCraneId(avId)
            if craneId == 0:
                self.request('Controlled', avId)

    def requestFree(self):
        avId = self.air.getAvatarIdFromSender()
        if avId == self.avId:
            self.request('Free')

    def removeToon(self, avId):
        if avId == self.avId:
            self.request('Free')

    def __getCraneId(self, avId):
        if self.boss and self.boss.cranes != None:
            for crane in self.boss.cranes:
                if crane.avId == avId:
                    return crane.doId

        return 0

    def enterOn(self):
        pass

    def exitOn(slef):
        pass

    def enterOff(self):
        self.goonShield.detachNode()

    def exitOff(self):
        pass

    def enterControlled(self, avId):
        self.avId = avId
        self.d_setState('C')

    def exitControlled(self):
        if self.objectId:
            obj = self.air.doId2do[self.objectId]
            obj.request('Dropped', self.avId, self.doId)

    def enterFree(self):
        self.avId = 0
        self.d_setState('F')

    def exitFree(self):
        pass