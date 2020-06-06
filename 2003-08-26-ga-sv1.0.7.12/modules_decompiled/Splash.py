# File: S (Python 2.2)

from PandaModules import *
from IntervalGlobal import *
from Ripples import *
from BattleProps import globalPropPool
import BattleParticles

class Splash(NodePath):
    splashCount = 0
    
    def __init__(self, parent = hidden):
        NodePath.__init__(self, parent)
        self.assign(parent.attachNewNode('splash'))
        self.splashdown = globalPropPool.getProp('splashdown')
        self.splashdown.reparentTo(self)
        self.splashdown.setZ(-0.01)
        self.splashdown.setScale(0.40000000000000002)
        ta = TransparencyAttrib.make(TransparencyAttrib.MBinary)
        self.splashdown.node().setAttrib(ta, 1)
        self.splashdown.setBin('fixed', 130, 1)
        self.ripples = Ripples(self)
        self.ripples.setBin('fixed', 120, 1)
        self.pSystem = BattleParticles.createParticleEffect('SplashLines')
        self.pSystem.setScale(0.40000000000000002)
        self.pSystem.setBin('fixed', 150, 1)
        self.particles = self.pSystem.particlesDict.get('particles-1')
        self.track = None
        self.trackId = Splash.splashCount
        Splash.splashCount += 1
        self.setBin('fixed', 100, 1)
        self.hide()

    
    def createTrack(self, rate = 1):
        self.ripples.createTrack(rate)
        self.splashdown.setPlayRate(rate, 'splashdown')
        animDuration = self.splashdown.getDuration('splashdown') * 0.65000000000000002
        self.track = Sequence(Func(self.show), Parallel(self.ripples.track, Sequence(Func(self.splashdown.show), Func(self.splashdown.play, 'splashdown'), Wait(animDuration), Func(self.splashdown.hide)), Sequence(Func(self.pSystem.show), Func(self.particles.induceLabor), Func(self.pSystem.start, self), Wait(2.2000000000000002), Func(self.pSystem.hide), Func(self.pSystem.disable))), Func(self.hide), name = 'splashdown-%d-track' % self.trackId)

    
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
        self.ripples.destroy()
        del self.ripples
        self.pSystem.cleanup()
        del self.pSystem
        del self.particles
        self.removeNode()


