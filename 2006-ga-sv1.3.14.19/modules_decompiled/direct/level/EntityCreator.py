# File: E (Python 2.2)

import CutScene
import EntityCreatorBase
import BasicEntities
from direct.directnotify import DirectNotifyGlobal
import EditMgr
import EntrancePoint
import LevelMgr
import LogicGate
import ZoneEntity
import ModelEntity
import PathEntity
import VisibilityExtender
import PropSpinner
import AmbientSound

def nothing(*args):
    return 'nothing'


class EntityCreator(EntityCreatorBase.EntityCreatorBase):
    
    def __init__(self, level):
        EntityCreatorBase.EntityCreatorBase.__init__(self, level)
        self.level = level
        self.privRegisterTypes({
            'ambientSound': AmbientSound.AmbientSound,
            'cutScene': CutScene.CutScene,
            'editMgr': EditMgr.EditMgr,
            'entityGroup': nothing,
            'entrancePoint': EntrancePoint.EntrancePoint,
            'levelMgr': LevelMgr.LevelMgr,
            'logicGate': LogicGate.LogicGate,
            'model': ModelEntity.ModelEntity,
            'nodepath': BasicEntities.NodePathEntity,
            'path': PathEntity.PathEntity,
            'propSpinner': PropSpinner.PropSpinner,
            'visibilityExtender': VisibilityExtender.VisibilityExtender,
            'zone': ZoneEntity.ZoneEntity })

    
    def doCreateEntity(self, ctor, entId):
        return ctor(self.level, entId)


