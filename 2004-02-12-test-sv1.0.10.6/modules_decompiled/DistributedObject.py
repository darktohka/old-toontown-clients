# File: D (Python 2.2)

from PandaObject import *
from DirectNotifyGlobal import *
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
            self.setCacheable(0)
            self.delayDeleteCount = 0
            self.deleteImminent = 0
            self.activeState = ESNew
            self._DistributedObject__nextContext = 0
            self._DistributedObject__callbacks = { }
            self._DistributedObject__barrierContext = None


    
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
            self.notify.debug('delayDeleteCount for doId %s now 0' % self.doId)
            if self.deleteImminent:
                self.notify.debug('delayDeleteCount for doId %s -- deleteImminent' % self.doId)
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
        self.activeState = ESGenerated
        messenger.send(self.uniqueName('generate'), [
            self])

    
    def disable(self):
        self.activeState = ESDisabled
        self._DistributedObject__callbacks = { }

    
    def isDisabled(self):
        return self.activeState < ESGenerating

    
    def isGenerated(self):
        return self.activeState == ESGenerated

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedObject_deleted = 1
            del self.cr


    
    def generate(self):
        self.activeState = ESGenerating

    
    def generateInit(self):
        self.activeState = ESGenerating

    
    def getDoId(self):
        return self.doId

    
    def updateRequiredFields(self, cdc, di):
        for i in cdc.broadcastRequiredCDU:
            i.updateField(cdc, self, di)
        
        self.announceGenerate()

    
    def updateAllRequiredFields(self, cdc, di):
        for i in cdc.allRequiredCDU:
            i.updateField(cdc, self, di)
        
        self.announceGenerate()

    
    def updateRequiredOtherFields(self, cdc, di):
        for i in cdc.broadcastRequiredCDU:
            i.updateField(cdc, self, di)
        
        self.announceGenerate()
        numberOfOtherFields = di.getArg(STUint16)
        for i in range(numberOfOtherFields):
            cdc.updateField(self, di)
        

    
    def sendUpdate(self, fieldName, args = [], sendToId = None):
        self.cr.sendUpdate(self, fieldName, args, sendToId)

    
    def taskName(self, taskString):
        return taskString + '-' + str(self.getDoId())

    
    def uniqueName(self, idString):
        return idString + '-' + str(self.getDoId())

    
    def isLocal(self):
        return 0

    
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
        dg = Datagram(data)
        dgi = DatagramIterator(dg)
        while dgi.getRemainingSize() > 0:
            context = dgi.getUint16()
            numToons = dgi.getUint16()
            for i in range(numToons):
                avId = dgi.getUint32()
                if avId == toonbase.localToon.doId:
                    self._DistributedObject__barrierContext = context
                    return None
                
            
        self._DistributedObject__barrierContext = None

    
    def doneBarrier(self):
        if self._DistributedObject__barrierContext != None:
            self.sendUpdate('setBarrierReady', [
                self._DistributedObject__barrierContext])
            self._DistributedObject__barrierContext = None
        


