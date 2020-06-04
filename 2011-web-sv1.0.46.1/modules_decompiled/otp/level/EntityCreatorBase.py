# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\EntityCreatorBase.py
from direct.directnotify import DirectNotifyGlobal

class EntityCreatorBase:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('EntityCreator')

    def __init__(self, level):
        self.level = level
        self.entType2Ctor = {}

    def createEntity(self, entId):
        entType = self.level.getEntityType(entId)
        if not self.entType2Ctor.has_key(entType):
            self.notify.error('unknown entity type: %s (ent%s)' % (entType, entId))
        ent = self.doCreateEntity(self.entType2Ctor[entType], entId)
        return ent

    def getEntityTypes(self):
        return self.entType2Ctor.keys()

    def privRegisterType(self, entType, ctor):
        if self.entType2Ctor.has_key(entType):
            self.notify.debug('replacing %s ctor %s with %s' % (entType, self.entType2Ctor[entType], ctor))
        self.entType2Ctor[entType] = ctor

    def privRegisterTypes(self, type2ctor):
        for (entType, ctor) in type2ctor.items():
            self.privRegisterType(entType, ctor)