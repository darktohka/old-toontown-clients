# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\LobbyManager.py
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class LobbyManager(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('LobbyManager')
    SetFactoryZoneMsg = 'setFactoryZone'

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def generate(self):
        self.notify.debug('generate')
        DistributedObject.DistributedObject.generate(self)

    def disable(self):
        self.notify.debug('disable')
        self.ignoreAll()
        DistributedObject.DistributedObject.disable(self)

    def getSuitDoorOrigin(self):
        return 1

    def getBossLevel(self):
        return 0