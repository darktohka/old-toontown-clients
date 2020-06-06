# File: L (Python 2.2)

import sys
sys.path = [
    '']
import os
import time
import types
import string
LauncherPhases = [
    3,
    3.5,
    4,
    5,
    5.5,
    6,
    7,
    8]
ltime = time.localtime()
logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000, ltime[1], ltime[2], ltime[3], ltime[4], ltime[5])
logfile = 'toontown-' + logSuffix + '.log'

class LogAndOutput:
    
    def __init__(self, orig, log):
        self.orig = orig
        self.log = log

    
    def write(self, str):
        self.log.write(str)
        self.log.flush()
        self.orig.write(str)
        self.orig.flush()


log = open(logfile, 'a')
logOut = LogAndOutput(sys.__stdout__, log)
logErr = LogAndOutput(sys.__stderr__, log)
sys.stdout = logOut
sys.stderr = logErr
print '\n\nStarting Toontown...'
print 'Current time: ' + time.asctime(time.localtime(time.time())) + ' ' + time.tzname[0]
print 'sys.path = ', sys.path
print 'sys.argv = ', sys.argv
if len(sys.argv) >= 7:
    Configrc_args = sys.argv[6]
    print "generating configrc using: '" + Configrc_args + "'"
else:
    Configrc_args = ''
    print 'generating standard configrc'
if os.environ.has_key('CONFIG_CONFIG'):
    print 'CONFIG_CONFIG is set to: ' + os.environ['CONFIG_CONFIG']
    print 'Resetting CONFIG_CONFIG'

os.environ['CONFIG_CONFIG'] = ':_:configpath_:configname_Configrc.exe:configargs_-stdout ' + Configrc_args
import libdtoolconfig
import libpandaexpress
from libpandaexpressModules import *
launcherConfig = getConfigExpress()
__builtins__['config'] = launcherConfig
nout = MultiplexStream()
Notify.ptr().setOstreamPtr(nout, 0)
nout.addFile(Filename(logfile))
nout.addStandardOutput()
nout.addSystemDebug()
import win32api
from MessengerGlobal import *
from DirectObject import *
from EventManagerGlobal import *
from TaskManagerGlobal import *
import Task
from DirectNotifyGlobal import *
import Localizer

class Launcher(DirectObject):
    VerifyFiles = launcherConfig.GetInt('launcher-verify', 1)
    ServerVersion = launcherConfig.GetString('server-version', 'no_version_set')
    UserUpdateDelay = launcherConfig.GetFloat('launcher-user-update-delay', 0.5)
    TELEMETRY_BANDWIDTH = launcherConfig.GetInt('launcher-telemetry-bandwidth', 2000)
    INCREASE_THRESHOLD = launcherConfig.GetFloat('launcher-increase-threshold', 0.75)
    DECREASE_THRESHOLD = launcherConfig.GetFloat('launcher-decrease-threshold', 0.5)
    BPS_WINDOW = launcherConfig.GetFloat('launcher-bps-window', 8.0)
    DECREASE_BANDWIDTH = launcherConfig.GetBool('launcher-decrease-bandwidth', 1)
    MAX_BANDWIDTH = launcherConfig.GetInt('launcher-max-bandwidth', 0)
    BANDWIDTH_ARRAY = [
        1800,
        3600,
        4200,
        6600,
        8000,
        12000,
        16000,
        24000,
        32000,
        48000,
        72000,
        96000,
        128000,
        192000,
        250000,
        500000,
        750000,
        1000000,
        1250000,
        1500000,
        1750000,
        2000000,
        3000000,
        4000000,
        6000000,
        8000000,
        10000000,
        12000000,
        14000000,
        16000000,
        24000000,
        32000000,
        48000000,
        64000000,
        96000000,
        128000000,
        256000000,
        512000000,
        1024000000]
    win32con_FILE_PERSISTENT_ACLS = 8
    
    def __init__(self):
        self.notify = directNotify.newCategory('Launcher')
        self.clock = ClockObject()
        configDownloadServer = launcherConfig.GetString('download-server', '')
        if configDownloadServer:
            self.downloadServer = URLSpec(configDownloadServer, 1)
            self.notify.info('Overriding downloadServer to %s.' % self.downloadServer.cStr())
        else:
            self.downloadServer = downloadServer
        self.gameServer = gameServer
        self.accountServer = accountServer
        self.testServerFlag = testServerFlag
        self.notify.info('isTestServer: %s' % self.testServerFlag)
        self.downloadServerRetries = 3
        self.multifileRetries = 1
        self.curMultifileRetry = 0
        self.downloadServerRetryPause = 1
        self.bandwidthIndex = len(self.BANDWIDTH_ARRAY) - 1
        self.everIncreasedBandwidth = 0
        self.goUserName = ''
        self.downloadPercentage = 90
        self.decompressPercentage = 5
        self.extractPercentage = 4
        if self.testServerFlag:
            self.toontownRegistryKey = 'Software\\Disney\\Disney Online\\ToontownTest'
        else:
            self.toontownRegistryKey = 'Software\\Disney\\Disney Online\\Toontown'
        self.game1DoneKey = 'GAME1_DONE'
        self.game2DoneKey = 'GAME2_DONE'
        self.tutorialCompleteKey = 'TUTORIAL_DONE'
        self.installDirKey = 'INSTALL_DIR'
        self.pandaWindowOpenKey = 'PANDA_WINDOW_OPEN'
        self.pandaErrorCodeKey = 'PANDA_ERROR_CODE'
        self.toontownBlueKey = 'TOONTOWN_BLUE'
        self.toontownPlayTokenKey = 'TOONTOWN_PLAYTOKEN'
        self.launcherMessageKey = 'LAUNCHER_MESSAGE'
        self.newInstallationKey = 'IS_NEW_INSTALLATION'
        self.lastLoginKey = 'LAST_LOGIN'
        self.userLoggedInKey = 'USER_LOGGED_IN'
        self.paidUserLoggedInKey = 'PAID_USER_LOGGED_IN'
        self.referrerKey = 'REFERRER_CODE'
        self.periodTimeRemainingKey = 'PERIOD_TIME_REMAINING'
        self.periodNameKey = 'PERIOD_NAME'
        self.swidKey = 'SWID'
        self.proxyServerKey = 'PROXY_SERVER'
        self.proxyDirectHostsKey = 'PROXY_DIRECT_HOSTS'
        self.lastLauncherMsg = None
        self.topDir = self.getRegistry(self.installDirKey, '.')
        self.topDir = string.replace(self.topDir, '\\', '/')
        if self.topDir[-1:] != '/':
            self.topDir = self.topDir + '/'
        
        self.notify.debug('init: Launcher found install dir: ' + self.topDir)
        self.dbDir = self.topDir
        self.patchDir = self.topDir
        self.mfDir = self.topDir
        self.clientDbFilename = 'client.ddb'
        self.compClientDbFilename = self.clientDbFilename + '.pz'
        self.serverDbFilename = 'server.ddb'
        self.compServerDbFilename = self.serverDbFilename + '.pz'
        self.serverDbFilePath = self.compServerDbFilename
        self.clientStarterDbFilePath = self.compClientDbFilename
        self.progressFilename = 'progress'
        self.overallComplete = 0
        self.progressSoFar = 0
        self.patchExtension = 'pch'
        self.firstPhase = LauncherPhases[0]
        self.finalPhase = LauncherPhases[-1]
        self.showPhase = 3.5
        self.numPhases = len(LauncherPhases)
        self.phaseCompleteMap = { }
        self.phaseNewDownload = { }
        self.phaseOverallMap = { }
        tmpOverallMap = [
            0.27000000000000002,
            0.16,
            0.13,
            0.23000000000000001,
            0.080000000000000002,
            0.059999999999999998,
            0.02,
            0.050000000000000003]
        tmpPhase3Map = [
            0.001,
            0.996,
            0.0,
            0.0,
            0.0030000000000000001]
        phaseIdx = 0
        for phase in LauncherPhases:
            self.phaseCompleteMap[phase] = 0
            self.phaseNewDownload[phase] = 0
            self.phaseOverallMap[phase] = tmpOverallMap[phaseIdx]
            phaseIdx += 1
        
        self.patchList = []
        self.reextractList = []
        self.byteRate = 0
        self.byteRateRequested = 0
        self.resetBytesPerSecond()
        self.dldb = None
        self.currentMfname = None
        self.currentPhase = 0
        self.currentPhaseIndex = 1
        self.currentPhaseName = Localizer.LauncherPhaseNames[self.currentPhase]
        if self.ServerVersion == 'no_version_set':
            self.setPandaErrorCode(10)
            self.notify.info('Aborting, Configrc did not run!')
            sys.exit()
        
        self.launcherMessage(Localizer.LauncherStartingMessage)
        self.http = HTTPClient()
        if self.http.getProxySpec() == '':
            self.http.setProxySpec(self.getRegistry(self.proxyServerKey, ''))
            self.http.setDirectHostSpec(self.getRegistry(self.proxyDirectHostsKey, ''))
        
        self.notify.info('Proxy spec is: %s' % self.http.getProxySpec())
        if self.http.getDirectHostSpec() != '':
            self.notify.info('Direct hosts list is: %s' % self.http.getDirectHostSpec())
        
        self.httpChannel = self.http.makeChannel(0)
        self.httpChannel.setDownloadThrottle(1)
        proxies = self.http.getProxiesForUrl(self.downloadServer)
        if proxies == 'DIRECT':
            self.notify.info('No proxy for download.')
        else:
            self.notify.info('Download proxy: %s' % proxies)
        connOk = self.httpChannel.getHeader(DocumentSpec(self.downloadServer))
        statusCode = self.httpChannel.getStatusCode()
        statusString = self.httpChannel.getStatusString()
        if not connOk:
            self.notify.warning('Could not contact download server at %s' % self.downloadServer.cStr())
            self.notify.warning('Status code = %s %s' % (statusCode, statusString))
            if statusCode == 407 or statusCode == 1407:
                self.setPandaErrorCode(3)
            elif statusCode == 0:
                self.setPandaErrorCode(4)
            elif statusCode > 1000:
                self.setPandaErrorCode(9)
            else:
                self.setPandaErrorCode(6)
            sys.exit()
        
        self.notify.info('Download server: %s' % self.downloadServer.cStr())
        if self.notify.getDebug():
            self.accept('page_up', self.increaseBandwidth)
            self.accept('page_down', self.decreaseBandwidth)
        
        self.httpChannel.setPersistentConnection(1)
        self.foreground()
        self.prepareClient()
        self.setBandwidth()
        self.downloadServerDbFile()

    
    def getTime(self):
        return self.clock.getRealTime()

    
    def isDummy(self):
        return 0

    
    def background(self):
        self.notify.info('background: Launcher now operating in background')
        self.backgrounded = 1

    
    def foreground(self):
        self.notify.info('foreground: Launcher now operating in foreground')
        self.backgrounded = 0

    
    def setRegistry(self, name, value):
        t = type(value)
        if t == types.IntType:
            WindowsRegistry.setIntValue(self.toontownRegistryKey, name, value)
        elif t == types.StringType:
            WindowsRegistry.setStringValue(self.toontownRegistryKey, name, value)
        else:
            self.notify.warning('setRegistry: Invalid type for registry value: ' + `value`)

    
    def getRegistry(self, name, missingValue = None):
        t = WindowsRegistry.getKeyType(self.toontownRegistryKey, name)
        if t == WindowsRegistry.TInt:
            if missingValue == None:
                missingValue = 0
            
            return WindowsRegistry.getIntValue(self.toontownRegistryKey, name, missingValue)
        elif t == WindowsRegistry.TString:
            if missingValue == None:
                missingValue = ''
            
            return WindowsRegistry.getStringValue(self.toontownRegistryKey, name, missingValue)
        else:
            return missingValue

    
    def handleInitiateFatalError(self, errorCode):
        self.notify.warning('handleInitiateFatalError: ' + errorToText(errorCode))
        sys.exit()

    
    def handleDecompressFatalError(self, task, errorCode):
        self.notify.warning('handleDecompressFatalError: ' + errorToText(errorCode))
        taskMgr.remove(task)
        self.handleGenericMultifileError()

    
    def handleDecompressWriteError(self, task, errorCode):
        self.notify.warning('handleDecompressWriteError: ' + errorToText(errorCode))
        taskMgr.remove(task)
        self.handleGenericMultifileError()

    
    def handleDecompressZlibError(self, task, errorCode):
        self.notify.warning('handleDecompressZlibError: ' + errorToText(errorCode))
        taskMgr.remove(task)
        self.handleGenericMultifileError()

    
    def handleExtractFatalError(self, task, errorCode):
        self.notify.warning('handleExtractFatalError: ' + errorToText(errorCode))
        taskMgr.remove(task)
        self.handleGenericMultifileError()

    
    def handleExtractWriteError(self, task, errorCode):
        self.notify.warning('handleExtractWriteError: ' + errorToText(errorCode))
        taskMgr.remove(task)
        self.handleGenericMultifileError()

    
    def handlePatchFatalError(self, task, errorCode):
        self.notify.warning('handlePatchFatalError: ' + errorToText(errorCode))
        taskMgr.remove(task)
        self.handleGenericMultifileError()

    
    def handlePatchWriteError(self, task, errorCode):
        self.notify.warning('handlePatchWriteError: ' + errorToText(errorCode))
        taskMgr.remove(task)
        self.handleGenericMultifileError()

    
    def handleDownloadFatalError(self, task):
        self.notify.warning('handleDownloadFatalError: status code = %s %s' % (self.httpChannel.getStatusCode(), self.httpChannel.getStatusString()))
        taskMgr.remove(task)
        statusCode = self.httpChannel.getStatusCode()
        if statusCode == 404:
            self.setPandaErrorCode(5)
        elif statusCode == 0:
            self.setPandaErrorCode(4)
        else:
            self.setPandaErrorCode(6)
        sys.exit()

    
    def handleDownloadWriteError(self, task):
        self.notify.warning('handleDownloadWriteError.')
        taskMgr.remove(task)
        self.setPandaErrorCode(2)
        sys.exit()

    
    def handleGenericMultifileError(self):
        if not (self.currentMfname):
            sys.exit()
        
        if self.curMultifileRetry < self.multifileRetries:
            self.notify.info('recover attempt: %s / %s' % (self.curMultifileRetry, self.multifileRetries))
            self.curMultifileRetry += 1
            self.notify.info('downloadPatchDone: Recovering from error.' + ' Deleting files in: ' + self.currentMfname)
            self.dldb.setClientMultifileIncomplete(self.currentMfname)
            self.dldb.setClientMultifileSize(self.currentMfname, 0)
            self.notify.info('downloadPatchDone: Recovering from error.' + ' redownloading: ' + self.currentMfname)
            self.httpChannel.reset()
            self.getMultifile(self.currentMfname)
        else:
            self.setPandaErrorCode(6)
            self.notify.info('handleGenericMultifileError: Failed to download multifile')
            sys.exit()

    
    def foregroundSleep(self):
        if not (self.backgrounded):
            time.sleep(0.01)
        

    
    def forceSleep(self):
        if not (self.backgrounded):
            time.sleep(3.0)
        

    
    def addDownloadVersion(self, serverFilePath):
        url = URLSpec(self.downloadServer)
        origPath = url.getPath()
        if origPath and origPath[-1] == '/':
            origPath = origPath[:-1]
        
        url.setPath('%s/%s/content/%s' % (origPath, self.ServerVersion, serverFilePath))
        return url

    
    def download(self, serverFilePath, localFilename, callback):
        self.launcherMessage(Localizer.LauncherDownloadFile % {
            'name': self.currentPhaseName,
            'current': self.currentPhaseIndex,
            'total': self.numPhases })
        task = Task.Task(self.downloadTask)
        task.downloadRam = 0
        task.serverFilePath = serverFilePath
        task.serverFileURL = self.addDownloadVersion(serverFilePath)
        self.notify.info('Download request: %s' % task.serverFileURL.cStr())
        task.callback = callback
        task.lastUpdate = 0
        self.resetBytesPerSecond()
        task.localFilename = localFilename
        self.httpChannel.beginGetDocument(DocumentSpec(task.serverFileURL))
        self.httpChannel.downloadToFile(task.localFilename)
        taskMgr.add(task, 'launcher-download')

    
    def downloadRam(self, serverFilePath, callback):
        self.ramfile = Ramfile()
        task = Task.Task(self.downloadTask)
        task.downloadRam = 1
        task.serverFilePath = serverFilePath
        task.serverFileURL = self.addDownloadVersion(serverFilePath)
        self.notify.info('Download request: %s' % task.serverFileURL.cStr())
        task.callback = callback
        task.lastUpdate = 0
        self.resetBytesPerSecond()
        self.httpChannel.beginGetDocument(DocumentSpec(task.serverFileURL))
        self.httpChannel.downloadToRam(self.ramfile)
        taskMgr.add(task, 'launcher-download')

    
    def downloadTask(self, task):
        if self.httpChannel.run():
            now = self.getTime()
            if now - task.lastUpdate >= self.UserUpdateDelay:
                task.lastUpdate = now
                self.testBandwidth()
                bytesWritten = self.httpChannel.getBytesDownloaded()
                totalBytes = self.httpChannel.getFileSize()
                if totalBytes:
                    pct = int(round((bytesWritten / float(totalBytes)) * 100))
                    self.launcherMessage(Localizer.LauncherDownloadFilePercent % {
                        'name': self.currentPhaseName,
                        'current': self.currentPhaseIndex,
                        'total': self.numPhases,
                        'percent': pct })
                else:
                    self.launcherMessage(Localizer.LauncherDownloadFileBytes % {
                        'name': self.currentPhaseName,
                        'current': self.currentPhaseIndex,
                        'total': self.numPhases,
                        'bytes': bytesWritten })
            
            self.foregroundSleep()
            return Task.cont
        
        if self.httpChannel.isValid() and self.httpChannel.isDownloadComplete():
            bytesWritten = self.httpChannel.getBytesDownloaded()
            totalBytes = self.httpChannel.getFileSize()
            if totalBytes:
                pct = int(round((bytesWritten / float(totalBytes)) * 100))
                self.launcherMessage(Localizer.LauncherDownloadFilePercent % {
                    'name': self.currentPhaseName,
                    'current': self.currentPhaseIndex,
                    'total': self.numPhases,
                    'percent': pct })
            else:
                self.launcherMessage(Localizer.LauncherDownloadFileBytes % {
                    'name': self.currentPhaseName,
                    'current': self.currentPhaseIndex,
                    'total': self.numPhases,
                    'bytes': bytesWritten })
            self.notify.info('downloadTask: Download done: %s' % task.serverFileURL.cStr())
            task.callback()
            del task.callback
            return Task.done
        elif self.httpChannel.isValid():
            self.handleDownloadWriteError(task)
        elif int(self.httpChannel.getStatusCode() / 100) == 2:
            gotBytes = self.httpChannel.getBytesDownloaded()
            self.notify.info('Connection lost while downloading; got %s bytes.  Reconnecting.' % gotBytes)
            if task.downloadRam:
                self.downloadRam(task.serverFilePath, task.callback)
            else:
                self.download(task.serverFilePath, task.localFilename, task.callback)
        else:
            self.handleDownloadFatalError(task)
        return Task.done

    
    def downloadMultifile(self, mfname, localFilename, callback, totalSize, currentSize, callbackProgress):
        if currentSize == totalSize:
            callback()
            return None
        
        self.launcherMessage(Localizer.LauncherDownloadFile % {
            'name': self.currentPhaseName,
            'current': self.currentPhaseIndex,
            'total': self.numPhases })
        task = Task.Task(self.downloadMultifileTask)
        mfURL = self.addDownloadVersion(mfname)
        task.mfURL = mfURL
        task.mfname = mfname
        self.notify.info('downloadMultifile: %s ' % task.mfURL.cStr())
        task.callback = callback
        task.callbackProgress = callbackProgress
        task.lastUpdate = 0
        task.currentSize = currentSize
        task.totalSize = totalSize
        self.resetBytesPerSecond()
        task.localFilename = localFilename
        if currentSize != 0:
            self.httpChannel.beginGetSubdocument(DocumentSpec(task.mfURL), currentSize, 0)
            if not self.httpChannel.downloadToFile(task.localFilename, currentSize):
                currentSize = 0
                task.currentSize = 0
            
        else:
            self.httpChannel.beginGetDocument(DocumentSpec(task.mfURL))
            self.httpChannel.downloadToFile(task.localFilename)
        taskMgr.add(task, 'launcher-download-multifile')

    
    def downloadMultifilePatchWriteToDisk(self, task):
        bytesWritten = self.httpChannel.getBytesDownloaded() + task.currentSize
        self.notify.debug('bytesWritten: ' + str(bytesWritten))
        percentPatchComplete = int(round(((self.patchDownloadSoFar + bytesWritten) / float(self.totalPatchDownload)) * self.downloadPercentage))
        self.setPercentPhaseComplete(self.currentPhase, percentPatchComplete)

    
    def downloadMultifileWriteToDisk(self, task):
        bytesWritten = self.httpChannel.getBytesDownloaded() + task.currentSize
        self.notify.debug('bytesWritten: ' + str(bytesWritten))
        self.dldb.setClientMultifileSize(task.mfname, bytesWritten)
        percentComplete = int(round((bytesWritten / float(task.totalSize)) * self.downloadPercentage))
        self.setPercentPhaseComplete(self.currentPhase, percentComplete)

    
    def downloadMultifileTask(self, task):
        if self.httpChannel.run():
            now = self.getTime()
            if now - task.lastUpdate >= self.UserUpdateDelay:
                task.lastUpdate = now
                self.testBandwidth()
                if task.callbackProgress:
                    task.callbackProgress(task)
                
                bytesWritten = self.httpChannel.getBytesDownloaded() + task.currentSize
                percentComplete = int(round(100.0 * bytesWritten / float(task.totalSize)))
                self.launcherMessage(Localizer.LauncherDownloadFilePercent % {
                    'name': self.currentPhaseName,
                    'current': self.currentPhaseIndex,
                    'total': self.numPhases,
                    'percent': percentComplete })
            
            self.foregroundSleep()
            return Task.cont
        
        if self.httpChannel.isValid() and self.httpChannel.isDownloadComplete():
            if task.callbackProgress:
                task.callbackProgress(task)
            
            self.notify.info('done: %s' % task.mfname)
            self.dldb.setClientMultifileComplete(task.mfname)
            task.callback()
            del task.callback
            return Task.done
        elif self.httpChannel.isValid():
            self.handleDownloadWriteError(task)
        elif int(self.httpChannel.getStatusCode() / 100) == 2:
            gotBytes = self.httpChannel.getBytesDownloaded()
            self.notify.info('Connection lost while downloading; got %s bytes.  Reconnecting.' % gotBytes)
            self.downloadMultifile(task.mfname, task.localFilename, task.callback, task.totalSize, task.currentSize + gotBytes, task.callbackProgress)
        elif self.httpChannel.getStatusCode() == 416 and task.currentSize != 0:
            self.notify.info('Got 416, invalid subrange; redownloading entire file.')
            self.downloadMultifile(task.mfname, task.localFilename, task.callback, task.totalSize, 0, task.callbackProgress)
        else:
            self.handleDownloadFatalError(task)
        return Task.done

    
    def decompressFile(self, localFilename, callback):
        self.notify.info('decompress: request: ' + localFilename.cStr())
        self.launcherMessage(Localizer.LauncherDecompressingFile % {
            'name': self.currentPhaseName,
            'current': self.currentPhaseIndex,
            'total': self.numPhases })
        task = Task.Task(self.decompressFileTask)
        task.localFilename = localFilename
        task.callback = callback
        task.lastUpdate = 0
        task.decompressor = Decompressor()
        errorCode = task.decompressor.initiate(task.localFilename)
        if errorCode > 0:
            taskMgr.add(task, 'launcher-decompressFile')
        else:
            self.handleInitiateFatalError(errorCode)

    
    def decompressFileTask(self, task):
        errorCode = task.decompressor.run()
        if errorCode == EUOk:
            now = self.getTime()
            if now - task.lastUpdate >= self.UserUpdateDelay:
                task.lastUpdate = now
                progress = task.decompressor.getProgress()
                self.launcherMessage(Localizer.LauncherDecompressingPercent % {
                    'name': self.currentPhaseName,
                    'current': self.currentPhaseIndex,
                    'total': self.numPhases,
                    'percent': int(round(progress * 100)) })
            
            self.foregroundSleep()
            return Task.cont
        elif errorCode == EUSuccess:
            self.launcherMessage(Localizer.LauncherDecompressingPercent % {
                'name': self.currentPhaseName,
                'current': self.currentPhaseIndex,
                'total': self.numPhases,
                'percent': 100 })
            self.notify.info('decompressTask: Decompress done: ' + task.localFilename.cStr())
            del task.decompressor
            task.callback()
            del task.callback
            return Task.done
        elif errorCode == EUErrorAbort:
            self.handleDecompressFatalError(task, errorCode)
            return Task.done
        elif errorCode == EUErrorWriteOutOfFiles and errorCode == EUErrorWriteDiskFull and errorCode == EUErrorWriteDiskSectorNotFound and errorCode == EUErrorWriteOutOfMemory and errorCode == EUErrorWriteSharingViolation and errorCode == EUErrorWriteDiskFault or errorCode == EUErrorWriteDiskNotFound:
            self.handleDecompressWriteError(task, errorCode)
            return Task.done
        elif errorCode == EUErrorZlib:
            self.handleDecompressZlibError(task, errorCode)
            return Task.done
        elif errorCode > 0:
            self.notify.warning('decompressMultifileTask: Unknown success return code: ' + errorToText(errorCode))
            return Task.cont
        else:
            self.notify.warning('decompressMultifileTask: Unknown return code: ' + errorToText(errorCode))
            self.handleDecompressFatalError(task, errorCode)
            return Task.done

    
    def decompressMultifile(self, mfname, localFilename, callback):
        self.notify.info('decompressMultifile: request: ' + localFilename.cStr())
        self.launcherMessage(Localizer.LauncherDecompressingFile % {
            'name': self.currentPhaseName,
            'current': self.currentPhaseIndex,
            'total': self.numPhases })
        task = Task.Task(self.decompressMultifileTask)
        task.mfname = mfname
        task.localFilename = localFilename
        task.callback = callback
        task.lastUpdate = 0
        task.decompressor = Decompressor()
        errorCode = task.decompressor.initiate(task.localFilename)
        if errorCode > 0:
            taskMgr.add(task, 'launcher-decompressMultifile')
        else:
            self.handleInitiateFatalError(errorCode)

    
    def decompressMultifileTask(self, task):
        errorCode = task.decompressor.run()
        if errorCode == EUOk:
            now = self.getTime()
            if now - task.lastUpdate >= self.UserUpdateDelay:
                task.lastUpdate = now
                progress = task.decompressor.getProgress()
                self.launcherMessage(Localizer.LauncherDecompressingPercent % {
                    'name': self.currentPhaseName,
                    'current': self.currentPhaseIndex,
                    'total': self.numPhases,
                    'percent': int(round(progress * 100)) })
                percentProgress = int(round(progress * self.decompressPercentage))
                totalPercent = self.downloadPercentage + percentProgress
                self.setPercentPhaseComplete(self.currentPhase, totalPercent)
            
            self.foregroundSleep()
            return Task.cont
        elif errorCode == EUSuccess:
            self.launcherMessage(Localizer.LauncherDecompressingPercent % {
                'name': self.currentPhaseName,
                'current': self.currentPhaseIndex,
                'total': self.numPhases,
                'percent': 100 })
            totalPercent = self.downloadPercentage + self.decompressPercentage
            self.setPercentPhaseComplete(self.currentPhase, totalPercent)
            self.notify.info('decompressMultifileTask: Decompress multifile done: ' + task.localFilename.cStr())
            self.dldb.setClientMultifileDecompressed(task.mfname)
            del task.decompressor
            task.callback()
            del task.callback
            return Task.done
        elif errorCode == EUErrorAbort:
            self.handleDecompressFatalError(task, errorCode)
            return Task.done
        elif errorCode == EUErrorWriteOutOfFiles and errorCode == EUErrorWriteDiskFull and errorCode == EUErrorWriteDiskSectorNotFound and errorCode == EUErrorWriteOutOfMemory and errorCode == EUErrorWriteSharingViolation and errorCode == EUErrorWriteDiskFault or errorCode == EUErrorWriteDiskNotFound:
            self.handleDecompressWriteError(task, errorCode)
            return Task.done
        elif errorCode == EUErrorZlib:
            self.handleDecompressZlibError(task, errorCode)
            return Task.done
        elif errorCode > 0:
            self.notify.warning('decompressMultifileTask: Unknown success return code: ' + errorToText(errorCode))
            return Task.cont
        else:
            self.notify.warning('decompressMultifileTask: Unknown return code: ' + errorToText(errorCode))
            self.handleDecompressFatalError(task, errorCode)
            return Task.done

    
    def extract(self, mfname, localFilename, destDir, callback):
        self.notify.info('extract: request: ' + localFilename.cStr() + ' destDir: ' + destDir.cStr())
        self.launcherMessage(Localizer.LauncherExtractingFile % {
            'name': self.currentPhaseName,
            'current': self.currentPhaseIndex,
            'total': self.numPhases })
        task = Task.Task(self.extractTask)
        task.mfname = mfname
        task.localFilename = localFilename
        task.destDir = destDir
        task.callback = callback
        task.lastUpdate = 0
        task.extractor = Extractor()
        task.extractor.setExtractDir(task.destDir)
        if not task.extractor.setMultifile(task.localFilename):
            self.setPandaErrorCode(6)
            self.notify.info('extract: Unable to open multifile %s' % task.localFilename.cStr())
            sys.exit()
        
        numFiles = self.dldb.getServerNumFiles(mfname)
        for i in range(numFiles):
            subfile = self.dldb.getServerFileName(mfname, i)
            if not task.extractor.requestSubfile(Filename(subfile)):
                self.setPandaErrorCode(6)
                self.notify.info('extract: Unable to find subfile %s in multifile %s' % (subfile, mfname))
                sys.exit()
            
        
        self.notify.info('Extracting %d subfiles from multifile %s.' % (numFiles, mfname))
        taskMgr.add(task, 'launcher-extract')

    
    def extractTask(self, task):
        errorCode = task.extractor.step()
        if errorCode == EUOk:
            now = self.getTime()
            if now - task.lastUpdate >= self.UserUpdateDelay:
                task.lastUpdate = now
                progress = task.extractor.getProgress()
                self.launcherMessage(Localizer.LauncherExtractingPercent % {
                    'name': self.currentPhaseName,
                    'current': self.currentPhaseIndex,
                    'total': self.numPhases,
                    'percent': int(round(progress * 100.0)) })
                percentProgress = int(round(progress * self.extractPercentage))
                totalPercent = self.downloadPercentage + self.decompressPercentage + percentProgress
                self.setPercentPhaseComplete(self.currentPhase, totalPercent)
            
            self.foregroundSleep()
            return Task.cont
        elif errorCode == EUSuccess:
            self.launcherMessage(Localizer.LauncherExtractingPercent % {
                'name': self.currentPhaseName,
                'current': self.currentPhaseIndex,
                'total': self.numPhases,
                'percent': 100 })
            totalPercent = self.downloadPercentage + self.decompressPercentage + self.extractPercentage
            self.setPercentPhaseComplete(self.currentPhase, totalPercent)
            self.notify.info('extractTask: Extract multifile done: ' + task.localFilename.cStr())
            self.dldb.setClientMultifileExtracted(task.mfname)
            del task.extractor
            task.callback()
            del task.callback
            return Task.done
        elif errorCode == EUErrorAbort:
            self.handleExtractFatalError(task, errorCode)
            return Task.done
        elif errorCode == EUErrorFileEmpty:
            self.handleExtractFatalError(task, errorCode)
            return Task.done
        elif errorCode == EUErrorWriteOutOfFiles and errorCode == EUErrorWriteDiskFull and errorCode == EUErrorWriteDiskSectorNotFound and errorCode == EUErrorWriteOutOfMemory and errorCode == EUErrorWriteSharingViolation and errorCode == EUErrorWriteDiskFault or errorCode == EUErrorWriteDiskNotFound:
            self.handleExtractWriteError(task, errorCode)
            return Task.done
        elif errorCode > 0:
            self.notify.warning('extractTask: Unknown success return code: ' + errorToText(errorCode))
            return Task.cont
        else:
            self.notify.warning('extractTask: Unknown error return code: ' + errorToText(errorCode))
            self.handleExtractFatalError(task, errorCode)
            return Task.done

    
    def patch(self, patchFile, patcheeFile, callback):
        self.notify.info('patch: request: ' + patchFile.cStr() + ' patchee: ' + patcheeFile.cStr())
        self.launcherMessage(Localizer.LauncherPatchingFile % {
            'name': self.currentPhaseName,
            'current': self.currentPhaseIndex,
            'total': self.numPhases })
        task = Task.Task(self.patchTask)
        task.patchFile = patchFile
        task.patcheeFile = patcheeFile
        task.callback = callback
        task.lastUpdate = 0
        task.patcher = Patcher()
        errorCode = task.patcher.initiate(task.patchFile, task.patcheeFile)
        if errorCode > 0:
            taskMgr.add(task, 'launcher-patch')
        else:
            self.handleInitiateFatalError(errorCode)

    
    def patchTask(self, task):
        errorCode = task.patcher.run()
        if errorCode == EUOk:
            now = self.getTime()
            if now - task.lastUpdate >= self.UserUpdateDelay:
                task.lastUpdate = now
                progress = task.patcher.getProgress()
                self.launcherMessage(Localizer.LauncherPatchingPercent % {
                    'name': self.currentPhaseName,
                    'current': self.currentPhaseIndex,
                    'total': self.numPhases,
                    'percent': int(round(progress * 100.0)) })
            
            self.foregroundSleep()
            return Task.cont
        elif errorCode == EUSuccess:
            self.launcherMessage(Localizer.LauncherPatchingPercent % {
                'name': self.currentPhaseName,
                'current': self.currentPhaseIndex,
                'total': self.numPhases,
                'percent': 100 })
            self.notify.info('patchTask: Patch done: ' + task.patcheeFile.cStr())
            del task.patcher
            task.callback()
            del task.callback
            return Task.done
        elif errorCode == EUErrorAbort:
            self.handlePatchFatalError(task, errorCode)
            return Task.done
        elif errorCode == EUErrorFileEmpty:
            self.handlePatchFatalError(task, errorCode)
            return Task.done
        elif errorCode == EUErrorWriteOutOfFiles and errorCode == EUErrorWriteDiskFull and errorCode == EUErrorWriteDiskSectorNotFound and errorCode == EUErrorWriteOutOfMemory and errorCode == EUErrorWriteSharingViolation and errorCode == EUErrorWriteDiskFault or errorCode == EUErrorWriteDiskNotFound:
            self.handlePatchWriteError(task, errorCode)
            return Task.done
        elif errorCode > 0:
            self.notify.warning('patchTask: Unknown success return code: ' + errorToText(errorCode))
            return Task.cont
        else:
            self.notify.warning('patchTask: Unknown error return code: ' + errorToText(errorCode))
            self.handlePatchFatalError(task, errorCode)
            return Task.done

    
    def downloadProgressFile(self):
        localFilename = Filename(self.dbDir + 'progress')
        self.download(self.progressFilename, localFilename, self.downloadProgressFileDone)

    
    def getProgressSum(self, phase):
        sum = 0
        for i in xrange(0, len(self.linesInProgress)):
            if self.linesInProgress[i].find(phase) > -1:
                nameSizeTuple = self.linesInProgress[i].split()
                numSize = nameSizeTuple[1].split('L')
                sum += string.atoi(numSize[0])
            
        
        return sum

    
    def downloadProgressFileDone(self):
        localFilename = Filename(self.dbDir + 'progress')
        f = open(localFilename.cStr())
        self.linesInProgress = f.readlines()
        f.close()
        localFilename.unlink()
        self.progressSum = 0
        token = 'phase_'
        self.progressSum = self.getProgressSum(token)
        self.progressSum -= self.getProgressSum(token + '2')
        self.notify.info('total phases to be downloaded = ' + `self.progressSum`)
        self.checkClientDbExists()

    
    def prepareClient(self):
        self.notify.info('prepareClient: Preparing client for install')
        if not os.path.exists(self.topDir):
            self.notify.info('prepareClient: Creating top directory: ' + self.topDir)
            os.makedirs(self.topDir)
        
        if not os.path.exists(self.dbDir):
            self.notify.info('prepareClient: Creating db directory: ' + self.dbDir)
            os.makedirs(self.dbDir)
        
        if not os.path.exists(self.patchDir):
            self.notify.info('prepareClient: Creating patch directory: ' + self.patchDir)
            os.makedirs(self.patchDir)
        
        if not os.path.exists(self.mfDir):
            self.notify.info('prepareClient: Creating mf directory: ' + self.mfDir)
            os.makedirs(self.mfDir)
        

    
    def downloadServerDbFile(self):
        self.notify.info('Downloading server db file')
        self.launcherMessage(Localizer.LauncherDownloadServerFileList)
        self.downloadRam(self.serverDbFilePath, self.downloadServerDbFileDone)

    
    def downloadServerDbFileDone(self):
        self.downloadProgressFile()

    
    def checkClientDbExists(self):
        clientFilename = Filename(self.dbDir + self.clientDbFilename)
        if clientFilename.exists():
            self.notify.info('Client Db exists')
            self.createDownloadDb()
        else:
            self.notify.info('Client Db does not exist')
            self.downloadClientDbStarterFile()

    
    def downloadClientDbStarterFile(self):
        self.notify.info('Downloading Client Db starter file')
        localFilename = Filename(self.dbDir + self.compClientDbFilename)
        self.download(self.clientStarterDbFilePath, localFilename, self.downloadClientDbStarterFileDone)

    
    def downloadClientDbStarterFileDone(self):
        localFilename = Filename(self.dbDir + self.compClientDbFilename)
        decompressor = Decompressor()
        decompressor.decompress(localFilename)
        self.createDownloadDb()

    
    def createDownloadDb(self):
        self.notify.info('Creating downloadDb')
        self.launcherMessage(Localizer.LauncherCreatingDownloadDb)
        clientFilename = Filename(self.dbDir + self.clientDbFilename)
        self.notify.info('Client file name: ' + clientFilename.cStr())
        self.launcherMessage(Localizer.LauncherDownloadClientFileList)
        serverFile = self.ramfile
        decompressor = Decompressor()
        decompressor.decompress(serverFile)
        self.notify.info('Finished decompress')
        self.dldb = DownloadDb(serverFile, clientFilename)
        self.notify.info('created download db')
        self.launcherMessage(Localizer.LauncherFinishedDownloadDb)
        self.currentPhase = LauncherPhases[0]
        self.currentPhaseIndex = 1
        self.currentPhaseName = Localizer.LauncherPhaseNames[self.currentPhase]
        self.updatePhase(self.currentPhase)

    
    def maybeStartToontown(self):
        if self.currentPhase >= self.showPhase:
            self.notify.info('maybeStartToontown: starting toontown')
            self.launcherMessage(Localizer.LauncherStartingToontown)
            messenger.send('startToontown')
        

    
    def updatePhase(self, phase):
        self.notify.info('Updating multifiles in phase: ' + `phase`)
        self.setPercentPhaseComplete(self.currentPhase, 0)
        self.phaseMultifileNames = []
        numfiles = self.dldb.getServerNumMultifiles()
        for i in range(self.dldb.getServerNumMultifiles()):
            mfname = self.dldb.getServerMultifileName(i)
            if self.dldb.getServerMultifilePhase(mfname) == phase:
                self.phaseMultifileNames.append(mfname)
            
        
        self.updateNextMultifile()

    
    def updateNextMultifile(self):
        if len(self.phaseMultifileNames) > 0:
            self.currentMfname = self.phaseMultifileNames.pop()
            self.curMultifileRetry = 0
            self.getMultifile(self.currentMfname)
        elif self.currentMfname is None:
            self.notify.warning('no multifile found! See below for debug info:')
            for i in range(self.dldb.getServerNumMultifiles()):
                mfname = self.dldb.getServerMultifileName(i)
                phase = self.dldb.getServerMultifilePhase(mfname)
                print i, mfname, phase
            
            self.handleGenericMultifileError()
        
        decompressedMfname = os.path.splitext(self.currentMfname)[0]
        localFilename = Filename(self.mfDir + decompressedMfname)
        nextIndex = LauncherPhases.index(self.currentPhase) + 1
        if nextIndex < len(LauncherPhases):
            self.MakeNTFSFilesGlobalWriteable(localFilename)
        else:
            self.MakeNTFSFilesGlobalWriteable()
        vfs = VirtualFileSystem.getGlobalPtr()
        vfs.mount(localFilename, '.', VirtualFileSystem.MFReadOnly)
        self.setPercentPhaseComplete(self.currentPhase, 100)
        self.notify.info('Done updating multifiles in phase: ' + `self.currentPhase`)
        self.progressSoFar += int(round(self.phaseOverallMap[self.currentPhase] * 100))
        self.notify.info('progress so far ' + `self.progressSoFar`)
        messenger.send('phaseComplete-' + `self.currentPhase`)
        if nextIndex < len(LauncherPhases):
            self.currentPhase = LauncherPhases[nextIndex]
            self.currentPhaseIndex = nextIndex + 1
            self.currentPhaseName = Localizer.LauncherPhaseNames[self.currentPhase]
            self.updatePhase(self.currentPhase)
        else:
            self.notify.info('ALL PHASES COMPLETE')
            self.maybeStartToontown()
            messenger.send('launcherAllPhasesComplete')
            self.cleanup()

    
    def updateMultifileDone(self):
        self.updateNextMultifile()

    
    def downloadMultifileDone(self):
        self.getDecompressMultifile(self.currentMfname)

    
    def getMultifile(self, mfname):
        self.notify.info('Downloading multifile: ' + mfname)
        if not self.dldb.clientMultifileExists(mfname):
            self.maybeStartToontown()
            self.notify.info('Multifile does not exist in client db,' + 'creating new record: ' + mfname)
            self.dldb.addClientMultifile(mfname)
        
        decompressedMfname = os.path.splitext(mfname)[0]
        decompressedFilename = Filename(self.mfDir + decompressedMfname)
        if not self.dldb.clientMultifileComplete(mfname) or not decompressedFilename.exists():
            self.maybeStartToontown()
            currentSize = self.dldb.getClientMultifileSize(mfname)
            totalSize = self.dldb.getServerMultifileSize(mfname)
            localFilename = Filename(self.mfDir + mfname)
            if not localFilename.exists():
                currentSize = 0
            
            if currentSize == 0:
                self.notify.info('Multifile has not been started, ' + 'downloading new file: ' + mfname)
                curHash = self.dldb.getServerMultifileHash(mfname)
                self.dldb.setClientMultifileHash(mfname, curHash)
                self.phaseNewDownload[self.currentPhase] = 1
                self.downloadMultifile(mfname, localFilename, self.downloadMultifileDone, totalSize, 0, self.downloadMultifileWriteToDisk)
            else:
                clientHash = self.dldb.getClientMultifileHash(mfname)
                serverHash = self.dldb.getServerMultifileHash(mfname)
                if clientHash.eq(serverHash):
                    self.notify.info('Multifile is not complete, finishing download for %s, size = %s / %s' % (mfname, currentSize, totalSize))
                    self.downloadMultifile(mfname, localFilename, self.downloadMultifileDone, totalSize, currentSize, self.downloadMultifileWriteToDisk)
                elif self.curMultifileRetry < self.multifileRetries:
                    self.notify.info('recover attempt: %s / %s' % (self.curMultifileRetry, self.multifileRetries))
                    self.curMultifileRetry += 1
                    self.notify.info('Multifile is not complete, and is out of date. ' + 'Restarting download with newest multifile')
                    self.dldb.setClientMultifileIncomplete(self.currentMfname)
                    self.dldb.setClientMultifileSize(self.currentMfname, 0)
                    self.getMultifile(self.currentMfname)
                else:
                    self.setPandaErrorCode(6)
                    self.notify.info('getMultifile: Failed to download multifile')
                    sys.exit()
        else:
            self.notify.info('Multifile already complete: ' + mfname)
            self.downloadMultifileDone()

    
    def getDecompressMultifile(self, mfname):
        if not self.dldb.clientMultifileDecompressed(mfname):
            self.maybeStartToontown()
            self.notify.info('decompressMultifile: Decompressing multifile: ' + mfname)
            localFilename = Filename(self.mfDir + mfname)
            self.decompressMultifile(mfname, localFilename, self.decompressMultifileDone)
        else:
            self.notify.info('decompressMultifile: Multifile already decompressed: ' + mfname)
            self.decompressMultifileDone()

    
    def decompressMultifileDone(self):
        if self.phaseNewDownload[self.currentPhase]:
            self.setPercentPhaseComplete(self.currentPhase, 95)
        
        self.extractMultifile(self.currentMfname)

    
    def extractMultifile(self, mfname):
        if not self.dldb.clientMultifileExtracted(mfname):
            self.maybeStartToontown()
            self.notify.info('extractMultifile: Extracting multifile: ' + mfname)
            decompressedMfname = os.path.splitext(mfname)[0]
            localFilename = Filename(self.mfDir + decompressedMfname)
            destDir = Filename(self.topDir)
            self.notify.info('extractMultifile: Extracting: ' + localFilename.cStr() + ' to: ' + destDir.cStr())
            self.extract(mfname, localFilename, destDir, self.extractMultifileDone)
        else:
            self.notify.info('extractMultifile: Multifile already extracted: ' + mfname)
            self.extractMultifileDone()

    
    def extractMultifileDone(self):
        if self.phaseNewDownload[self.currentPhase]:
            self.setPercentPhaseComplete(self.currentPhase, 99)
        
        self.notify.info('extractMultifileDone: Finished updating multifile: ' + self.currentMfname)
        self.patchMultifile()

    
    def getPatchFilename(self, fname, currentVersion):
        return fname + '.v' + `currentVersion` + '.' + self.patchExtension

    
    def downloadPatches(self):
        if len(self.patchList) > 0:
            (self.currentPatch, self.currentPatchee, self.currentPatchVersion) = self.patchList.pop()
            serverPatchFilePath = self.currentPatch + '.pz'
            serverPatchFilePath = string.replace(serverPatchFilePath, '\\', '/')
            localPatchFilename = Filename(self.patchDir + self.currentPatch + '.pz')
            if self.currentPhase > 3:
                self.download(serverPatchFilePath, localPatchFilename, self.downloadPatchDone)
            else:
                self.downloadMultifile(serverPatchFilePath, localPatchFilename, self.downloadPatchDone, self.totalPatchDownload, 0, self.downloadMultifilePatchWriteToDisk)
        else:
            self.notify.info('applyNextPatch: Done patching multifile: ' + `self.currentPhase`)
            self.patchDone()

    
    def downloadPatchDone(self):
        self.patchDownloadSoFar += self.httpChannel.getBytesDownloaded()
        self.notify.info('downloadPatchDone: Decompressing patch file: ' + self.currentPatch + '.pz')
        self.decompressFile(Filename(self.patchDir + self.currentPatch + '.pz'), self.decompressPatchDone)

    
    def decompressPatchDone(self):
        self.notify.info('decompressPatchDone: Patching file: ' + self.currentPatchee + ' from ver: ' + `self.currentPatchVersion`)
        patchFile = Filename(self.patchDir + self.currentPatch)
        patchFile.setBinary()
        patchee = Filename(self.mfDir + self.currentPatchee)
        patchee.setBinary()
        self.patch(patchFile, patchee, self.downloadPatches)

    
    def patchDone(self):
        self.notify.info('patchDone: Patch successful')
        del self.currentPatch
        del self.currentPatchee
        del self.currentPatchVersion
        decompressedMfname = os.path.splitext(self.currentMfname)[0]
        localFilename = Filename(self.mfDir + decompressedMfname)
        destDir = Filename(self.topDir)
        self.extract(self.currentMfname, localFilename, destDir, self.updateMultifileDone)

    
    def startReextractingFiles(self):
        self.notify.info('startReextractingFiles: Reextracting ' + `len(self.reextractList)` + ' files for multifile: ' + self.currentMfname)
        self.launcherMessage(Localizer.LauncherRecoverFiles)
        self.currentMfile = Multifile()
        decompressedMfname = os.path.splitext(self.currentMfname)[0]
        self.currentMfile.openRead(Filename(self.mfDir + decompressedMfname))
        self.reextractNextFile()

    
    def reextractNextFile(self):
        failure = 0
        while not failure and len(self.reextractList) > 0:
            currentReextractFile = self.reextractList.pop()
            subfileIndex = self.currentMfile.findSubfile(currentReextractFile)
            if subfileIndex >= 0:
                destFilename = Filename(self.topDir + currentReextractFile)
                result = self.currentMfile.extractSubfile(subfileIndex, destFilename)
                if not result:
                    self.notify.warning('reextractNextFile: Failure on reextract.')
                    failure = 1
                
            else:
                self.notify.warning('reextractNextFile: File not found in multifile: ' + `currentReextractFile`)
                failure = 1
        if failure:
            sys.exit()
        
        self.notify.info('reextractNextFile: Done reextracting files for multifile: ' + `self.currentPhase`)
        del self.currentMfile
        self.updateMultifileDone()

    
    def patchMultifile(self):
        self.launcherMessage(Localizer.LauncherCheckUpdates % {
            'name': self.currentPhaseName,
            'current': self.currentPhaseIndex,
            'total': self.numPhases })
        self.notify.info('patchMultifile: Checking for patches on multifile: ' + self.currentMfname)
        self.patchList = []
        clientMd5 = HashVal()
        decompressedMfname = os.path.splitext(self.currentMfname)[0]
        localFilename = Filename(self.mfDir + decompressedMfname)
        localFilename.setBinary()
        md5AFile(localFilename, clientMd5)
        clientVer = self.dldb.getVersion(Filename(decompressedMfname), clientMd5)
        if clientVer == 1:
            self.patchAndHash()
            return None
        elif clientVer == -1:
            self.notify.info('patchMultifile: Invalid hash for file: ' + self.currentMfname)
            self.maybeStartToontown()
            if self.curMultifileRetry < self.multifileRetries:
                self.notify.info('recover attempt: %s / %s' % (self.curMultifileRetry, self.multifileRetries))
                self.curMultifileRetry += 1
                self.notify.info('patchMultifile: Restarting download with newest multifile')
                self.dldb.setClientMultifileIncomplete(self.currentMfname)
                self.dldb.setClientMultifileSize(self.currentMfname, 0)
                self.getMultifile(self.currentMfname)
            else:
                self.setPandaErrorCode(6)
                self.notify.info('patchMultifile: Failed to download multifile')
                sys.exit()
            return None
        elif clientVer > 1:
            self.notify.info('patchMultifile: Old version for multifile: ' + self.currentMfname + ' Client ver: ' + `clientVer`)
            self.maybeStartToontown()
            self.totalPatchDownload = 0
            self.patchDownloadSoFar = 0
            for ver in range(1, clientVer):
                patch = self.getPatchFilename(decompressedMfname, ver + 1)
                patchee = decompressedMfname
                patchVersion = ver + 1
                self.patchList.append((patch, patchee, patchVersion))
                if self.currentPhase == 3:
                    self.totalPatchDownload += self.getProgressSum(patch)
                
            
            self.notify.info('total patch to be downloaded = ' + `self.totalPatchDownload`)
            self.downloadPatches()
            return None
        

    
    def patchAndHash(self):
        self.reextractList = []
        self.PAHClean = 1
        self.PAHNumFiles = self.dldb.getServerNumFiles(self.currentMfname)
        self.PAHFileCounter = 0
        if self.PAHNumFiles > 0:
            task = Task.Task(self.patchAndHashTask)
            task.cleanCallback = self.updateMultifileDone
            task.uncleanCallback = self.startReextractingFiles
            taskMgr.add(task, 'patchAndHash')
        else:
            self.updateMultifileDone()

    
    def patchAndHashTask(self, task):
        self.launcherMessage(Localizer.LauncherVerifyPhase)
        if self.PAHFileCounter == self.PAHNumFiles:
            if self.PAHClean:
                task.cleanCallback()
            else:
                task.uncleanCallback()
            return Task.done
        else:
            i = self.PAHFileCounter
            self.PAHFileCounter += 1
        fname = self.dldb.getServerFileName(self.currentMfname, i)
        fnameFilename = Filename(self.topDir + fname)
        if not os.path.exists(fnameFilename.toOsSpecific()):
            self.notify.info('patchAndHash: File not found: ' + fname)
            self.reextractList.append(fname)
            self.PAHClean = 0
            return Task.cont
        
        if self.VerifyFiles and self.dldb.hasVersion(Filename(fname)):
            clientMd5 = HashVal()
            md5AFile(fnameFilename, clientMd5)
            clientVer = self.dldb.getVersion(Filename(fname), clientMd5)
            if clientVer == 1:
                return Task.cont
            else:
                self.notify.info('patchAndHash: Invalid hash for file: ' + fname)
                self.reextractList.append(fname)
                self.PAHClean = 0
        
        return Task.cont

    
    def launcherMessage(self, msg):
        if msg != self.lastLauncherMsg:
            self.lastLauncherMsg = msg
            self.notify.info(msg)
        
        self.setRegistry(self.launcherMessageKey, msg)

    
    def getGameServer(self):
        return self.gameServer

    
    def isTestServer(self):
        return self.testServerFlag

    
    def getAccountServer(self):
        return self.accountServer

    
    def setTutorialComplete(self):
        self.setRegistry(self.tutorialCompleteKey, 0)

    
    def getTutorialComplete(self):
        return self.getRegistry(self.tutorialCompleteKey, 0)

    
    def getGame2Done(self):
        return self.getRegistry(self.game2DoneKey, 0)

    
    def getBlue(self):
        blue = self.getRegistry(self.toontownBlueKey)
        self.setRegistry(self.toontownBlueKey, '')
        if blue == 'NO BLUE':
            blue = None
        
        return blue

    
    def getPlayToken(self):
        playToken = self.getRegistry(self.toontownPlayTokenKey)
        self.setRegistry(self.toontownPlayTokenKey, '')
        if playToken == 'NO PLAYTOKEN':
            playToken = None
        
        return playToken

    
    def recordPeriodTimeRemaining(self, secondsRemaining):
        self.setRegistry(self.periodTimeRemainingKey, int(secondsRemaining))

    
    def recordPeriodName(self, periodName):
        self.setRegistry(self.periodNameKey, periodName)

    
    def recordSwid(self, swid):
        self.setRegistry(self.swidKey, swid)

    
    def getGoUserName(self):
        return self.goUserName

    
    def setGoUserName(self, userName):
        self.goUserName = userName

    
    def getInstallDir(self):
        return self.topDir

    
    def setPandaWindowOpen(self):
        self.setRegistry(self.pandaWindowOpenKey, 1)

    
    def setPandaErrorCode(self, code):
        self.notify.info('setting panda error code to %s' % code)
        self.setRegistry(self.pandaErrorCodeKey, code)

    
    def getIsNewInstallation(self):
        result = self.getRegistry(self.newInstallationKey, 1)
        result = base.config.GetBool('new-installation', result)
        return result

    
    def setIsNotNewInstallation(self):
        self.setRegistry(self.newInstallationKey, 0)

    
    def getLastLogin(self):
        return self.getRegistry(self.lastLoginKey, '')

    
    def setLastLogin(self, login):
        self.setRegistry(self.lastLoginKey, login)

    
    def setUserLoggedIn(self):
        self.setRegistry(self.userLoggedInKey, '1')

    
    def setPaidUserLoggedIn(self):
        self.setRegistry(self.paidUserLoggedInKey, '1')

    
    def getReferrerCode(self):
        return self.getRegistry(self.referrerKey, None)

    
    def getPhaseComplete(self, phase):
        percentDone = self.phaseCompleteMap[phase]
        return percentDone == 100

    
    def setPercentPhaseComplete(self, phase, percent):
        oldPercent = self.phaseCompleteMap[phase]
        if oldPercent != percent:
            self.phaseCompleteMap[phase] = percent
            messenger.send('launcherPercentPhaseComplete', [
                phase,
                percent,
                self.getBandwidth(),
                self.byteRate])
            percentPhaseCompleteKey = 'PERCENT_PHASE_COMPLETE_' + `phase`
            self.setRegistry(percentPhaseCompleteKey, percent)
            self.overallComplete = int(round(percent * self.phaseOverallMap[phase])) + self.progressSoFar
            self.setRegistry('PERCENT_OVERALL_COMPLETE', self.overallComplete)
        

    
    def getPercentPhaseComplete(self, phase):
        return self.phaseCompleteMap[phase]

    
    def resetBytesPerSecond(self):
        self.bpsList = []

    
    def recordBytesPerSecond(self):
        bytesDownloaded = self.httpChannel.getBytesDownloaded()
        bytesRequested = self.httpChannel.getBytesRequested()
        t = self.getTime()
        self.bpsList.append((t, bytesDownloaded, bytesRequested))
        while 1:
            if len(self.bpsList) == 0:
                break
            
            (ft, fb, fr) = self.bpsList[0]
            if ft < t - self.BPS_WINDOW:
                self.bpsList.pop(0)
            else:
                break

    
    def getBytesPerSecond(self):
        if len(self.bpsList) < 2:
            self.notify.debug('getBytesPerSecond: bpsList not enough elements: %s' % self.bpsList)
            return -1
        
        (startTime, startBytes, startRequested) = self.bpsList[0]
        (finalTime, finalBytes, finalRequested) = self.bpsList[-1]
        dt = finalTime - startTime
        db = finalBytes - startBytes
        dr = finalRequested - startRequested
        if dt <= 0.0:
            self.notify.debug('getBytesPerSecond: negative dt')
            return -1
        
        self.byteRate = db / dt
        self.byteRateRequested = dr / dt
        self.notify.debug('getBytesPerSecond: db = %s, dr = %s, dt = %s byte rate = %s' % (db, dr, dt, self.byteRate))
        return self.byteRate

    
    def testBandwidth(self):
        self.recordBytesPerSecond()
        byteRate = self.getBytesPerSecond()
        if byteRate < 0:
            self.notify.debug('testBandwidth: not enough data yet')
            return None
        
        self.notify.debug('testBandwidth: comparing byteRate %s with getBandwidth %s and byteRateRequested %s.' % (byteRate, self.getBandwidth(), self.byteRateRequested))
        if byteRate >= self.getBandwidth() * self.INCREASE_THRESHOLD:
            self.increaseBandwidth(byteRate)
        elif byteRate < self.byteRateRequested * self.DECREASE_THRESHOLD:
            self.decreaseBandwidth(byteRate)
        

    
    def getBandwidth(self):
        if self.backgrounded:
            bandwidth = self.BANDWIDTH_ARRAY[self.bandwidthIndex] - self.TELEMETRY_BANDWIDTH
        else:
            bandwidth = self.BANDWIDTH_ARRAY[self.bandwidthIndex]
        if self.MAX_BANDWIDTH > 0:
            bandwidth = min(bandwidth, self.MAX_BANDWIDTH)
        
        return bandwidth

    
    def increaseBandwidth(self, targetBandwidth = None):
        maxBandwidthIndex = len(self.BANDWIDTH_ARRAY) - 1
        if self.bandwidthIndex == maxBandwidthIndex:
            self.notify.debug('increaseBandwidth: Already at maximum bandwidth')
            return 0
        
        self.bandwidthIndex += 1
        self.notify.debug('increaseBandwidth: Increasing bandwidth to: ' + `self.getBandwidth()`)
        self.everIncreasedBandwidth = 1
        self.setBandwidth()
        return 1

    
    def decreaseBandwidth(self, targetBandwidth = None):
        if not (self.DECREASE_BANDWIDTH):
            return 0
        
        if self.backgrounded and self.everIncreasedBandwidth:
            self.notify.debug('decreaseBandwidth: Running in background, not reducing bandwidth.')
            return 0
        
        if self.bandwidthIndex == 0:
            self.notify.debug('decreaseBandwidth: Already at minimum bandwidth')
            return 0
        else:
            self.bandwidthIndex -= 1
            if targetBandwidth:
                while self.bandwidthIndex > 0 and self.BANDWIDTH_ARRAY[self.bandwidthIndex] > targetBandwidth:
                    self.bandwidthIndex -= 1
            
            self.notify.debug('decreaseBandwidth: Decreasing bandwidth to: ' + `self.getBandwidth()`)
            self.setBandwidth()
            return 1

    
    def setBandwidth(self):
        self.resetBytesPerSecond()
        self.httpChannel.setMaxBytesPerSecond(self.getBandwidth())

    
    def MakeNTFSFilesGlobalWriteable(self, pathToSet = None):
        if pathToSet == None:
            pathToSet = self.getInstallDir()
        else:
            pathToSet = pathToSet.cStr() + '*'
        DrivePath = pathToSet[0:3]
        
        try:
            (volname, volsernum, maxfilenamlen, sysflags, filesystemtype) = win32api.GetVolumeInformation(DrivePath)
        except:
            return None

        if self.win32con_FILE_PERSISTENT_ACLS & sysflags:
            self.notify.info('NTFS detected, making files global writeable\n')
            win32dir = win32api.GetWindowsDirectory()
            cmdLine = win32dir + '\\system32\\cacls.exe "' + pathToSet + '" /T /E /C /G Everyone:F > nul'
            os.system(cmdLine)
        

    
    def cleanup(self):
        self.notify.info('cleanup: cleaning up Launcher')
        self.ignoreAll()
        del self.clock
        del self.dldb
        del self.httpChannel
        del self.http


if len(sys.argv) == 6 or len(sys.argv) == 7:
    downloadServer = URLSpec(sys.argv[2], 1)
    gameServer = sys.argv[3]
    accountServer = sys.argv[4]
    testServerFlag = int(sys.argv[5])
else:
    sys.exit()
eventMgr.restart()
launcher = Launcher()

def startToontownCallback():
    launcher.background()
    __builtins__['launcher'] = launcher
    import Phase3
    import ToontownStart

launcher.acceptOnce('startToontown', startToontownCallback)

try:
    taskMgr.run()
except SystemExit:
    if __builtins__.has_key('base') and getattr(base, 'graphicsEngine', None):
        base.graphicsEngine.removeAllWindows()
    
    launcher.notify.info('Normal exit.')
    raise 
except:
    launcher.setPandaErrorCode(12)
    launcher.notify.warning('Handling Python exception.')
    if __builtins__.has_key('toonbase') and getattr(toonbase, 'tcr', None):
        if toonbase.tcr.timeManager:
            import ToontownGlobals
            toonbase.tcr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectPythonError)
            toonbase.tcr.timeManager.setExceptionInfo()
        
        toonbase.tcr.sendDisconnect()
    
    if __builtins__.has_key('base') and getattr(base, 'graphicsEngine', None):
        base.graphicsEngine.removeAllWindows()
    
    launcher.notify.info('Exception exit.\n')
    raise 

launcher.notify.info('Reached end of Launcher.py.')
