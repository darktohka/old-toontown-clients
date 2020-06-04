# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\DistCogdoLevelGame.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.level.DistributedLevel import DistributedLevel
from otp.level import LevelConstants
from otp.level import EditorGlobals
from toontown.cogdominium.DistCogdoGame import DistCogdoGame
from toontown.cogdominium.CogdoLevelGameBase import CogdoLevelGameBase
from toontown.cogdominium.CogdoEntityCreator import CogdoEntityCreator

class DistCogdoLevelGame(CogdoLevelGameBase, DistCogdoGame, DistributedLevel):
    __module__ = __name__
    notify = directNotify.newCategory('DistCogdoLevelGame')

    def __init__(self, cr):
        DistributedLevel.__init__(self, cr)
        DistCogdoGame.__init__(self, cr)

    def generate(self):
        DistributedLevel.generate(self)
        DistCogdoGame.generate(self)
        if __dev__:
            bboard.post(EditorGlobals.EditTargetPostName, self)

    def announceGenerate(self):
        DistributedLevel.announceGenerate(self)
        DistCogdoGame.announceGenerate(self)
        if __dev__:
            self.startHandleEdits()

    def createEntityCreator(self):
        return CogdoEntityCreator(level=self)

    def levelAnnounceGenerate(self):
        self.notify.debug('levelAnnounceGenerate')
        DistributedLevel.levelAnnounceGenerate(self)
        spec = self.getLevelSpec()
        if __dev__:
            typeReg = self.getEntityTypeReg()
            spec.setEntityTypeReg(typeReg)
        DistributedLevel.initializeLevel(self, spec)

    def privGotSpec(self, levelSpec):
        if __dev__:
            if not levelSpec.hasEntityTypeReg():
                typeReg = self.getEntityTypeReg()
                levelSpec.setEntityTypeReg(typeReg)
        DistributedLevel.privGotSpec(self, levelSpec)

    def initVisibility(self):
        levelMgr = self.getEntity(LevelConstants.LevelMgrEntId)
        levelMgr.geom.reparentTo(render)
        DistributedLevel.initVisibility(self)

    def placeLocalToon(self):
        DistributedLevel.placeLocalToon(self, moveLocalAvatar=False)

    def disable(self):
        if __dev__:
            self.stopHandleEdits()
        DistCogdoGame.disable(self)
        DistributedLevel.disable(self)

    def delete(self):
        DistCogdoGame.delete(self)
        DistributedLevel.delete(self)
        if __dev__:
            bboard.removeIfEqual(EditorGlobals.EditTargetPostName, self)