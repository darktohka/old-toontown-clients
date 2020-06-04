# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedFoodBeltAI.py
from direct.distributed import DistributedObjectAI
from direct.fsm import FSM
from direct.directnotify import DirectNotifyGlobal
from toontown.coghq import FoodBeltBase

class DistributedFoodBeltAI(DistributedObjectAI.DistributedObjectAI, FSM.FSM, FoodBeltBase.FoodBeltBase):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFoodBeltAI')

    def __init__(self, air, boss, index):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        FSM.FSM.__init__(self, 'DistributedFoodBeltAI')
        self.boss = boss
        self.index = index

    def delete(self):
        DistributedObjectAI.DistributedObjectAI.delete(self)

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
        elif state == 'Inactive':
            newState = 'I'
        elif state == 'Toonup':
            newState = 'T'
        self.sendUpdate('setState', [newState])

    def b_setState(self, state):
        self.request(state)
        self.d_setState(state)

    def turnOn(self):
        self.b_setState('On')

    def goInactive(self):
        self.b_setState('Inactive')

    def goToonup(self):
        self.b_setState('Toonup')

    def enterOn(self):
        pass

    def exitOn(slef):
        pass

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterInactive(self):
        pass

    def exitInactive(slef):
        pass