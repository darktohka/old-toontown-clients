# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\ObjectReport.py
__all__ = [
 'ExclusiveObjectPool', 'ObjectReport']
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase import DirectObject, ObjectPool, GarbageReport
from direct.showbase.PythonUtil import makeList, Sync
import gc, sys, __builtin__

class ExclusiveObjectPool(DirectObject.DirectObject):
    __module__ = __name__
    _ExclObjs = []
    _ExclObjIds = {}
    _SyncMaster = Sync('ExclusiveObjectPool.ExcludedObjectList')
    _SerialNumGen = SerialNumGen()

    @classmethod
    def addExclObjs(cls, *objs):
        for obj in makeList(objs):
            if id(obj) not in cls._ExclObjIds:
                cls._ExclObjs.append(obj)
            cls._ExclObjIds.setdefault(id(obj), 0)
            cls._ExclObjIds[id(obj)] += 1

        cls._SyncMaster.change()

    @classmethod
    def removeExclObjs(cls, *objs):
        for obj in makeList(objs):
            cls._ExclObjIds[id(obj)] -= 1
            if cls._ExclObjIds[id(obj)] == 0:
                del cls._ExclObjIds[id(obj)]
                cls._ExclObjs.remove(obj)

        cls._SyncMaster.change()

    def __init__(self, objects):
        self._objects = list(objects)
        self._postFilterObjs = []
        self._sync = Sync('%s-%s' % (self.__class__.__name__, self._SerialNumGen.next()), self._SyncMaster)
        self._sync.invalidate()
        ExclusiveObjectPool.addExclObjs(self._objects, self._postFilterObjs, self._sync)

    def destroy(self):
        self.ignoreAll()
        ExclusiveObjectPool.removeExclObjs(self._objects, self._postFilterObjs, self._sync)
        del self._objects
        del self._postFilterObjs
        del self._sync

    def _resync(self):
        if self._sync.isSynced(self._SyncMaster):
            return
        if hasattr(self, '_filteredPool'):
            ExclusiveObjectPool.removeExclObjs(*self._filteredPool._getInternalObjs())
            ExclusiveObjectPool.removeExclObjs(self._filteredPool)
            del self._filteredPool
        del self._postFilterObjs[:]
        for obj in self._objects:
            if id(obj) not in ExclusiveObjectPool._ExclObjIds:
                self._postFilterObjs.append(obj)

        self._filteredPool = ExclusiveObjectPool(self._postFilterObjs)
        ExclusiveObjectPool.addExclObjs(self._filteredPool)
        ExclusiveObjectPool.addExclObjs(*self._filteredPool._getInternalObjs())
        self._sync.sync(self._SyncMaster)

    def getObjsOfType(self, type):
        self._resync()
        return self._filteredPool.getObjsOfType(type)

    def printObjsOfType(self, type):
        self._resync()
        return self._filteredPool.printObjsOfType(type)

    def diff(self, other):
        self._resync()
        return self._filteredPool.diff(other._filteredPool)

    def typeFreqStr(self):
        self._resync()
        return self._filteredPool.typeFreqStr()

    def __len__(self):
        self._resync()
        return len(self._filteredPool)


class ObjectReport:
    __module__ = __name__
    notify = directNotify.newCategory('ObjectReport')

    def __init__(self, name, log=True):
        gr = GarbageReport.GarbageReport("ObjectReport's GarbageReport: %s" % name, log=log)
        gr.destroy()
        del gr
        self._name = name
        self._pool = ObjectPool.ObjectPool(self._getObjectList())
        if log:
            self.notify.info("===== ObjectReport: '%s' =====\n%s" % (self._name, self.typeFreqStr()))

    def destroy(self):
        self._pool.destroy()
        del self._pool
        del self._name

    def typeFreqStr(self):
        return self._pool.typeFreqStr()

    def diff(self, other):
        return self._pool.diff(other._pool)

    def getObjectPool(self):
        return self._pool

    def _getObjectList(self):
        if hasattr(sys, 'getobjects'):
            return sys.getobjects(0)
        else:
            gc.collect()
            gc_objects = gc.get_objects()
            objects = gc_objects
            objects.append(__builtin__.__dict__)
            nextObjList = gc_objects
            found = set()
            found.add(id(objects))
            found.add(id(found))
            found.add(id(gc_objects))
            for obj in objects:
                found.add(id(obj))

            while len(nextObjList):
                curObjList = nextObjList
                nextObjList = []
                for obj in curObjList:
                    refs = gc.get_referents(obj)
                    for ref in refs:
                        if id(ref) not in found:
                            found.add(id(ref))
                            objects.append(ref)
                            nextObjList.append(ref)

            return objects