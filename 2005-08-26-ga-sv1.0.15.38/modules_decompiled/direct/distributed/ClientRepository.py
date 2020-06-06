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
        if wantOtpServer:
            self._ClientRepository__doHierarchy = { }
        
        self.readDCFile()
        self.cache = CRCache.CRCache()
        self.serverDelta = 0
        self.bootedIndex = None
        self.bootedText = None
        self.worldScale = render.attachNewNode('worldScale')
        self.worldScale.setScale(base.config.GetFloat('world-scale', 100))
        self.priorWorldPos = None
        self.parentMgr = ParentMgr.ParentMgr()
        self.relatedObjectMgr = RelatedObjectMgr.RelatedObjectMgr(self)
        self.heartbeatInterval = base.config.GetDouble('heartbeat-interval', 10)
        self.heartbeatStarted = 0
        self.lastHeartbeat = 0
        if wantOtpServer:
            self._interestIdAssign = 1
            self._interests = { }
        
        self.handler = self.publicServerDatagramHandler
        self.DOIDbase = 0
        self.DOIDnext = 0
        self.DOIDlast = 0

    
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

    
    def setWorldOffset(self, xOffset = 0, yOffset = 0):
        self.worldXOffset = xOffset
        self.worldYOffset = yOffset

    
    def getWorldPos(self, nodePath):
        pos = nodePath.getPos(self.worldScale)
        return (int(round(pos.getX())), int(round(pos.getY())))

    
    def sendWorldPos(self, x, y):
        onScreenDebug.add('worldPos', '%-4d, %-4d' % (x, y))
        return None
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_WORLD_POS)
        datagram.addInt16(x)
        datagram.addSint16(y)
        self.send(datagram)

    
    def checkWorldPos(self, nodePath):
        worldPos = self.getWorldPos(nodePath)
        if self.priorWorldPos != worldPos:
            self.priorWorldPos = worldPos
            self.sendWorldPos(worldPos[0], worldPos[1])
        

    
    def setServerDelta(self, delta):
        self.serverDelta = delta

    
    def getServerDelta(self):
        return self.serverDelta

    
    def getServerTimeOfDay(self):
        return time.time() + self.serverDelta

    if wantOtpServer:
        
        def handleObjectLocation(self, di):
            doId = di.getUint32()
            parentId = di.getUint32()
            zoneId = di.getUint32()
            obj = self.doId2do.get(doId)
            if obj != None:
                self.notify.info('handleObjectLocation: doId: %s parentId: %s zoneId: %s' % (doId, parentId, zoneId))
                obj.setLocation(parentId, zoneId)
            else:
                ClientRepository.notify.warning('handleObjectLocation: Asked to update non-existent obj: %s' % doId)

        
        def storeObjectLocation(self, objId, parentId, zoneId):
            if parentId is None or zoneId is None:
                return None
            
            obj = self.doId2do.get(objId)
            (oldParentId, oldZoneId) = obj.getLocation()
            if oldParentId == parentId:
                parentZoneDict = self._ClientRepository__doHierarchy.get(parentId)
                oldObjList = parentZoneDict.get(oldZoneId)
                oldObjList.remove(objId)
                objList = parentZoneDict.get(zoneId)
                if objList is None:
                    parentZoneDict[zoneId] = [
                        objId]
                    return None
                else:
                    objList.append(objId)
                    return None
            
            if oldParentId is not None and oldZoneId is not None:
                self.deleteObjectLocation(objId, oldParentId, oldZoneId)
            
            parentZoneDict = self._ClientRepository__doHierarchy.get(parentId)
            if parentZoneDict is None:
                self._ClientRepository__doHierarchy[parentId] = {
                    zoneId: [
                        objId] }
            else:
                objList = parentZoneDict.get(zoneId)
                if objList is None:
                    parentZoneDict[zoneId] = [
                        objId]
                else:
                    objList.append(objId)

        
        def deleteObjectLocation(self, objId, parentId, zoneId):
            if parentId is None or zoneId is None:
                return None
            
            parentZoneDict = self._ClientRepository__doHierarchy.get(parentId)
            objList = parentZoneDict.get(zoneId)
            if len(objList) == 1:
                del parentZoneDict[zoneId]
            else:
                objList.remove(objId)

    
    
    def handleGenerateWithRequired(self, di):
        if wantOtpServer:
            parentId = di.getUint32()
            zoneId = di.getUint32()
        
        classId = di.getUint16()
        doId = di.getUint32()
        dclass = self.dclassesByNumber[classId]
        dclass.startGenerate()
        if wantOtpServer:
            distObj = self.generateWithRequiredFields(dclass, doId, di, parentId, zoneId)
        else:
            distObj = self.generateWithRequiredFields(dclass, doId, di)
        dclass.stopGenerate()

    
    def handleGenerateWithRequiredOther(self, di):
        if wantOtpServer:
            parentId = di.getUint32()
            zoneId = di.getUint32()
        
        classId = di.getUint16()
        doId = di.getUint32()
        dclass = self.dclassesByNumber[classId]
        dclass.startGenerate()
        if wantOtpServer:
            distObj = self.generateWithRequiredOtherFields(dclass, doId, di, parentId, zoneId)
        else:
            distObj = self.generateWithRequiredOtherFields(dclass, doId, di)
        dclass.stopGenerate()

    
    def handleQuietZoneGenerateWithRequired(self, di):
        if wantOtpServer:
            parentId = di.getUint32()
            zoneId = di.getUint32()
        
        classId = di.getUint16()
        doId = di.getUint32()
        dclass = self.dclassesByNumber[classId]
        dclass.startGenerate()
        if not wantOtpServer:
            if dclass.getClassDef().neverDisable:
                distObj = self.generateWithRequiredFields(dclass, doId, di)
            
        else:
            distObj = self.generateWithRequiredFields(dclass, doId, di, parentId, zoneId)
        dclass.stopGenerate()

    
    def handleQuietZoneGenerateWithRequiredOther(self, di):
        if wantOtpServer:
            parentId = di.getUint32()
            zoneId = di.getUint32()
        
        classId = di.getUint16()
        doId = di.getUint32()
        dclass = self.dclassesByNumber[classId]
        dclass.startGenerate()
        if not wantOtpServer:
            if dclass.getClassDef().neverDisable:
                distObj = self.generateWithRequiredOtherFields(dclass, doId, di)
            
        else:
            distObj = self.generateWithRequiredOtherFields(dclass, doId, di, parentId, zoneId)
        dclass.stopGenerate()

    
    def generateWithRequiredFields(self, dclass, doId, di, parentId = None, zoneId = None):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            if wantOtpServer:
                distObj.setLocation(parentId, zoneId)
            
            distObj.generate()
            distObj.updateRequiredFields(dclass, di)
        elif self.cache.contains(doId):
            distObj = self.cache.retrieve(doId)
            self.doId2do[doId] = distObj
            if wantOtpServer:
                distObj.setLocation(parentId, zoneId)
            
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
            if wantOtpServer:
                distObj.setLocation(parentId, zoneId)
            
            distObj.generateInit()
            distObj.generate()
            distObj.updateRequiredFields(dclass, di)
            if wantOtpServer:
                print 'New DO:%s, dclass:%s' % (doId, dclass.getName())
            
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
        if wantOtpServer:
            parentId = None
            zoneId = None
            distObj.setLocation(parentId, zoneId)
        
        distObj.generateInit()
        distObj.generate()
        return distObj

    
    def generateWithRequiredOtherFields(self, dclass, doId, di, parentId = None, zoneId = None):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            if wantOtpServer:
                distObj.setLocation(parentId, zoneId)
            
            distObj.generate()
            distObj.updateRequiredOtherFields(dclass, di)
        elif self.cache.contains(doId):
            distObj = self.cache.retrieve(doId)
            self.doId2do[doId] = distObj
            if wantOtpServer:
                distObj.setLocation(parentId, zoneId)
            
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
            if wantOtpServer:
                distObj.setLocation(parentId, zoneId)
            
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

    
    def handleSetDOIDrange(self, di):
        self.DOIDbase = di.getUint32()
        self.DOIDlast = self.DOIDbase + di.getUint32()
        self.DOIDnext = self.DOIDbase
        return None

    
    def handleRequestGenerates(self, di):
        zone = di.getUint32()
        for obj in self.doId2do.values():
            if obj.zone == zone:
                id = obj.doId
                if self.isLocalId(id):
                    self.send(obj.dclass.clientFormatGenerate(obj, id, zone, []))
                
            
        

    
    def handleUnexpectedMsgType(self, msgType, di):
        if msgType == CLIENT_GO_GET_LOST:
            self.handleGoGetLost(di)
        elif msgType == CLIENT_HEARTBEAT:
            self.handleServerHeartbeat(di)
        elif msgType == CLIENT_SYSTEM_MESSAGE:
            self.handleSystemMessage(di)
        elif wantOtpServer:
            if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
                self.handleGenerateWithRequired(di)
            elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
                self.handleGenerateWithRequiredOther(di)
            elif msgType == CLIENT_OBJECT_UPDATE_FIELD:
                self.handleUpdateField(di)
            elif msgType == CLIENT_OBJECT_DISABLE_RESP:
                self.handleDisable(di)
            elif msgType == CLIENT_OBJECT_DELETE_RESP:
                self.handleDelete(di)
            elif msgType == CLIENT_CREATE_OBJECT_REQUIRED:
                self.handleGenerateWithRequired(di)
            elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
                self.handleGenerateWithRequiredOther(di)
            elif msgType == CLIENT_DONE_SET_ZONE_RESP:
                self.handleSetZoneDone()
            elif msgType == CLIENT_OBJECT_LOCATION:
                self.handleObjectLocation(di)
            
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

    
    def createWithRequired(self, className, zoneId = 0, optionalFields = None):
        if self.DOIDnext >= self.DOIDlast:
            self.notify.error('Cannot allocate a distributed object ID: all IDs used up.')
            return None
        
        id = self.DOIDnext
        self.DOIDnext = self.DOIDnext + 1
        dclass = self.dclassesByName[className]
        classDef = dclass.getClassDef()
        if classDef == None:
            self.notify.error('Could not create an undefined %s object.' % dclass.getName())
        
        obj = classDef(self)
        obj.dclass = dclass
        obj.zone = zoneId
        obj.doId = id
        self.doId2do[id] = obj
        obj.generateInit()
        obj.generate()
        obj.announceGenerate()
        datagram = dclass.clientFormatGenerate(obj, id, zoneId, optionalFields)
        self.send(datagram)
        return obj

    
    def sendDisableMsg(self, doId):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_OBJECT_DISABLE)
        datagram.addUint32(doId)
        self.send(datagram)

    
    def sendDeleteMsg(self, doId):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_OBJECT_DELETE)
        datagram.addUint32(doId)
        self.send(datagram)

    
    def sendRemoveZoneMsg(self, zoneId, visibleZoneList = None):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_REMOVE_ZONE)
        datagram.addUint32(zoneId)
        if visibleZoneList is not None:
            vzl = list(visibleZoneList)
            vzl.sort()
            for zone in vzl:
                datagram.addUint32(zone)
            
        
        self.send(datagram)

    
    def sendSetShardMsg(self, shardId):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_SHARD)
        datagram.addUint32(shardId)
        self.send(datagram)

    
    def getObjectsOfClass(self, objClass):
        doDict = { }
        for (doId, do) in self.doId2do.items():
            if isinstance(do, objClass):
                doDict[doId] = do
            
        
        return doDict

    
    def getObjectsOfExactClass(self, objClass):
        doDict = { }
        for (doId, do) in self.doId2do.items():
            if do.__class__ == objClass:
                doDict[doId] = do
            
        
        return doDict

    if wantOtpServer:
        
        def sendSetZoneMsg(self, zoneId, visibleZoneList = None, parent = None):
            datagram = PyDatagram()
            datagram.addUint16(CLIENT_SET_ZONE)
            if parent is not None:
                datagram.addUint32(parent)
            else:
                datagram.addUint32(base.localAvatar.defaultShard)
            datagram.addUint32(zoneId)
            if visibleZoneList is not None:
                vzl = list(visibleZoneList)
                vzl.sort()
                for zone in vzl:
                    datagram.addUint32(zone)
                
            
            self.send(datagram)

    else:
        
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

    
    def publicServerDatagramHandler(self, msgType, di):
        if msgType == CLIENT_SET_DOID_RANGE:
            self.handleSetDOIDrange(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_RESP:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER_RESP:
            self.handleGenerateWithRequiredOther(di)
        elif msgType == CLIENT_OBJECT_UPDATE_FIELD_RESP:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_DELETE_RESP:
            self.handleDelete(di)
        elif msgType == CLIENT_OBJECT_DISABLE_RESP:
            self.handleDisable(di)
        elif msgType == CLIENT_REQUEST_GENERATES:
            self.handleRequestGenerates(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)

    if wantOtpServer:
        
        def addInterest(self, parentId, zoneId, description):
            self._interestIdAssign += 1
            self._interests[self._interestIdAssign] = description
            contextId = self._interestIdAssign
            self._sendAddInterest(contextId, parentId, zoneId)
            return contextId

        
        def removeInterest(self, contextId):
            answer = 0
            if self._interests.has_key(contextId):
                self._sendRemoveInterest(contextId)
                del self._interests[contextId]
                answer = 1
            
            return answer

        
        def alterInterest(self, contextId, parentId, zoneId, description = None):
            print 'new'
            answer = 0
            if self._interests.has_key(contextId):
                if description is not None:
                    self._interests[contextId] = description
                
                self._sendAddInterest(contextId, parentId, zoneId)
                answer = 1
            else:
                self.notify.warning('alterInterest: contextId not found: %s' % contextId)
            return answer

        
        def _sendAddInterest(self, contextId, parentId, zoneId):
            datagram = PyDatagram()
            datagram.addUint16(CLIENT_ADD_INTEREST)
            datagram.addUint16(contextId)
            datagram.addUint32(parentId)
            datagram.addUint32(zoneId)
            self.send(datagram)

        
        def _sendRemoveInterest(self, contextId):
            datagram = PyDatagram()
            datagram.addUint16(CLIENT_REMOVE_INTEREST)
            datagram.addUint16(contextId)
            self.send(datagram)

    
    
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

    
    def sendUpdateZone(self, obj, zoneId):
        id = obj.doId
        self.sendDeleteMsg(id, 1)
        obj.zone = zoneId
        self.send(obj.dclass.clientFormatGenerate(obj, id, zoneId, []))

    
    def replaceMethod(self, oldMethod, newFunction):
        return 0

    
    def getAllOfType(self, type):
        result = []
        for obj in self.doId2do.values():
            if isinstance(obj, type):
                result.append(obj)
            
        
        return result

    
    def findAnyOfType(self, type):
        for obj in self.doId2do.values():
            if isinstance(obj, type):
                return obj
            
        
        return None

    
    def isLocalId(self, id):
        if id >= self.DOIDbase:
            pass
        return id < self.DOIDlast

    
    def haveCreateAuthority(self):
        return self.DOIDlast > self.DOIDnext


