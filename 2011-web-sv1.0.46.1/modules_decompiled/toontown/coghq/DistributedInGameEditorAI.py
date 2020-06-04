# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\DistributedInGameEditorAI.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from direct.directutil import DistributedLargeBlobSenderAI
from SpecImports import *

class DistributedInGameEditorAI(DistributedObjectAI.DistributedObjectAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInGameEditorAI')

    def __init__(self, air, level, editorAvId, editUsername):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.editorAvId = editorAvId
        self.editUsername = editUsername
        self.level = level
        self.levelDoId = self.level.getDoId()
        self.generateWithRequired(level.zoneId)

    def generate(self):
        self.notify.debug('generate')
        DistributedObjectAI.DistributedObjectAI.generate(self)
        simbase.levelEditor = self
        self.acceptOnce(self.air.getAvatarExitEvent(self.editorAvId), self.setFinished)
        self.accept(self.level.getAttribChangeEventName(), self.handleAttribChange)

    def delete(self):
        self.notify.debug('delete')
        messenger.send(self.getDoneEvent())
        DistributedObjectAI.DistributedObjectAI.delete(self)
        self.ignoreAll()

    def getDoneEvent(self):
        return self.uniqueName('levelEditorDone')

    def getEditorAvId(self):
        return self.editorAvId

    def getEditUsername(self):
        return self.editUsername

    def getLevelDoId(self):
        return self.levelDoId

    def requestCurrentLevelSpec(self):
        print 'requestCurrentLevelSpec'
        spec = self.level.levelSpec
        specStr = repr(spec)
        largeBlob = DistributedLargeBlobSenderAI.DistributedLargeBlobSenderAI(self.air, self.zoneId, self.editorAvId, specStr, useDisk=simbase.air._specByDisk)
        self.sendUpdateToAvatarId(self.editorAvId, 'setSpecSenderDoId', [largeBlob.doId])

    def setEdit(self, entId, attribName, valueStr, username):
        self.level.setAttribChange(entId, attribName, eval(valueStr), username)

    def handleAttribChange(self, entId, attrib, value, username):
        self.sendUpdateToAvatarId(self.editorAvId, 'setAttribChange', [
         entId, attrib, repr(value), username])

    def setFinished(self):
        self.requestDelete()