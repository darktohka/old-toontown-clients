# File: R (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal

class RelatedObjectMgr(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('RelatedObjectMgr')
    doLaterSequence = 1
    
    def __init__(self, cr):
        self.cr = cr
        self.pendingObjects = { }

    
    def destroy(self):
        self.abortAllRequests()
        del self.cr
        del self.pendingObjects

    
    def requestObjects(self, doIdList, allCallback = None, eachCallback = None, timeout = None, timeoutCallback = None):
        (objects, doIdsPending) = self._RelatedObjectMgr__generateObjectList(doIdList)
        if eachCallback:
            for object in objects:
                if object:
                    eachCallback(object)
                
            
        
        if len(doIdsPending) == 0:
            if allCallback:
                allCallback(objects)
            
            return None
        
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
                self._RelatedObjectMgr__listenFor(doId)
            
            pendingList.append(tuple)
        
        if doLaterName:
            taskMgr.doMethodLater(timeout, self._RelatedObjectMgr__timeoutExpired, doLaterName, extraArgs = [
                tuple])
        
        return tuple

    
    def abortRequest(self, tuple):
        if tuple:
            (allCallback, eachCallback, timeoutCallback, doIdsPending, doIdList, doLaterName) = tuple
            if doLaterName:
                taskMgr.remove(doLaterName)
            
            self._RelatedObjectMgr__removePending(tuple, doIdsPending)
        

    
    def abortAllRequests(self):
        self.ignoreAll()
        for pendingList in self.pendingObjects.values():
            for tuple in pendingList:
                (allCallback, eachCallback, timeoutCallback, doIdsPending, doIdList, doLaterName) = tuple
                if doLaterName:
                    taskMgr.remove(doLaterName)
                
            
        
        self.pendingObjects = { }

    
    def _RelatedObjectMgr__timeoutExpired(self, tuple):
        (allCallback, eachCallback, timeoutCallback, doIdsPending, doIdList, doLaterName) = tuple
        self._RelatedObjectMgr__removePending(tuple, doIdsPending)
        if timeoutCallback:
            timeoutCallback(doIdList)
        else:
            (objects, doIdsPending) = self._RelatedObjectMgr__generateObjectList(doIdList)
            if allCallback:
                allCallback(objects)
            

    
    def _RelatedObjectMgr__removePending(self, tuple, doIdsPending):
        while len(doIdsPending) > 0:
            doId = doIdsPending.pop()
            pendingList = self.pendingObjects[doId]
            pendingList.remove(tuple)
            if len(pendingList) == 0:
                del self.pendingObjects[doId]
                self._RelatedObjectMgr__noListenFor(doId)
            

    
    def _RelatedObjectMgr__listenFor(self, doId):
        announceGenerateName = 'generate-%s' % doId
        self.acceptOnce(announceGenerateName, self._RelatedObjectMgr__generated)

    
    def _RelatedObjectMgr__noListenFor(self, doId):
        announceGenerateName = 'generate-%s' % doId
        self.ignore(announceGenerateName)

    
    def _RelatedObjectMgr__generated(self, object):
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
                
                (objects, doIdsPending) = self._RelatedObjectMgr__generateObjectList(doIdList)
                if allCallback:
                    allCallback(objects)
                
            
        

    
    def _RelatedObjectMgr__generateObjectList(self, doIdList):
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
        
        return (objects, doIdsPending)


