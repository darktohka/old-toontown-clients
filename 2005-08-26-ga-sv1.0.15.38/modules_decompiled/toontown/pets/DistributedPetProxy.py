# File: D (Python 2.2)

from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.pets import PetTraits
from toontown.pets import PetMood, PetTricks
from toontown.toonbase import ToontownGlobals
import string

class DistributedPetProxy(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPetProxy')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self._DistributedPetProxy__funcsToDelete = []
        self._DistributedPetProxy__generateDistTraitFuncs()
        self._DistributedPetProxy__generateDistMoodFuncs()
        self.dominantMood = 'neutral'
        self.sendGenerateMessage = 0
        self.trickAptitudes = []
        self.ghostMode = False
        self.bFake = False

    
    def generate(self):
        self.traitList = [
            0] * PetTraits.PetTraits.NumTraits
        self.requiredMoodComponents = { }

    
    def getSetterName(self, valueName, prefix = 'set'):
        return '%s%s%s' % (prefix, string.upper(valueName[0]), valueName[1:])

    
    def setOwnerId(self, ownerId):
        self.ownerId = ownerId

    
    def getOwnerId(self):
        return self.ownerId

    
    def setPetName(self, petName):
        self.petName = petName

    
    def setTraitSeed(self, traitSeed):
        self.traitSeed = traitSeed

    
    def setSafeZone(self, safeZone):
        self.safeZone = safeZone

    
    def _DistributedPetProxy__generateDistTraitFuncs(self):
        for i in xrange(PetTraits.PetTraits.NumTraits):
            traitName = PetTraits.getTraitNames()[i]
            setterName = self.getSetterName(traitName)
            
            def traitSetter(value, self = self, i = i):
                self.traitList[i] = value

            self.__dict__[setterName] = traitSetter
            self._DistributedPetProxy__funcsToDelete.append(setterName)
        

    
    def setHead(self, head):
        DistributedPetProxy.notify.debug('setHead: %s' % head)
        self.head = head

    
    def setEars(self, ears):
        DistributedPetProxy.notify.debug('setEars: %s' % ears)
        self.ears = ears

    
    def setNose(self, nose):
        DistributedPetProxy.notify.debug('setNose: %s' % nose)
        self.nose = nose

    
    def setTail(self, tail):
        DistributedPetProxy.notify.debug('setTail: %s' % tail)
        self.tail = tail

    
    def setBodyTexture(self, bodyTexture):
        DistributedPetProxy.notify.debug('setBodyTexture: %s' % bodyTexture)
        self.bodyTexture = bodyTexture

    
    def setColor(self, color):
        DistributedPetProxy.notify.debug('setColor: %s' % color)
        self.color = color

    
    def setColorScale(self, colorScale):
        DistributedPetProxy.notify.debug('setColorScale: %s' % colorScale)
        self.colorScale = colorScale

    
    def setEyeColor(self, eyeColor):
        DistributedPetProxy.notify.debug('setEyeColor: %s' % eyeColor)
        self.eyeColor = eyeColor

    
    def setGender(self, gender):
        DistributedPetProxy.notify.debug('setGender: %s' % gender)
        self.gender = gender

    
    def getDNA(self):
        return self.style

    
    def getName(self):
        return self.petName

    
    def getFont(self):
        return ToontownGlobals.getToonFont()

    
    def setLastSeenTimestamp(self, timestamp):
        DistributedPetProxy.notify.debug('setLastSeenTimestamp: %s' % timestamp)
        self.lastSeenTimestamp = timestamp

    
    def getTimeSinceLastSeen(self):
        t = self.cr.getServerTimeOfDay() - self.lastSeenTimestamp
        return max(0.0, t)

    
    def updateOfflineMood(self):
        self.mood.driftMood(dt = self.getTimeSinceLastSeen(), curMood = self.lastKnownMood)

    
    def _DistributedPetProxy__handleMoodSet(self, component, value):
        if self.isGenerated():
            self.mood.setComponent(component, value)
        else:
            self.requiredMoodComponents[component] = value

    
    def _DistributedPetProxy__generateDistMoodFuncs(self):
        for compName in PetMood.PetMood.Components:
            setterName = self.getSetterName(compName)
            
            def moodSetter(value, self = self, compName = compName):
                self._DistributedPetProxy__handleMoodSet(compName, value)

            self.__dict__[setterName] = moodSetter
            self._DistributedPetProxy__funcsToDelete.append(setterName)
        

    
    def setMood(self, *componentValues):
        for (value, name) in zip(componentValues, PetMood.PetMood.Components):
            setterName = self.getSetterName(name)
            self.__dict__[setterName](value)
        

    
    def announceGenerate(self):
        self.traits = PetTraits.PetTraits(self.traitSeed, self.safeZone, traitValueList = self.traitList)
        self.mood = PetMood.PetMood(self)
        self.lastKnownMood = self.mood.makeCopy()
        for (mood, value) in self.requiredMoodComponents.items():
            self.mood.setComponent(mood, value, announce = 0)
        
        self.requiredMoodComponents = { }
        DistributedPetProxy.notify.debug('time since last seen: %s' % self.getTimeSinceLastSeen())
        self.style = [
            self.head,
            self.ears,
            self.nose,
            self.tail,
            self.bodyTexture,
            self.color,
            self.colorScale,
            self.eyeColor,
            self.gender]
        self.setLastSeenTimestamp(self.lastSeenTimestamp)
        self.updateOfflineMood()
        self.sendGenerateMessage = 1

    
    def disable(self):
        if hasattr(self, 'lastKnownMood'):
            self.lastKnownMood.destroy()
            del self.lastKnownMood
        
        self.mood.destroy()
        del self.mood
        del self.traits

    
    def delete(self):
        for funcName in self._DistributedPetProxy__funcsToDelete:
            del self.__dict__[funcName]
        

    
    def setDominantMood(self, dominantMood):
        self.dominantMood = dominantMood
        if self.sendGenerateMessage == 1:
            proxyGenerateMessage = 'petProxy-%d-generated' % self.doId
            messenger.send(proxyGenerateMessage)
            self.sendGenerateMessage = 0
        

    
    def getDominantMood(self):
        return self.dominantMood

    
    def setTrickAptitudes(self, aptitudes):
        self.trickAptitudes = aptitudes

    
    def isPet(self):
        return True

    
    def isProxy(self):
        return True


