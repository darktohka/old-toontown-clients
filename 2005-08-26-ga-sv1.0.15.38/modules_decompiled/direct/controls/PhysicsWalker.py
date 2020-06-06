# File: P (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject
from pandac import PhysicsManager
import math

class PhysicsWalker(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('PhysicsWalker')
    wantDebugIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    wantAvatarPhysicsIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    useLifter = 0
    useHeightRay = 0
    
    def __init__(self, gravity = -32.173999999999999, standableGround = 0.70699999999999996, hardLandingForce = 16.0):
        DirectObject.DirectObject.__init__(self)
        self._PhysicsWalker__gravity = gravity
        self._PhysicsWalker__standableGround = standableGround
        self._PhysicsWalker__hardLandingForce = hardLandingForce
        self.needToDeltaPos = 0
        self.physVelocityIndicator = None
        self.avatarControlForwardSpeed = 0
        self.avatarControlJumpForce = 0
        self.avatarControlReverseSpeed = 0
        self.avatarControlRotateSpeed = 0
        self._PhysicsWalker__oldAirborneHeight = None
        self.getAirborneHeight = None
        self._PhysicsWalker__oldContact = None
        self._PhysicsWalker__oldPosDelta = Vec3(0)
        self._PhysicsWalker__oldDt = 0
        self._PhysicsWalker__speed = 0.0
        self._PhysicsWalker__rotationSpeed = 0.0
        self._PhysicsWalker__slideSpeed = 0.0
        self._PhysicsWalker__vel = Vec3(0.0)
        self.collisionsActive = 0
        self.isAirborne = 0
        self.highMark = 0

    
    def setWalkSpeed(self, forward, jump, reverse, rotate):
        self.avatarControlForwardSpeed = forward
        self.avatarControlJumpForce = jump
        self.avatarControlReverseSpeed = reverse
        self.avatarControlRotateSpeed = rotate

    
    def getSpeeds(self):
        return (self._PhysicsWalker__speed, self._PhysicsWalker__rotationSpeed)

    
    def setAvatar(self, avatar):
        self.avatar = avatar
        if avatar is not None:
            self.setupPhysics(avatar)
        

    
    def setupRay(self, floorBitmask, floorOffset):
        self.cRay = CollisionRay(0.0, 0.0, CollisionHandlerRayStart, 0.0, 0.0, -1.0)
        cRayNode = CollisionNode('PW.cRayNode')
        cRayNode.addSolid(self.cRay)
        self.cRayNodePath = self.avatarNodePath.attachNewNode(cRayNode)
        self.cRayBitMask = floorBitmask
        cRayNode.setFromCollideMask(self.cRayBitMask)
        cRayNode.setIntoCollideMask(BitMask32.allOff())
        if 0 or self.useLifter:
            self.lifter = CollisionHandlerFloor()
            self.lifter.setInPattern('enter%in')
            self.lifter.setOutPattern('exit%in')
            self.lifter.setOffset(floorOffset)
            self.lifter.addCollider(self.cRayNodePath, self.avatarNodePath)
        else:
            self.cRayQueue = CollisionHandlerQueue()
            self.cTrav.addCollider(self.cRayNodePath, self.cRayQueue)

    
    def determineHeight(self):
        if self.useLifter:
            height = self.avatarNodePath.getPos(self.cRayNodePath)
            return height.getZ() - self.floorOffset
        else:
            height = 0.0
            if self.cRayQueue.getNumEntries() != 0:
                self.cRayQueue.sortEntries()
                floorPoint = self.cRayQueue.getEntry(0).getFromIntersectionPoint()
                height = -floorPoint.getZ()
            
            self.cRayQueue.clearEntries()
            return height

    
    def setupSphere(self, bitmask, avatarRadius):
        self.avatarRadius = avatarRadius
        centerHeight = avatarRadius
        if self.useHeightRay:
            centerHeight *= 2.0
        
        self.cSphere = CollisionSphere(0.0, 0.0, centerHeight, avatarRadius)
        cSphereNode = CollisionNode('PW.cSphereNode')
        cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.avatarNodePath.attachNewNode(cSphereNode)
        self.cSphereBitMask = bitmask
        cSphereNode.setFromCollideMask(self.cSphereBitMask)
        cSphereNode.setIntoCollideMask(BitMask32.allOff())
        self.pusher = PhysicsCollisionHandler()
        self.pusher.setInPattern('enter%in')
        self.pusher.setOutPattern('exit%in')
        self.pusher.addCollider(self.cSphereNodePath, self.avatarNodePath)

    
    def setupPhysics(self, avatarNodePath):
        self.actorNode = ActorNode('PW physicsActor')
        self.actorNode.getPhysicsObject().setOriented(1)
        self.actorNode.getPhysical(0).setViscosity(0.10000000000000001)
        physicsActor = NodePath(self.actorNode)
        avatarNodePath.reparentTo(physicsActor)
        avatarNodePath.assign(physicsActor)
        self.phys = PhysicsManager.PhysicsManager()
        fn = ForceNode('gravity')
        fnp = NodePath(fn)
        fnp.reparentTo(render)
        gravity = LinearVectorForce(0.0, 0.0, self._PhysicsWalker__gravity)
        fn.addForce(gravity)
        self.phys.addLinearForce(gravity)
        self.gravity = gravity
        fn = ForceNode('priorParent')
        fnp = NodePath(fn)
        fnp.reparentTo(render)
        priorParent = LinearVectorForce(0.0, 0.0, 0.0)
        fn.addForce(priorParent)
        self.phys.addLinearForce(priorParent)
        self.priorParentNp = fnp
        self.priorParent = priorParent
        fn = ForceNode('viscosity')
        fnp = NodePath(fn)
        fnp.reparentTo(render)
        self.avatarViscosity = LinearFrictionForce(0.0, 1.0, 0)
        fn.addForce(self.avatarViscosity)
        self.phys.addLinearForce(self.avatarViscosity)
        self.phys.attachLinearIntegrator(LinearEulerIntegrator())
        self.phys.attachPhysicalnode(physicsActor.node())
        self.acForce = LinearVectorForce(0.0, 0.0, 0.0)
        fn = ForceNode('avatarControls')
        fnp = NodePath(fn)
        fnp.reparentTo(render)
        fn.addForce(self.acForce)
        self.phys.addLinearForce(self.acForce)
        return avatarNodePath

    
    def initializeCollisions(self, collisionTraverser, avatarNodePath, wallBitmask, floorBitmask, avatarRadius = 1.3999999999999999, floorOffset = 1.0, reach = 1.0):
        self.cTrav = collisionTraverser
        self.floorOffset = 7.0
        floorOffset = 7.0
        self.avatarNodePath = self.setupPhysics(avatarNodePath)
        if 0 or self.useHeightRay:
            self.setupRay(floorBitmask, 0.0)
        
        self.setupSphere(wallBitmask | floorBitmask, avatarRadius)
        self.setCollisionsActive(1)

    
    def setAirborneHeightFunc(self, getAirborneHeight):
        self.getAirborneHeight = getAirborneHeight

    
    def setAvatarPhysicsIndicator(self, indicator):
        self.cSphereNodePath.show()
        if indicator:
            change = render.attachNewNode('change')
            change.setScale(0.10000000000000001)
            indicator.reparentTo(change)
            indicatorNode = render.attachNewNode('physVelocityIndicator')
            indicatorNode.setPos(self.avatarNodePath, 0.0, 0.0, 6.0)
            indicatorNode.setColor(0.0, 0.0, 1.0, 1.0)
            change.reparentTo(indicatorNode)
            self.physVelocityIndicator = indicatorNode
            contactIndicatorNode = render.attachNewNode('physContactIndicator')
            contactIndicatorNode.setScale(0.25)
            contactIndicatorNode.setP(90.0)
            contactIndicatorNode.setPos(self.avatarNodePath, 0.0, 0.0, 5.0)
            contactIndicatorNode.setColor(1.0, 0.0, 0.0, 1.0)
            indicator.instanceTo(contactIndicatorNode)
            self.physContactIndicator = contactIndicatorNode
        else:
            print 'failed load of physics indicator'

    
    def avatarPhysicsIndicator(self, task):
        self.physVelocityIndicator.setPos(self.avatarNodePath, 0.0, 0.0, 6.0)
        physObject = self.actorNode.getPhysicsObject()
        a = physObject.getVelocity()
        self.physVelocityIndicator.setScale(math.sqrt(a.length()))
        a += self.physVelocityIndicator.getPos()
        self.physVelocityIndicator.lookAt(Point3(a))
        contact = self.actorNode.getContactVector()
        if contact == Vec3.zero():
            self.physContactIndicator.hide()
        else:
            self.physContactIndicator.show()
            self.physContactIndicator.setPos(self.avatarNodePath, 0.0, 0.0, 5.0)
            point = Point3(contact + self.physContactIndicator.getPos())
            self.physContactIndicator.lookAt(point)
        return Task.cont

    
    def deleteCollisions(self):
        del self.cTrav
        if self.useHeightRay:
            del self.cRayQueue
            self.cRayNodePath.removeNode()
            del self.cRayNodePath
        
        del self.cSphere
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath
        del self.pusher
        del self.getAirborneHeight

    
    def setCollisionsActive(self, active = 1):
        if self.collisionsActive != active:
            self.collisionsActive = active
            if active:
                self.cTrav.addCollider(self.cSphereNodePath, self.pusher)
                if self.useHeightRay:
                    if self.useLifter:
                        self.cTrav.addCollider(self.cRayNodePath, self.lifter)
                    else:
                        self.cTrav.addCollider(self.cRayNodePath, self.cRayQueue)
                
            else:
                self.cTrav.removeCollider(self.cSphereNodePath)
                if self.useHeightRay:
                    self.cTrav.removeCollider(self.cRayNodePath)
                
                self.oneTimeCollide()
        

    
    def getCollisionsActive(self):
        return self.collisionsActive

    
    def placeOnFloor(self):
        self.oneTimeCollide()
        self.avatarNodePath.setZ(self.avatarNodePath.getZ() - self.getAirborneHeight())

    
    def oneTimeCollide(self):
        tempCTrav = CollisionTraverser('oneTimeCollide')
        if self.useHeightRay:
            if self.useLifter:
                tempCTrav.addCollider(self.cRayNodePath, self.lifter)
            else:
                tempCTrav.addCollider(self.cRayNodePath, self.cRayQueue)
        
        tempCTrav.traverse(render)

    
    def displayDebugInfo(self):
        onScreenDebug.add('w controls', 'PhysicsWalker')
        if self.useLifter:
            onScreenDebug.add('w airborneHeight', self.lifter.getAirborneHeight())
            onScreenDebug.add('w isOnGround', self.lifter.isOnGround())
            onScreenDebug.add('w contact normal', self.lifter.getContactNormal().pPrintValues())
            onScreenDebug.add('w impact', self.lifter.getImpactVelocity())
            onScreenDebug.add('w velocity', self.lifter.getVelocity())
            onScreenDebug.add('w hasContact', self.lifter.hasContact())
        
        onScreenDebug.add('w isAirborne', self.isAirborne)

    
    def handleAvatarControls(self, task):
        physObject = self.actorNode.getPhysicsObject()
        contact = self.actorNode.getContactVector()
        if contact == Vec3.zero() and self.avatarNodePath.getZ() < -50.0:
            self.reset()
            self.avatarNodePath.setZ(50.0)
            messenger.send('walkerIsOutOfWorld', [
                self.avatarNodePath])
        
        if self.wantDebugIndicator:
            self.displayDebugInfo()
        
        forward = inputState.isSet('forward')
        reverse = inputState.isSet('reverse')
        turnLeft = inputState.isSet('turnLeft')
        turnRight = inputState.isSet('turnRight')
        slide = 0
        slideLeft = 0
        slideRight = 0
        jump = inputState.isSet('jump')
        if forward and self.avatarControlForwardSpeed and reverse:
            pass
        self._PhysicsWalker__speed = -(self.avatarControlReverseSpeed)
        avatarSlideSpeed = self.avatarControlForwardSpeed * 0.5
        if slideLeft and -avatarSlideSpeed and slideRight:
            pass
        self._PhysicsWalker__slideSpeed = avatarSlideSpeed
        if not slide:
            if turnLeft and self.avatarControlRotateSpeed and turnRight:
                pass
        self._PhysicsWalker__rotationSpeed = -(self.avatarControlRotateSpeed)
        dt = ClockObject.getGlobalClock().getDt()
        if self.needToDeltaPos:
            self.setPriorParentVector()
            self.needToDeltaPos = 0
        
        self._PhysicsWalker__oldPosDelta = self.avatarNodePath.getPosDelta(render)
        self._PhysicsWalker__oldDt = dt
        airborneHeight = self.getAirborneHeight()
        if airborneHeight > self.highMark:
            self.highMark = airborneHeight
        
        if 1:
            if airborneHeight > self.avatarRadius * 0.5 or physObject.getVelocity().getZ() > 0.0:
                self.isAirborne = 1
            elif self.isAirborne and physObject.getVelocity().getZ() <= 0.0:
                contactLength = contact.length()
                if contactLength > self._PhysicsWalker__hardLandingForce:
                    messenger.send('jumpHardLand')
                else:
                    messenger.send('jumpLand')
                self.priorParent.setVector(Vec3.zero())
                self.isAirborne = 0
            elif jump:
                messenger.send('jumpStart')
                jumpVec = Vec3.up()
                jumpVec *= self.avatarControlJumpForce
                physObject.addImpulse(Vec3(jumpVec))
                self.isAirborne = 1
            else:
                self.isAirborne = 0
        elif contact != Vec3.zero():
            contactLength = contact.length()
            contact.normalize()
            angle = contact.dot(Vec3.up())
            if angle > self._PhysicsWalker__standableGround:
                if self._PhysicsWalker__oldContact == Vec3.zero():
                    self.jumpCount -= 1
                    if contactLength > self._PhysicsWalker__hardLandingForce:
                        messenger.send('jumpHardLand')
                    else:
                        messenger.send('jumpLand')
                elif jump:
                    self.jumpCount += 1
                    messenger.send('jumpStart')
                    jump = Vec3(contact + Vec3.up())
                    jump.normalize()
                    jump *= self.avatarControlJumpForce
                    physObject.addImpulse(Vec3(jump))
                
            
        
        if contact != self._PhysicsWalker__oldContact:
            self._PhysicsWalker__oldContact = Vec3(contact)
        
        self._PhysicsWalker__oldAirborneHeight = airborneHeight
        moveToGround = Vec3.zero()
        if not (self.useHeightRay) or self.isAirborne:
            self.phys.doPhysics(dt)
        else:
            physObject.setVelocity(Vec3.zero())
            moveToGround = Vec3(0.0, 0.0, -self.determineHeight())
        if self._PhysicsWalker__speed and self._PhysicsWalker__slideSpeed and self._PhysicsWalker__rotationSpeed or moveToGround != Vec3.zero():
            distance = dt * self._PhysicsWalker__speed
            slideDistance = dt * self._PhysicsWalker__slideSpeed
            rotation = dt * self._PhysicsWalker__rotationSpeed
            self._PhysicsWalker__vel = Vec3(Vec3.forward() * distance + Vec3.right() * slideDistance)
            rotMat = Mat3.rotateMatNormaxis(self.avatarNodePath.getH(), Vec3.up())
            step = rotMat.xform(self._PhysicsWalker__vel)
            physObject.setPosition(Point3(physObject.getPosition() + step + moveToGround))
            o = physObject.getOrientation()
            r = LRotationf()
            r.setHpr(Vec3(rotation, 0.0, 0.0))
            physObject.setOrientation(o * r)
            self.actorNode.updateTransform()
            messenger.send('avatarMoving')
        else:
            self._PhysicsWalker__vel.set(0.0, 0.0, 0.0)
        self.actorNode.setContactVector(Vec3.zero())
        return Task.cont

    
    def doDeltaPos(self):
        self.needToDeltaPos = 1

    
    def setPriorParentVector(self):
        print 'self.__oldDt', self._PhysicsWalker__oldDt, 'self.__oldPosDelta', self._PhysicsWalker__oldPosDelta
        velocity = self._PhysicsWalker__oldPosDelta * (1 / self._PhysicsWalker__oldDt) * 4.0
        self.priorParent.setVector(Vec3(velocity))

    
    def reset(self):
        self.actorNode.getPhysicsObject().resetPosition(self.avatarNodePath.getPos())
        self.priorParent.setVector(Vec3.zero())
        self.highMark = 0
        self.actorNode.setContactVector(Vec3.zero())

    
    def enableAvatarControls(self):
        taskName = 'AvatarControls-%s' % (id(self),)
        taskMgr.remove(taskName)
        taskMgr.add(self.handleAvatarControls, taskName, 25)
        if self.physVelocityIndicator:
            taskMgr.add(self.avatarPhysicsIndicator, 'AvatarControlsIndicator%s' % (id(self),), 35)
        

    
    def disableAvatarControls(self):
        taskName = 'AvatarControls-%s' % (id(self),)
        taskMgr.remove(taskName)
        taskName = 'AvatarControlsIndicator%s' % (id(self),)
        taskMgr.remove(taskName)


