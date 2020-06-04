# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\p3d\InstalledHostData.py
from pandac.PandaModules import URLSpec

class InstalledHostData:
    __module__ = __name__

    def __init__(self, host, dirnode):
        self.host = host
        self.pathname = dirnode.pathname
        self.totalSize = dirnode.getTotalSize()
        self.packages = []
        if self.host:
            self.hostUrl = self.host.hostUrl
            self.descriptiveName = self.host.descriptiveName
            if not self.descriptiveName:
                self.descriptiveName = URLSpec(self.hostUrl).getServer()
        else:
            self.hostUrl = 'unknown'
            self.descriptiveName = 'unknown'