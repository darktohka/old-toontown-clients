# File: R (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from pandac import NodePath
import Ring
import RingTrack
import RingTrackGroup
import RingGameGlobals

class RingGroup(NodePath.NodePath):
    
    def __init__(self, trackGroup, ringModel, posScale, colorIndices):
        NodePath.NodePath.__init__(self)
        self.assign(hidden.attachNewNode(base.localAvatar.uniqueName('ring-group')))
        self._RingGroup__period = trackGroup.period
        self._RingGroup__reverseFlag = trackGroup.reverseFlag
        self._RingGroup__tOffset = trackGroup.tOffset
        self._RingGroup__numRings = len(trackGroup.tracks)
        self._RingGroup__rings = []
        self._RingGroup__ringModels = []
        for i in range(0, self._RingGroup__numRings):
            track = trackGroup.tracks[i]
            tOffset = trackGroup.trackTOffsets[i]
            ring = Ring.Ring(track, tOffset, posScale)
            ring.reparentTo(self)
            model = ringModel.copyTo(ring)
            model.setColor(RingGameGlobals.ringColors[colorIndices[i]][1])
            self._RingGroup__rings.append(ring)
            self._RingGroup__ringModels.append(model)
        

    
    def delete(self):
        for model in self._RingGroup__ringModels:
            model.removeNode()
        
        for ring in self._RingGroup__rings:
            ring.removeNode()
        
        del self._RingGroup__rings
        del self._RingGroup__ringModels

    
    def getRing(self, index):
        return self._RingGroup__ringModels[index]

    
    def setT(self, t):
        normT = (t / self._RingGroup__period + self._RingGroup__tOffset) % 1.0
        if self._RingGroup__reverseFlag:
            normT = 1.0 - normT
        
        for ring in self._RingGroup__rings:
            ring.setT(normT)
        


