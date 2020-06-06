# File: G (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject
import math

class GravityWalker(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('GravityWalker')
    wantDebugIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    wantFloorSphere = base.config.GetBool('want-floor-sphere', 0)
    
    def __init__(self, gravity = -32.173999999999999, standableGround = 0.70699999999999996, hardLandingForce = 16.0):
        DirectObject.DirectObject.__init__(self)
        self._GravityWalker__gravity = gravity
        self._GravityWalker__standableGround = standableGround
        self._GravityWalker__hardLandingForce = hardLandingForce
        self.mayJump = 1
        self.jumpDelayTask = None
        self.controlsTask = None
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
        

    
    def setWalkSpeed(self, forward, jump, reverse, rotate):
        self.avatarControlForwardSpeed = forward
        self.avatarControlJumpForce = jump
        self.avatarControlReverseSpeed = reverse
        self.avatarControlRotateSpeed = rotate

    
    def getSpeeds(self):
        return (self.speed, self.rotationSpeed)

    
    def setAvatar(self, avatar):
        self.avatar = avatar
        if avatar is not None:
            pass
        1

    
    def setupRay(self, bitmask, floorOffset, reach):
        cRay = CollisionRay(0.0, 0.0, CollisionHandlerRayStart, 0.0, 0.0, -1.0)
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
        self.lifter.setReach(reach)
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

    
    def setWallBitMask(self, bitMask):
        self.wallBitmask = bitMask

    
    def setFloorBitMask(self, bitMask):
        self.floorBitmask = bitMask

    
    def initializeCollisions(self, collisionTraverser, avatarNodePath, avatarRadius = 1.3999999999999999, floorOffset = 1.0, reach = 1.0):
        self.avatarNodePath = avatarNodePath
        self.cTrav = collisionTraverser
        self.setupRay(self.floorBitmask, floorOffset, reach)
        self.setupWallSphere(self.wallBitmask, avatarRadius)
        self.setupEventSphere(self.wallBitmask, avatarRadius)
        if self.wantFloorSphere:
            self.setupFloorSphere(self.floorBitmask, avatarRadius)
        
        self.setCollisionsActive(1)

    
    def setTag(self, key, value):
        self.cEventSphereNodePath.setTag(key, value)

    
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
        if self.wantFloorSphere:
            self.cFloorSphereNodePath.removeNode()
            del self.cFloorSphereNodePath
        
        del self.pusher
        del self.event
        del self.lifter
        del self.getAirborneHeight

    
    def setCollisionsActive(self, active = 1):
        if self.collisionsActive != active:
            self.collisionsActive = active
            self.oneTimeCollide()
            if active:
                if 1:
                    self.avatarNodePath.setP(0.0)
                    self.avatarNodePath.setR(0.0)
                
                self.cTrav.addCollider(self.cWallSphereNodePath, self.pusher)
                if self.wantFloorSphere:
                    self.cTrav.addCollider(self.cFloorSphereNodePath, self.pusherFloor)
                
                self.cTrav.addCollider(self.cEventSphereNodePath, self.event)
                self.cTrav.addCollider(self.cRayNodePath, self.lifter)
            else:
                self.cTrav.removeCollider(self.cWallSphereNodePath)
                if self.wantFloorSphere:
                    self.cTrav.removeCollider(self.cFloorSphereNodePath)
                
                self.cTrav.removeCollider(self.cEventSphereNodePath)
                self.cTrav.removeCollider(self.cRayNodePath)
        

    
    def getCollisionsActive(self):
        return self.collisionsActive

    
    def placeOnFloor(self):
        self.oneTimeCollide()
        self.avatarNodePath.setZ(self.avatarNodePath.getZ() - self.lifter.getAirborneHeight())

    
    def oneTimeCollide(self):
        self.isAirborne = 0
        self.mayJump = 1
        tempCTrav = CollisionTraverser('oneTimeCollide')
        tempCTrav.addCollider(self.cWallSphereNodePath, self.pusher)
        if self.wantFloorSphere:
            tempCTrav.addCollider(self.cFloorSphereNodePath, self.event)
        
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
        onScreenDebug.add('w controls', 'GravityWalker')
        onScreenDebug.add('w airborneHeight', self.lifter.getAirborneHeight())
        onScreenDebug.add('w falling', self.falling)
        onScreenDebug.add('w isOnGround', self.lifter.isOnGround())
        onScreenDebug.add('w contact normal', self.lifter.getContactNormal().pPrintValues())
        onScreenDebug.add('w mayJump', self.mayJump)
        onScreenDebug.add('w impact', self.lifter.getImpactVelocity())
        onScreenDebug.add('w velocity', self.lifter.getVelocity())
        onScreenDebug.add('w isAirborne', self.isAirborne)
        onScreenDebug.add('w hasContact', self.lifter.hasContact())

    
    def handleAvatarControls(self, task):
        run = inputState.isSet('run')
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
                if 1:
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
        if self.controlsTask:
            self.controlsTask.remove()
        
        taskName = 'AvatarControls-%s' % (id(self),)
        self.controlsTask = taskMgr.add(self.handleAvatarControls, taskName, 25)
        self.isAirborne = 0
        self.mayJump = 1
        if self.physVelocityIndicator:
            if self.indicatorTask:
                self.indicatorTask.remove()
            
            self.indicatorTask = taskMgr.add(self.avatarPhysicsIndicator, 'AvatarControlsIndicator-%s' % (id(self),), 35)
        

    
    def disableAvatarControls(self):
        if self.controlsTask:
            self.controlsTask.remove()
            self.controlsTask = None
        
        if self.indicatorTask:
            self.indicatorTask.remove()
            self.indicatorTask = None
        
        if self.jumpDelayTask:
            self.jumpDelayTask.remove()
            self.jumpDelayTask = None
        


