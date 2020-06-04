# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\hood\DLHood.py
from pandac.PandaModules import *
import ToonHood
from toontown.town import DLTownLoader
from toontown.safezone import DLSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *

class DLHood(ToonHood.ToonHood):
    __module__ = __name__

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = DonaldsDreamland
        self.townLoaderClass = DLTownLoader.DLTownLoader
        self.safeZoneLoaderClass = DLSafeZoneLoader.DLSafeZoneLoader
        self.storageDNAFile = 'phase_8/dna/storage_DL.dna'
        self.holidayStorageDNADict = {WINTER_DECORATIONS: ['phase_8/dna/winter_storage_DL.dna'], HALLOWEEN_PROPS: ['phase_8/dna/halloween_props_storage_DL.dna']}
        self.skyFile = 'phase_8/models/props/DL_sky'
        self.titleColor = (1.0, 0.9, 0.5, 1.0)

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('DLHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('DLHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    def enter(self, *args):
        ToonHood.ToonHood.enter(self, *args)

    def exit(self):
        ToonHood.ToonHood.exit(self)