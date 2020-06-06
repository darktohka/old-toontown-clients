# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from DistributedNPCToonBase import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
import NPCToons
from toontown.toonbase import TTLocalizer
from direct.distributed import DistributedObject
from toontown.quest import QuestParser

class DistributedNPCBlocker(DistributedNPCToonBase):
    
    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.cSphereNodePath.setScale(4.5, 1.0, 6.0)
        self.isLocalToon = 1
        self.movie = None

    
    def announceGenerate(self):
        self.setAnimState('neutral', 0.90000000000000002, None, None)
        posh = NPCToons.BlockerPositions[self.name]
        self.setPos(posh[0])
        self.setH(posh[1])
        DistributedObject.DistributedObject.announceGenerate(self)

    
    def disable(self):
        if self.movie:
            self.movie.cleanup()
            del self.movie
            if self.isLocalToon == 1:
                base.localAvatar.posCamera(0, 0)
            
        
        DistributedNPCToonBase.disable(self)

    
    def handleCollisionSphereEnter(self, collEntry):
        base.cr.playGame.getPlace().fsm.request('quest', [
            self])
        self.sendUpdate('avatarEnter', [])

    
    def _DistributedNPCBlocker__handleUnexpectedExit(self):
        self.notify.warning('unexpected exit')

    
    def resetBlocker(self):
        self.cSphereNode.setCollideMask(BitMask32())
        if self.movie:
            self.movie.cleanup()
            self.movie = None
        
        self.startLookAround()
        self.clearMat()
        if self.isLocalToon == 1:
            base.localAvatar.posCamera(0, 0)
            self.freeAvatar()
            self.isLocalToon = 0
        

    
    def setMovie(self, mode, npcId, avId, timestamp):
        timeStamp = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.npcId = npcId
        self.isLocalToon = avId == base.localAvatar.doId
        if mode == NPCToons.BLOCKER_MOVIE_CLEAR:
            return None
        elif mode == NPCToons.BLOCKER_MOVIE_START:
            self.movie = QuestParser.NPCMoviePlayer('tutorial_blocker', base.localAvatar, self)
            self.movie.play()
        elif mode == NPCToons.BLOCKER_MOVIE_TIMEOUT:
            return None
        
        return None

    
    def finishMovie(self, av, isLocalToon, elapsedTime):
        self.resetBlocker()


