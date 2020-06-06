# File: D (Python 2.2)

from direct.showbase.PandaObject import *
from direct.directnotify.DirectNotifyGlobal import *
from PyDatagram import PyDatagram
from PyDatagramIterator import PyDatagramIterator
ESNew = 1
ESDeleted = 2
ESDisabling = 3
ESDisabled = 4
ESGenerating = 5
ESGenerated = 6

class DistributedObject(PandaObject):
    notify = directNotify.newCategory('DistributedObject')
    neverDisable = 0
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedObject_initialized = 1
            self.cr = cr
            if wantOtpServer:
                self._DistributedObject__location = (None, None)
            
            self.setCacheable(0)
            self.delayDeleteCount = 0
            self.deleteImminent = 0
            self.activeState = ESNew
            self._DistributedObject__nextContext = 0
            self._DistributedObject__callbacks = { }
            self._DistributedObject__barrierContext = None
            self.zone = 0


    
    def setNeverDisable(self, bool):
        self.neverDisable = bool

    
    def getNeverDisable(self):
        return self.neverDisable

    
    def setCacheable(self, bool):
        self.cacheable = bool
        return None

    
    def getCacheable(self):
        return self.cacheable

    
    def deleteOrDelay(self):
        if self.delayDeleteCount > 0:
            self.deleteImminent = 1
        else:
            self.disableAnnounceAndDelete()

    
    def delayDelete(self, flag):
        if flag == 1:
            self.delayDeleteCount += 1
        elif flag == 0:
            self.delayDeleteCount -= 1
        else:
            self.notify.error('Invalid flag passed to delayDelete: ' + str(flag))
        if self.delayDeleteCount < 0:
            self.notify.error('Somebody decremented delayDelete for doId %s without incrementing' % self.doId)
        elif self.delayDeleteCount == 0:
            if self.deleteImminent:
                self.disableAnnounceAndDelete()
            
        else:
            self.notify.debug('delayDeleteCount for doId %s now %s' % (self.doId, self.delayDeleteCount))
        return self.delayDeleteCount

    
    def disableAnnounceAndDelete(self):
        self.disableAndAnnounce()
        self.delete()

    
    def disableAndAnnounce(self):
        if self.activeState != ESDisabled:
            self.activeState = ESDisabling
            messenger.send(self.uniqueName('disable'))
            self.disable()
        

    
    def announceGenerate(self):
        if self.activeState != ESGenerated:
            self.activeState = ESGenerated
            messenger.send(self.uniqueName('generate'), [
                self])
        

    
    def disable(self):
        if self.activeState != ESDisabled:
            self.activeState = ESDisabled
            self._DistributedObject__callbacks = { }
            if wantOtpServer:
                self.cr.deleteObjectLocation(self.doId, self._DistributedObject__location[0], self._DistributedObject__location[1])
                self._DistributedObject__location = (None, None)
            
        

    
    def isDisabled(self):
        return self.activeState < ESGenerating

    
    def isGenerated(self):
        return self.activeState == ESGenerated

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedObject_deleted = 1
            self.cr = None
            self.dclass = None


    
    def generate(self):
        self.activeState = ESGenerating

    
    def generateInit(self):
        self.activeState = ESGenerating

    
    def getDoId(self):
        return self.doId

    
    def updateRequiredFields(self, dclass, di):
        dclass.receiveUpdateBroadcastRequired(self, di)
        self.announceGenerate()

    
    def updateAllRequiredFields(self, dclass, di):
        dclass.receiveUpdateAllRequired(self, di)
        self.announceGenerate()

    
    def updateRequiredOtherFields(self, dclass, di):
        dclass.receiveUpdateBroadcastRequired(self, di)
        self.announceGenerate()
        dclass.receiveUpdateOther(self, di)

    
    def sendUpdate(self, fieldName, args = [], sendToId = None):
        if self.cr:
            self.cr.sendUpdate(self, fieldName, args, sendToId)
        

    
    def sendDisableMsg(self):
        self.cr.sendDisableMsg(self.doId)

    
    def sendDeleteMsg(self):
        self.cr.sendDeleteMsg(self.doId)

    
    def taskName(self, taskString):
        return taskString + '-' + str(self.getDoId())

    
    def uniqueName(self, idString):
        return idString + '-' + str(self.getDoId())

    
    def getCallbackContext(self, callback, extraArgs = []):
        context = self._DistributedObject__nextContext
        self._DistributedObject__callbacks[context] = (callback, extraArgs)
        self._DistributedObject__nextContext = self._DistributedObject__nextContext + 1 & 65535
        return context

    
    def getCurrentContexts(self):
        return self._DistributedObject__callbacks.keys()

    
    def getCallback(self, context):
        return self._DistributedObject__callbacks[context][0]

    
    def getCallbackArgs(self, context):
        return self._DistributedObject__callbacks[context][1]

    
    def doCallbackContext(self, context, args):
        tuple = self._DistributedObject__callbacks.get(context)
        if tuple:
            (callback, extraArgs) = tuple
            completeArgs = args + extraArgs
            if callback != None:
                callback(*completeArgs)
            
            del self._DistributedObject__callbacks[context]
        else:
            self.notify.warning('Got unexpected context from AI: %s' % context)

    
    def setBarrierData(self, data):
        for (context, name, avIds) in data:
            if base.localAvatar.doId in avIds:
                self._DistributedObject__barrierContext = (context, name)
                return None
            
        
        self._DistributedObject__barrierContext = None

    
    def doneBarrier(self, name = None):
        if self._DistributedObject__barrierContext != None:
            (context, aiName) = self._DistributedObject__barrierContext
            if name == None or name == aiName:
                self.sendUpdate('setBarrierReady', [
                    context])
                self._DistributedObject__barrierContext = None
            
        

    if wantOtpServer:
        
        def addInterest(self, zoneId, note = ''):
            self.cr.addInterest(self.getDoId(), zoneId, note)

        
        def setLocation(self, parentId, zoneId):
            self.cr.storeObjectLocation(self.doId, parentId, zoneId)
            self._DistributedObject__location = (parentId, zoneId)

        
        def getLocation(self):
            return self._DistributedObject__location

    
    
    def isLocal(self):
        if self.cr:
            pass
        return self.cr.isLocalId(self.doId)

    
    def updateZone(self, zoneId):
        self.cr.sendUpdateZone(self, zoneId)


