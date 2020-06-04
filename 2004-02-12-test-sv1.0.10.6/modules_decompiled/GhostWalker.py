# File: G (Python 2.2)

from ShowBaseGlobal import *
import DirectNotifyGlobal
import NonPhysicsWalker

class GhostWalker(NonPhysicsWalker.NonPhysicsWalker):
    notify = DirectNotifyGlobal.directNotify.newCategory('GhostWalker')
    slideName = 'jump'

