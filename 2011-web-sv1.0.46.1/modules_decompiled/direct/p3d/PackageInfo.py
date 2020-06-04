# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\PackageInfo.py
from pandac.PandaModules import Filename, URLSpec, DocumentSpec, Ramfile, Multifile, Decompressor, EUOk, EUSuccess, VirtualFileSystem, Thread, getModelPath, ExecutionEnvironment, PStatCollector, TiXmlDocument, TiXmlDeclaration, TiXmlElement
from pandac import PandaModules
from libpandaexpress import ConfigVariableInt
from direct.p3d.FileSpec import FileSpec
from direct.p3d.ScanDirectoryNode import ScanDirectoryNode
from direct.showbase import VFSImporter
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task.TaskManagerGlobal import taskMgr
import os, sys, random, time, copy

class PackageInfo:
    __module__ = __name__
    notify = directNotify.newCategory('PackageInfo')
    downloadFactor = 1
    uncompressFactor = 0.01
    unpackFactor = 0.01
    patchFactor = 0.01
    stepComplete = 1
    stepFailed = 2
    restartDownload = 3
    stepContinue = 4
    UsageBasename = 'usage.xml'

    class InstallStep:
        __module__ = __name__

        def __init__(self, func, bytes, factor, stepType):
            self.__funcPtr = func
            self.bytesNeeded = bytes
            self.bytesDone = 0
            self.bytesFactor = factor
            self.stepType = stepType
            self.pStatCol = PStatCollector(':App:PackageInstaller:%s' % stepType)

        def func(self):
            self.pStatCol.start()
            for token in self.__funcPtr(self):
                self.pStatCol.stop()
                yield token
                self.pStatCol.start()

            self.pStatCol.stop()
            raise StopIteration

        def getEffort(self):
            return self.bytesNeeded * self.bytesFactor

        def getProgress(self):
            if self.bytesNeeded == 0:
                return 1
            return min(float(self.bytesDone) / float(self.bytesNeeded), 1)

    def __init__(self, host, packageName, packageVersion, platform=None, solo=False, asMirror=False):
        self.host = host
        self.packageName = packageName
        self.packageVersion = packageVersion
        self.platform = platform
        self.solo = solo
        self.asMirror = asMirror
        self.http = None
        self.packageDir = None
        self.descFile = None
        self.importDescFile = None
        self.hasDescFile = False
        self.patchVersion = None
        self.displayName = None
        self.guiApp = False
        self.uncompressedArchive = None
        self.compressedArchive = None
        self.extracts = []
        self.requires = []
        self.installPlans = None
        self.downloadProgress = 0
        self.hasPackage = False
        self.installed = False
        self.updated = False
        self.diskSpace = None
        return

    def getPackageDir(self):
        if not self.packageDir:
            if not self.host.hasContentsFile:
                if not self.host.readContentsFile():
                    self.host.downloadContentsFile(self.http)
            self.packageDir = Filename(self.host.hostDir, self.packageName)
            if self.packageVersion:
                self.packageDir = Filename(self.packageDir, self.packageVersion)
            if self.host.perPlatform:
                if self.platform:
                    self.packageDir = Filename(self.packageDir, self.platform)
        return self.packageDir

    def getDownloadEffort(self):
        if not self.installPlans:
            return 0
        plan = self.installPlans[0]
        size = sum(map(lambda step: step.getEffort(), plan))
        return size

    def getPrevDownloadedEffort(self):
        effort = 0
        if self.compressedArchive:
            effort += self.compressedArchive.size * self.downloadFactor
        if self.uncompressedArchive:
            effort += self.uncompressedArchive.size * self.uncompressFactor
        return effort

    def getFormattedName(self):
        if self.displayName:
            name = self.displayName
        else:
            name = self.packageName
            if self.packageVersion:
                name += ' %s' % self.packageVersion
        if self.patchVersion:
            name += ' rev %s' % self.patchVersion
        return name

    def setupFilenames(self):
        (dirname, basename) = self.descFile.filename.rsplit('/', 1)
        self.descFileDirname = dirname
        self.descFileBasename = basename

    def checkStatus(self):
        if self.hasPackage:
            return True
        if not self.hasDescFile:
            filename = Filename(self.getPackageDir(), self.descFileBasename)
            if self.descFile.quickVerify(self.getPackageDir(), pathname=filename, notify=self.notify):
                if self.__readDescFile():
                    return self.hasPackage
        if self.hasDescFile:
            if self.__checkArchiveStatus():
                self.hasPackage = True
        return self.hasPackage

    def hasCurrentDescFile(self):
        if not self.host.hasCurrentContentsFile():
            return False
        return self.hasDescFile

    def downloadDescFile(self, http):
        for token in self.downloadDescFileGenerator(http):
            if token != self.stepContinue:
                break
            Thread.considerYield()

        return token == self.stepComplete

    def downloadDescFileGenerator(self, http):
        if self.hasDescFile:
            yield self.stepComplete
            return
        if self.host.appRunner and self.host.appRunner.verifyContents != self.host.appRunner.P3DVCNever:
            self.http = http
            func = lambda step, self=self: self.__downloadFile(None, self.descFile, urlbase=self.descFile.filename, filename=self.descFileBasename)
            step = self.InstallStep(func, self.descFile.size, self.downloadFactor, 'downloadDesc')
            for token in step.func():
                if token == self.stepContinue:
                    yield token
                else:
                    break

            while token == self.restartDownload:
                func = lambda step, self=self: self.__downloadFile(None, self.descFile, urlbase=self.descFile.filename, filename=self.descFileBasename)
                step = self.InstallStep(func, self.descFile.size, self.downloadFactor, 'downloadDesc')
                for token in step.func():
                    if token == self.stepContinue:
                        yield token
                    else:
                        break

            if token == self.stepFailed:
                yield self.stepFailed
                return
            filename = Filename(self.getPackageDir(), self.descFileBasename)
            os.chmod(filename.toOsSpecific(), 292)
        if not self.__readDescFile():
            self.notify.warning('Failure reading %s' % filename)
            yield self.stepFailed
            return
        yield self.stepComplete

    def __readDescFile(self):
        if self.hasDescFile:
            return True
        if self.solo:
            self.hasDescFile = True
            self.hasPackage = True
            return True
        filename = Filename(self.getPackageDir(), self.descFileBasename)
        if not hasattr(PandaModules, 'TiXmlDocument'):
            return False
        doc = PandaModules.TiXmlDocument(filename.toOsSpecific())
        if not doc.LoadFile():
            return False
        xpackage = doc.FirstChildElement('package')
        if not xpackage:
            return False
        try:
            self.patchVersion = int(xpackage.Attribute('patch_version') or '')
        except ValueError:
            self.patchVersion = None

        self.displayName = None
        xconfig = xpackage.FirstChildElement('config')
        if xconfig:
            self.displayName = xconfig.Attribute('display_name')
            guiApp = xconfig.Attribute('gui_app')
            if guiApp:
                self.guiApp = int(guiApp)
        xuncompressedArchive = xpackage.FirstChildElement('uncompressed_archive')
        if xuncompressedArchive:
            self.uncompressedArchive = FileSpec()
            self.uncompressedArchive.loadXml(xuncompressedArchive)
        xcompressedArchive = xpackage.FirstChildElement('compressed_archive')
        if xcompressedArchive:
            self.compressedArchive = FileSpec()
            self.compressedArchive.loadXml(xcompressedArchive)
        self.extracts = []
        xextract = xpackage.FirstChildElement('extract')
        while xextract:
            file = FileSpec()
            file.loadXml(xextract)
            self.extracts.append(file)
            xextract = xextract.NextSiblingElement('extract')

        self.requires = []
        xrequires = xpackage.FirstChildElement('requires')
        while xrequires:
            packageName = xrequires.Attribute('name')
            version = xrequires.Attribute('version')
            hostUrl = xrequires.Attribute('host')
            if packageName and hostUrl:
                host = self.host.appRunner.getHostWithAlt(hostUrl)
                self.requires.append((packageName, version, host))
            xrequires = xrequires.NextSiblingElement('requires')

        self.hasDescFile = True
        if self.__checkArchiveStatus():
            self.hasPackage = True
            return True
        self.__buildInstallPlans()
        return True

    def __buildInstallPlans(self):
        pc = PStatCollector(':App:PackageInstaller:buildInstallPlans')
        pc.start()
        self.hasPackage = False
        if self.host.appRunner and self.host.appRunner.verifyContents == self.host.appRunner.P3DVCNever:
            self.installPlans = []
            pc.stop()
            return
        if self.asMirror:
            downloadSize = self.compressedArchive.size
            func = lambda step, fileSpec=self.compressedArchive: self.__downloadFile(step, fileSpec, allowPartial=True)
            step = self.InstallStep(func, downloadSize, self.downloadFactor, 'download')
            installPlan = [step]
            self.installPlans = [installPlan]
            pc.stop()
            return
        self.installPlans = None
        unpackSize = 0
        for file in self.extracts:
            unpackSize += file.size

        step = self.InstallStep(self.__unpackArchive, unpackSize, self.unpackFactor, 'unpack')
        planA = [step]
        self.uncompressedArchive.actualFile = None
        if self.uncompressedArchive.quickVerify(self.getPackageDir(), notify=self.notify):
            self.installPlans = [
             planA]
            pc.stop()
            return
        if self.compressedArchive.quickVerify(self.getPackageDir(), notify=self.notify):
            uncompressSize = self.uncompressedArchive.size
            step = self.InstallStep(self.__uncompressArchive, uncompressSize, self.uncompressFactor, 'uncompress')
            planA = [step] + planA
            self.installPlans = [planA]
            pc.stop()
            return
        planB = planA[:]
        uncompressSize = self.uncompressedArchive.size
        step = self.InstallStep(self.__uncompressArchive, uncompressSize, self.uncompressFactor, 'uncompress')
        planB = [step] + planB
        downloadSize = self.compressedArchive.size
        func = lambda step, fileSpec=self.compressedArchive: self.__downloadFile(step, fileSpec, allowPartial=True)
        step = self.InstallStep(func, downloadSize, self.downloadFactor, 'download')
        planB = [step] + planB
        pathname = Filename(self.getPackageDir(), self.uncompressedArchive.filename)
        fileSpec = self.uncompressedArchive.actualFile
        if fileSpec is None and pathname.exists():
            fileSpec = FileSpec()
            fileSpec.fromFile(self.getPackageDir(), self.uncompressedArchive.filename)
        plan = None
        if fileSpec:
            plan = self.__findPatchChain(fileSpec)
        if plan:
            planA = plan + planA
            self.installPlans = [planA, planB]
        else:
            self.installPlans = [planB]
        for retry in range(ConfigVariableInt('package-full-dl-retries', 1)):
            self.installPlans.append(planB[:])

        pc.stop()
        return

    def __scanDirectoryRecursively(self, dirname):
        contents = []
        for (dirpath, dirnames, filenames) in os.walk(dirname.toOsSpecific()):
            dirpath = Filename.fromOsSpecific(dirpath)
            if dirpath == dirname:
                dirpath = Filename('')
            else:
                dirpath.makeRelativeTo(dirname)
            for filename in filenames:
                contents.append(Filename(dirpath, filename))

        return contents

    def __removeFileFromList(self, contents, filename):
        try:
            contents.remove(Filename(filename))
        except ValueError:
            pass

    def __checkArchiveStatus(self):
        if self.host.appRunner and self.host.appRunner.verifyContents == self.host.appRunner.P3DVCNever:
            return True
        contents = self.__scanDirectoryRecursively(self.getPackageDir())
        self.__removeFileFromList(contents, self.descFileBasename)
        self.__removeFileFromList(contents, self.compressedArchive.filename)
        self.__removeFileFromList(contents, self.UsageBasename)
        if not self.asMirror:
            self.__removeFileFromList(contents, self.uncompressedArchive.filename)
            for file in self.extracts:
                self.__removeFileFromList(contents, file.filename)

        for filename in contents:
            self.notify.info('Removing %s' % filename)
            pathname = Filename(self.getPackageDir(), filename)
            pathname.unlink()
            self.updated = True

        if self.asMirror:
            return self.compressedArchive.quickVerify(self.getPackageDir(), notify=self.notify)
        allExtractsOk = True
        if not self.uncompressedArchive.quickVerify(self.getPackageDir(), notify=self.notify):
            self.notify.debug('File is incorrect: %s' % self.uncompressedArchive.filename)
            allExtractsOk = False
        if allExtractsOk:
            pathname = Filename(self.getPackageDir(), self.compressedArchive.filename)
            pathname.unlink()
            for file in self.extracts:
                if not file.quickVerify(self.getPackageDir(), notify=self.notify):
                    self.notify.debug('File is incorrect: %s' % file.filename)
                    allExtractsOk = False
                    break

        if allExtractsOk:
            self.notify.debug('All %s extracts of %s seem good.' % (len(self.extracts), self.packageName))
        return allExtractsOk

    def __updateStepProgress(self, step):
        size = self.totalPlanCompleted + self.currentStepEffort * step.getProgress()
        self.downloadProgress = min(float(size) / float(self.totalPlanSize), 1)

    def downloadPackage(self, http):
        for token in self.downloadPackageGenerator(http):
            if token != self.stepContinue:
                break
            Thread.considerYield()

        return token == self.stepComplete

    def downloadPackageGenerator(self, http):
        if self.hasPackage:
            yield self.stepComplete
            return
        if self.host.appRunner and self.host.appRunner.verifyContents == self.host.appRunner.P3DVCNever:
            yield self.stepComplete
            return
        self.http = http
        for token in self.__followInstallPlans():
            if token == self.stepContinue:
                yield token
            else:
                break

        while token == self.restartDownload:
            for token in self.downloadDescFileGenerator(http):
                if token == self.stepContinue:
                    yield token
                else:
                    break

            if token == self.stepComplete:
                for token in self.__followInstallPlans():
                    if token == self.stepContinue:
                        yield token
                    else:
                        break

        if token == self.stepFailed:
            yield self.stepFailed
            return
        yield self.stepComplete

    def __followInstallPlans(self):
        if not self.installPlans:
            self.__buildInstallPlans()
        installPlans = self.installPlans
        self.installPlans = None
        for plan in installPlans:
            self.totalPlanSize = sum(map(lambda step: step.getEffort(), plan))
            self.totalPlanCompleted = 0
            self.downloadProgress = 0
            planFailed = False
            for step in plan:
                self.currentStepEffort = step.getEffort()
                for token in step.func():
                    if token == self.stepContinue:
                        yield token
                    else:
                        break

                if token == self.restartDownload:
                    yield token
                if token == self.stepFailed:
                    planFailed = True
                    break
                self.totalPlanCompleted += self.currentStepEffort

            if not planFailed:
                yield self.stepComplete
                return
            if taskMgr.destroyed:
                yield self.stepFailed
                return

        yield self.stepFailed
        return

    def __findPatchChain(self, fileSpec):
        from direct.p3d.PatchMaker import PatchMaker
        patchMaker = PatchMaker(self.getPackageDir())
        patchChain = patchMaker.getPatchChainToCurrent(self.descFileBasename, fileSpec)
        if patchChain is None:
            patchMaker.cleanup()
            return
        plan = []
        for patchfile in patchChain:
            downloadSize = patchfile.file.size
            func = lambda step, fileSpec=patchfile.file: self.__downloadFile(step, fileSpec, allowPartial=True)
            step = self.InstallStep(func, downloadSize, self.downloadFactor, 'download')
            plan.append(step)
            patchSize = patchfile.targetFile.size
            func = lambda step, patchfile=patchfile: self.__applyPatch(step, patchfile)
            step = self.InstallStep(func, patchSize, self.patchFactor, 'patch')
            plan.append(step)

        patchMaker.cleanup()
        return plan

    def __downloadFile(self, step, fileSpec, urlbase=None, filename=None, allowPartial=False):
        if self.host.appRunner and self.host.appRunner.verifyContents == self.host.appRunner.P3DVCNever:
            yield self.stepFailed
            return
        self.updated = True
        if not urlbase:
            urlbase = self.descFileDirname + '/' + fileSpec.filename
        tryUrls = []
        if self.host.appRunner and self.host.appRunner.superMirrorUrl:
            url = self.host.appRunner.superMirrorUrl + urlbase
            tryUrls.append((url, False))
        if self.host.mirrors:
            mirrors = self.host.mirrors[:]
            for i in range(2):
                mirror = random.choice(mirrors)
                mirrors.remove(mirror)
                url = mirror + urlbase
                tryUrls.append((url, False))
                if not mirrors:
                    break

        url = self.host.downloadUrlPrefix + urlbase
        tryUrls.append((url, False))
        tryUrls.append((url, True))
        for (url, cacheBust) in tryUrls:
            request = DocumentSpec(url)
            if cacheBust:
                url += '?' + str(int(time.time()))
                request = DocumentSpec(url)
                request.setCacheControl(DocumentSpec.CCNoCache)
            self.notify.info('%s downloading %s' % (self.packageName, url))
            if not filename:
                filename = fileSpec.filename
            targetPathname = Filename(self.getPackageDir(), filename)
            targetPathname.setBinary()
            channel = self.http.makeChannel(False)
            bytesStarted = 0
            if allowPartial:
                if not cacheBust and targetPathname.exists():
                    bytesStarted = targetPathname.getFileSize()
                if bytesStarted < 1024 * 1024:
                    bytesStarted = 0
                elif bytesStarted >= fileSpec.size:
                    bytesStarted = 0
                if bytesStarted:
                    self.notify.info('Resuming %s after %s bytes already downloaded' % (url, bytesStarted))
                    os.chmod(targetPathname.toOsSpecific(), 420)
                    channel.beginGetSubdocument(request, bytesStarted, 0)
                else:
                    targetPathname.makeDir()
                    targetPathname.unlink()
                    channel.beginGetDocument(request)
                channel.downloadToFile(targetPathname)
                while channel.run():
                    if step:
                        step.bytesDone = channel.getBytesDownloaded() + channel.getFirstByteDelivered()
                        if step.bytesDone > step.bytesNeeded:
                            self.notify.warning('Got more data than expected for download %s' % url)
                            break
                        self.__updateStepProgress(step)
                    if taskMgr.destroyed:
                        self.notify.warning('Task Manager destroyed, aborting %s' % url)
                        yield self.stepFailed
                        return
                    yield self.stepContinue

                if step:
                    step.bytesDone = channel.getBytesDownloaded() + channel.getFirstByteDelivered()
                    self.__updateStepProgress(step)
                channel.isValid() or self.notify.warning('Failed to download %s' % url)
            elif not fileSpec.fullVerify(self.getPackageDir(), pathname=targetPathname, notify=self.notify):
                self.notify.warning('After downloading, %s incorrect' % Filename(fileSpec.filename).getBasename())
                if self.host.redownloadContentsFile(self.http):
                    yield self.restartDownload
                    return
            else:
                yield self.stepComplete
                return

        if self.host.redownloadContentsFile(self.http):
            yield self.restartDownload
            return
        yield self.stepFailed

    def __applyPatch(self, step, patchfile):
        self.updated = True
        origPathname = Filename(self.getPackageDir(), self.uncompressedArchive.filename)
        patchPathname = Filename(self.getPackageDir(), patchfile.file.filename)
        result = Filename.temporary('', 'patch_')
        self.notify.info('Patching %s with %s' % (origPathname, patchPathname))
        p = PandaModules.Patchfile()
        ret = p.initiate(patchPathname, origPathname, result)
        if ret == EUSuccess:
            ret = p.run()
        while ret == EUOk:
            step.bytesDone = step.bytesNeeded * p.getProgress()
            self.__updateStepProgress(step)
            if taskMgr.destroyed:
                self.notify.warning('Task Manager destroyed, aborting patch %s' % origPathname)
                yield self.stepFailed
                return
            yield self.stepContinue
            ret = p.run()

        del p
        patchPathname.unlink()
        if ret < 0:
            self.notify.warning('Patching of %s failed.' % origPathname)
            result.unlink()
            yield self.stepFailed
            return
        if not result.renameTo(origPathname):
            self.notify.warning("Couldn't rename %s to %s" % (result, origPathname))
            yield self.stepFailed
            return
        yield self.stepComplete

    def __uncompressArchive(self, step):
        if self.host.appRunner and self.host.appRunner.verifyContents == self.host.appRunner.P3DVCNever:
            yield self.stepFailed
            return
        self.updated = True
        sourcePathname = Filename(self.getPackageDir(), self.compressedArchive.filename)
        targetPathname = Filename(self.getPackageDir(), self.uncompressedArchive.filename)
        targetPathname.unlink()
        self.notify.info('Uncompressing %s to %s' % (sourcePathname, targetPathname))
        decompressor = Decompressor()
        decompressor.initiate(sourcePathname, targetPathname)
        totalBytes = self.uncompressedArchive.size
        result = decompressor.run()
        while result == EUOk:
            step.bytesDone = int(totalBytes * decompressor.getProgress())
            self.__updateStepProgress(step)
            result = decompressor.run()
            if taskMgr.destroyed:
                self.notify.warning('Task Manager destroyed, aborting decompresss %s' % sourcePathname)
                yield self.stepFailed
                return
            yield self.stepContinue

        if result != EUSuccess:
            yield self.stepFailed
            return
        step.bytesDone = totalBytes
        self.__updateStepProgress(step)
        if not self.uncompressedArchive.quickVerify(self.getPackageDir(), notify=self.notify):
            self.notify.warning('after uncompressing, %s still incorrect' % self.uncompressedArchive.filename)
            yield self.stepFailed
            return
        os.chmod(targetPathname.toOsSpecific(), 292)
        sourcePathname.unlink()
        yield self.stepComplete

    def __unpackArchive(self, step):
        if not self.extracts:
            self.hasPackage = True
            yield self.stepComplete
            return
        if self.host.appRunner and self.host.appRunner.verifyContents == self.host.appRunner.P3DVCNever:
            yield self.stepFailed
            return
        self.updated = True
        mfPathname = Filename(self.getPackageDir(), self.uncompressedArchive.filename)
        self.notify.info('Unpacking %s' % mfPathname)
        mf = Multifile()
        if not mf.openRead(mfPathname):
            self.notify.warning("Couldn't open %s" % mfPathname)
            yield self.stepFailed
            return
        allExtractsOk = True
        step.bytesDone = 0
        for file in self.extracts:
            i = mf.findSubfile(file.filename)
            if i == -1:
                self.notify.warning('Not in Multifile: %s' % file.filename)
                allExtractsOk = False
                continue
            targetPathname = Filename(self.getPackageDir(), file.filename)
            targetPathname.unlink()
            if not mf.extractSubfile(i, targetPathname):
                self.notify.warning("Couldn't extract: %s" % file.filename)
                allExtractsOk = False
                continue
            if not file.quickVerify(self.getPackageDir(), notify=self.notify):
                self.notify.warning('After extracting, still incorrect: %s' % file.filename)
                allExtractsOk = False
                continue
            os.chmod(targetPathname.toOsSpecific(), 365)
            step.bytesDone += file.size
            self.__updateStepProgress(step)
            if taskMgr.destroyed:
                self.notify.warning('Task Manager destroyed, aborting unpacking %s' % mfPathname)
                yield self.stepFailed
                return
            yield self.stepContinue

        if not allExtractsOk:
            yield self.stepFailed
            return
        self.hasPackage = True
        yield self.stepComplete

    def installPackage(self, appRunner):
        if self.installed:
            return True
        mfPathname = Filename(self.getPackageDir(), self.uncompressedArchive.filename)
        mf = Multifile()
        if not mf.openRead(mfPathname):
            self.notify.warning("Couldn't open %s" % mfPathname)
            return False
        root = self.getPackageDir().cStr()
        vfs = VirtualFileSystem.getGlobalPtr()
        vfs.mount(mf, root, vfs.MFReadOnly)
        osRoot = self.getPackageDir().toOsSpecific()
        foundOnPath = False
        for p in sys.path:
            if osRoot == p:
                foundOnPath = True
                break
            elif osRoot == Filename.fromOsSpecific(p).toOsSpecific():
                foundOnPath = True
                break

        if not foundOnPath:
            sys.path.append(osRoot)
        getModelPath().appendDirectory(self.getPackageDir())
        envvar = '%s_ROOT' % self.packageName.upper()
        ExecutionEnvironment.setEnvironmentVariable(envvar, osRoot)
        appRunner.loadMultifilePrcFiles(mf, self.getPackageDir())
        for filename in mf.getSubfileNames():
            if filename.endswith('/__init__.pyc') or filename.endswith('/__init__.pyo') or filename.endswith('/__init__.py'):
                components = filename.split('/')[:-1]
                moduleName = ('.').join(components)
                VFSImporter.sharedPackages[moduleName] = True

        VFSImporter.reloadSharedPackages()
        self.installed = True
        appRunner.installedPackages.append(self)
        self.markUsed()
        return True

    def __measureDiskSpace(self):
        thisDir = ScanDirectoryNode(self.getPackageDir(), ignoreUsageXml=True)
        diskSpace = thisDir.getTotalSize()
        self.notify.info('Package %s uses %s MB' % (self.packageName, (diskSpace + 524288) / 1048576))
        return diskSpace

    def markUsed(self):
        if not hasattr(PandaModules, 'TiXmlDocument'):
            return
        if self.host.appRunner and self.host.appRunner.verifyContents == self.host.appRunner.P3DVCNever:
            return
        if self.updated:
            self.diskSpace = self.__measureDiskSpace()
        filename = Filename(self.getPackageDir(), self.UsageBasename)
        doc = TiXmlDocument(filename.toOsSpecific())
        if not doc.LoadFile():
            decl = TiXmlDeclaration('1.0', 'utf-8', '')
            doc.InsertEndChild(decl)
        xusage = doc.FirstChildElement('usage')
        if not xusage:
            doc.InsertEndChild(TiXmlElement('usage'))
            xusage = doc.FirstChildElement('usage')
        now = int(time.time())
        count = xusage.Attribute('count_app')
        try:
            count = int(count or '')
        except ValueError:
            count = 0
            xusage.SetAttribute('first_use', str(now))

        count += 1
        xusage.SetAttribute('count_app', str(count))
        xusage.SetAttribute('last_use', str(now))
        if self.updated:
            xusage.SetAttribute('last_update', str(now))
            self.updated = False
        else:
            diskSpace = xusage.Attribute('disk_space')
            try:
                diskSpace = int(diskSpace or '')
            except ValueError:
                self.diskSpace = self.__measureDiskSpace()

        xusage.SetAttribute('disk_space', str(self.diskSpace))
        tfile = Filename.temporary(self.getPackageDir().cStr(), '.xml')
        if doc.SaveFile(tfile.toOsSpecific()):
            tfile.renameTo(filename)

    def getUsage(self):
        if not hasattr(PandaModules, 'TiXmlDocument'):
            return
        filename = Filename(self.getPackageDir(), self.UsageBasename)
        doc = TiXmlDocument(filename.toOsSpecific())
        if not doc.LoadFile():
            return
        xusage = doc.FirstChildElement('usage')
        if not xusage:
            return
        return copy.copy(xusage)