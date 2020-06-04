# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\pets\PetLeash.py
from pandac.PandaModules import *
from otp.movement import Impulse

class PetLeash(Impulse.Impulse):
    __module__ = __name__

    def __init__(self, origin, length):
        Impulse.Impulse.__init__(self)
        self.origin = origin
        self.length = length

    def _process(self, dt):
        Impulse.Impulse._process(self, dt)
        myPos = self.nodePath.getPos()
        myDist = self.VecType(myPos - self.origin.getPos()).length()
        if myDist > self.length:
            excess = myDist - self.length
            shove = self.VecType(myPos)
            shove.normalize()
            shove *= -excess
            self.mover.addShove(shove)