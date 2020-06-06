# File: F (Python 2.2)

import AnimatedProp
import Actor
from IntervalGlobal import *
from Splash import *
from Ripples import *
import random

class FishAnimatedProp(AnimatedProp.AnimatedProp):
    
    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        self.fish = Actor.Actor()
        self.fish.reparentTo(self.node.getParent())
        self.fish.setTransform(self.node.getTransform())
        self.node.clearMat()
        self.fish.prepareBundle(self.node)
        self.fish.loadAnims({
            'jump': 'phase_4/models/props/SZ_fish-jump',
            'swim': 'phase_4/models/props/SZ_fish-swim' })
        self.splashSfxList = (loader.loadSfx('phase_4/audio/sfx/TT_splash1.mp3'), loader.loadSfx('phase_4/audio/sfx/TT_splash2.mp3'))
        self.node = self.fish
        self.geom = self.fish.getGeomNode()
        self.exitRipples = Ripples(self.geom)
        self.exitRipples.setBin('fixed', 25, 1)
        self.exitRipples.setPosHprScale(-0.29999999999999999, 0.0, 1.24, 0.0, 0.0, 0.0, 0.69999999999999996, 0.69999999999999996, 0.69999999999999996)
        self.splash = Splash(self.geom)
        self.splash.setPosHprScale(-1, 0.0, 1.23, 0.0, 0.0, 0.0, 0.69999999999999996, 0.69999999999999996, 0.69999999999999996)
        randomSplash = random.choice(self.splashSfxList)
        self.track = Sequence(FunctionInterval(self.randomizePosition), Parallel(self.fish.actorInterval('jump'), Sequence(Wait(0.25), Func(self.exitRipples.play, 0.75)), Sequence(Wait(1.1399999999999999), Func(self.splash.play), SoundInterval(randomSplash, volume = 0.80000000000000004, node = self.node))), Wait(5 + 10 * random.random()), name = self.uniqueName('Fish'))

    
    def delete(self):
        self.exitRipples.destroy()
        del self.exitRipples
        self.splash.destroy()
        del self.splash
        del self.track
        self.fish.removeNode()
        del self.fish
        del self.node
        del self.geom

    
    def randomizePosition(self):
        x = 5 * (random.random() - 0.5)
        y = 5 * (random.random() - 0.5)
        h = 360 * random.random()
        self.geom.setPos(x, y, 0)
        self.geom.setHpr(h, 0, 0)

    
    def enter(self):
        AnimatedProp.AnimatedProp.enter(self)
        self.track.loop()

    
    def exit(self):
        AnimatedProp.AnimatedProp.exit(self)
        self.track.stop()
        self.splash.stop()
        self.exitRipples.stop()


