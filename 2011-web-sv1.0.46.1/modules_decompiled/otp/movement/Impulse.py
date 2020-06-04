# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\movement\Impulse.py
from pandac.PandaModules import *
from direct.showbase import DirectObject

class Impulse(DirectObject.DirectObject):
    __module__ = __name__

    def __init__(self):
        self.mover = None
        self.nodePath = None
        return

    def destroy(self):
        pass

    def _process(self, dt):
        pass

    def _setMover(self, mover):
        self.mover = mover
        self.nodePath = self.mover.getNodePath()
        self.VecType = self.mover.VecType

    def _clearMover(self, mover):
        if self.mover == mover:
            self.mover = None
            self.nodePath = None
        return

    def isCpp(self):
        return 0