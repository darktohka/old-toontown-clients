# File: D (Python 2.2)

from ShowBaseGlobal import *
from PandaObject import *
from IntervalGlobal import *
from ToontownGlobals import *
from CrateGlobals import *
import DistributedObject
import DirectNotifyGlobal
import MovingPlatform
import DistributedCrushableEntity

class DistributedCrate(DistributedCrushableEntity.DistributedCrushableEntity):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCrate')
    UP_KEY = 'arrow_up'
    DOWN_KEY = 'arrow_down'
    LEFT_KEY = 'arrow_left'
    RIGHT_KEY = 'arrow_right'
    
    def __init__(self, cr):
        DistributedCrushableEntity.DistributedCrushableEntity.__init__(self, cr)
        self.initNodePath()
        self.modelPath = 'phase_9/models/cogHQ/woodCrateB'
        self.crate = None
        self.gridSize = 3.0
        self.tContact = 0
        self.tStick = 0.01
        self.moveTrack = None
        self.avMoveTrack = None
        self.avPushTrack = None
        self.crate = None
        self.crushTrack = None
        self.isLocalToon = 0
        self.stuckToCrate = 0
        self.upPressed = 0
        self.isPushing = 0
        self.creakSound = loader.loadSfx('phase_9/audio/sfx/CHQ_FACT_crate_effort.mp3')
        self.pushSound = loader.loadSfx('phase_9/audio/sfx/CHQ_FACT_crate_sliding.mp3')

    
    def disable(self):
        self.ignoreAll()
        if self.moveTrack:
            self.moveTrack.pause()
            del self.moveTrack
        
        if self.avMoveTrack:
            self.avMoveTrack.pause()
            del self.avMoveTrack
        
        if self.avPushTrack:
            self.avPushTrack.pause()
            del self.avPushTrack
        
        if self.crate:
            self.crate.destroy()
            del self.crate
        
        if self.crushTrack:
            self.crushTrack.pause()
            del self.crushTrack
        
        taskMgr.remove(self.taskName('crushTask'))
        if self.pushable:
            self._DistributedCrate__listenForCollisions(0)
            self.ignore('arrow_up')
            self.ignore('arrow_up-up')
        
        DistributedCrushableEntity.DistributedCrushableEntity.disable(self)

    
    def delete(self):
        DistributedCrushableEntity.DistributedCrushableEntity.delete(self)
        del self.creakSound
        del self.pushSound

    
    def generateInit(self):
        DistributedCrushableEntity.DistributedCrushableEntity.generateInit(self)

    
    def generate(self):
        DistributedCrushableEntity.DistributedCrushableEntity.generate(self)

    
    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        DistributedCrushableEntity.DistributedCrushableEntity.announceGenerate(self)
        self.loadModel()
        self.modCrateCollisions()
        if self.pushable:
            self._DistributedCrate__listenForCollisions(1)
            self.accept('arrow_up', self._DistributedCrate__upKeyPressed)
        

    
    def modCrateCollisions(self):
        cNode = self.find('**/wall')
        cNode.setName(self.uniqueName('crateCollision'))
        cNode.setZ(-0.80000000000000004)
        colNode = self.find('**/collision')
        floor = colNode.find('**/MovingPlatform*')
        floor2 = floor.copyTo(colNode)
        floor2.setZ(-0.80000000000000004)

    
    def _DistributedCrate__upKeyPressed(self):
        self.ignore('arrow_up')
        self.accept('arrow_up-up', self._DistributedCrate__upKeyReleased)
        self.upPressed = 1

    
    def _DistributedCrate__upKeyReleased(self):
        self.ignore('arrow_up-up')
        self.accept('arrow_up', self._DistributedCrate__upKeyPressed)
        self.upPressed = 0
        if self.stuckToCrate:
            self._DistributedCrate__resetStick()
        

    
    def loadModel(self):
        crateModel = loader.loadModelCopy(self.modelPath)
        self.crate = MovingPlatform.MovingPlatform()
        self.crate.setupCopyModel(self.entId, crateModel, 'floor')
        self.setScale(1.0)
        self.crate.setScale(self.scale)
        self.crate.reparentTo(self)
        self.crate.flattenLight()

    
    def setScale(self, scale):
        if self.crate:
            self.crate.setScale(scale)
        

    
    def _DistributedCrate__listenForCollisions(self, on):
        if on:
            self.accept(self.uniqueName('entercrateCollision'), self.handleCollision)
        else:
            self.ignore(self.uniqueName('entercrateCollision'))

    
    def setPosition(self, x, y, z):
        self.setPos(x, y, z)

    
    def handleCollision(self, collEntry = None):
        if not (self.upPressed):
            return None
        
        crateNormal = Vec3(collEntry.getIntoSurfaceNormal())
        relativeVec = toonbase.localToon.getRelativeVector(self, crateNormal)
        relativeVec.normalize()
        worldVec = render.getRelativeVector(self, crateNormal)
        worldVec.normalize()
        offsetVec = Vec3(toonbase.localToon.getPos(render) - self.getPos(render))
        offsetVec.normalize()
        offsetDot = offsetVec[0] * worldVec[0] + offsetVec[1] * worldVec[1]
        self.notify.debug('offsetDot = %s, world = %s, rel = %s' % (offsetDot, worldVec, offsetVec))
        if relativeVec.getY() < -0.69999999999999996 and offsetDot > 0.90000000000000002 and offsetVec.getZ() < 0.050000000000000003:
            self.getCrateSide(crateNormal)
            self.tContact = globalClock.getFrameTime()
            self._DistributedCrate__listenForCollisions(0)
            self._DistributedCrate__listenForCancelEvents(1)
            self._DistributedCrate__startStickTask(crateNormal, toonbase.localToon.getPos(render))
        

    
    def setReject(self):
        self.notify.debug('setReject')
        self.sentRequest = 0
        if self.stuckToCrate:
            self._DistributedCrate__resetStick()
        

    
    def _DistributedCrate__startStickTask(self, crateNormal, toonPos):
        self._DistributedCrate__killStickTask()
        self.stuckToCrate = 1
        sTask = Task.Task(self._DistributedCrate__stickTask)
        sTask.crateNormal = crateNormal
        sTask.toonPos = toonPos
        taskMgr.add(sTask, self.taskName('stickTask'))

    
    def _DistributedCrate__killStickTask(self):
        taskMgr.remove(self.taskName('stickTask'))

    
    def _DistributedCrate__stickTask(self, task):
        tElapsed = globalClock.getFrameTime() - self.tContact
        if tElapsed > self.tStick:
            lToon = toonbase.localToon
            self.isLocalToon = 1
            crateNormal = task.crateNormal
            crateWidth = 2.75 * self.scale[0]
            offset = crateWidth + 1.5 + TorsoToOffset[lToon.style.torso]
            newPos = self.getPos(render) + crateNormal * offset
            if self.avPushTrack:
                self.avPushTrack.pause()
            
            place = toonbase.tcr.playGame.getPlace()
            newHpr = CrateHprs[self.crateSide]
            h = lToon.getH() % 360
            if h > 316 and h < 360:
                h -= 360
            
            lToon.setH(h)
            self.avPushTrack = Sequence(LerpPosHprInterval(lToon, 0.25, newPos, newHpr, other = render, blendType = 'easeInOut'), Func(place.fsm.request, 'push'), Func(self._DistributedCrate__sendPushRequest, task.crateNormal), SoundInterval(self.creakSound, node = self))
            self.avPushTrack.start()
            return Task.done
        else:
            pos = task.toonPos
            toonbase.localToon.setPos(task.toonPos)
            return Task.cont

    
    def getCrateSide(self, crateNormal):
        for i in range(len(CrateNormals)):
            dotP = CrateNormals[i].dot(crateNormal)
            if dotP > 0.90000000000000002:
                self.crateSide = i
            
        

    
    def _DistributedCrate__sendPushRequest(self, crateNormal):
        self.notify.debug('__sendPushRequest')
        if self.crateSide != None:
            self.sentRequest = 1
            self.sendUpdate('requestPush', [
                self.crateSide])
        else:
            self.notify.debug("didn't send request")

    
    def _DistributedCrate__listenForCancelEvents(self, on):
        self.notify.debug('%s, __listenForCancelEvents(%s)' % (self.doId, on))
        if on:
            self.accept('arrow_down', self._DistributedCrate__resetStick)
            self.accept('arrow_left', self._DistributedCrate__resetStick)
            self.accept('arrow_right', self._DistributedCrate__resetStick)
        else:
            self.ignore('arrow_down')
            self.ignore('arrow_left')
            self.ignore('arrow_right')

    
    def setMoveTo(self, avId, x0, y0, z0, x1, y1, z1):
        self.notify.debug('setMoveTo')
        self._DistributedCrate__moveCrateTo(Vec3(x0, y0, z0), Vec3(x1, y1, z1))
        isLocal = toonbase.localToon.doId == avId
        if isLocal and self.stuckToCrate or not isLocal:
            self._DistributedCrate__moveAvTo(avId, Vec3(x0, y0, z0), Vec3(x1, y1, z1))
        

    
    def _DistributedCrate__moveCrateTo(self, startPos, endPos):
        if self.moveTrack:
            self.moveTrack.finish()
            self.moveTrack = None
        
        self.moveTrack = Parallel(Sequence(LerpPosInterval(self, T_PUSH, endPos, startPos = startPos, fluid = 1)), SoundInterval(self.creakSound, node = self), SoundInterval(self.pushSound, node = self, duration = T_PUSH, volume = 0.20000000000000001))
        self.moveTrack.start()

    
    def _DistributedCrate__moveAvTo(self, avId, startPos, endPos):
        if self.avMoveTrack:
            self.avMoveTrack.finish()
            self.avMoveTrack = None
        
        av = toonbase.tcr.doId2do.get(avId)
        if av:
            avMoveTrack = Sequence()
            moveDir = endPos - startPos
            crateNormal = Vec3(moveDir)
            crateNormal.normalize()
            crateWidth = 2.75 * self.scale[0]
            offset = crateWidth + 1.5 + TorsoToOffset[av.style.torso]
            oldToonPos = self.getPos(render) - crateNormal * offset
            newToonPos = oldToonPos + moveDir
            avMoveTrack.append(Sequence(LerpPosInterval(av, T_PUSH, newToonPos, startPos = oldToonPos)))
            self.avMoveTrack = avMoveTrack
            self.avMoveTrack.start()
        

    
    def _DistributedCrate__resetStick(self):
        self.notify.debug('__resetStick')
        self._DistributedCrate__killStickTask()
        self._DistributedCrate__listenForCancelEvents(0)
        self._DistributedCrate__listenForCollisions(1)
        self.sendUpdate('setDone')
        if self.avPushTrack:
            self.avPushTrack.pause()
            del self.avPushTrack
            self.avPushTrack = None
        
        if self.avMoveTrack:
            self.avMoveTrack.pause()
            del self.avMoveTrack
            self.avMoveTrack = None
        
        toonbase.tcr.playGame.getPlace().fsm.request('walk')
        self.crateSide = None
        self.crateNormal = None
        self.isLocalToon = 0
        self.stuckToCrate = 0

    
    def playCrushMovie(self, crusherId, axis):
        self.notify.debug('playCrushMovie')
        taskMgr.remove(self.taskName('crushTask'))
        taskMgr.add(self.crushTask, self.taskName('crushTask'), extraArgs = (crusherId, axis), priority = 25)

    
    def crushTask(self, crusherId, axis):
        crusher = self.level.entities.get(crusherId, None)
        if crusher:
            crusherHeight = crusher.model.getPos(self)[2]
            maxHeight = self.pos[2] + self.scale[2]
            minHeight = crusher.getPos(self)[2]
            minScale = minHeight / maxHeight
            self.notify.debug('cHeight= %s' % crusherHeight)
            if crusherHeight < maxHeight and crusherHeight >= minHeight:
                if crusherHeight == minHeight:
                    self.setScale(Vec3(1.2, 1.2, minScale))
                    taskMgr.doMethodLater(2, self.setScale, 'resetScale', extraArgs = (1,))
                    return Task.done
                else:
                    k = crusherHeight / maxHeight
                    sx = min(1 / k, 0.20000000000000001)
                    self.setScale(Vec3(1 + sx, 1 + sx, k))
            
        
        return Task.cont

    
    def originalTry(self, axis):
        tSquash = 0.40000000000000002
        if self.crushTrack:
            self.crushTrack.finish()
            del self.crushTrack
            self.crushTrack = None
        
        self.crushTrack = Sequence(LerpScaleInterval(self, tSquash, VBase3(1.2, 1.2, 0.25), blendType = 'easeInOut'), LerpColorScaleInterval(self, 2.0, VBase4(1, 1, 1, 0), blendType = 'easeInOut'), Wait(2.0), LerpScaleInterval(self, 0.10000000000000001, VBase3(1, 1, 1), blendType = 'easeInOut'), LerpColorScaleInterval(self, 0.10000000000000001, VBase4(1, 1, 1, 0), blendType = 'easeInOut'))
        self.crushTrack.start()


