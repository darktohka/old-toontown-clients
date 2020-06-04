# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\EntityCreatorAI.py
import EntityCreatorBase, LogicGate, EditMgrAI, LevelMgrAI, ZoneEntityAI
from direct.showbase.PythonUtil import Functor

def createDistributedEntity(AIclass, level, entId, zoneId):
    ent = AIclass(level, entId)
    ent.generateWithRequired(zoneId)
    return ent


def createLocalEntity(AIclass, level, entId, zoneId):
    ent = AIclass(level, entId)
    return ent


def nothing(*args):
    return 'nothing'


class EntityCreatorAI(EntityCreatorBase.EntityCreatorBase):
    __module__ = __name__

    def __init__(self, level):
        EntityCreatorBase.EntityCreatorBase.__init__(self, level)
        cLE = createLocalEntity
        self.privRegisterTypes({'attribModifier': nothing, 'ambientSound': nothing, 'collisionSolid': nothing, 'cutScene': nothing, 'editMgr': Functor(cLE, EditMgrAI.EditMgrAI), 'entityGroup': nothing, 'entrancePoint': nothing, 'levelMgr': Functor(cLE, LevelMgrAI.LevelMgrAI), 'locator': nothing, 'logicGate': Functor(cLE, LogicGate.LogicGate), 'model': nothing, 'nodepath': nothing, 'path': nothing, 'propSpinner': nothing, 'visibilityExtender': nothing, 'zone': Functor(cLE, ZoneEntityAI.ZoneEntityAI)})

    def doCreateEntity(self, ctor, entId):
        zoneId = self.level.getEntityZoneId(entId)
        self.notify.debug('creating entity %s in zone %s' % (entId, zoneId))
        return ctor(self.level, entId, zoneId)