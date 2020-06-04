# File: D (Python 2.2)

import ToontownGlobals
import PhoneGlobals
import CatalogScreen
import CatalogItem
import ToontownDialog
import Localizer
import DistributedHouseInterior
import Actor
import DistributedFurnitureItem
import ClockDelta
import PythonUtil
import Rope
from DirectNotifyGlobal import *
from PandaModules import *
from IntervalGlobal import *
import string

class DistributedPhone(DistributedFurnitureItem.DistributedFurnitureItem):
    notify = directNotify.newCategory('DistributedPhone')
    movieDelay = 0.5
    
    def __init__(self, cr):
        DistributedFurnitureItem.DistributedFurnitureItem.__init__(self, cr)
        self.lastAvId = 0
        self.lastTime = 0
        self.initialScale = None
        self.usedInitialScale = 0
        self.toonScale = None
        self.phoneGui = None
        self.phoneDialog = None
        self.model = None
        self.cord = None
        self.receiverGeom = None
        self.receiverJoint = None
        self.phoneSphereEvent = 'phoneSphere'
        self.phoneSphereEnterEvent = 'enter' + self.phoneSphereEvent
        self.phoneGuiDoneEvent = 'phoneGuiDone'
        self.pickupMovieDoneEvent = 'phonePickupDone'
        self.numHouseItems = None
        self.interval = None
        self.intervalAvatar = None
        self.phoneInUse = 0
        self.origToonHpr = None

    
    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        self.accept(self.phoneSphereEnterEvent, self._DistributedPhone__handleEnterSphere)
        self.load()

    
    def loadModel(self):
        self.model = Actor.Actor('phase_5.5/models/estate/prop_phone-mod', {
            'SS_phoneOut': 'phase_5.5/models/estate/prop_phone-SS_phoneOut',
            'SS_takePhone': 'phase_5.5/models/estate/prop_phone-SS_takePhone',
            'SS_phoneNeutral': 'phase_5.5/models/estate/prop_phone-SS_phoneNeutral',
            'SS_phoneBack': 'phase_5.5/models/estate/prop_phone-SS_phoneBack',
            'SM_phoneOut': 'phase_5.5/models/estate/prop_phone-SM_phoneOut',
            'SM_takePhone': 'phase_5.5/models/estate/prop_phone-SM_takePhone',
            'SM_phoneNeutral': 'phase_5.5/models/estate/prop_phone-SM_phoneNeutral',
            'SM_phoneBack': 'phase_5.5/models/estate/prop_phone-SM_phoneBack',
            'SL_phoneOut': 'phase_5.5/models/estate/prop_phone-SL_phoneOut',
            'SL_takePhone': 'phase_5.5/models/estate/prop_phone-SL_takePhone',
            'SL_phoneNeutral': 'phase_5.5/models/estate/prop_phone-SL_phoneNeutral',
            'SL_phoneBack': 'phase_5.5/models/estate/prop_phone-SL_phoneBack',
            'MS_phoneOut': 'phase_5.5/models/estate/prop_phone-MS_phoneOut',
            'MS_takePhone': 'phase_5.5/models/estate/prop_phone-MS_takePhone',
            'MS_phoneNeutral': 'phase_5.5/models/estate/prop_phone-MS_phoneNeutral',
            'MS_phoneBack': 'phase_5.5/models/estate/prop_phone-MS_phoneBack',
            'MM_phoneOut': 'phase_5.5/models/estate/prop_phone-MM_phoneOut',
            'MM_takePhone': 'phase_5.5/models/estate/prop_phone-MM_takePhone',
            'MM_phoneNeutral': 'phase_5.5/models/estate/prop_phone-MM_phoneNeutral',
            'MM_phoneBack': 'phase_5.5/models/estate/prop_phone-MM_phoneBack',
            'ML_phoneOut': 'phase_5.5/models/estate/prop_phone-ML_phoneOut',
            'ML_takePhone': 'phase_5.5/models/estate/prop_phone-ML_takePhone',
            'ML_phoneNeutral': 'phase_5.5/models/estate/prop_phone-ML_phoneNeutral',
            'ML_phoneBack': 'phase_5.5/models/estate/prop_phone-ML_phoneBack',
            'LS_phoneOut': 'phase_5.5/models/estate/prop_phone-LS_phoneOut',
            'LS_takePhone': 'phase_5.5/models/estate/prop_phone-LS_takePhone',
            'LS_phoneNeutral': 'phase_5.5/models/estate/prop_phone-LS_phoneNeutral',
            'LS_phoneBack': 'phase_5.5/models/estate/prop_phone-LS_phoneBack',
            'LM_phoneOut': 'phase_5.5/models/estate/prop_phone-LM_phoneOut',
            'LM_takePhone': 'phase_5.5/models/estate/prop_phone-LM_takePhone',
            'LM_phoneNeutral': 'phase_5.5/models/estate/prop_phone-LM_phoneNeutral',
            'LM_phoneBack': 'phase_5.5/models/estate/prop_phone-LM_phoneBack',
            'LL_phoneOut': 'phase_5.5/models/estate/prop_phone-LL_phoneOut',
            'LL_takePhone': 'phase_5.5/models/estate/prop_phone-LL_takePhone',
            'LL_phoneNeutral': 'phase_5.5/models/estate/prop_phone-LL_phoneNeutral',
            'LL_phoneBack': 'phase_5.5/models/estate/prop_phone-LL_phoneBack' })
        self.model.pose('SS_phoneOut', 0)
        self.receiverJoint = self.model.find('**/joint_receiver')
        self.receiverGeom = self.receiverJoint.getChild(0)
        mount = loader.loadModel('phase_5.5/models/estate/phoneMount-mod')
        mount.setTransparency(0, 1)
        self.model.reparentTo(mount)
        self.ringSfx = loader.loadSfx('phase_3.5/audio/sfx/telephone_ring.mp3')
        self.handleSfx = loader.loadSfx('phase_5.5/audio/sfx/telephone_handle2.mp3')
        self.hangUpSfx = loader.loadSfx('phase_5.5/audio/sfx/telephone_hang_up.mp3')
        self.pickUpSfx = loader.loadSfx('phase_5.5/audio/sfx/telephone_pickup1.mp3')
        if self.initialScale:
            mount.setScale(*self.initialScale)
            self.usedInitialScale = 1
        
        phoneSphere = CollisionSphere(0, -0.66000000000000003, 0, 0.20000000000000001)
        phoneSphere.setTangible(0)
        phoneSphereNode = CollisionNode(self.phoneSphereEvent)
        phoneSphereNode.setIntoCollideMask(ToontownGlobals.WallBitmask)
        phoneSphereNode.addSolid(phoneSphere)
        mount.attachNewNode(phoneSphereNode)
        if not self.model.find('**/CurveNode7').isEmpty():
            self.setupCord()
        
        return mount

    
    def setupCamera(self, mode):
        camera.wrtReparentTo(render)
        if mode == PhoneGlobals.PHONE_MOVIE_PICKUP:
            camera.lerpPosHpr(4, -4, toonbase.localToon.getHeight() - 0.5, 35, -8, 0, 1, other = toonbase.localToon, blendType = 'easeOut', task = self.uniqueName('lerpCamera'))
        

    
    def setupCord(self):
        if self.cord:
            self.cord.detachNode()
            self.cord = None
        
        self.cord = Rope.Rope(self.uniqueName('phoneCord'))
        self.cord.setColor(0, 0, 0, 1)
        self.cord.setup(4, ((self.receiverGeom, (0, 0, 0)), (self.model.find('**/joint_curveNode1'), (0, 0, 0)), (self.model.find('**/joint_curveNode2'), (0, 0, 0)), (self.model.find('**/joint_curveNode3'), (0, 0, 0)), (self.model.find('**/joint_curveNode4'), (0, 0, 0)), (self.model.find('**/joint_curveNode5'), (0, 0, 0)), (self.model.find('**/joint_curveNode6'), (0, 0, 0)), (self.model.find('**/CurveNode7'), (0, 0, 0))))
        self.cord.reparentTo(self.model)
        self.cord.node().setBound(BoundingSphere(Point3(-1.0, -3.2000000000000002, 2.6000000000000001), 2.0))

    
    def disable(self):
        self.notify.debug('disable')
        if self.interval:
            self.interval.finish()
            self.interval = None
        
        self.intervalAvatar = None
        if self.phoneGui:
            self.phoneGui.hide()
            self.phoneGui.unload()
            self.phoneGui = None
        
        if self.phoneDialog:
            self.phoneDialog.cleanup()
            self.phoneDialog = None
        
        self._DistributedPhone__receiverToPhone()
        self.ignoreAll()
        DistributedFurnitureItem.DistributedFurnitureItem.disable(self)

    
    def delete(self):
        self.notify.debug('delete')
        self.model.cleanup()
        DistributedFurnitureItem.DistributedFurnitureItem.delete(self)

    
    def setInitialScale(self, sx, sy, sz):
        self.initialScale = (sx, sy, sz)
        if not (self.usedInitialScale) and self.model:
            self.setScale(*self.initialScale)
            self.usedInitialScale = 1
        

    
    def _DistributedPhone__handleEnterSphere(self, collEntry):
        if toonbase.localToon.doId == self.lastAvId and globalClock.getFrameTime() <= self.lastTime + 0.5:
            self.notify.info('Ignoring duplicate entry for avatar.')
            return None
        
        self.notify.debug('Entering Phone Sphere....')
        self.ignore(self.phoneSphereEnterEvent)
        self.cr.playGame.getPlace().detectedPhoneCollision()
        self.sendUpdate('avatarEnter', [])

    
    def _DistributedPhone__handlePhoneDone(self):
        self.sendUpdate('avatarExit', [])
        self.ignore(self.phoneGuiDoneEvent)
        self.phoneGui = None

    
    def freeAvatar(self):
        toonbase.localToon.speed = 0
        taskMgr.remove(self.uniqueName('lerpCamera'))
        toonbase.localToon.posCamera(0, 0)
        toonbase.tcr.playGame.getPlace().setState('walk')
        self.ignore(self.pickupMovieDoneEvent)
        self.accept(self.phoneSphereEnterEvent, self._DistributedPhone__handleEnterSphere)
        self.lastTime = globalClock.getFrameTime()

    
    def setLimits(self, numHouseItems):
        self.numHouseItems = numHouseItems

    
    def setMovie(self, mode, avId, timestamp):
        elapsed = ClockDelta.globalClockDelta.localElapsedTime(timestamp, bits = 32)
        elapsed = max(elapsed - self.movieDelay, 0)
        self.ignore(self.pickupMovieDoneEvent)
        if avId != 0:
            self.lastAvId = avId
        
        self.lastTime = globalClock.getFrameTime()
        isLocalToon = avId == toonbase.localToon.doId
        avatar = self.cr.doId2do.get(avId)
        self.notify.info('setMovie: %s %s %s' % (mode, avId, isLocalToon))
        if mode == PhoneGlobals.PHONE_MOVIE_CLEAR:
            self.notify.debug('setMovie: clear')
            self.numHouseItems = None
            if self.phoneInUse:
                self.clearInterval()
            
            self.phoneInUse = 0
        elif mode == PhoneGlobals.PHONE_MOVIE_EMPTY:
            self.notify.debug('setMovie: empty')
            if isLocalToon:
                self.phoneDialog = ToontownDialog.ToontownDialog(dialogName = 'PhoneEmpty', style = ToontownDialog.Acknowledge, text = Localizer.DistributedPhoneEmpty, text_wordwrap = 15, fadeScreen = 1, command = self._DistributedPhone__clearDialog)
            
            self.numHouseItems = None
            self.phoneInUse = 0
        elif mode == PhoneGlobals.PHONE_MOVIE_PICKUP:
            self.notify.debug('setMovie: gui')
            if avatar:
                interval = self.takePhoneInterval(avatar)
                if isLocalToon:
                    self.setupCamera(mode)
                    interval.setDoneEvent(self.pickupMovieDoneEvent)
                    self.acceptOnce(self.pickupMovieDoneEvent, self._DistributedPhone__showPhoneGui)
                
                self.playInterval(interval, elapsed, avatar)
                self.phoneInUse = 1
            
        elif mode == PhoneGlobals.PHONE_MOVIE_HANGUP:
            self.notify.debug('setMovie: gui')
            if avatar:
                interval = self.replacePhoneInterval(avatar)
                self.playInterval(interval, elapsed, avatar)
            
            self.numHouseItems = None
            self.phoneInUse = 0
        else:
            self.notify.warning('unknown mode in setMovie: %s' % mode)

    
    def _DistributedPhone__showPhoneGui(self):
        if self.toonScale:
            self.sendUpdate('setNewScale', [
                self.toonScale[0],
                self.toonScale[1],
                self.toonScale[2]])
        
        self.phoneGui = CatalogScreen.CatalogScreen(phone = self, doneEvent = self.phoneGuiDoneEvent)
        self.phoneGui.show()
        self.accept(self.phoneGuiDoneEvent, self._DistributedPhone__handlePhoneDone)

    
    def requestPurchase(self, item, callback, optional = -1):
        blob = item.getBlob(store = CatalogItem.Customization)
        context = self.getCallbackContext(callback, [
            item])
        self.sendUpdate('requestPurchaseMessage', [
            context,
            blob,
            optional])

    
    def requestPurchaseResponse(self, context, retcode):
        self.doCallbackContext(context, [
            retcode])

    
    def _DistributedPhone__clearDialog(self, event):
        self.phoneDialog.cleanup()
        self.phoneDialog = None
        self.freeAvatar()

    
    def takePhoneInterval(self, toon):
        torso = string.upper(toon.style.torso[0])
        legs = string.upper(toon.style.legs[0])
        phoneOutAnim = '%s%s_phoneOut' % (torso, legs)
        takePhoneAnim = '%s%s_takePhone' % (torso, legs)
        phoneNeutralAnim = '%s%s_phoneNeutral' % (torso, legs)
        self.toonScale = toon.getGeomNode().getChild(0).getScale(self.getParent())
        walkTime = 1.0
        scaleTime = 1.0
        origScale = self.getScale()
        origToonPos = toon.getPos()
        origToonHpr = toon.getHpr()
        self.origToonHpr = origToonHpr
        self.setScale(self.toonScale)
        toon.setPosHpr(self, 0, -4.5, 0, 0, 0, 0)
        destToonPos = toon.getPos()
        destToonHpr = toon.getHpr()
        destToonHpr = VBase3(PythonUtil.fitSrcAngle2Dest(destToonHpr[0], origToonHpr[0]), destToonHpr[1], destToonHpr[2])
        self.setScale(origScale)
        toon.setPos(origToonPos)
        toon.setHpr(origToonHpr)
        walkToPhone = Sequence(Func(toon.stopSmooth), Func(toon.loop, 'walk'), Func(base.playSfx, toonbase.localToon.soundWalk), toon.posHprInterval(walkTime, destToonPos, destToonHpr, blendType = 'easeInOut'), Func(toon.loop, 'neutral'), Func(toon.startSmooth))
        interval = Sequence(Parallel(walkToPhone, ActorInterval(self.model, phoneOutAnim), self.scaleInterval(scaleTime, self.toonScale, blendType = 'easeInOut')), Parallel(ActorInterval(self.model, takePhoneAnim), ActorInterval(toon, 'takePhone'), Sequence(Wait(0.625), Func(base.playSfx, self.pickUpSfx), Func(self._DistributedPhone__receiverToHand, toon), Wait(1), Func(base.playSfx, self.handleSfx))), Func(self.model.loop, phoneNeutralAnim), Func(toon.loop, 'phoneNeutral'), Func(base.playSfx, self.ringSfx))
        return interval

    
    def replacePhoneInterval(self, toon):
        torso = string.upper(toon.style.torso[0])
        legs = string.upper(toon.style.legs[0])
        phoneBackAnim = '%s%s_phoneBack' % (torso, legs)
        scaleTime = 1.0
        interval = Sequence(Parallel(ActorInterval(self.model, phoneBackAnim), ActorInterval(toon, 'phoneBack'), Sequence(Wait(1.0), Func(self._DistributedPhone__receiverToPhone), Func(base.playSfx, self.hangUpSfx))), Func(toon.loop, 'neutral'))
        if self.origToonHpr:
            interval.append(Func(toon.setHpr, self.origToonHpr))
            self.origToonHpr = None
        
        if toon == toonbase.localToon:
            interval.append(Func(self.freeAvatar))
        
        return interval

    
    def _DistributedPhone__receiverToHand(self, toon):
        self.receiverGeom.reparentTo(toon.leftHand)
        self.receiverGeom.setPosHpr(0.090681300000000006, 0.38037500000000002, 0.10000000000000001, 8.66615, -73.588200000000001, -166.81700000000001)

    
    def _DistributedPhone__receiverToPhone(self):
        self.receiverGeom.reparentTo(self.receiverJoint)
        self.receiverGeom.setPosHpr(0, 0, 0, 0, 0, 0)

    
    def playInterval(self, interval, elapsed, avatar):
        if self.interval != None:
            self.interval.finish()
            self.interval = None
        
        self.interval = interval
        self.interval.start(elapsed)
        if self.intervalAvatar != avatar:
            if self.intervalAvatar:
                self.ignore(self.intervalAvatar.uniqueName('disable'))
            
            if avatar:
                self.accept(avatar.uniqueName('disable'), self.clearInterval)
            
            self.intervalAvatar = avatar
        

    
    def clearInterval(self):
        if self.interval != None:
            self.interval.finish()
            self.interval = None
        
        if self.intervalAvatar:
            self.ignore(self.intervalAvatar.uniqueName('disable'))
            self.intervalAvatar = None
        
        self._DistributedPhone__receiverToPhone()
        self.model.pose('SS_phoneOut', 0)
        self.phoneInUse = 0

