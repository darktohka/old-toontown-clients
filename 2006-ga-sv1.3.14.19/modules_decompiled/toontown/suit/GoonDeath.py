# File: G (Python 2.2)

from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from toontown.battle import BattleParticles

def createExplosionTrack(parent, explosionPoint = Point3(0)):
    explosion = loader.loadModelOnce('phase_3.5/models/props/explosion.bam')
    sequenceNode = explosion.find('**/+SequenceNode').node()
    explosion.setBillboardPointEye()
    return Sequence(Func(explosion.reparentTo, parent), Func(explosion.setPos, explosionPoint), Func(explosion.setScale, 0.40000000000000002), Wait(0.59999999999999998), Func(explosion.detachNode))


def createGoonExplosion(goonExplosionNP):
    BattleParticles.loadParticles()
    explosion = createExplosionTrack(goonExplosionNP, explosionPoint = Point3(0, 0, 2))
    smallGearExplosion = BattleParticles.createParticleEffect('GearExplosion', numParticles = 10)
    bigGearExplosion = BattleParticles.createParticleEffect('WideGearExplosion', numParticles = 30)
    deathSound = base.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.mp3')
    return Parallel(explosion, SoundInterval(deathSound), ParticleInterval(smallGearExplosion, goonExplosionNP, worldRelative = 0, duration = 4.2999999999999998), ParticleInterval(bigGearExplosion, goonExplosionNP, worldRelative = 0, duration = 1.0), name = 'gears2MTrack')

