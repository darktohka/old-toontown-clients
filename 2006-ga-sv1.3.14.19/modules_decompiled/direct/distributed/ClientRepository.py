# File: C (Python 2.2)

from pandac.PandaModules import *
from MsgTypes import *
from direct.task import Task
from direct.directnotify import DirectNotifyGlobal
import CRCache
import ConnectionRepository
from direct.showbase import PythonUtil
import ParentMgr
import RelatedObjectMgr
import time
from ClockDelta import *
from PyDatagram import PyDatagram
from PyDatagramIterator import PyDatagramIterator

class ClientRepository(ConnectionRepository.ConnectionRepository):
    notify = DirectNotifyGlobal.directNotify.newCategory('ClientRepository')
    
    def __init__(self):
        ConnectionRepository.ConnectionRepository.__init__(self, base.config)
        self.setClientDatagram(1)
        self.recorder = base.recorder
        self.doId2do = { }
        self.readDCFile()
        self.cache = CRCache.CRCache()
        self.serverDelta = 0
        self.bootedIndex = None
        self.bootedText = None
        self.parentMgr = ParentMgr.ParentMgr()
        self.relatedObjectMgr = RelatedObjectMgr.RelatedObjectMgr(self)
        self.heartbeatInterval = base.config.GetDouble('heartbeat-interval', 10)
        self.heartbeatStarted = 0
        self.lastHeartbeat = 0

    
    def abruptCleanup(self):
        self.relatedObjectMgr.abortAllRequests()

    
    def sendDisconnect(self):
        if self.isConnected():
            datagram = PyDatagram()
            datagram.addUint16(CLIENT_DISCONNECT)
            self.send(datagram)
            self.notify.info('Sent disconnect message to server')
            self.disconnect()
        
        self.stopHeartbeat()

    
    def setServerDelta(self, delta):
        self.serverDelta = delta

    
    def getServerDelta(self):
        return self.serverDelta

    
    def getServerTimeOfDay(self):
        return time.time() + self.serverDelta

    
    def handleGenerateWithRequired(self, di):
        classId = di.getUint16()
        doId = di.getUint32()
        dclass = self.dclassesByNumber[classId]
        distObj = self.generateWithRequiredFields(dclass, doId, di)

    
    def handleGenerateWithRequiredOther(self, di):
        classId = di.getUint16()
        doId = di.getUint32()
        dclass = self.dclassesByNumber[classId]
        distObj = self.generateWithRequiredOtherFields(dclass, doId, di)

    
    def handleQuietZoneGenerateWithRequired(self, di):
        classId = di.getUint16()
        doId = di.getUint32()
        dclass = self.dclassesByNumber[classId]
        if dclass.getClassDef().neverDisable:
            distObj = self.generateWithRequiredFields(dclass, doId, di)
        

    
    def handleQuietZoneGenerateWithRequiredOther(self, di):
        classId = di.getUint16()
        doId = di.getUint32()
        dclass = self.dclassesByNumber[classId]
        if dclass.getClassDef().neverDisable:
            distObj = self.generateWithRequiredOtherFields(dclass, doId, di)
        

    
    def generateWithRequiredFields(self, dclass, doId, di):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            distObj.generate()
            distObj.updateRequiredFields(dclass, di)
        elif self.cache.contains(doId):
            distObj = self.cache.retrieve(doId)
            self.doId2do[doId] = distObj
            distObj.generate()
            distObj.updateRequiredFields(dclass, di)
        else:
            classDef = dclass.getClassDef()
            if classDef == None:
                self.notify.error('Could not create an undefined %s object.' % dclass.getName())
            
            distObj = classDef(self)
            distObj.dclass = dclass
            distObj.doId = doId
            self.doId2do[doId] = distObj
            distObj.generateInit()
            distObj.generate()
            distObj.updateRequiredFields(dclass, di)
        return distObj

    
    def generateGlobalObject(self, doId, dcname):
        dclass = self.dclassesByName[dcname]
        classDef = dclass.getClassDef()
        if classDef == None:
            self.notify.error('Could not create an undefined %s object.' % dclass.getName())
        
        distObj = classDef(self)
        distObj.dclass = dclass
        distObj.doId = doId
        self.doId2do[doId] = distObj
        distObj.generateInit()
        distObj.generate()
        return distObj

    
    def generateWithRequiredOtherFields(self, dclass, doId, di):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            distObj.generate()
            distObj.updateRequiredOtherFields(dclass, di)
        elif self.cache.contains(doId):
            distObj = self.cache.retrieve(doId)
            self.doId2do[doId] = distObj
            distObj.generate()
            distObj.updateRequiredOtherFields(dclass, di)
        else:
            classDef = dclass.getClassDef()
            if classDef == None:
                self.notify.error('Could not create an undefined %s object.' % dclass.getName())
            
            distObj = classDef(self)
            distObj.dclass = dclass
            distObj.doId = doId
            self.doId2do[doId] = distObj
            distObj.generateInit()
            distObj.generate()
            distObj.updateRequiredOtherFields(dclass, di)
        return distObj

    
    def handleDisable(self, di):
        doId = di.getUint32()
        self.disableDoId(doId)

    
    def disableDoId(self, doId):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            del self.doId2do[doId]
            if distObj.getCacheable():
                self.cache.cache(distObj)
            else:
                distObj.deleteOrDelay()
        else:
            ClientRepository.notify.warning('Disable failed. DistObj ' + str(doId) + ' is not in dictionary')

    
    def handleDelete(self, di):
        doId = di.getUint32()
        self.deleteObject(doId)

    
    def deleteObject(self, doId):
        if self.doId2do.has_key(doId):
            obj = self.doId2do[doId]
            del self.doId2do[doId]
            obj.deleteOrDelay()
        elif self.cache.contains(doId):
            self.cache.delete(doId)
        else:
            ClientRepository.notify.warning('Asked to delete non-existent DistObj ' + str(doId))

    
    def handleUpdateField(self, di):
        doId = di.getUint32()
        do = self.doId2do.get(doId)
        if do != None:
            do.dclass.receiveUpdate(do, di)
        else:
            ClientRepository.notify.warning('Asked to update non-existent DistObj ' + str(doId))

    
    def handleGoGetLost(self, di):
        if di.getRemainingSize() > 0:
            self.bootedIndex = di.getUint16()
            self.bootedText = di.getString()
            ClientRepository.notify.warning('Server is booting us out (%d): %s' % (self.bootedIndex, self.bootedText))
        else:
            self.bootedIndex = None
            self.bootedText = None
            ClientRepository.notify.warning('Server is booting us out with no explanation.')

    
    def handleServerHeartbeat(self, di):
        if base.config.GetBool('server-heartbeat-info', 1):
            ClientRepository.notify.info('Server heartbeat.')
        

    
    def handleSystemMessage(self, di):
        message = di.getString()
        self.notify.info('Message from server: %s' % message)
        return message

    
    def handleUnexpectedMsgType(self, msgType, di):
        if msgType == CLIENT_GO_GET_LOST:
            self.handleGoGetLost(di)
        elif msgType == CLIENT_HEARTBEAT:
            self.handleServerHeartbeat(di)
        elif msgType == CLIENT_SYSTEM_MESSAGE:
            self.handleSystemMessage(di)
        else:
            currentLoginState = self.loginFSM.getCurrentState()
            if currentLoginState:
                currentLoginStateName = currentLoginState.getName()
            else:
                currentLoginStateName = 'None'
            currentGameState = self.gameFSM.getCurrentState()
            if currentGameState:
                currentGameStateName = currentGameState.getName()
            else:
                currentGameStateName = 'None'
            ClientRepository.notify.warning('Ignoring unexpected message type: ' + str(msgType) + ' login state: ' + currentLoginStateName + ' game state: ' + currentGameStateName)

    
    def sendSetShardMsg(self, shardId):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_SHARD)
        datagram.addUint32(shardId)
        self.send(datagram)

    
    def sendSetZoneMsg(self, zoneId, visibleZoneList = None):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_ZONE)
        datagram.addUint32(zoneId)
        if visibleZoneList is not None:
            vzl = list(visibleZoneList)
            vzl.sort()
            for zone in vzl:
                datagram.addUint32(zone)
            
        
        self.send(datagram)

    
    def handleDatagram(self, di):
        if self.notify.getDebug():
            print 'ClientRepository received datagram:'
            di.getDatagram().dumpHex(ostream)
        
        msgType = self.getMsgType()
        if msgType == CLIENT_DONE_SET_ZONE_RESP:
            self.handleSetZoneDone()
        
        if self.handler == None:
            self.handleUnexpectedMsgType(msgType, di)
        else:
            self.handler(msgType, di)
        self.considerHeartbeat()

    
    def sendHeartbeat(self):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_HEARTBEAT)
        self.send(datagram)
        self.lastHeartbeat = globalClock.getRealTime()
        self.considerFlush()

    
    def considerHeartbeat(self):
        if not (self.heartbeatStarted):
            self.notify.debug('Heartbeats not started; not sending.')
            return None
        
        elapsed = globalClock.getRealTime() - self.lastHeartbeat
        if elapsed < 0 or elapsed > self.heartbeatInterval:
            self.notify.info('Sending heartbeat mid-frame.')
            self.startHeartbeat()
        

    
    def stopHeartbeat(self):
        taskMgr.remove('heartBeat')
        self.heartbeatStarted = 0

    
    def startHeartbeat(self):
        self.stopHeartbeat()
        self.heartbeatStarted = 1
        self.sendHeartbeat()
        self.waitForNextHeartBeat()

    
    def sendHeartbeatTask(self, task):
        self.sendHeartbeat()
        self.waitForNextHeartBeat()
        return Task.done

    
    def waitForNextHeartBeat(self):
        taskMgr.doMethodLater(self.heartbeatInterval, self.sendHeartbeatTask, 'heartBeat')

    
    def sendUpdate(self, do, fieldName, args, sendToId = None):
        if not sendToId:
            pass
        dg = do.dclass.clientFormatUpdate(fieldName, do.doId, args)
        self.send(dg)

    
    def replaceMethod(self, oldMethod, newFunction):
        return 0

    
    def getAllOfType(self, type):
        result = []
        for obj in self.doId2do.values():
            if isinstance(obj, type):
                result.append(obj)
            
        
        return result


