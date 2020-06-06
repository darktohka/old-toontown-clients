# File: C (Python 2.2)

from pandac.PandaModules import *
from direct.task import Task
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject
from PyDatagram import PyDatagram
from PyDatagramIterator import PyDatagramIterator
import types
import imp

class ConnectionRepository(DirectObject.DirectObject, CConnectionRepository):
    notify = DirectNotifyGlobal.directNotify.newCategory('ConnectionRepository')
    taskPriority = -30
    
    def __init__(self, config):
        DirectObject.DirectObject.__init__(self)
        CConnectionRepository.__init__(self)
        self.setPythonRepository(self)
        self.config = config
        self.connectMethod = self.config.GetString('connect-method', 'default')
        self.connectHttp = None
        self.http = None
        self._ConnectionRepository__di = PyDatagramIterator()
        self.recorder = None
        self.dcSuffix = ''

    
    def readDCFile(self, dcFileNames = None):
        dcFile = self.getDcFile()
        dcFile.clear()
        self.dclassesByName = { }
        self.dclassesByNumber = { }
        self.hashVal = 0
        dcImports = { }
        if dcFileNames == None:
            readResult = dcFile.readAll()
            if not readResult:
                self.notify.error('Could not read dc file.')
            
        else:
            for dcFileName in dcFileNames:
                readResult = dcFile.read(Filename(dcFileName))
                if not readResult:
                    self.notify.error('Could not read dc file: %s' % dcFileName)
                
            
        self.hashVal = dcFile.getHash()
        for n in range(dcFile.getNumImportModules()):
            moduleName = dcFile.getImportModule(n)
            suffix = moduleName.split('/')
            moduleName = suffix[0]
            if self.dcSuffix and self.dcSuffix in suffix[1:]:
                moduleName += self.dcSuffix
            
            importSymbols = []
            for i in range(dcFile.getNumImportSymbols(n)):
                symbolName = dcFile.getImportSymbol(n, i)
                suffix = symbolName.split('/')
                symbolName = suffix[0]
                if self.dcSuffix and self.dcSuffix in suffix[1:]:
                    symbolName += self.dcSuffix
                
                importSymbols.append(symbolName)
            
            self.importModule(dcImports, moduleName, importSymbols)
        
        for i in range(dcFile.getNumClasses()):
            dclass = dcFile.getClass(i)
            number = dclass.getNumber()
            className = dclass.getName() + self.dcSuffix
            classDef = dcImports.get(className)
            if classDef == None:
                self.notify.info('No class definition for %s.' % className)
            elif type(classDef) == types.ModuleType:
                if not hasattr(classDef, className):
                    self.notify.error('Module %s does not define class %s.' % (className, className))
                
                classDef = getattr(classDef, className)
            
            if type(classDef) != types.ClassType:
                self.notify.error('Symbol %s is not a class name.' % className)
            else:
                dclass.setClassDef(classDef)
            self.dclassesByName[className] = dclass
            if number >= 0:
                self.dclassesByNumber[number] = dclass
            
        

    
    def importModule(self, dcImports, moduleName, importSymbols):
        module = __import__(moduleName, globals(), locals(), importSymbols)
        if importSymbols:
            if importSymbols == [
                '*']:
                if hasattr(module, '__all__'):
                    importSymbols = module.__all__
                else:
                    importSymbols = module.__dict__.keys()
            
            for symbolName in importSymbols:
                if hasattr(module, symbolName):
                    dcImports[symbolName] = getattr(module, symbolName)
                else:
                    raise StandardError, 'Symbol %s not defined in module %s.' % (symbolName, moduleName)
            
        else:
            components = moduleName.split('.')
            dcImports[components[0]] = module

    
    def connect(self, serverList, successCallback = None, successArgs = [], failureCallback = None, failureArgs = []):
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
        else:
            for url in serverList:
                self.notify.info('Connecting to %s via NSPR interface.' % url.cStr())
                if self.tryConnectNspr(url):
                    self.startReaderPollTask()
                    if successCallback:
                        successCallback(*successArgs)
                    
                    return None
                
            
            if failureCallback:
                failureCallback(0, '', *failureArgs)
            

    
    def disconnect(self):
        self.notify.info('Closing connection to server.')
        CConnectionRepository.disconnect(self)
        self.stopReaderPollTask()

    
    def httpConnectCallback(self, ch, serverList, serverIndex, successCallback, successArgs, failureCallback, failureArgs):
        if ch.isConnectionReady():
            self.setConnectionHttp(ch)
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
        self.accept(CConnectionRepository.getOverflowEventName(), self.handleReaderOverflow)
        taskMgr.add(self.readerPollUntilEmpty, 'readerPollTask', priority = self.taskPriority)

    
    def stopReaderPollTask(self):
        taskMgr.remove('readerPollTask')
        self.ignore(CConnectionRepository.getOverflowEventName())

    
    def readerPollUntilEmpty(self, task):
        while self.readerPollOnce():
            pass
        return Task.cont

    
    def readerPollOnce(self):
        if self.checkDatagram():
            self.getDatagramIterator(self._ConnectionRepository__di)
            self.handleDatagram(self._ConnectionRepository__di)
            return 1
        
        if not self.isConnected():
            self.stopReaderPollTask()
            self.lostConnection()
        
        return 0

    
    def handleReaderOverflow(self):
        pass

    
    def lostConnection(self):
        self.notify.warning('Lost connection to gameserver.')

    
    def handleDatagram(self, di):
        pass

    
    def send(self, datagram):
        if self.notify.getDebug():
            print 'ConnectionRepository sending datagram:'
            datagram.dumpHex(ostream)
        
        self.sendDatagram(datagram)

    
    def pullNetworkPlug(self):
        self.notify.warning('*** SIMULATING A NETWORK-PLUG-PULL ***')
        self.setSimulatedDisconnect(1)

    
    def networkPlugPulled(self):
        return self.getSimulatedDisconnect()

    
    def restoreNetworkPlug(self):
        if self.networkPlugPulled():
            self.notify.info('*** RESTORING SIMULATED PULLED-NETWORK-PLUG ***')
            self.setSimulatedDisconnect(0)
        

    
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


