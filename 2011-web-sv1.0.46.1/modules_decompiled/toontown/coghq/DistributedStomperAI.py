# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedStomperAI.py
from otp.ai.AIBase import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
import DistributedCrusherEntityAI, StomperGlobals
from direct.distributed import ClockDelta

class DistributedStomperAI(DistributedCrusherEntityAI.DistributedCrusherEntityAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStomperAI')

    def __init__(self, level, entId, pairId=-1):
        DistributedCrusherEntityAI.DistributedCrusherEntityAI.__init__(self, level, entId)
        self.pairId = pairId

    def generate(self):
        DistributedCrusherEntityAI.DistributedCrusherEntityAI.generate(self)
        if self.switchId != 0:
            self.accept(self.getOutputEventName(self.switchId), self.reactToSwitch)
        self.d_startStomper()

    def delete(self):
        del self.pos
        self.ignoreAll()
        DistributedCrusherEntityAI.DistributedCrusherEntityAI.delete(self)

    def d_startStomper(self):
        self.sendUpdate('setMovie', [StomperGlobals.STOMPER_START, ClockDelta.globalClockDelta.getRealNetworkTime(), []])

    def reactToSwitch(self, on):
        if on:
            crushedList = []
            if self.crushCell:
                self.crushCell.updateCrushables()
                for id in self.crushCell.occupantIds:
                    if id in self.crushCell.crushables:
                        crushedList.append(id)

                self.sendCrushMsg()
            self.sendUpdate('setMovie', [StomperGlobals.STOMPER_STOMP, ClockDelta.globalClockDelta.getRealNetworkTime(), crushedList])
        else:
            self.sendUpdate('setMovie', [StomperGlobals.STOMPER_RISE, ClockDelta.globalClockDelta.getRealNetworkTime(), []])