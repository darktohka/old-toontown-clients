# File: C (Python 2.2)

from PandaModules import *
import Task
import DirectNotifyGlobal
import DirectObject

class ConnectionRepository(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('ConnectionRepository')
    taskPriority = -30
    
    def __init__(self, config):
        DirectObject.DirectObject.__init__(self)
        self.config = config
        self.connectMethod = self.config.GetString('connect-method', 'default')
        self.connectHttp = None
        self.http = None
        self.qcm = None
        self.cw = None
        self.tcpConn = None
        self.recorder = None
        self.rsDatagramCount = 0
        self.rsUpdateObjs = { }
        self.rsLastUpdate = 0
        self.rsDoReport = self.config.GetBool('reader-statistics', 0)
        self.rsUpdateInterval = self.config.GetDouble('reader-statistics-interval', 10)

    
    def connect(self, serverList, successCallback = None, successArgs = [], failureCallback = None, failureArgs = []):
        if self.recorder and self.recorder.isPlaying():
            self.notify.info('Not connecting to gameserver; using playback data instead.')
            self.connectHttp = 1
            self.tcpConn = SocketStreamRecorder()
            self.recorder.addRecorder('gameserver', self.tcpConn)
            self.startReaderPollTask()
            if successCallback:
                successCallback(*successArgs)
            
            return None
        
        hasProxy = 0
        if self.checkHttp():
            proxies = self.http.getProxiesForUrl(serverList[0])
            hasProxy = proxies != 'DIRECT'
        
        if hasProxy:
            self.notify.info('Connecting to gameserver via proxy list: %s' % proxies)
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
            self.httpConnectCallback(ch, serverList, 0, successCallback, successArgs, failureCallback, failureArgs)
        elif self.qcm == None:
            self.qcm = QueuedConnectionManager()
        
        if self.cw == None:
            self.cw = ConnectionWriter(self.qcm, 0)
            self.qcr = QueuedConnectionReader(self.qcm, 0)
            minLag = self.config.GetFloat('min-lag', 0.0)
            maxLag = self.config.GetFloat('max-lag', 0.0)
            if minLag or maxLag:
                self.qcr.startDelay(minLag, maxLag)
            
        
        gameServerTimeoutMs = self.config.GetInt('game-server-timeout-ms', 20000)
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
            failureCallback(0, '', *failureArgs)
        

    
    def disconnect(self):
        self.notify.info('Closing connection to server.')
        if self.tcpConn != None:
            if self.connectHttp:
                self.tcpConn.close()
            else:
                self.qcm.closeConnection(self.tcpConn)
            self.tcpConn = None
        
        self.stopReaderPollTask()

    
    def httpConnectCallback(self, ch, serverList, serverIndex, successCallback, successArgs, failureCallback, failureArgs):
        if ch.isConnectionReady():
            self.tcpConn = ch.getConnection()
            self.tcpConn.userManagesMemory = 1
            if self.recorder:
                stream = SocketStreamRecorder(self.tcpConn, 1)
                self.recorder.addRecorder('gameserver', stream)
                self.tcpConn.userManagesMemory = 0
                self.tcpConn = stream
            
            self.startReaderPollTask()
            if successCallback:
                successCallback(*successArgs)
            
        elif serverIndex < len(serverList):
            url = serverList[serverIndex]
            self.notify.info('Connecting to %s via HTTP interface.' % url.cStr())
            ch.preserveStatus()
            ch.beginConnectTo(DocumentSpec(url))
            ch.spawnTask(name = 'connect-to-server', callback = self.httpConnectCallback, extraArgs = [
                ch,
                serverList,
                serverIndex + 1,
                successCallback,
                successArgs,
                failureCallback,
                failureArgs])
        elif failureCallback:
            failureCallback(ch.getStatusCode(), ch.getStatusString(), *failureArgs)
        

    
    def checkHttp(self):
        if self.http == None:
            
            try:
                self.http = HTTPClient()
            except:
                pass

        
        return self.http

    
    def startReaderPollTask(self):
        self.stopReaderPollTask()
        taskMgr.add(self.readerPollUntilEmpty, 'readerPollTask', priority = self.taskPriority)

    
    def stopReaderPollTask(self):
        taskMgr.remove('readerPollTask')

    
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
                self.lostConnection()
            
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

    
    def flush(self):
        if self.tcpConn:
            self.tcpConn.flush()
        

    
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
                    self.lostConnection()
                else:
                    self.notify.warning('Lost unknown connection.')
            
        

    
    def lostConnection(self):
        self.notify.warning('Lost connection to gameserver.')

    
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

    
    def send(self, datagram):
        if not (self.tcpConn):
            self.notify.warning('Unable to send message after connection is closed.')
            return None
        
        if self.connectHttp:
            if not self.tcpConn.sendDatagram(datagram):
                self.notify.warning('Could not send datagram.')
            
        else:
            self.cw.send(datagram, self.tcpConn)

    
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
        

    
    def doFind(self, str):
        for value in self.doId2do.values():
            if `value`.find(str) >= 0:
                return value
            
        

    
    def doFindAll(self, str):
        matches = []
        for value in self.doId2do.values():
            if `value`.find(str) >= 0:
                matches.append(value)
            
        
        return matches


