# File: D (Python 2.2)

from ShowBaseGlobal import *
from IntervalGlobal import *
from DirectGui import *
import DistributedObject
import DirectNotifyGlobal
import ToontownGlobals
import FishingCodes
import FishPage
import Localizer
import Quests
import Actor
import Rope
import math

class DistributedFishingSpot(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingSpot')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.lastAvId = 0
        self.lastFrame = 0
        self.avId = 0
        self.av = None
        self.placedAvatar = 0
        self.localToonFishing = 0
        self.nodePath = None
        self.collSphere = None
        self.collNode = None
        self.collNodePath = None
        self.protSphere = None
        self.protNode = None
        self.protNodePath = None
        self.track = None
        self.madeGui = 0
        self.castGui = None
        self.reelGui = None
        self.crankGui = None
        self.crankHeld = 0
        self.turnCrankTask = None
        self.itemGui = None
        self.failureGui = None
        self.brokeGui = None
        self.pole = None
        self.poleNode = []
        self.ptop = None
        self.bob = None
        self.bobBobTask = None
        self.splashSound = None
        self.ripples = None
        self.gotBobSpot = 0
        self.bobSpot = None
        self.nibbleStart = 0
        self.targetSpeed = None
        self.netTime = 0.0
        self.netDistance = 0.0
        self.line = None
        self.lineSphere = None
        self.pendingFish = 0

    
    def disable(self):
        self.ignore(self.uniqueName('enterFishingSpotSphere'))
        self.setOccupied(0)
        self.avId = 0
        self._DistributedFishingSpot__hideBob()
        self.nodePath.detachNode()
        self._DistributedFishingSpot__unmakeGui()
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    
    def generateInit(self):
        self.nodePath = NodePath(self.uniqueName('FishingSpot'))
        self.line = Rope.Rope(self.uniqueName('Line'))
        self.line.setColor(1, 1, 1, 0.40000000000000002)
        self.line.setTransparency(1)
        self.lineSphere = BoundingSphere(Point3(-0.59999999999999998, -2, -5), 5.5)
        self.collSphere = CollisionSphere(0, 0, 0, self.getSphereRadius())
        self.collSphere.setTangible(0)
        self.collNode = CollisionNode(self.uniqueName('FishingSpotSphere'))
        self.collNode.setCollideMask(ToontownGlobals.WallBitmask)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.nodePath.attachNewNode(self.collNode)
        self.protSphere = CollisionSphere(0, 0, 0, 1.5)
        self.protNode = CollisionNode(self.uniqueName('ProtectionSphere'))
        self.protNode.setCollideMask(ToontownGlobals.WallBitmask)
        self.protNode.addSolid(self.protSphere)
        self.protNodePath = NodePath(self.protNode)
        self.protNodePath.setScale(1, 1.5, 1.5)
        self.protNodePath.setPos(0, 7, 0)

    
    def generate(self):
        self.nodePath.reparentTo(self.getParentNodePath())
        self.accept(self.uniqueName('enterFishingSpotSphere'), self._DistributedFishingSpot__handleEnterSphere)

    
    def _DistributedFishingSpot__handleEnterSphere(self, collEntry):
        if toonbase.localToon.doId == self.lastAvId and globalClock.getFrameCount() <= self.lastFrame + 1:
            self.notify.info('Ignoring duplicate entry for avatar.')
            return None
        
        if toonbase.localToon.hp > 0:
            self.d_requestEnter()
        

    
    def d_requestEnter(self):
        self.sendUpdate('requestEnter', [])

    
    def d_requestExit(self):
        self.sendUpdate('requestExit', [])

    
    def d_doCast(self):
        self.sendUpdate('doCast', [])

    
    def d_doAutoReel(self):
        self.sendUpdate('doAutoReel', [])

    
    def d_doReel(self, speed, netTime, netDistance):
        self.sendUpdate('doReel', [
            speed,
            netTime,
            netDistance])

    
    def getSphereRadius(self):
        return 1.5

    
    def getParentNodePath(self):
        return render

    
    def setPosHpr(self, x, y, z, h, p, r):
        self.nodePath.setPosHpr(x, y, z, h, p, r)

    
    def setOccupied(self, avId):
        if self.track != None:
            if self.track.isPlaying():
                self.track.setFinalT()
            
            self.track = None
        
        if self.av != None:
            if not self.av.isEmpty():
                self.av.disableBlend()
                self.av.setPlayRate(1.0, 'cast')
                self._DistributedFishingSpot__dropPole()
                self.av.loop('neutral')
                self.av.setParent(ToontownGlobals.SPRender)
                self.av.startSmooth()
            
            self.ignore(self.av.uniqueName('disable'))
            self._DistributedFishingSpot__hideBob()
            self.av.fishingSpot = None
            self.av = None
            self.placedAvatar = 0
        
        self._DistributedFishingSpot__hideLine()
        wasLocalToon = self.localToonFishing
        self.lastAvId = self.avId
        self.lastFrame = globalClock.getFrameCount()
        self.avId = avId
        self.localToonFishing = 0
        if self.avId == 0:
            self.collSphere.setTangible(0)
            self.protNodePath.detachNode()
        else:
            self.collSphere.setTangible(1)
            self.protNodePath.reparentTo(self.nodePath)
            self._DistributedFishingSpot__loadStuff()
            if self.avId == toonbase.localToon.doId:
                toonbase.tcr.playGame.getPlace().setState('fishing')
                toonbase.setCellsAvailable([
                    toonbase.bottomCells[1],
                    toonbase.bottomCells[2]], 0)
                self.localToonFishing = 1
            
            if self.cr.doId2do.has_key(self.avId):
                self.av = self.cr.doId2do[self.avId]
                self.placedAvatar = 0
                self.acceptOnce(self.av.uniqueName('disable'), self._DistributedFishingSpot__avatarGone)
                self.av.stopSmooth()
                self.av.wrtReparentTo(self.nodePath)
                self.av.fishingSpot = self
                self.av.setAnimState('neutral', 1.0)
                self._DistributedFishingSpot__setupNeutralBlend()
            else:
                self.notify.warning('Unknown avatar %d in fishing spot %d' % (self.avId, self.doId))
        if wasLocalToon and not (self.localToonFishing):
            self._DistributedFishingSpot__hideGui()
            toonbase.setCellsAvailable([
                toonbase.bottomCells[1],
                toonbase.bottomCells[2]], 1)
            place = toonbase.tcr.playGame.getPlace()
            if place:
                place.setState('walk')
            
        
        return None

    
    def _DistributedFishingSpot__avatarGone(self):
        self.setOccupied(0)

    
    def _DistributedFishingSpot__setupNeutralBlend(self):
        self.av.stop()
        self.av.loop('neutral')
        self.av.enableBlend()
        self.av.pose('cast', 0)
        self.av.setControlEffect('neutral', 0.20000000000000001)
        self.av.setControlEffect('cast', 0.80000000000000004)

    
    def setTargetSpeed(self, speed):
        self.targetSpeed = speed
        self.speedGauge.show()
        self._DistributedFishingSpot__updateSpeedGauge()

    
    def setMovie(self, mode, code, item, speed):
        if self.track != None:
            if self.track.isPlaying():
                self.track.setFinalT()
            
            self.track = None
        
        if self.av == None:
            return None
        
        self._DistributedFishingSpot__hideLine()
        if mode == FishingCodes.NoMovie:
            pass
        1
        if mode == FishingCodes.EnterMovie:
            trackList = []
            self.av.stopLookAround()
            if self.localToonFishing:
                trackList.append(LerpPosHprInterval(node = camera, other = self.av, duration = 1.5, pos = Point3(14, -7.4000000000000004, 7.2999999999999998), hpr = VBase3(45, -12, 0), blendType = 'easeInOut'))
            
            self.av.disableBlend()
            self.av.setPlayRate(1.0, 'walk')
            self.av.loop('walk')
            toonTrack = Sequence(LerpPosHprInterval(self.av, 1.5, Point3(0, 0, 0), Point3(0, 0, 0)), Func(self._DistributedFishingSpot__setupNeutralBlend), Func(self._DistributedFishingSpot__holdPole), Parallel(ActorInterval(self.av, 'cast', playRate = 0.5, duration = 27.0 / 12.0), ActorInterval(self.pole, 'cast', playRate = 0.5, duration = 27.0 / 12.0), LerpScaleInterval(self.pole, duration = 2.0, scale = 1.0, startScale = 0.01)))
            if self.localToonFishing:
                toonTrack.append(Func(self._DistributedFishingSpot__showCastGui))
            
            trackList.append(toonTrack)
            self.track = Parallel(trackList)
            self.track.start()
        elif mode == FishingCodes.ExitMovie:
            if self.localToonFishing:
                self._DistributedFishingSpot__hideGui()
                if hasattr(self.av, 'fishPage'):
                    if self.av.fishPage.state == FishPage.FP_RELEASE:
                        self.av.fishPage.forceReleaseFish()
                    
                
            
            self.av.stopLookAround()
            self.av.startLookAround()
            self._DistributedFishingSpot__placeAvatar()
            self._DistributedFishingSpot__hideLine()
            self._DistributedFishingSpot__hideBob()
            self.track = Sequence(Parallel(ActorInterval(self.av, 'cast', duration = 1.0, startTime = 1.0, endTime = 0.0), ActorInterval(self.pole, 'cast', duration = 1.0, startTime = 1.0, endTime = 0.0), LerpScaleInterval(self.pole, duration = 0.5, scale = 0.01, startScale = 1.0)), Func(self._DistributedFishingSpot__dropPole))
            self.track.start()
        elif mode == FishingCodes.CastMovie:
            self.av.stopLookAround()
            self.av.startLookAround()
            self._DistributedFishingSpot__placeAvatar()
            self._DistributedFishingSpot__getBobSpot()
            self.track = Sequence(Parallel(ActorInterval(self.av, 'cast', duration = 2.0, startTime = 1.0), ActorInterval(self.pole, 'cast', duration = 2.0, startTime = 1.0), Sequence(Wait(1.3), Func(self._DistributedFishingSpot__showBobCast), Func(self._DistributedFishingSpot__showLineWaiting), LerpPosInterval(self.bob, 0.20000000000000001, self.bobSpot), Func(self._DistributedFishingSpot__showBob), SoundInterval(self.splashSound))))
            if self.localToonFishing:
                self.track.append(Func(self._DistributedFishingSpot__showReelGui))
            
            self.track.start()
        elif mode == FishingCodes.NibbleMovie:
            self._DistributedFishingSpot__placeAvatar()
            self.av.pose('cast', 71)
            self.pole.pose('cast', 71)
            self._DistributedFishingSpot__showLineWaiting()
            self._DistributedFishingSpot__nibbleBob()
        elif mode == FishingCodes.BeginReelMovie:
            self.av.stopLookAround()
            self._DistributedFishingSpot__placeAvatar()
            self._DistributedFishingSpot__hideBob()
            self._DistributedFishingSpot__showLineReelTaught()
            self.av.setPlayRate(speed, 'cast')
            self.pole.setPlayRate(speed, 'cast')
            self.track = Sequence(Parallel(ActorInterval(self.av, 'cast', duration = 1.0 / speed, startTime = 3.0 / speed, playRate = speed), ActorInterval(self.pole, 'cast', duration = 1.0 / speed, startTime = 3.0 / speed, playRate = speed)), Func(self.av.loop, 'cast', 1, None, 96, 126), Func(self.pole.loop, 'cast', 1, None, 96, 126))
            self.track.start()
        elif mode == FishingCodes.ContinueReelMovie:
            self.av.stopLookAround()
            self._DistributedFishingSpot__showLineReelTaught()
            if not (self.placedAvatar):
                self._DistributedFishingSpot__placeAvatar()
                self.av.pose('cast', 88)
                self.pole.pose('cast', 88)
            
            if speed < 0:
                self.av.loop('cast', restart = 0, fromFrame = 126, toFrame = 88)
                self.pole.loop('cast', restart = 0, fromFrame = 126, toFrame = 88)
            else:
                self.av.loop('cast', restart = 0, fromFrame = 88, toFrame = 126)
                self.pole.loop('cast', restart = 0, fromFrame = 88, toFrame = 126)
            self.av.setPlayRate(speed, 'cast')
            self.pole.setPlayRate(speed, 'cast')
        elif mode == FishingCodes.PullInMovie:
            self.av.startLookAround()
            self._DistributedFishingSpot__placeAvatar()
            self.av.pose('cast', 26)
            self.pole.pose('cast', 26)
            if self.localToonFishing:
                self._DistributedFishingSpot__showCastGui()
                if code == FishingCodes.QuestItem:
                    self._DistributedFishingSpot__showQuestItem(item)
                elif code == FishingCodes.FishItem:
                    self._DistributedFishingSpot__showFishItem(item)
                elif code == FishingCodes.OverLimitFishItem:
                    self._DistributedFishingSpot__hideGui()
                    self.b_fishReleaseQuery(item)
                else:
                    self._DistributedFishingSpot__showFailureReason(code)
            
        
        return None

    
    def getStareAtNodeAndOffset(self):
        return (self.nodePath, Point3())

    
    def _DistributedFishingSpot__loadStuff(self):
        if self.pole == None:
            self.pole = Actor.Actor()
            self.pole.loadModel('phase_4/models/props/fishing-pole-mod')
            self.pole.loadAnims({
                'cast': 'phase_4/models/props/fishing-pole-chan' })
            self.pole.pose('cast', 0)
            self.ptop = self.pole.find('**/joint_attachBill')
        
        if self.bob == None:
            import Ripples
            self.bob = loader.loadModelCopy('phase_4/models/props/fishing_bob')
            self.ripples = Ripples.Ripples(self.nodePath)
            self.ripples.hide()
        
        if self.splashSound == None:
            self.splashSound = base.loadSfx('phase_4/audio/sfx/TT_splash1.mp3')
        

    
    def _DistributedFishingSpot__placeAvatar(self):
        if not (self.placedAvatar):
            self.placedAvatar = 1
            self._DistributedFishingSpot__holdPole()
            self._DistributedFishingSpot__setupNeutralBlend()
            self.av.setPosHpr(0, 0, 0, 0, 0, 0)
        

    
    def _DistributedFishingSpot__holdPole(self):
        if self.poleNode != []:
            self._DistributedFishingSpot__dropPole()
        
        np = NodePath('pole-holder')
        hands = self.av.getRightHands()
        for h in hands:
            self.poleNode.append(np.instanceTo(h))
        
        self.pole.reparentTo(self.poleNode[0])

    
    def _DistributedFishingSpot__dropPole(self):
        self._DistributedFishingSpot__hideBob()
        self._DistributedFishingSpot__hideLine()
        if self.pole != None:
            self.pole.clearMat()
            self.pole.detachNode()
        
        for pn in self.poleNode:
            pn.removeNode()
        
        self.poleNode = []

    
    def _DistributedFishingSpot__showLineWaiting(self):
        self.line.setup(4, ((None, (0, 0, 0)), (None, (0, -2, -4)), (self.bob, (0, -1, 0)), (self.bob, (0, 0, 0))))
        self.line.ropeNode.setBound(self.lineSphere)
        self.line.reparentTo(self.ptop)

    
    def _DistributedFishingSpot__showLineReelTaught(self):
        self._DistributedFishingSpot__getBobSpot()
        self.line.setup(2, ((None, (0, 0, 0)), (self.nodePath, self.bobSpot)))
        self.line.ropeNode.setBound(self.lineSphere)
        self.line.reparentTo(self.ptop)

    
    def _DistributedFishingSpot__showLineReelSlack(self):
        self._DistributedFishingSpot__getBobSpot()
        self.line.setup(3, ((None, (0, 0, 0)), (None, (0, -2, -4)), (self.nodePath, self.bobSpot)))
        self.line.ropeNode.setBound(self.lineSphere)
        self.line.reparentTo(self.ptop)

    
    def _DistributedFishingSpot__hideLine(self):
        self.line.detachNode()

    
    def _DistributedFishingSpot__showBobCast(self):
        self._DistributedFishingSpot__hideBob()
        self.bob.reparentTo(self.nodePath)
        self.av.update(0)
        self.bob.setPos(self.ptop, 0, 0, 0)

    
    def _DistributedFishingSpot__showBob(self):
        self._DistributedFishingSpot__hideBob()
        self._DistributedFishingSpot__getBobSpot()
        self.bob.reparentTo(self.nodePath)
        self.bob.setPos(self.bobSpot)
        self.ripples.reparentTo(self.nodePath)
        self.ripples.setPos(self.bobSpot)
        self.ripples.play(0.75)
        self.bobBobTask = taskMgr.add(self._DistributedFishingSpot__doBobBob, self.taskName('bob'))

    
    def _DistributedFishingSpot__nibbleBob(self):
        self._DistributedFishingSpot__hideBob()
        self._DistributedFishingSpot__getBobSpot()
        self.bob.reparentTo(self.nodePath)
        self.bob.setPos(self.bobSpot)
        self.ripples.reparentTo(self.nodePath)
        self.ripples.setPos(self.bobSpot)
        self.ripples.play()
        self.nibbleStart = globalClock.getFrameTime()
        self.bobBobTask = taskMgr.add(self._DistributedFishingSpot__doNibbleBob, self.taskName('bob'))

    
    def _DistributedFishingSpot__hideBob(self):
        if self.bob != None:
            self.bob.detachNode()
        
        if self.bobBobTask != None:
            taskMgr.remove(self.bobBobTask)
            self.bobBobTask = None
        
        if self.ripples != None:
            self.ripples.stop()
            self.ripples.detachNode()
        

    
    def _DistributedFishingSpot__doBobBob(self, task):
        now = globalClock.getFrameTime()
        z = math.sin(now) * 0.050000000000000003
        self.bob.setZ(self.bobSpot[2] + z)
        return Task.cont

    
    def _DistributedFishingSpot__doNibbleBob(self, task):
        now = globalClock.getFrameTime()
        elapsed = now - self.nibbleStart
        if elapsed > FishingCodes.NibbleTime:
            self._DistributedFishingSpot__showBob()
            return Task.done
        
        x = (elapsed / FishingCodes.NibbleTime + 1.0) * 0.5
        y = math.sin(x * math.pi)
        amplitude = y * y * y * 0.20000000000000001
        nibbleEffect = math.sin(now * 12) * amplitude
        z = math.sin(now) * 0.050000000000000003 + nibbleEffect
        self.bob.setZ(self.bobSpot[2] + z)
        return Task.cont

    
    def _DistributedFishingSpot__userExit(self):
        self._DistributedFishingSpot__hideGui()
        self.d_requestExit()

    
    def _DistributedFishingSpot__userReel(self):
        self._DistributedFishingSpot__hideGui()
        self.d_doAutoReel()

    
    def _DistributedFishingSpot__userCast(self):
        self.itemGui.detachNode()
        self.failureGui.detachNode()
        if self.av.getMoney() > 0:
            self._DistributedFishingSpot__hideCastButtons()
            self.jar['text'] = str(max(self.av.getMoney() - 1, 0))
            self.d_doCast()
        else:
            self._DistributedFishingSpot__showBroke()

    
    def _DistributedFishingSpot__showCastGui(self):
        self._DistributedFishingSpot__hideGui()
        self._DistributedFishingSpot__makeGui()
        self.castButton.show()
        self.exitButton.show()
        self.castGui.reparentTo(aspect2d)
        self.castButton['state'] = NORMAL
        self.jar['text'] = str(self.av.getMoney())

    
    def _DistributedFishingSpot__hideCastButtons(self):
        self.castButton.hide()
        self.exitButton.hide()

    
    def _DistributedFishingSpot__showReelGui(self):
        self._DistributedFishingSpot__hideGui()
        self._DistributedFishingSpot__makeGui()
        self.reelGui.reparentTo(aspect2d)
        self.crankGui.show()
        self.speedGauge.hide()
        self.crankHandle.bind(B1PRESS, self._DistributedFishingSpot__clickCrank)
        self.crankHandle.bind(B1RELEASE, self._DistributedFishingSpot__releaseCrank)
        self.reelButton.hide()
        self.netTime = 0.0
        self.netDistance = 0.0
        self.targetSpeed = None

    
    def _DistributedFishingSpot__clickCrank(self, param):
        if self.crankHeld:
            self._DistributedFishingSpot__releaseCrank(param)
        
        self.reelButton.hide()
        self.crankHeld = 1
        self.d_doReel(1.0, self.netTime, self.netDistance)
        mpos = param.getMouse()
        angle = self._DistributedFishingSpot__getMouseAngleToCrank(mpos[0], mpos[1])
        self.crankR = self.crankHandle.getR() - angle
        self.crankAngle = angle
        self.crankDelta = 0
        self.crankTime = globalClock.getFrameTime()
        if self.turnCrankTask == None:
            self.turnCrankTask = taskMgr.add(self._DistributedFishingSpot__turnCrank, self.taskName('turnCrank'))
        

    
    def _DistributedFishingSpot__releaseCrank(self, unused):
        if not (self.crankHeld):
            return None
        
        self.crankHeld = 0
        self._DistributedFishingSpot__updateCrankSpeed(1)

    
    def _DistributedFishingSpot__turnCrank(self, task):
        if self.crankHeld and base.mouseWatcherNode.hasMouse():
            mx = base.mouseWatcherNode.getMouseX()
            my = base.mouseWatcherNode.getMouseY()
            angle = self._DistributedFishingSpot__getMouseAngleToCrank(mx, my)
            self.crankHandle.setR(self.crankR + angle)
            delta = angle - self.crankAngle
            if delta > 180:
                delta = delta - 360
            elif delta < -180:
                delta = delta + 360
            
            self.crankDelta += delta
            self.crankAngle = angle
        
        self._DistributedFishingSpot__updateCrankSpeed(0)
        if self.targetSpeed != None:
            self._DistributedFishingSpot__updateSpeedGauge()
        
        return Task.cont

    
    def _DistributedFishingSpot__updateCrankSpeed(self, forceUpdate):
        now = globalClock.getFrameTime()
        elapsed = now - self.crankTime
        if elapsed != 0 and forceUpdate or elapsed >= FishingCodes.CalcCrankSpeed:
            degreesPerSecond = -(self.crankDelta / elapsed)
            speed = degreesPerSecond / FishingCodes.StandardCrankSpeed
            self.netTime += elapsed
            self.netDistance += speed * elapsed
            self.d_doReel(speed, self.netTime, self.netDistance)
            self.crankTime = now
            self.crankDelta = 0
        

    
    def _DistributedFishingSpot__updateSpeedGauge(self):
        now = globalClock.getFrameTime()
        elapsed = now - self.crankTime
        if elapsed > 0:
            degreesPerSecond = -(self.crankDelta / elapsed)
            speed = degreesPerSecond / FishingCodes.StandardCrankSpeed
            totalTime = self.netTime + elapsed
            totalDistance = self.netDistance + speed * elapsed
        else:
            totalTime = self.netTime
            totalDistance = self.netDistance
        self.tooSlow.hide()
        self.tooFast.hide()
        if totalTime > 0:
            avgSpeed = totalDistance / totalTime
            pctDiff = 100.0 * (avgSpeed - self.targetSpeed) / self.targetSpeed
            self.speedGauge['value'] = pctDiff + 50.0
            if pctDiff >= FishingCodes.ManualReelMatch * 0.80000000000000004:
                self.tooFast.show()
            elif pctDiff <= -(FishingCodes.ManualReelMatch) * 0.80000000000000004:
                self.tooSlow.show()
            
        

    
    def _DistributedFishingSpot__getMouseAngleToCrank(self, x, y):
        p = self.crankGui.getRelativePoint(NodePath(), Point3(x, 0, y))
        angle = math.atan2(p[2], p[0]) * 180.0 / math.pi
        return angle

    
    def _DistributedFishingSpot__showQuestItem(self, itemId):
        self._DistributedFishingSpot__makeGui()
        itemName = Quests.getItemName(itemId)
        self.itemLabel['text'] = itemName
        self.itemGui.reparentTo(aspect2d)

    
    def _DistributedFishingSpot__showFishItem(self, itemId):
        self._DistributedFishingSpot__makeGui()
        itemName = FishingCodes.getFishName(itemId)
        self.itemLabel['text'] = itemName
        self.itemGui.reparentTo(aspect2d)

    
    def _DistributedFishingSpot__showFailureReason(self, code):
        self._DistributedFishingSpot__makeGui()
        reason = ''
        if code == FishingCodes.TooSoon:
            reason = Localizer.FishingFailureTooSoon
        elif code == FishingCodes.TooLate:
            reason = Localizer.FishingFailureTooLate
        elif code == FishingCodes.AutoReel:
            reason = Localizer.FishingFailureAutoReel
        elif code == FishingCodes.TooSlow:
            reason = Localizer.FishingFailureTooSlow
        elif code == FishingCodes.TooFast:
            reason = Localizer.FishingFailureTooFast
        
        self.failureLabel['text'] = reason
        self.failureGui.reparentTo(aspect2d)

    
    def _DistributedFishingSpot__showBroke(self):
        self._DistributedFishingSpot__makeGui()
        self.brokeGui.reparentTo(aspect2d)
        self.castButton['state'] = DISABLED

    
    def _DistributedFishingSpot__hideGui(self):
        if self.madeGui:
            if self.crankHeld:
                self._DistributedFishingSpot__releaseCrank(None)
            
            if self.turnCrankTask != None:
                taskMgr.remove(self.turnCrankTask)
                self.turnCrankTask = None
            
            self.castGui.detachNode()
            self.reelGui.detachNode()
            self.crankHandle.unbind(B1PRESS)
            self.crankHandle.unbind(B1RELEASE)
            self.itemGui.detachNode()
            self.failureGui.detachNode()
            self.brokeGui.detachNode()
        

    
    def _DistributedFishingSpot__makeGui(self):
        if self.madeGui:
            return None
        
        buttonModels = loader.loadModelOnce('phase_3.5/models/gui/inventory_gui')
        upButton = buttonModels.find('**/InventoryButtonUp')
        downButton = buttonModels.find('**/InventoryButtonDown')
        rolloverButton = buttonModels.find('**/InventoryButtonRollover')
        buttonModels.removeNode()
        crankModels = loader.loadModelOnce('phase_4/models/gui/fishing_crank')
        crank = crankModels.find('**/fishing_crank')
        crankArrow = crankModels.find('**/fishing_crank_arrow')
        crankModels.removeNode()
        jarGui = loader.loadModelOnce('phase_3.5/models/gui/jar_gui')
        jarImage = jarGui.find('**/Jar')
        jarGui.removeNode()
        self.castGui = NodePath('castGui')
        self.exitButton = DirectButton(parent = self.castGui, relief = None, text = Localizer.FishingExit, text_fg = (1, 1, 0.65000000000000002, 1), text_pos = (0, -0.23000000000000001), text_scale = 0.80000000000000004, image = (upButton, downButton, rolloverButton), image_color = (1, 0, 0, 1), image_scale = (15, 1, 11), pos = (-0.20000000000000001, 0, -0.80000000000000004), scale = 0.12, command = self._DistributedFishingSpot__userExit)
        self.castButton = DirectButton(parent = self.castGui, relief = None, text = Localizer.FishingCast, text_fg = (1, 1, 0.65000000000000002, 1), text3_fg = (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1), text_pos = (0, -0.23000000000000001), text_scale = 0.80000000000000004, image = (upButton, downButton, rolloverButton), image_color = (1, 0, 0, 1), image3_color = (0.80000000000000004, 0.5, 0.5, 1), image_scale = (15, 1, 11), pos = (-0.20000000000000001, 0, -0.62), scale = 0.12, command = self._DistributedFishingSpot__userCast)
        self.jar = DirectLabel(parent = self.castGui, relief = None, text = str(self.av.getMoney()), text_scale = 0.20000000000000001, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_pos = (0, -0.10000000000000001, 0), text_font = ToontownGlobals.getSignFont(), image = jarImage, pos = (-0.20000000000000001, 0, -0.34999999999999998), scale = 0.65000000000000002)
        self.reelGui = NodePath('reelGui')
        self.reelButton = DirectButton(parent = self.reelGui, relief = None, text = Localizer.FishingAutoReel, text_fg = (1, 1, 0.65000000000000002, 1), text_pos = (0, -0.23000000000000001), text_scale = 0.80000000000000004, image = (upButton, downButton, rolloverButton), image_color = (0, 0.69999999999999996, 0, 1), image_scale = (24, 1, 11), pos = (1.0, 0, -0.29999999999999999), scale = 0.10000000000000001, command = self._DistributedFishingSpot__userReel)
        self.crankGui = self.reelGui.attachNewNode('crankGui')
        arrow1 = crankArrow.copyTo(self.crankGui)
        arrow1.setColor(1, 0, 0, 1)
        arrow1.setPos(0.25, 0, -0.25)
        arrow2 = crankArrow.copyTo(self.crankGui)
        arrow2.setColor(1, 0, 0, 1)
        arrow2.setPos(-0.25, 0, 0.25)
        arrow2.setR(180)
        self.crankGui.setPos(-0.20000000000000001, 0, -0.69999999999999996)
        self.crankGui.setScale(0.5)
        self.crankHandle = DirectFrame(parent = self.crankGui, state = NORMAL, relief = None, image = crank)
        self.speedGauge = DirectWaitBar(parent = self.crankGui, relief = SUNKEN, frameSize = (-0.80000000000000004, 0.80000000000000004, -0.14999999999999999, 0.14999999999999999), borderWidth = (0.02, 0.02), scale = 0.41999999999999998, pos = (0, 0, 0.75), barColor = (0, 0.69999999999999996, 0, 1))
        self.speedGauge.hide()
        self.tooSlow = DirectLabel(parent = self.speedGauge, relief = None, text = Localizer.FishingCrankTooSlow, scale = 0.20000000000000001, pos = (-1, 0, 0.050000000000000003))
        self.tooFast = DirectLabel(parent = self.speedGauge, relief = None, text = Localizer.FishingCrankTooFast, scale = 0.20000000000000001, pos = (1, 0, 0.050000000000000003))
        self.tooSlow.hide()
        self.tooFast.hide()
        self.itemGui = NodePath('itemGui')
        self.itemFrame = DirectFrame(parent = self.itemGui, relief = None, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (1, 1, 0.5), text = Localizer.FishingItemFound, text_pos = (0, 0.080000000000000002), text_scale = 0.080000000000000002, pos = (0, 0, 0.58699999999999997))
        self.itemLabel = DirectLabel(parent = self.itemFrame, text = '', text_scale = 0.059999999999999998, pos = (0, 0, -0.080000000000000002))
        self.failureGui = NodePath('failureGui')
        self.failureFrame = DirectFrame(parent = self.failureGui, relief = None, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (1.2, 1, 0.59999999999999998), text = Localizer.FishingFailure, text_pos = (0, 0.12), text_scale = 0.080000000000000002, pos = (0, 0, 0.58699999999999997))
        self.failureLabel = DirectLabel(parent = self.failureFrame, text = '', text_scale = 0.059999999999999998, text_wordwrap = 16, pos = (0, 0, -0.040000000000000001))
        self.brokeGui = NodePath('brokeGui')
        self.brokeFrame = DirectFrame(parent = self.brokeGui, relief = None, geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (1.2, 1, 0.59999999999999998), text = Localizer.FishingBrokeHeader, text_pos = (0, 0.12), text_scale = 0.080000000000000002, pos = (0, 0, 0.58699999999999997))
        self.brokeLabel = DirectLabel(parent = self.brokeFrame, relief = None, text = Localizer.FishingBroke, text_scale = 0.059999999999999998, text_wordwrap = 16, pos = (0, 0, -0.040000000000000001))
        self.madeGui = 1

    
    def _DistributedFishingSpot__unmakeGui(self):
        if not (self.madeGui):
            return None
        
        self.exitButton.destroy()
        self.castButton.destroy()
        self.jar.destroy()
        self.reelButton.destroy()
        self.crankHandle.destroy()
        self.speedGauge.destroy()
        self.itemFrame.destroy()
        self.failureFrame.destroy()
        self.brokeFrame.destroy()
        self.madeGui = 0

    
    def _DistributedFishingSpot__getBobSpot(self):
        if self.gotBobSpot:
            return None
        
        startSpot = (0, 8, 5)
        ray = CollisionRay(startSpot[0], startSpot[1], startSpot[2], 0, 0, -1)
        rayNode = CollisionNode('BobRay')
        rayNode.setCollideMask(BitMask32.allOff())
        rayNode.setCollideGeom(1)
        rayNode.addSolid(ray)
        rayNodePath = self.nodePath.attachNewNode(rayNode)
        cqueue = CollisionHandlerQueue()
        
        try:
            world = toonbase.tcr.playGame.getPlace().loader.geom
        except:
            world = None

        if world != None:
            trav = CollisionTraverser()
            trav.addCollider(rayNode, cqueue)
            trav.traverse(world)
        
        rayNodePath.removeNode()
        cqueue.sortEntries()
        if cqueue.getNumEntries() == 0:
            self.notify.warning("Couldn't find bob spot for %d" % self.doId)
            self.bobSpot = Point3(startSpot[0], startSpot[1], 0)
        else:
            entry = cqueue.getEntry(0)
            self.bobSpot = Point3(entry.getFromIntersectionPoint())
        self.gotBobSpot = 1

    
    def b_fishReleaseQuery(self, fish):
        self.fishReleaseQuery(fish)
        self.d_fishReleaseQuery(fish)

    
    def fishReleaseQuery(self, fish):
        self.av.fishPage.showReleaseFishPanel(fish)

    
    def d_fishReleaseQuery(self, fish):
        self.sendUpdate('fishReleaseQuery', [
            fish])

    
    def b_fishReleased(self, fish):
        self.fishReleased(fish)
        self.d_fishReleased(fish)

    
    def d_fishReleased(self, fish):
        self.sendUpdate('fishReleased', [
            fish])

    
    def fishReleased(self, fish):
        self._DistributedFishingSpot__showCastGui()


