# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\suit\GoonDeath.py
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *
from direct.particles import ParticleEffect
from toontown.battle import BattleParticles

def createExplosionTrack(parent, deathNode, scale):
    explosion = loader.loadModel('phase_3.5/models/props/explosion.bam')
    explosion.getChild(0).setScale(scale)
    explosion.reparentTo(deathNode)
    explosion.setBillboardPointEye()
    explosion.setPos(0, 0, 2)
    return Sequence(Func(deathNode.reparentTo, parent), Wait(0.6), Func(deathNode.detachNode))


def createGoonExplosion(parent, explosionPoint, scale):
    BattleParticles.loadParticles()
    deathNode = NodePath('goonDeath')
    deathNode.setPos(explosionPoint)
    explosion = createExplosionTrack(parent, deathNode, scale)
    smallGearExplosion = BattleParticles.createParticleEffect('GearExplosion', numParticles=10)
    bigGearExplosion = BattleParticles.createParticleEffect('WideGearExplosion', numParticles=30)
    deathSound = base.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.mp3')
    return Parallel(explosion, SoundInterval(deathSound), ParticleInterval(smallGearExplosion, deathNode, worldRelative=0, duration=4.3, cleanup=True), ParticleInterval(bigGearExplosion, deathNode, worldRelative=0, duration=1.0, cleanup=True), name='gears2MTrack')