# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\safezone\MMSafeZoneLoader.py
from pandac.PandaModules import *
import SafeZoneLoader, MMPlayground
from toontown.toonbase import ToontownGlobals

class MMSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    __module__ = __name__

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = MMPlayground.MMPlayground
        self.musicFile = 'phase_6/audio/bgm/MM_nbrhood.mid'
        self.activityMusicFile = 'phase_6/audio/bgm/MM_SZ_activity.mid'
        self.dnaFile = 'phase_6/dna/minnies_melody_land_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_MM_sz.dna'

    def load(self):
        print 'loading MM safezone'
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.piano = self.geom.find('**/center_icon')
        if self.piano.isEmpty():
            self.notify.error('Piano not found')
        else:
            hq = self.geom.find('**/*toon_landmark_hqMM_DNARoot')
            hq.wrtReparentTo(self.piano)

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.piano