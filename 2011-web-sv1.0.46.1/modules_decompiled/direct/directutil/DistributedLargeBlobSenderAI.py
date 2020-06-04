# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\directutil\DistributedLargeBlobSenderAI.py
from direct.distributed import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
import LargeBlobSenderConsts

class DistributedLargeBlobSenderAI(DistributedObjectAI.DistributedObjectAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLargeBlobSenderAI')

    def __init__(self, air, zoneId, targetAvId, data, useDisk=0):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.targetAvId = targetAvId
        self.mode = 0
        if useDisk:
            self.mode |= LargeBlobSenderConsts.USE_DISK
        self.generateWithRequired(zoneId)
        s = str(data)
        if useDisk:
            import os, random
            origDir = os.getcwd()
            bPath = LargeBlobSenderConsts.getLargeBlobPath()
            try:
                os.chdir(bPath)
            except OSError:
                DistributedLargeBlobSenderAI.notify.error('could not access %s' % bPath)
            else:
                while 1:
                    num = random.randrange((1 << 30) - 1)
                    filename = LargeBlobSenderConsts.FilePattern % num
                    try:
                        os.stat(filename)
                    except OSError:
                        break

                f = file(filename, 'wb')
                f.write(s)
                f.close()
                os.chdir(origDir)
                self.sendUpdateToAvatarId(self.targetAvId, 'setFilename', [filename])
        else:
            chunkSize = LargeBlobSenderConsts.ChunkSize
            while len(s):
                self.sendUpdateToAvatarId(self.targetAvId, 'setChunk', [s[:chunkSize]])
                s = s[chunkSize:]

            self.sendUpdateToAvatarId(self.targetAvId, 'setChunk', [''])

    def getMode(self):
        return self.mode

    def getTargetAvId(self):
        return self.targetAvId

    def setAck(self):
        DistributedLargeBlobSenderAI.notify.debug('setAck')
        self.requestDelete()