# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\EntityCreator.py
import CutScene, EntityCreatorBase, BasicEntities
from direct.directnotify import DirectNotifyGlobal
import EditMgr, EntrancePoint, LevelMgr, LogicGate, ZoneEntity, ModelEntity, PathEntity, VisibilityExtender, PropSpinner, AmbientSound, LocatorEntity, CollisionSolidEntity

def nothing(*args):
    return 'nothing'


def nonlocal(*args):
    return 'nonlocal'


class EntityCreator(EntityCreatorBase.EntityCreatorBase):
    __module__ = __name__

    def __init__(self, level):
        EntityCreatorBase.EntityCreatorBase.__init__(self, level)
        self.level = level
        self.privRegisterTypes({'attribModifier': nothing, 'ambientSound': AmbientSound.AmbientSound, 'collisionSolid': CollisionSolidEntity.CollisionSolidEntity, 'cutScene': CutScene.CutScene, 'editMgr': EditMgr.EditMgr, 'entityGroup': nothing, 'entrancePoint': EntrancePoint.EntrancePoint, 'levelMgr': LevelMgr.LevelMgr, 'locator': LocatorEntity.LocatorEntity, 'logicGate': LogicGate.LogicGate, 'model': ModelEntity.ModelEntity, 'nodepath': BasicEntities.NodePathEntity, 'path': PathEntity.PathEntity, 'propSpinner': PropSpinner.PropSpinner, 'visibilityExtender': VisibilityExtender.VisibilityExtender, 'zone': ZoneEntity.ZoneEntity})

    def doCreateEntity(self, ctor, entId):
        return ctor(self.level, entId)