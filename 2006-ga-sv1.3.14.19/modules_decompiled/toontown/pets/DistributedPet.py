# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.PythonUtil import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedSmoothNode
from direct.distributed.ClockDelta import globalClockDelta
from direct.distributed.MsgTypes import *
from direct.task import Task
from otp.otpbase import OTPGlobals
from toontown.pets import Pet, PetBase, PetTraits, PetConstants, PetManager, PetAvatarPanel
from toontown.pets import PetMood, PetTricks
from toontown.hood import ZoneUtil
from toontown.toonbase import TTLocalizer
from direct.distributed import DelayDelete
import random
if __dev__:
    import pdb

BeanColors = (VBase4(1.0, 0.20000000000000001, 0.20000000000000001, 1.0), VBase4(0.20000000000000001, 1.0, 0.20000000000000001, 1.0), VBase4(0.20000000000000001, 0.20000000000000001, 1.0, 1.0), VBase4(0.0, 1.0, 1.0, 1.0), VBase4(1.0, 1.0, 0.0, 1.0), VBase4(1.0, 0.59999999999999998, 1.0, 1.0), VBase4(0.59999999999999998, 0.0, 0.59999999999999998, 1.0))

class DistributedPet(DistributedSmoothNode.DistributedSmoothNode, Pet.Pet, PetBase.PetBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPet')
    swallowSfx = None
    callSfx = None
    petSfx = None
    
    def __init__(self, cr, bFake = False):
        DistributedSmoothNode.DistributedSmoothNode.__init__(self, cr)
        Pet.Pet.__init__(self)
        self.bFake = bFake
        if not (self.swallowSfx):
            self.swallowSfx = loader.loadSfx('phase_5.5/audio/sfx/beg_eat_swallow.mp3')
        
        if not (self.callSfx):
            self.callSfx = loader.loadSfx('phase_5.5/audio/sfx/call_pet.mp3')
        
        if not (self.petSfx):
            self.petSfx = loader.loadSfx('phase_5.5/audio/sfx/pet_the_pet.mp3')
        
        self.isLocalToon = 0
        self.inWater = 0
        self._DistributedPet__funcsToDelete = []
        self._DistributedPet__generateDistTraitFuncs()
        self._DistributedPet__generateDistMoodFuncs()

    
    def generate(self):
        DistributedPet.notify.debug('generate(), fake=%s' % self.bFake)
        if not (self.bFake):
            PetManager.acquirePetManager()
        
        DistributedSmoothNode.DistributedSmoothNode.generate(self)
        self.trickIval = None
        self.movieTrack = None
        self.traitList = [
            0] * PetTraits.PetTraits.NumTraits
        self.requiredMoodComponents = { }

    
    def getDisplayPrefix(self):
        return 'pet%s' % self.doId

    
    def display(self, key, value, category = ''):
        if self.bFake:
            return 1
        
        if len(category) > 0:
            category = '-' + category
        
        onScreenDebug.add('%s%s-%s' % (self.getDisplayPrefix(), category, key), value)
        return 1

    
    def clearDisplay(self):
        onScreenDebug.removeAllWithPrefix(self.getDisplayPrefix())
        return 1

    
    def moodComponentChanged(self, components = []):
        if len(components) == 0:
            components = PetMood.PetMood.Components
        
        for comp in components:
            self.display(comp, self.mood.getComponent(comp), 'mood')
        

    
    def setOwnerId(self, ownerId):
        self.ownerId = ownerId

    
    def getOwnerId(self):
        return self.ownerId

    
    def setPetName(self, petName):
        self.petName = petName
        DistributedSmoothNode.DistributedSmoothNode.setName(self, self.petName)
        if self.isGenerated():
            Pet.Pet.setName(self, self.petName)
        
        messenger.send('petNameChanged', [
            self])

    
    def setTraitSeed(self, traitSeed):
        self.traitSeed = traitSeed

    
    def setSafeZone(self, safeZone):
        self.safeZone = safeZone

    
    def _DistributedPet__generateDistTraitFuncs(self):
        for i in xrange(PetTraits.PetTraits.NumTraits):
            traitName = PetTraits.getTraitNames()[i]
            setterName = self.getSetterName(traitName)
            
            def traitSetter(value, self = self, i = i):
                self.traitList[i] = value

            self.__dict__[setterName] = traitSetter
            self._DistributedPet__funcsToDelete.append(setterName)
        

    
    def setHead(self, head):
        DistributedPet.notify.setDebug('setHead: %s' % head)
        self.head = head

    
    def setEars(self, ears):
        DistributedPet.notify.setDebug('setEars: %s' % ears)
        self.ears = ears

    
    def setNose(self, nose):
        DistributedPet.notify.setDebug('setNose: %s' % nose)
        self.nose = nose

    
    def setTail(self, tail):
        DistributedPet.notify.setDebug('setTail: %s' % tail)
        self.tail = tail

    
    def setBodyTexture(self, bodyTexture):
        DistributedPet.notify.setDebug('setBodyTexture: %s' % bodyTexture)
        self.bodyTexture = bodyTexture

    
    def setColor(self, color):
        DistributedPet.notify.setDebug('setColor: %s' % color)
        self.color = color

    
    def setColorScale(self, colorScale):
        DistributedPet.notify.setDebug('setColorScale: %s' % colorScale)
        self.colorScale = colorScale

    
    def setEyeColor(self, eyeColor):
        DistributedPet.notify.setDebug('setEyeColor: %s' % eyeColor)
        self.eyeColor = eyeColor

    
    def setGender(self, gender):
        DistributedPet.notify.setDebug('setGender: %s' % gender)
        self.gender = gender

    
    def setLastSeenTimestamp(self, timestamp):
        DistributedPet.notify.setDebug('setLastSeenTimestamp: %s' % timestamp)
        self.lastSeenTimestamp = timestamp

    
    def getTimeSinceLastSeen(self):
        t = self.cr.getServerTimeOfDay() - self.lastSeenTimestamp
        return max(0.0, t)

    
    def updateOfflineMood(self):
        self.mood.driftMood(dt = self.getTimeSinceLastSeen(), curMood = self.lastKnownMood)

    
    def _DistributedPet__handleMoodSet(self, component, value):
        if self.isGenerated():
            self.mood.setComponent(component, value)
        else:
            self.requiredMoodComponents[component] = value

    
    def _DistributedPet__generateDistMoodFuncs(self):
        for compName in PetMood.PetMood.Components:
            setterName = self.getSetterName(compName)
            
            def moodSetter(value, self = self, compName = compName):
                self._DistributedPet__handleMoodSet(compName, value)

            self.__dict__[setterName] = moodSetter
            self._DistributedPet__funcsToDelete.append(setterName)
        

    
    def setMood(self, *componentValues):
        for (value, name) in zip(componentValues, PetMood.PetMood.Components):
            setterName = self.getSetterName(name)
            self.__dict__[setterName](value)
        

    
    def doTrick(self, trickId, timestamp):
        if not self.isLockedDown():
            if self.trickIval is not None and self.trickIval.isPlaying():
                self.trickIval.finish()
            
            self.trickIval = PetTricks.getTrickIval(self, trickId)
            if trickId == PetTricks.Tricks.BALK:
                mood = self.getDominantMood()
                self.trickIval = Parallel(self.trickIval, Sequence(Func(self.handleMoodChange, 'confusion'), Wait(1.0), Func(self.handleMoodChange, mood)))
            
            self.trickIval.start(globalClockDelta.localElapsedTime(timestamp))
        

    
    def getName(self):
        return Pet.Pet.getName(self)

    
    def announceGenerate(self):
        DistributedPet.notify.debug('announceGenerate(), fake=%s' % self.bFake)
        DistributedSmoothNode.DistributedSmoothNode.announceGenerate(self)
        self.traits = PetTraits.PetTraits(self.traitSeed, self.safeZone, traitValueList = self.traitList)
        self.mood = PetMood.PetMood(self)
        for (mood, value) in self.requiredMoodComponents.items():
            self.mood.setComponent(mood, value, announce = 0)
        
        self.requiredMoodComponents = { }
        DistributedPet.notify.debug('time since last seen: %s' % self.getTimeSinceLastSeen())
        self.setDNA([
            self.head,
            self.ears,
            self.nose,
            self.tail,
            self.bodyTexture,
            self.color,
            self.colorScale,
            self.eyeColor,
            self.gender])
        av = self.cr.doId2do.get(self.ownerId)
        if av:
            av.petDNA = self.style
        
        if self.bFake:
            self.lastKnownMood = self.mood.makeCopy()
            self.updateOfflineMood()
        else:
            self._DistributedPet__initCollisions()
            self.startSmooth()
            self.setActiveShadow(1)
        self.setPetName(self.petName)
        if not (self.bFake):
            self.addActive()
            self.startBlink()
            self.handleMoodChange()
            self.accept(self.mood.getDominantMoodChangeEvent(), self.handleMoodChange)
            self.accept(self.mood.getMoodChangeEvent(), self.moodComponentChanged)
        

    
    def disable(self):
        DistributedPet.notify.debug('disable(), fake=%s' % self.bFake)
        if self.isLocalToon:
            base.localAvatar.enableSmartCameraViews()
            self.freeAvatar()
        
        self.ignore(self.mood.getDominantMoodChangeEvent())
        self.ignore(self.mood.getMoodChangeEvent())
        if hasattr(self, 'lastKnownMood'):
            self.lastKnownMood.destroy()
            del self.lastKnownMood
        
        self.mood.destroy()
        del self.mood
        del self.traits
        self.removeActive()
        if not (self.bFake):
            self.stopSmooth()
            self._DistributedPet__cleanupCollisions()
            self.stopAnimations()
        
        taskMgr.remove(self.uniqueName('lerpCamera'))
        self.clearDisplay()
        DistributedSmoothNode.DistributedSmoothNode.disable(self)

    
    def delete(self):
        DistributedPet.notify.debug('delete(), fake=%s' % self.bFake)
        if self.trickIval is not None:
            self.trickIval.finish()
            del self.trickIval
        
        if self.movieTrack is not None:
            self.movieTrack.finish()
            del self.movieTrack
        
        taskMgr.remove(self.uniqueName('Pet-Movie-%s' % self.getDoId()))
        for funcName in self._DistributedPet__funcsToDelete:
            del self.__dict__[funcName]
        
        Pet.Pet.delete(self)
        DistributedSmoothNode.DistributedSmoothNode.delete(self)
        if not (self.bFake):
            PetManager.releasePetManager()
        

    
    def _DistributedPet__initCollisions(self):
        cRay = CollisionRay(0.0, 0.0, 40000.0, 0.0, 0.0, -1.0)
        cRayNode = CollisionNode('pet-cRayNode-%s' % self.doId)
        cRayNode.addSolid(cRay)
        cRayNode.setFromCollideMask(OTPGlobals.FloorBitmask)
        cRayNode.setIntoCollideMask(BitMask32.allOff())
        self.cRayNodePath = self.attachNewNode(cRayNode)
        self.lifter = CollisionHandlerFloor()
        self.lifter.setInPattern('enter%in')
        self.lifter.setOutPattern('exit%in')
        self.lifter.setOffset(OTPGlobals.FloorOffset)
        self.lifter.setReach(4.0)
        self.lifter.addCollider(self.cRayNodePath, self)
        self.cTrav = base.petManager.cTrav
        self.cTrav.addCollider(self.cRayNodePath, self.lifter)
        taskMgr.add(self._detectWater, self.getDetectWaterTaskName(), priority = 32)
        self.initializeBodyCollisions('pet-%s' % self.doId)

    
    def _DistributedPet__cleanupCollisions(self):
        self.disableBodyCollisions()
        taskMgr.remove(self.getDetectWaterTaskName())
        self.cTrav.removeCollider(self.cRayNodePath)
        del self.cTrav
        self.cRayNodePath.removeNode()
        del self.cRayNodePath
        del self.lifter

    
    def lockPet(self):
        if not (self.lockedDown):
            self.prevAnimState = self.animFSM.getCurrentState().getName()
            self.animFSM.request('neutral')
        
        self.lockedDown += 1

    
    def isLockedDown(self):
        return self.lockedDown != 0

    
    def unlockPet(self):
        if self.lockedDown <= 0:
            DistributedPet.notify.warning('%s: unlockPet called on unlockedPet' % self.doId)
        else:
            self.lockedDown -= 1
            if not (self.lockedDown):
                self.animFSM.request(self.prevAnimState)
                self.prevAnimState = None
            

    
    def smoothPosition(self):
        DistributedSmoothNode.DistributedSmoothNode.smoothPosition(self)
        if not (self.lockedDown):
            self.trackAnimToSpeed(self.smoother.getSmoothForwardVelocity(), self.smoother.getSmoothRotationalVelocity())
        

    
    def getDetectWaterTaskName(self):
        return self.uniqueName('detectWater')

    
    def _detectWater(self, task):
        (showWake, wakeWaterHeight) = ZoneUtil.getWakeInfo()
        self.inWater = 0
        if showWake:
            if self.getZ() <= wakeWaterHeight:
                self.setZ(wakeWaterHeight - PetConstants.SubmergeDistance)
                self.inWater = 1
            
        
        return Task.cont

    
    def isInWater(self):
        return self.inWater

    
    def isExcited(self):
        return PetBase.PetBase.isExcited(self)

    
    def isSad(self):
        return PetBase.PetBase.isSad(self)

    
    def handleMoodChange(self, mood = None):
        if mood is None:
            mood = self.mood.getDominantMood()
        
        if mood == PetMood.PetMood.Neutral:
            self.clearMood()
        else:
            self.showMood(mood)
        messenger.send('petStateUpdated', [
            self])

    
    def getDominantMood(self):
        if not hasattr(self, 'mood'):
            return PetMood.PetMood.Neutral
        
        return self.mood.getDominantMood()

    
    def getRequestID(self):
        return CLIENT_GET_PET_DETAILS

    
    def teleportIn(self, timestamp):
        self.lockPet()
        self.animFSM.request('teleportIn', [
            timestamp])
        self.unlockPet()

    
    def teleportOut(self, timestamp):
        self.lockPet()
        self.animFSM.request('teleportOut', [
            timestamp])
        self.unlockPet()

    
    def avatarInteract(self, avId):
        place = base.cr.playGame.getPlace()
        place.preserveFriendsList()
        place.setState('pet')
        base.localAvatar.disableSmartCameraViews()

    
    def freeAvatar(self):
        place = base.cr.playGame.getPlace()
        if place:
            place.preserveFriendsList()
            place.setState('walk')
        
        base.localAvatar.unlock()
        messenger.send('pet-interaction-done')

    
    def setUpMovieAvatar(self, av):
        self.avDelayDelete = DelayDelete.DelayDelete(av)
        av.headsUp(self, 0, 0, 0)
        av.stopLookAround()

    
    def holdPetDownForMovie(self):
        self.lockPet()
        self.stopSmooth()

    
    def releasePetFromHoldDown(self):
        self.unlockPet()
        self.startSmooth()

    
    def clearMovieAvatar(self):
        self.avDelayDelete = None

    
    def clearMovie(self):
        self.clearMovieAvatar()
        return Task.done

    
    def resetAvatarAndPet(self, task = None):
        if self.isLocalToon:
            base.localAvatar.enableSmartCameraViews()
            base.localAvatar.setH(base.localAvatar, 30)
            self.freeAvatar()
            self.isLocalToon = 0
        
        return Task.done

    
    def _petMovieStart(self, av):
        if not (self.isLocalToon):
            av.stopSmooth()
        
        self.setUpMovieAvatar(av)
        if self.isLocalToon:
            base.localAvatar.setCameraPosForPetInteraction()
            base.localAvatar.lock()
        

    
    def _getPetMovieCompleteIval(self, av):
        
        def _petMovieComplete(self = self):
            if self.isLocalToon:
                base.localAvatar.unsetCameraPosForPetInteraction()
            else:
                av.startSmooth()

        return Sequence(Func(_petMovieComplete), Wait(0.80000000000000004), Func(self.resetAvatarAndPet))

    
    def setMovie(self, mode, avId, timestamp):
        timeStamp = globalClockDelta.localElapsedTime(timestamp)
        if mode in (PetConstants.PET_MOVIE_CALL, PetConstants.PET_MOVIE_SCRATCH, PetConstants.PET_MOVIE_FEED):
            if self.movieTrack is not None and self.movieTrack.isPlaying():
                self.movieTrack.finish()
            
        
        if avId != 0:
            self.isLocalToon = avId == base.localAvatar.doId
            av = base.cr.doId2do.get(avId)
            if av is None:
                self.notify.warning('Avatar %d not found in doId' % avId)
                return None
            
        
        if mode == PetConstants.PET_MOVIE_CLEAR:
            self.clearMovie()
            return None
        
        if mode == PetConstants.PET_MOVIE_CALL:
            
            try:
                self.movieTrack = Sequence(Func(self._petMovieStart, av), Parallel(av.getCallPetIval(), Sequence(Wait(0.54000000000000004), SoundInterval(self.callSfx))), self._getPetMovieCompleteIval(av))
                self.movieTrack.start()
            except StandardError:
                error = None
                print str(error)

        
        if mode == PetConstants.PET_MOVIE_SCRATCH:
            
            try:
                self.movieTrack = Sequence(Func(self._petMovieStart, av), Func(self.holdPetDownForMovie), Parallel(self.getInteractIval(self.Interactions.SCRATCH), av.getScratchPetIval(), SoundInterval(self.petSfx)), Func(self.releasePetFromHoldDown), self._getPetMovieCompleteIval(av))
                self.movieTrack.start()
            except StandardError:
                error = None
                print str(error)

        
        if mode == PetConstants.PET_MOVIE_FEED:
            self.bean = loader.loadModelCopy('phase_5.5/models/props/jellybean4')
            bean = self.bean.find('**/jellybean')
            bean.setColor(random.choice(BeanColors))
            self.movieTrack = Sequence(Func(self._petMovieStart, av), Func(self.holdPetDownForMovie), Parallel(Func(base.playSfx, self.swallowSfx, 0, 1, 1, 2.5, self.bean), Sequence(ActorInterval(self, 'toBeg'), ActorInterval(self, 'beg'), ActorInterval(self, 'fromBeg'), ActorInterval(self, 'eat'), ActorInterval(self, 'swallow'), Func(self.loop, 'neutral')), Sequence(Wait(0.29999999999999999), ActorInterval(av, 'feedPet'), Func(av.animFSM.request, 'neutral')), Sequence(Wait(0.29999999999999999), Func(self.bean.reparentTo, av.rightHand), Func(self.bean.setPos, 0.10000000000000001, 0.0, 0.20000000000000001), Wait(2.1000000000000001), Func(av.update, 0), Func(av.update, 1), Func(av.update, 2), Func(self.bean.wrtReparentTo, render), Parallel(LerpHprInterval(self.bean, hpr = Point3(random.random() * 360.0 * 2, random.random() * 360.0 * 2, random.random() * 360.0 * 2), duration = 1.2), ProjectileInterval(self.bean, endPos = self.find('**/joint_tongueBase').getPos(render), duration = 1.2, gravityMult = 0.45000000000000001)), Func(self.bean.removeNode))), Func(self.releasePetFromHoldDown), self._getPetMovieCompleteIval(av))
            self.movieTrack.start()
        
        return None


