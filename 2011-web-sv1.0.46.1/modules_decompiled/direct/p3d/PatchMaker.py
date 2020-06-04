# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\PatchMaker.py
from direct.p3d.FileSpec import FileSpec
from direct.p3d.SeqValue import SeqValue
from pandac.PandaModules import *
import copy

class PatchMaker:
    __module__ = __name__

    class PackageVersion:
        __module__ = __name__

        def __init__(self, packageName, platform, version, hostUrl, file):
            self.packageName = packageName
            self.platform = platform
            self.version = version
            self.hostUrl = hostUrl
            self.file = file
            self.printName = None
            self.packageCurrent = None
            self.packageBase = None
            self.packageTop = None
            self.fromPatches = []
            self.toPatches = []
            self.tempFile = None
            return

        def cleanup(self):
            if self.tempFile:
                self.tempFile.unlink()

        def getPatchChain(self, startPv, alreadyVisited=[]):
            if self is startPv:
                return []
            if self in alreadyVisited:
                return
            alreadyVisited = alreadyVisited[:]
            alreadyVisited.append(self)
            bestPatchChain = None
            for patchfile in self.fromPatches:
                fromPv = patchfile.fromPv
                patchChain = fromPv.getPatchChain(startPv, alreadyVisited)
                if patchChain is not None:
                    patchChain = patchChain + [patchfile]
                    if bestPatchChain is None or len(patchChain) < len(bestPatchChain):
                        bestPatchChain = patchChain

            return bestPatchChain

        def getRecreateFilePlan(self, alreadyVisited=[]):
            if self.tempFile:
                return (
                 self.tempFile, self, [])
            if self in alreadyVisited:
                return (None, None, None)
            alreadyVisited = alreadyVisited[:]
            alreadyVisited.append(self)
            if self.packageCurrent:
                package = self.packageCurrent
                return (Filename(package.packageDir, package.compressedFilename), self, [])
            if self.packageBase:
                package = self.packageBase
                return (Filename(package.packageDir, package.baseFile.filename + '.pz'), self, [])
            bestPlan = None
            bestStartFile = None
            bestStartPv = None
            for patchfile in self.fromPatches:
                fromPv = patchfile.fromPv
                (startFile, startPv, plan) = fromPv.getRecreateFilePlan(alreadyVisited)
                if plan is not None:
                    plan = plan + [(patchfile, self)]
                    if bestPlan is None or len(plan) < len(bestPlan):
                        bestPlan = plan
                        bestStartFile = startFile
                        bestStartPv = startPv

            return (bestStartFile, bestStartPv, bestPlan)

        def getFile(self):
            (startFile, startPv, plan) = self.getRecreateFilePlan()
            if startFile.getExtension() == 'pz':
                startPv.tempFile = Filename.temporary('', 'patch_')
                if not decompressFile(startFile, startPv.tempFile):
                    return
                startFile = startPv.tempFile
            if not plan:
                return startFile
            prevFile = startFile
            for (patchfile, pv) in plan:
                fromPv = patchfile.fromPv
                patchFilename = Filename(patchfile.package.packageDir, patchfile.file.filename)
                result = self.applyPatch(prevFile, patchFilename)
                if not result:
                    return
                pv.tempFile = result
                prevFile = result

            return prevFile

        def applyPatch(self, origFile, patchFilename):
            result = Filename.temporary('', 'patch_')
            p = Patchfile()
            if not p.apply(patchFilename, origFile, result):
                print 'Internal patching failed: %s' % patchFilename
                return
            return result

        def getNext(self, package):
            for patch in self.toPatches:
                if patch.packageName == package.packageName and patch.platform == package.platform and patch.version == package.version and patch.hostUrl == package.hostUrl:
                    return patch.toPv

            return

    class Patchfile:
        __module__ = __name__

        def __init__(self, package):
            self.package = package
            self.packageName = package.packageName
            self.platform = package.platform
            self.version = package.version
            self.hostUrl = None
            self.file = None
            self.sourceFile = None
            self.targetFile = None
            self.fromPv = None
            self.toPv = None
            return

        def getSourceKey(self):
            return (
             self.packageName, self.platform, self.version, self.hostUrl, self.sourceFile)

        def getTargetKey(self):
            return (
             self.packageName, self.platform, self.version, self.hostUrl, self.targetFile)

        def fromFile(self, packageDir, patchFilename, sourceFile, targetFile):
            self.file = FileSpec()
            self.file.fromFile(packageDir, patchFilename)
            self.sourceFile = sourceFile
            self.targetFile = targetFile

        def loadXml(self, xpatch):
            self.packageName = xpatch.Attribute('name') or self.packageName
            self.platform = xpatch.Attribute('platform') or self.platform
            self.version = xpatch.Attribute('version') or self.version
            self.hostUrl = xpatch.Attribute('host') or self.hostUrl
            self.file = FileSpec()
            self.file.loadXml(xpatch)
            xsource = xpatch.FirstChildElement('source')
            if xsource:
                self.sourceFile = FileSpec()
                self.sourceFile.loadXml(xsource)
            xtarget = xpatch.FirstChildElement('target')
            if xtarget:
                self.targetFile = FileSpec()
                self.targetFile.loadXml(xtarget)

        def makeXml(self, package):
            xpatch = TiXmlElement('patch')
            if self.packageName != package.packageName:
                xpatch.SetAttribute('name', self.packageName)
            if self.platform != package.platform:
                xpatch.SetAttribute('platform', self.platform)
            if self.version != package.version:
                xpatch.SetAttribute('version', self.version)
            if self.hostUrl != package.hostUrl:
                xpatch.SetAttribute('host', self.hostUrl)
            self.file.storeXml(xpatch)
            xsource = TiXmlElement('source')
            self.sourceFile.storeMiniXml(xsource)
            xpatch.InsertEndChild(xsource)
            xtarget = TiXmlElement('target')
            self.targetFile.storeMiniXml(xtarget)
            xpatch.InsertEndChild(xtarget)
            return xpatch

    class Package:
        __module__ = __name__

        def __init__(self, packageDesc, patchMaker, xpackage=None):
            self.packageDir = Filename(patchMaker.installDir, packageDesc.getDirname())
            self.packageDesc = packageDesc
            self.patchMaker = patchMaker
            self.contentsDocPackage = xpackage
            self.patchVersion = 1
            self.currentPv = None
            self.basePv = None
            self.topPv = None
            self.packageName = None
            self.platform = None
            self.version = None
            self.hostUrl = None
            self.currentFile = None
            self.baseFile = None
            self.doc = None
            self.anyChanges = False
            self.patches = []
            return

        def getCurrentKey(self):
            return (
             self.packageName, self.platform, self.version, self.hostUrl, self.currentFile)

        def getBaseKey(self):
            return (
             self.packageName, self.platform, self.version, self.hostUrl, self.baseFile)

        def getTopKey(self):
            return (
             self.packageName, self.platform, self.version, self.hostUrl, self.topFile)

        def getGenericKey(self, fileSpec):
            return (
             self.packageName, self.platform, self.version, self.hostUrl, fileSpec)

        def readDescFile(self, doProcessing=False):
            self.anyChanges = False
            packageDescFullpath = Filename(self.patchMaker.installDir, self.packageDesc)
            self.doc = TiXmlDocument(packageDescFullpath.toOsSpecific())
            if not self.doc.LoadFile():
                print "Couldn't read %s" % packageDescFullpath
                return False
            xpackage = self.doc.FirstChildElement('package')
            if not xpackage:
                return False
            self.packageName = xpackage.Attribute('name')
            self.platform = xpackage.Attribute('platform')
            self.version = xpackage.Attribute('version')
            self.hostUrl = None
            self.currentFile = None
            self.baseFile = None
            self.topFile = None
            self.compressedFilename = None
            compressedFile = None
            isNewVersion = True
            xarchive = xpackage.FirstChildElement('uncompressed_archive')
            if xarchive:
                self.currentFile = FileSpec()
                self.currentFile.loadXml(xarchive)
            xarchive = xpackage.FirstChildElement('top_version')
            if xarchive:
                self.topFile = FileSpec()
                self.topFile.loadXml(xarchive)
                if self.topFile.hash == self.currentFile.hash:
                    isNewVersion = False
                else:
                    self.anyChanges = True
            else:
                self.topFile = copy.copy(self.currentFile)
                self.anyChanges = True
            patchVersion = xpackage.Attribute('patch_version')
            if patchVersion:
                self.patchVersion = int(patchVersion)
            else:
                patchVersion = xpackage.Attribute('last_patch_version')
                if patchVersion:
                    self.patchVersion = int(patchVersion)
                    if isNewVersion:
                        self.patchVersion += 1
                self.anyChanges = True
            xcompressed = xpackage.FirstChildElement('compressed_archive')
            if xcompressed:
                compressedFile = FileSpec()
                compressedFile.loadXml(xcompressed)
                oldCompressedFilename = compressedFile.filename
                self.compressedFilename = oldCompressedFilename
                if doProcessing:
                    newCompressedFilename = '%s.%s.pz' % (self.currentFile.filename, self.patchVersion)
                    if newCompressedFilename != oldCompressedFilename:
                        oldCompressedPathname = Filename(self.packageDir, oldCompressedFilename)
                        newCompressedPathname = Filename(self.packageDir, newCompressedFilename)
                        if oldCompressedPathname.renameTo(newCompressedPathname):
                            compressedFile.fromFile(self.packageDir, newCompressedFilename)
                            compressedFile.storeXml(xcompressed)
                        self.compressedFilename = newCompressedFilename
                        self.anyChanges = True
            xarchive = xpackage.FirstChildElement('base_version')
            if xarchive:
                self.baseFile = FileSpec()
                self.baseFile.loadXml(xarchive)
            else:
                self.baseFile = copy.copy(self.currentFile)
                self.baseFile.filename += '.base'
                if doProcessing and self.compressedFilename:
                    fromPathname = Filename(self.packageDir, self.compressedFilename)
                    toPathname = Filename(self.packageDir, self.baseFile.filename + '.pz')
                    fromPathname.copyTo(toPathname)
                self.anyChanges = True
            self.patches = []
            xpatch = xpackage.FirstChildElement('patch')
            while xpatch:
                patchfile = PatchMaker.Patchfile(self)
                patchfile.loadXml(xpatch)
                self.patches.append(patchfile)
                xpatch = xpatch.NextSiblingElement('patch')

            return True

        def writeDescFile(self):
            if not self.anyChanges:
                return
            xpackage = self.doc.FirstChildElement('package')
            if not xpackage:
                return
            packageSeq = SeqValue()
            packageSeq.loadXml(xpackage, 'seq')
            packageSeq += 1
            packageSeq.storeXml(xpackage, 'seq')
            xremove = []
            for value in ['base_version', 'top_version', 'patch']:
                xpatch = xpackage.FirstChildElement(value)
                while xpatch:
                    xremove.append(xpatch)
                    xpatch = xpatch.NextSiblingElement(value)

            for xelement in xremove:
                xpackage.RemoveChild(xelement)

            xpackage.RemoveAttribute('last_patch_version')
            xpackage.SetAttribute('patch_version', str(self.patchVersion))
            xarchive = TiXmlElement('base_version')
            self.baseFile.storeXml(xarchive)
            xpackage.InsertEndChild(xarchive)
            xarchive = TiXmlElement('top_version')
            self.currentFile.storeXml(xarchive)
            xpackage.InsertEndChild(xarchive)
            for patchfile in self.patches:
                xpatch = patchfile.makeXml(self)
                xpackage.InsertEndChild(xpatch)

            self.doc.SaveFile()
            importDescFullpath = Filename(self.patchMaker.installDir, self.packageDesc.cStr()[:-3] + 'import.xml')
            doc = TiXmlDocument(importDescFullpath.toOsSpecific())
            if doc.LoadFile():
                xpackage = doc.FirstChildElement('package')
                if xpackage:
                    packageSeq.storeXml(xpackage, 'seq')
                    doc.SaveFile()
            else:
                print "Couldn't read %s" % importDescFullpath
            if self.contentsDocPackage:
                fileSpec = FileSpec()
                fileSpec.fromFile(self.patchMaker.installDir, self.packageDesc)
                fileSpec.storeXml(self.contentsDocPackage)
                packageSeq.storeXml(self.contentsDocPackage, 'seq')

    def __init__(self, installDir):
        self.installDir = installDir
        self.packageVersions = {}
        self.packages = []

    def buildPatches(self, packageNames=None):
        if not self.readContentsFile():
            return False
        self.buildPatchChains()
        if packageNames is None:
            self.processAllPackages()
        else:
            self.processSomePackages(packageNames)
        self.writeContentsFile()
        self.cleanup()
        return True

    def cleanup(self):
        for pv in self.packageVersions.values():
            pv.cleanup()

    def getPatchChainToCurrent(self, descFilename, fileSpec):
        package = self.readPackageDescFile(descFilename)
        if not package:
            return
        self.buildPatchChains()
        fromPv = self.getPackageVersion(package.getGenericKey(fileSpec))
        toPv = package.currentPv
        patchChain = None
        if toPv and fromPv:
            patchChain = toPv.getPatchChain(fromPv)
        return patchChain

    def readPackageDescFile(self, descFilename):
        package = self.Package(Filename(descFilename), self)
        if not package.readDescFile(doProcessing=False):
            return
        self.packages.append(package)
        return package

    def readContentsFile(self):
        contentsFilename = Filename(self.installDir, 'contents.xml')
        doc = TiXmlDocument(contentsFilename.toOsSpecific())
        if not doc.LoadFile():
            print "couldn't read %s" % contentsFilename
            return False
        xcontents = doc.FirstChildElement('contents')
        if xcontents:
            contentsSeq = SeqValue()
            contentsSeq.loadXml(xcontents)
            contentsSeq += 1
            contentsSeq.storeXml(xcontents)
            xpackage = xcontents.FirstChildElement('package')
            while xpackage:
                solo = xpackage.Attribute('solo')
                solo = int(solo or '0')
                filename = xpackage.Attribute('filename')
                if filename and not solo:
                    filename = Filename(filename)
                    package = self.Package(filename, self, xpackage)
                    package.readDescFile(doProcessing=True)
                    self.packages.append(package)
                xpackage = xpackage.NextSiblingElement('package')

        self.contentsDoc = doc
        return True

    def writeContentsFile(self):
        for package in self.packages:
            package.writeDescFile()

        self.contentsDoc.SaveFile()

    def getPackageVersion(self, key):
        (packageName, platform, version, hostUrl, file) = key
        k = (
         packageName, platform, version, hostUrl, file.hash)
        pv = self.packageVersions.get(k, None)
        if not pv:
            pv = self.PackageVersion(*key)
            self.packageVersions[k] = pv
        return pv

    def buildPatchChains(self):
        self.patchFilenames = {}
        for package in self.packages:
            if not package.baseFile:
                continue
            currentPv = self.getPackageVersion(package.getCurrentKey())
            package.currentPv = currentPv
            currentPv.packageCurrent = package
            currentPv.printName = package.currentFile.filename
            basePv = self.getPackageVersion(package.getBaseKey())
            package.basePv = basePv
            basePv.packageBase = package
            basePv.printName = package.baseFile.filename
            topPv = self.getPackageVersion(package.getTopKey())
            package.topPv = topPv
            topPv.packageTop = package
            for patchfile in package.patches:
                self.recordPatchfile(patchfile)

    def recordPatchfile(self, patchfile):
        self.patchFilenames[patchfile.file.filename] = patchfile
        fromPv = self.getPackageVersion(patchfile.getSourceKey())
        patchfile.fromPv = fromPv
        fromPv.toPatches.append(patchfile)
        toPv = self.getPackageVersion(patchfile.getTargetKey())
        patchfile.toPv = toPv
        toPv.fromPatches.append(patchfile)
        toPv.printName = patchfile.file.filename

    def processSomePackages(self, packageNames):
        remainingNames = packageNames[:]
        for package in self.packages:
            if package.packageName in packageNames:
                self.processPackage(package)
            if package.packageName in remainingNames:
                remainingNames.remove(package.packageName)

        if remainingNames:
            print 'Unknown packages: %s' % (remainingNames,)

    def processAllPackages(self):
        for package in self.packages:
            self.processPackage(package)

    def processPackage(self, package):
        if not package.baseFile:
            return
        topPv = package.topPv
        currentPv = package.currentPv
        if topPv != currentPv:
            filename = Filename(package.currentFile.filename + '.%s.patch' % package.patchVersion)
            if not self.buildPatch(topPv, currentPv, package, filename):
                raise StandardError, "Couldn't build patch."

    def buildPatch(self, v1, v2, package, patchFilename):
        pathname = Filename(package.packageDir, patchFilename)
        if not self.buildPatchFile(v1.getFile(), v2.getFile(), pathname, v1.printName, v2.printName):
            return False
        compressedPathname = Filename(pathname + '.pz')
        compressedPathname.unlink()
        if not compressFile(pathname, compressedPathname, 9):
            raise StandardError, "Couldn't compress patch."
        pathname.unlink()
        patchfile = self.Patchfile(package)
        patchfile.fromFile(package.packageDir, patchFilename + '.pz', v1.file, v2.file)
        package.patches.append(patchfile)
        package.anyChanges = True
        self.recordPatchfile(patchfile)
        return True

    def buildPatchFile(self, origFilename, newFilename, patchFilename, printOrigName, printNewName):
        if not origFilename.exists():
            return False
        print 'Building patch from %s to %s' % (printOrigName, printNewName)
        patchFilename.unlink()
        p = Patchfile()
        if p.build(origFilename, newFilename, patchFilename):
            return True
        patchFilename.unlink()
        return False