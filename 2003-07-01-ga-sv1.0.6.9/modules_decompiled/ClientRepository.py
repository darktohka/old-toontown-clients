# File: C (Python 2.2)

from PandaModules import *
from TaskManagerGlobal import *
from MsgTypes import *
from ShowBaseGlobal import *
import Task
import DirectNotifyGlobal
import ClientDistClass
import CRCache
import DirectObject

class ClientRepository(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('ClientRepository')
    TASK_PRIORITY = -30
    
    def __init__(self, dcFileName):
        self.number2cdc = { }
        self.name2cdc = { }
        self.doId2do = { }
        self.doId2cdc = { }
        self.parseDcFile(dcFileName)
        self.cache = CRCache.CRCache()
        self.serverDelta = 0
        self.connectMethod = base.config.GetString('connect-method', 'default')
        self.connectHttp = None
        self.qcm = None
        self.bootedIndex = None
        self.bootedText = None
        self.tcpConn = None
        self.rsDatagramCount = 0
        self.rsUpdateObjs = { }
        self.rsLastUpdate = 0
        self.rsDoReport = base.config.GetBool('reader-statistics', 0)
        self.rsUpdateInterval = base.config.GetDouble('reader-statistics-interval', 10)
        return None

    
    def setServerDelta(self, delta):
        self.serverDelta = delta

    
    def getServerDelta(self):
        return self.serverDelta

    
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
        
        return None

    
    def connect(self, serverList, allowProxy, successCallback = None, successArgs = [], failureCallback = None, failureArgs = []):
        hasProxy = 0
        if allowProxy:
            proxies = self.http.getProxiesForUrl(serverList[0])
            hasProxy = proxies != ''
        
        if hasProxy:
            self.notify.info('Connecting to gameserver via proxy: %s' % proxies)
        else:
            self.notify.info('Connecting to gameserver directly (no proxy).')
        if self.connectMethod == 'http':
            self.connectHttp = 1
        elif self.connectMethod == 'nspr':
            self.connectHttp = 0
        elif not hasProxy:
            pass
        self.connectHttp = serverList[0].isSsl()
        self.bootedIndex = None
        self.bootedText = None
        if self.connectHttp:
            ch = self.http.makeChannel(0)
            
            try:
                ch.setAllowProxy(allowProxy)
            except:
                pass

            self.httpConnectCallback(ch, serverList, 0, hasProxy, successCallback, successArgs, failureCallback, failureArgs)
        elif self.qcm == None:
            self.qcm = QueuedConnectionManager()
            self.cw = ConnectionWriter(self.qcm, 0)
            self.qcr = QueuedConnectionReader(self.qcm, 0)
            minLag = config.GetFloat('min-lag', 0.0)
            maxLag = config.GetFloat('max-lag', 0.0)
            if minLag or maxLag:
                self.qcr.startDelay(minLag, maxLag)
            
        
        gameServerTimeoutMs = base.config.GetInt('game-server-timeout-ms', 20000)
        for url in serverList:
            self.notify.info('Connecting to %s via NSPR interface.' % url.cStr())
            self.tcpConn = self.qcm.openTCPClientConnection(url.getServer(), url.getPort(), gameServerTimeoutMs)
            if self.tcpConn:
                self.tcpConn.setNoDelay(1)
                self.qcr.addConnection(self.tcpConn)
                self.startReaderPollTask()
                if successCallback:
                    successCallback(*successArgs)
                
                return None
            
        
        if failureCallback:
            failureCallback(hasProxy, 0, *failureArgs)
        

    
    def disconnect(self):
        self.notify.info('Closing connection to server.')
        if self.tcpConn != None:
            if self.connectHttp:
                self.tcpConn.close()
            else:
                self.qcm.closeConnection(self.tcpConn)
            self.tcpConn = None
        
        self.stopReaderPollTask()

    
    def httpConnectCallback(self, ch, serverList, serverIndex, hasProxy, successCallback, successArgs, failureCallback, failureArgs):
        if ch.isConnectionReady():
            self.tcpConn = ch.getConnection()
            self.tcpConn.userManagesMemory = 1
            self.startReaderPollTask()
            if successCallback:
                successCallback(*successArgs)
            
        elif serverIndex < len(serverList):
            url = serverList[serverIndex]
            self.notify.info('Connecting to %s via HTTP interface.' % url.cStr())
            ch.beginConnectTo(DocumentSpec(url))
            ch.spawnTask(name = 'connect-to-server', callback = self.httpConnectCallback, extraArgs = [
                ch,
                serverList,
                serverIndex + 1,
                hasProxy,
                successCallback,
                successArgs,
                failureCallback,
                failureArgs])
        elif failureCallback:
            failureCallback(hasProxy, ch.getStatusCode(), *failureArgs)
        

    
    def startReaderPollTask(self):
        self.stopReaderPollTask()
        taskMgr.add(self.readerPollUntilEmpty, 'readerPollTask', priority = self.TASK_PRIORITY)
        return None

    
    def stopReaderPollTask(self):
        taskMgr.remove('readerPollTask')
        return None

    
    def readerPollUntilEmpty(self, task):
        while self.readerPollOnce():
            pass
        return Task.cont

    
    def readerPollOnce(self):
        if not (self.tcpConn):
            return 0
        
        self.tcpConn.considerFlush()
        if self.rsDoReport:
            self.reportReaderStatistics()
        
        if self.connectHttp:
            datagram = Datagram()
            if self.tcpConn.receiveDatagram(datagram):
                if self.rsDoReport:
                    self.rsDatagramCount += 1
                
                self.handleDatagram(datagram)
                return 1
            
            if self.tcpConn.isClosed():
                self.tcpConn = None
                self.stopReaderPollTask()
                self.loginFSM.request('noConnection')
            
            return 0
        else:
            self.ensureValidConnection()
            if self.qcr.dataAvailable():
                datagram = NetDatagram()
                if self.qcr.getData(datagram):
                    if self.rsDoReport:
                        self.rsDatagramCount += 1
                    
                    self.handleDatagram(datagram)
                    return 1
                
            
            return 0

    
    def ensureValidConnection(self):
        if self.connectHttp:
            pass
        1
        if self.qcm.resetConnectionAvailable():
            resetConnectionPointer = PointerToConnection()
            if self.qcm.getResetConnection(resetConnectionPointer):
                resetConn = resetConnectionPointer.p()
                self.qcm.closeConnection(resetConn)
                self.restoreNetworkPlug()
                if self.tcpConn.this == resetConn.this:
                    self.tcpConn = None
                    self.stopReaderPollTask()
                    self.loginFSM.request('noConnection')
                else:
                    self.notify.warning('Lost unknown connection.')
            
        
        return None

    
    def handleDatagram(self, datagram):
        pass

    
    def reportReaderStatistics(self):
        now = globalClock.getRealTime()
        if now - self.rsLastUpdate < self.rsUpdateInterval:
            return None
        
        self.rsLastUpdate = now
        self.notify.info('Received %s datagrams' % self.rsDatagramCount)
        if self.rsUpdateObjs:
            self.notify.info('Updates: %s' % self.rsUpdateObjs)
        
        self.rsDatagramCount = 0
        self.rsUpdateObjs = { }

    
    def handleGenerateWithRequired(self, di):
        classId = di.getArg(STUint16)
        doId = di.getArg(STUint32)
        cdc = self.number2cdc[classId]
        distObj = self.generateWithRequiredFields(cdc, doId, di)
        return None

    
    def handleGenerateWithRequiredOther(self, di):
        classId = di.getArg(STUint16)
        doId = di.getArg(STUint32)
        cdc = self.number2cdc[classId]
        distObj = self.generateWithRequiredOtherFields(cdc, doId, di)
        return None

    
    def handleQuietZoneGenerateWithRequired(self, di):
        classId = di.getArg(STUint16)
        doId = di.getArg(STUint32)
        cdc = self.number2cdc[classId]
        if cdc.constructor.neverDisable:
            distObj = self.generateWithRequiredFields(cdc, doId, di)
        
        return None

    
    def handleQuietZoneGenerateWithRequiredOther(self, di):
        classId = di.getArg(STUint16)
        doId = di.getArg(STUint32)
        cdc = self.number2cdc[classId]
        if cdc.constructor.neverDisable:
            distObj = self.generateWithRequiredOtherFields(cdc, doId, di)
        
        return None

    
    def generateWithRequiredFields(self, cdc, doId, di):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            distObj.generate()
            distObj.updateRequiredFields(cdc, di)
            distObj.announceGenerate()
        elif self.cache.contains(doId):
            distObj = self.cache.retrieve(doId)
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generate()
            distObj.updateRequiredFields(cdc, di)
            distObj.announceGenerate()
        else:
            distObj = cdc.constructor(self)
            distObj.doId = doId
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generateInit()
            distObj.generate()
            distObj.updateRequiredFields(cdc, di)
            distObj.announceGenerate()
        return distObj

    
    def generateWithRequiredOtherFields(self, cdc, doId, di):
        if self.doId2do.has_key(doId):
            distObj = self.doId2do[doId]
            distObj.generate()
            distObj.updateRequiredOtherFields(cdc, di)
            distObj.announceGenerate()
        elif self.cache.contains(doId):
            distObj = self.cache.retrieve(doId)
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generate()
            distObj.updateRequiredOtherFields(cdc, di)
            distObj.announceGenerate()
        else:
            distObj = cdc.constructor(self)
            distObj.doId = doId
            self.doId2do[doId] = distObj
            self.doId2cdc[doId] = cdc
            distObj.generateInit()
            distObj.generate()
            distObj.updateRequiredOtherFields(cdc, di)
            distObj.announceGenerate()
        return distObj

    
    def handleDisable(self, di):
        doId = di.getArg(STUint32)
        self.disableDoId(doId)
        return None

    
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
        return None

    
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
        return None

    
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
        return None

    
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
        return None

    
    def sendSetShardMsg(self, shardId):
        datagram = Datagram()
        datagram.addUint16(CLIENT_SET_SHARD)
        datagram.addUint32(shardId)
        self.send(datagram)
        return None

    
    def sendSetZoneMsg(self, zoneId):
        datagram = Datagram()
        datagram.addUint16(CLIENT_SET_ZONE)
        datagram.addUint16(zoneId)
        self.send(datagram)
        return None

    
    def sendUpdate(self, do, fieldName, args, sendToId = None):
        doId = do.doId
        cdc = self.doId2cdc.get(doId, None)
        if cdc:
            cdc.sendUpdate(self, do, fieldName, args, sendToId)
        

    
    def send(self, datagram):
        if self.notify.getDebug():
            print 'ClientRepository sending datagram:'
            datagram.dumpHex(ostream)
        
        if not (self.tcpConn):
            self.notify.warning('Unable to send message after connection is closed.')
            return None
        
        if self.connectHttp:
            if not self.tcpConn.sendDatagram(datagram):
                self.notify.warning('Could not send datagram.')
            
        else:
            self.cw.send(datagram, self.tcpConn)
        return None

    
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

    
    def pullNetworkPlug(self):
        self.restoreNetworkPlug()
        self.notify.warning('*** SIMULATING A NETWORK-PLUG-PULL ***')
        self.hijackedTcpConn = self.tcpConn
        self.tcpConn = None

    
    def networkPlugPulled(self):
        return hasattr(self, 'hijackedTcpConn')

    
    def restoreNetworkPlug(self):
        if self.networkPlugPulled():
            self.notify.info('*** RESTORING SIMULATED PULLED-NETWORK-PLUG ***')
            self.tcpConn = self.hijackedTcpConn
            del self.hijackedTcpConn
        

    
    def getAllOfType(self, type):
        result = []
        for obj in self.doId2do.values():
            if isinstance(obj, type):
                result.append(obj)
            
        
        return result


