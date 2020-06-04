# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\launcher\ToontownWebLauncher.py
import os
from otp.launcher.WebLauncherBase import WebLauncherBase
from toontown.toonbase import TTLocalizer
from pandac.PandaModules import *

class ToontownWebLauncher(WebLauncherBase):
    __module__ = __name__
    GameName = 'Toontown'
    LauncherPhases = [
     (3, 'tt_3'), (3.5, 'tt_3_5'), (4, 'tt_4'), (5, 'tt_5'), (5.5, 'tt_5_5'), (6, 'tt_6'), (7, 'tt_7'), (8, 'tt_8'), (9, 'tt_9'), (10, 'tt_10'), (11, 'tt_11'), (12, 'tt_12'), (13, 'tt_13')]
    Localizer = TTLocalizer

    def __init__(self, appRunner):
        WebLauncherBase.__init__(self, appRunner)
        self.http = HTTPClient.getGlobalPtr()
        self.webAcctParams = 'WEB_ACCT_PARAMS'
        self.parseWebAcctParams()
        self.startDownload()
        self.toontownBlueKey = 'TOONTOWN_BLUE'
        self.toontownPlayTokenKey = 'TOONTOWN_PLAYTOKEN'
        self.launcherMessageKey = 'LAUNCHER_MESSAGE'
        self.game1DoneKey = 'GAME1_DONE'
        self.game2DoneKey = 'GAME2_DONE'
        self.tutorialCompleteKey = 'TUTORIAL_DONE'
        from toontown.toonbase import ToontownStart

    def getAccountServer(self):
        return self.getValue('ACCOUNT_SERVER', '')

    def getNeedPwForSecretKey(self):
        return self.secretNeedsParentPasswordKey

    def getParentPasswordSet(self):
        return self.chatEligibleKey

    def setTutorialComplete(self):
        pass

    def getTutorialComplete(self):
        return False

    def getGame2Done(self):
        return True

    def parseWebAcctParams(self):
        s = ConfigVariableString('fake-web-acct-params', '').getValue()
        if not s:
            s = self.getValue(self.webAcctParams, '')
        l = s.split('&')
        length = len(l)
        dict = {}
        for index in range(0, len(l)):
            args = l[index].split('=')
            if len(args) == 3:
                (name, value) = args[-2:]
                dict[name] = int(value)
            elif len(args) == 2:
                (name, value) = args
                dict[name] = int(value)

        self.secretNeedsParentPasswordKey = 1
        if dict.has_key('secretsNeedsParentPassword'):
            self.secretNeedsParentPasswordKey = dict['secretsNeedsParentPassword']
        else:
            self.notify.warning('no secretNeedsParentPassword token in webAcctParams')
        self.notify.info('secretNeedsParentPassword = %d' % self.secretNeedsParentPasswordKey)
        self.chatEligibleKey = 0
        if dict.has_key('chatEligible'):
            self.chatEligibleKey = dict['chatEligible']
        else:
            self.notify.warning('no chatEligible token in webAcctParams')
        self.notify.info('chatEligibleKey = %d' % self.chatEligibleKey)

    def getBlue(self):
        blue = self.getValue(self.toontownBlueKey)
        self.setValue(self.toontownBlueKey, '')
        if blue == 'NO BLUE':
            blue = None
        return blue

    def getPlayToken(self):
        playToken = self.getValue(self.toontownPlayTokenKey)
        self.setValue(self.toontownPlayTokenKey, '')
        if playToken == 'NO PLAYTOKEN':
            playToken = None
        return playToken