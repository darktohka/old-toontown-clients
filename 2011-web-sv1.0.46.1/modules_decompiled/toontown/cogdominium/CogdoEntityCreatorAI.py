# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\CogdoEntityCreatorAI.py
from direct.showbase.PythonUtil import Functor
from otp.level import EntityCreatorAI
from toontown.cogdominium.CogdoLevelMgrAI import CogdoLevelMgrAI
from toontown.cogdominium import CogdoBoardroomGameConsts
from toontown.cogdominium import CogdoCraneGameConsts

class CogdoEntityCreatorAI(EntityCreatorAI.EntityCreatorAI):
    __module__ = __name__

    def __init__(self, level):
        EntityCreatorAI.EntityCreatorAI.__init__(self, level)
        cDE = EntityCreatorAI.createDistributedEntity
        cLE = EntityCreatorAI.createLocalEntity
        nothing = EntityCreatorAI.nothing
        self.privRegisterTypes({'levelMgr': Functor(cLE, CogdoLevelMgrAI), 'cogdoBoardroomGameSettings': Functor(cLE, Functor(self._createCogdoSettings, CogdoBoardroomGameConsts.Settings)), 
           'cogdoCraneGameSettings': Functor(cLE, Functor(self._createCogdoSettings, CogdoCraneGameConsts.Settings)), 
           'cogdoCraneCogSettings': Functor(cLE, Functor(self._createCogdoSettings, CogdoCraneGameConsts.CogSettings))})

    def _createCogdoSettings(self, ent, level, entId):
        ent.initializeEntity(level, entId)
        return ent