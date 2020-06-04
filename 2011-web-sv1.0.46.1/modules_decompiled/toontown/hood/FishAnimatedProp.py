# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\hood\FishAnimatedProp.py
import AnimatedProp
from direct.actor import Actor
from direct.interval.IntervalGlobal import *
from toontown.effects.Splash import *
from toontown.effects.Ripples import *
import random

class FishAnimatedProp(AnimatedProp.AnimatedProp):
    __module__ = __name__

    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        parent = node.getParent()
        self.fish = Actor.Actor(node, copy=0)
        self.fish.reparentTo(parent)
        self.fish.setTransform(node.getTransform())
        node.clearMat()
        self.fish.loadAnims({'jump': 'phase_4/models/props/SZ_fish-jump', 'swim': 'phase_4/models/props/SZ_fish-swim'})
        self.splashSfxList = (
         loader.loadSfx('phase_4/audio/sfx/TT_splash1.mp3'), loader.loadSfx('phase_4/audio/sfx/TT_splash2.mp3'))
        self.node = self.fish
        self.geom = self.fish.getGeomNode()
        self.exitRipples = Ripples(self.geom)
        self.exitRipples.setBin('fixed', 25, 1)
        self.exitRipples.setPosHprScale(-0.3, 0.0, 1.24, 0.0, 0.0, 0.0, 0.7, 0.7, 0.7)
        self.splash = Splash(self.geom, wantParticles=0)
        self.splash.setPosHprScale(-1, 0.0, 1.23, 0.0, 0.0, 0.0, 0.7, 0.7, 0.7)
        randomSplash = random.choice(self.splashSfxList)
        self.track = Sequence(FunctionInterval(self.randomizePosition), Func(self.node.unstash), Parallel(self.fish.actorInterval('jump'), Sequence(Wait(0.25), Func(self.exitRipples.play, 0.75)), Sequence(Wait(1.14), Func(self.splash.play), SoundInterval(randomSplash, volume=0.8, node=self.node))), Wait(1), Func(self.node.stash), Wait(4 + 10 * random.random()), name=self.uniqueName('Fish'))

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
        self.track.finish()
        self.splash.stop()
        self.exitRipples.stop()