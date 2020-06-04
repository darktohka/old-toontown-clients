# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\effects\Ripples.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import globalPropPool

class Ripples(NodePath):
    __module__ = __name__
    rippleCount = 0

    def __init__(self, parent=hidden):
        NodePath.__init__(self)
        self.assign(globalPropPool.getProp('ripples'))
        self.reparentTo(parent)
        self.getChild(0).setZ(0.1)
        self.seqNode = self.find('**/+SequenceNode').node()
        self.seqNode.setPlayRate(0)
        self.track = None
        self.trackId = Ripples.rippleCount
        Ripples.rippleCount += 1
        self.setBin('fixed', 100, 1)
        self.hide()
        return

    def createTrack(self, rate=1):
        tflipDuration = self.seqNode.getNumChildren() / (float(rate) * 24)
        self.track = Sequence(Func(self.show), Func(self.seqNode.play, 0, self.seqNode.getNumFrames() - 1), Func(self.seqNode.setPlayRate, rate), Wait(tflipDuration), Func(self.seqNode.setPlayRate, 0), Func(self.hide), name='ripples-track-%d' % self.trackId)

    def play(self, rate=1):
        self.stop()
        self.createTrack(rate)
        self.track.start()

    def loop(self, rate=1):
        self.stop()
        self.createTrack(rate)
        self.track.loop()

    def stop(self):
        if self.track:
            self.track.finish()

    def destroy(self):
        self.stop()
        self.track = None
        del self.seqNode
        self.removeNode()
        return