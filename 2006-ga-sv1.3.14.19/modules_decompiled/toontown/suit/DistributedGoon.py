# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import *
from GoonGlobals import *
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.distributed import ClockDelta
from direct.level import BasicEntities
from direct.level import DistributedEntity
from direct.directnotify import DirectNotifyGlobal
from toontown.coghq import DistributedCrushableEntity
from toontown.toonbase import ToontownGlobals
from toontown.coghq import MovingPlatform
import Goon
from direct.level import PathEntity
import GoonDeath
import whrandom

class DistributedGoon(DistributedCrushableEntity.DistributedCrushableEntity, Goon.Goon):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGoon')
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedGoon_initialized = 1
            DistributedCrushableEntity.DistributedCrushableEntity.__init__(self, cr)
            Goon.Goon.__init__(self, 'pg')
            self.createHead()
            self.find('**/actorGeom').setH(180)
            self.initCollisions()

        self.setCacheable(1)
        self.rayNode = None
        self.checkForWalls = 0
        self.triggerEvent = None
        self.animTrack = None
        self.walkTrack = None
        self.crushTrack = None
        self.pauseTime = 0
        self.paused = 0
        self.path = None
        self.dir = GOON_FORWARD
        self.animMultiplier = 1.0
        self.isDead = 0
        self.collapseSound = loader.loadSfx('phase_9/audio/sfx/CHQ_GOON_hunker_down.mp3')
        self.recoverSound = loader.loadSfx('phase_9/audio/sfx/CHQ_GOON_rattle_shake.mp3')
        self.attackSound = loader.loadSfx('phase_9/audio/sfx/CHQ_GOON_tractor_beam_alarmed.mp3')
        self.fsm = ClassicFSM.ClassicFSM('DistributedGoon', [
            State.State('Off', self.enterOff, self.exitOff, [
                'Walk']),
            State.State('Walk', self.enterWalk, self.exitWalk, [
                'Battle',
                'Stunned']),
            State.State('Stunned', self.enterStunned, self.exitStunned, [
                'Recovery']),
            State.State('Recovery', self.enterRecovery, self.exitRecovery, [
                'Walk']),
            State.State('Battle', self.enterBattle, self.exitBattle, [
                'Walk'])], 'Off', 'Off')

    
    def announceGenerate(self):
        DistributedCrushableEntity.DistributedCrushableEntity.announceGenerate(self)
        self.scaleRadar()
        self.initializeBodyCollisions()
        triggerName = self.uniqueName('GoonTrigger')
        self.trigger.setName(triggerName)
        self.triggerEvent = 'enter%s' % triggerName
        self.initClipPlanes()
        self.level.setEntityCreateCallback(self.parentEntId, self.setPath)
        if self.strength > 19:
            self.hat.setColorScale(0.94999999999999996, 0, 0, 1)
        elif self.strength > 14:
            self.hat.setColorScale(0.75, 0.34999999999999998, 0.10000000000000001, 1)
        
        self.setScale(self.scale)
        self.animMultiplier = self.velocity / ANIM_WALK_RATE
        self.setPlayRate(self.animMultiplier, 'walk')
        self.fsm.enterInitialState()
        self._DistributedGoon__startToonDetect()

    
    def generate(self):
        DistributedCrushableEntity.DistributedCrushableEntity.generate(self)

    
    def createHead(self):
        self.headHeight = 3.0
        head = self.find('**/joint35')
        if head.isEmpty():
            head = self.find('**/joint40')
        
        self.hat = self.find('**/joint8')
        parentNode = head.getParent()
        self.head = parentNode.attachNewNode('headRotate')
        head.reparentTo(self.head)
        self.hat.reparentTo(self.head)
        self.eye = self.find('**/eye')
        self.eye.setColorScale(1, 1, 1, 1)
        self.eye.setColor(1, 1, 0, 1)
        self.radar = None
        self.trigger = None

    
    def scaleRadar(self):
        if self.radar:
            self.radar.removeNode()
        
        self.radar = loader.loadModelCopy('phase_9/models/cogHQ/alphaCone2')
        transform = self.radar.find('**/transform')
        if not transform.isEmpty():
            self.radar = transform
        
        self.radar.setPos(0, -0.5, 0.40000000000000002)
        self.radar.setHpr(0, 25, 0)
        self.radar.setTransparency(1)
        self.radar.setDepthWrite(0)
        self.radar.reparentTo(self.eye)
        self.halfFov = self.hFov / 2.0
        fovRad = self.halfFov * math.pi / 180.0
        self.cosHalfFov = math.cos(fovRad)
        kw = math.tan(fovRad) * self.attackRadius / 10.5
        kl = math.sqrt(self.attackRadius * self.attackRadius + 9.0) / 25.0
        self.radar.setScale(kw, kl, kw)
        self.radar.setP(self.halfFov)
        self.radar.flattenLight()
        self.radar.setColor(1, 1, 1, 0.20000000000000001)
        self.trigger = self.radar.find('**/trigger')
        triggerName = self.uniqueName('GoonTrigger')
        self.trigger.setName(triggerName)

    
    def initCollisions(self):
        self.cSphere = CollisionSphere(0.0, 0.0, 1.0, 1.0)
        self.cSphereNode = CollisionNode('goonCollSphere')
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.head.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereBitMask = ToontownGlobals.WallBitmask
        self.cSphereNode.setCollideMask(self.cSphereBitMask)
        self.cSphere.setTangible(1)
        self.sSphere = CollisionSphere(0.0, 0.0, self.headHeight + 0.80000000000000004, 0.20000000000000001)
        self.sSphereNode = CollisionNode('toonSphere')
        self.sSphereNode.addSolid(self.sSphere)
        self.sSphereNodePath = self.head.attachNewNode(self.sSphereNode)
        self.sSphereNodePath.hide()
        self.sSphereBitMask = ToontownGlobals.WallBitmask
        self.sSphereNode.setCollideMask(self.sSphereBitMask)
        self.sSphere.setTangible(1)

    
    def initializeBodyCollisions(self):
        self.cSphereNode.setName(self.uniqueName('goonCollSphere'))
        self.sSphereNode.setName(self.uniqueName('toonSphere'))
        self.accept(self.uniqueName('entertoonSphere'), self._DistributedGoon__handleStun)

    
    def disableBodyCollisions(self):
        self.ignore(self.uniqueName('entertoonSphere'))

    
    def deleteCollisions(self):
        self.sSphereNodePath.removeNode()
        del self.sSphereNodePath
        del self.sSphereNode
        del self.sSphere
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath
        del self.cSphereNode
        del self.cSphere

    
    def initClipPlanes(self):
        zoneNum = self.getZoneEntity().getZoneNum()
        clipList = self.level.goonClipPlanes.get(zoneNum)
        if clipList:
            planes = []
            for id in clipList:
                clipPlane = self.level.getEntity(id)
                planes.append(clipPlane.getPlane())
            
            cpa = ClipPlaneAttrib.make(ClipPlaneAttrib.OAdd, *planes)
            self.radar.node().setAttrib(cpa)
        

    
    def disableClipPlanes(self):
        if self.radar:
            cpaType = ClipPlaneAttrib.getClassType()
            self.radar.node().clearAttrib(cpaType)
        

    
    def setPath(self):
        self.path = self.level.getEntity(self.parentEntId)
        if self.walkTrack:
            del self.walkTrack
            self.walkTrack = None
        
        self.walkTrack = self.path.makePathTrack(self, self.velocity, self.uniqueName('goonWalk'), turnTime = T_TURN)
        if self.gridId != None:
            self.sendUpdate('setParameterize', [
                self.path.pos[0],
                self.path.pos[1],
                self.path.pos[2],
                self.path.pathIndex])
        

    
    def disable(self):
        self.notify.debug('DistributedGoon %d: disabling' % self.getDoId())
        self.ignoreAll()
        self._DistributedGoon__stopToonDetect()
        taskMgr.remove(self.taskName('resumeWalk'))
        taskMgr.remove(self.taskName('recoveryDone'))
        self.fsm.request('Off')
        self.disableBodyCollisions()
        self.disableClipPlanes()
        if self.animTrack:
            self.animTrack.pause()
            del self.animTrack
            self.animTrack = None
        
        if self.walkTrack:
            self.walkTrack.pause()
            del self.walkTrack
            self.walkTrack = None
        
        DistributedCrushableEntity.DistributedCrushableEntity.disable(self)

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedSuit_deleted = 1
            self.notify.debug('DistributedGoon %d: deleting' % self.getDoId())
            self.deleteCollisions()
            del self.fsm
            self.fsm = None
            self.head.removeNode()
            del self.head
            del self.attackSound
            del self.collapseSound
            del self.recoverSound
            DistributedCrushableEntity.DistributedCrushableEntity.delete(self)
            Goon.Goon.delete(self)


    
    def enterOff(self, *args):
        self.hideNametag3d()
        self.hideNametag2d()
        self.hide()

    
    def exitOff(self):
        self.show()
        self.showNametag3d()
        self.showNametag2d()

    
    def enterWalk(self, avId = None, ts = 0):
        self.notify.debug('enterWalk, ts = %s' % ts)
        self._DistributedGoon__startToonDetect()
        self.loop('walk', 0)
        if self.path:
            if not (self.walkTrack):
                self.walkTrack = self.path.makePathTrack(self, self.velocity, self.uniqueName('goonWalk'), turnTime = T_TURN)
            
            self.startWalk(ts)
        

    
    def startWalk(self, ts):
        tOffset = ts % self.walkTrack.getDuration()
        self.walkTrack.loop()
        self.walkTrack.pause()
        self.walkTrack.setT(tOffset)
        self.walkTrack.resume()
        self.paused = 0

    
    def exitWalk(self):
        self.notify.debug('exitWalk')
        self._DistributedGoon__stopToonDetect()
        if self.walkTrack and not (self.paused):
            self.pauseTime = self.walkTrack.pause()
            self.paused = 1
        
        self.stop()

    
    def enterBattle(self, avId = None, ts = 0):
        self.notify.debug('enterBattle')
        self._DistributedGoon__stopToonDetect()
        if self.animTrack:
            self.animTrack.finish()
            del self.animTrack
            self.animTrack = None
        
        if avId == base.localAvatar.doId:
            self.level.b_setOuch(self.strength)
        
        self.animTrack = self.makeAttackTrack()
        self.animTrack.loop()

    
    def exitBattle(self):
        self.notify.debug('exitBattle')
        if self.animTrack:
            self.animTrack.finish()
            del self.animTrack
        
        self.animTrack = None
        self.head.setHpr(0, 0, 0)

    
    def enterStunned(self, ts = 0):
        self.ignore(self.uniqueName('entertoonSphere'))
        self.notify.debug('enterStunned')
        if self.radar:
            self.radar.hide()
        
        self.animTrack = Parallel(Sequence(ActorInterval(self, 'collapse'), Func(self.pose, 'collapse', 48)), SoundInterval(self.collapseSound, node = self))
        self.animTrack.start(ts)

    
    def exitStunned(self):
        self.notify.debug('exitStunned')
        if self.radar:
            self.radar.show()
        
        if self.animTrack != None:
            self.animTrack.finish()
            self.animTrack = None
        

    
    def enterRecovery(self, ts = 0, pauseTime = 0):
        self.notify.debug('enterRecovery')
        if self.animTrack:
            self.animTrack.pause()
            del self.animTrack
            self.animTrack = None
        
        self.animTrack = self.getRecoveryTrack()
        duration = self.animTrack.getDuration()
        self.animTrack.start(ts)
        delay = max(0, duration - ts)
        taskMgr.remove(self.taskName('recoveryDone'))
        taskMgr.doMethodLater(delay, self.recoveryDone, self.taskName('recoveryDone'), extraArgs = (pauseTime,))

    
    def getRecoveryTrack(self):
        return Parallel(Sequence(ActorInterval(self, 'recovery'), Func(self.pose, 'recovery', 96)), Func(base.playSfx, self.recoverSound, node = self))

    
    def recoveryDone(self, pauseTime):
        self.fsm.request('Walk', [
            None,
            pauseTime])

    
    def exitRecovery(self):
        self.notify.debug('exitRecovery')
        if self.animTrack != None:
            self.animTrack.finish()
            self.animTrack = None
        
        self.accept(self.uniqueName('entertoonSphere'), self._DistributedGoon__handleStun)

    
    def makeAttackTrack(self):
        h = self.head.getH()
        freakDeg = 60
        hatZ = self.hat.getZ()
        track = Parallel(Sequence(LerpColorScaleInterval(self.eye, 0.20000000000000001, Vec4(1, 0, 0, 1)), LerpColorScaleInterval(self.eye, 0.20000000000000001, Vec4(0, 0, 1, 1)), LerpColorScaleInterval(self.eye, 0.20000000000000001, Vec4(1, 0, 0, 1)), LerpColorScaleInterval(self.eye, 0.20000000000000001, Vec4(0, 0, 1, 1)), Func(self.eye.clearColorScale)), SoundInterval(self.attackSound, node = self, volume = 0.40000000000000002))
        return track

    
    def doDetect(self):
        pass

    
    def doAttack(self, avId):
        return None

    
    def _DistributedGoon__startResumeWalkTask(self, ts):
        resumeTime = 1.5
        if ts < resumeTime:
            taskMgr.remove(self.taskName('resumeWalk'))
            taskMgr.doMethodLater(resumeTime - ts, self.fsm.request, self.taskName('resumeWalk'), extraArgs = ('Walk',))
        else:
            self.fsm.request('Walk', [
                ts - resumeTime])

    
    def _DistributedGoon__reverseWalk(self, task):
        if self.fsm:
            self.fsm.request('Walk')
        
        return Task.done

    
    def _DistributedGoon__startRecoverTask(self, ts):
        stunTime = 4.0
        if ts < stunTime:
            taskMgr.remove(self.taskName('resumeWalk'))
            taskMgr.doMethodLater(stunTime - ts, self.fsm.request, self.taskName('resumeWalk'), extraArgs = ('Recovery',))
        else:
            self.fsm.request('Recovery', [
                ts - stunTime])

    
    def _DistributedGoon__startToonDetect(self):
        if self.triggerEvent:
            self.accept(self.triggerEvent, self._DistributedGoon__handleToonDetect)
        

    
    def _DistributedGoon__stopToonDetect(self):
        if self.triggerEvent:
            self.ignore(self.triggerEvent)
        

    
    def _DistributedGoon__handleToonDetect(self, collEntry = None):
        if base.localAvatar.isStunned:
            return None
        
        self._DistributedGoon__stopToonDetect()
        self.fsm.request('Battle', [
            base.localAvatar.doId])
        if self.walkTrack:
            self.pauseTime = self.walkTrack.pause()
            self.paused = 1
        
        self.sendUpdate('requestBattle', [
            self.pauseTime])

    
    def _DistributedGoon__handleStun(self, collEntry):
        self.fsm.request('Stunned')
        if self.walkTrack:
            self.pauseTime = self.walkTrack.pause()
            self.paused = 1
        
        self.sendUpdate('requestStunned', [
            self.pauseTime])

    
    def setMovie(self, mode, avId, pauseTime, timestamp):
        if self.isDead:
            return None
        
        ts = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.notify.debug('%s: setMovie(%s,%s,%s,%s)' % (self.doId, mode, avId, pauseTime, ts))
        if mode == GOON_MOVIE_BATTLE:
            self.fsm.request('Battle', [
                avId,
                ts])
        elif mode == GOON_MOVIE_STUNNED:
            self.fsm.request('Stunned', [
                ts])
        elif mode == GOON_MOVIE_RECOVERY:
            self.fsm.request('Recovery', [
                ts,
                pauseTime])
        elif mode == GOON_MOVIE_SYNC:
            if self.fsm.getCurrentState().getName() == 'Walk':
                self.fsm.request('Off')
                if self.walkTrack:
                    self.walkTrack.pause()
                    self.paused = 1
                
            
            if self.fsm.getCurrentState().getName() == 'Off':
                self.fsm.request('Walk', [
                    avId,
                    pauseTime + ts])
            
        elif self.fsm.getCurrentState().getName() == 'Walk':
            self.fsm.request('Off')
            if self.walkTrack:
                self.walkTrack.pause()
                del self.walkTrack
                self.walkTrack = None
            
        
        self.fsm.request('Walk', [
            avId,
            pauseTime + ts])

    
    def stunToon(self, avId):
        self.notify.debug('stunToon(%s)' % avId)
        av = base.cr.doId2do.get(avId)
        if av != None:
            av.stunToon()
        

    
    def isLocalToon(self, avId):
        if avId == base.localAvatar.doId:
            return 1
        
        return 0

    
    def playCrushMovie(self, crusherId, axis):
        goonPos = self.getPos()
        deathNode = self.getParent().attachNewNode('deathNode')
        deathNode.setPos(goonPos)
        dx = 1.5 * whrandom.random()
        dy = 1.5 * whrandom.random()
        deathNode.setScale(1 + dx, 1 + dy, 1)
        self.crushTrack = Sequence(Func(self.dead), GoonDeath.createGoonExplosion(deathNode))
        self.crushTrack.start()

    
    def setVelocity(self, velocity):
        self.velocity = velocity
        self.animMultiplier = velocity / ANIM_WALK_RATE
        self.setPlayRate(self.animMultiplier, 'walk')

    
    def dead(self):
        if not (self.isDead):
            self._DistributedGoon__stopToonDetect()
            self.stash()
            self.isDead = 1
        

    
    def undead(self):
        if self.isDead:
            self.unstash()
            self._DistributedGoon__startToonDetect()
            self.isDead = 0
        

    
    def resync(self):
        if not (self.isDead):
            self.sendUpdate('requestResync')
        

    
    def setHFov(self, hFov):
        self.hFov = hFov
        self.scaleRadar()


