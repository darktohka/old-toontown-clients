# File: B (Python 2.2)

from PandaModules import *
from IntervalGlobal import *
import ParticleEffect
import Particles
import ForceGroup
import random

class Bubbles(NodePath):
    
    def __init__(self, parent, renderParent):
        NodePath.__init__(self)
        self.renderParent = renderParent.attachNewNode('bubbleRenderParent')
        self.renderParent.setBin('fixed', 0)
        self.assign(parent.attachNewNode('bubbles'))
        texture = loader.loadModelOnce('phase_4/models/char/bubble')
        self.effect = ParticleEffect.ParticleEffect()
        p0 = Particles.Particles('particles-1')
        p0.setFactory('PointParticleFactory')
        p0.setRenderer('SpriteParticleRenderer')
        p0.setEmitter('DiscEmitter')
        p0.setPoolSize(8)
        p0.setBirthRate(0.75)
        p0.setLitterSize(2)
        p0.setLitterSpread(1)
        p0.factory.setLifespanBase(2.0)
        p0.factory.setLifespanSpread(0.5)
        p0.factory.setTerminalVelocityBase(400.0)
        p0.factory.setTerminalVelocitySpread(40.0)
        p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
        p0.renderer.setUserAlpha(1.0)
        p0.renderer.setFromNode(texture)
        p0.renderer.setXScaleFlag(1)
        p0.renderer.setYScaleFlag(1)
        p0.renderer.setInitialXScale(0.0030000000000000001)
        p0.renderer.setFinalXScale(0.01)
        p0.renderer.setInitialYScale(0.0030000000000000001)
        p0.renderer.setFinalYScale(0.01)
        p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        p0.emitter.setAmplitudeSpread(0.025000000000000001)
        p0.emitter.setAmplitude(0.10000000000000001)
        p0.emitter.setRadius(0.5)
        gravityForceGroup = ForceGroup.ForceGroup('air')
        force0 = LinearVectorForce(Vec3(0.0, 0.0, 1.0), 1.0, 0)
        force0.setActive(1)
        force1 = LinearJitterForce(2.5, 0)
        force1.setActive(1)
        gravityForceGroup.addForce(force0)
        gravityForceGroup.addForce(force1)
        self.effect.addForceGroup(gravityForceGroup)
        self.effect.addParticles(p0)
        self.effect.setPos(0, 0, 0)

    
    def start(self):
        self.effect.start(self, self.renderParent)

    
    def stop(self):
        self.effect.disable()

    
    def destroy(self):
        self.effect.cleanup()
        self.renderParent.removeNode()
        del self.effect
        del self.renderParent


