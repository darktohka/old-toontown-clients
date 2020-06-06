# File: D (Python 2.2)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import globalPropPool

class DustCloud(NodePath):
    dustCloudCount = 0
    
    def __init__(self, parent = hidden, fBillboard = 1):
        NodePath.__init__(self)
        self.assign(globalPropPool.getProp('suit_explosion_dust'))
        if fBillboard:
            self.setBillboardAxis()
        
        self.reparentTo(parent)
        self.seqNode = self.find('**/+SequenceNode').node()
        self.seqNode.setCycleRate(0)
        self.track = None
        self.trackId = DustCloud.dustCloudCount
        DustCloud.dustCloudCount += 1
        self.setBin('fixed', 100, 1)
        self.hide()

    
    def createTrack(self, rate = 1):
        tflipDuration = self.seqNode.getNumChildren() / float(rate) * 24
        self.track = Sequence(Func(self.show), Func(self.seqNode.setVisibleChild, 0), Func(self.seqNode.setCycleRate, rate * 24), Wait(tflipDuration), Func(self.seqNode.setCycleRate, 0), Func(self.hide), name = 'dustCloud-track-%d' % self.trackId)

    
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


