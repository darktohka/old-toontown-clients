# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownTimer
from pandac import NodePath
from direct.task import Task
from toontown.minigame import Trajectory
import math
from toontown.toon import ToonHead
from toontown.effects import Splash
from toontown.effects import DustCloud
from toontown.minigame import CannonGameGlobals
import CannonGlobals
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from direct.distributed import DistributedObject
from toontown.effects import Wake
LAND_TIME = 2
WORLD_SCALE = 2.0
GROUND_SCALE = 1.3999999999999999 * WORLD_SCALE
CANNON_SCALE = 1.0
FAR_PLANE_DIST = 600 * WORLD_SCALE
GROUND_PLANE_MIN = -15
CANNON_Y = -int((CannonGameGlobals.TowerYRange / 2) * 1.3)
CANNON_X_SPACING = 12
CANNON_Z = 20
CANNON_ROTATION_MIN = -55
CANNON_ROTATION_MAX = 50
CANNON_ROTATION_VEL = 15.0
CANNON_ANGLE_MIN = 10
CANNON_ANGLE_MAX = 85
CANNON_ANGLE_VEL = 15.0
CANNON_MOVE_UPDATE_FREQ = 0.5
CAMERA_PULLBACK_MIN = 20
CAMERA_PULLBACK_MAX = 40
MAX_LOOKAT_OFFSET = 80
TOON_TOWER_THRESHOLD = 150
SHADOW_Z_OFFSET = 0.5
TOWER_HEIGHT = 43.850000000000001
TOWER_RADIUS = 10.5
BUCKET_HEIGHT = 36
TOWER_Y_RANGE = CannonGameGlobals.TowerYRange
TOWER_X_RANGE = int(TOWER_Y_RANGE / 2.0)
INITIAL_VELOCITY = 80.0
WHISTLE_SPEED = INITIAL_VELOCITY * 0.34999999999999998

class DistributedCannon(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCannon')
    font = ToontownGlobals.getToonFont()
    LOCAL_CANNON_MOVE_TASK = 'localCannonMoveTask'
    REWARD_COUNTDOWN_TASK = 'cannonGameRewardCountdown'
    HIT_GROUND = 0
    HIT_TOWER = 1
    HIT_WATER = 2
    FIRE_KEY = 'control'
    UP_KEY = 'arrow_up'
    DOWN_KEY = 'arrow_down'
    LEFT_KEY = 'arrow_left'
    RIGHT_KEY = 'arrow_right'
    INTRO_TASK_NAME = 'CannonGameIntro'
    INTRO_TASK_NAME_CAMERA_LERP = 'CannonGameIntroCamera'
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.avId = 0
        self.av = None
        self.localToonShooting = 0
        self.nodePath = None
        self.collSphere = None
        self.collNode = None
        self.collNodePath = None
        self.madeGui = 0
        self.gui = None
        self.cannonLocation = None
        self.cannonPostion = None
        self.cannon = None
        self.toonModel = None
        self.shadowNode = None
        self.toonHead = None
        self.toonScale = None
        self.estateId = None
        self.splash = None
        self.dustCloud = None
        self.model_Created = 0
        self.lastWakeTime = 0
        self.leftPressed = 0
        self.rightPressed = 0
        self.upPressed = 0
        self.downPressed = 0
        self.hitBumper = 0
        self.hitTarget = 0
        self.lastPos = Vec3(0, 0, 0)
        self.lastVel = Vec3(0, 0, 0)
        self.vel = Vec3(0, 0, 0)
        self.landingPos = Vec3(0, 0, 0)
        self.t = 0
        self.lastT = 0
        self.deltaT = 0
        self.hitTrack = None
        self.cTrav = None
        self.cRay = None
        self.cRayNode = None
        self.cRayNodePath = None
        self.lifter = None
        self.flyColNode = None
        self.flyColNodePath = None
        self.cannonMoving = 0
        self.inWater = 0
        self.localAvId = base.localAvatar.doId
        self.nextState = None
        self.nextKey = None
        self.cannonsActive = 0
        self.codeFSM = ClassicFSM.ClassicFSM('CannonCode', [
            State.State('init', self.enterInit, self.exitInit, [
                'u1',
                'init']),
            State.State('u1', self.enteru1, self.exitu1, [
                'u2',
                'init']),
            State.State('u2', self.enteru2, self.exitu2, [
                'd3',
                'init']),
            State.State('d3', self.enterd3, self.exitd3, [
                'd4',
                'init']),
            State.State('d4', self.enterd4, self.exitd4, [
                'l5',
                'init']),
            State.State('l5', self.enterl5, self.exitl5, [
                'r6',
                'init']),
            State.State('r6', self.enterr6, self.exitr6, [
                'l7',
                'init']),
            State.State('l7', self.enterl7, self.exitl7, [
                'r8',
                'init']),
            State.State('r8', self.enterr8, self.exitr8, [
                'acceptCode',
                'init']),
            State.State('acceptCode', self.enterAcceptCode, self.exitAcceptCode, [
                'init',
                'final']),
            State.State('final', self.enterFinal, self.exitFinal, [])], 'init', 'final')
        self.codeFSM.enterInitialState()

    
    def disable(self):
        taskMgr.remove(self.uniqueName('fireCannon'))
        taskMgr.remove(self.uniqueName('shootTask'))
        taskMgr.remove(self.uniqueName('flyTask'))
        self.ignoreAll()
        self.setMovie(CannonGlobals.CANNON_MOVIE_CLEAR, 0)
        self.nodePath.detachNode()
        self._DistributedCannon__unmakeGui()
        if self.hitTrack:
            self.hitTrack.finish()
            del self.hitTrack
            self.hitTrack = None
        
        DistributedObject.DistributedObject.disable(self)

    
    def _DistributedCannon__unmakeGui(self):
        if not (self.madeGui):
            return None
        
        self.aimPad.destroy()
        del self.aimPad
        del self.fireButton
        del self.upButton
        del self.downButton
        del self.leftButton
        del self.rightButton
        self.madeGui = 0

    
    def generateInit(self):
        self.nodePath = NodePath(self.uniqueName('Cannon'))
        self.load()
        self.activateCannons()
        self.listenForCode()

    
    def listenForCode(self):
        self.accept(self.UP_KEY + '-up', self._DistributedCannon__upKeyCode)
        self.accept(self.DOWN_KEY + '-up', self._DistributedCannon__downKeyCode)
        self.accept(self.LEFT_KEY + '-up', self._DistributedCannon__leftKeyCode)
        self.accept(self.RIGHT_KEY + '-up', self._DistributedCannon__rightKeyCode)

    
    def ignoreCode(self):
        self.ignore(self.UP_KEY + '-up')
        self.ignore(self.DOWN_KEY + '-up')
        self.ignore(self.LEFT_KEY + '-up')
        self.ignore(self.RIGHT_KEY + '-up')

    
    def activateCannons(self):
        if not (self.cannonsActive):
            self.cannonsActive = 1
            self.onstage()
            self.nodePath.reparentTo(self.getParentNodePath())
            self.accept(self.uniqueName('enterCannonSphere'), self._DistributedCannon__handleEnterSphere)
        

    
    def deActivateCannons(self):
        if self.cannonsActive:
            self.cannonsActive = 0
            self.offstage()
            self.nodePath.reparentTo(hidden)
            self.ignore(self.uniqueName('enterCannonSphere'))
        

    
    def delete(self):
        self.offstage()
        self.unload()
        DistributedObject.DistributedObject.delete(self)

    
    def _DistributedCannon__handleEnterSphere(self, collEntry):
        self.d_requestEnter()

    
    def d_requestEnter(self):
        self.sendUpdate('requestEnter', [])

    
    def getSphereRadius(self):
        return 1.5

    
    def getParentNodePath(self):
        return base.cr.playGame.hood.loader.geom

    
    def setEstateId(self, estateId):
        self.estateId = estateId

    
    def setPosHpr(self, x, y, z, h, p, r):
        self.nodePath.setPosHpr(x, y, z, h, p, r)

    
    def setMovie(self, mode, avId):
        wasLocalToon = self.localToonShooting
        self.avId = avId
        if mode == CannonGlobals.CANNON_MOVIE_CLEAR:
            self.listenForCode()
            self.setLanded()
        elif mode == CannonGlobals.CANNON_MOVIE_LANDED:
            self.setLanded()
        elif mode == CannonGlobals.CANNON_MOVIE_FORCE_EXIT:
            self.exitCannon(self.avId)
            self.setLanded()
        elif mode == CannonGlobals.CANNON_MOVIE_LOAD:
            self.ignoreCode()
            if self.avId == base.localAvatar.doId:
                base.localAvatar.pose('lose', 110)
                base.localAvatar.pose('slip-forward', 25)
                base.cr.playGame.getPlace().setState('fishing')
                base.localAvatar.setTeleportAvailable(0)
                base.localAvatar.collisionsOff()
                base.setCellsAvailable([
                    base.bottomCells[1],
                    base.bottomCells[2]], 0)
                self.localToonShooting = 1
                self._DistributedCannon__makeGui()
                camera.reparentTo(self.barrel)
                camera.setPos(0.5, -2, 2.5)
            
            if self.cr.doId2do.has_key(self.avId):
                self.av = self.cr.doId2do[self.avId]
                self.acceptOnce(self.av.uniqueName('disable'), self._DistributedCannon__avatarGone)
                self.av.stopSmooth()
                self._DistributedCannon__createToonModels()
            else:
                self.notify.warning('Unknown avatar %d in cannon %d' % (self.avId, self.doId))
        
        if wasLocalToon and not (self.localToonShooting):
            base.setCellsAvailable([
                base.bottomCells[1],
                base.bottomCells[2]], 1)
        
        return None

    
    def _DistributedCannon__avatarGone(self):
        self.setMovie(CannonGlobals.CANNON_MOVIE_CLEAR, 0)

    
    def load(self):
        self.cannon = loader.loadModel('phase_4/models/minigames/toon_cannon')
        self.shadow = loader.loadModel('phase_3/models/props/drop_shadow')
        self.shadowNode = hidden.attachNewNode('dropShadow')
        self.shadow.copyTo(self.shadowNode)
        self.smoke = loader.loadModel('phase_8/models/props/test_clouds')
        self.smoke.setBillboardPointEye()
        self.cannon.setScale(CANNON_SCALE)
        self.shadowNode.setColor(0, 0, 0, 0.5)
        self.shadowNode.setBin('fixed', 0, 1)
        self.splash = Splash.Splash(render)
        self.dustCloud = DustCloud.DustCloud(render)
        self.dustCloud.setBillboardPointEye()
        self.sndCannonMove = base.loadSfx('phase_4/audio/sfx/MG_cannon_adjust.mp3')
        self.sndCannonFire = base.loadSfx('phase_4/audio/sfx/MG_cannon_fire_alt.mp3')
        self.sndHitGround = base.loadSfx('phase_4/audio/sfx/MG_cannon_hit_dirt.mp3')
        self.sndHitTower = base.loadSfx('phase_4/audio/sfx/MG_cannon_hit_tower.mp3')
        self.sndHitWater = base.loadSfx('phase_4/audio/sfx/MG_cannon_splash.mp3')
        self.sndWhizz = base.loadSfx('phase_4/audio/sfx/MG_cannon_whizz.mp3')
        self.sndWin = base.loadSfx('phase_4/audio/sfx/MG_win.mp3')
        self.sndHitHouse = base.loadSfx('phase_5/audio/sfx/AA_drop_sandbag.mp3')
        self.collSphere = CollisionSphere(0, 0, 0, self.getSphereRadius())
        self.collSphere.setTangible(1)
        self.collNode = CollisionNode(self.uniqueName('CannonSphere'))
        self.collNode.setCollideMask(ToontownGlobals.WallBitmask)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.nodePath.attachNewNode(self.collNode)

    
    def setupMovingShadow(self):
        self.cTrav = base.cTrav
        self.cRay = CollisionRay(0.0, 0.0, CollisionHandlerRayStart, 0.0, 0.0, -1.0)
        self.cRayNode = CollisionNode('cRayNode')
        self.cRayNode.addSolid(self.cRay)
        self.cRayNodePath = self.shadowNode.attachNewNode(self.cRayNode)
        self.cRayNodePath.hide()
        self.cRayBitMask = ToontownGlobals.FloorBitmask
        self.cRayNode.setFromCollideMask(self.cRayBitMask)
        self.cRayNode.setIntoCollideMask(BitMask32.allOff())
        self.lifter = CollisionHandlerFloor()
        self.lifter.setOffset(ToontownGlobals.FloorOffset)
        self.lifter.setReach(20.0)
        self.enableRaycast(1)

    
    def enableRaycast(self, enable = 1):
        if not (self.cTrav) and not hasattr(self, 'cRayNode') or not (self.cRayNode):
            return None
        
        print '-------enabling raycast--------'
        self.cTrav.removeCollider(self.cRayNodePath)
        if enable:
            self.cTrav.addCollider(self.cRayNodePath, self.lifter)
        

    
    def _DistributedCannon__makeGui(self):
        if self.madeGui:
            return None
        
        guiModel = 'phase_4/models/gui/cannon_game_gui'
        cannonGui = loader.loadModel(guiModel)
        self.aimPad = DirectFrame(image = cannonGui.find('**/CannonFire_PAD'), relief = None, pos = (0.69999999999999996, 0, -0.55333299999999996), scale = 0.80000000000000004)
        cannonGui.removeNode()
        self.fireButton = DirectButton(parent = self.aimPad, image = ((guiModel, '**/Fire_Btn_UP'), (guiModel, '**/Fire_Btn_DN'), (guiModel, '**/Fire_Btn_RLVR')), relief = None, pos = (0.0115741, 0, 0.0050505100000000002), scale = 1.0, command = self._DistributedCannon__firePressed)
        self.upButton = DirectButton(parent = self.aimPad, image = ((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief = None, pos = (0.0115741, 0, 0.221717))
        self.downButton = DirectButton(parent = self.aimPad, image = ((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief = None, pos = (0.0136112, 0, -0.21010100000000001), image_hpr = (0, 0, 180))
        self.leftButton = DirectButton(parent = self.aimPad, image = ((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief = None, pos = (-0.199352, 0, -0.00050526900000000003), image_hpr = (0, 0, -90))
        self.rightButton = DirectButton(parent = self.aimPad, image = ((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief = None, pos = (0.219167, 0, -0.0010102399999999999), image_hpr = (0, 0, 90))
        self.aimPad.setColor(1, 1, 1, 0.90000000000000002)
        
        def bindButton(button, upHandler, downHandler):
            button.bind(B1PRESS, lambda x, handler = upHandler: handler())
            button.bind(B1RELEASE, lambda x, handler = downHandler: handler())

        bindButton(self.upButton, self._DistributedCannon__upPressed, self._DistributedCannon__upReleased)
        bindButton(self.downButton, self._DistributedCannon__downPressed, self._DistributedCannon__downReleased)
        bindButton(self.leftButton, self._DistributedCannon__leftPressed, self._DistributedCannon__leftReleased)
        bindButton(self.rightButton, self._DistributedCannon__rightPressed, self._DistributedCannon__rightReleased)
        self._DistributedCannon__enableAimInterface()
        self.madeGui = 1

    
    def _DistributedCannon__unmakeGui(self):
        self.notify.debug('__unmakeGui')
        if not (self.madeGui):
            return None
        
        self._DistributedCannon__disableAimInterface()
        self.upButton.unbind(B1PRESS)
        self.upButton.unbind(B1RELEASE)
        self.downButton.unbind(B1PRESS)
        self.downButton.unbind(B1RELEASE)
        self.leftButton.unbind(B1PRESS)
        self.leftButton.unbind(B1RELEASE)
        self.rightButton.unbind(B1PRESS)
        self.rightButton.unbind(B1RELEASE)
        self.aimPad.destroy()
        del self.aimPad
        del self.fireButton
        del self.upButton
        del self.downButton
        del self.leftButton
        del self.rightButton
        self.madeGui = 0

    
    def unload(self):
        self.ignoreCode()
        del self.codeFSM
        if self.cannon:
            self.cannon.removeNode()
            del self.cannon
        
        if self.shadowNode != None:
            self.shadowNode.removeNode()
            del self.shadowNode
        
        if self.splash != None:
            self.splash.destroy()
            del self.splash
        
        if self.dustCloud != None:
            self.dustCloud.destroy()
            del self.dustCloud
        
        del self.sndCannonMove
        del self.sndCannonFire
        del self.sndHitHouse
        del self.sndHitGround
        del self.sndHitTower
        del self.sndHitWater
        del self.sndWhizz
        del self.sndWin
        if self.av:
            self._DistributedCannon__resetToon(self.av)
            self.av.loop('neutral')
            self.av.setPlayRate(1.0, 'run')
            self.av.nametag.removeNametag(self.toonHead.tag)
        
        if self.toonHead != None:
            self.toonHead.stopBlink()
            self.toonHead.stopLookAroundNow()
            self.toonHead.delete()
            del self.toonHead
        
        if self.toonModel != None:
            self.toonModel.removeNode()
            del self.toonModel
        
        del self.toonScale
        del self.cannonLocation
        del self.cRay
        del self.cRayNode
        if self.cRayNodePath:
            self.cRayNodePath.removeNode()
            del self.cRayNodePath
        
        del self.lifter
        self.enableRaycast(0)

    
    def onstage(self):
        self._DistributedCannon__createCannon()
        self.cannon.reparentTo(self.nodePath)
        self.splash.reparentTo(render)
        self.dustCloud.reparentTo(render)

    
    def offstage(self):
        if self.cannon:
            self.cannon.reparentTo(hidden)
        
        if self.splash:
            self.splash.reparentTo(hidden)
            self.splash.stop()
        
        if self.dustCloud:
            self.dustCloud.reparentTo(hidden)
            self.dustCloud.stop()
        

    
    def _DistributedCannon__createCannon(self):
        self.barrel = self.cannon.find('**/cannon')
        self.cannonLocation = Point3(0, 0, 0.025000000000000001)
        self.cannonPosition = [
            0,
            CANNON_ANGLE_MIN]
        self.cannon.setPos(self.cannonLocation)
        self._DistributedCannon__updateCannonPosition(self.avId)

    
    def _DistributedCannon__createToonModels(self):
        self.model_Created = 1
        toon = self.av
        self.toonScale = toon.getScale()
        toon.useLOD(1000)
        toonParent = render.attachNewNode('toonOriginChange')
        toon.wrtReparentTo(toonParent)
        toon.setPosHpr(0, 0, -(toon.getHeight() / 2.0), 0, -90, 0)
        self.toonModel = toonParent
        self.toonHead = ToonHead.ToonHead()
        self.toonHead.setupHead(self.av.style)
        self.toonHead.reparentTo(hidden)
        tag = NametagFloat3d()
        tag.setContents(Nametag.CSpeech | Nametag.CThought)
        tag.setBillboardOffset(0)
        tag.setAvatar(self.toonHead)
        toon.nametag.addNametag(tag)
        tagPath = self.toonHead.attachNewNode(tag.upcastToPandaNode())
        tagPath.setPos(0, 0, 1)
        self.toonHead.tag = tag
        self._DistributedCannon__loadToonInCannon()
        self.av.dropShadow.hide()
        self.dropShadow = self.shadowNode.copyTo(hidden)

    
    def _DistributedCannon__destroyToonModels(self):
        if self.av != None:
            self.av.dropShadow.show()
            if self.dropShadow != None:
                self.dropShadow.removeNode()
                self.dropShadow = None
            
            self.hitBumper = 0
            self.hitTarget = 0
            self.angularVel = 0
            self.vel = Vec3(0, 0, 0)
            self.lastVel = Vec3(0, 0, 0)
            self.lastPos = Vec3(0, 0, 0)
            self.landingPos = Vec3(0, 0, 0)
            self.t = 0
            self.lastT = 0
            self.deltaT = 0
            self.av = None
            self.lastWakeTime = 0
            self.localToonShooting = 0
        
        if self.toonHead != None:
            self.toonHead.reparentTo(hidden)
            self.toonHead.stopBlink()
            self.toonHead.stopLookAroundNow()
            self.toonHead = None
        
        if self.toonModel != None:
            self.toonModel.removeNode()
            self.toonModel = None
        
        self.model_Created = 0

    
    def updateCannonPosition(self, avId, zRot, angle):
        if avId != self.localAvId:
            self.cannonPosition = [
                zRot,
                angle]
            self._DistributedCannon__updateCannonPosition(avId)
        

    
    def setCannonWillFire(self, avId, fireTime, zRot, angle, timestamp):
        self.notify.debug('setCannonWillFire: ' + str(avId) + ': zRot=' + str(zRot) + ', angle=' + str(angle) + ', time=' + str(fireTime))
        if not (self.model_Created):
            self.notify.warning("We walked into the zone mid-flight, so we won't see it")
            return None
        
        self.cannonPosition[0] = zRot
        self.cannonPosition[1] = angle
        self._DistributedCannon__updateCannonPosition(avId)
        task = Task.Task(self._DistributedCannon__fireCannonTask)
        task.avId = avId
        ts = globalClockDelta.localElapsedTime(timestamp)
        task.fireTime = fireTime - ts
        if task.fireTime < 0.0:
            task.fireTime = 0.0
        
        taskMgr.add(task, self.taskName('fireCannon'))

    
    def exitCannon(self, avId):
        self._DistributedCannon__unmakeGui()
        if self.avId == avId:
            self.av.reparentTo(render)
            self._DistributedCannon__resetToonToCannon(self.av)
        

    
    def _DistributedCannon__enableAimInterface(self):
        self.aimPad.show()
        self.accept(self.FIRE_KEY, self._DistributedCannon__fireKeyPressed)
        self.accept(self.UP_KEY, self._DistributedCannon__upKeyPressed)
        self.accept(self.DOWN_KEY, self._DistributedCannon__downKeyPressed)
        self.accept(self.LEFT_KEY, self._DistributedCannon__leftKeyPressed)
        self.accept(self.RIGHT_KEY, self._DistributedCannon__rightKeyPressed)
        self._DistributedCannon__spawnLocalCannonMoveTask()

    
    def _DistributedCannon__disableAimInterface(self):
        self.aimPad.hide()
        self.ignore(self.FIRE_KEY)
        self.ignore(self.UP_KEY)
        self.ignore(self.DOWN_KEY)
        self.ignore(self.LEFT_KEY)
        self.ignore(self.RIGHT_KEY)
        self.ignore(self.FIRE_KEY + '-up')
        self.ignore(self.UP_KEY + '-up')
        self.ignore(self.DOWN_KEY + '-up')
        self.ignore(self.LEFT_KEY + '-up')
        self.ignore(self.RIGHT_KEY + '-up')
        self._DistributedCannon__killLocalCannonMoveTask()

    
    def _DistributedCannon__fireKeyPressed(self):
        self.ignore(self.FIRE_KEY)
        self.accept(self.FIRE_KEY + '-up', self._DistributedCannon__fireKeyReleased)
        self._DistributedCannon__firePressed()

    
    def _DistributedCannon__upKeyPressed(self):
        self.ignore(self.UP_KEY)
        self.accept(self.UP_KEY + '-up', self._DistributedCannon__upKeyReleased)
        self._DistributedCannon__upPressed()

    
    def _DistributedCannon__downKeyPressed(self):
        self.ignore(self.DOWN_KEY)
        self.accept(self.DOWN_KEY + '-up', self._DistributedCannon__downKeyReleased)
        self._DistributedCannon__downPressed()

    
    def _DistributedCannon__leftKeyPressed(self):
        self.ignore(self.LEFT_KEY)
        self.accept(self.LEFT_KEY + '-up', self._DistributedCannon__leftKeyReleased)
        self._DistributedCannon__leftPressed()

    
    def _DistributedCannon__rightKeyPressed(self):
        self.ignore(self.RIGHT_KEY)
        self.accept(self.RIGHT_KEY + '-up', self._DistributedCannon__rightKeyReleased)
        self._DistributedCannon__rightPressed()

    
    def _DistributedCannon__fireKeyReleased(self):
        self.ignore(self.FIRE_KEY + '-up')
        self.accept(self.FIRE_KEY, self._DistributedCannon__fireKeyPressed)
        self._DistributedCannon__fireReleased()

    
    def _DistributedCannon__leftKeyReleased(self):
        self.ignore(self.LEFT_KEY + '-up')
        self.accept(self.LEFT_KEY, self._DistributedCannon__leftKeyPressed)
        self.handleCodeKey('left')
        self._DistributedCannon__leftReleased()

    
    def _DistributedCannon__rightKeyReleased(self):
        self.ignore(self.RIGHT_KEY + '-up')
        self.accept(self.RIGHT_KEY, self._DistributedCannon__rightKeyPressed)
        self.handleCodeKey('right')
        self._DistributedCannon__rightReleased()

    
    def _DistributedCannon__upKeyReleased(self):
        self.ignore(self.UP_KEY + '-up')
        self.accept(self.UP_KEY, self._DistributedCannon__upKeyPressed)
        self._DistributedCannon__upReleased()

    
    def _DistributedCannon__downKeyReleased(self):
        self.ignore(self.DOWN_KEY + '-up')
        self.accept(self.DOWN_KEY, self._DistributedCannon__downKeyPressed)
        self.handleCodeKey('down')
        self._DistributedCannon__downReleased()

    
    def _DistributedCannon__upKeyCode(self):
        self.handleCodeKey('up')

    
    def _DistributedCannon__downKeyCode(self):
        self.handleCodeKey('down')

    
    def _DistributedCannon__rightKeyCode(self):
        self.handleCodeKey('right')

    
    def _DistributedCannon__leftKeyCode(self):
        self.handleCodeKey('left')

    
    def _DistributedCannon__firePressed(self):
        self.notify.debug('fire pressed')
        self._DistributedCannon__broadcastLocalCannonPosition()
        self._DistributedCannon__unmakeGui()
        self.sendUpdate('setCannonLit', [
            self.cannonPosition[0],
            self.cannonPosition[1]])

    
    def _DistributedCannon__upPressed(self):
        self.notify.debug('up pressed')
        self.upPressed = self._DistributedCannon__enterControlActive(self.upPressed)

    
    def _DistributedCannon__downPressed(self):
        self.notify.debug('down pressed')
        self.downPressed = self._DistributedCannon__enterControlActive(self.downPressed)

    
    def _DistributedCannon__leftPressed(self):
        self.notify.debug('left pressed')
        self.leftPressed = self._DistributedCannon__enterControlActive(self.leftPressed)

    
    def _DistributedCannon__rightPressed(self):
        self.notify.debug('right pressed')
        self.rightPressed = self._DistributedCannon__enterControlActive(self.rightPressed)

    
    def _DistributedCannon__upReleased(self):
        self.notify.debug('up released')
        self.upPressed = self._DistributedCannon__exitControlActive(self.upPressed)

    
    def _DistributedCannon__downReleased(self):
        self.notify.debug('down released')
        self.downPressed = self._DistributedCannon__exitControlActive(self.downPressed)

    
    def _DistributedCannon__leftReleased(self):
        self.notify.debug('left released')
        self.leftPressed = self._DistributedCannon__exitControlActive(self.leftPressed)

    
    def _DistributedCannon__rightReleased(self):
        self.notify.debug('right released')
        self.rightPressed = self._DistributedCannon__exitControlActive(self.rightPressed)

    
    def _DistributedCannon__enterControlActive(self, control):
        return control + 1

    
    def _DistributedCannon__exitControlActive(self, control):
        return max(0, control - 1)

    
    def _DistributedCannon__spawnLocalCannonMoveTask(self):
        self.leftPressed = 0
        self.rightPressed = 0
        self.upPressed = 0
        self.downPressed = 0
        self.cannonMoving = 0
        task = Task.Task(self._DistributedCannon__localCannonMoveTask)
        task.lastPositionBroadcastTime = 0.0
        taskMgr.add(task, self.LOCAL_CANNON_MOVE_TASK)

    
    def _DistributedCannon__killLocalCannonMoveTask(self):
        taskMgr.remove(self.LOCAL_CANNON_MOVE_TASK)
        if self.cannonMoving:
            self.sndCannonMove.stop()
        

    
    def _DistributedCannon__localCannonMoveTask(self, task):
        pos = self.cannonPosition
        oldRot = pos[0]
        oldAng = pos[1]
        rotVel = 0
        if self.leftPressed:
            rotVel += CANNON_ROTATION_VEL
        
        if self.rightPressed:
            rotVel -= CANNON_ROTATION_VEL
        
        pos[0] += rotVel * globalClock.getDt()
        if pos[0] < CANNON_ROTATION_MIN:
            pos[0] = CANNON_ROTATION_MIN
        elif pos[0] > CANNON_ROTATION_MAX:
            pos[0] = CANNON_ROTATION_MAX
        
        angVel = 0
        if self.upPressed:
            angVel += CANNON_ANGLE_VEL
        
        if self.downPressed:
            angVel -= CANNON_ANGLE_VEL
        
        pos[1] += angVel * globalClock.getDt()
        if pos[1] < CANNON_ANGLE_MIN:
            pos[1] = CANNON_ANGLE_MIN
        elif pos[1] > CANNON_ANGLE_MAX:
            pos[1] = CANNON_ANGLE_MAX
        
        if oldRot != pos[0] or oldAng != pos[1]:
            if self.cannonMoving == 0:
                self.cannonMoving = 1
                base.playSfx(self.sndCannonMove, looping = 1)
            
            self._DistributedCannon__updateCannonPosition(self.localAvId)
            if task.time - task.lastPositionBroadcastTime > CANNON_MOVE_UPDATE_FREQ:
                task.lastPositionBroadcastTime = task.time
                self._DistributedCannon__broadcastLocalCannonPosition()
            
        elif self.cannonMoving:
            self.cannonMoving = 0
            self.sndCannonMove.stop()
            self._DistributedCannon__broadcastLocalCannonPosition()
        
        return Task.cont

    
    def _DistributedCannon__broadcastLocalCannonPosition(self):
        self.sendUpdate('setCannonPosition', [
            self.cannonPosition[0],
            self.cannonPosition[1]])

    
    def _DistributedCannon__updateCannonPosition(self, avId):
        self.cannon.setHpr(self.cannonPosition[0], 0.0, 0.0)
        self.barrel.setHpr(0.0, self.cannonPosition[1], 0.0)
        maxP = 90
        newP = self.barrel.getP()
        yScale = 1 - 0.5 * float(newP) / maxP
        shadow = self.cannon.find('**/square_drop_shadow')
        shadow.setScale(1, yScale, 1)

    
    def _DistributedCannon__getCameraPositionBehindCannon(self):
        return Point3(self.cannonLocationDict[self.localAvId][0], CANNON_Y - 5.0, CANNON_Z + 7)

    
    def _DistributedCannon__putCameraBehindCannon(self):
        camera.setPos(self._DistributedCannon__getCameraPositionBehindCannon())
        camera.setHpr(0, 0, 0)

    
    def _DistributedCannon__loadToonInCannon(self):
        self.toonModel.reparentTo(hidden)
        self.toonHead.startBlink()
        self.toonHead.startLookAround()
        self.toonHead.reparentTo(self.barrel)
        self.toonHead.setPosHpr(0, 6, 0, 0, -45, 0)
        sc = self.toonScale
        self.toonHead.setScale(render, sc[0], sc[1], sc[2])

    
    def _DistributedCannon__toRadians(self, angle):
        return angle * 2.0 * math.pi / 360.0

    
    def _DistributedCannon__toDegrees(self, angle):
        return angle * 360.0 / 2.0 * math.pi

    
    def _DistributedCannon__calcFlightResults(self, avId, launchTime):
        head = self.toonHead
        startPos = head.getPos(render)
        startHpr = head.getHpr(render)
        hpr = self.barrel.getHpr(render)
        rotation = self._DistributedCannon__toRadians(hpr[0])
        angle = self._DistributedCannon__toRadians(hpr[1])
        horizVel = INITIAL_VELOCITY * math.cos(angle)
        xVel = horizVel * -math.sin(rotation)
        yVel = horizVel * math.cos(rotation)
        zVel = INITIAL_VELOCITY * math.sin(angle)
        startVel = Vec3(xVel, yVel, zVel)
        trajectory = Trajectory.Trajectory(launchTime, startPos, startVel)
        self.trajectory = trajectory
        hitTreasures = self._DistributedCannon__calcHitTreasures(trajectory)
        (timeOfImpact, hitWhat) = self._DistributedCannon__calcToonImpact(trajectory)
        return {
            'startPos': startPos,
            'startHpr': startHpr,
            'startVel': startVel,
            'trajectory': trajectory,
            'timeOfImpact': 3 * timeOfImpact,
            'hitWhat': hitWhat }

    
    def _DistributedCannon__fireCannonTask(self, task):
        launchTime = task.fireTime
        avId = task.avId
        flightResults = self._DistributedCannon__calcFlightResults(avId, launchTime)
        for key in flightResults:
            exec "%s = flightResults['%s']" % (key, key)
        
        self.notify.debug('start position: ' + str(startPos))
        self.notify.debug('start velocity: ' + str(startVel))
        self.notify.debug('time of launch: ' + str(launchTime))
        self.notify.debug('time of impact: ' + str(timeOfImpact))
        self.notify.debug('location of impact: ' + str(trajectory.getPos(timeOfImpact)))
        if hitWhat == self.HIT_WATER:
            self.notify.debug('toon will land in the water')
        elif hitWhat == self.HIT_TOWER:
            self.notify.debug('toon will hit the tower')
        else:
            self.notify.debug('toon will hit the ground')
        head = self.toonHead
        head.stopBlink()
        head.stopLookAroundNow()
        head.reparentTo(hidden)
        av = self.toonModel
        av.reparentTo(render)
        av.setPos(startPos)
        barrelHpr = self.barrel.getHpr(render)
        av.setHpr(startHpr)
        avatar = self.av
        avatar.loop('swim')
        avatar.setPosHpr(0, 0, -(avatar.getHeight() / 2.0), 0, 0, 0)
        info = { }
        info['avId'] = avId
        info['trajectory'] = trajectory
        info['launchTime'] = launchTime
        info['timeOfImpact'] = timeOfImpact
        info['hitWhat'] = hitWhat
        info['toon'] = self.toonModel
        info['hRot'] = self.cannonPosition[0]
        info['haveWhistled'] = 0
        info['maxCamPullback'] = CAMERA_PULLBACK_MIN
        if self.localToonShooting:
            camera.reparentTo(self.av)
            camera.setP(45.0)
            camera.setZ(-10.0)
        
        self.flyColSphere = CollisionSphere(0, 0, self.av.getHeight() / 2.0, 1.0)
        self.flyColNode = CollisionNode(self.uniqueName('flySphere'))
        self.flyColNode.setCollideMask(ToontownGlobals.WallBitmask | ToontownGlobals.FloorBitmask)
        self.flyColNode.addSolid(self.flyColSphere)
        self.flyColNodePath = self.av.attachNewNode(self.flyColNode)
        self.flyColNodePath.setColor(1, 0, 0, 1)
        self.handler = CollisionHandlerEvent()
        self.handler.setInPattern(self.uniqueName('cannonHit'))
        base.cTrav.addCollider(self.flyColNodePath, self.handler)
        self.accept(self.uniqueName('cannonHit'), self._DistributedCannon__handleCannonHit)
        shootTask = Task.Task(self._DistributedCannon__shootTask, self.taskName('shootTask'))
        smokeTask = Task.Task(self._DistributedCannon__smokeTask, self.taskName('smokeTask'))
        flyTask = Task.Task(self._DistributedCannon__flyTask, self.taskName('flyTask'))
        shootTask.info = info
        flyTask.info = info
        seqTask = Task.sequence(shootTask, smokeTask, flyTask)
        taskMgr.add(seqTask, self.taskName('flyingToon') + '-' + str(avId))
        self.acceptOnce(self.uniqueName('stopFlyTask'), self._DistributedCannon__stopFlyTask)
        return Task.done

    
    def _DistributedCannon__stopFlyTask(self, avId):
        taskMgr.remove(self.taskName('flyingToon') + '-' + str(avId))

    
    def b_setLanded(self):
        self.d_setLanded()

    
    def d_setLanded(self):
        self.notify.debug('localTOonshooting = %s' % self.localToonShooting)
        if self.localToonShooting:
            self.sendUpdate('setLanded', [])
        

    
    def setLanded(self):
        self.removeAvFromCannon()

    
    def removeAvFromCannon(self):
        if self.av != None:
            self._DistributedCannon__stopCollisionHandler(self.av)
            self.av.resetLOD()
            place = base.cr.playGame.getPlace()
            if self.av == base.localAvatar:
                if place:
                    place.setState('walk')
                
            
            if self.inWater:
                self.av.loop('swim')
                place.forceUnderWater()
            else:
                self.av.loop('neutral')
            self.inWater = 0
            self.av.setPlayRate(1.0, 'run')
            self.av.nametag.removeNametag(self.toonHead.tag)
            if self.av.getParent().getName() == 'toonOriginChange':
                self.av.wrtReparentTo(render)
                self._DistributedCannon__setToonUpright(self.av)
            
            if self.av == base.localAvatar:
                self.av.startPosHprBroadcast()
            
            self.av.startSmooth()
            self.av.setScale(1, 1, 1)
            self.ignore(self.av.uniqueName('disable'))
            self._DistributedCannon__destroyToonModels()
        

    
    def _DistributedCannon__stopCollisionHandler(self, avatar):
        if avatar:
            avatar.loop('neutral')
            if self.flyColNode:
                self.flyColNode = None
            
            if avatar == base.localAvatar:
                avatar.collisionsOn()
            
            self.flyColSphere = None
            if self.flyColNodePath:
                base.cTrav.removeCollider(self.flyColNodePath)
                self.flyColNodePath.removeNode()
                self.flyColNodePath = None
            
            self.handler = None
        

    
    def _DistributedCannon__handleCannonHit(self, collisionEntry):
        if self.av == None or self.flyColNode == None:
            return None
        
        hitNode = collisionEntry.getIntoNode().getName()
        vel = self.vel
        vel = render.getRelativeVector(self.av, vel)
        vel.normalize()
        space = collisionEntry.getIntoMat()
        intoNormal = collisionEntry.getSurfaceNormal(collisionEntry.getIntoNodePath())
        hitNormal = space.xformVec(intoNormal)
        if hitNode.find('cSphere') == 0 and hitNode.find('treasureSphere') == 0 and hitNode.find('prop') == 0 and hitNode.find('distAvatarCollNode') == 0 and hitNode.find('CannonSphere') == 0 or hitNode.find('flySphere') == 0:
            print '--------------hit and ignoring %s' % hitNode
            return None
        
        if vel.dot(hitNormal) > 0:
            print '--------------hit and ignoring backfacing %s, dot=%s' % (hitNode, vel.dot(hitNormal))
            return None
        
        if 1:
            intoNode = collisionEntry.getIntoNodePath()
            if not (hitNode in [
                'collision_house',
                'collision_fence',
                'targetSphere']):
                self._DistributedCannon__stopCollisionHandler(self.av)
                self._DistributedCannon__stopFlyTask(self.avId)
                if self.hitTarget == 0:
                    messenger.send('missedTarget')
                
            elif hitNode == 'collision_house' or hitNode == 'collision_fence':
                self._DistributedCannon__hitHouse(self.av, collisionEntry)
            elif hitNode == 'targetSphere':
                self._DistributedCannon__hitTarget(self.av, collisionEntry, [
                    vel])
            else:
                self.notify.debug('*************** hit something else ************')
            return None
            if self.localToonShooting:
                camera.wrtReparentTo(render)
            
            if self.dropShadow:
                self.dropShadow.reparentTo(hidden)
            
            pos = collisionEntry.getIntoIntersectionPoint()
            hpr = self.av.getHpr()
            hitPos = space.xformPoint(pos)
            pos = hitPos
            self.landingPos = pos
            print 'hitNode,Normal = %s,%s' % (hitNode, intoNormal)
            track = Sequence()
            track.append(Func(self.av.wrtReparentTo, render))
            if self.localToonShooting:
                track.append(Func(self.av.collisionsOff))
            
            if hitNode in [
                'matCollisions',
                'collision1',
                'floor']:
                track.append(Func(self._DistributedCannon__hitGround, self.av, pos))
                track.append(Wait(1.0))
                track.append(Func(self._DistributedCannon__setToonUpright, self.av, self.landingPos))
            elif hitNode == 'collision_house':
                track.append(Func(self._DistributedCannon__hitHouse, self.av, collisionEntry))
            elif hitNode == 'collision_fence' or hitNode == 'collision4':
                track.append(Func(self._DistributedCannon__hitHouse, self.av, collisionEntry))
            elif hitNode == 'targetSphere':
                track.append(Func(self._DistributedCannon__hitHouse, self.av, collisionEntry))
            elif hitNode == 'collision3':
                track.append(Func(self._DistributedCannon__hitWater, self.av, pos, collisionEntry))
                track.append(Wait(2.0))
                track.append(Func(self._DistributedCannon__setToonUpright, self.av, self.landingPos))
            elif hitNode == 'roofOutside' and hitNode == 'collision_roof' or hitNode == 'roofclision':
                track.append(Func(self._DistributedCannon__hitRoof, self.av, collisionEntry))
                track.append(Wait(2.0))
                track.append(Func(self._DistributedCannon__setToonUpright, self.av, self.landingPos))
            elif hitNode.find('MovingPlatform') == 0 or hitNode.find('cloudSphere') == 0:
                track.append(Func(self._DistributedCannon__hitCloudPlatform, self.av, collisionEntry))
            
            track.append(Func(self.b_setLanded))
            if self.localToonShooting:
                track.append(Func(self.av.collisionsOn))
            
            if self.hitTrack:
                self.hitTrack.finish()
            
            self.hitTrack = track
            self.hitTrack.start()
        

    
    def _DistributedCannon__hitGround(self, avatar, pos, extraArgs = []):
        hitP = avatar.getPos(render)
        print 'hitGround pos = %s, hitP = %s' % (pos, hitP)
        print 'avatar hpr = %s' % avatar.getHpr()
        h = self.barrel.getH(render)
        avatar.setPos(pos[0], pos[1], pos[2] + avatar.getHeight() / 3.0)
        avatar.setHpr(h, -135, 0)
        print 'parent = %s' % avatar.getParent()
        print 'new pos,hpr = %s,%s' % (avatar.getPos(render), avatar.getHpr(render))
        self.dustCloud.setPos(render, pos[0], pos[1], pos[2] + avatar.getHeight() / 3.0)
        self.dustCloud.setScale(0.34999999999999998)
        self.dustCloud.play()
        base.playSfx(self.sndHitGround)
        avatar.setPlayRate(2.0, 'run')
        avatar.loop('run')

    
    def _DistributedCannon__hitHouse(self, avatar, collisionEntry, extraArgs = []):
        self._DistributedCannon__hitBumper(avatar, collisionEntry, self.sndHitHouse, kr = 0.20000000000000001, angVel = 3)

    
    def _DistributedCannon__hitTarget(self, avatar, collisionEntry, extraArgs = []):
        self._DistributedCannon__hitBumper(avatar, collisionEntry, self.sndHitHouse, kr = 0.10000000000000001, angVel = 2)
        if self.localToonShooting:
            self.hitTarget = 1
            messenger.send('hitTarget', [
                self.avId,
                self.lastVel])
        

    
    def _DistributedCannon__hitBumper(self, avatar, collisionEntry, sound, kr = 0.59999999999999998, angVel = 1):
        self.hitBumper = 1
        base.playSfx(self.sndHitHouse)
        hitP = avatar.getPos(render)
        self.lastPos = hitP
        house = collisionEntry.getIntoNodePath()
        normal = collisionEntry.getSurfaceNormal(house)
        normal.normalize()
        space = collisionEntry.getIntoMat()
        normal = space.xformVec(normal)
        vel = self.vel
        vel = render.getRelativeVector(self.av, vel)
        speed = vel.length()
        if self.deltaT > 1.0000000000000001e-005:
            speed = vel.length() / self.deltaT
        
        vel.normalize()
        newVel = (normal * 2.0 + vel) * kr * speed
        self.lastVel = newVel
        self.angularVel = angVel * 360
        t = Sequence(Func(avatar.pose, 'lose', 110))
        t.start()

    
    def _DistributedCannon__hitRoof(self, avatar, collisionEntry, extraArgs = []):
        np = collisionEntry.getIntoNodePath()
        roof = np.getParent()
        normal = collisionEntry.getSurfaceNormal(np)
        normal.normalize()
        vel = self.trajectory.getVel(self.t)
        vel.normalize()
        dot = normal.dot(vel)
        print '--------------dot product = %s---------------' % dot
        temp = render.attachNewNode('temp')
        temp.iPosHpr()
        temp.lookAt(Point3(normal))
        temp.reparentTo(roof)
        print 'avatar pos = %s, landingPos = %s' % (avatar.getPos(), self.landingPos)
        temp.setPos(render, self.landingPos)
        avatar.reparentTo(temp)
        avatar.setPosHpr(0, 0.25, 0.5, 0, 270, 180)
        avatar.pose('slip-forward', 25)
        base.playSfx(self.sndHitHouse)
        avatar.setPlayRate(1.0, 'jump')
        h = self.barrel.getH(render)
        t = Sequence(LerpPosInterval(avatar, 0.5, Point3(0, 0, -0.5), blendType = 'easeInOut'), Func(avatar.clearColorScale), Func(avatar.wrtReparentTo, render), Wait(0.29999999999999999), Parallel(Func(avatar.setP, 0), Func(avatar.play, 'jump', None, 19, 39), LerpHprInterval(avatar, 0.29999999999999999, Vec3(h, 0, 0), blendType = 'easeOut')), Func(avatar.play, 'neutral'))
        t.start()
        hitP = avatar.getPos(render)

    
    def _DistributedCannon__hitBridge(self, avatar, collisionEntry, extraArgs = []):
        print 'hit bridge'
        hitP = avatar.getPos(render)
        self.dustCloud.setPos(render, hitP[0], hitP[1], hitP[2] - 0.5)
        self.dustCloud.setScale(0.34999999999999998)
        self.dustCloud.play()
        base.playSfx(self.sndHitGround)

    
    def _DistributedCannon__hitWater(self, avatar, pos, collisionEntry, extraArgs = []):
        hitP = avatar.getPos(render)
        if hitP[2] > ToontownGlobals.EstateWakeWaterHeight:
            self.notify.debug('we hit the ground before we hit water')
            self._DistributedCannon__hitGround(avatar, pos, extraArgs)
            return None
        
        self.inWater = 1
        print 'hit water'
        hitP = avatar.getPos(render)
        avatar.loop('neutral')
        self.splash.setPos(hitP)
        self.splash.setZ(ToontownGlobals.EstateWakeWaterHeight)
        self.splash.setScale(2)
        self.splash.play()
        base.playSfx(self.sndHitWater)
        place = base.cr.playGame.getPlace()
        print 'hitWater: submerged = %s' % place.toonSubmerged
        avatar.loop('swim')

    
    def _DistributedCannon__hitCloudPlatform(self, avatar, collisionEntry, extraArgs = []):
        avatar.reparentTo(collisionEntry.getIntoNodePath())
        h = self.barrel.getH(render)
        avatar.setPosHpr(0, 0, 0, h, 0, 0)
        messenger.send('hitCloud')

    
    def _DistributedCannon__setToonUpright(self, avatar, pos = None):
        if avatar:
            if not pos:
                pos = avatar.getPos(render)
            
            avatar.setPos(render, pos)
            avatar.loop('neutral')
            if not (self.inWater):
                h = self.barrel.getH(render)
                p = Point3(self.vel[0], self.vel[1], self.vel[2])
                print 'lookat = %s' % p
                avatar.lookAt(self.cannon)
                avatar.setP(0)
                avatar.setR(0)
            else:
                pos -= Vec3(0, 0, 1)
                avatar.setPos(pos)
                avatar.setHpr(60, 0, 0)
            avatar.setScale(1, 1, 1)
        

    
    def _DistributedCannon__calcToonImpact(self, trajectory):
        t_groundImpact = trajectory.checkCollisionWithGround(GROUND_PLANE_MIN)
        if t_groundImpact >= trajectory.getStartTime():
            return (t_groundImpact, self.HIT_GROUND)
        else:
            self.notify.error('__calcToonImpact: toon never impacts ground?')
            return (0.0, self.HIT_GROUND)

    
    def _DistributedCannon__calcHitTreasures(self, trajectory):
        estate = self.cr.doId2do.get(self.estateId)
        self.hitTreasures = []
        if estate:
            doIds = estate.flyingTreasureId
            for id in doIds:
                t = self.cr.doId2do.get(id)
                if t:
                    pos = t.pos
                    rad = 10.5
                    height = 10.0
                    t_impact = trajectory.checkCollisionWithCylinderSides(pos, rad, height)
                    if t_impact > 0:
                        self.hitTreasures.append([
                            t_impact,
                            t])
                    
                
            
        
        del estate
        return None

    
    def _DistributedCannon__shootTask(self, task):
        base.playSfx(self.sndCannonFire)
        self.dropShadow.reparentTo(render)
        return Task.done

    
    def _DistributedCannon__smokeTask(self, task):
        self.smoke.reparentTo(self.barrel)
        self.smoke.setPos(0, 6, -3)
        self.smoke.setScale(0.5)
        self.smoke.wrtReparentTo(render)
        track = Sequence(Parallel(LerpScaleInterval(self.smoke, 0.5, 3), LerpColorScaleInterval(self.smoke, 0.5, Vec4(2, 2, 2, 0))), Func(self.smoke.reparentTo, hidden), Func(self.smoke.clearColorScale))
        track.start()
        return Task.done

    
    def _DistributedCannon__flyTask(self, task):
        toon = task.info['toon']
        if toon.isEmpty():
            self._DistributedCannon__resetToonToCannon(self.av)
            return Task.done
        
        curTime = task.time + task.info['launchTime']
        t = min(curTime, task.info['timeOfImpact'])
        self.lastT = self.t
        self.t = t
        deltaT = self.t - self.lastT
        self.deltaT = deltaT
        if t >= task.info['timeOfImpact']:
            self._DistributedCannon__resetToonToCannon(self.av)
            return Task.done
        
        if self.hitBumper:
            pos = self.lastPos + self.lastVel * deltaT
            vel = self.lastVel
            self.lastVel += Vec3(0, 0, -32.0) * deltaT
            self.lastPos = pos
            toon.setPos(pos)
            lastH = toon.getH()
            toon.setH(lastH + deltaT * self.angularVel)
            view = 0
        else:
            pos = task.info['trajectory'].getPos(t)
            toon.setFluidPos(pos)
            shadowPos = Point3(pos)
            shadowPos.setZ(SHADOW_Z_OFFSET)
            self.dropShadow.setPos(shadowPos)
            vel = task.info['trajectory'].getVel(t)
            run = math.sqrt(vel[0] * vel[0] + vel[1] * vel[1])
            rise = vel[2]
            theta = self._DistributedCannon__toDegrees(math.atan(rise / run))
            toon.setHpr(self.cannon.getH(render), -90 + theta, 0)
            view = 2
        lookAt = task.info['toon'].getPos(render)
        hpr = task.info['toon'].getHpr(render)
        if self.localToonShooting:
            if view == 0:
                camera.wrtReparentTo(render)
                camera.lookAt(lookAt)
            elif view == 1:
                camera.reparentTo(render)
                camera.setPos(render, 100, 100, 35.25)
                camera.lookAt(render, lookAt)
            elif view == 2:
                if hpr[1] > -90:
                    camera.setPos(0, 0, -30)
                    if camera.getZ() < lookAt[2]:
                        camera.setZ(render, lookAt[2] + 10)
                    
                    camera.lookAt(Point3(0, 0, 0))
                
            
            self._DistributedCannon__pickupTreasures(t)
        
        return Task.cont

    
    def _DistributedCannon__pickupTreasures(self, t):
        updatedList = []
        for tList in self.hitTreasures:
            if t > tList[0]:
                messenger.send(tList[1].uniqueName('entertreasureSphere'))
                print 'hit something!'
            else:
                updatedList.append(tList)
        
        self.hitTreasures = updatedList

    
    def _DistributedCannon__resetToonToCannon(self, avatar):
        pos = None
        if not avatar:
            if self.avId:
                avatar = base.cr.doId2do.get(self.avId, None)
            
        
        if avatar:
            if self.cannon:
                avatar.reparentTo(self.cannon)
                avatar.setPos(2, -4, 0)
                avatar.wrtReparentTo(render)
            
            self._DistributedCannon__resetToon(avatar)
        

    
    def _DistributedCannon__resetToon(self, avatar, pos = None):
        if avatar:
            self._DistributedCannon__stopCollisionHandler(avatar)
            self._DistributedCannon__setToonUpright(avatar, pos)
            if self.localToonShooting:
                self.notify.debug('toon setting position to %s' % pos)
                if pos:
                    base.localAvatar.setPos(pos)
                
                camera.reparentTo(avatar)
            
            self.b_setLanded()
        

    
    def setActiveState(self, active):
        self.notify.debug('got setActiveState(%s)' % active)
        if active and not (self.cannonsActive):
            self.activateCannons()
        elif not active and self.cannonsActive:
            self.deActivateCannons()
        

    
    def enterInit(self):
        self.nextKey = 'up'
        self.nextState = 'u1'

    
    def exitInit(self):
        pass

    
    def enteru1(self):
        self.nextKey = 'up'
        self.nextState = 'u2'

    
    def exitu1(self):
        pass

    
    def enteru2(self):
        self.nextKey = 'down'
        self.nextState = 'd3'

    
    def exitu2(self):
        pass

    
    def enterd3(self):
        self.nextKey = 'down'
        self.nextState = 'd4'

    
    def exitd3(self):
        pass

    
    def enterd4(self):
        self.nextKey = 'left'
        self.nextState = 'l5'

    
    def exitd4(self):
        pass

    
    def enterl5(self):
        self.nextKey = 'right'
        self.nextState = 'r6'

    
    def exitl5(self):
        pass

    
    def enterr6(self):
        self.nextKey = 'left'
        self.nextState = 'l7'

    
    def exitr6(self):
        pass

    
    def enterl7(self):
        self.nextKey = 'right'
        self.nextState = 'r8'

    
    def exitl7(self):
        pass

    
    def enterr8(self):
        self.nextKey = None
        self.nextState = ''
        self.codeFSM.request('acceptCode')

    
    def exitr8(self):
        pass

    
    def enterAcceptCode(self):
        if not (self.cannonsActive):
            self.activateCannons()
            self.sendUpdate('setActive', [
                1])
        else:
            self.deActivateCannons()
            self.sendUpdate('setActive', [
                0])
        self.codeFSM.request('init')

    
    def exitAcceptCode(self):
        pass

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def handleCodeKey(self, key):
        if self.nextKey and self.nextState:
            if key == self.nextKey:
                self.codeFSM.request(self.nextState)
            else:
                self.codeFSM.request('init')
        


