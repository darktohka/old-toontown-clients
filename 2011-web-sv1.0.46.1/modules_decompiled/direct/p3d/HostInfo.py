# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\HostInfo.py
from pandac.PandaModules import HashVal, Filename, PandaSystem, DocumentSpec, Ramfile
from pandac.PandaModules import HTTPChannel
from pandac import PandaModules
from libpandaexpress import ConfigVariableInt
from direct.p3d.PackageInfo import PackageInfo
from direct.p3d.FileSpec import FileSpec
from direct.directnotify.DirectNotifyGlobal import directNotify
import time

class HostInfo:
    __module__ = __name__
    notify = directNotify.newCategory('HostInfo')

    def __init__(self, hostUrl, appRunner=None, hostDir=None, rootDir=None, asMirror=False, perPlatform=None):
        self.__setHostUrl(hostUrl)
        self.appRunner = appRunner
        self.rootDir = rootDir
        if rootDir is None and appRunner:
            self.rootDir = appRunner.rootDir
        if hostDir and not isinstance(hostDir, Filename):
            hostDir = Filename.fromOsSpecific(hostDir)
        self.hostDir = hostDir
        self.asMirror = asMirror
        self.perPlatform = perPlatform
        if perPlatform is None:
            self.perPlatform = asMirror
        self.hasContentsFile = False
        self.contentsExpiration = 0
        self.contentsSpec = FileSpec()
        self.descriptiveName = None
        self.mirrors = []
        self.altHosts = {}
        self.packages = {}
        if self.appRunner and self.appRunner.verifyContents != self.appRunner.P3DVCForce:
            self.readContentsFile()
        return

    def __setHostUrl(self, hostUrl):
        self.hostUrl = hostUrl
        if not self.hostUrl:
            self.hostUrlPrefix = None
            self.downloadUrlPrefix = None
        else:
            self.hostUrlPrefix = hostUrl
            if self.hostUrlPrefix[(-1)] != '/':
                self.hostUrlPrefix += '/'
            self.downloadUrlPrefix = self.hostUrlPrefix
        return

    def downloadContentsFile(self, http, redownload=False, hashVal=None):
        if self.hasCurrentContentsFile():
            return True
        if self.appRunner:
            if self.appRunner.verifyContents == self.appRunner.P3DVCNever:
                return False
            rf = None
            if http:
                if not redownload:
                    if self.appRunner and self.appRunner.superMirrorUrl:
                        url = self.appRunner.superMirrorUrl + 'contents.xml'
                        request = DocumentSpec(url)
                        self.notify.info('Downloading contents file %s' % request)
                        rf = Ramfile()
                        channel = http.makeChannel(False)
                        channel.getDocument(request)
                        if not channel.downloadToRam(rf):
                            self.notify.warning('Unable to download %s' % url)
                            rf = None
                    url = rf or self.hostUrlPrefix + 'contents.xml'
                    url += '?' + str(int(time.time()))
                    request = DocumentSpec(url)
                    request.setCacheControl(DocumentSpec.CCNoCache)
                    self.notify.info('Downloading contents file %s' % request)
                    statusCode = None
                    statusString = ''
                    for attempt in range(ConfigVariableInt('contents-xml-dl-attempts', 3)):
                        if attempt > 0:
                            self.notify.info('Retrying (%s)...' % (attempt,))
                        rf = Ramfile()
                        channel = http.makeChannel(False)
                        channel.getDocument(request)
                        if channel.downloadToRam(rf):
                            self.notify.warning('Successfully downloaded %s' % (url,))
                            break
                        else:
                            rf = None
                            statusCode = channel.getStatusCode()
                            statusString = channel.getStatusString()
                            self.notify.warning('Could not contact download server at %s' % (url,))
                            self.notify.warning('Status code = %s %s' % (statusCode, statusString))

                    rf or self.notify.warning('Unable to download %s' % (url,))
                    try:
                        if statusCode == HTTPChannel.SCDownloadOpenError or statusCode == HTTPChannel.SCDownloadWriteError:
                            launcher.setPandaErrorCode(2)
                        elif statusCode == 404:
                            launcher.setPandaErrorCode(5)
                        elif statusCode < 100:
                            launcher.setPandaErrorCode(4)
                        else:
                            launcher.setPandaErrorCode(6)
                    except NameError, e:
                        pass
                    except AttributeError, e:
                        self.notify.warning('%s' % (str(e),))
                    else:
                        return False
        tempFilename = Filename.temporary('', 'p3d_', '.xml')
        if rf:
            f = open(tempFilename.toOsSpecific(), 'wb')
            f.write(rf.getData())
            f.close()
            if hashVal:
                hashVal.hashString(rf.getData())
            if not self.readContentsFile(tempFilename, freshDownload=True):
                self.notify.warning('Failure reading %s' % url)
                tempFilename.unlink()
                return False
            tempFilename.unlink()
            return True
        return False

    def redownloadContentsFile(self, http):
        if self.appRunner and self.appRunner.verifyContents == self.appRunner.P3DVCNever:
            return False
        url = self.hostUrlPrefix + 'contents.xml'
        self.notify.info('Redownloading %s' % url)
        hv1 = HashVal()
        if self.contentsSpec.hash:
            hv1.setFromHex(self.contentsSpec.hash)
        else:
            filename = Filename(self.hostDir, 'contents.xml')
            hv1.hashFile(filename)
        self.hasContentsFile = False
        hv2 = HashVal()
        if not self.downloadContentsFile(http, redownload=True, hashVal=hv2):
            return False
        if hv2 == HashVal():
            self.notify.info("%s didn't actually redownload." % url)
            return False
        elif hv1 != hv2:
            self.notify.info('%s has changed.' % url)
            return True
        else:
            self.notify.info('%s has not changed.' % url)
            return False

    def hasCurrentContentsFile(self):
        if not self.appRunner or self.appRunner.verifyContents == self.appRunner.P3DVCNone or self.appRunner.verifyContents == self.appRunner.P3DVCNever:
            return self.hasContentsFile
        now = int(time.time())
        return now < self.contentsExpiration and self.hasContentsFile

    def readContentsFile(self, tempFilename=None, freshDownload=False):
        if not hasattr(PandaModules, 'TiXmlDocument'):
            self.notify.warning('readContentsFile: missing tix')
            return False
        if not tempFilename:
            if self.hostDir:
                hostDir = self.hostDir
            else:
                hostDir = self.__determineHostDir(None, self.hostUrl)
            tempFilename = Filename(hostDir, 'contents.xml')
        doc = PandaModules.TiXmlDocument(tempFilename.toOsSpecific())
        if not doc.LoadFile():
            self.notify.warning('readContentsFile: doc.LoadFile() failed')
            return False
        xcontents = doc.FirstChildElement('contents')
        if not xcontents:
            self.notify.warning('readContentsFile: no xcontents')
            return False
        maxAge = xcontents.Attribute('max_age')
        if maxAge:
            try:
                maxAge = int(maxAge)
            except:
                maxAge = None

        if maxAge is None:
            from direct.p3d.AppRunner import AppRunner
            maxAge = AppRunner.P3D_CONTENTS_DEFAULT_MAX_AGE
        now = int(time.time())
        self.contentsExpiration = now + maxAge
        if freshDownload:
            self.contentsSpec.readHash(tempFilename)
            xorig = xcontents.FirstChildElement('orig')
            while xorig:
                xcontents.RemoveChild(xorig)
                xorig = xcontents.FirstChildElement('orig')

            xorig = PandaModules.TiXmlElement('orig')
            self.contentsSpec.storeXml(xorig)
            xorig.SetAttribute('expiration', str(self.contentsExpiration))
            xcontents.InsertEndChild(xorig)
        else:
            expiration = None
            xorig = xcontents.FirstChildElement('orig')
            if xorig:
                self.contentsSpec.loadXml(xorig)
                expiration = xorig.Attribute('expiration')
                if expiration:
                    try:
                        expiration = int(expiration)
                    except:
                        expiration = None

            if not self.contentsSpec.hash:
                self.contentsSpec.readHash(tempFilename)
            if expiration is not None:
                self.contentsExpiration = min(self.contentsExpiration, expiration)
        if self.hostUrl:
            self.__findHostXml(xcontents)
        else:
            self.__findHostXmlForHostDir(xcontents)
        if not self.hostDir:
            self.hostDir = self.__determineHostDir(None, self.hostUrl)
        xpackage = xcontents.FirstChildElement('package')
        while xpackage:
            name = xpackage.Attribute('name')
            platform = xpackage.Attribute('platform')
            version = xpackage.Attribute('version')
            try:
                solo = int(xpackage.Attribute('solo') or '')
            except ValueError:
                solo = False

            package = self.__makePackage(name, platform, version, solo)
            package.descFile = FileSpec()
            package.descFile.loadXml(xpackage)
            package.setupFilenames()
            package.importDescFile = None
            ximport = xpackage.FirstChildElement('import')
            if ximport:
                package.importDescFile = FileSpec()
                package.importDescFile.loadXml(ximport)
            xpackage = xpackage.NextSiblingElement('package')

        self.hasContentsFile = True
        if not self.appRunner or self.appRunner.verifyContents != self.appRunner.P3DVCNever:
            filename = Filename(self.hostDir, 'contents.xml')
            filename.makeDir()
            if freshDownload:
                doc.SaveFile(filename.toOsSpecific())
            elif filename != tempFilename:
                tempFilename.copyTo(filename)
        return True

    def __findHostXml(self, xcontents):
        xhost = xcontents.FirstChildElement('host')
        while xhost:
            url = xhost.Attribute('url')
            if url == self.hostUrl:
                self.readHostXml(xhost)
                return
            xalthost = xhost.FirstChildElement('alt_host')
            while xalthost:
                url = xalthost.Attribute('url')
                if url == self.hostUrl:
                    self.readHostXml(xalthost)
                    return
                xalthost = xalthost.NextSiblingElement('alt_host')

            xhost = xhost.NextSiblingElement('host')

    def __findHostXmlForHostDir(self, xcontents):
        xhost = xcontents.FirstChildElement('host')
        while xhost:
            url = xhost.Attribute('url')
            hostDirBasename = xhost.Attribute('host_dir')
            hostDir = self.__determineHostDir(hostDirBasename, url)
            if hostDir == self.hostDir:
                self.__setHostUrl(url)
                self.readHostXml(xhost)
                return
            xalthost = xhost.FirstChildElement('alt_host')
            while xalthost:
                url = xalthost.Attribute('url')
                hostDirBasename = xalthost.Attribute('host_dir')
                hostDir = self.__determineHostDir(hostDirBasename, url)
                if hostDir == self.hostDir:
                    self.__setHostUrl(url)
                    self.readHostXml(xalthost)
                    return
                xalthost = xalthost.NextSiblingElement('alt_host')

            xhost = xhost.NextSiblingElement('host')

    def readHostXml(self, xhost):
        descriptiveName = xhost.Attribute('descriptive_name')
        if descriptiveName and not self.descriptiveName:
            self.descriptiveName = descriptiveName
        hostDirBasename = xhost.Attribute('host_dir')
        if not self.hostDir:
            self.hostDir = self.__determineHostDir(hostDirBasename, self.hostUrl)
        downloadUrl = xhost.Attribute('download_url')
        if downloadUrl:
            self.downloadUrlPrefix = downloadUrl
            if self.downloadUrlPrefix[(-1)] != '/':
                self.downloadUrlPrefix += '/'
        else:
            self.downloadUrlPrefix = self.hostUrlPrefix
        xmirror = xhost.FirstChildElement('mirror')
        while xmirror:
            url = xmirror.Attribute('url')
            if url:
                if url[(-1)] != '/':
                    url += '/'
                if url not in self.mirrors:
                    self.mirrors.append(url)
            xmirror = xmirror.NextSiblingElement('mirror')

        xalthost = xhost.FirstChildElement('alt_host')
        while xalthost:
            keyword = xalthost.Attribute('keyword')
            url = xalthost.Attribute('url')
            if url and keyword:
                self.altHosts[keyword] = url
            xalthost = xalthost.NextSiblingElement('alt_host')

    def __makePackage(self, name, platform, version, solo):
        if not platform:
            platform = None
        platforms = self.packages.setdefault((name, version), {})
        package = platforms.get(platform, None)
        if not package:
            package = PackageInfo(self, name, version, platform=platform, solo=solo, asMirror=self.asMirror)
            platforms[platform] = package
        return package

    def getPackage(self, name, version, platform=None):
        platforms = self.packages.get((name, version or None), {})
        if platform is not None:
            return platforms.get(platform or None, None)
        package = platforms.get(PandaSystem.getPlatform(), None)
        if not package:
            package = platforms.get(None, None)
        return package

    def getPackages(self, name=None, platform=None):
        packages = []
        for ((pn, version), platforms) in self.packages.items():
            if name and pn != name:
                continue
            if platform is None:
                for p2 in platforms:
                    package = self.getPackage(pn, version, platform=p2)
                    if package:
                        packages.append(package)

            else:
                package = self.getPackage(pn, version, platform=platform)
                if package:
                    packages.append(package)

        return packages

    def getAllPackages(self):
        result = []
        items = self.packages.items()
        items.sort()
        for (key, platforms) in items:
            if self.perPlatform:
                pitems = platforms.items()
                pitems.sort()
                for (pkey, package) in pitems:
                    result.append(package)

            else:
                package = platforms.get(PandaSystem.getPlatform(), None)
                if not package:
                    package = platforms.get(None, None)
                if package:
                    result.append(package)

        return result

    def deletePackages(self, packages):
        packages = packages[:]
        for (key, platforms) in self.packages.items():
            for (platform, package) in platforms.items():
                if package in packages:
                    self.__deletePackageFiles(package)
                    del platforms[platform]
                    packages.remove(package)

            if not platforms:
                del self.packages[key]

        return packages

    def __deletePackageFiles(self, package):
        if self.appRunner:
            self.notify.info('Deleting package %s: %s' % (package.packageName, package.getPackageDir()))
            self.appRunner.rmtree(package.getPackageDir())
            self.appRunner.sendRequest('forget_package', self.hostUrl, package.packageName, package.packageVersion or '')

    def __determineHostDir(self, hostDirBasename, hostUrl):
        if hostDirBasename:
            hostDir = self.rootDir.cStr() + '/hosts'
            for component in hostDirBasename.split('/'):
                if component:
                    if component[0] == '.':
                        component = 'x' + component
                    hostDir += '/'
                    hostDir += component

            return Filename(hostDir)
        hostDir = 'hosts/'
        p = hostUrl.find('://')
        hostname = ''
        if p != -1:
            start = p + 3
            end = hostUrl.find('/', start)
            at = hostUrl.find('@', start)
            if at != -1 and at < end:
                start = at + 1
            colon = hostUrl.find(':', start)
            if colon != -1 and colon < end:
                end = colon
            hostname = hostUrl[start:end]
        hashSize = 16
        keepHash = hashSize
        if hostname:
            hostDir += hostname + '_'
            keepHash = keepHash / 2
        md = HashVal()
        md.hashString(hostUrl)
        hostDir += md.asHex()[:keepHash * 2]
        hostDir = Filename(self.rootDir, hostDir)
        return hostDir