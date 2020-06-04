# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\DGSafeZoneLoader.py
from pandac.PandaModules import *
import SafeZoneLoader, DGPlayground

class DGSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    __module__ = __name__

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DGPlayground.DGPlayground
        self.musicFile = 'phase_8/audio/bgm/DG_nbrhood.mid'
        self.activityMusicFile = 'phase_8/audio/bgm/DG_SZ.mid'
        self.dnaFile = 'phase_8/dna/daisys_garden_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_8/dna/storage_DG_sz.dna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.bird1Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_01.mp3')
        self.bird2Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_02.mp3')
        self.bird3Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_03.mp3')
        self.bird4Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_04.mp3')

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.bird1Sound
        del self.bird2Sound
        del self.bird3Sound
        del self.bird4Sound

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)