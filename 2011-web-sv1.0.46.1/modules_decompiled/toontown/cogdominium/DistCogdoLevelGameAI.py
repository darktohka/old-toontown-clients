# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\DistCogdoLevelGameAI.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.level.DistributedLevelAI import DistributedLevelAI
from toontown.cogdominium.DistCogdoGameAI import DistCogdoGameAI
from toontown.cogdominium.CogdoEntityCreatorAI import CogdoEntityCreatorAI
from toontown.cogdominium.CogdoLevelGameBase import CogdoLevelGameBase

class DistCogdoLevelGameAI(CogdoLevelGameBase, DistCogdoGameAI, DistributedLevelAI):
    __module__ = __name__
    notify = directNotify.newCategory('DistCogdoLevelGameAI')

    def __init__(self, air, interior):
        DistCogdoGameAI.__init__(self, air, interior)
        DistributedLevelAI.__init__(self, air, self.zoneId, 0, self.getToonIds())

    def generate(self):
        self.notify.info('loading spec')
        spec = self.getLevelSpec()
        if __dev__:
            self.notify.info('creating entity type registry')
            typeReg = self.getEntityTypeReg()
            spec.setEntityTypeReg(typeReg)
        DistributedLevelAI.generate(self, spec)
        DistCogdoGameAI.generate(self)
        if __dev__:
            self.startHandleEdits()

    def createEntityCreator(self):
        return CogdoEntityCreatorAI(level=self)

    def _levelControlsRequestDelete(self):
        return False

    def requestDelete(self):
        DistCogdoGameAI.requestDelete(self)

    def delete(self):
        if __dev__:
            self.stopHandleEdits()
        DistCogdoGameAI.delete(self)
        DistributedLevelAI.delete(self, deAllocZone=False)