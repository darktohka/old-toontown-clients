# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\DistributedEntity.py
from direct.distributed import DistributedObject
import Entity
from direct.directnotify import DirectNotifyGlobal

class DistributedEntity(DistributedObject.DistributedObject, Entity.Entity):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEntity')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        Entity.Entity.__init__(self)
        self.levelDoId = 0
        self.entId = 0
        self.level = None
        return

    def generateInit(self):
        DistributedEntity.notify.debug('generateInit')
        DistributedObject.DistributedObject.generateInit(self)

    def generate(self):
        DistributedEntity.notify.debug('generate')
        DistributedObject.DistributedObject.generate(self)

    def setLevelDoId(self, levelDoId):
        DistributedEntity.notify.debug('setLevelDoId: %s' % levelDoId)
        self.levelDoId = levelDoId

    def setEntId(self, entId):
        DistributedEntity.notify.debug('setEntId: %s' % entId)
        self.entId = entId

    def announceGenerate(self):
        DistributedEntity.notify.debug('announceGenerate (%s)' % self.entId)
        if self.levelDoId != 0:
            level = base.cr.doId2do[self.levelDoId]
            self.initializeEntity(level, self.entId)
            self.level.onEntityCreate(self.entId)
        else:
            self.level = None
        DistributedObject.DistributedObject.announceGenerate(self)
        return

    def disable(self):
        DistributedEntity.notify.debug('disable (%s)' % self.entId)
        self.destroy()
        DistributedObject.DistributedObject.disable(self)

    def delete(self):
        DistributedEntity.notify.debug('delete')
        DistributedObject.DistributedObject.delete(self)