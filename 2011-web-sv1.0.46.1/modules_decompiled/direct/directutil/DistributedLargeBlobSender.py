# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\directutil\DistributedLargeBlobSender.py
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
import LargeBlobSenderConsts

class DistributedLargeBlobSender(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLargeBlobSender')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def generate(self):
        DistributedLargeBlobSender.notify.debug('generate')
        DistributedObject.DistributedObject.generate(self)
        self.complete = 0
        self.doneEvent = None
        return

    def setMode(self, mode):
        self.mode = mode
        self.useDisk = mode & LargeBlobSenderConsts.USE_DISK

    def setTargetAvId(self, avId):
        self.targetAvId = avId

    def announceGenerate(self):
        DistributedLargeBlobSender.notify.debug('announceGenerate')
        DistributedObject.DistributedObject.announceGenerate(self)
        if self.targetAvId != base.localAvatar.doId:
            return
        if not self.useDisk:
            self.blob = ''

    def setChunk(self, chunk):
        DistributedLargeBlobSender.notify.debug('setChunk')
        if len(chunk) > 0:
            self.blob += chunk
        else:
            self.privOnBlobComplete()

    def setFilename(self, filename):
        DistributedLargeBlobSender.notify.debug('setFilename: %s' % filename)
        import os
        origDir = os.getcwd()
        bPath = LargeBlobSenderConsts.getLargeBlobPath()
        try:
            os.chdir(bPath)
        except OSError:
            DistributedLargeBlobSender.notify.error('could not access %s' % bPath)

        f = file(filename, 'rb')
        self.blob = f.read()
        f.close()
        os.unlink(filename)
        os.chdir(origDir)
        self.privOnBlobComplete()

    def isComplete(self):
        return self.complete

    def setDoneEvent(self, event):
        self.doneEvent = event

    def privOnBlobComplete(self):
        self.complete = 1
        if self.doneEvent is not None:
            messenger.send(self.doneEvent, [self.blob])
        return

    def getBlob(self):
        return self.blob

    def sendAck(self):
        self.sendUpdate('setAck', [])