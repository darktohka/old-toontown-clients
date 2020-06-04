# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\DistCogdoCraneMoneyBagAI.py
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from toontown.cogdominium.DistCogdoCraneObjectAI import DistCogdoCraneObjectAI
from toontown.cogdominium import CogdoCraneGameConsts as GameConsts

class DistCogdoCraneMoneyBagAI(DistCogdoCraneObjectAI):
    __module__ = __name__
    wantsWatchDrift = 0

    def __init__(self, air, boss, index):
        DistCogdoCraneObjectAI.__init__(self, air, boss)
        self.index = index
        self.avoidHelmet = 0
        cn = CollisionNode('sphere')
        cs = CollisionSphere(0, 0, 0, 6)
        cn.addSolid(cs)
        self.attachNewNode(cn)

    def resetToInitialPosition(self):
        posHpr = GameConsts.MoneyBagPosHprs[self.index]
        self.setPosHpr(*posHpr)

    def getIndex(self):
        return self.index

    def hitBoss(self, impact):
        avId = self.air.getAvatarIdFromSender()
        self.validate(avId, impact <= 1.0, 'invalid hitBoss impact %s' % impact)
        if avId not in self.boss.involvedToons:
            return
        if self.state != 'Dropped' and self.state != 'Grabbed':
            return
        if self.avoidHelmet or self == self.boss.heldObject:
            return
        if self.boss.heldObject == None:
            if self.boss.attackCode == ToontownGlobals.BossCogDizzy:
                damage = int(impact * 50)
                self.boss.recordHit(max(damage, 2))
            elif self.boss.acceptHelmetFrom(avId):
                self.demand('Grabbed', self.boss.doId, self.boss.doId)
                self.boss.heldObject = self
        elif impact >= ToontownGlobals.CashbotBossSafeKnockImpact:
            self.boss.heldObject.demand('Dropped', avId, self.boss.doId)
            self.boss.heldObject.avoidHelmet = 1
            self.boss.heldObject = None
            self.avoidHelmet = 1
            self.boss.waitForNextHelmet()
        return

    def requestInitial(self):
        avId = self.air.getAvatarIdFromSender()
        if avId == self.avId:
            self.demand('Initial')

    def enterGrabbed(self, avId, craneId):
        DistCogdoCraneObjectAI.enterGrabbed(self, avId, craneId)
        self.avoidHelmet = 0

    def enterInitial(self):
        self.avoidHelmet = 0
        self.resetToInitialPosition()
        if self.index == 0:
            self.stash()
        self.d_setObjectState('I', 0, 0)

    def exitInitial(self):
        if self.index == 0:
            self.unstash()

    def enterFree(self):
        DistCogdoCraneObjectAI.enterFree(self)
        self.avoidHelmet = 0