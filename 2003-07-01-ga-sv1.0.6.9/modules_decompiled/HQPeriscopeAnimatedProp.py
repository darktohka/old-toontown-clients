# File: H (Python 2.2)

import AnimatedProp
import Actor
from IntervalGlobal import *

class HQPeriscopeAnimatedProp(AnimatedProp.AnimatedProp):
    
    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        self.periscope = Actor.Actor()
        self.periscope.reparentTo(self.node.getParent())
        self.periscope.prepareBundle(self.node)
        self.periscope.loadAnims({
            'anim': 'phase_3.5/models/props/HQ_periscope-chan' })
        self.periscope.pose('anim', 0)
        self.node = self.periscope
        self.track = Sequence(Wait(2.0), self.periscope.actorInterval('anim', startTime = 0.0, endTime = 40 / 24.0), Wait(0.69999999999999996), self.periscope.actorInterval('anim', startTime = 40 / 24.0, endTime = 90 / 24.0), Wait(0.69999999999999996), self.periscope.actorInterval('anim', startTime = 91 / 24.0, endTime = 121 / 24.0), Wait(0.69999999999999996), self.periscope.actorInterval('anim', startTime = 121 / 24.0, endTime = 91 / 24.0), Wait(0.69999999999999996), self.periscope.actorInterval('anim', startTime = 90 / 24.0, endTime = 40 / 24.0), Wait(0.69999999999999996), self.periscope.actorInterval('anim', startTime = 40 / 24.0, endTime = 90 / 24.0), Wait(0.69999999999999996), self.periscope.actorInterval('anim', startTime = 91 / 24.0, endTime = 121 / 24.0), Wait(0.5), self.periscope.actorInterval('anim', startTime = 121 / 24.0, endTime = 148 / 24.0), Wait(3.0), name = self.uniqueName('HQPeriscope'))

    
    def enter(self):
        AnimatedProp.AnimatedProp.enter(self)
        self.track.loop()

    
    def exit(self):
        AnimatedProp.AnimatedProp.exit(self)
        self.track.stop()


