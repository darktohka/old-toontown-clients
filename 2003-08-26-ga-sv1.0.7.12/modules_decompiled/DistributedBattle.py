# File: D (Python 2.2)

from PandaModules import *
from IntervalGlobal import *
from BattleBase import *
import ToontownGlobals
import ToontownBattleGlobals
import DistributedBattleBase
import DirectNotifyGlobal
import MovieUtil
import Suit
import Actor
import Emote
import SuitBattleGlobals
import DelayDelete
import whrandom

class DistributedBattle(DistributedBattleBase.DistributedBattleBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBattle')
    camFOFov = ToontownBattleGlobals.BattleCamFaceOffFov
    camFOPos = ToontownBattleGlobals.BattleCamFaceOffPos
    
    def __init__(self, cr):
        townBattle = cr.playGame.hood.loader.townBattle
        DistributedBattleBase.DistributedBattleBase.__init__(self, cr, townBattle)
        self._DistributedBattle__setupCollisions(self.uniqueBattleName('battle-collide'))

    
    def generate(self):
        DistributedBattleBase.DistributedBattleBase.generate(self)

    
    def disable(self):
        DistributedBattleBase.DistributedBattleBase.disable(self)

    
    def delete(self):
        DistributedBattleBase.DistributedBattleBase.delete(self)
        self._DistributedBattle__removeCollisionData()

    
    def setPosition(self, x, y, z):
        self.notify.debug('setPosition() - %d %d %d' % (x, y, z))
        pos = Point3(x, y, z)
        self.setPos(pos)

    
    def setInitialSuitPos(self, x, y, z):
        self.initialSuitPos = Point3(x, y, z)
        self.headsUp(self.initialSuitPos)

    
    def setMembers(self, suits, suitsJoining, suitsPending, suitsActive, suitsLured, suitTraps, toons, toonsJoining, toonsPending, toonsActive, toonsRunning, timestamp):
        oldtoons = DistributedBattleBase.DistributedBattleBase.setMembers(self, suits, suitsJoining, suitsPending, suitsActive, suitsLured, suitTraps, toons, toonsJoining, toonsPending, toonsActive, toonsRunning, timestamp)
        if len(self.toons) == 4 and len(oldtoons) < 4:
            self.notify.debug('setMembers() - battle is now full of toons')
            self._DistributedBattle__closeBattleCollision()
        elif len(self.toons) < 4 and len(oldtoons) == 4:
            self._DistributedBattle__openBattleCollision()
        

    
    def _DistributedBattle__setupCollisions(self, name):
        self.cSphere = CollisionSphere(0.0, 0.0, 0.0, 9.0)
        self.cSphereNode = CollisionNode(name)
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.reparentTo(hidden)
        self.cSphereNodePath.hide()
        self.cSphereBitMask = ToontownGlobals.WallBitmask
        self.cSphereNode.setCollideMask(self.cSphereBitMask)
        self.cSphere.setTangible(0)

    
    def _DistributedBattle__removeCollisionData(self):
        del self.cSphere
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath
        del self.cSphereNode
        self.cSphereBitMask = None

    
    def _DistributedBattle__enableCollision(self):
        self.cSphereNodePath.reparentTo(self)
        if len(self.toons) < 4:
            self.accept('enter' + self.cSphereNode.getName(), self._DistributedBattle__handleLocalToonCollision)
        

    
    def _DistributedBattle__handleLocalToonCollision(self, collEntry):
        self.notify.debug('localToonCollision')
        toonbase.tcr.playGame.getPlace().setState('WaitForBattle')
        toon = toonbase.localToon
        self.d_toonRequestJoin(toon.doId, toon.getPos(self))
        toonbase.localToon.preBattleHpr = toonbase.localToon.getHpr(render)
        self.localToonFsm.request('WaitForServer')

    
    def denyLocalToonJoin(self):
        self.notify.debug('denyLocalToonJoin()')
        toonbase.tcr.playGame.getPlace().setState('walk')
        self.localToonFsm.request('NoLocalToon')

    
    def _DistributedBattle__disableCollision(self):
        self.ignore('enter' + self.cSphereNode.getName())
        self.cSphereNodePath.reparentTo(hidden)

    
    def _DistributedBattle__openBattleCollision(self):
        self.cSphere.setTangible(0)
        if not self.hasLocalToon():
            self._DistributedBattle__enableCollision()
        

    
    def _DistributedBattle__closeBattleCollision(self):
        self.cSphere.setTangible(1)
        self.ignore('enter' + self.cSphereNode.getName())

    
    def _DistributedBattle__faceOff(self, ts, name, callback):
        if len(self.suits) == 0:
            self.notify.warning('__faceOff(): no suits.')
            return None
        
        if len(self.toons) == 0:
            self.notify.warning('__faceOff(): no toons.')
            return None
        
        suit = self.suits[0]
        point = self.suitPoints[0][0]
        suitPos = point[0]
        suitHpr = VBase3(point[1], 0.0, 0.0)
        toon = self.toons[0]
        point = self.toonPoints[0][0]
        toonPos = point[0]
        toonHpr = VBase3(point[1], 0.0, 0.0)
        suit.setState('Battle')
        suitTrack = Sequence()
        toonTrack = Sequence()
        camTrack = Sequence()
        suitTrack.append(Func(suit.loop, 'neutral'))
        suitTrack.append(Func(suit.headsUp, toon.getPos()))
        taunt = SuitBattleGlobals.getFaceoffTaunt(suit.getStyleName(), suit.doId)
        suitTrack.append(Func(suit.setChatAbsolute, taunt, CFSpeech | CFTimeout))
        toonTrack.append(Func(toon.loop, 'neutral'))
        toonTrack.append(Func(toon.headsUp, suit.getPos()))
        
        def setCamFov(fov):
            base.camLens.setFov(fov)

        camTrack.append(Func(camera.wrtReparentTo, suit))
        camTrack.append(Func(setCamFov, self.camFOFov))
        suitHeight = suit.getHeight()
        suitOffsetPnt = Point3(0, 0, suitHeight)
        MidTauntCamHeight = suitHeight * 0.66000000000000003
        MidTauntCamHeightLim = suitHeight - 1.8
        if MidTauntCamHeight < MidTauntCamHeightLim:
            MidTauntCamHeight = MidTauntCamHeightLim
        
        TauntCamY = 16
        TauntCamX = whrandom.choice((-5, 5))
        TauntCamHeight = whrandom.choice((MidTauntCamHeight, 1, 11))
        camTrack.append(Func(camera.setPos, TauntCamX, TauntCamY, TauntCamHeight))
        camTrack.append(Func(camera.lookAt, suit, suitOffsetPnt))
        delay = FACEOFF_TAUNT_T
        camTrack.append(Wait(delay))
        suitTrack.append(Wait(delay))
        toonTrack.append(Wait(delay))
        suitTrack.append(Func(suit.headsUp, self, suitPos))
        suitTrack.append(Func(suit.clearChat))
        toonTrack.append(Func(toon.headsUp, self, toonPos))
        faceoffTime = self.calcFaceoffTime(self.getPos(), self.initialSuitPos)
        faceoffTime = max(faceoffTime, BATTLE_SMALL_VALUE)
        suitTrack.append(Func(suit.loop, 'walk'))
        suitTrack.append(LerpPosInterval(suit, faceoffTime, suitPos, other = self))
        suitTrack.append(Func(suit.loop, 'neutral'))
        suitTrack.append(Func(suit.setHpr, self, suitHpr))
        toonTrack.append(Func(toon.loop, 'run'))
        toonTrack.append(LerpPosInterval(toon, faceoffTime, toonPos, other = self))
        toonTrack.append(Func(toon.loop, 'neutral'))
        toonTrack.append(Func(toon.setHpr, self, toonHpr))
        camTrack.append(Func(setCamFov, self.camFov))
        camTrack.append(Func(camera.wrtReparentTo, self))
        camTrack.append(Func(camera.setPos, self.camFOPos))
        camTrack.append(Func(camera.lookAt, suit.getPos(self)))
        camTrack.append(Wait(faceoffTime))
        if toonbase.localToon == toon:
            soundTrack = Sequence(Wait(delay), SoundInterval(toonbase.localToon.soundRun, loop = 1, duration = faceoffTime, node = toonbase.localToon))
        else:
            soundTrack = Wait(delay + faceoffTime)
        mtrack = Parallel(suitTrack, toonTrack, soundTrack)
        done = Func(callback)
        track = Sequence(mtrack, done, name = name)
        track.delayDeletes = [
            DelayDelete.DelayDelete(toon),
            DelayDelete.DelayDelete(suit)]
        track.start(ts)
        self.activeIntervals[name] = track
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
            camTrack.start(ts)
        

    
    def enterFaceOff(self, ts):
        self.notify.debug('enterFaceOff()')
        self.delayDeleteMembers()
        if len(self.toons) > 0 and toonbase.localToon == self.toons[0]:
            Emote.DisableAll(self.toons[0], 'dbattle, enterFaceOff')
        
        self._DistributedBattle__faceOff(ts, self.faceOffName, self._DistributedBattle__handleFaceOffDone)
        return None

    
    def _DistributedBattle__handleFaceOffDone(self):
        self.notify.debug('FaceOff done')
        if len(self.toons) > 0 and toonbase.localToon == self.toons[0]:
            self.d_faceOffDone(toonbase.localToon.doId)
        

    
    def exitFaceOff(self):
        self.notify.debug('exitFaceOff()')
        if len(self.toons) > 0 and toonbase.localToon == self.toons[0]:
            Emote.ReleaseAll(self.toons[0], 'dbattle exitFaceOff')
        
        self.membersKeep = None
        self.finishInterval(self.faceOffName)
        return None

    
    def enterReward(self, ts):
        self.notify.debug('enterReward()')
        self._DistributedBattle__disableCollision()
        self.delayDeleteMembers()
        for toon in self.toons:
            Emote.DisableAll(toon, 'dbattle, enterReward')
        
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
            if self.localToonActive() == 0:
                self.removeInactiveLocalToon(toonbase.localToon)
            
        
        for toon in self.toons:
            toon.startSmooth()
        
        self.accept('resumeAfterReward', self.handleResumeAfterReward)
        self.playReward(ts)
        return None

    
    def playReward(self, ts):
        self.movie.playReward(ts, self.uniqueName('reward'), self.handleRewardDone)

    
    def handleRewardDone(self):
        self.notify.debug('Reward done')
        if self.hasLocalToon():
            self.d_rewardDone(toonbase.localToon.doId)
        
        self.movie.resetReward()
        messenger.send('resumeAfterReward')

    
    def handleResumeAfterReward(self):
        self.fsm.request('Resume')

    
    def exitReward(self):
        self.notify.debug('exitReward()')
        self.ignore('resumeAfterReward')
        self.membersKeep = None
        self.movie.resetReward(finish = 1)
        NametagGlobals.setMasterArrowsOn(1)
        for toon in self.toons:
            Emote.ReleaseAll(toon, 'dbattle exitReward')
        
        return None

    
    def enterResume(self, ts = 0):
        self.notify.debug('enterResume()')
        if self.hasLocalToon():
            self.removeLocalToon()
        
        return None

    
    def exitResume(self):
        return None

    
    def enterNoLocalToon(self):
        self.notify.debug('enterNoLocalToon()')
        self._DistributedBattle__enableCollision()
        return None

    
    def exitNoLocalToon(self):
        self._DistributedBattle__disableCollision()
        return None

    
    def enterWaitForServer(self):
        self.notify.debug('enterWaitForServer()')
        return None

    
    def exitWaitForServer(self):
        return None


