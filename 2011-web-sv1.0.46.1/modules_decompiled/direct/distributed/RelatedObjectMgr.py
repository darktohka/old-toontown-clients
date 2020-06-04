# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\distributed\RelatedObjectMgr.py
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal

class RelatedObjectMgr(DirectObject.DirectObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('RelatedObjectMgr')
    doLaterSequence = 1

    def __init__(self, cr):
        self.cr = cr
        self.pendingObjects = {}

    def destroy(self):
        self.abortAllRequests()
        del self.cr
        del self.pendingObjects

    def requestObjects(self, doIdList, allCallback=None, eachCallback=None, timeout=None, timeoutCallback=None):
        (objects, doIdsPending) = self.__generateObjectList(doIdList)
        if eachCallback:
            for object in objects:
                if object:
                    eachCallback(object)

        if len(doIdsPending) == 0:
            if allCallback:
                allCallback(objects)
            return
        doIdList = doIdList[:]
        doLaterName = None
        if timeout != None:
            doLaterName = 'RelatedObject-%s' % RelatedObjectMgr.doLaterSequence
            RelatedObjectMgr.doLaterSequence += 1
        tuple = (allCallback, eachCallback, timeoutCallback, doIdsPending, doIdList, doLaterName)
        for doId in doIdsPending:
            pendingList = self.pendingObjects.get(doId)
            if pendingList == None:
                pendingList = []
                self.pendingObjects[doId] = pendingList
                self.__listenFor(doId)
            pendingList.append(tuple)

        if doLaterName:
            taskMgr.doMethodLater(timeout, self.__timeoutExpired, doLaterName, extraArgs=[tuple])
        return tuple

    def abortRequest(self, tuple):
        if tuple:
            (allCallback, eachCallback, timeoutCallback, doIdsPending, doIdList, doLaterName) = tuple
            if doLaterName:
                taskMgr.remove(doLaterName)
            self.__removePending(tuple, doIdsPending)

    def abortAllRequests(self):
        self.ignoreAll()
        for pendingList in self.pendingObjects.values():
            for tuple in pendingList:
                (allCallback, eachCallback, timeoutCallback, doIdsPending, doIdList, doLaterName) = tuple
                if doLaterName:
                    taskMgr.remove(doLaterName)

        self.pendingObjects = {}

    def __timeoutExpired(self, tuple):
        (allCallback, eachCallback, timeoutCallback, doIdsPending, doIdList, doLaterName) = tuple
        self.__removePending(tuple, doIdsPending)
        if timeoutCallback:
            timeoutCallback(doIdList)
        else:
            (objects, doIdsPending) = self.__generateObjectList(doIdList)
            if allCallback:
                allCallback(objects)

    def __removePending(self, tuple, doIdsPending):
        while len(doIdsPending) > 0:
            doId = doIdsPending.pop()
            pendingList = self.pendingObjects[doId]
            pendingList.remove(tuple)
            if len(pendingList) == 0:
                del self.pendingObjects[doId]
                self.__noListenFor(doId)

    def __listenFor(self, doId):
        announceGenerateName = 'generate-%s' % doId
        self.acceptOnce(announceGenerateName, self.__generated)

    def __noListenFor(self, doId):
        announceGenerateName = 'generate-%s' % doId
        self.ignore(announceGenerateName)

    def __generated(self, object):
        doId = object.doId
        pendingList = self.pendingObjects[doId]
        del self.pendingObjects[doId]
        for tuple in pendingList:
            (allCallback, eachCallback, timeoutCallback, doIdsPending, doIdList, doLaterName) = tuple
            doIdsPending.remove(doId)
            if eachCallback:
                eachCallback(object)
            if len(doIdsPending) == 0:
                if doLaterName:
                    taskMgr.remove(doLaterName)
                (objects, doIdsPending) = self.__generateObjectList(doIdList)
                if None in objects:
                    pass
                if allCallback:
                    allCallback(objects)

        return

    def __generateObjectList(self, doIdList):
        objects = []
        doIdsPending = []
        for doId in doIdList:
            if doId:
                object = self.cr.doId2do.get(doId)
                objects.append(object)
                if object == None:
                    doIdsPending.append(doId)
            else:
                objects.append(None)

        return (
         objects, doIdsPending)