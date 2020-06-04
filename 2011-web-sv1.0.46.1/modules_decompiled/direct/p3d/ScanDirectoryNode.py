# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\ScanDirectoryNode.py
from pandac.PandaModules import VirtualFileSystem, VirtualFileMountSystem, Filename, TiXmlDocument
vfs = VirtualFileSystem.getGlobalPtr()

class ScanDirectoryNode:
    __module__ = __name__

    def __init__(self, pathname, ignoreUsageXml=False):
        self.pathname = pathname
        self.filenames = []
        self.fileSize = 0
        self.nested = []
        self.nestedSize = 0
        xusage = None
        if not ignoreUsageXml:
            usageFilename = Filename(pathname, 'usage.xml')
            doc = TiXmlDocument(usageFilename.toOsSpecific())
            if doc.LoadFile():
                xusage = doc.FirstChildElement('usage')
                if xusage:
                    diskSpace = xusage.Attribute('disk_space')
                    try:
                        diskSpace = int(diskSpace or '')
                    except ValueError:
                        diskSpace = None
                    else:
                        if diskSpace is not None:
                            self.fileSize = diskSpace
                            return
        for vfile in vfs.scanDirectory(self.pathname):
            if hasattr(vfile, 'getMount'):
                if not isinstance(vfile.getMount(), VirtualFileMountSystem):
                    continue
            if vfile.isDirectory():
                subdir = ScanDirectoryNode(vfile.getFilename(), ignoreUsageXml=ignoreUsageXml)
                self.nested.append(subdir)
                self.nestedSize += subdir.getTotalSize()
            elif vfile.isRegularFile():
                self.filenames.append(vfile.getFilename())
                self.fileSize += vfile.getFileSize()
            else:
                self.filenames.append(vfile.getFilename())

        if xusage:
            xusage.SetAttribute('disk_space', str(self.getTotalSize()))
            tfile = Filename.temporary(pathname.cStr(), '.xml')
            if doc.SaveFile(tfile.toOsSpecific()):
                tfile.renameTo(usageFilename)
        return

    def getTotalSize(self):
        return self.nestedSize + self.fileSize

    def extractSubdir(self, pathname):
        for subdir in self.nested:
            if subdir.pathname == pathname:
                self.nested.remove(subdir)
                self.nestedSize -= subdir.getTotalSize()
                return subdir
            result = subdir.extractSubdir(pathname)
            if result:
                self.nestedSize -= result.getTotalSize()
                if subdir.getTotalSize() == 0:
                    self.nested.remove(subdir)
                return result

        return