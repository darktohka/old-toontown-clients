# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\effects\Splash.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from Ripples import *
from toontown.battle.BattleProps import globalPropPool
from toontown.battle import BattleParticles

class Splash(NodePath):
    __module__ = __name__
    splashCount = 0

    def __init__(self, parent=hidden, wantParticles=1):
        NodePath.__init__(self, parent)
        self.assign(parent.attachNewNode('splash'))
        self.splashdown = globalPropPool.getProp('splashdown')
        self.splashdown.reparentTo(self)
        self.splashdown.setZ(-0.01)
        self.splashdown.setScale(0.4)
        ta = TransparencyAttrib.make(TransparencyAttrib.MBinary)
        self.splashdown.node().setAttrib(ta, 1)
        self.splashdown.setBin('fixed', 130, 1)
        self.ripples = Ripples(self)
        self.ripples.setBin('fixed', 120, 1)
        self.wantParticles = wantParticles
        if self.wantParticles:
            self.pSystem = BattleParticles.createParticleEffect('SplashLines')
            self.pSystem.setScale(0.4)
            self.pSystem.setBin('fixed', 150, 1)
            self.particles = self.pSystem.particlesDict.get('particles-1')
        self.track = None
        self.trackId = Splash.splashCount
        Splash.splashCount += 1
        self.setBin('fixed', 100, 1)
        self.hide()
        return

    def createTrack(self, rate=1):
        self.ripples.createTrack(rate)
        self.splashdown.setPlayRate(rate, 'splashdown')
        animDuration = self.splashdown.getDuration('splashdown') * 0.65
        rippleSequence = Sequence(Func(self.splashdown.show), Func(self.splashdown.play, 'splashdown'), Wait(animDuration), Func(self.splashdown.hide))
        if self.wantParticles:
            particleSequence = Sequence(Func(self.pSystem.show), Func(self.particles.induceLabor), Func(self.pSystem.start, self), Wait(2.2), Func(self.pSystem.hide), Func(self.pSystem.disable))
        else:
            particleSequence = Sequence()
        self.track = Sequence(Func(self.show), Parallel(self.ripples.track, rippleSequence, particleSequence), Func(self.hide), name='splashdown-%d-track' % self.trackId)

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
        del self.track
        self.ripples.destroy()
        del self.ripples
        if self.wantParticles:
            self.pSystem.cleanup()
            del self.pSystem
            del self.particles
        self.removeNode()