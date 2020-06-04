# File: R (Python 2.2)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import globalPropPool

class Ripples(NodePath):
    rippleCount = 0
    
    def __init__(self, parent = hidden):
        NodePath.__init__(self)
        self.assign(globalPropPool.getProp('ripples'))
        self.reparentTo(parent)
        self.getChild(0).setZ(0.10000000000000001)
        self.seqNode = self.find('**/+SequenceNode').node()
        self.seqNode.setCycleRate(0)
        self.track = None
        self.trackId = Ripples.rippleCount
        Ripples.rippleCount += 1
        self.setBin('fixed', 100, 1)
        self.hide()

    
    def createTrack(self, rate = 1):
        tflipDuration = self.seqNode.getNumChildren() / float(rate) * 24
        self.track = Sequence(Func(self.show), Func(self.seqNode.setVisibleChild, 0), Func(self.seqNode.setCycleRate, rate * 24), Wait(tflipDuration), Func(self.seqNode.setCycleRate, 0), Func(self.hide), name = 'ripples-track-%d' % self.trackId)

    
    def play(self, rate = 1):
        self.stop()
        self.createTrack(rate)
        self.track.start()

    
    def loop(self, rate = 1):
        self.stop()
        self.createTrack(rate)
        self.track.loop()

    
    def stop(self):
        if self.track:
            self.track.finish()
        

    
    def destroy(self):
        self.stop()
        del self.track
        del self.seqNode
        self.removeNode()


