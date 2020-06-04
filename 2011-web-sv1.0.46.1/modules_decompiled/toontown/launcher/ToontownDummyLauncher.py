# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\launcher\ToontownDummyLauncher.py
from direct.directnotify import DirectNotifyGlobal
from otp.launcher.DummyLauncherBase import DummyLauncherBase
from toontown.launcher.ToontownLauncher import ToontownLauncher

class ToontownDummyLauncher(DummyLauncherBase, ToontownLauncher):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownDummyLauncher')

    def __init__(self):
        DummyLauncherBase.__init__(self)
        self.setPhaseComplete(1, 100)
        self.setPhaseComplete(2, 100)
        self.setPhaseComplete(3, 100)
        self.tutorialComplete = 1
        self.frequency = 0.0
        self.windowOpen = 0
        self.firstPhase = 3.5
        self.pandaErrorCodeKey = 'PANDA_ERROR_CODE'
        self.goUserName = ''
        self.periodTimeRemainingKey = 'PERIOD_TIME_REMAINING'
        self.periodNameKey = 'PERIOD_NAME'
        self.swidKey = 'SWID'
        self.reg = {}
        self.startFakeDownload()

    def setTutorialComplete(self, complete):
        self.tutorialComplete = complete

    def getTutorialComplete(self):
        return self.tutorialComplete

    def setFrequency(self, freq):
        self.frequency = freq

    def getFrequency(self):
        return self.frequency

    def getInstallDir(self):
        return 'C:\\Program Files\\Disney\\Disney Online\\Toontown'

    def getUserName(self):
        return 'dummy'

    def getReferrerCode(self):
        return

    def setRegistry(self, name, value):
        print 'setRegistry[%s] = %s' % (name, value)
        self.reg[name] = value

    def getRegistry(self, name, defaultValue=None):
        if name in self.reg:
            value = self.reg[name]
        else:
            value = defaultValue
        print 'getRegistry[%s] = %s' % (name, value)
        return value

    def getGame2Done(self):
        return 1

    def recordPeriodTimeRemaining(self, secondsRemaining):
        self.setRegistry(self.periodTimeRemainingKey, secondsRemaining)

    def recordPeriodName(self, periodName):
        self.setRegistry(self.periodNameKey, periodName)

    def recordSwid(self, swid):
        self.setRegistry(self.swidKey, swid)

    def getGoUserName(self):
        return self.goUserName

    def setGoUserName(self, userName):
        self.goUserName = userName

    def getParentPasswordSet(self):
        return 0

    def getNeedPwForSecretKey(self):
        return 0