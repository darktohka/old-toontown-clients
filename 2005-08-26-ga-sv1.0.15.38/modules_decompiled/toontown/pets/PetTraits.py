# File: P (Python 2.2)

from direct.showbase.PythonUtil import randFloat, normalDistrib, Enum
from direct.showbase.PythonUtil import clampScalar
from toontown.toonbase import TTLocalizer, ToontownGlobals
import random
import copy
TraitDivisor = 10000

def getTraitNames():
    if not hasattr(PetTraits, 'TraitNames'):
        traitNames = []
        for desc in PetTraits.TraitDescs:
            traitNames.append(desc[0])
            PetTraits.TraitNames = traitNames
        
    
    return PetTraits.TraitNames


def uniform(min, max, rng):
    return randFloat(min, max, rng.random)


def gaussian(min, max, rng):
    return normalDistrib(min, max, rng.gauss)


class TraitDistribution:
    TraitQuality = Enum('VERY_BAD, BAD, AVERAGE, GOOD, VERY_GOOD')
    TraitTypes = Enum('INCREASING, DECREASING')
    Sz2MinMax = None
    TraitType = None
    TraitCutoffs = {
        TraitTypes.INCREASING: {
            TraitQuality.VERY_BAD: 0.10000000000000001,
            TraitQuality.BAD: 0.25,
            TraitQuality.GOOD: 0.75,
            TraitQuality.VERY_GOOD: 0.90000000000000002 },
        TraitTypes.DECREASING: {
            TraitQuality.VERY_BAD: 0.90000000000000002,
            TraitQuality.BAD: 0.75,
            TraitQuality.GOOD: 0.25,
            TraitQuality.VERY_GOOD: 0.10000000000000001 } }
    
    def __init__(self, rndFunc = gaussian):
        self.rndFunc = rndFunc
        if not hasattr(self.__class__, 'GlobalMinMax'):
            _min = 1.0
            _max = 0.0
            minMax = self.Sz2MinMax
            for sz in minMax:
                (thisMin, thisMax) = minMax[sz]
                _min = min(_min, thisMin)
                _max = max(_max, thisMax)
            
            self.__class__.GlobalMinMax = [
                _min,
                _max]
        

    
    def getRandValue(self, szId, rng = random):
        (min, max) = self.getMinMax(szId)
        return self.rndFunc(min, max, rng)

    
    def getHigherIsBetter(self):
        return self.TraitType == TraitDistribution.TraitTypes.INCREASING

    
    def getMinMax(self, szId):
        return (self.Sz2MinMax[szId][0], self.Sz2MinMax[szId][1])

    
    def getGlobalMinMax(self):
        return (self.GlobalMinMax[0], self.GlobalMinMax[1])

    
    def _getTraitPercent(self, traitValue):
        (gMin, gMax) = self.getGlobalMinMax()
        if traitValue < gMin:
            gMin = traitValue
        elif traitValue > gMax:
            gMax = traitValue
        
        return (traitValue - gMin) / (gMax - gMin)

    
    def getPercentile(self, traitValue):
        if self.TraitType is TraitDistribution.TraitTypes.INCREASING:
            return self._getTraitPercent(traitValue)
        else:
            return 1.0 - self._getTraitPercent(traitValue)

    
    def getQuality(self, traitValue):
        TraitQuality = TraitDistribution.TraitQuality
        TraitCutoffs = self.TraitCutoffs[self.TraitType]
        percent = self._getTraitPercent(traitValue)
        if self.TraitType is TraitDistribution.TraitTypes.INCREASING:
            if percent <= TraitCutoffs[TraitQuality.VERY_BAD]:
                return TraitQuality.VERY_BAD
            elif percent <= TraitCutoffs[TraitQuality.BAD]:
                return TraitQuality.BAD
            elif percent >= TraitCutoffs[TraitQuality.VERY_GOOD]:
                return TraitQuality.VERY_GOOD
            elif percent >= TraitCutoffs[TraitQuality.GOOD]:
                return TraitQuality.GOOD
            else:
                return TraitQuality.AVERAGE
        elif percent <= TraitCutoffs[TraitQuality.VERY_GOOD]:
            return TraitQuality.VERY_GOOD
        elif percent <= TraitCutoffs[TraitQuality.GOOD]:
            return TraitQuality.GOOD
        elif percent >= TraitCutoffs[TraitQuality.VERY_BAD]:
            return TraitQuality.VERY_BAD
        elif percent >= TraitCutoffs[TraitQuality.BAD]:
            return TraitQuality.BAD
        else:
            return TraitQuality.AVERAGE

    
    def getExtremeness(self, traitValue):
        percent = self._getTraitPercent(traitValue)
        if percent < 0.5:
            howExtreme = (0.5 - percent) * 2.0
        else:
            howExtreme = (percent - 0.5) * 2.0
        return clampScalar(howExtreme, 0.0, 1.0)



class PetTraits:
    
    class StdIncDistrib(TraitDistribution):
        TraitType = TraitDistribution.TraitTypes.INCREASING
        Sz2MinMax = {
            ToontownGlobals.ToontownCentral: (0.20000000000000001, 0.65000000000000002),
            ToontownGlobals.DonaldsDock: (0.29999999999999999, 0.69999999999999996),
            ToontownGlobals.DaisyGardens: (0.40000000000000002, 0.75),
            ToontownGlobals.MinniesMelodyland: (0.5, 0.80000000000000004),
            ToontownGlobals.TheBrrrgh: (0.59999999999999998, 0.84999999999999998),
            ToontownGlobals.DonaldsDreamland: (0.69999999999999996, 0.90000000000000002) }

    
    class StdDecDistrib(TraitDistribution):
        TraitType = TraitDistribution.TraitTypes.DECREASING
        Sz2MinMax = {
            ToontownGlobals.ToontownCentral: (0.34999999999999998, 0.80000000000000004),
            ToontownGlobals.DonaldsDock: (0.29999999999999999, 0.69999999999999996),
            ToontownGlobals.DaisyGardens: (0.25, 0.59999999999999998),
            ToontownGlobals.MinniesMelodyland: (0.20000000000000001, 0.5),
            ToontownGlobals.TheBrrrgh: (0.14999999999999999, 0.40000000000000002),
            ToontownGlobals.DonaldsDreamland: (0.10000000000000001, 0.29999999999999999) }

    
    class ForgetfulnessDistrib(TraitDistribution):
        TraitType = TraitDistribution.TraitTypes.DECREASING
        Sz2MinMax = {
            ToontownGlobals.ToontownCentral: (0.0, 1.0),
            ToontownGlobals.DonaldsDock: (0.0, 0.90000000000000002),
            ToontownGlobals.DaisyGardens: (0.0, 0.80000000000000004),
            ToontownGlobals.MinniesMelodyland: (0.0, 0.69999999999999996),
            ToontownGlobals.TheBrrrgh: (0.0, 0.59999999999999998),
            ToontownGlobals.DonaldsDreamland: (0.0, 0.5) }

    TraitDescs = (('forgetfulness', ForgetfulnessDistrib(), True), ('boredomThreshold', StdIncDistrib(), True), ('restlessnessThreshold', StdIncDistrib(), True), ('playfulnessThreshold', StdDecDistrib(), True), ('lonelinessThreshold', StdIncDistrib(), True), ('sadnessThreshold', StdIncDistrib(), True), ('fatigueThreshold', StdIncDistrib(), True), ('hungerThreshold', StdIncDistrib(), True), ('confusionThreshold', StdIncDistrib(), True), ('excitementThreshold', StdDecDistrib(), True), ('angerThreshold', StdIncDistrib(), True), ('surpriseThreshold', StdIncDistrib(), False), ('affectionThreshold', StdDecDistrib(), True))
    NumTraits = len(TraitDescs)
    
    class Trait:
        
        def __init__(self, index, traitsObj, value = None):
            (self.name, distrib, self.hasWorth) = PetTraits.TraitDescs[index]
            if value is not None:
                self.value = value
            else:
                szId = traitsObj.safeZoneId
                self.value = distrib.getRandValue(szId, traitsObj.rng)
                self.value = int(self.value * TraitDivisor) / float(TraitDivisor)
            self.higherIsBetter = distrib.getHigherIsBetter()
            self.percentile = distrib.getPercentile(self.value)
            self.quality = distrib.getQuality(self.value)
            self.howExtreme = distrib.getExtremeness(self.value)

        
        def __repr__(self):
            return 'Trait: %s, %s, %s, %s' % (self.name, self.value, TraitDistribution.TraitQuality.getString(self.quality), self.howExtreme)


    
    def __init__(self, traitSeed, safeZoneId, traitValueList = []):
        self.traitSeed = traitSeed
        self.safeZoneId = safeZoneId
        self.rng = random.Random(self.traitSeed)
        self.traits = { }
        for i in xrange(len(PetTraits.TraitDescs)):
            if i < len(traitValueList) and traitValueList[i] > 0.0:
                trait = PetTraits.Trait(i, self, traitValueList[i])
            else:
                trait = PetTraits.Trait(i, self)
            self.traits[trait.name] = trait
            self.__dict__[trait.name] = trait.value
        
        extremeTraits = []
        for trait in self.traits.values():
            if not (trait.hasWorth):
                continue
            
            if trait.quality == TraitDistribution.TraitQuality.AVERAGE:
                continue
            
            i = 0
            while i < len(extremeTraits) and extremeTraits[i].howExtreme > trait.howExtreme:
                i += 1
            extremeTraits.insert(i, trait)
        
        self.extremeTraits = []
        for trait in extremeTraits:
            self.extremeTraits.append((trait.name, trait.quality))
        

    
    def getValueList(self):
        traitValues = []
        for desc in PetTraits.TraitDescs:
            traitName = desc[0]
            traitValues.append(self.traits[traitName].value)
        
        return traitValues

    
    def getTraitValue(self, traitName):
        return self.traits[traitName].value

    
    def getExtremeTraits(self):
        return copy.copy(self.extremeTraits)

    
    def getOverallValue(self):
        total = 0
        numUsed = 0
        for trait in self.traits.values():
            if trait.hasWorth:
                if trait.higherIsBetter:
                    value = trait.value
                else:
                    value = 1.0 - trait.value
                total += value
                numUsed += 1
            
        
        value = total / len(self.traits.values())
        return value

    
    def getExtremeTraitDescriptions(self):
        descs = []
        TraitQuality = TraitDistribution.TraitQuality
        Quality2index = {
            TraitQuality.VERY_BAD: 0,
            TraitQuality.BAD: 1,
            TraitQuality.GOOD: 2,
            TraitQuality.VERY_GOOD: 3 }
        for (name, quality) in self.extremeTraits:
            descs.append(TTLocalizer.PetTrait2descriptions[name][Quality2index[quality]])
        
        return descs


