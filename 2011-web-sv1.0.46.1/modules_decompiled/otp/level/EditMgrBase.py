# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\EditMgrBase.py
import Entity
from direct.directnotify import DirectNotifyGlobal

class EditMgrBase(Entity.Entity):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('EditMgr')

    def __init__(self, level, entId):
        Entity.Entity.__init__(self, level, entId)

    def destroy(self):
        Entity.Entity.destroy(self)
        self.ignoreAll()

    if __dev__:

        def setInsertEntity(self, data):
            self.level.setEntityCreatorUsername(data['entId'], data['username'])
            self.level.levelSpec.insertEntity(data['entId'], data['entType'], data['parentEntId'])
            self.level.levelSpec.doSetAttrib(self.entId, 'insertEntity', None)
            return

        def setRemoveEntity(self, data):
            self.level.levelSpec.removeEntity(data['entId'])
            self.level.levelSpec.doSetAttrib(self.entId, 'removeEntity', None)
            return