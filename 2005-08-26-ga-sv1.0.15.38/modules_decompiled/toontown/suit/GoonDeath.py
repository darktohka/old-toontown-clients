# File: G (Python 2.2)

from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from toontown.battle import BattleParticles

def createExplosionTrack(parent, deathNode, scale):
    explosion = loader.loadModelCopy('phase_3.5/models/props/explosion.bam')
    explosion.getChild(0).setScale(scale)
    explosion.reparentTo(deathNode)
    explosion.setBillboardPointEye()
    explosion.setPos(0, 0, 2)
    return Sequence(Func(deathNode.reparentTo, parent), Wait(0.59999999999999998), Func(deathNode.detachNode))


def createGoonExplosion(parent, explosionPoint, scale):
    BattleParticles.loadParticles()
    deathNode = NodePath('goonDeath')
    deathNode.setPos(explosionPoint)
    explosion = createExplosionTrack(parent, deathNode, scale)
    smallGearExplosion = BattleParticles.createParticleEffect('GearExplosion', numParticles = 10)
    bigGearExplosion = BattleParticles.createParticleEffect('WideGearExplosion', numParticles = 30)
    deathSound = base.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.mp3')
    return Parallel(explosion, SoundInterval(deathSound), ParticleInterval(smallGearExplosion, deathNode, worldRelative = 0, duration = 4.2999999999999998), ParticleInterval(bigGearExplosion, deathNode, worldRelative = 0, duration = 1.0), name = 'gears2MTrack')

