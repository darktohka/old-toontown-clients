# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\racing\PiejectileManager.py
from pandac.PandaModules import *
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import *
from toontown.racing import Piejectile

class PiejectileManager(DirectObject):
    __module__ = __name__
    pieCounter = 0

    def __init__(self):
        self.piejectileList = []

    def delete(self):
        for piejectile in self.piejectileList:
            self.__removePiejectile(piejectile)

    def addPiejectile(self, sourceId, targetId=0, type=0):
        name = 'PiejectileManager Pie %s' % PiejectileManager.pieCounter
        pie = Piejectile.Piejectile(sourceId, targetId, type, name)
        self.piejectileList.append(pie)
        PiejectileManager.pieCounter += 1

    def __removePiejectile(self, piejectile):
        self.piejectileList.remove(piejectile)
        piejectile.delete()
        piejectile = None
        return