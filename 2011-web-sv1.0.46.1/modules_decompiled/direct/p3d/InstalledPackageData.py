# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\InstalledPackageData.py


class InstalledPackageData:
    __module__ = __name__

    def __init__(self, package, dirnode):
        self.package = package
        self.pathname = dirnode.pathname
        self.totalSize = dirnode.getTotalSize()
        self.lastUse = None
        if self.package:
            self.displayName = self.package.getFormattedName()
            xusage = self.package.getUsage()
            if xusage:
                lastUse = xusage.Attribute('last_use')
                try:
                    lastUse = int(lastUse or '')
                except ValueError:
                    lastUse = None
                else:
                    self.lastUse = lastUse
        else:
            self.displayName = dirnode.pathname.getBasename()
        return