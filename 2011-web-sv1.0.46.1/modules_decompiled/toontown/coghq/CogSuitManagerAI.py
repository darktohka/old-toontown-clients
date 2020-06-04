# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\CogSuitManagerAI.py
from otp.ai.AIBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
import random
from toontown.suit import SuitDNA
import CogDisguiseGlobals

class CogSuitManagerAI:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('CogSuitManagerAI')

    def __init__(self, air):
        self.air = air

    def recoverPart(self, av, factoryType, suitTrack, zoneId, avList):
        partsRecovered = [
         0, 0, 0, 0]
        part = av.giveGenericCogPart(factoryType, suitTrack)
        if part:
            partsRecovered[CogDisguiseGlobals.dept2deptIndex(suitTrack)] = part
            self.air.questManager.toonRecoveredCogSuitPart(av, zoneId, avList)
        return partsRecovered