# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedKartShopInterior.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject
from pandac.PandaModules import *
from toontown.building import ToonInteriorColors
from toontown.hood import ZoneUtil
from toontown.toonbase.ToonBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
if __debug__:
    import pdb

class DistributedKartShopInterior(DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedKartShopInterior')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.dnaStore = cr.playGame.dnaStore

    def generate(self):
        DistributedObject.generate(self)

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        self.__handleInteriorSetup()

    def disable(self):
        self.interior.removeNode()
        del self.interior
        DistributedObject.disable(self)

    def setZoneIdAndBlock(self, zoneId, block):
        self.zoneId = zoneId
        self.block = block

    def __handleInteriorSetup(self):
        self.interior = loader.loadModel('phase_6/models/karting/KartShop_Interior')
        self.interior.reparentTo(render)
        self.interior.flattenMedium()