# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\DistributedTagTreasure.py
from toontown.safezone import DistributedTreasure

class DistributedTagTreasure(DistributedTreasure.DistributedTreasure):
    __module__ = __name__

    def __init__(self, cr):
        DistributedTreasure.DistributedTreasure.__init__(self, cr)
        self.modelPath = 'phase_4/models/props/icecream'
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.mp3'
        self.accept('minigameOffstage', self.handleMinigameOffstage)

    def handleEnterSphere(self, collEntry):
        if not base.localAvatar.isIt:
            self.d_requestGrab()
        return

    def handleMinigameOffstage(self):
        self.nodePath.reparentTo(hidden)