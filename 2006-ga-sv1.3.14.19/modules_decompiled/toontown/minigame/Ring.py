# File: R (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from pandac import NodePath
import RingTrack

class Ring(NodePath.NodePath):
    
    def __init__(self, moveTrack, tOffset, posScale = 1.0):
        NodePath.NodePath.__init__(self)
        self.assign(hidden.attachNewNode(base.localAvatar.uniqueName('ring')))
        self.setMoveTrack(moveTrack)
        self.setTOffset(tOffset)
        self.setPosScale(posScale)
        self.setT(0.0)

    
    def setMoveTrack(self, moveTrack):
        self._Ring__moveTrack = moveTrack

    
    def setTOffset(self, tOffset):
        self._Ring__tOffset = float(tOffset)

    
    def setPosScale(self, posScale):
        self._Ring__posScale = posScale

    
    def setT(self, t):
        pos = self._Ring__moveTrack.eval((t + self._Ring__tOffset) % 1.0)
        self.setPos(pos[0] * self._Ring__posScale, 0, pos[1] * self._Ring__posScale)


