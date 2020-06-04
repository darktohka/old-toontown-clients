# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\distributed\CRDataCache.py
from direct.distributed.CachedDOData import CachedDOData

class CRDataCache:
    __module__ = __name__

    def __init__(self):
        self._doId2name2data = {}
        self._size = config.GetInt('crdatacache-size', 10)
        self._junkIndex = 0

    def destroy(self):
        del self._doId2name2data

    def setCachedData(self, doId, name, data):
        if len(self._doId2name2data) >= self._size:
            if self._junkIndex >= len(self._doId2name2data):
                self._junkIndex = 0
            junkDoId = self._doId2name2data.keys()[self._junkIndex]
            self._junkIndex += 1
            for name in self._doId2name2data[junkDoId]:
                self._doId2name2data[junkDoId][name].flush()

            del self._doId2name2data[junkDoId]
        self._doId2name2data.setdefault(doId, {})
        cachedData = self._doId2name2data[doId].get(name)
        if cachedData:
            cachedData.flush()
            cachedData.destroy()
        self._doId2name2data[doId][name] = data

    def hasCachedData(self, doId):
        return doId in self._doId2name2data

    def popCachedData(self, doId):
        data = self._doId2name2data[doId]
        del self._doId2name2data[doId]
        return data

    def flush(self):
        for doId in self._doId2name2data:
            for name in self._doId2name2data[doId]:
                self._doId2name2data[doId][name].flush()

        self._doId2name2data = {}