# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\toon\DistributedNPCFlippyInToonHall.py
from pandac.PandaModules import *
from DistributedNPCToon import *

class DistributedNPCFlippyInToonHall(DistributedNPCToon):
    __module__ = __name__

    def __init__(self, cr):
        DistributedNPCToon.__init__(self, cr)

    def getCollSphereRadius(self):
        return 4

    def initPos(self):
        self.clearMat()
        self.setScale(1.25)

    def handleCollisionSphereEnter(self, collEntry):
        if self.allowedToTalk():
            base.cr.playGame.getPlace().fsm.request('quest', [self])
            self.sendUpdate('avatarEnter', [])
            self.nametag3d.setDepthTest(0)
            self.nametag3d.setBin('fixed', 0)
            self.lookAt(base.localAvatar)
        else:
            place = base.cr.playGame.getPlace()
            if place:
                place.fsm.request('stopped')
            self.dialog = TeaserPanel.TeaserPanel(pageName='quests', doneFunc=self.handleOkTeaser)