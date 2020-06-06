# File: G (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
import NonPhysicsWalker

class GhostWalker(NonPhysicsWalker.NonPhysicsWalker):
    notify = DirectNotifyGlobal.directNotify.newCategory('GhostWalker')
    slideName = 'jump'

