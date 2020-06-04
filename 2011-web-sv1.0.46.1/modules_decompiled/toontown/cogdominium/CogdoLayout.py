# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\CogdoLayout.py
from direct.directnotify import DirectNotifyGlobal

class CogdoLayout:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('CogdoLayout')

    def __init__(self, numFloors):
        self._numFloors = numFloors

    def getNumGameFloors(self):
        return self._numFloors

    def hasBossBattle(self):
        return self._numFloors >= 1

    def getNumFloors(self):
        if self.hasBossBattle():
            return self._numFloors + 1
        else:
            return self._numFloors

    def getBossBattleFloor(self):
        if not self.hasBossBattle():
            self.notify.error('getBossBattleFloor(): cogdo has no boss battle')
        return self.getNumFloors() - 1