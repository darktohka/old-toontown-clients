# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\distributed\DelayDeletable.py
from direct.distributed.DistributedObject import ESGenerating, ESGenerated, ESNum2Str

class DelayDeletable:
    __module__ = __name__
    DelayDeleteSerialGen = SerialNumGen()

    def delayDelete(self):
        pass

    def acquireDelayDelete(self, name):
        global ESGenerated
        global ESGenerating
        if not self._delayDeleteForceAllow and self.activeState not in (ESGenerating, ESGenerated):
            self.notify.error('cannot acquire DelayDelete "%s" on %s because it is in state %s' % (name, self.__class__.__name__, ESNum2Str[self.activeState]))
        if self.getDelayDeleteCount() == 0:
            self.cr._addDelayDeletedDO(self)
        token = DelayDeletable.DelayDeleteSerialGen.next()
        self._token2delayDeleteName[token] = name
        return token

    def releaseDelayDelete(self, token):
        name = self._token2delayDeleteName.pop(token)
        if len(self._token2delayDeleteName) == 0:
            self.cr._removeDelayDeletedDO(self)
            if self._delayDeleted:
                self.disableAnnounceAndDelete()

    def getDelayDeleteNames(self):
        return self._token2delayDeleteName.values()

    def forceAllowDelayDelete(self):
        self._delayDeleteForceAllow = True