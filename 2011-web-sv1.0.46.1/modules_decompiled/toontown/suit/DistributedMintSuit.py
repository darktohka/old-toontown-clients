# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\suit\DistributedMintSuit.py
from toontown.suit import DistributedFactorySuit
from direct.directnotify import DirectNotifyGlobal

class DistributedMintSuit(DistributedFactorySuit.DistributedFactorySuit):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMintSuit')