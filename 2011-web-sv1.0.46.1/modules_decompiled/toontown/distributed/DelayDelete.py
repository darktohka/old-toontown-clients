# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\distributed\DelayDelete.py


class DelayDelete:
    __module__ = __name__

    def __init__(self, distObj, name):
        self._distObj = distObj
        self._name = name
        self._token = self._distObj.acquireDelayDelete(name)

    def getObject(self):
        return self._distObj

    def getName(self):
        return self._name

    def destroy(self):
        token = self._token
        del self._token
        self._distObj.releaseDelayDelete(token)
        del self._distObj
        del self._name


def cleanupDelayDeletes(interval):
    if hasattr(interval, 'delayDelete'):
        delayDelete = interval.delayDelete
        del interval.delayDelete
        if type(delayDelete) == type([]):
            for i in delayDelete:
                i.destroy()

        else:
            delayDelete.destroy()
    if hasattr(interval, 'delayDeletes'):
        delayDeletes = interval.delayDeletes
        del interval.delayDeletes
        if type(delayDeletes) == type([]):
            for i in delayDeletes:
                i.destroy()

        else:
            delayDeletes.destroy()