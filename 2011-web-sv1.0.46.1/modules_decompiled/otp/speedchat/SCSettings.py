# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\speedchat\SCSettings.py
from SCColorScheme import SCColorScheme
from otp.otpbase import OTPLocalizer

class SCSettings:
    __module__ = __name__

    def __init__(self, eventPrefix, whisperMode=0, colorScheme=None, submenuOverlap=OTPLocalizer.SCOsubmenuOverlap, topLevelOverlap=None):
        self.eventPrefix = eventPrefix
        self.whisperMode = whisperMode
        if colorScheme is None:
            colorScheme = SCColorScheme()
        self.colorScheme = colorScheme
        self.submenuOverlap = submenuOverlap
        self.topLevelOverlap = topLevelOverlap
        return