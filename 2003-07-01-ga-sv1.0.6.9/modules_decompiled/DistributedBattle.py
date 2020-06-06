# File: D (Python 2.2)

from PandaModules import *
from IntervalGlobal import *
from BattleBase import *
import ToontownGlobals
import ToontownBattleGlobals
import DistributedBattleBase
import CollisionSphere
import CollisionNode
import DirectNotifyGlobal
import MovieUtil
import Suit
import Actor
import Emote
import SuitBattleGlobals
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
        pos = Point3(x, y, -0.47499999999999998)
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
        self.cSphere = CollisionSphere.CollisionSphere(0.0, 0.0, 0.0, 9.0)
        self.cSphereNode = CollisionNode.CollisionNode(name)
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
        suitIvals = []
        toonIvals = []
        camIvals = []
        suitIvals.append(FunctionInterval(suit.loop, extraArgs = [
            'neutral']))
        suitIvals.append(FunctionInterval(suit.headsUp, extraArgs = [
            toon.getPos()]))
        taunt = SuitBattleGlobals.getFaceoffTaunt(suit.getStyleName(), suit.doId)
        suitIvals.append(FunctionInterval(suit.setChatAbsolute, extraArgs = [
            taunt,
            CFSpeech | CFTimeout]))
        toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
            'neutral']))
        toonIvals.append(FunctionInterval(toon.headsUp, extraArgs = [
            suit.getPos()]))
        
        def setCamFov(fov):
            base.camLens.setFov(fov)

        camIvals.append(FunctionInterval(camera.wrtReparentTo, extraArgs = [
            suit]))
        camIvals.append(FunctionInterval(setCamFov, extraArgs = [
            self.camFOFov]))
        suitHeight = suit.getHeight()
        suitOffsetPnt = Point3(0, 0, suitHeight)
        MidTauntCamHeight = suitHeight * 0.66000000000000003
        MidTauntCamHeightLim = suitHeight - 1.8
        if MidTauntCamHeight < MidTauntCamHeightLim:
            MidTauntCamHeight = MidTauntCamHeightLim
        
        TauntCamY = 16
        TauntCamX = whrandom.choice((-5, 5))
        TauntCamHeight = whrandom.choice((MidTauntCamHeight, 1, 11))
        camIvals.append(FunctionInterval(camera.setPos, extraArgs = [
            TauntCamX,
            TauntCamY,
            TauntCamHeight]))
        camIvals.append(FunctionInterval(camera.lookAt, extraArgs = [
            suit,
            suitOffsetPnt]))
        delay = FACEOFF_TAUNT_T
        camIvals.append(WaitInterval(delay))
        sFaceSpot = FunctionInterval(suit.headsUp, extraArgs = [
            self,
            suitPos])
        suitIvals.append((delay, sFaceSpot))
        suitIvals.append(FunctionInterval(suit.clearChat))
        tFaceSpot = FunctionInterval(toon.headsUp, extraArgs = [
            self,
            toonPos])
        toonIvals.append((delay, tFaceSpot))
        faceoffTime = self.calcFaceoffTime(self.getPos(), self.initialSuitPos)
        fromBattle = Vec3(self.getPos() - self.initialSuitPos)
        distance = fromBattle.length()
        if distance > MAX_EXPECTED_DISTANCE_FROM_BATTLE:
            
            try:
                zoneId = toonbase.tcr.playGame.getPlace().getZoneId()
                zoneStr = str(zoneId)
            except:
                zoneStr = 'Unknown'

            self.notify.warning('WARNING: Possible missing battle cell in zone ' + zoneStr + '!!')
            toonbase.tcr.timeManager.synchronize('Suit is %0.1f ft from battle cell.' % distance)
        
        suitIvals.append(FunctionInterval(suit.loop, extraArgs = [
            'walk']))
        suitIvals.append(LerpPosInterval(suit, faceoffTime, suitPos, other = self))
        suitIvals.append(FunctionInterval(suit.loop, extraArgs = [
            'neutral']))
        suitIvals.append(FunctionInterval(suit.setHpr, extraArgs = [
            self,
            suitHpr]))
        toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
            'run']))
        toonIvals.append(LerpPosInterval(toon, faceoffTime, toonPos, other = self))
        toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
            'neutral']))
        toonIvals.append(FunctionInterval(toon.setHpr, extraArgs = [
            self,
            toonHpr]))
        camIvals.append(FunctionInterval(setCamFov, extraArgs = [
            self.camFov]))
        camIvals.append(FunctionInterval(camera.wrtReparentTo, extraArgs = [
            self]))
        camIvals.append(FunctionInterval(camera.setPos, extraArgs = [
            self.camFOPos]))
        camIvals.append(FunctionInterval(camera.lookAt, extraArgs = [
            suit.getPos(self)]))
        camIvals.append(WaitInterval(faceoffTime))
        if toonbase.localToon == toon:
            soundTrack = Track((WaitInterval(delay), SoundInterval(toonbase.localToon.soundRun, loop = 1, duration = faceoffTime, node = toonbase.localToon)))
        else:
            soundTrack = WaitInterval(faceoffTime + delay)
        suitTrack = Track(suitIvals)
        toonTrack = Track(toonIvals)
        camTrack = Track(camIvals)
        mtrack = MultiTrack([
            suitTrack,
            toonTrack,
            soundTrack])
        done = FunctionInterval(callback)
        track = Track([
            mtrack,
            done], name)
        track.start(ts)
        self.activeIntervals[name] = track
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
            camTrack.start(ts)
        

    
    def enterFaceOff(self, ts):
        self.notify.debug('enterFaceOff()')
        self.delayDeleteToons()
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
        
        self.toonsKeep = None
        self.finishInterval(self.faceOffName)
        return None

    
    def enterReward(self, ts):
        self.notify.debug('enterReward()')
        self._DistributedBattle__disableCollision()
        self.delayDeleteToons()
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
        self.toonsKeep = None
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


