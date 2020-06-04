# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\FileSpec.py
import os
from pandac.PandaModules import Filename, HashVal, VirtualFileSystem

class FileSpec:
    __module__ = __name__

    def __init__(self):
        self.actualFile = None
        self.filename = None
        self.size = 0
        self.timestamp = 0
        self.hash = None
        return

    def fromFile(self, packageDir, filename, pathname=None, st=None):
        vfs = VirtualFileSystem.getGlobalPtr()
        filename = Filename(filename)
        if pathname is None:
            pathname = Filename(packageDir, filename)
        self.filename = filename.cStr()
        self.basename = filename.getBasename()
        if st is None:
            st = os.stat(pathname.toOsSpecific())
        self.size = st.st_size
        self.timestamp = st.st_mtime
        self.readHash(pathname)
        return

    def readHash(self, pathname):
        hv = HashVal()
        hv.hashFile(pathname)
        self.hash = hv.asHex()

    def loadXml(self, xelement):
        self.filename = xelement.Attribute('filename')
        self.basename = None
        if self.filename:
            self.basename = Filename(self.filename).getBasename()
        size = xelement.Attribute('size')
        try:
            self.size = int(size)
        except:
            self.size = 0

        timestamp = xelement.Attribute('timestamp')
        try:
            self.timestamp = int(timestamp)
        except:
            self.timestamp = 0

        self.hash = xelement.Attribute('hash')
        return

    def storeXml(self, xelement):
        if self.filename:
            xelement.SetAttribute('filename', self.filename)
        if self.size:
            xelement.SetAttribute('size', str(self.size))
        if self.timestamp:
            xelement.SetAttribute('timestamp', str(int(self.timestamp)))
        if self.hash:
            xelement.SetAttribute('hash', self.hash)

    def storeMiniXml(self, xelement):
        if self.size:
            xelement.SetAttribute('size', str(self.size))
        if self.hash:
            xelement.SetAttribute('hash', self.hash)

    def quickVerify(self, packageDir=None, pathname=None, notify=None):
        if not pathname:
            pathname = Filename(packageDir, self.filename)
        try:
            st = os.stat(pathname.toOsSpecific())
        except OSError:
            if notify:
                notify.debug('file not found: %s' % pathname)
            return False

        if st.st_size != self.size:
            if notify:
                notify.debug('size wrong: %s' % pathname)
            return False
        if st.st_mtime == self.timestamp:
            if notify:
                notify.debug('file ok: %s' % pathname)
            return True
        if notify:
            notify.debug('modification time wrong: %s' % pathname)
        if not self.checkHash(packageDir, pathname, st):
            if notify:
                notify.debug('hash check wrong: %s' % pathname)
                notify.debug('  found %s, expected %s' % (self.actualFile.hash, self.hash))
            return False
        if notify:
            notify.info('hash check ok: %s' % pathname)
        self.__updateTimestamp(pathname, st)
        return True

    def fullVerify(self, packageDir=None, pathname=None, notify=None):
        if not pathname:
            pathname = Filename(packageDir, self.filename)
        try:
            st = os.stat(pathname.toOsSpecific())
        except OSError:
            if notify:
                notify.debug('file not found: %s' % pathname)
            return False

        if st.st_size != self.size:
            if notify:
                notify.debug('size wrong: %s' % pathname)
            return False
        if not self.checkHash(packageDir, pathname, st):
            if notify:
                notify.debug('hash check wrong: %s' % pathname)
                notify.debug('  found %s, expected %s' % (self.actualFile.hash, self.hash))
            return False
        if notify:
            notify.info('hash check ok: %s' % pathname)
        if st.st_mtime != self.timestamp:
            self.__updateTimestamp(pathname, st)
        return True

    def __updateTimestamp(self, pathname, st):
        try:
            os.chmod(pathname.toOsSpecific(), 493)
            os.utime(pathname.toOsSpecific(), (st.st_atime, self.timestamp))
            os.chmod(pathname.toOsSpecific(), 365)
        except OSError:
            pass

    def checkHash(self, packageDir, pathname, st):
        fileSpec = FileSpec()
        fileSpec.fromFile(packageDir, self.filename, pathname=pathname, st=st)
        self.actualFile = fileSpec
        return fileSpec.hash == self.hash