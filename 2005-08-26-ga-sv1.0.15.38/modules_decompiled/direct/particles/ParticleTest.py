# File: P (Python 2.2)

from direct.directbase.TestStart import *
from pandac.LinearVectorForce import LinearVectorForce
from pandac.Vec3 import Vec3
import ParticleEffect
from direct.tkpanels import ParticlePanel
import ForceGroup
base.enableParticles()
fg = ForceGroup.ForceGroup()
gravity = LinearVectorForce(Vec3(0.0, 0.0, -10.0))
fg.addForce(gravity)
pe = ParticleEffect.ParticleEffect('particle-fx')
pe.reparentTo(render)
pe.addForceGroup(fg)
pp = ParticlePanel.ParticlePanel(pe)
