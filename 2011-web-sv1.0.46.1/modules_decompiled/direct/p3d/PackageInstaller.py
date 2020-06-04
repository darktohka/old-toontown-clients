# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\PackageInstaller.py
from direct.showbase.DirectObject import DirectObject
from direct.stdpy.threading import Lock, RLock
from direct.showbase.MessengerGlobal import messenger
from direct.task.TaskManagerGlobal import taskMgr
from direct.p3d.PackageInfo import PackageInfo
from pandac.PandaModules import TPLow, PStatCollector
from direct.directnotify.DirectNotifyGlobal import directNotify

class PackageInstaller(DirectObject):
    __module__ = __name__
    notify = directNotify.newCategory('PackageInstaller')
    globalLock = Lock()
    nextUniqueId = 1
    S_initial = 0
    S_ready = 1
    S_started = 2
    S_done = 3

    class PendingPackage:
        __module__ = __name__
        notify = directNotify.newCategory('PendingPackage')

        def __init__(self, packageName, version, host):
            self.packageName = packageName
            self.version = version
            self.host = host
            self.package = PackageInfo(host, packageName, version)
            self.done = False
            self.success = False
            self.notified = False
            self.calledPackageStarted = False
            self.calledPackageFinished = False
            self.downloadEffort = 0
            self.prevDownloadedEffort = 0

        def __cmp__(self, pp):
            return cmp((self.packageName, self.version, self.host), (
             pp.packageName, pp.version, pp.host))

        def getProgress(self):
            return self.package.downloadProgress

        def checkDescFile(self):
            if not self.host.hasCurrentContentsFile():
                return False
            package = self.host.getPackage(self.packageName, self.version)
            if not package:
                self.notify.warning('Package %s %s not known on %s' % (self.packageName, self.version, self.host.hostUrl))
                return False
            self.package = package
            self.package.checkStatus()
            if not self.package.hasDescFile:
                return False
            self.downloadEffort = self.package.getDownloadEffort()
            self.prevDownloadEffort = 0
            if self.downloadEffort == 0:
                self.prevDownloadedEffort = self.package.getPrevDownloadedEffort()
            return True

        def getDescFile(self, http):
            if not self.host.downloadContentsFile(http):
                return False
            package = self.host.getPackage(self.packageName, self.version)
            if not package:
                self.notify.warning('Package %s %s not known on %s' % (self.packageName, self.version, self.host.hostUrl))
                return False
            self.package = package
            if not self.package.downloadDescFile(http):
                return False
            self.package.checkStatus()
            self.downloadEffort = self.package.getDownloadEffort()
            self.prevDownloadEffort = 0
            if self.downloadEffort == 0:
                self.prevDownloadedEffort = self.package.getPrevDownloadedEffort()
            return True

    def __init__(self, appRunner, taskChain='default'):
        self.globalLock.acquire()
        try:
            self.uniqueId = PackageInstaller.nextUniqueId
            PackageInstaller.nextUniqueId += 1
        finally:
            self.globalLock.release()
        self.appRunner = appRunner
        self.taskChain = taskChain
        if taskChain != 'default' and not taskMgr.hasTaskChain(self.taskChain):
            taskMgr.setupTaskChain(self.taskChain, numThreads=1, threadPriority=TPLow)
        self.callbackLock = Lock()
        self.calledDownloadStarted = False
        self.calledDownloadFinished = False
        self.packageLock = RLock()
        self.packages = []
        self.state = self.S_initial
        self.needsDescFile = []
        self.descFileTask = None
        self.needsDownload = []
        self.downloadTask = None
        self.earlyDone = []
        self.done = []
        self.failed = []
        self.progressTask = None
        self.accept('PackageInstaller-%s-allHaveDesc' % self.uniqueId, self.__allHaveDesc)
        self.accept('PackageInstaller-%s-packageStarted' % self.uniqueId, self.__packageStarted)
        self.accept('PackageInstaller-%s-packageDone' % self.uniqueId, self.__packageDone)
        return

    def destroy(self):
        self.cleanup()

    def cleanup(self):
        self.packageLock.acquire()
        try:
            if self.descFileTask:
                taskMgr.remove(self.descFileTask)
                self.descFileTask = None
            if self.downloadTask:
                taskMgr.remove(self.downloadTask)
                self.downloadTask = None
        finally:
            self.packageLock.release()
        if self.progressTask:
            taskMgr.remove(self.progressTask)
            self.progressTask = None
        self.ignoreAll()
        return

    def addPackage(self, packageName, version=None, hostUrl=None):
        if self.state != self.S_initial:
            raise ValueError, 'addPackage called after donePackages'
        host = self.appRunner.getHostWithAlt(hostUrl)
        pp = self.PendingPackage(packageName, version, host)
        self.packageLock.acquire()
        try:
            self.__internalAddPackage(pp)
        finally:
            self.packageLock.release()

    def __internalAddPackage(self, pp):
        if pp in self.packages:
            return
        self.packages.append(pp)
        self.needsDescFile.append(pp)
        if not self.descFileTask:
            self.descFileTask = taskMgr.add(self.__getDescFileTask, 'getDescFile', taskChain=self.taskChain)

    def donePackages(self):
        if self.state != self.S_initial:
            return
        for pp in self.earlyDone:
            self.__donePackage(pp, True)

        self.earlyDone = []
        self.packageLock.acquire()
        try:
            if self.state != self.S_initial:
                return
            self.state = self.S_ready
            if not self.needsDescFile:
                self.__prepareToStart()
        finally:
            self.packageLock.release()
        if not self.packages:
            self.__callDownloadFinished(True)

    def downloadStarted(self):
        self.notify.info('downloadStarted')

    def packageStarted(self, package):
        self.notify.debug('packageStarted: %s' % package.packageName)

    def packageProgress(self, package, progress):
        self.notify.debug('packageProgress: %s %s' % (package.packageName, progress))

    def downloadProgress(self, overallProgress):
        self.notify.debug('downloadProgress: %s' % overallProgress)

    def packageFinished(self, package, success):
        self.notify.info('packageFinished: %s %s' % (package.packageName, success))

    def downloadFinished(self, success):
        self.notify.info('downloadFinished: %s' % success)

    def __prepareToStart(self):
        if not self.needsDownload:
            self.state = self.S_done
            return False
        self.state = self.S_started
        self.downloadTask = taskMgr.add(self.__downloadPackageTask, 'downloadPackage', taskChain=self.taskChain)
        self.progressTask = taskMgr.add(self.__progressTask, 'packageProgress')
        return True

    def __allHaveDesc(self):
        working = True
        self.packageLock.acquire()
        try:
            if self.state == self.S_ready:
                working = self.__prepareToStart()
        finally:
            self.packageLock.release()
        if not working:
            self.__callDownloadFinished(True)

    def __packageStarted(self, pp):
        self.__callDownloadStarted()
        self.__callPackageStarted(pp)

    def __packageDone(self, pp):
        self.__callPackageFinished(pp, pp.success)
        pp.notified = True
        success = True
        allDone = True
        self.packageLock.acquire()
        try:
            for pp in self.packages:
                if pp.notified:
                    success = success and pp.success
                else:
                    allDone = False

        finally:
            self.packageLock.release()
        if allDone:
            self.__callDownloadFinished(success)

    def __callPackageStarted(self, pp):
        self.callbackLock.acquire()
        try:
            if not pp.calledPackageStarted:
                self.packageStarted(pp.package)
                self.packageProgress(pp.package, 0)
                pp.calledPackageStarted = True
        finally:
            self.callbackLock.release()

    def __callPackageFinished(self, pp, success):
        self.callbackLock.acquire()
        try:
            if not pp.calledPackageFinished:
                if success:
                    self.packageProgress(pp.package, 1)
                self.packageFinished(pp.package, success)
                pp.calledPackageFinished = True
        finally:
            self.callbackLock.release()

    def __callDownloadStarted(self):
        self.callbackLock.acquire()
        try:
            if not self.calledDownloadStarted:
                self.downloadStarted()
                self.downloadProgress(0)
                self.calledDownloadStarted = True
        finally:
            self.callbackLock.release()

    def __callDownloadFinished(self, success):
        self.callbackLock.acquire()
        try:
            if not self.calledDownloadFinished:
                if success:
                    self.downloadProgress(1)
                self.downloadFinished(success)
                self.calledDownloadFinished = True
        finally:
            self.callbackLock.release()

    def __getDescFileTask(self, task):
        self.packageLock.acquire()
        try:
            if not self.needsDescFile:
                self.descFileTask = None
                eventName = 'PackageInstaller-%s-allHaveDesc' % self.uniqueId
                messenger.send(eventName, taskChain='default')
                return task.done
            pp = self.needsDescFile[0]
            del self.needsDescFile[0]
        finally:
            self.packageLock.release()
        if not pp.checkDescFile():
            if not pp.getDescFile(self.appRunner.http):
                self.__donePackage(pp, False)
                return task.cont
        self.packageLock.acquire()
        try:
            for (packageName, version, host) in pp.package.requires:
                pp2 = self.PendingPackage(packageName, version, host)
                self.__internalAddPackage(pp2)

            self.needsDownload.append(pp)
        finally:
            self.packageLock.release()
        return task.cont

    def __downloadPackageTask(self, task):
        while True:
            self.packageLock.acquire()
            try:
                if self.state == self.S_done or not self.needsDownload:
                    self.downloadTask = None
                    self.packageLock.release()
                    yield task.done
                    return
                pp = self.needsDownload[0]
                del self.needsDownload[0]
            except:
                self.packageLock.release()
                raise

            self.packageLock.release()
            eventName = 'PackageInstaller-%s-packageStarted' % self.uniqueId
            messenger.send(eventName, [pp], taskChain='default')
            if not pp.package.hasPackage:
                for token in pp.package.downloadPackageGenerator(self.appRunner.http):
                    if token == pp.package.stepContinue:
                        yield task.cont
                    else:
                        break

                if token != pp.package.stepComplete:
                    pc = PStatCollector(':App:PackageInstaller:donePackage:%s' % pp.package.packageName)
                    pc.start()
                    self.__donePackage(pp, False)
                    pc.stop()
                    yield task.cont
                    continue
            pc = PStatCollector(':App:PackageInstaller:donePackage:%s' % pp.package.packageName)
            pc.start()
            self.__donePackage(pp, True)
            pc.stop()

        return

    def __donePackage(self, pp, success):
        if success:
            pc = PStatCollector(':App:PackageInstaller:install:%s' % pp.package.packageName)
            pc.start()
            pp.package.installPackage(self.appRunner)
            pc.stop()
        self.packageLock.acquire()
        try:
            pp.done = True
            pp.success = success
            if success:
                self.done.append(pp)
            else:
                self.failed.append(pp)
        finally:
            self.packageLock.release()
        eventName = 'PackageInstaller-%s-packageDone' % self.uniqueId
        messenger.send(eventName, [pp], taskChain='default')

    def __progressTask(self, task):
        self.callbackLock.acquire()
        try:
            if not self.calledDownloadStarted:
                return task.cont
            if self.calledDownloadFinished:
                self.progressTask = None
                return task.done
            downloadEffort = 0
            currentDownloadSize = 0
            for pp in self.packages:
                downloadEffort += pp.downloadEffort + pp.prevDownloadedEffort
                packageProgress = pp.getProgress()
                currentDownloadSize += pp.downloadEffort * packageProgress + pp.prevDownloadedEffort
                if pp.calledPackageStarted and not pp.calledPackageFinished:
                    self.packageProgress(pp.package, packageProgress)

            if not downloadEffort:
                progress = 1
            else:
                progress = float(currentDownloadSize) / float(downloadEffort)
            self.downloadProgress(progress)
        finally:
            self.callbackLock.release()
        return task.cont