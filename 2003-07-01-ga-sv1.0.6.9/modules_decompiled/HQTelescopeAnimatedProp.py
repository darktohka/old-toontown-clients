# File: H (Python 2.2)

import AnimatedProp
import Actor
from IntervalGlobal import *

class HQTelescopeAnimatedProp(AnimatedProp.AnimatedProp):
    
    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        self.telescope = Actor.Actor()
        self.telescope.reparentTo(self.node.getParent())
        self.telescope.prepareBundle(self.node)
        self.telescope.loadAnims({
            'anim': 'phase_3.5/models/props/HQ_telescope-chan' })
        self.telescope.pose('anim', 0)
        self.node = self.telescope
        self.track = Sequence(Wait(5.0), self.telescope.actorInterval('anim', startTime = 0.0, endTime = 32 / 24.0), Wait(0.5), self.telescope.actorInterval('anim', startTime = 32 / 24.0, endTime = 78 / 24.0), Wait(0.5), self.telescope.actorInterval('anim', startTime = 79 / 24.0, endTime = 112 / 24.0), Wait(0.5), self.telescope.actorInterval('anim', startTime = 112 / 24.0, endTime = 79 / 24.0), Wait(0.5), self.telescope.actorInterval('anim', startTime = 78 / 24.0, endTime = 32 / 24.0), Wait(0.5), self.telescope.actorInterval('anim', startTime = 32 / 24.0, endTime = 78 / 24.0), Wait(0.5), self.telescope.actorInterval('anim', startTime = 79 / 24.0, endTime = 112 / 24.0), Wait(0.5), self.telescope.actorInterval('anim', startTime = 112 / 24.0, endTime = 148 / 24.0), Wait(4.0), name = self.uniqueName('HQTelescope'))

    
    def enter(self):
        AnimatedProp.AnimatedProp.enter(self)
        self.track.loop()

    
    def exit(self):
        AnimatedProp.AnimatedProp.exit(self)
        self.track.stop()


