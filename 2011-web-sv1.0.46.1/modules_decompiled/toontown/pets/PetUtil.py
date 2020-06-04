# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\pets\PetUtil.py
from toontown.pets import PetDNA, PetTraits, PetConstants
from toontown.pets import PetNameGenerator
from direct.showbase import PythonUtil
import random

def getPetInfoFromSeed(seed, safezoneId):
    S = random.getstate()
    random.seed(seed)
    dnaArray = PetDNA.getRandomPetDNA(safezoneId)
    gender = PetDNA.getGender(dnaArray)
    nameString = PetNameGenerator.PetNameGenerator().randomName(gender=gender, seed=seed + safezoneId)
    traitSeed = PythonUtil.randUint31()
    random.setstate(S)
    return (nameString, dnaArray, traitSeed)


def getPetCostFromSeed(seed, safezoneId):
    (name, dna, traitSeed) = getPetInfoFromSeed(seed, safezoneId)
    traits = PetTraits.PetTraits(traitSeed, safezoneId)
    traitValue = traits.getOverallValue()
    traitValue -= 0.3
    traitValue = max(0, traitValue)
    rarity = PetDNA.getRarity(dna)
    rarity *= 1.0 - traitValue
    rarity = pow(0.001, rarity) - 0.001
    (minCost, maxCost) = PetConstants.ZoneToCostRange[safezoneId]
    cost = rarity * (maxCost - minCost) + minCost
    cost = int(cost)
    return cost