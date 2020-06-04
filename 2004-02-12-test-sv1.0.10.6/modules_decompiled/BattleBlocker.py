# File: B (Python 2.2)

from ShowBaseGlobal import *
from PandaModules import *
from IntervalGlobal import *
import BasicEntities
import ToontownGlobals
import DirectNotifyGlobal

class BattleBlocker(BasicEntities.DistributedNodePathEntity):
    notify = DirectNotifyGlobal.directNotify.newCategory('BattleBlocker')
    
    def __init__(self, cr):
        BasicEntities.DistributedNodePathEntity.__init__(self, cr)
        self.suitIds = []
        self.battleId = None

    
    def setActive(self, active):
        self.active = active

    
    def announceGenerate(self):
        BasicEntities.DistributedNodePathEntity.announceGenerate(self)
        self.initCollisionGeom()

    
    def disable(self):
        self.ignoreAll()
        self.unloadCollisionGeom()
        BasicEntities.DistributedNodePathEntity.disable(self)

    
    def destroy(self):
        BasicEntities.DistributedNodePathEntity.destroy(self)

    
    def setSuits(self, suitIds):
        self.suitIds = suitIds

    
    def setBattle(self, battleId):
        self.battleId = battleId

    
    def setBattleFinished(self):
        return None

    
    def initCollisionGeom(self):
        self.cSphere = CollisionSphere(0, 0, 0, self.radius)
        self.cSphereNode = CollisionNode('battleBlocker-' + str(self.entId))
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNode.setCollideMask(ToontownGlobals.WallBitmask)
        self.cSphere.setTangible(0)
        self.enterEvent = 'enter' + self.cSphereNode.getName()
        self.accept(self.enterEvent, self._BattleBlocker__handleToonEnter)

    
    def unloadCollisionGeom(self):
        if hasattr(self, 'cSphereNodePath'):
            self.ignore(self.enterEvent)
            del self.cSphere
            del self.cSphereNode
            self.cSphereNodePath.removeNode()
            del self.cSphereNodePath
        

    
    def _BattleBlocker__handleToonEnter(self, collEntry):
        self.notify.debug('__handleToonEnter, %s' % self.entId)
        if not (self.active):
            return None
        
        self.ignoreAll()
        callback = None
        if self.battleId != None:
            battle = toonbase.tcr.doId2do.get(self.battleId)
            if battle:
                self.notify.debug('act like we collided with battle %d' % self.battleId)
                callback = battle.handleBattleBlockerCollision
            
        elif len(self.suitIds) > 0:
            for suitId in self.suitIds:
                suit = toonbase.tcr.doId2do.get(suitId)
                if suit:
                    self.notify.debug('act like we collided with Suit %d ( in state %s )' % (suitId, suit.fsm.getCurrentState().getName()))
                    callback = suit.handleBattleBlockerCollision
                    break
                
            
        
        self.showReaction(callback)

    
    def showReaction(self, callback = None):
        if not (toonbase.localToon.wantBattles):
            return None
        
        track = Sequence()
        if callback:
            track.append(Func(callback))
        
        track.start()

    if __dev__:
        
        def attribChanged(self, *args):
            self.unloadCollisionGeom()
            self.initCollisionGeom()

    

