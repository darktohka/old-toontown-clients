# File: C (Python 2.2)

from PandaModules import *
from MsgTypes import *
import Task
import DirectNotifyGlobal
import ClientDistClass
import CRCache
import ConnectionRepository
import PythonUtil
import ParentMgr
import RelatedObjectMgr
import time

class ClientRepository(ConnectionRepository.ConnectionRepository):
    notify = DirectNotifyGlobal.directNotify.newCategory('ClientRepository')
    
    def __init__(self, dcFileName):
        ConnectionRepository.ConnectionRepository.__init__(self, base.config)
        self.recorder = base.recorder
        self.number2cdc = { }
        self.name2cdc = { }
        self.doId2do = { }
        self.doId2cdc = { }
        self.parseDcFile(dcFileName)
        self.cache = CRCache.CRCache()
        self.serverDelta = 0
        self.bootedIndex = None
        self.bootedText = None
        self.parentMgr = ParentMgr.ParentMgr()
        self.relatedObjectMgr = RelatedObjectMgr.RelatedObjectMgr(self)

    
    def abruptCleanup(self):
        self.relatedObjectMgr.abortAllRequests()

    
    def setServerDelta(self, delta):
        self.serverDelta = delta

    
    def getServerDelta(self):
        return self.serverDelta

    
    def getServerTimeOfDay(self):
        return time.time() + self.serverDelta

    
    def parseDcFile(self, dcFileName):
        self.dcFile = DCFile()
        readResult = self.dcFile.read(dcFileName)
        if not readResult:
            self.notify.error('Could not read dcfile: %s' % dcFileName.cStr())
        
        self.hashVal = self.dcFile.getHash()
        return self.parseDcClasses(self.dcFile)

    
    def parseDcClasses(self, dcFile):
        numClasses = dcFile.getNumClasses()
        for i in range(0, numClasses):
            dcClass = dcFile.getClass(i)
            clientDistClass = ClientDistClass.ClientDistClass(dcClass)
            self.number2cdc[dcClass.getNumber()] = clientDistClass
            self.name2cdc[dcClass.getName()] = clientDistClass
        

    
    def handleGenerateWithRequired(self, di):
        classId = di.getArg(STUint16)
        doId = di.getArg(STUint32)
        cdc = self.number2cdc[classId]
        distObj = self.generateWithRequiredFields(cdc, doId, di)

    
    def handleGenerateWithRequiredOther(self, di):
        classId = di.getArg(STUint16)
        doId = di.getArg(STUint32)
        cdc = self.number2cdc[classId]
        distObj = self.generateWithRequiredOtherFields(cdc, doId, di)

    
    def handleQuietZoneGenerateWithRequired(self, di):
        classId = di.getArg(STUint16)
        doId = di.getArg(STUint32)
        cdc = self.number2cdc[classId]
        if cdc.constructor.neverDisable:
            distObj = self.generateWithRequiredFields(cdc, doId, di)
        

    
    def handleQuietZoneGenerateWithRequiredOther(self, di):
        classId = di.getArg(STUint16)
        doId = di.getArg(STUint32)
        cdc = self.number2cdc[classId]
        if cdc.constructor.neverDisable:
            distObj = self.generateWithRequiredOtherFields(cdc, doId, di)
        

    
    def generateWithRequiredFields(self, cdc, doId, di):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            distObj.generate()
            distObj.updateRequiredFields(cdc, di)
        elif self.cache.contains(doId):
            distObj = self.cache.retrieve(doId)
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generate()
            distObj.updateRequiredFields(cdc, di)
        else:
            distObj = cdc.constructor(self)
            distObj.doId = doId
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generateInit()
            distObj.generate()
            distObj.updateRequiredFields(cdc, di)
        return distObj

    
    def generateWithRequiredOtherFields(self, cdc, doId, di):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            distObj.generate()
            distObj.updateRequiredOtherFields(cdc, di)
        elif self.cache.contains(doId):
            distObj = self.cache.retrieve(doId)
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generate()
            distObj.updateRequiredOtherFields(cdc, di)
        elif cdc.constructor == None:
            self.notify.error('Could not create an undefined %s object.' % cdc.name)
        
        distObj = cdc.constructor(self)
        distObj.doId = doId
        self.doId2do[doId] = distObj
        self.doId2cdc[doId] = cdc
        distObj.generateInit()
        distObj.generate()
        distObj.updateRequiredOtherFields(cdc, di)
        return distObj

    
    def handleDisable(self, di):
        doId = di.getArg(STUint32)
        self.disableDoId(doId)

    
    def disableDoId(self, doId):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            del self.doId2do[doId]
            del self.doId2cdc[doId]
            if distObj.getCacheable():
                self.cache.cache(distObj)
            else:
                distObj.deleteOrDelay()
        else:
            ClientRepository.notify.warning('Disable failed. DistObj ' + str(doId) + ' is not in dictionary')

    
    def handleDelete(self, di):
        doId = di.getArg(STUint32)
        self.deleteObject(doId)

    
    def deleteObject(self, doId):
        if self.doId2do.has_key(doId):
            obj = self.doId2do[doId]
            del self.doId2do[doId]
            del self.doId2cdc[doId]
            obj.deleteOrDelay()
        elif self.cache.contains(doId):
            self.cache.delete(doId)
        else:
            ClientRepository.notify.warning('Asked to delete non-existent DistObj ' + str(doId))

    
    def handleUpdateField(self, di):
        doId = di.getArg(STUint32)
        if self.rsDoReport:
            self.rsUpdateObjs[doId] = self.rsUpdateObjs.get(doId, 0) + 1
        
        do = self.doId2do.get(doId)
        cdc = self.doId2cdc.get(doId)
        if do != None and cdc != None:
            cdc.updateField(do, di)
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
        

    
    def handleUnexpectedMsgType(self, msgType, di):
        if msgType == CLIENT_GO_GET_LOST:
            self.handleGoGetLost(di)
        elif msgType == CLIENT_HEARTBEAT:
            self.handleServerHeartbeat(di)
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
        datagram = Datagram()
        datagram.addUint16(CLIENT_SET_SHARD)
        datagram.addUint32(shardId)
        self.send(datagram)

    
    def sendSetZoneMsg(self, zoneId, visibleZoneList = None):
        datagram = Datagram()
        datagram.addUint16(CLIENT_SET_ZONE)
        datagram.addUint32(zoneId)
        if visibleZoneList is not None:
            vzl = list(visibleZoneList)
            vzl.sort()
            for zone in vzl:
                datagram.addUint32(zone)
            
        
        self.send(datagram)

    
    def sendUpdate(self, do, fieldName, args, sendToId = None):
        doId = do.doId
        cdc = self.doId2cdc.get(doId, None)
        if cdc:
            cdc.sendUpdate(self, do, fieldName, args, sendToId)
        

    
    def replaceMethod(self, oldMethod, newFunction):
        foundIt = 0
        import new
        for cdc in self.number2cdc.values():
            for cdu in cdc.allCDU:
                method = cdu.func
                if method and method.im_func == oldMethod:
                    newMethod = new.instancemethod(newFunction, method.im_self, method.im_class)
                    cdu.func = newMethod
                    foundIt = 1
                
            
        
        return foundIt

    
    def getAllOfType(self, type):
        result = []
        for obj in self.doId2do.values():
            if isinstance(obj, type):
                result.append(obj)
            
        
        return result


