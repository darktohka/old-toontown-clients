# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\launcher\ToontownDownloadWatcher.py
from direct.directnotify import DirectNotifyGlobal
from otp.launcher.DownloadWatcher import DownloadWatcher
from toontown.toonbase import TTLocalizer

class ToontownDownloadWatcher(DownloadWatcher):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownDownloadWatcher')

    def __init__(self, phaseNames):
        DownloadWatcher.__init__(self, phaseNames)

    def update(self, phase, percent, reqByteRate, actualByteRate):
        DownloadWatcher.update(self, phase, percent, reqByteRate, actualByteRate)
        phaseName = self.phaseNames[phase]
        self.text['text'] = TTLocalizer.LoadingDownloadWatcherUpdate % phaseName