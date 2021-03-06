# File: P (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from direct.showbase.PythonUtil import lerp, average, clampScalar
from toontown.toonbase import TTLocalizer
import random
import time

class PetMood:
    notify = DirectNotifyGlobal.directNotify.newCategory('PetMood')
    Neutral = 'neutral'
    Components = ('boredom', 'restlessness', 'playfulness', 'loneliness', 'sadness', 'affection', 'hunger', 'confusion', 'excitement', 'fatigue', 'anger', 'surprise')
    SerialNum = 0
    ContentedMoods = ('neutral', 'excitement', 'playfulness', 'affection')
    ExcitedMoods = ('excitement', 'playfulness')
    UnhappyMoods = ('boredom', 'restlessness', 'loneliness', 'sadness', 'fatigue', 'hunger', 'anger')
    DisabledDominants = ('restlessness', 'playfulness')
    AssertiveDominants = ('fatigue',)
    HOUR = 1.0
    MINUTE = HOUR / 60.0
    DAY = 24.0 * HOUR
    WEEK = 7 * DAY
    LONGTIME = 5000 * WEEK
    TBoredom = 12 * HOUR
    TRestlessness = 18 * HOUR
    TPlayfulness = -1 * HOUR
    TLoneliness = 24 * HOUR
    TSadness = -1 * HOUR
    TFatigue = -15 * MINUTE
    THunger = 24 * HOUR
    TConfusion = -5 * MINUTE
    TExcitement = -5 * MINUTE
    TSurprise = -5 * MINUTE
    TAffection = -10 * MINUTE
    TAngerDec = -20 * MINUTE
    TAngerInc = 2 * WEEK
    
    def __init__(self, pet = None):
        self.pet = pet
        self.started = 0
        self.serialNum = PetMood.SerialNum
        PetMood.SerialNum += 1
        for comp in PetMood.Components:
            self.__dict__[comp] = 0.0
        
        
        def calcDrift(baseT, trait, lowerIsBetter = 0):
            if trait.higherIsBetter:
                thresh = trait.value
            else:
                thresh = 1.0 - trait.value
            if thresh < 0.5:
                factor = lerp(0.75, 1.0, thresh * 2.0)
            else:
                rebased = (thresh - 0.5) * 2.0
                factor = lerp(1.0, 28.0, rebased * rebased)
            return baseT * factor

        self.tBoredom = calcDrift(PetMood.TBoredom, self.pet.traits.traits['boredomThreshold'])
        self.tRestlessness = calcDrift(PetMood.TRestlessness, self.pet.traits.traits['restlessnessThreshold'])
        self.tPlayfulness = calcDrift(PetMood.TPlayfulness, self.pet.traits.traits['playfulnessThreshold'])
        self.tLoneliness = calcDrift(PetMood.TLoneliness, self.pet.traits.traits['lonelinessThreshold'])
        self.tSadness = calcDrift(PetMood.TSadness, self.pet.traits.traits['sadnessThreshold'])
        self.tFatigue = calcDrift(PetMood.TFatigue, self.pet.traits.traits['fatigueThreshold'])
        self.tHunger = calcDrift(PetMood.THunger, self.pet.traits.traits['hungerThreshold'])
        self.tConfusion = calcDrift(PetMood.TConfusion, self.pet.traits.traits['confusionThreshold'])
        self.tExcitement = calcDrift(PetMood.TExcitement, self.pet.traits.traits['excitementThreshold'])
        self.tSurprise = calcDrift(PetMood.TSurprise, self.pet.traits.traits['surpriseThreshold'])
        self.tAffection = calcDrift(PetMood.TAffection, self.pet.traits.traits['affectionThreshold'])
        self.tAngerDec = calcDrift(PetMood.TAngerDec, self.pet.traits.traits['angerThreshold'])
        self.tAngerInc = calcDrift(PetMood.TAngerInc, self.pet.traits.traits['angerThreshold'])
        self.dominantMood = PetMood.Neutral

    
    def destroy(self):
        self.stop()
        del self.pet

    
    def getMoodDriftTaskName(self):
        return 'petMoodDrift-%s' % self.serialNum

    
    def getMoodChangeEvent(self):
        return 'petMoodChange-%s' % self.serialNum

    
    def getDominantMoodChangeEvent(self):
        return 'petDominantMoodChange-%s' % self.serialNum

    
    def announceChange(self, components = []):
        oldMood = self.dominantMood
        if hasattr(self, 'dominantMood'):
            del self.dominantMood
        
        newMood = self.getDominantMood()
        messenger.send(self.getMoodChangeEvent(), [
            components])
        if newMood != oldMood:
            messenger.send(self.getDominantMoodChangeEvent(), [
                newMood])
        

    
    def getComponent(self, compName):
        return self.__dict__[compName]

    
    def setComponent(self, compName, value, announce = 1):
        different = self.__dict__[compName] != value
        self.__dict__[compName] = value
        if announce and different:
            self.announceChange([
                compName])
        

    
    def _getComponentThreshold(self, compName):
        threshName = compName + 'Threshold'
        return self.pet.traits.__dict__[threshName]

    
    def isComponentActive(self, compName):
        return self.getComponent(compName) >= self._getComponentThreshold(compName)

    
    def anyActive(self, compNames):
        for comp in compNames:
            if self.isComponentActive(comp):
                return 1
            
        
        return 0

    
    def getDominantMood(self):
        if hasattr(self, 'dominantMood'):
            return self.dominantMood
        
        dominantMood = PetMood.Neutral
        priority = 1.0
        for comp in PetMood.Components:
            if comp in PetMood.DisabledDominants:
                continue
            
            value = self.getComponent(comp)
            pri = value / max(self._getComponentThreshold(comp), 0.01)
            if pri >= priority:
                dominantMood = comp
                priority = pri
            elif comp in PetMood.AssertiveDominants and pri >= 1.0:
                dominantMood = comp
            
        
        self.dominantMood = dominantMood
        return dominantMood

    
    def makeCopy(self):
        other = PetMood(self.pet)
        for comp in PetMood.Components:
            other.__dict__[comp] = self.__dict__[comp]
        
        return other

    
    def start(self):
        self.driftMood(self.pet.getTimeSinceLastSeen())
        taskMgr.doMethodLater(simbase.petMoodDriftPeriod * random.random(), self._driftMoodTask, self.getMoodDriftTaskName())
        self.started = 1

    
    def stop(self):
        if not (self.started):
            return None
        
        self.started = 0
        taskMgr.remove(self.getMoodDriftTaskName())

    
    def driftMood(self, dt = None, curMood = None):
        now = globalClock.getFrameTime()
        if dt is None:
            dt = now - self.lastDriftTime
        
        self.lastDriftTime = now
        if dt <= 0.0:
            return None
        
        if curMood is None:
            curMood = self
        
        
        def doDrift(curValue, timeToMedian, dt = float(dt)):
            newValue = curValue + dt / timeToMedian * 7200
            return clampScalar(newValue, 0.0, 1.0)

        self.boredom = doDrift(curMood.boredom, self.tBoredom)
        self.loneliness = doDrift(curMood.loneliness, self.tLoneliness)
        self.sadness = doDrift(curMood.sadness, self.tSadness)
        self.fatigue = doDrift(curMood.fatigue, self.tFatigue)
        self.hunger = doDrift(curMood.hunger, self.tHunger)
        self.confusion = doDrift(curMood.confusion, self.tConfusion)
        self.excitement = doDrift(curMood.excitement, self.tExcitement)
        self.surprise = doDrift(curMood.surprise, self.tSurprise)
        self.affection = doDrift(curMood.affection, self.tAffection)
        abuse = average(self.hunger, self.hunger, self.hunger, self.boredom, self.loneliness)
        tipPoint = 0.59999999999999998
        if abuse < tipPoint:
            tAnger = lerp(self.tAngerDec, -(PetMood.LONGTIME), abuse / tipPoint)
        else:
            tAnger = lerp(PetMood.LONGTIME, self.tAngerInc, (abuse - tipPoint) / (1.0 - tipPoint))
        self.anger = doDrift(curMood.anger, tAnger)
        self.announceChange()

    
    def _driftMoodTask(self, task = None):
        self.driftMood()
        taskMgr.doMethodLater(simbase.petMoodDriftPeriod / simbase.petMoodTimescale, self._driftMoodTask, self.getMoodDriftTaskName())
        return Task.done

    
    def __repr__(self):
        s = '%s' % self.__class__.__name__
        for comp in PetMood.Components:
            s += '\n %s: %s' % (comp, self.__dict__[comp])
        
        return s


