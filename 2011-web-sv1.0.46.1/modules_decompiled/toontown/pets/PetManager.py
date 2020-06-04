# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\pets\PetManager.py
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from direct.task import Task

def acquirePetManager():
    if not hasattr(base, 'petManager'):
        PetManager()
    base.petManager.incRefCount()


def releasePetManager():
    base.petManager.decRefCount()


class PetManager:
    __module__ = __name__
    CollTaskName = 'petFloorCollisions'

    def __init__(self):
        base.petManager = self
        self.refCount = 0
        self.cTrav = CollisionTraverser('petFloorCollisions')
        taskMgr.add(self._doCollisions, PetManager.CollTaskName, priority=ToontownGlobals.PetFloorCollPriority)

    def _destroy(self):
        taskMgr.remove(PetManager.CollTaskName)
        del self.cTrav

    def _doCollisions(self, task):
        self.cTrav.traverse(render)
        return Task.cont

    def incRefCount(self):
        self.refCount += 1

    def decRefCount(self):
        self.refCount -= 1
        if self.refCount == 0:
            self._destroy()
            del base.petManager