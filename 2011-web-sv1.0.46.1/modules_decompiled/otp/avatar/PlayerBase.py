# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\avatar\PlayerBase.py


class PlayerBase:
    __module__ = __name__

    def __init__(self):
        self.gmState = False

    def atLocation(self, locationId):
        return True

    def getLocation(self):
        return []

    def setAsGM(self, state):
        self.gmState = state

    def isGM(self):
        return self.gmState