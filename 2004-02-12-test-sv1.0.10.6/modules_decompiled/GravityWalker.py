# File: G (Python 2.2)

from ShowBaseGlobal import *
import DirectNotifyGlobal
import DirectObject
import PhysicsManager
import math

class GravityWalker(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('GravityWalker')
    wantDebugIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    
    def __init__(self, gravity = -32.173999999999999, standableGround = 0.70699999999999996, hardLandingForce = 16.0):
        DirectObject.DirectObject.__init__(self)
        self._GravityWalker__gravity = gravity
        self._GravityWalker__standableGround = standableGround
        self._GravityWalker__hardLandingForce = hardLandingForce
        self.mayJump = 1
        self.jumpDelayTask = None
        self.controlsTask = None
        self.fixCliffTask = None
        self.indicatorTask = None
        self.falling = 0
        self.needToDeltaPos = 0
        self.physVelocityIndicator = None
        self.avatarControlForwardSpeed = 0
        self.avatarControlJumpForce = 0
        self.avatarControlReverseSpeed = 0
        self.avatarControlRotateSpeed = 0
        self.getAirborneHeight = None
        self.priorParent = Vec3(0)
        self._GravityWalker__oldPosDelta = Vec3(0)
        self._GravityWalker__oldDt = 0
        self.moving = 0
        self.speed = 0.0
        self.rotationSpeed = 0.0
        self.slideSpeed = 0.0
        self.vel = Vec3(0.0)
        self.collisionsActive = 0
        self.isAirborne = 0
        self.highMark = 0

    
    def delete(self):
        if self.doLaterTask is not None:
            self.doLaterTask.remove()
            del self.doLaterTask
        

    
    def spawnTest(self):
        if not (self.wantDebugIndicator):
            return None
        
        from PandaModules import *
        from IntervalGlobal import *
        import MovingPlatform
        if hasattr(self, 'platform'):
            self.moveIval.pause()
            del self.moveIval
            self.platform.destroy()
            del self.platform
            self.platform2.destroy()
            del self.platform2
        
        model = loader.loadModelCopy('phase_9/models/cogHQ/platform1')
        fakeId = id(self)
        self.platform = MovingPlatform.MovingPlatform()
        self.platform.setupCopyModel(fakeId, model, 'platformcollision')
        self.platformRoot = render.attachNewNode('GravityWalker-spawnTest-%s' % fakeId)
        self.platformRoot.setPos(toonbase.localToon, Vec3(0.0, 0.0, 1.0))
        self.platformRoot.setHpr(toonbase.localToon, Vec3.zero())
        self.platform.reparentTo(self.platformRoot)
        self.platform2 = MovingPlatform.MovingPlatform()
        self.platform2.setupCopyModel(1 + fakeId, model, 'platformcollision')
        self.platform2Root = render.attachNewNode('GravityWalker-spawnTest2-%s' % fakeId)
        self.platform2Root.setPos(toonbase.localToon, Vec3(-16.0, 30.0, 1.0))
        self.platform2Root.setHpr(toonbase.localToon, Vec3.zero())
        self.platform2.reparentTo(self.platform2Root)
        duration = 5
        self.moveIval = Parallel(Sequence(WaitInterval(0.29999999999999999), LerpPosInterval(self.platform, duration, Vec3(0.0, 30.0, 0.0), name = 'platformOut%s' % fakeId, fluid = 1), WaitInterval(0.29999999999999999), LerpPosInterval(self.platform, duration, Vec3(0.0, 0.0, 0.0), name = 'platformBack%s' % fakeId, fluid = 1), WaitInterval(0.29999999999999999), LerpPosInterval(self.platform, duration, Vec3(0.0, 0.0, 30.0), name = 'platformUp%s' % fakeId, fluid = 1), WaitInterval(0.29999999999999999), LerpPosInterval(self.platform, duration, Vec3(0.0, 0.0, 0.0), name = 'platformDown%s' % fakeId, fluid = 1)), Sequence(WaitInterval(0.29999999999999999), LerpPosInterval(self.platform2, duration, Vec3(0.0, -30.0, 0.0), name = 'platform2Out%s' % fakeId, fluid = 1), WaitInterval(0.29999999999999999), LerpPosInterval(self.platform2, duration, Vec3(0.0, 30.0, 30.0), name = 'platform2Back%s' % fakeId, fluid = 1), WaitInterval(0.29999999999999999), LerpPosInterval(self.platform2, duration, Vec3(0.0, -30.0, 0.0), name = 'platform2Up%s' % fakeId, fluid = 1), WaitInterval(0.29999999999999999), LerpPosInterval(self.platform2, duration, Vec3(0.0, 0.0, 0.0), name = 'platformDown%s' % fakeId, fluid = 1)), name = 'platformIval%s' % fakeId)
        self.moveIval.loop()

    
    def setWalkSpeed(self, forward, jump, reverse, rotate):
        self.avatarControlForwardSpeed = forward
        self.avatarControlJumpForce = jump
        self.avatarControlReverseSpeed = reverse
        self.avatarControlRotateSpeed = rotate

    
    def getSpeeds(self):
        return (self.speed, self.rotationSpeed)

    
    def setupRay(self, bitmask, floorOffset):
        cRay = CollisionRay(0.0, 0.0, 4.0, 0.0, 0.0, -1.0)
        cRayNode = CollisionNode('GW.cRayNode')
        cRayNode.addSolid(cRay)
        self.cRayNodePath = self.avatarNodePath.attachNewNode(cRayNode)
        cRayNode.setFromCollideMask(bitmask)
        cRayNode.setIntoCollideMask(BitMask32.allOff())
        self.lifter = CollisionHandlerGravity()
        self.lifter.setGravity(32.173999999999999 * 2.0)
        self.lifter.addInPattern('enter%in')
        self.lifter.addOutPattern('exit%in')
        self.lifter.setOffset(floorOffset)
        self.lifter.addCollider(self.cRayNodePath, self.avatarNodePath)

    
    def setupWallSphere(self, bitmask, avatarRadius):
        self.avatarRadius = avatarRadius
        cSphere = CollisionSphere(0.0, 0.0, avatarRadius, avatarRadius)
        cSphereNode = CollisionNode('GW.cWallSphereNode')
        cSphereNode.addSolid(cSphere)
        cSphereNodePath = self.avatarNodePath.attachNewNode(cSphereNode)
        cSphereNode.setFromCollideMask(bitmask)
        cSphereNode.setIntoCollideMask(BitMask32.allOff())
        handler = CollisionHandlerPusher()
        handler.addCollider(cSphereNodePath, self.avatarNodePath)
        self.pusher = handler
        self.cWallSphereNodePath = cSphereNodePath

    
    def setupEventSphere(self, bitmask, avatarRadius):
        self.avatarRadius = avatarRadius
        cSphere = CollisionSphere(0.0, 0.0, avatarRadius - 0.10000000000000001, avatarRadius * 1.04)
        cSphere.setTangible(0)
        cSphereNode = CollisionNode('GW.cEventSphereNode')
        cSphereNode.addSolid(cSphere)
        cSphereNodePath = self.avatarNodePath.attachNewNode(cSphereNode)
        cSphereNode.setFromCollideMask(bitmask)
        cSphereNode.setIntoCollideMask(BitMask32.allOff())
        handler = CollisionHandlerEvent()
        handler.addInPattern('enter%in')
        handler.addOutPattern('exit%in')
        self.event = handler
        self.cEventSphereNodePath = cSphereNodePath

    
    def setupFloorSphere(self, bitmask, avatarRadius):
        self.avatarRadius = avatarRadius
        cSphere = CollisionSphere(0.0, 0.0, avatarRadius, 0.01)
        cSphereNode = CollisionNode('GW.cFloorSphereNode')
        cSphereNode.addSolid(cSphere)
        cSphereNodePath = self.avatarNodePath.attachNewNode(cSphereNode)
        cSphereNode.setFromCollideMask(bitmask)
        cSphereNode.setIntoCollideMask(BitMask32.allOff())
        handler = CollisionHandlerPusher()
        handler.addCollider(cSphereNodePath, self.avatarNodePath)
        self.pusherFloor = handler
        self.cFloorSphereNodePath = cSphereNodePath

    
    def initializeCollisions(self, collisionTraverser, avatarNodePath, wallBitmask, floorBitmask, avatarRadius = 1.3999999999999999, floorOffset = 1.0):
        self.avatarNodePath = avatarNodePath
        self.cTrav = collisionTraverser
        self.floorOffset = 0.0
        self.setupRay(floorBitmask, self.floorOffset)
        self.setupWallSphere(wallBitmask, avatarRadius)
        self.setupEventSphere(wallBitmask, avatarRadius)
        self.setCollisionsActive(1)

    
    def setAirborneHeightFunc(self, unused_parameter):
        self.getAirborneHeight = self.lifter.getAirborneHeight

    
    def getAirborneHeight(self):
        self.lifter.getAirborneHeight()

    
    def setAvatarPhysicsIndicator(self, indicator):
        self.cWallSphereNodePath.show()

    
    def deleteCollisions(self):
        del self.cTrav
        self.cWallSphereNodePath.removeNode()
        del self.cWallSphereNodePath
        del self.pusher
        del self.event
        del self.lifter
        del self.getAirborneHeight

    
    def setCollisionsActive(self, active = 1):
        if self.collisionsActive != active:
            self.collisionsActive = active
            self.oneTimeCollide()
            if active:
                self.cTrav.addCollider(self.cWallSphereNodePath, self.pusher)
                self.cTrav.addCollider(self.cEventSphereNodePath, self.event)
                self.cTrav.addCollider(self.cRayNodePath, self.lifter)
            else:
                self.cTrav.removeCollider(self.cWallSphereNodePath)
                self.cTrav.removeCollider(self.cEventSphereNodePath)
                self.cTrav.removeCollider(self.cRayNodePath)
        

    
    def getCollisionsActive(self):
        return self.collisionsActive

    
    def FixCliff(self, task):
        if self.collisionsActive and self.moving and self.lifter.isInOuterSpace():
            temp = self.cRayNodePath.getZ()
            self.cRayNodePath.setZ(14.0)
            self.oneTimeCollide()
            self.cRayNodePath.setZ(temp)
        
        return Task.cont

    
    def placeOnFloor(self):
        self.oneTimeCollide()
        self.avatarNodePath.setZ(self.avatarNodePath.getZ() - self.lifter.getAirborneHeight())

    
    def oneTimeCollide(self):
        tempCTrav = CollisionTraverser('oneTimeCollide')
        tempCTrav.addCollider(self.cWallSphereNodePath, self.pusher)
        tempCTrav.addCollider(self.cRayNodePath, self.lifter)
        tempCTrav.traverse(render)

    
    def setMayJump(self, task):
        self.mayJump = 1
        return Task.done

    
    def startJumpDelay(self, delay):
        if self.jumpDelayTask:
            self.jumpDelayTask.remove()
        
        self.mayJump = 0
        self.jumpDelayTask = taskMgr.doMethodLater(delay, self.setMayJump, 'jumpDelay-%s' % id(self))

    
    def displayDebugInfo(self):
        onScreenDebug.add('airborneHeight', self.lifter.getAirborneHeight())
        onScreenDebug.add('falling', self.falling)
        onScreenDebug.add('isOnGround', self.lifter.isOnGround())
        onScreenDebug.add('gravity', self.lifter.getGravity())
        onScreenDebug.add('jumpForce', self.avatarControlJumpForce)
        onScreenDebug.add('mayJump', self.mayJump)
        onScreenDebug.add('impact', self.lifter.getImpactVelocity())
        onScreenDebug.add('velocity', self.lifter.getVelocity())
        onScreenDebug.add('isAirborne', self.isAirborne)
        onScreenDebug.add('inOuterSpace', self.lifter.isInOuterSpace())

    
    def handleAvatarControls(self, task):
        forward = inputState.isSet('forward')
        reverse = inputState.isSet('reverse')
        turnLeft = inputState.isSet('turnLeft')
        turnRight = inputState.isSet('turnRight')
        slide = 0
        jump = inputState.isSet('jump')
        if forward and self.avatarControlForwardSpeed and reverse:
            pass
        self.speed = -(self.avatarControlReverseSpeed)
        if slide:
            if turnLeft and -(self.avatarControlForwardSpeed) and turnRight:
                pass
        self.slideSpeed = self.avatarControlForwardSpeed
        if not slide:
            if turnLeft and self.avatarControlRotateSpeed and turnRight:
                pass
        self.rotationSpeed = -(self.avatarControlRotateSpeed)
        if self.needToDeltaPos:
            self.setPriorParentVector()
            self.needToDeltaPos = 0
        
        if self.wantDebugIndicator:
            self.displayDebugInfo()
        
        if self.lifter.isOnGround():
            if self.isAirborne:
                self.isAirborne = 0
                impact = self.lifter.getImpactVelocity()
                if impact < -30.0:
                    messenger.send('jumpHardLand')
                    self.startJumpDelay(0.29999999999999999)
                else:
                    messenger.send('jumpLand')
                    if impact < -5.0:
                        self.startJumpDelay(0.20000000000000001)
                    
            
            self.priorParent = Vec3.zero()
            if jump and self.mayJump:
                self.lifter.addVelocity(self.avatarControlJumpForce)
                messenger.send('jumpStart')
                self.isAirborne = 1
            
        elif self.isAirborne == 0:
            pass
        
        self.isAirborne = 1
        self._GravityWalker__oldPosDelta = self.avatarNodePath.getPosDelta(render)
        self._GravityWalker__oldDt = ClockObject.getGlobalClock().getDt()
        dt = self._GravityWalker__oldDt
        if not self.speed and self.slideSpeed and self.rotationSpeed:
            pass
        self.moving = self.priorParent != Vec3.zero()
        if self.moving:
            distance = dt * self.speed
            slideDistance = dt * self.slideSpeed
            rotation = dt * self.rotationSpeed
            self.vel = Vec3(Vec3.forward() * distance + Vec3.right() * slideDistance)
            if self.vel != Vec3.zero() or self.priorParent != Vec3.zero():
                rotMat = Mat3.rotateMatNormaxis(self.avatarNodePath.getH(), Vec3.up())
                step = rotMat.xform(self.vel) + self.priorParent * dt
                self.avatarNodePath.setFluidPos(Point3(self.avatarNodePath.getPos() + step))
            
            self.avatarNodePath.setH(self.avatarNodePath.getH() + rotation)
        else:
            self.vel.set(0.0, 0.0, 0.0)
        if self.moving or jump:
            messenger.send('avatarMoving')
        
        return Task.cont

    
    def doDeltaPos(self):
        self.needToDeltaPos = 1

    
    def setPriorParentVector(self):
        velocity = self._GravityWalker__oldPosDelta * (1.0 / self._GravityWalker__oldDt)
        self.priorParent = Vec3(velocity)

    
    def reset(self):
        self.lifter.setVelocity(0.0)
        self.priorParent = Vec3.zero()

    
    def enableAvatarControls(self):
        print id(self), 'GW.enableAvatarControls()'
        if self.controlsTask:
            self.controlsTask.remove()
        
        taskName = 'AvatarControls%s' % (id(self),)
        self.controlsTask = taskMgr.add(self.handleAvatarControls, taskName, 25)
        if self.fixCliffTask:
            self.fixCliffTask.remove()
        
        taskName = 'AvatarControls-FixCliff%s' % (id(self),)
        self.fixCliffTask = taskMgr.add(self.FixCliff, taskName, 31)
        if self.physVelocityIndicator:
            if self.indicatorTask:
                self.indicatorTask.remove()
            
            self.indicatorTask = taskMgr.add(self.avatarPhysicsIndicator, 'AvatarControlsIndicator%s' % (id(self),), 35)
        

    
    def disableAvatarControls(self):
        print id(self), 'GW.disableAvatarControls()'
        if self.controlsTask:
            self.controlsTask.remove()
            self.controlsTask = None
        
        if self.fixCliffTask:
            self.fixCliffTask.remove()
            self.fixCliffTask = None
        
        if self.indicatorTask:
            self.indicatorTask.remove()
            self.indicatorTask = None
        


