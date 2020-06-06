# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
import DistributedSuitBase
import random
from toontown.toonbase import ToontownGlobals
from otp.level import LevelConstants

class DistributedFactorySuit(DistributedSuitBase.DistributedSuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFactorySuit')
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedSuit_initialized = 1
            DistributedSuitBase.DistributedSuitBase.__init__(self, cr)
            self.fsm = ClassicFSM.ClassicFSM('DistributedSuit', [
                State.State('Off', self.enterOff, self.exitOff, [
                    'Walk',
                    'Battle']),
                State.State('Walk', self.enterWalk, self.exitWalk, [
                    'WaitForBattle',
                    'Battle',
                    'Chase']),
                State.State('Chase', self.enterChase, self.exitChase, [
                    'WaitForBattle',
                    'Battle',
                    'Return']),
                State.State('Return', self.enterReturn, self.exitReturn, [
                    'WaitForBattle',
                    'Battle',
                    'Walk']),
                State.State('Battle', self.enterBattle, self.exitBattle, [
                    'Walk',
                    'Chase',
                    'Return']),
                State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, [
                    'Battle'])], 'Off', 'Off')
            self.path = None
            self.walkTrack = None
            self.chaseTrack = None
            self.returnTrack = None
            self.fsm.enterInitialState()
            self.chasing = 0
            self.paused = 0
            self.pauseTime = 0
            self.velocity = 3
            self.factoryRequest = None

        return None

    
    def generate(self):
        DistributedSuitBase.DistributedSuitBase.generate(self)

    
    def setLevelDoId(self, levelDoId):
        self.levelDoId = levelDoId

    
    def setCogId(self, cogId):
        self.cogId = cogId

    
    def setReserve(self, reserve):
        self.reserve = reserve

    
    def denyBattle(self):
        self.notify.warning('denyBattle()')
        place = self.cr.playGame.getPlace()
        if place.fsm.getCurrentState().getName() == 'WaitForBattle':
            place.setState('walk')
        

    
    def doReparent(self):
        self.notify.debug('Suit requesting reparenting')
        self.factory.requestReparent(self, self.spec['parentEntId'])
        if self.pathEntId:
            self.factory.setEntityCreateCallback(self.pathEntId, self.setPath)
        else:
            self.setPath()

    
    def setCogSpec(self, spec):
        self.spec = spec
        self.setPos(spec['pos'])
        self.setH(spec['h'])
        self.originalPos = spec['pos']
        self.escapePos = spec['pos']
        self.behavior = spec['behavior']
        self.pathEntId = spec['path']
        self.behavior = spec['behavior']
        self.skeleton = spec['skeleton']
        self.boss = spec['boss']
        if self.reserve:
            self.reparentTo(hidden)
        else:
            self.doReparent()

    
    def comeOutOfReserve(self):
        self.doReparent()

    
    def getCogSpec(self, cogId):
        if self.reserve:
            return self.factory.getReserveCogSpec(cogId)
        else:
            return self.factory.getCogSpec(cogId)

    
    def announceGenerate(self):
        self.notify.debug('announceGenerate %s' % self.doId)
        
        def onFactoryGenerate(factoryList, self = self):
            self.factory = factoryList[0]
            
            def onFactoryReady(self = self):
                self.notify.debug('factory ready, read spec')
                spec = self.getCogSpec(self.cogId)
                self.setCogSpec(spec)
                self.factoryRequest = None

            self.factory.setEntityCreateCallback(LevelConstants.LevelMgrEntId, onFactoryReady)

        self.factoryRequest = self.cr.relatedObjectMgr.requestObjects([
            self.levelDoId], onFactoryGenerate)

    
    def disable(self):
        self.ignoreAll()
        if self.factoryRequest is not None:
            self.cr.relatedObjectMgr.abortRequest(self.factoryRequest)
            self.factoryRequest = None
        
        self.notify.debug('DistributedSuit %d: disabling' % self.getDoId())
        self.setState('Off')
        if self.walkTrack:
            del self.walkTrack
            self.walkTrack = None
        
        DistributedSuitBase.DistributedSuitBase.disable(self)
        taskMgr.remove(self.taskName('returnTask'))
        taskMgr.remove(self.taskName('checkStray'))
        taskMgr.remove(self.taskName('chaseTask'))
        return None

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedSuit_deleted = 1
            self.notify.debug('DistributedSuit %d: deleting' % self.getDoId())
            del self.fsm
            DistributedSuitBase.DistributedSuitBase.delete(self)


    
    def d_requestBattle(self, pos, hpr):
        self.cr.playGame.getPlace().setState('WaitForBattle')
        self.factory.lockVisibility(zoneNum = self.factory.getEntityZoneEntId(self.spec['parentEntId']))
        self.sendUpdate('requestBattle', [
            pos[0],
            pos[1],
            pos[2],
            hpr[0],
            hpr[1],
            hpr[2]])

    
    def handleBattleBlockerCollision(self):
        self._DistributedFactorySuit__handleToonCollision(None)

    
    def _DistributedFactorySuit__handleToonCollision(self, collEntry):
        if not (base.localAvatar.wantBattles):
            return None
        
        toonId = base.localAvatar.getDoId()
        self.notify.debug('Distributed suit %d: requesting a Battle with toon: %d' % (self.doId, toonId))
        self.d_requestBattle(self.getPos(), self.getHpr())
        self.setState('WaitForBattle')
        return None

    
    def setPath(self):
        self.notify.debug('setPath %s' % self.doId)
        if self.pathEntId != None:
            parent = self.factory.entities.get(self.spec['parentEntId'])
            self.path = self.factory.entities.get(self.pathEntId)
            self.idealPathNode = self.path.attachNewNode('idealPath')
            self.reparentTo(self.idealPathNode)
            self.setPos(0, 0, 0)
            self.path.reparentTo(parent)
            self.walkTrack = self.path.makePathTrack(self.idealPathNode, self.velocity, self.uniqueName('suitWalk'))
        
        self.setState('Walk')

    
    def initializeBodyCollisions(self, collIdStr):
        DistributedSuitBase.DistributedSuitBase.initializeBodyCollisions(self, collIdStr)
        self.sSphere = CollisionSphere(0.0, 0.0, 0.0, 15)
        self.sSphereNode = CollisionNode(self.uniqueName('toonSphere'))
        self.sSphereNode.addSolid(self.sSphere)
        self.sSphereNodePath = self.attachNewNode(self.sSphereNode)
        self.sSphereNodePath.hide()
        self.sSphereBitMask = ToontownGlobals.WallBitmask
        self.sSphereNode.setCollideMask(self.sSphereBitMask)
        self.sSphere.setTangible(0)

    
    def enableBattleDetect(self, name, handler):
        DistributedSuitBase.DistributedSuitBase.enableBattleDetect(self, name, handler)
        self.lookForToon(1)

    
    def disableBattleDetect(self):
        DistributedSuitBase.DistributedSuitBase.disableBattleDetect(self)
        self.lookForToon(0)

    
    def subclassManagesParent(self):
        return 1

    
    def enterWalk(self, ts = 0):
        self.enableBattleDetect('walk', self._DistributedFactorySuit__handleToonCollision)
        if self.path:
            if self.walkTrack:
                self.walkTrack.loop()
                self.walkTrack.pause()
                if self.paused:
                    self.walkTrack.setT(self.pauseTime)
                else:
                    self.walkTrack.setT(ts)
                self.walkTrack.resume()
            
            self.loop('walk', 0)
            self.paused = 0
        else:
            self.loop('neutral', 0)

    
    def exitWalk(self):
        self.disableBattleDetect()
        if self.walkTrack:
            self.pauseTime = self.walkTrack.pause()
            self.paused = 1
        
        return None

    
    def lookForToon(self, on = 1):
        if self.behavior == 'chase':
            if on:
                self.accept(self.uniqueName('entertoonSphere'), self._DistributedFactorySuit__handleToonAlert)
            else:
                self.ignore(self.uniqueName('entertoonSphere'))
        

    
    def _DistributedFactorySuit__handleToonAlert(self, collEntry):
        self.notify.debug('%s: ahah!  i saw you' % self.doId)
        toonZ = base.localAvatar.getZ(render)
        suitZ = self.getZ(render)
        dZ = abs(toonZ - suitZ)
        if dZ < 8.0:
            self.sendUpdate('setAlert', [
                base.localAvatar.doId])
        

    
    def resumePath(self, state):
        self.setState('Walk')

    
    def enterChase(self):
        self.enableBattleDetect('walk', self._DistributedFactorySuit__handleToonCollision)
        self.startChaseTime = globalClock.getFrameTime()
        self.startCheckStrayTask(1)
        self.startChaseTask()

    
    def exitChase(self):
        self.disableBattleDetect()
        taskMgr.remove(self.taskName('chaseTask'))
        if self.chaseTrack:
            self.chaseTrack.pause()
            del self.chaseTrack
            self.chaseTrack = None
        
        self.chasing = 0
        self.startCheckStrayTask(0)

    
    def setConfrontToon(self, avId):
        self.chasing = avId
        self.setState('Chase')

    
    def startChaseTask(self, delay = 0):
        taskMgr.remove(self.taskName('chaseTask'))
        taskMgr.doMethodLater(delay, self.chaseTask, self.taskName('chaseTask'))

    
    def chaseTask(self, task):
        if not (self.chasing):
            return Task.done
        
        av = base.cr.doId2do.get(self.chasing, None)
        if not av:
            self.notify.warning("avatar %s isn't here to chase" % self.chasing)
            return Task.done
        
        if globalClock.getFrameTime() - self.startChaseTime > 3.0:
            self.setReturn()
            return Task.done
        
        toonPos = av.getPos(self.getParent())
        suitPos = self.getPos()
        distance = Vec3(suitPos - toonPos).length()
        if self.chaseTrack:
            self.chaseTrack.pause()
            del self.chaseTrack
            self.chaseTrack = None
        
        import random
        rand1 = 0.5
        rand2 = 0.5
        rand3 = 0.5
        targetPos = Vec3(toonPos[0] + 4.0 * (rand1 - 0.5), toonPos[1] + 4.0 * (rand2 - 0.5), suitPos[2])
        track = Sequence(Func(self.headsUp, targetPos[0], targetPos[1], targetPos[2]), Func(self.loop, 'walk', 0))
        chaseSpeed = 4.0
        duration = distance / chaseSpeed
        track.extend([
            LerpPosInterval(self, duration = duration, pos = Point3(targetPos), startPos = Point3(suitPos))])
        self.chaseTrack = track
        self.chaseTrack.start()
        self.startChaseTask(1.0)

    
    def startCheckStrayTask(self, on = 1):
        taskMgr.remove(self.taskName('checkStray'))
        if on:
            taskMgr.add(self.checkStrayTask, self.taskName('checkStray'))
        

    
    def checkStrayTask(self, task):
        curPos = self.getPos()
        distance = Vec3(curPos - self.originalPos).length()
        if distance > 10.0:
            self.sendUpdate('setStrayed', [])
        

    
    def enterReturn(self):
        self.enableBattleDetect('walk', self._DistributedFactorySuit__handleToonCollision)
        self.lookForToon(0)
        self.startReturnTask()

    
    def exitReturn(self):
        self.disableBattleDetect()
        taskMgr.remove(self.taskName('checkStray'))
        taskMgr.remove(self.taskName('returnTask'))
        if self.returnTrack:
            self.returnTrack.pause()
            self.returnTrack = None
        

    
    def setReturn(self):
        self.setState('Return')

    
    def startReturnTask(self, delay = 0):
        taskMgr.remove(self.taskName('returnTask'))
        taskMgr.doMethodLater(delay, self.returnTask, self.taskName('returnTask'))

    
    def returnTask(self, task):
        self.factory.requestReparent(self, self.spec['parentEntId'])
        if self.returnTrack:
            self.returnTrack.pause()
            self.returnTrack = None
        
        if self.path:
            targetPos = VBase3(0, 0, 0)
        else:
            targetPos = self.originalPos
        track = Sequence(Func(self.headsUp, targetPos[0], targetPos[1], targetPos[2]), Func(self.loop, 'walk', 0))
        curPos = self.getPos()
        distance = Vec3(curPos - targetPos).length()
        duration = distance / 3.0
        track.append(LerpPosInterval(self, duration = duration, pos = Point3(targetPos), startPos = Point3(curPos)))
        track.append(Func(self.returnDone))
        self.returnTrack = track
        self.returnTrack.start()

    
    def returnDone(self):
        self.setHpr(self.spec['h'], 0, 0)
        self.setState('Walk')
        if not (self.path):
            self.loop('neutral')
        

    
    def setActive(self, active):
        if active:
            self.setState('Walk')
        else:
            self.setState('Off')


