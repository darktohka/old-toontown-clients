# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.toonbase import ToontownGlobals
import DistributedToon
from direct.distributed import DistributedObject
import NPCToons
from toontown.quest import Quests
from direct.distributed import ClockDelta
from direct.distributed import DelayDelete
from toontown.quest import QuestParser
from toontown.quest import QuestChoiceGui
from direct.interval.IntervalGlobal import *

class DistributedNPCToonBase(DistributedToon.DistributedToon):
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedNPCToon_initialized = 1
            DistributedToon.DistributedToon.__init__(self, cr)
            self._DistributedNPCToonBase__initCollisions()
            self.setPickable(0)
            self.setPlayerType(NametagGroup.CCNonPlayer)


    
    def disable(self):
        self.ignore('enter' + self.cSphereNode.getName())
        DistributedToon.DistributedToon.disable(self)

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedNPCToon_deleted = 1
            self._DistributedNPCToonBase__deleteCollisions()
            DistributedToon.DistributedToon.delete(self)


    
    def generate(self):
        DistributedToon.DistributedToon.generate(self)
        self.cSphereNode.setName(self.uniqueName('NPCToon'))
        self.detectAvatars()
        self.setParent(ToontownGlobals.SPRender)
        self.startLookAround()

    
    def generateToon(self):
        self.setLODs()
        self.generateToonLegs()
        self.generateToonHead()
        self.generateToonTorso()
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.rightHands = []
        self.leftHands = []
        self.headParts = []
        self.hipsParts = []
        self.torsoParts = []
        self.legsParts = []
        self._DistributedNPCToonBase__bookActors = []
        self._DistributedNPCToonBase__holeActors = []

    
    def announceGenerate(self):
        self.setAnimState('neutral', 0.90000000000000002, None, None)
        npcOrigin = render.find('**/npc_origin_' + `self.posIndex`)
        if not npcOrigin.isEmpty():
            self.reparentTo(npcOrigin)
            self.clearMat()
        else:
            self.notify.warning('announceGenerate: Could not find npc_origin_' + str(self.posIndex))
        DistributedObject.DistributedObject.announceGenerate(self)

    
    def wantsSmoothing(self):
        return 0

    
    def detectAvatars(self):
        self.accept('enter' + self.cSphereNode.getName(), self.handleCollisionSphereEnter)

    
    def ignoreAvatars(self):
        self.ignore('enter' + self.cSphereNode.getName())

    
    def getCollSphereRadius(self):
        return 3.0

    
    def _DistributedNPCToonBase__initCollisions(self):
        self.cSphere = CollisionSphere(0.0, 1.0, 0.0, self.getCollSphereRadius())
        self.cSphere.setTangible(0)
        self.cSphereNode = CollisionNode('cSphereNode')
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereNode.setCollideMask(ToontownGlobals.WallBitmask)

    
    def _DistributedNPCToonBase__deleteCollisions(self):
        del self.cSphere
        del self.cSphereNode
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath

    
    def handleCollisionSphereEnter(self, collEntry):
        pass

    
    def setupAvatars(self, av):
        self.ignoreAvatars()
        av.headsUp(self, 0, 0, 0)
        self.headsUp(av, 0, 0, 0)
        av.stopLookAround()
        av.lerpLookAt(Point3(-0.5, 4, 0), time = 0.5)
        self.stopLookAround()
        self.lerpLookAt(Point3(av.getPos(self)), time = 0.5)

    
    def b_setPageNumber(self, paragraph, pageNumber):
        self.setPageNumber(paragraph, pageNumber)
        self.d_setPageNumber(paragraph, pageNumber)

    
    def d_setPageNumber(self, paragraph, pageNumber):
        timestamp = ClockDelta.globalClockDelta.getFrameNetworkTime()
        self.sendUpdate('setPageNumber', [
            paragraph,
            pageNumber,
            timestamp])

    
    def freeAvatar(self):
        base.localAvatar.posCamera(0, 0)
        base.cr.playGame.getPlace().setState('walk')

    
    def setPositionIndex(self, posIndex):
        self.posIndex = posIndex


