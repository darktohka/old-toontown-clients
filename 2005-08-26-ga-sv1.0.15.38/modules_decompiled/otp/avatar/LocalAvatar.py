# File: L (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.gui.DirectGui import *
from direct.showbase.PythonUtil import *
from direct.interval.IntervalGlobal import *
import Avatar
from direct.controls import ControlManager
import DistributedAvatar
from direct.task import Task
import PositionExaminer
from otp.otpbase import OTPGlobals
from otp.chat import ChatManager
import math
import string
import whrandom
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedSmoothNode
from direct.gui import DirectGuiGlobals
from otp.otpbase import OTPLocalizer
from direct.controls import GhostWalker
from direct.controls import GravityWalker
from direct.controls import NonPhysicsWalker
from direct.controls import PhysicsWalker

class LocalAvatar(DistributedAvatar.DistributedAvatar, DistributedSmoothNode.DistributedSmoothNode):
    notify = DirectNotifyGlobal.directNotify.newCategory('LocalAvatar')
    wantDevCameraPositions = base.config.GetBool('want-dev-camera-positions', 0)
    wantMouse = base.config.GetBool('want-mouse', 0)
    sleepTimeout = base.config.GetInt('sleep-timeout', 120)
    _LocalAvatar__enableMarkerPlacement = base.config.GetBool('place-markers', 0)
    acceptingNewFriends = base.config.GetBool('accepting-new-friends', 1)
    
    def __init__(self, cr, chatMgr):
        
        try:
            return None
        except:
            pass

        self.LocalAvatar_initialized = 1
        DistributedAvatar.DistributedAvatar.__init__(self, cr)
        DistributedSmoothNode.DistributedSmoothNode.__init__(self, cr)
        self.cTrav = CollisionTraverser('base.cTrav')
        base.cTrav = self.cTrav
        self.cTrav.setRespectPrevTransform(1)
        self.avatarControlsEnabled = 0
        self.controlManager = ControlManager.ControlManager()
        self.initializeCollisions()
        self.initializeSmartCamera()
        self.animMultiplier = 1.0
        self.runTimeout = 2.5
        self.customMessages = []
        self.chatMgr = chatMgr
        self.commonChatFlags = 0
        self.garbleChat = 1
        self.teleportAllowed = 1
        self.lockedDown = 0
        self.isPageUp = 0
        self.isPageDown = 0
        self.sleepFlag = 0
        self.isDisguised = 0
        self.movingFlag = 0
        self.lastNeedH = None
        self.accept('friendOnline', self._LocalAvatar__friendOnline)
        self.accept('friendOffline', self._LocalAvatar__friendOffline)
        self.accept('clickedWhisper', self._LocalAvatar__clickedWhisper)
        self.sleepCallback = None
        self.accept('wakeup', self.wakeUp)
        self.jumpLandAnimFixTask = None
        self.fov = OTPGlobals.DefaultCameraFov
        self.accept('avatarMoving', self.clearPageUpDown)
        self.nametag2dNormalContents = Nametag.CSpeech
        self.showNametag2d()
        self.setPickable(0)

    
    def useSwimControls(self):
        self.controlManager.use('swim', self)

    
    def useGhostControls(self):
        self.controlManager.use('ghost', self)

    
    def useWalkControls(self):
        self.controlManager.use('walk', self)

    
    def isLockedDown(self):
        return self.lockedDown

    
    def lock(self):
        if self.lockedDown == 1:
            self.notify.debug('lock() - already locked!')
        
        self.lockedDown = 1

    
    def unlock(self):
        if self.lockedDown == 0:
            self.notify.debug('unlock() - already unlocked!')
        
        self.lockedDown = 0

    
    def isInWater(self):
        return self.getZ(render) <= 0.0

    
    def isTeleportAllowed(self):
        if self.teleportAllowed:
            pass
        return not (self.isDisguised)

    
    def setTeleportAllowed(self, flag):
        self.teleportAllowed = flag
        self.refreshOnscreenButtons()

    
    def sendFriendsListEvent(self):
        messenger.send('wakeup')
        messenger.send('openFriendsList')

    
    def delete(self):
        
        try:
            return None
        except:
            self.LocalAvatar_deleted = 1

        taskMgr.remove('shadowReach')
        taskMgr.remove('posCamera')
        self.disableAvatarControls()
        self.stopTrackAnimToSpeed()
        self.stopUpdateSmartCamera()
        self.deleteCollisions()
        self.controlManager.delete()
        del self.controlManager
        self.positionExaminer.delete()
        del self.positionExaminer
        self.bFriendsList.destroy()
        del self.bFriendsList
        taskMgr.remove(self.uniqueName('walkReturnTask'))
        self.chatMgr.delete()
        del self.chatMgr
        del self.soundRun
        del self.soundWalk
        del self.soundWhisper
        self.ignoreAll()
        DistributedAvatar.DistributedAvatar.delete(self)

    
    def shadowReach(self, state):
        base.localAvatar.shadowPlacer.lifter.setReach(base.localAvatar.getAirborneHeight() + 4.0)
        return Task.cont

    
    def setupControls(self, avatarRadius = 1.3999999999999999, floorOffset = OTPGlobals.FloorOffset, reach = 4.0, wallBitmask = OTPGlobals.WallBitmask, floorBitmask = OTPGlobals.FloorBitmask, ghostBitmask = OTPGlobals.GhostBitmask):
        walkControls = GravityWalker.GravityWalker(gravity = -32.173999999999999 * 2.0)
        walkControls.setWallBitMask(wallBitmask)
        walkControls.setFloorBitMask(floorBitmask)
        walkControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        walkControls.setAirborneHeightFunc(self.getAirborneHeight)
        self.controlManager.add(walkControls, 'walk')
        swimControls = NonPhysicsWalker.NonPhysicsWalker()
        swimControls.setWallBitMask(wallBitmask)
        swimControls.setFloorBitMask(floorBitmask)
        swimControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        swimControls.setAirborneHeightFunc(self.getAirborneHeight)
        self.controlManager.add(swimControls, 'swim')
        ghostControls = GhostWalker.GhostWalker()
        ghostControls.setWallBitMask(ghostBitmask)
        ghostControls.setFloorBitMask(floorBitmask)
        ghostControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        ghostControls.setAirborneHeightFunc(self.getAirborneHeight)
        self.controlManager.add(ghostControls, 'ghost')
        self.controlManager.use('walk', self)
        self.controlManager.disable()

    
    def initializeCollisions(self):
        self.setupControls()
        taskMgr.add(self.shadowReach, 'shadowReach', priority = 33)
        self.ccTrav = CollisionTraverser('LocalAvatar.ccTrav')
        self.ccLine = CollisionSegment(0.0, 0.0, 0.0, 1.0, 0.0, 0.0)
        self.ccLineNode = CollisionNode('ccLineNode')
        self.ccLineNode.addSolid(self.ccLine)
        self.ccLineNodePath = self.attachNewNode(self.ccLineNode)
        self.ccLineBitMask = OTPGlobals.CameraBitmask
        self.ccLineNode.setFromCollideMask(self.ccLineBitMask)
        self.ccLineNode.setIntoCollideMask(BitMask32.allOff())
        self.camCollisionQueue = CollisionHandlerQueue()
        self.ccTrav.addCollider(self.ccLineNodePath, self.camCollisionQueue)
        self.ccSphere = CollisionSphere(0, 0, 0, 1)
        self.ccSphereNode = CollisionNode('ccSphereNode')
        self.ccSphereNode.addSolid(self.ccSphere)
        self.ccSphereNodePath = base.camera.attachNewNode(self.ccSphereNode)
        self.ccSphereNode.setFromCollideMask(OTPGlobals.CameraBitmask)
        self.ccSphereNode.setIntoCollideMask(BitMask32.allOff())
        self.camPusher = CollisionHandlerPusher()
        self.camPusher.addCollider(self.ccSphereNodePath, base.camera)
        self.camPusher.setCenter(self)
        self.ccPusherTrav = CollisionTraverser('LocalAvatar.ccPusherTrav')
        self.ccSphere2 = self.ccSphere
        self.ccSphereNode2 = CollisionNode('ccSphereNode2')
        self.ccSphereNode2.addSolid(self.ccSphere2)
        self.ccSphereNodePath2 = base.camera.attachNewNode(self.ccSphereNode2)
        self.ccSphereNode2.setFromCollideMask(OTPGlobals.CameraBitmask)
        self.ccSphereNode2.setIntoCollideMask(BitMask32.allOff())
        self.camPusher2 = CollisionHandlerPusher()
        self.ccPusherTrav.addCollider(self.ccSphereNodePath2, self.camPusher2)
        self.camPusher2.addCollider(self.ccSphereNodePath2, base.camera)
        self.camPusher2.setCenter(self)
        self.camFloorRayNode = self.attachNewNode('camFloorRayNode')
        self.ccRay = CollisionRay(0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
        self.ccRayNode = CollisionNode('ccRayNode')
        self.ccRayNode.addSolid(self.ccRay)
        self.ccRayNodePath = self.camFloorRayNode.attachNewNode(self.ccRayNode)
        self.ccRayBitMask = OTPGlobals.FloorBitmask
        self.ccRayNode.setFromCollideMask(self.ccRayBitMask)
        self.ccRayNode.setIntoCollideMask(BitMask32.allOff())
        self.ccTravFloor = CollisionTraverser('LocalAvatar.ccTravFloor')
        self.camFloorCollisionQueue = CollisionHandlerQueue()
        self.ccTravFloor.addCollider(self.ccRayNodePath, self.camFloorCollisionQueue)
        self.ccTravOnFloor = CollisionTraverser('LocalAvatar.ccTravOnFloor')
        self.ccRay2 = CollisionRay(0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
        self.ccRay2Node = CollisionNode('ccRay2Node')
        self.ccRay2Node.addSolid(self.ccRay2)
        self.ccRay2NodePath = self.camFloorRayNode.attachNewNode(self.ccRay2Node)
        self.ccRay2BitMask = OTPGlobals.FloorBitmask
        self.ccRay2Node.setFromCollideMask(self.ccRay2BitMask)
        self.ccRay2Node.setIntoCollideMask(BitMask32.allOff())
        self.ccRay2MoveNodePath = hidden.attachNewNode('ccRay2MoveNode')
        self.camFloorCollisionBroadcaster = CollisionHandlerFloor()
        self.camFloorCollisionBroadcaster.setInPattern('on-floor')
        self.camFloorCollisionBroadcaster.setOutPattern('off-floor')
        self.camFloorCollisionBroadcaster.addCollider(self.ccRay2NodePath, self.ccRay2MoveNodePath)

    
    def deleteCollisions(self):
        self.controlManager.deleteCollisions()
        self.ignore('entero157')
        del self.cTrav
        del self.ccTrav
        del self.ccLine
        del self.ccLineNode
        self.ccLineNodePath.removeNode()
        del self.ccLineNodePath
        del self.camCollisionQueue
        del self.ccRay
        del self.ccRayNode
        self.ccRayNodePath.removeNode()
        del self.ccRayNodePath
        del self.ccRay2
        del self.ccRay2Node
        self.ccRay2NodePath.removeNode()
        del self.ccRay2NodePath
        self.ccRay2MoveNodePath.removeNode()
        del self.ccRay2MoveNodePath
        del self.ccTravOnFloor
        del self.ccTravFloor
        del self.camFloorCollisionQueue
        del self.camFloorCollisionBroadcaster
        del self.ccSphere
        del self.ccSphereNode
        self.ccSphereNodePath.removeNode()
        del self.ccSphereNodePath
        del self.camPusher
        del self.ccPusherTrav
        del self.ccSphere2
        del self.ccSphereNode2
        self.ccSphereNodePath2.removeNode()
        del self.ccSphereNodePath2
        del self.camPusher2

    
    def collisionsOff(self):
        self.controlManager.collisionsOff()

    
    def collisionsOn(self):
        self.controlManager.collisionsOn()

    
    def recalcCameraSphere(self):
        nearPlaneDist = base.camLens.getNear()
        hFov = base.camLens.getHfov()
        vFov = base.camLens.getVfov()
        hOff = nearPlaneDist * math.tan(deg2Rad(hFov / 2.0))
        vOff = nearPlaneDist * math.tan(deg2Rad(vFov / 2.0))
        camPnts = [
            Point3(hOff, nearPlaneDist, vOff),
            Point3(-hOff, nearPlaneDist, vOff),
            Point3(hOff, nearPlaneDist, -vOff),
            Point3(-hOff, nearPlaneDist, -vOff),
            Point3(0.0, 0.0, 0.0)]
        avgPnt = Point3(0.0, 0.0, 0.0)
        for camPnt in camPnts:
            avgPnt = avgPnt + camPnt
        
        avgPnt = avgPnt / len(camPnts)
        sphereRadius = 0.0
        for camPnt in camPnts:
            dist = Vec3(camPnt - avgPnt).length()
            if dist > sphereRadius:
                sphereRadius = dist
            
        
        avgPnt = Point3(avgPnt)
        self.ccSphereNodePath.setPos(avgPnt)
        self.ccSphereNodePath2.setPos(avgPnt)
        self.ccSphere.setRadius(sphereRadius)

    
    def putCameraFloorRayOnAvatar(self):
        self.camFloorRayNode.setPos(self, 0, 0, 5)

    
    def putCameraFloorRayOnCamera(self):
        self.camFloorRayNode.setPos(self.ccSphereNodePath, 0, 0, 0)

    
    def attachCamera(self):
        pos = self.getPos()
        hpr = self.getHpr()
        camera.reparentTo(self)
        base.enableMouse()
        base.setMouseOnNode(self.node())
        self.ignoreMouse = not (self.wantMouse)
        self.setWalkSpeedNormal()

    
    def detachCamera(self):
        base.disableMouse()

    
    def setupAnimationEvents(self):
        
        def jumpStart(self):
            if not (self.sleepFlag) and self.hp > 0:
                self.b_setAnimState('jumpAirborne', 1.0)
                if self.jumpLandAnimFixTask:
                    self.jumpLandAnimFixTask.remove()
                    self.jumpLandAnimFixTask = None
                
            

        
        def jumpLandAnimFix(self, jumpTime):
            if self.playingAnim != 'run' and self.playingAnim != 'walk':
                
                def returnToWalk(state):
                    if self.sleepFlag:
                        state = 'Sleep'
                    elif self.hp > 0:
                        state = 'Happy'
                    else:
                        state = 'Sad'
                    self.b_setAnimState(state, 1.0)
                    return Task.done

                return taskMgr.doMethodLater(jumpTime, returnToWalk, self.uniqueName('walkReturnTask'))
            

        
        def jumpHardLand(self):
            if self.allowHardLand():
                self.b_setAnimState('jumpLand', 1.0)
                if self.jumpLandAnimFixTask:
                    self.jumpLandAnimFixTask.remove()
                    self.jumpLandAnimFixTask = None
                
                self.jumpLandAnimFixTask = jumpLandAnimFix(self, 1.0)
            
            self.d_broadcastPosHpr()

        
        def jumpLand(self):
            self.jumpLandAnimFixTask = jumpLandAnimFix(self, 0.01)
            self.d_broadcastPosHpr()

        self.accept('jumpStart', jumpStart, [
            self])
        self.accept('jumpHardLand', jumpHardLand, [
            self])
        self.accept('jumpLand', jumpLand, [
            self])

    
    def allowHardLand(self):
        if not (self.sleepFlag):
            pass
        return self.hp > 0

    
    def enableSmartCameraViews(self):
        self.accept('tab', self.nextCameraPos, [
            1])
        self.accept('shift-tab', self.nextCameraPos, [
            0])
        self.accept('page_up', self.pageUp)
        self.accept('page_down', self.pageDown)

    
    def disableSmartCameraViews(self):
        self.ignore('tab')
        self.ignore('shift-tab')
        self.ignore('page_up')
        self.ignore('page_down')
        self.ignore('page_down-up')

    
    def enableAvatarControls(self):
        if self.avatarControlsEnabled:
            return None
        
        self.avatarControlsEnabled = 1
        self.setupAnimationEvents()
        self.enableSmartCameraViews()
        self.controlManager.enable()

    
    def disableAvatarControls(self):
        if not (self.avatarControlsEnabled):
            return None
        
        self.avatarControlsEnabled = 0
        self.disableSmartCameraViews()
        self.controlManager.disable()
        self.clearPageUpDown()

    
    def setWalkSpeedNormal(self):
        self.controlManager.setSpeeds(OTPGlobals.ToonForwardSpeed, OTPGlobals.ToonJumpForce, OTPGlobals.ToonReverseSpeed, OTPGlobals.ToonRotateSpeed)

    
    def setWalkSpeedSlow(self):
        self.controlManager.setSpeeds(OTPGlobals.ToonForwardSlowSpeed, OTPGlobals.ToonJumpSlowForce, OTPGlobals.ToonReverseSlowSpeed, OTPGlobals.ToonRotateSlowSpeed)

    
    def pageUp(self):
        if not (self.isPageUp):
            self.isPageDown = 0
            self.isPageUp = 1
            self.lerpCameraFov(70, 0.59999999999999998)
            self.setCameraPositionByIndex(self.cameraIndex)
        else:
            self.clearPageUpDown()

    
    def pageDown(self):
        if not (self.isPageDown):
            self.isPageUp = 0
            self.isPageDown = 1
            self.lerpCameraFov(70, 0.59999999999999998)
            self.setCameraPositionByIndex(self.cameraIndex)
        else:
            self.clearPageUpDown()

    
    def clearPageUpDown(self):
        if self.isPageDown or self.isPageUp:
            self.lerpCameraFov(self.fov, 0.59999999999999998)
            self.isPageDown = 0
            self.isPageUp = 0
            self.setCameraPositionByIndex(self.cameraIndex)
        

    
    def nextCameraPos(self, forward):
        self._LocalAvatar__cameraHasBeenMoved = 1
        if forward:
            self.cameraIndex += 1
            if self.cameraIndex > len(self.cameraPositions) - 1:
                self.cameraIndex = 0
            
        else:
            self.cameraIndex -= 1
            if self.cameraIndex < 0:
                self.cameraIndex = len(self.cameraPositions) - 1
            
        self.setCameraPositionByIndex(self.cameraIndex)

    
    def initCameraPositions(self):
        camHeight = self.getClampedAvatarHeight()
        heightScaleFactor = camHeight * 0.33333333329999998
        defLookAt = Point3(0.0, 1.5, camHeight)
        scXoffset = 3.0
        scPosition = (Point3(scXoffset - 1, -10.0, camHeight + 5.0), Point3(scXoffset, 2.0, camHeight))
        self.cameraPositions = [
            (Point3(0.0, -9.0 * heightScaleFactor, camHeight), defLookAt, Point3(0.0, camHeight, camHeight * 4.0), Point3(0.0, camHeight, camHeight * -1.0), 0),
            (Point3(0.0, 0.5, camHeight), defLookAt, Point3(0.0, camHeight, camHeight * 1.3300000000000001), Point3(0.0, camHeight, camHeight * 0.66000000000000003), 1),
            (Point3(5.7000000000000002 * heightScaleFactor, 7.6500000000000004 * heightScaleFactor, camHeight + 2.0), Point3(0.0, 1.0, camHeight), Point3(0.0, 1.0, camHeight * 4.0), Point3(0.0, 1.0, camHeight * -1.0), 0),
            (Point3(0.0, -24.0 * heightScaleFactor, camHeight + 4.0), defLookAt, Point3(0.0, 1.5, camHeight * 4.0), Point3(0.0, 1.5, camHeight * -1.0), 0),
            (Point3(0.0, -12.0 * heightScaleFactor, camHeight + 4.0), defLookAt, Point3(0.0, 1.5, camHeight * 4.0), Point3(0.0, 1.5, camHeight * -1.0), 0)] + self.auxCameraPositions
        if self.wantDevCameraPositions:
            self.cameraPositions += [
                (Point3(0.0, 0.0, camHeight * 3), Point3(0.0, 0.0, 0.0), Point3(0.0, camHeight * 2, 0.0), Point3(0.0, -camHeight * 2, 0.0), 1),
                (Point3(camHeight * 3, 0.0, camHeight), Point3(0.0, 0.0, camHeight), Point3(0.0, camHeight, camHeight * 1.1000000000000001), Point3(0.0, camHeight, camHeight * 0.90000000000000002), 1),
                (Point3(camHeight * 3, 0.0, 0.0), Point3(0.0, 0.0, camHeight), Point3(0.0, camHeight, camHeight * 1.1000000000000001), Point3(0.0, camHeight, camHeight * 0.90000000000000002), 1),
                (Point3(-camHeight * 3, 0.0, camHeight), Point3(0.0, 0.0, camHeight), Point3(0.0, camHeight, camHeight * 1.1000000000000001), Point3(0.0, camHeight, camHeight * 0.90000000000000002), 1),
                (Point3(0.0, -60, 60), defLookAt + Point3(0, 15, 0), defLookAt + Point3(0, 15, 0), defLookAt + Point3(0, 15, 0), 1),
                (Point3(0.0, -20, 20), defLookAt + Point3(0, 5, 0), defLookAt + Point3(0, 5, 0), defLookAt + Point3(0, 5, 0), 1)]
        

    
    def addCameraPosition(self, camPos = None):
        if camPos == None:
            lookAtNP = self.attachNewNode('lookAt')
            lookAtNP.setPos(base.cam, 0, 1, 0)
            lookAtPos = lookAtNP.getPos()
            camHeight = self.getClampedAvatarHeight()
            camPos = (base.cam.getPos(self), lookAtPos, Point3(0.0, 1.5, camHeight * 4.0), Point3(0.0, 1.5, camHeight * -1.0), 1)
            lookAtNP.removeNode()
        
        self.auxCameraPositions.append(camPos)
        self.cameraPositions.append(camPos)

    
    def resetCameraPosition(self):
        self.cameraIndex = 0
        self.setCameraPositionByIndex(self.cameraIndex)

    
    def removeCameraPosition(self):
        if len(self.cameraPositions) > 1:
            camPos = self.cameraPositions[self.cameraIndex]
            if camPos in self.auxCameraPositions:
                self.auxCameraPositions.remove(camPos)
            
            if camPos in self.cameraPositions:
                self.cameraPositions.remove(camPos)
            
            self.nextCameraPos(1)
        

    
    def printCameraPositions(self):
        print '['
        for i in range(len(self.cameraPositions)):
            self.printCameraPosition(i)
            print ','
        
        print ']'

    
    def printCameraPosition(self, index):
        cp = self.cameraPositions[index]
        print '(Point3(%0.2f, %0.2f, %0.2f),' % (cp[0][0], cp[0][1], cp[0][2])
        print 'Point3(%0.2f, %0.2f, %0.2f),' % (cp[1][0], cp[1][1], cp[1][2])
        print 'Point3(%0.2f, %0.2f, %0.2f),' % (cp[2][0], cp[2][1], cp[2][2])
        print 'Point3(%0.2f, %0.2f, %0.2f),' % (cp[3][0], cp[3][1], cp[3][2])
        print '%d,' % cp[4]
        print ')'
def posCamera(self, lerp, time):
        if not lerp:
            self.positionCameraWithPusher(self.getCompromiseCameraPos(), self.getLookAtPoint())
        else:
            camPos = self.getCompromiseCameraPos()
            savePos = camera.getPos()
            saveHpr = camera.getHpr()
            self.positionCameraWithPusher(camPos, self.getLookAtPoint())
            x = camPos[0]
            y = camPos[1]
            z = camPos[2]
            destHpr = camera.getHpr()
            h = destHpr[0]
            p = destHpr[1]
            r = destHpr[2]
            camera.setPos(savePos)
            camera.setHpr(saveHpr)
            taskMgr.remove('posCamera')
            camera.lerpPosHpr(x, y, z, h, p, r, time, task = 'posCamera')

    
    def getClampedAvatarHeight(self):
        return max(self.getHeight(), 3.0)

    
    def getVisibilityPoint(self):
        return Point3(0.0, 0.0, self.getHeight())

    
    def setLookAtPoint(self, la):
        self._LocalAvatar__curLookAt = Point3(la)

    
    def getLookAtPoint(self):
        return Point3(self._LocalAvatar__curLookAt)

    
    def setIdealCameraPos(self, pos):
        self._LocalAvatar__idealCameraPos = Point3(pos)
        self.updateSmartCameraCollisionLineSegment()

    
    def getIdealCameraPos(self):
        return Point3(self._LocalAvatar__idealCameraPos)

    
    def setCameraPositionByIndex(self, index):
        self.notify.debug('switching to camera position %s' % index)
        self.setCameraSettings(self.cameraPositions[index])

    
    def setCameraPosForPetInteraction(self):
        height = self.getClampedAvatarHeight()
        point = Point3(height * (7 / 3.0), height * (-7 / 3.0), height)
        self.prevIdealPos = self.getIdealCameraPos()
        self.setIdealCameraPos(point)
        self.posCamera(1, 0.69999999999999996)

    
    def unsetCameraPosForPetInteraction(self):
        self.setIdealCameraPos(self.prevIdealPos)
        del self.prevIdealPos
        self.posCamera(1, 0.69999999999999996)

    
    def setCameraSettings(self, camSettings):
        self.setIdealCameraPos(camSettings[0])
        if self.isPageUp and self.isPageDown and not (self.isPageUp) and not (self.isPageDown):
            self._LocalAvatar__cameraHasBeenMoved = 1
            self.setLookAtPoint(camSettings[1])
        elif self.isPageUp:
            self._LocalAvatar__cameraHasBeenMoved = 1
            self.setLookAtPoint(camSettings[2])
        elif self.isPageDown:
            self._LocalAvatar__cameraHasBeenMoved = 1
            self.setLookAtPoint(camSettings[3])
        else:
            self.notify.error('This case should be impossible.')
        self._LocalAvatar__disableSmartCam = camSettings[4]
        if self._LocalAvatar__disableSmartCam:
            self.putCameraFloorRayOnAvatar()
            self.cameraZOffset = 0.0
        

    
    def getCompromiseCameraPos(self):
        if self._LocalAvatar__idealCameraObstructed == 0:
            compromisePos = self.getIdealCameraPos()
        else:
            visPnt = self.getVisibilityPoint()
            idealPos = self.getIdealCameraPos()
            distance = Vec3(idealPos - visPnt).length()
            ratio = self.closestObstructionDistance / distance
            compromisePos = idealPos * ratio + visPnt * (1 - ratio)
            liftMult = 1.0 - ratio * ratio
            compromisePos = Point3(compromisePos[0], compromisePos[1], compromisePos[2] + self.getHeight() * 0.40000000000000002 * liftMult)
        compromisePos.setZ(compromisePos[2] + self.cameraZOffset)
        return compromisePos

    
    def updateSmartCameraCollisionLineSegment(self):
        pointB = self.getIdealCameraPos()
        pointA = self.getVisibilityPoint()
        vectorAB = Vec3(pointB - pointA)
        lengthAB = vectorAB.length()
        if lengthAB > 0.001:
            self.ccLine.setPointA(pointA)
            self.ccLine.setPointB(pointB)
        

    
    def initializeSmartCamera(self):
        self._LocalAvatar__idealCameraObstructed = 0
        self.closestObstructionDistance = 0.0
        self.cameraIndex = 0
        self.auxCameraPositions = []
        self.cameraZOffset = 0.0
        self._LocalAvatar__onLevelGround = 0
        self._LocalAvatar__camCollCanMove = 0
        self._LocalAvatar__geom = render
        self._LocalAvatar__disableSmartCam = 0

    
    def setOnLevelGround(self, flag):
        self._LocalAvatar__onLevelGround = flag

    
    def setCameraCollisionsCanMove(self, flag):
        self._LocalAvatar__camCollCanMove = flag

    
    def setGeom(self, geom):
        self._LocalAvatar__geom = geom

    
    def startUpdateSmartCamera(self):
        self._LocalAvatar__floorDetected = 0
        self._LocalAvatar__cameraHasBeenMoved = 0
        self.recalcCameraSphere()
        self.initCameraPositions()
        self.setCameraPositionByIndex(self.cameraIndex)
        self.posCamera(0, 0.0)
        self._LocalAvatar__instantaneousCamPos = camera.getPos()
        self.cTrav.addCollider(self.ccSphereNodePath, self.camPusher)
        self.ccTravOnFloor.addCollider(self.ccRay2NodePath, self.camFloorCollisionBroadcaster)
        self._LocalAvatar__lastPosWrtRender = camera.getPos(render)
        self._LocalAvatar__lastHprWrtRender = camera.getHpr(render)
        taskName = self.taskName('updateSmartCamera')
        taskMgr.remove(taskName)
        taskMgr.add(self.updateSmartCamera, taskName, priority = 47)

    
    def stopUpdateSmartCamera(self):
        self.cTrav.removeCollider(self.ccSphereNodePath)
        self.ccTravOnFloor.removeCollider(self.ccRay2NodePath)
        if not base.localAvatar.isEmpty():
            self.putCameraFloorRayOnAvatar()
        
        taskName = self.taskName('updateSmartCamera')
        taskMgr.remove(taskName)

    
    def updateSmartCamera(self, task):
        if not (self._LocalAvatar__camCollCanMove) and not (self._LocalAvatar__cameraHasBeenMoved):
            if self._LocalAvatar__lastPosWrtRender == camera.getPos(render):
                if self._LocalAvatar__lastHprWrtRender == camera.getHpr(render):
                    return Task.cont
                
            
        
        self._LocalAvatar__cameraHasBeenMoved = 0
        self._LocalAvatar__lastPosWrtRender = camera.getPos(render)
        self._LocalAvatar__lastHprWrtRender = camera.getHpr(render)
        self._LocalAvatar__idealCameraObstructed = 0
        if not (self._LocalAvatar__disableSmartCam):
            self.ccTrav.traverse(self._LocalAvatar__geom)
            if self.camCollisionQueue.getNumEntries() > 0:
                self.camCollisionQueue.sortEntries()
                self.handleCameraObstruction(self.camCollisionQueue.getEntry(0))
            
            if not (self._LocalAvatar__onLevelGround):
                self.handleCameraFloorInteraction()
            
        
        if not (self._LocalAvatar__idealCameraObstructed):
            self.nudgeCamera()
        
        if not (self._LocalAvatar__disableSmartCam):
            self.ccPusherTrav.traverse(self._LocalAvatar__geom)
            self.putCameraFloorRayOnCamera()
        
        self.ccTravOnFloor.traverse(self._LocalAvatar__geom)
        return Task.cont

    
    def positionCameraWithPusher(self, pos, lookAt):
        camera.setPos(pos)
        self.ccPusherTrav.traverse(self._LocalAvatar__geom)
        camera.lookAt(lookAt)

    
    def nudgeCamera(self):
        CLOSE_ENOUGH = 0.10000000000000001
        curCamPos = self._LocalAvatar__instantaneousCamPos
        curCamHpr = camera.getHpr()
        targetCamPos = self.getCompromiseCameraPos()
        targetCamLookAt = self.getLookAtPoint()
        posDone = 0
        if Vec3(curCamPos - targetCamPos).length() <= CLOSE_ENOUGH:
            camera.setPos(targetCamPos)
            posDone = 1
        
        camera.setPos(targetCamPos)
        camera.lookAt(targetCamLookAt)
        targetCamHpr = camera.getHpr()
        hprDone = 0
        if Vec3(curCamHpr - targetCamHpr).length() <= CLOSE_ENOUGH:
            hprDone = 1
        
        if posDone and hprDone:
            return None
        
        lerpRatio = 0.14999999999999999
        lerpRatio = 1 - pow(1 - lerpRatio, globalClock.getDt() * 30.0)
        self._LocalAvatar__instantaneousCamPos = targetCamPos * lerpRatio + curCamPos * (1 - lerpRatio)
        if self._LocalAvatar__disableSmartCam or not (self._LocalAvatar__idealCameraObstructed):
            newHpr = targetCamHpr * lerpRatio + curCamHpr * (1 - lerpRatio)
        else:
            newHpr = targetCamHpr
        camera.setPos(self._LocalAvatar__instantaneousCamPos)
        camera.setHpr(newHpr)

    
    def popCameraToDest(self):
        newCamPos = self.getCompromiseCameraPos()
        newCamLookAt = self.getLookAtPoint()
        self.positionCameraWithPusher(newCamPos, newCamLookAt)
        self._LocalAvatar__instantaneousCamPos = camera.getPos()

    
    def handleCameraObstruction(self, camObstrCollisionEntry):
        collisionPoint = camObstrCollisionEntry.getSurfacePoint(self.ccLineNodePath)
        collisionVec = Vec3(collisionPoint - self.ccLine.getPointA())
        distance = collisionVec.length()
        self._LocalAvatar__idealCameraObstructed = 1
        self.closestObstructionDistance = distance
        self.popCameraToDest()

    
    def handleCameraFloorInteraction(self):
        self.putCameraFloorRayOnCamera()
        self.ccTravFloor.traverse(self._LocalAvatar__geom)
        if self._LocalAvatar__onLevelGround:
            return None
        
        if self.camFloorCollisionQueue.getNumEntries() == 0:
            return None
        
        self.camFloorCollisionQueue.sortEntries()
        camObstrCollisionEntry = self.camFloorCollisionQueue.getEntry(0)
        camHeightFromFloor = camObstrCollisionEntry.getSurfacePoint(self.ccRayNodePath)[2]
        self.cameraZOffset = camera.getPos()[2] + camHeightFromFloor
        if self.cameraZOffset < 0:
            self.cameraZOffset = 0
        
        if self._LocalAvatar__floorDetected == 0:
            self._LocalAvatar__floorDetected = 1
            self.popCameraToDest()
        

    
    def lerpCameraFov(self, fov, time):
        taskMgr.remove('cam-fov-lerp-play')
        oldFov = base.camLens.getHfov()
        if abs(fov - oldFov) > 0.10000000000000001:
            
            def setCamFov(fov):
                base.camLens.setFov(fov)

            self.camLerpInterval = LerpFunctionInterval(setCamFov, fromData = oldFov, toData = fov, duration = time, name = 'cam-fov-lerp')
            self.camLerpInterval.start()
        

    
    def setCameraFov(self, fov):
        self.fov = fov
        if not self.isPageDown:
            pass
        if not (self.isPageUp):
            base.camLens.setFov(self.fov)
        

    
    def gotoNode(self, node, eyeHeight = 3):
        possiblePoints = (Point3(3, 6, 0), Point3(-3, 6, 0), Point3(6, 6, 0), Point3(-6, 6, 0), Point3(3, 9, 0), Point3(-3, 9, 0), Point3(6, 9, 0), Point3(-6, 9, 0), Point3(9, 9, 0), Point3(-9, 9, 0), Point3(6, 0, 0), Point3(-6, 0, 0), Point3(6, 3, 0), Point3(-6, 3, 0), Point3(9, 9, 0), Point3(-9, 9, 0), Point3(0, 12, 0), Point3(3, 12, 0), Point3(-3, 12, 0), Point3(6, 12, 0), Point3(-6, 12, 0), Point3(9, 12, 0), Point3(-9, 12, 0), Point3(0, -6, 0), Point3(-3, -6, 0), Point3(0, -9, 0), Point3(-6, -9, 0))
        for point in possiblePoints:
            pos = self.positionExaminer.consider(node, point, eyeHeight)
            if pos:
                self.setPos(node, pos)
                self.lookAt(node)
                self.setHpr(self.getH() + whrandom.choice((-10, 10)), 0, 0)
                return None
            
        
        self.setPos(node, 0, 0, 0)

    
    def setCustomMessages(self, customMessages):
        self.customMessages = customMessages
        messenger.send('customMessagesChanged')

    
    def displayWhisper(self, fromId, chatString, whisperType):
        sender = None
        sfx = self.soundWhisper
        if whisperType == WhisperPopup.WTNormal or whisperType == WhisperPopup.WTQuickTalker:
            if sender == None:
                return None
            
            chatString = sender.getName() + ': ' + chatString
        
        whisper = WhisperPopup(chatString, OTPGlobals.getInterfaceFont(), whisperType)
        if sender != None:
            whisper.setClickable(sender.getName(), fromId)
        
        whisper.manage(base.marginManager)
        base.playSfx(sfx)

    
    def setAnimMultiplier(self, value):
        self.animMultiplier = value

    
    def getAnimMultiplier(self):
        return self.animMultiplier

    
    def enableRun(self):
        self.accept('arrow_up', self.startRunWatch)
        self.accept('arrow_up-up', self.stopRunWatch)
        self.accept('control-arrow_up', self.startRunWatch)
        self.accept('control-arrow_up-up', self.stopRunWatch)
        self.accept('alt-arrow_up', self.startRunWatch)
        self.accept('alt-arrow_up-up', self.stopRunWatch)
        self.accept('shift-arrow_up', self.startRunWatch)
        self.accept('shift-arrow_up-up', self.stopRunWatch)

    
    def disableRun(self):
        self.ignore('arrow_up')
        self.ignore('arrow_up-up')
        self.ignore('control-arrow_up')
        self.ignore('control-arrow_up-up')
        self.ignore('alt-arrow_up')
        self.ignore('alt-arrow_up-up')
        self.ignore('shift-arrow_up')
        self.ignore('shift-arrow_up-up')

    
    def startRunWatch(self):
        
        def setRun(ignored):
            messenger.send('running-on')

        taskMgr.doMethodLater(self.runTimeout, setRun, self.uniqueName('runWatch'))
        return Task.cont

    
    def stopRunWatch(self):
        taskMgr.remove(self.uniqueName('runWatch'))
        messenger.send('running-off')
        return Task.cont

    
    def runSound(self):
        self.soundWalk.stop()
        base.playSfx(self.soundRun, looping = 1)

    
    def walkSound(self):
        self.soundRun.stop()
        base.playSfx(self.soundWalk, looping = 1)

    
    def stopSound(self):
        self.soundRun.stop()
        self.soundWalk.stop()

    
    def wakeUp(self):
        if self.sleepCallback != None:
            taskMgr.remove(self.uniqueName('sleepwatch'))
            self.startSleepWatch(self.sleepCallback)
        
        self.lastMoved = globalClock.getFrameTime()
        if self.sleepFlag:
            self.sleepFlag = 0
        

    
    def gotoSleep(self):
        if not (self.sleepFlag):
            self.b_setAnimState('Sleep', self.animMultiplier)
            self.sleepFlag = 1
        

    
    def forceGotoSleep(self):
        if self.hp > 0:
            self.sleepFlag = 0
            self.gotoSleep()
        

    
    def startSleepWatch(self, callback):
        self.sleepCallback = callback
        taskMgr.doMethodLater(self.sleepTimeout, callback, self.uniqueName('sleepwatch'))

    
    def stopSleepWatch(self):
        taskMgr.remove(self.uniqueName('sleepwatch'))
        self.sleepCallback = None

    
    def trackAnimToSpeed(self, task):
        (speed, rotSpeed) = self.controlManager.getSpeeds()
        if speed != 0.0 and rotSpeed != 0.0 or inputState.isSet('jump'):
            if not (self.movingFlag):
                self.movingFlag = 1
                self.stopLookAround()
            
        elif self.movingFlag:
            self.movingFlag = 0
            self.startLookAround()
        
        if self.movingFlag or self.hp <= 0:
            self.wakeUp()
        elif not (self.sleepFlag):
            now = globalClock.getFrameTime()
            if now - self.lastMoved > self.sleepTimeout:
                self.gotoSleep()
            
        
        state = None
        if self.sleepFlag:
            state = 'Sleep'
        elif self.hp > 0:
            state = 'Happy'
        else:
            state = 'Sad'
        if state != self.lastState:
            self.lastState = state
            self.b_setAnimState(state, self.animMultiplier)
            if state == 'Sad':
                self.setWalkSpeedSlow()
            else:
                self.setWalkSpeedNormal()
        
        if self.cheesyEffect == OTPGlobals.CEFlatProfile or self.cheesyEffect == OTPGlobals.CEFlatPortrait:
            needH = None
            if rotSpeed > 0.0:
                needH = -10
            elif rotSpeed < 0.0:
                needH = 10
            elif speed != 0.0:
                needH = 0
            
            if needH != None and self.lastNeedH != needH:
                node = self.getGeomNode().getChild(0)
                lerp = Sequence(LerpHprInterval(node, 0.5, Vec3(needH, 0, 0), blendType = 'easeInOut'), name = 'cheesy-lerp-hpr', autoPause = 1)
                lerp.start()
                self.lastNeedH = needH
            
        else:
            self.lastNeedH = None
        action = self.setSpeed(speed, rotSpeed)
        if action != self.lastAction:
            self.lastAction = action
            if self.emoteTrack:
                self.emoteTrack.finish()
                self.emoteTrack = None
            
            if action == OTPGlobals.WALK_INDEX or action == OTPGlobals.REVERSE_INDEX:
                self.walkSound()
            elif action == OTPGlobals.RUN_INDEX:
                self.runSound()
            else:
                self.stopSound()
        
        return Task.cont

    
    def hasTrackAnimToSpeed(self):
        taskName = self.taskName('trackAnimToSpeed')
        return taskMgr.hasTaskNamed(taskName)

    
    def startTrackAnimToSpeed(self):
        taskName = self.taskName('trackAnimToSpeed')
        taskMgr.remove(taskName)
        task = Task.Task(self.trackAnimToSpeed)
        self.lastMoved = globalClock.getFrameTime()
        self.lastState = None
        self.lastAction = None
        self.trackAnimToSpeed(task)
        taskMgr.add(self.trackAnimToSpeed, taskName, 35)

    
    def stopTrackAnimToSpeed(self):
        taskName = self.taskName('trackAnimToSpeed')
        taskMgr.remove(taskName)
        self.stopSound()

    
    def startChat(self):
        self.chatMgr.start()
        self.accept('chatUpdate', self.b_setChat)
        self.accept('chatUpdateSC', self.b_setSC)
        self.accept('chatUpdateSCCustom', self.b_setSCCustom)
        self.accept('chatUpdateSCEmote', self.b_setSCEmote)
        self.accept('whisperUpdate', self.whisperTo)
        self.accept('whisperUpdateSC', self.whisperSCTo)
        self.accept('whisperUpdateSCCustom', self.whisperSCCustomTo)
        self.accept('whisperUpdateSCEmote', self.whisperSCEmoteTo)
        self.accept(OTPGlobals.ThinkPosHotkey, self.thinkPos)
        self.accept(OTPGlobals.PrintCamPosHotkey, self.printCamPos)
        if self._LocalAvatar__enableMarkerPlacement:
            self.accept(OTPGlobals.PlaceMarkerHotkey, self._LocalAvatar__placeMarker)
        

    
    def stopChat(self):
        self.chatMgr.stop()
        self.ignore('chatUpdate')
        self.ignore('chatUpdateSC')
        self.ignore('chatUpdateSCCustom')
        self.ignore('whisperUpdate')
        self.ignore('whisperUpdateSC')
        self.ignore('whisperUpdateSCCustom')
        self.ignore(OTPGlobals.ThinkPosHotkey)
        if self._LocalAvatar__enableMarkerPlacement:
            self.ignore(OTPGlobals.PlaceMarkerHotkey)
        

    
    def printCamPos(self):
        node = base.camera.getParent()
        pos = base.cam.getPos(node)
        hpr = base.cam.getHpr(node)
        print 'cam pos = ', `pos`, ', cam hpr = ', `hpr`

    
    def d_broadcastPositionNow(self):
        self.d_clearSmoothing()
        self.d_broadcastPosHpr()

    
    def travCollisionsLOS(self, n = None):
        if n == None:
            n = self._LocalAvatar__geom
        
        self.ccTrav.traverse(n)

    
    def travCollisionsFloor(self, n = None):
        if n == None:
            n = self._LocalAvatar__geom
        
        self.ccTravFloor.traverse(n)

    
    def travCollisionsPusher(self, n = None):
        if n == None:
            n = self._LocalAvatar__geom
        
        self.ccPusherTrav.traverse(n)

    
    def _LocalAvatar__friendOnline(self, doId):
        if self.oldFriendsList != None:
            now = globalClock.getFrameTime()
            elapsed = now - self.timeFriendsListChanged
            if elapsed < 10.0 and self.oldFriendsList.count(doId) == 0:
                self.oldFriendsList.append(doId)
                return None
            
        
        friend = base.cr.identifyFriend(doId)
        if friend != None:
            self.setSystemMessage(doId, OTPLocalizer.WhisperFriendComingOnline % friend.getName())
        

    
    def _LocalAvatar__friendOffline(self, doId):
        friend = base.cr.identifyFriend(doId)
        if friend != None:
            self.setSystemMessage(0, OTPLocalizer.WhisperFriendLoggedOut % friend.getName())
        

    
    def _LocalAvatar__clickedWhisper(self, doId):
        friend = base.cr.identifyFriend(doId)
        if friend != None:
            messenger.send('clickedNametag', [
                friend])
            self.chatMgr.whisperTo(friend.getName(), doId)
        

    
    def d_setParent(self, parentToken):
        DistributedSmoothNode.DistributedSmoothNode.d_setParent(self, parentToken)


