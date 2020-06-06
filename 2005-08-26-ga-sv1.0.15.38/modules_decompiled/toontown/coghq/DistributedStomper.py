# File: D (Python 2.2)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from StomperGlobals import *
from direct.distributed import ClockDelta
from direct.showbase.PythonUtil import lerp
import math
import DistributedCrusherEntity
import MovingPlatform
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task

class DistributedStomper(DistributedCrusherEntity.DistributedCrusherEntity):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStomper')
    stomperSounds = [
        'phase_9/audio/sfx/CHQ_FACT_stomper_small.mp3',
        'phase_9/audio/sfx/CHQ_FACT_stomper_med.mp3',
        'phase_9/audio/sfx/CHQ_FACT_stomper_large.mp3']
    stomperModels = [
        'phase_9/models/cogHQ/square_stomper']
    
    def __init__(self, cr):
        self.lastPos = Point3(0, 0, 0)
        self.model = None
        self.smokeTrack = None
        self.ival = None
        self.smoke = None
        self.shadow = None
        self.sound = None
        self.crushSurface = None
        self.crushedList = []
        self.sounds = []
        self.wantSmoke = 1
        self.wantShadow = 1
        self.animateShadow = 1
        for s in self.stomperSounds:
            self.sounds.append(loader.loadSfx(s))
        
        DistributedCrusherEntity.DistributedCrusherEntity.__init__(self, cr)

    
    def generateInit(self):
        self.notify.debug('generateInit')
        DistributedCrusherEntity.DistributedCrusherEntity.generateInit(self)

    
    def generate(self):
        self.notify.debug('generate')
        DistributedCrusherEntity.DistributedCrusherEntity.generate(self)

    
    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        DistributedCrusherEntity.DistributedCrusherEntity.announceGenerate(self)
        self.loadModel()

    
    def disable(self):
        self.notify.debug('disable')
        self.ignoreAll()
        if self.ival:
            self.ival.pause()
            del self.ival
            self.ival = None
        
        if self.smokeTrack:
            self.smokeTrack.pause()
            del self.smokeTrack
            self.smokeTrack = None
        
        DistributedCrusherEntity.DistributedCrusherEntity.disable(self)

    
    def delete(self):
        self.notify.debug('delete')
        self.unloadModel()
        taskMgr.remove(self.taskName('smokeTask'))
        DistributedCrusherEntity.DistributedCrusherEntity.delete(self)

    
    def loadModel(self):
        self.notify.debug('loadModel')
        shadow = None
        self.sound = self.sounds[self.soundPath]
        self.rotateNode = self.attachNewNode('rotate')
        stomperModel = loader.loadModelCopy(self.stomperModels[self.modelPath])
        if self.style == 'vertical':
            model = stomperModel
            self.rotateNode.setP(-90)
            sideList = model.findAllMatches('**/collSide').asList()
            for side in sideList:
                side.stash()
            
            upList = model.findAllMatches('**/collUp').asList()
            for up in upList:
                up.stash()
            
            head = model.find('**/head')
            shaft = model.find('**/shaft')
            self.crushSurface = head.find('**/collDownWalls')
            self.shadow = None
            if self.wantShadow:
                shadow = loader.loadModelCopy('phase_3/models/props/square_drop_shadow').getChild(0)
                shadow.setScale(0.29999999999999999 * self.headScale[0], 0.29999999999999999 * self.headScale[2], 1)
                shadow.setAlphaScale(0.80000000000000004)
                shadow.flattenMedium()
                shadow.reparentTo(self)
                shadow.setPos(0, 0, 0.025000000000000001)
                shadow.setTransparency(1)
                self.shadow = shadow
            
            floorHead = model.find('**/head_collisions/**/collDownFloor').node()
            for i in range(floorHead.getNumSolids()):
                floorHead.getSolid(i).setEffectiveNormal(Vec3(0.0, -1.0, 0.0))
            
            floorShaft = model.find('**/shaft_collisions/**/collDownFloor').node()
            for i in range(floorShaft.getNumSolids()):
                floorShaft.getSolid(i).setEffectiveNormal(Vec3(0.0, -1.0, 0.0))
            
            self.accept(self.crushMsg, self.checkSquashedToon)
        elif self.style == 'horizontal':
            model = MovingPlatform.MovingPlatform()
            model.setupCopyModel(self.getParentToken(), stomperModel, 'collSideFloor')
            head = model.find('**/head')
            head.node().setPreserveTransform(0)
            head.setZ(1.0)
            for child in head.findAllMatches('+ModelNode').asList():
                child.node().setPreserveTransform(ModelNode.PTNet)
            
            model.flattenLight()
            upList = model.findAllMatches('**/collUp').asList()
            for up in upList:
                up.stash()
            
            downList = model.findAllMatches('**/collDown').asList()
            for down in downList:
                down.stash()
            
            self.crushSurface = model.find('**/head_collisions/**/collSideWalls')
        
        shaft = model.find('**/shaft')
        shaft.setScale(self.shaftScale)
        head.setScale(self.headScale)
        model.find('**/shaft').node().setPreserveTransform(0)
        model.flattenLight()
        self.model = model
        if self.motion == MotionSwitched:
            self.model.setPos(0, -(self.range), 0)
        
        self.model.reparentTo(self.rotateNode)
        if self.wantSmoke:
            self.smoke = loader.loadModelCopy('phase_8/models/props/test_clouds')
            self.smoke.setColor(0.80000000000000004, 0.69999999999999996, 0.5, 1)
            self.smoke.setBillboardPointEye()
        

    
    def stashCrushSurface(self, isStunned):
        self.notify.debug('stashCrushSurface(%s)' % isStunned)
        if self.crushSurface and not self.crushSurface.isEmpty():
            if isStunned:
                self.crushSurface.stash()
            else:
                self.crushSurface.unstash()
        

    
    def unloadModel(self):
        if self.ival:
            self.ival.pause()
            del self.ival
            self.ival = None
        
        if self.smoke:
            self.smoke.removeNode()
            del self.smoke
            self.smoke = None
        
        if self.shadow:
            self.shadow.removeNode()
            del self.shadow
            self.shadow = None
        
        if self.model:
            if isinstance(self.model, MovingPlatform.MovingPlatform):
                self.model.destroy()
            else:
                self.model.removeNode()
            del self.model
            self.model = None
        

    
    def sendStompToon(self):
        messenger.send(self.crushMsg)

    
    def doCrush(self):
        self.notify.debug('doCrush, crushedList = %s' % self.crushedList)
        for crushableId in self.crushedList:
            crushable = self.level.entities.get(crushableId)
            if crushable:
                if self.style == 'vertical':
                    axis = 2
                else:
                    axis = 0
                crushable.playCrushMovie(self.entId, axis)
            
        
        self.crushedList = []

    
    def getMotionIval(self, mode = STOMPER_START):
        if self.range == 0.0:
            return (None, 0)
        
        wantSound = self.soundOn
        if self.motion is MotionLinear:
            motionIval = Sequence(LerpPosInterval(self.model, self.period / 2.0, Point3(0, -(self.range), 0), startPos = Point3(0, 0, 0), fluid = 1), WaitInterval(self.period / 4.0), LerpPosInterval(self.model, self.period / 4.0, Point3(0, 0, 0), startPos = Point3(0, -(self.range), 0), fluid = 1))
        elif self.motion is MotionSinus:
            
            def sinusFunc(t, self = self):
                theta = math.pi + t * 2.0 * math.pi
                c = math.cos(theta)
                self.model.setFluidY((0.5 + c * 0.5) * -(self.range))

            motionIval = Sequence(LerpFunctionInterval(sinusFunc, duration = self.period))
        elif self.motion is MotionSlowFast:
            
            def motionFunc(t, self = self):
                stickTime = 0.20000000000000001
                turnaround = 0.94999999999999996
                t = t % 1
                if t < stickTime:
                    self.model.setFluidY(0)
                elif t < turnaround:
                    self.model.setFluidY((t - stickTime) * -(self.range) / (turnaround - stickTime))
                elif t > turnaround:
                    self.model.setFluidY(-(self.range) + (t - turnaround) * self.range / (1 - turnaround))
                

            motionIval = Sequence(LerpFunctionInterval(motionFunc, duration = self.period))
        elif self.motion is MotionCrush:
            
            def motionFunc(t, self = self):
                stickTime = 0.20000000000000001
                pauseAtTopTime = 0.5
                turnaround = 0.84999999999999998
                t = t % 1
                if t < stickTime:
                    self.model.setFluidY(0)
                elif t <= turnaround - pauseAtTopTime:
                    self.model.setFluidY((t - stickTime) * -(self.range) / (turnaround - pauseAtTopTime - stickTime))
                elif t > turnaround - pauseAtTopTime and t <= turnaround:
                    self.model.setFluidY(-(self.range))
                elif t > turnaround:
                    self.model.setFluidY(-(self.range) + (t - turnaround) * self.range / (1 - turnaround))
                

            tStick = 0.20000000000000001 * self.period
            tUp = 0.45000000000000001 * self.period
            tPause = 0.20000000000000001 * self.period
            tDown = 0.14999999999999999 * self.period
            motionIval = Sequence(Wait(tStick), LerpPosInterval(self.model, tUp, Vec3(0, -(self.range), 0), blendType = 'easeInOut', fluid = 1), Wait(tPause), Func(self.doCrush), LerpPosInterval(self.model, tDown, Vec3(0, 0, 0), blendType = 'easeInOut', fluid = 1))
        elif self.motion is MotionSwitched:
            if mode == STOMPER_STOMP:
                motionIval = Sequence(Func(self.doCrush), LerpPosInterval(self.model, 0.34999999999999998, Vec3(0, 0, 0), blendType = 'easeInOut', fluid = 1))
            elif mode == STOMPER_RISE:
                motionIval = Sequence(LerpPosInterval(self.model, 0.5, Vec3(0, -(self.range), 0), blendType = 'easeInOut', fluid = 1))
                wantSound = 0
            else:
                motionIval = None
        else:
            
            def halfSinusFunc(t, self = self):
                self.model.setFluidY(math.sin(t * math.pi) * -(self.range))

            motionIval = Sequence(LerpFunctionInterval(halfSinusFunc, duration = self.period))
        return (motionIval, wantSound)

    
    def startStomper(self, startTime, mode = STOMPER_START):
        if self.ival:
            self.ival.pause()
            del self.ival
            self.ival = None
        
        (motionIval, wantSound) = self.getMotionIval(mode)
        if motionIval == None:
            return None
        
        self.ival = Parallel(Sequence(motionIval, Func(self._DistributedStomper__startSmokeTask), Func(self.sendStompToon)), name = self.uniqueName('Stomper'))
        if wantSound:
            sndDur = motionIval.getDuration()
            self.ival.append(Sequence(Wait(sndDur), Func(base.playSfx, self.sound, node = self.model, volume = 0.45000000000000001)))
        
        if self.shadow is not None and self.animateShadow:
            
            def adjustShadowScale(t, self = self):
                modelY = self.model.getY()
                maxHeight = 10
                a = min(-modelY / maxHeight, 1.0)
                self.shadow.setScale(lerp(1, 0.20000000000000001, a))
                self.shadow.setAlphaScale(lerp(1, 0.20000000000000001, a))

            self.ival.append(LerpFunctionInterval(adjustShadowScale, duration = self.period))
        
        if mode == STOMPER_START:
            self.ival.loop()
            self.ival.setT((globalClock.getFrameTime() - self.level.startTime) + self.period * self.phaseShift)
        else:
            self.ival.start(startTime)

    
    def stopStomper(self):
        if self.ival:
            self.ival.pause()
        
        if self.smokeTrack:
            self.smokeTrack.finish()
            del self.smokeTrack
            self.smokeTrack = None
        

    
    def setMovie(self, mode, timestamp, crushedList):
        self.notify.debug('setMovie %d' % mode)
        timestamp = ClockDelta.globalClockDelta.networkToLocalTime(timestamp)
        now = globalClock.getFrameTime()
        if mode == STOMPER_START and mode == STOMPER_RISE or mode == STOMPER_STOMP:
            self.crushedList = crushedList
            self.startStomper(timestamp, mode)
        

    
    def _DistributedStomper__startSmokeTask(self):
        taskMgr.remove(self.taskName('smokeTask'))
        if self.wantSmoke:
            taskMgr.add(self._DistributedStomper__smokeTask, self.taskName('smokeTask'))
        

    
    def _DistributedStomper__smokeTask(self, task):
        self.smoke.reparentTo(self)
        self.smoke.setScale(1)
        if self.smokeTrack:
            self.smokeTrack.finish()
            del self.smokeTrack
        
        self.smokeTrack = Sequence(Parallel(LerpScaleInterval(self.smoke, 0.20000000000000001, Point3(4, 1, 4)), LerpColorScaleInterval(self.smoke, 1, Vec4(1, 1, 1, 0))), Func(self.smoke.reparentTo, hidden), Func(self.smoke.clearColorScale))
        self.smokeTrack.start()
        return Task.done

    
    def checkSquashedToon(self):
        if self.style == 'vertical':
            tPos = base.localAvatar.getPos(self.rotateNode)
            zRange = self.headScale[2]
            xRange = self.headScale[0]
            yRange = 5
            if tPos[2] < zRange and tPos[2] > -zRange and tPos[0] < xRange and tPos[0] > -xRange and tPos[1] < yRange / 10.0 and tPos[1] > -yRange:
                self.level.b_setOuch(self.damage, 'Squish')
                base.localAvatar.setZ(self.getZ(render) + 0.025000000000000001)
            
        

    if __dev__:
        
        def attribChanged(self, *args):
            self.stopStomper()
            self.unloadModel()
            self.loadModel()
            self.startStomper(0)

    

