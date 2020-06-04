# File: P (Python 2.2)

from toontown.toonbase import ToontownGlobals
from toontown.pets import PetDNA, PetTraits
from toontown.pets import PetNameGenerator
from direct.showbase import PythonUtil
import random

def getPetInfoFromSeed(seed, safezoneId):
    S = random.getstate()
    random.seed(seed)
    dnaArray = PetDNA.getRandomPetDNA(safezoneId)
    gender = PetDNA.getGender(dnaArray)
    nameString = PetNameGenerator.PetNameGenerator().randomName(gender = gender, seed = seed + safezoneId)
    traitSeed = PythonUtil.randUint31()
    random.setstate(S)
    return (nameString, dnaArray, traitSeed)


def getPetCostFromSeed(seed, safezoneId):
    (name, dna, traitSeed) = getPetInfoFromSeed(seed, safezoneId)
    traits = PetTraits.PetTraits(traitSeed, safezoneId)
    traitValue = traits.getOverallValue()
    traitValue -= 0.29999999999999999
    traitValue = max(0, traitValue)
    rarity = PetDNA.getRarity(dna)
    rarity *= 1.0 - traitValue
    rarity = pow(0.001, rarity) - 0.001
    zoneMinMax = {
        ToontownGlobals.ToontownCentral: (100, 500),
        ToontownGlobals.DonaldsDock: (600, 1700),
        ToontownGlobals.DaisyGardens: (1000, 2500),
        ToontownGlobals.MinniesMelodyland: (1500, 3000),
        ToontownGlobals.TheBrrrgh: (2500, 4000),
        ToontownGlobals.DonaldsDreamland: (3000, 5000) }
    (minCost, maxCost) = zoneMinMax[safezoneId]
    cost = rarity * (maxCost - minCost) + minCost
    cost = int(cost)
    return cost

