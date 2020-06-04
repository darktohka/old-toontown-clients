# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\Ring.py
from pandac.PandaModules import *
from toontown.toonbase.ToonBaseGlobal import *
from pandac.PandaModules import NodePath
import RingTrack

class Ring(NodePath):
    __module__ = __name__

    def __init__(self, moveTrack, tOffset, posScale=1.0):
        NodePath.__init__(self)
        self.assign(hidden.attachNewNode(base.localAvatar.uniqueName('ring')))
        self.setMoveTrack(moveTrack)
        self.setTOffset(tOffset)
        self.setPosScale(posScale)
        self.setT(0.0)

    def setMoveTrack(self, moveTrack):
        self.__moveTrack = moveTrack

    def setTOffset(self, tOffset):
        self.__tOffset = float(tOffset)

    def setPosScale(self, posScale):
        self.__posScale = posScale

    def setT(self, t):
        pos = self.__moveTrack.eval((t + self.__tOffset) % 1.0)
        self.setPos(pos[0] * self.__posScale, 0, pos[1] * self.__posScale)