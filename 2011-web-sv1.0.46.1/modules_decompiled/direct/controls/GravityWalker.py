# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\controls\GravityWalker.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase import DirectObject
from direct.controls.ControlManager import CollisionHandlerRayStart
from direct.showbase.InputStateGlobal import inputState
from direct.task.Task import Task
from pandac.PandaModules import *
import math

class GravityWalker(DirectObject.DirectObject):
    __module__ = __name__
    notify = directNotify.newCategory('GravityWalker')
    wantDebugIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    wantFloorSphere = base.config.GetBool('want-floor-sphere', 0)
    earlyEventSphere = base.config.GetBool('early-event-sphere', 0)
    DiagonalFactor = math.sqrt(2.0) / 2.0

    def __init__(self, gravity=64.348, standableGround=0.707, hardLandingForce=16.0, legacyLifter=False):
        DirectObject.DirectObject.__init__(self)
        self.__gravity = gravity
        self.__standableGround = standableGround
        self.__hardLandingForce = hardLandingForce
        self._legacyLifter = legacyLifter
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
        self.__oldPosDelta = Vec3(0)
        self.__oldDt = 0
        self.moving = 0
        self.speed = 0.0
        self.rotationSpeed = 0.0
        self.slideSpeed = 0.0
        self.vel = Vec3(0.0)
        self.collisionsActive = 0
        self.isAirborne = 0
        self.highMark = 0
        return

    def setWalkSpeed(self, forward, jump, reverse, rotate):
        self.avatarControlForwardSpeed = forward
        self.avatarControlJumpForce = jump
        self.avatarControlReverseSpeed = reverse
        self.avatarControlRotateSpeed = rotate

    def getSpeeds(self):
        return (
         self.speed, self.rotationSpeed, self.slideSpeed)

    def getIsAirborne(self):
        return self.isAirborne

    def setAvatar(self, avatar):
        self.avatar = avatar
        if avatar is not None:
            pass
        return

    def setupRay(self, bitmask, floorOffset, reach):
        cRay = CollisionRay(0.0, 0.0, CollisionHandlerRayStart, 0.0, 0.0, -1.0)
        cRayNode = CollisionNode('GW.cRayNode')
        cRayNode.addSolid(cRay)
        self.cRayNodePath = self.avatarNodePath.attachNewNode(cRayNode)
        cRayNode.setFromCollideMask(bitmask)
        cRayNode.setIntoCollideMask(BitMask32.allOff())
        self.lifter = CollisionHandlerGravity()
        self.lifter.setLegacyMode(self._legacyLifter)
        self.lifter.setGravity(self.__gravity)
        self.lifter.addInPattern('enter%in')
        self.lifter.addAgainPattern('again%in')
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
        if config.GetBool('want-fluid-pusher', 0):
            self.pusher = CollisionHandlerFluidPusher()
        else:
            self.pusher = CollisionHandlerPusher()
        self.pusher.addCollider(cSphereNodePath, self.avatarNodePath)
        self.cWallSphereNodePath = cSphereNodePath

    def setupEventSphere(self, bitmask, avatarRadius):
        self.avatarRadius = avatarRadius
        cSphere = CollisionSphere(0.0, 0.0, avatarRadius - 0.1, avatarRadius * 1.04)
        cSphere.setTangible(0)
        cSphereNode = CollisionNode('GW.cEventSphereNode')
        cSphereNode.addSolid(cSphere)
        cSphereNodePath = self.avatarNodePath.attachNewNode(cSphereNode)
        cSphereNode.setFromCollideMask(bitmask)
        cSphereNode.setIntoCollideMask(BitMask32.allOff())
        self.event = CollisionHandlerEvent()
        self.event.addInPattern('enter%in')
        self.event.addOutPattern('exit%in')
        self.cEventSphereNodePath = cSphereNodePath

    def setupFloorSphere(self, bitmask, avatarRadius):
        self.avatarRadius = avatarRadius
        cSphere = CollisionSphere(0.0, 0.0, avatarRadius, 0.01)
        cSphereNode = CollisionNode('GW.cFloorSphereNode')
        cSphereNode.addSolid(cSphere)
        cSphereNodePath = self.avatarNodePath.attachNewNode(cSphereNode)
        cSphereNode.setFromCollideMask(bitmask)
        cSphereNode.setIntoCollideMask(BitMask32.allOff())
        self.pusherFloorhandler = CollisionHandlerPusher()
        self.pusherFloor.addCollider(cSphereNodePath, self.avatarNodePath)
        self.cFloorSphereNodePath = cSphereNodePath

    def setWallBitMask(self, bitMask):
        self.wallBitmask = bitMask

    def setFloorBitMask(self, bitMask):
        self.floorBitmask = bitMask

    def swapFloorBitMask(self, oldMask, newMask):
        self.floorBitmask = self.floorBitmask & ~oldMask
        self.floorBitmask |= newMask
        if self.cRayNodePath and not self.cRayNodePath.isEmpty():
            self.cRayNodePath.node().setFromCollideMask(self.floorBitmask)

    def setGravity(self, gravity):
        self.__gravity = gravity
        self.lifter.setGravity(self.__gravity)

    def getGravity(self, gravity):
        return self.__gravity

    def initializeCollisions(self, collisionTraverser, avatarNodePath, avatarRadius=1.4, floorOffset=1.0, reach=1.0):
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

    def setCollisionsActive(self, active=1):
        if self.collisionsActive != active:
            self.collisionsActive = active
            self.oneTimeCollide()
            base.initShadowTrav()
            if active:
                self.avatarNodePath.setP(0.0)
                self.avatarNodePath.setR(0.0)
                self.cTrav.addCollider(self.cWallSphereNodePath, self.pusher)
                if self.wantFloorSphere:
                    self.cTrav.addCollider(self.cFloorSphereNodePath, self.pusherFloor)
                base.shadowTrav.addCollider(self.cRayNodePath, self.lifter)
                if self.earlyEventSphere:
                    self.cTrav.addCollider(self.cEventSphereNodePath, self.event)
                else:
                    base.shadowTrav.addCollider(self.cEventSphereNodePath, self.event)
            else:
                if hasattr(self, 'cTrav'):
                    self.cTrav.removeCollider(self.cWallSphereNodePath)
                    if self.wantFloorSphere:
                        self.cTrav.removeCollider(self.cFloorSphereNodePath)
                    self.cTrav.removeCollider(self.cEventSphereNodePath)
                base.shadowTrav.removeCollider(self.cEventSphereNodePath)
                base.shadowTrav.removeCollider(self.cRayNodePath)

    def getCollisionsActive(self):
        return self.collisionsActive

    def placeOnFloor(self):
        self.oneTimeCollide()
        self.avatarNodePath.setZ(self.avatarNodePath.getZ() - self.lifter.getAirborneHeight())

    def oneTimeCollide(self):
        if not hasattr(self, 'cWallSphereNodePath'):
            return
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

    def addBlastForce(self, vector):
        self.lifter.addVelocity(vector.length())

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
        slideLeft = inputState.isSet('slideLeft')
        slideRight = inputState.isSet('slideRight')
        jump = inputState.isSet('jump')
        if 'localAvatar' in __builtins__:
            if base.localAvatar and base.localAvatar.getAutoRun():
                forward = 1
                reverse = 0
        self.speed = forward and self.avatarControlForwardSpeed or reverse and -self.avatarControlReverseSpeed
        self.slideSpeed = reverse and slideLeft and -self.avatarControlReverseSpeed * 0.75 or reverse and slideRight and self.avatarControlReverseSpeed * 0.75 or slideLeft and -self.avatarControlForwardSpeed * 0.75 or slideRight and self.avatarControlForwardSpeed * 0.75
        self.rotationSpeed = not (slideLeft or slideRight) and (turnLeft and self.avatarControlRotateSpeed or turnRight and -self.avatarControlRotateSpeed)
        if self.speed and self.slideSpeed:
            self.speed *= GravityWalker.DiagonalFactor
            self.slideSpeed *= GravityWalker.DiagonalFactor
        debugRunning = inputState.isSet('debugRunning')
        if debugRunning:
            self.speed *= base.debugRunningMultiplier
            self.slideSpeed *= base.debugRunningMultiplier
            self.rotationSpeed *= 1.25
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
                    self.startJumpDelay(0.3)
                else:
                    messenger.send('jumpLand')
                    if impact < -5.0:
                        self.startJumpDelay(0.2)
            self.priorParent = Vec3.zero()
            if jump and self.mayJump:
                self.lifter.addVelocity(self.avatarControlJumpForce)
                messenger.send('jumpStart')
                self.isAirborne = 1
        else:
            if self.isAirborne == 0:
                pass
            self.isAirborne = 1
        self.__oldPosDelta = self.avatarNodePath.getPosDelta(render)
        self.__oldDt = ClockObject.getGlobalClock().getDt()
        dt = self.__oldDt
        self.moving = self.speed or self.slideSpeed or self.rotationSpeed or self.priorParent != Vec3.zero()
        if self.moving:
            distance = dt * self.speed
            slideDistance = dt * self.slideSpeed
            rotation = dt * self.rotationSpeed
            if distance or slideDistance or self.priorParent != Vec3.zero():
                rotMat = Mat3.rotateMatNormaxis(self.avatarNodePath.getH(), Vec3.up())
                if self.isAirborne:
                    forward = Vec3.forward()
                else:
                    contact = self.lifter.getContactNormal()
                    forward = contact.cross(Vec3.right())
                    forward.normalize()
                self.vel = Vec3(forward * distance)
                if slideDistance:
                    if self.isAirborne:
                        right = Vec3.right()
                    else:
                        right = forward.cross(contact)
                        right.normalize()
                    self.vel = Vec3(self.vel + right * slideDistance)
                self.vel = Vec3(rotMat.xform(self.vel))
                step = self.vel + self.priorParent * dt
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
        if self.__oldDt == 0:
            velocity = 0
        else:
            velocity = self.__oldPosDelta * (1.0 / self.__oldDt)
        self.priorParent = Vec3(velocity)

    def reset(self):
        self.lifter.setVelocity(0.0)
        self.priorParent = Vec3.zero()

    def getVelocity(self):
        return self.vel

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
        return

    def flushEventHandlers(self):
        if hasattr(self, 'cTrav'):
            self.pusher.flush()
            if self.wantFloorSphere:
                self.floorPusher.flush()
            self.event.flush()
        self.lifter.flush()

    def setCollisionRayHeight(self, height):
        cRayNode = self.cRayNodePath.node()
        cRayNode.removeSolid(0)
        cRay = CollisionRay(0.0, 0.0, height, 0.0, 0.0, -1.0)
        cRayNode.addSolid(cRay)