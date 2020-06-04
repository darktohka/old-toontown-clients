# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\FactoryManagerAI.py
from direct.directnotify import DirectNotifyGlobal
import DistributedFactoryAI
from toontown.toonbase import ToontownGlobals
from direct.showbase import DirectObject

class FactoryManagerAI(DirectObject.DirectObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FactoryManagerAI')
    factoryId = None

    def __init__(self, air):
        DirectObject.DirectObject.__init__(self)
        self.air = air

    def getDoId(self):
        return 0

    def createFactory(self, factoryId, entranceId, players):
        factoryZone = self.air.allocateZone()
        if FactoryManagerAI.factoryId is not None:
            factoryId = FactoryManagerAI.factoryId
        factory = DistributedFactoryAI.DistributedFactoryAI(self.air, factoryId, factoryZone, entranceId, players)
        factory.generateWithRequired(factoryZone)
        return factoryZone