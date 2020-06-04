# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\AppRunner.py
import sys, os, types, __builtin__
if 'VFSImporter' in sys.modules:
    import VFSImporter, direct.showbase
    direct.showbase.VFSImporter = VFSImporter
    sys.modules['direct.showbase.VFSImporter'] = VFSImporter
else:
    import direct
    from pandac import PandaModules
    from direct.showbase import VFSImporter
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import VirtualFileSystem, Filename, Multifile, loadPrcFileData, unloadPrcFile, getModelPath, Thread, WindowProperties, ExecutionEnvironment, PandaSystem, Notify, StreamWriter, ConfigVariableString, initAppForGui
from pandac import PandaModules
from direct.stdpy import file, glob
from direct.task.TaskManagerGlobal import taskMgr
from direct.showbase.MessengerGlobal import messenger
from direct.showbase import AppRunnerGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.p3d.HostInfo import HostInfo
from direct.p3d.ScanDirectoryNode import ScanDirectoryNode
from direct.p3d.InstalledHostData import InstalledHostData
from direct.p3d.InstalledPackageData import InstalledPackageData
from direct.p3d.JavaScript import UndefinedObject, Undefined, ConcreteStruct, BrowserObject

class ArgumentError(AttributeError):
    __module__ = __name__


class ScriptAttributes:
    __module__ = __name__


class AppRunner(DirectObject):
    __module__ = __name__
    notify = directNotify.newCategory('AppRunner')
    ConfigBasename = 'config.xml'
    maxDiskUsage = 2048 * 1048576
    P3DVCNone = 0
    P3DVCNormal = 1
    P3DVCForce = 2
    P3DVCNever = 3
    P3D_CONTENTS_DEFAULT_MAX_AGE = 5

    def __init__(self):
        DirectObject.__init__(self)
        stream = StreamWriter(Notify.out(), False)
        sys.stdout = stream
        sys.stderr = stream
        self.dummy = False
        self.allowPythonDev = False
        self.guiApp = False
        self.interactiveConsole = False
        self.initialAppImport = False
        self.trueFileIO = False
        self.verifyContents = self.P3DVCNone
        self.sessionId = 0
        self.packedAppEnvironmentInitialized = False
        self.gotWindow = False
        self.gotP3DFilename = False
        self.started = False
        self.windowOpened = False
        self.windowPrc = None
        self.http = None
        if hasattr(PandaModules, 'HTTPClient'):
            self.http = PandaModules.HTTPClient.getGlobalPtr()
        self.Undefined = Undefined
        self.ConcreteStruct = ConcreteStruct
        self.nextScriptId = 0
        self.instanceId = None
        self.rootDir = None
        self.logDirectory = None
        self.superMirrorUrl = None
        self.installedPackages = []
        self.downloadingPackages = []
        self.hosts = {}
        self.altHost = None
        self.altHostMap = {}
        self.pandaHostUrl = PandaSystem.getPackageHostUrl()
        self.exceptionHandler = None
        self.downloadingPackages = []
        self.downloadTask = None
        self.multifileRoot = ExecutionEnvironment.getCwd().cStr()
        self.main = ScriptAttributes()
        self.main.stop = self.stop
        self.dom = None
        self.deferredEvals = []

        def defaultRequestFunc(*args):
            if args[1] == 'notify':
                return
            self.notify.info('Ignoring request: %s' % (args,))

        self.requestFunc = defaultRequestFunc
        self.windowProperties = None
        if AppRunnerGlobal.appRunner is None:
            AppRunnerGlobal.appRunner = self
        self.accept('AppRunner_startIfReady', self.__startIfReady)
        return

    def getToken(self, tokenName):
        return self.tokenDict.get(tokenName.lower(), None)

    def getTokenInt(self, tokenName):
        value = self.getToken(tokenName)
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                value = None

        return value

    def getTokenFloat(self, tokenName):
        value = self.getToken(tokenName)
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                value = None

        return value

    def getTokenBool(self, tokenName):
        value = self.getTokenInt(tokenName)
        if value is not None:
            value = bool(value)
        return value

    def installPackage(self, packageName, version=None, hostUrl=None):
        host = self.getHostWithAlt(hostUrl)
        if not host.downloadContentsFile(self.http):
            return False
        package = host.getPackage(packageName, version)
        if not package:
            self.notify.warning('Package %s %s not known on %s' % (packageName, version, hostUrl))
            return False
        return self.__rInstallPackage(package, [])

    def __rInstallPackage(self, package, nested):
        package.checkStatus()
        if not package.downloadDescFile(self.http):
            return False
        nested = nested[:] + [self]
        for (packageName, version, host) in package.requires:
            if host.downloadContentsFile(self.http):
                p2 = host.getPackage(packageName, version)
                if not p2:
                    self.notify.warning("Couldn't find %s %s on %s" % (packageName, version, host.hostUrl))
                elif p2 not in nested:
                    self.__rInstallPackage(p2, nested)

        if not package.downloadPackage(self.http):
            return False
        if not package.installPackage(self):
            return False
        self.notify.info('Package %s %s installed.' % (package.packageName, package.packageVersion))
        return True

    def getHostWithAlt(self, hostUrl):
        if hostUrl is None:
            hostUrl = self.pandaHostUrl
        altUrl = self.altHostMap.get(hostUrl, None)
        if altUrl:
            return self.getHost(altUrl)
        host = self.getHost(hostUrl)
        if self.altHost:
            host.downloadContentsFile(self.http)
            altUrl = host.altHosts.get(self.altHost, None)
            if altUrl:
                return self.getHost(altUrl)
        return host

    def getHost(self, hostUrl, hostDir=None):
        if not hostUrl:
            hostUrl = self.pandaHostUrl
        host = self.hosts.get(hostUrl, None)
        if not host:
            host = HostInfo(hostUrl, appRunner=self, hostDir=hostDir)
            self.hosts[hostUrl] = host
        return host

    def getHostWithDir(self, hostDir):
        host = HostInfo(None, hostDir=hostDir, appRunner=self)
        if not host.hasContentsFile:
            if not host.readContentsFile():
                return
        if not host.hostUrl:
            return
        host2 = self.hosts.get(host.hostUrl)
        if host2 is None:
            self.hosts[host.hostUrl] = host
            return host
        if host2.hostDir != host.hostDir:
            return
        return host2

    def deletePackages(self, packages):
        for (hostUrl, host) in self.hosts.items():
            packages = host.deletePackages(packages)
            if not host.packages:
                del self.hosts[hostUrl]
                self.__deleteHostFiles(host)

        return packages

    def __deleteHostFiles(self, host):
        self.notify.info('Deleting host %s: %s' % (host.hostUrl, host.hostDir))
        self.rmtree(host.hostDir)
        self.sendRequest('forget_package', host.hostUrl, '', '')

    def freshenFile(self, host, fileSpec, localPathname):
        if fileSpec.quickVerify(pathname=localPathname):
            return True
        doc = None
        if self.superMirrorUrl:
            url = PandaModules.URLSpec(self.superMirrorUrl + fileSpec.filename)
            self.notify.info('Freshening %s' % url)
            doc = self.http.getDocument(url)
        if not doc or not doc.isValid():
            url = PandaModules.URLSpec(host.hostUrlPrefix + fileSpec.filename)
            self.notify.info('Freshening %s' % url)
            doc = self.http.getDocument(url)
            if not doc.isValid():
                return False
        file = Filename.temporary('', 'p3d_')
        if not doc.downloadToFile(file):
            file.unlink()
            return False
        localPathname.makeDir()
        if not file.renameTo(localPathname):
            file.unlink()
            return False
        if not fileSpec.fullVerify(pathname=localPathname):
            self.notify.info('%s is still no good after downloading.' % url)
            return False
        return True

    def scanInstalledPackages(self):
        result = []
        hostsFilename = Filename(self.rootDir, 'hosts')
        hostsDir = ScanDirectoryNode(hostsFilename)
        for dirnode in hostsDir.nested:
            host = self.getHostWithDir(dirnode.pathname)
            hostData = InstalledHostData(host, dirnode)
            if host:
                for package in host.getAllPackages():
                    packageDir = package.getPackageDir()
                    if not packageDir.exists():
                        continue
                    subdir = dirnode.extractSubdir(packageDir)
                    if not subdir:
                        continue
                    packageData = InstalledPackageData(package, subdir)
                    hostData.packages.append(packageData)

            for subdir in dirnode.nested:
                packageData = InstalledPackageData(None, subdir)
                hostData.packages.append(packageData)

            result.append(hostData)

        return result

    def readConfigXml(self):
        if not hasattr(PandaModules, 'TiXmlDocument'):
            return
        from pandac.PandaModules import TiXmlDocument
        filename = Filename(self.rootDir, self.ConfigBasename)
        doc = TiXmlDocument(filename.toOsSpecific())
        if not doc.LoadFile():
            return
        xconfig = doc.FirstChildElement('config')
        if xconfig:
            maxDiskUsage = xconfig.Attribute('max_disk_usage')
            try:
                self.maxDiskUsage = int(maxDiskUsage or '')
            except ValueError:
                pass

    def writeConfigXml(self):
        from pandac.PandaModules import TiXmlDocument, TiXmlDeclaration, TiXmlElement
        filename = Filename(self.rootDir, self.ConfigBasename)
        doc = TiXmlDocument(filename.toOsSpecific())
        decl = TiXmlDeclaration('1.0', 'utf-8', '')
        doc.InsertEndChild(decl)
        xconfig = TiXmlElement('config')
        xconfig.SetAttribute('max_disk_usage', str(self.maxDiskUsage))
        doc.InsertEndChild(xconfig)
        tfile = Filename.temporary(self.rootDir.cStr(), '.xml')
        if doc.SaveFile(tfile.toOsSpecific()):
            tfile.renameTo(filename)

    def checkDiskUsage(self):
        totalSize = 0
        hosts = self.scanInstalledPackages()
        for hostData in hosts:
            for packageData in hostData.packages:
                totalSize += packageData.totalSize

        self.notify.info('Total Panda3D disk space used: %s MB' % ((totalSize + 524288) / 1048576))
        if self.verifyContents == self.P3DVCNever:
            return
        self.notify.info('Configured max usage is: %s MB' % ((self.maxDiskUsage + 524288) / 1048576))
        if totalSize <= self.maxDiskUsage:
            return
        usedPackages = []
        for hostData in hosts:
            for packageData in hostData.packages:
                if packageData.package and packageData.package.installed:
                    continue
                usedPackages.append((packageData.lastUse, packageData))

        usedPackages.sort()
        packages = []
        for (lastUse, packageData) in usedPackages:
            if totalSize <= self.maxDiskUsage:
                break
            totalSize -= packageData.totalSize
            if packageData.package:
                packages.append(packageData.package)
            else:
                print 'Deleting unknown package %s' % packageData.pathname
                self.rmtree(packageData.pathname)

        packages = self.deletePackages(packages)
        if packages:
            print 'Unable to delete %s packages' % len(packages)

    def stop(self):
        taskMgr.doMethodLater(0.5, sys.exit, 'exit')

    def run(self):
        try:
            taskMgr.run()
        except SystemExit:
            if hasattr(__builtin__, 'base'):
                base.destroy()
            self.notify.info('Normal exit.')
            raise
        except:
            if self.exceptionHandler and not self.interactiveConsole:
                self.exceptionHandler()
            else:
                raise

    def rmtree(self, filename):
        if filename.isDirectory():
            for child in filename.scanDirectory():
                self.rmtree(Filename(filename, child))

            if not filename.rmdir():
                print 'could not remove directory %s' % filename
        elif not filename.unlink():
            print 'could not delete %s' % filename

    def setSessionId(self, sessionId):
        self.sessionId = sessionId
        self.nextScriptId = self.sessionId * 1000 + 10000

    def initPackedAppEnvironment(self):
        if self.packedAppEnvironmentInitialized:
            return
        self.packedAppEnvironmentInitialized = True
        vfs = VirtualFileSystem.getGlobalPtr()
        VFSImporter.register()
        sys.path.append(self.multifileRoot)
        ExecutionEnvironment.setEnvironmentVariable('MAIN_DIR', Filename(self.multifileRoot).toOsSpecific())
        getModelPath().appendDirectory(self.multifileRoot)
        if not self.trueFileIO:
            __builtin__.file = file.file
            __builtin__.open = file.open
            os.listdir = file.listdir
            os.walk = file.walk
            os.path.isfile = file.isfile
            os.path.isdir = file.isdir
            os.path.exists = file.exists
            os.path.lexists = file.lexists
            os.path.getmtime = file.getmtime
            os.path.getsize = file.getsize
            sys.modules['glob'] = glob
        self.checkDiskUsage()

    def __startIfReady(self):
        if self.started:
            return
        if self.gotWindow and self.gotP3DFilename:
            self.started = True
            self.ignore('AppRunner_startIfReady')
            self.acceptOnce('window-event', self.__windowEvent)
            moduleName = 'main'
            if self.p3dPackage:
                mainName = self.p3dPackage.Attribute('main_module')
                if mainName:
                    moduleName = mainName
            self.initialAppImport = True
            __import__(moduleName)
            main = sys.modules[moduleName]
            if hasattr(main, 'main') and hasattr(main.main, '__call__'):
                main.main(self)
            self.initialAppImport = False
            if self.interactiveConsole:
                taskMgr.stop()

    def getPandaScriptObject(self):
        return self.main

    def setBrowserScriptObject(self, dom):
        self.dom = dom
        for expression in self.deferredEvals:
            self.scriptRequest('eval', self.dom, value=expression, needsResponse=False)

        self.deferredEvals = []

    def setInstanceInfo(self, rootDir, logDirectory, superMirrorUrl, verifyContents, main):
        self.rootDir = Filename.fromOsSpecific(rootDir)
        if logDirectory:
            self.logDirectory = Filename.fromOsSpecific(logDirectory)
        else:
            self.logDirectory = Filename(rootDir, 'log')
        self.superMirrorUrl = superMirrorUrl
        self.verifyContents = verifyContents
        if main is not None:
            self.main = main
        self.readConfigXml()
        return

    def addPackageInfo(self, name, platform, version, hostUrl, hostDir=None, recurse=False):
        host = self.getHost(hostUrl, hostDir=hostDir)
        if not host.hasContentsFile:
            host.readContentsFile()
        if not host.downloadContentsFile(self.http):
            message = 'Host %s cannot be downloaded, cannot preload %s.' % (hostUrl, name)
            raise OSError, message
        if name == 'panda3d' and not self.pandaHostUrl:
            self.pandaHostUrl = hostUrl
        if not platform:
            platform = None
        package = host.getPackage(name, version, platform=platform)
        if not package:
            if not recurse:
                if host.redownloadContentsFile(self.http):
                    return self.addPackageInfo(name, platform, version, hostUrl, hostDir=hostDir, recurse=True)
            message = "Couldn't find %s %s on %s" % (name, version, hostUrl)
            raise OSError, message
        package.checkStatus()
        if not package.downloadDescFile(self.http):
            message = "Couldn't get desc file for %s" % name
            raise OSError, message
        if not package.downloadPackage(self.http):
            message = "Couldn't download %s" % name
            raise OSError, message
        if not package.installPackage(self):
            message = "Couldn't install %s" % name
            raise OSError, message
        if package.guiApp:
            self.guiApp = True
            initAppForGui()
        return

    def setP3DFilename(self, p3dFilename, tokens, argv, instanceId, interactiveConsole, p3dOffset=0):
        self.instanceId = instanceId
        self.tokens = tokens
        self.argv = argv
        self.tokenDict = {}
        for (token, keyword) in tokens:
            self.tokenDict.setdefault(token, keyword)

        sys.argv = argv
        self.altHost = self.tokenDict.get('alt_host', None)
        self.notifyRequest('onpythonload')
        fname = Filename.fromOsSpecific(p3dFilename)
        vfs = VirtualFileSystem.getGlobalPtr()
        if not vfs.exists(fname):
            raise ArgumentError, 'No such file: %s' % p3dFilename
        fname.makeAbsolute()
        mf = Multifile()
        if p3dOffset == 0:
            if not mf.openRead(fname):
                raise ArgumentError, 'Not a Panda3D application: %s' % p3dFilename
        elif not mf.openRead(fname, p3dOffset):
            raise ArgumentError, 'Not a Panda3D application: %s at offset: %s' % (p3dFilename, p3dOffset)
        self.p3dInfo = None
        self.p3dPackage = None
        self.p3dConfig = None
        self.allowPythonDev = False
        i = mf.findSubfile('p3d_info.xml')
        if i >= 0 and hasattr(PandaModules, 'readXmlStream'):
            stream = mf.openReadSubfile(i)
            self.p3dInfo = PandaModules.readXmlStream(stream)
            mf.closeReadSubfile(stream)
        if self.p3dInfo:
            self.p3dPackage = self.p3dInfo.FirstChildElement('package')
        if self.p3dPackage:
            self.p3dConfig = self.p3dPackage.FirstChildElement('config')
            xhost = self.p3dPackage.FirstChildElement('host')
            while xhost:
                self.__readHostXml(xhost)
                xhost = xhost.NextSiblingElement('host')

        if self.p3dConfig:
            allowPythonDev = self.p3dConfig.Attribute('allow_python_dev')
            if allowPythonDev:
                self.allowPythonDev = int(allowPythonDev)
            guiApp = self.p3dConfig.Attribute('gui_app')
            if guiApp:
                self.guiApp = int(guiApp)
            trueFileIO = self.p3dConfig.Attribute('true_file_io')
            if trueFileIO:
                self.trueFileIO = int(trueFileIO)
        if not self.allowPythonDev and interactiveConsole:
            raise StandardError, 'Impossible, interactive_console set without allow_python_dev.'
        self.interactiveConsole = interactiveConsole
        if self.allowPythonDev:
            ConfigVariableString('frame-rate-meter-text-pattern').setValue('allow_python_dev %0.1f fps')
        if self.guiApp:
            initAppForGui()
        self.initPackedAppEnvironment()
        vfs.mount(mf, self.multifileRoot, vfs.MFReadOnly)
        VFSImporter.reloadSharedPackages()
        self.loadMultifilePrcFiles(mf, self.multifileRoot)
        self.gotP3DFilename = True
        messenger.send('AppRunner_startIfReady', taskChain='default')
        return

    def __readHostXml(self, xhost):
        url = xhost.Attribute('url')
        host = self.getHost(url)
        host.readHostXml(xhost)
        if self.altHost:
            xalthost = xhost.FirstChildElement('alt_host')
            while xalthost:
                keyword = xalthost.Attribute('keyword')
                if keyword == self.altHost:
                    origUrl = xhost.Attribute('url')
                    newUrl = xalthost.Attribute('url')
                    self.altHostMap[origUrl] = newUrl
                    break
                xalthost = xalthost.NextSiblingElement('alt_host')

    def loadMultifilePrcFiles(self, mf, root):
        for f in mf.getSubfileNames():
            fn = Filename(f)
            if fn.getDirname() == '' and fn.getExtension() == 'prc':
                pathname = '%s/%s' % (root, f)
                data = file.open(Filename(pathname), 'r').read()
                loadPrcFileData(pathname, data)

    def __clearWindowProperties(self):
        if self.windowPrc:
            unloadPrcFile(self.windowPrc)
            self.windowPrc = None
        WindowProperties.clearDefault()
        return

    def setupWindow(self, windowType, x, y, width, height, parent):
        if self.started and base.win:
            wp = WindowProperties()
            if x or y or windowType == 'embedded':
                wp.setOrigin(x, y)
            if width or height:
                wp.setSize(width, height)
            if windowType == 'embedded':
                wp.setParentWindow(parent)
            wp.setFullscreen(False)
            base.win.requestProperties(wp)
            self.windowProperties = wp
            return
        self.__clearWindowProperties()
        if windowType == 'hidden':
            data = 'window-type none\n'
        else:
            data = 'window-type onscreen\n'
        wp = WindowProperties.getDefault()
        wp.clearParentWindow()
        wp.clearOrigin()
        wp.clearSize()
        wp.setFullscreen(False)
        if windowType == 'fullscreen':
            wp.setFullscreen(True)
        if windowType == 'embedded':
            wp.setParentWindow(parent)
        if x or y or windowType == 'embedded':
            wp.setOrigin(x, y)
        if width or height:
            wp.setSize(width, height)
        self.windowProperties = wp
        self.windowPrc = loadPrcFileData('setupWindow', data)
        WindowProperties.setDefault(wp)
        self.gotWindow = True
        messenger.send('AppRunner_startIfReady', taskChain='default')

    def setRequestFunc(self, func):
        self.requestFunc = func

    def sendRequest(self, request, *args):
        return self.requestFunc(self.instanceId, request, args)

    def __windowEvent(self, win):
        if not self.windowOpened:
            self.windowOpened = True
            self.__clearWindowProperties()
            self.notifyRequest('onwindowopen')

    def notifyRequest(self, message):
        self.sendRequest('notify', message.lower())

    def evalScript(self, expression, needsResponse=False):
        if not self.dom:
            self.deferredEvals.append(expression)
        else:
            return self.scriptRequest('eval', self.dom, value=expression, needsResponse=needsResponse)

    def scriptRequest(self, operation, object, propertyName='', value=None, needsResponse=True):
        uniqueId = self.nextScriptId
        self.nextScriptId = (self.nextScriptId + 1) % 4294967295
        self.sendRequest('script', operation, object, propertyName, value, needsResponse, uniqueId)
        if needsResponse:
            result = self.sendRequest('wait_script_response', uniqueId)
            return result

    def dropObject(self, objectId):
        self.sendRequest('drop_p3dobj', objectId)


def dummyAppRunner(tokens=[], argv=None):
    if AppRunnerGlobal.appRunner:
        print 'Already have AppRunner, not creating a new one.'
        return AppRunnerGlobal.appRunner
    appRunner = AppRunner()
    appRunner.dummy = True
    AppRunnerGlobal.appRunner = appRunner
    platform = PandaSystem.getPlatform()
    version = PandaSystem.getPackageVersionString()
    hostUrl = PandaSystem.getPackageHostUrl()
    if platform.startswith('win'):
        rootDir = Filename(Filename.getUserAppdataDirectory(), 'Panda3D')
    elif platform.startswith('osx'):
        rootDir = Filename(Filename.getHomeDirectory(), 'Library/Caches/Panda3D')
    else:
        rootDir = Filename(Filename.getHomeDirectory(), '.panda3d')
    appRunner.rootDir = rootDir
    appRunner.logDirectory = Filename(rootDir, 'log')
    appRunner.addPackageInfo('panda3d', platform, version, hostUrl)
    appRunner.tokens = tokens
    appRunner.tokenDict = dict(tokens)
    if argv is None:
        argv = sys.argv
    appRunner.argv = argv
    appRunner.altHost = appRunner.tokenDict.get('alt_host', None)
    appRunner.p3dInfo = None
    appRunner.p3dPackage = None
    cwd = ExecutionEnvironment.getCwd()
    vfs = VirtualFileSystem.getGlobalPtr()
    vfs.mount(cwd, appRunner.multifileRoot, vfs.MFReadOnly)
    appRunner.initPackedAppEnvironment()
    return appRunner