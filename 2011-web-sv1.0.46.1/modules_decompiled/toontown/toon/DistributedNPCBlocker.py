# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\toon\DistributedNPCBlocker.py
from pandac.PandaModules import *
from DistributedNPCToonBase import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
import NPCToons
from toontown.toonbase import TTLocalizer
from direct.distributed import DistributedObject
from toontown.quest import QuestParser

class DistributedNPCBlocker(DistributedNPCToonBase):
    __module__ = __name__

    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.cSphereNodePath.setScale(4.5, 1.0, 6.0)
        self.isLocalToon = 1
        self.movie = None
        return

    def announceGenerate(self):
        DistributedNPCToonBase.announceGenerate(self)

    def initToonState(self):
        self.setAnimState('neutral', 0.9, None, None)
        posh = NPCToons.BlockerPositions[self.name]
        self.setPos(posh[0])
        self.setH(posh[1])
        return

    def disable(self):
        if hasattr(self, 'movie') and self.movie:
            self.movie.cleanup()
            del self.movie
            if self.isLocalToon == 1:
                base.localAvatar.posCamera(0, 0)
        DistributedNPCToonBase.disable(self)

    def handleCollisionSphereEnter(self, collEntry):
        base.cr.playGame.getPlace().fsm.request('quest', [self])
        self.sendUpdate('avatarEnter', [])

    def __handleUnexpectedExit(self):
        self.notify.warning('unexpected exit')

    def resetBlocker(self):
        self.cSphereNode.setCollideMask(BitMask32())
        if hasattr(self, 'movie') and self.movie:
            self.movie.cleanup()
            self.movie = None
        self.startLookAround()
        self.clearMat()
        if self.isLocalToon == 1:
            base.localAvatar.posCamera(0, 0)
            self.freeAvatar()
            self.isLocalToon = 0
        return

    def setMovie(self, mode, npcId, avId, timestamp):
        timeStamp = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.npcId = npcId
        self.isLocalToon = avId == base.localAvatar.doId
        if mode == NPCToons.BLOCKER_MOVIE_CLEAR:
            return
        elif mode == NPCToons.BLOCKER_MOVIE_START:
            self.movie = QuestParser.NPCMoviePlayer('tutorial_blocker', base.localAvatar, self)
            self.movie.play()
        elif mode == NPCToons.BLOCKER_MOVIE_TIMEOUT:
            return

    def finishMovie(self, av, isLocalToon, elapsedTime):
        self.resetBlocker()