# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\CogdoCraneGameBase.py
from toontown.cogdominium import CogdoCraneGameSpec
from toontown.cogdominium import CogdoCraneGameConsts as Consts

class CogdoCraneGameBase:
    __module__ = __name__

    def getConsts(self):
        return Consts

    def getSpec(self):
        return CogdoCraneGameSpec