# File: F (Python 2.2)

import Localizer
import math
import random
import ToontownGlobals
import copy
NoMovie = 0
EnterMovie = 1
ExitMovie = 2
CastMovie = 3
PullInMovie = 4
CastTimeout = 45.0
Nothing = 0
QuestItem = 1
FishItem = 2
JellybeanItem = 3
BootItem = 4
GagItem = 5
OverTankLimit = 8
FishItemNewEntry = 9
FishItemNewRecord = 10
HealAmount = 1
MAX_RARITY = 10
FishingAngleMax = 50.0
OVERALL_VALUE_SCALE = 15
RARITY_VALUE_SCALE = 0.20000000000000001
WEIGHT_VALUE_SCALE = 0.050000000000000003 / 16.0
COLLECT_NO_UPDATE = 0
COLLECT_NEW_ENTRY = 1
COLLECT_NEW_RECORD = 2
RodFileDict = {
    0: 'phase_4/models/props/pole_treebranch-mod',
    1: 'phase_4/models/props/pole_bamboo-mod',
    2: 'phase_4/models/props/pole_wood-mod',
    3: 'phase_4/models/props/pole_steel-mod',
    4: 'phase_4/models/props/pole_gold-mod' }
RodPriceDict = {
    0: 0,
    1: 400,
    2: 800,
    3: 1200,
    4: 2000 }
MaxRodId = 4
FishFileDict = {
    -1: (4, 'clownFish-zero', 'clownFish-swim', None, None, 0.11, -35, 20),
    4: (4, 'clownFish-zero', 'clownFish-swim', None, (0.12, 0, 0), 0.13, -35, 20),
    6: (4, 'frozenFish-zero', 'frozenFish-swim', None, (-0.10000000000000001, 0, 0.14999999999999999), 0.23999999999999999, -35, 20),
    8: (4, 'starFish-zero', 'starFish-swim', None, (0, 0, -0.22), 0.14000000000000001, -35, 20),
    10: (4, 'holeyMackerel-zero', 'holeyMackerel-swim', None, None, 0.23999999999999999, 0, 10),
    14: (4, 'amoreEel-zero', 'amoreEel-swim', None, (0.42499999999999999, 0, 0.59999999999999998), 0.32000000000000001, 0, 40),
    16: (4, 'nurseShark-zero', 'nurseShark-swim', None, (-0.45000000000000001, 0, -0.25), 0.10000000000000001, -35, 20),
    18: (4, 'kingCrab-zero', 'kingCrab-swim', None, None, 0.074999999999999997, 0, 20),
    20: (4, 'moonFish-zero', 'moonFish-swim', None, (-0.90000000000000002, 0, -1.5), 0.070000000000000007, 0, 0),
    22: (4, 'seaHorse-zero', 'seaHorse-swim', None, (0, 0, -1.3999999999999999), 0.089999999999999997, -35, 25),
    24: (4, 'poolShark-zero', 'poolShark-swim', None, (0, 0, -1.3999999999999999), 0.14999999999999999, -35, 20),
    26: (4, 'BearAcuda-zero', 'BearAcuda-swim', None, (0.65000000000000002, 0, -2.5), 0.080000000000000002, -35, 20),
    28: (4, 'cutThroatTrout-zero', 'cutThroatTrout-swim', None, (-0.29999999999999999, 0, 0.20000000000000001), 0.23999999999999999, 35, 20),
    30: (4, 'pianoTuna-zero', 'pianoTuna-swim', None, (0, 0, 0.34999999999999998), 0.20000000000000001, 45, 30),
    34: (4, 'devilRay-zero', 'devilRay-swim', None, (-0.40000000000000002, 0, 0.10000000000000001), 0.17000000000000001, -40, 20) }
FISH_PER_BONUS = 10
TrophyDict = {
    0: (Localizer.FishTrophyNameDict[0],),
    1: (Localizer.FishTrophyNameDict[1],),
    2: (Localizer.FishTrophyNameDict[2],),
    3: (Localizer.FishTrophyNameDict[3],),
    4: (Localizer.FishTrophyNameDict[4],) }
WEIGHT_MIN_INDEX = 0
WEIGHT_MAX_INDEX = 1
RARITY_INDEX = 2
ZONE_LIST_INDEX = 3
Anywhere = 1
TTG = ToontownGlobals
__fishDict = {
    4: ((2, 8, 1, (TTG.ToontownCentral, Anywhere)), (2, 8, 4, (TTG.ToontownCentral, Anywhere)), (2, 8, 2, (TTG.ToontownCentral, Anywhere)), (2, 8, 6, (TTG.ToontownCentral, TTG.MinniesMelodyland))),
    6: ((8, 12, 1, (TTG.TheBrrrgh,)),),
    8: ((1, 5, 1, (Anywhere,)), (2, 6, 2, (TTG.MinniesMelodyland, Anywhere)), (5, 10, 5, (TTG.MinniesMelodyland, Anywhere)), (1, 5, 7, (TTG.MyEstate, Anywhere)), (1, 5, 10, (TTG.MyEstate, Anywhere))),
    10: ((6, 10, 9, (TTG.MyEstate, Anywhere)),),
    14: ((2, 6, 1, (TTG.DaisyGardens, TTG.MyEstate, Anywhere)), (2, 6, 3, (TTG.DaisyGardens, TTG.MyEstate))),
    16: ((4, 12, 5, (TTG.MinniesMelodyland, Anywhere)), (4, 12, 7, (TTG.BaritoneBoulevard, TTG.MinniesMelodyland)), (4, 12, 8, (TTG.TenorTerrace, TTG.MinniesMelodyland))),
    18: ((2, 4, 3, (TTG.DonaldsDock, Anywhere)), (5, 8, 7, (TTG.TheBrrrgh,)), (4, 6, 8, (TTG.LighthouseLane,))),
    20: ((4, 6, 1, (TTG.DonaldsDreamland,)), (14, 18, 10, (TTG.DonaldsDreamland,)), (6, 10, 8, (TTG.LullabyLane,)), (1, 1, 3, (TTG.DonaldsDreamland,)), (2, 6, 6, (TTG.LullabyLane,)), (10, 14, 4, (TTG.DonaldsDreamland, TTG.DaisyGardens))),
    22: ((12, 16, 2, (TTG.MyEstate, TTG.DaisyGardens, Anywhere)), (14, 18, 3, (TTG.MyEstate, TTG.DaisyGardens, Anywhere)), (14, 20, 5, (TTG.MyEstate, TTG.DaisyGardens)), (14, 20, 7, (TTG.MyEstate, TTG.DaisyGardens))),
    24: ((9, 11, 3, (Anywhere,)), (8, 12, 5, (TTG.DaisyGardens, TTG.DonaldsDock)), (8, 12, 6, (TTG.DaisyGardens, TTG.DonaldsDock)), (8, 16, 7, (TTG.DaisyGardens, TTG.DonaldsDock))),
    26: ((10, 18, 2, (TTG.TheBrrrgh,)), (10, 18, 3, (TTG.TheBrrrgh,)), (10, 18, 4, (TTG.TheBrrrgh,)), (10, 18, 5, (TTG.TheBrrrgh,)), (12, 20, 6, (TTG.TheBrrrgh,)), (14, 20, 7, (TTG.TheBrrrgh,)), (14, 20, 8, (TTG.SleetStreet, TTG.TheBrrrgh)), (16, 20, 10, (TTG.WalrusWay, TTG.TheBrrrgh))),
    28: ((2, 10, 2, (TTG.DonaldsDock, Anywhere)), (4, 10, 6, (TTG.BarnacleBoulevard, TTG.DonaldsDock)), (4, 10, 7, (TTG.SeaweedStreet, TTG.DonaldsDock))),
    30: ((13, 17, 5, (TTG.MinniesMelodyland, Anywhere)), (16, 20, 10, (TTG.AltoAvenue, TTG.MinniesMelodyland)), (12, 18, 9, (TTG.TenorTerrace, TTG.MinniesMelodyland)), (12, 18, 6, (TTG.MinniesMelodyland,)), (12, 18, 7, (TTG.MinniesMelodyland,))),
    34: ((1, 20, 10, (TTG.DonaldsDreamland, Anywhere)),) }

def getSpecies(genus):
    return __fishDict[genus]


def getGenera():
    return __fishDict.keys()

ROD_WEIGHT_MIN_INDEX = 0
ROD_WEIGHT_MAX_INDEX = 1
ROD_CAST_COST_INDEX = 2
__rodDict = {
    0: (0, 4, 1),
    1: (0, 8, 2),
    2: (0, 12, 3),
    3: (0, 16, 5),
    4: (0, 20, 8) }

def getNumRods():
    return len(__rodDict)


def getCastCost(rodId):
    return __rodDict[rodId][ROD_CAST_COST_INDEX]


def getEffectiveRarity(rarity, offset):
    return min(MAX_RARITY, rarity + offset * 2)


def canBeCaughtByRod(genus, species, rodIndex):
    (minFishWeight, maxFishWeight) = getWeightRange(genus, species)
    (minRodWeight, maxRodWeight) = getRodWeightRange(rodIndex)
    if minRodWeight <= maxFishWeight and maxRodWeight >= minFishWeight:
        return 1
    else:
        return 0


def getRodWeightRange(rodIndex):
    rodProps = __rodDict[rodIndex]
    return (rodProps[ROD_WEIGHT_MIN_INDEX], rodProps[ROD_WEIGHT_MAX_INDEX])


def rollRarityDice():
    diceRoll = random.random()
    exp = 1.0 / 5.0
    rarity = int(math.ceil(10 * (1 - math.pow(diceRoll, exp))))
    if rarity <= 0:
        rarity = 1
    
    return rarity


def getRandomWeight(genus, species, rodIndex = None):
    (minFishWeight, maxFishWeight) = getWeightRange(genus, species)
    if rodIndex is None:
        minWeight = minFishWeight
        maxWeight = maxFishWeight
    else:
        (minRodWeight, maxRodWeight) = getRodWeightRange(rodIndex)
        minWeight = max(minFishWeight, minRodWeight)
        maxWeight = min(maxFishWeight, maxRodWeight)
    randNumA = random.random()
    randNumB = random.random()
    randNum = (randNumA + randNumB) / 2.0
    randWeight = minWeight + (maxWeight - minWeight) * randNum
    return int(round(randWeight * 16))


def getRandomFishVitals(zoneId, rodId):
    rarity = rollRarityDice()
    rodDict = __pondInfoDict.get(zoneId)
    rarityDict = rodDict.get(rodId)
    fishList = rarityDict.get(rarity)
    if fishList:
        (genus, species) = random.choice(fishList)
        weight = getRandomWeight(genus, species, rodId)
        return (1, genus, species, weight)
    else:
        return (0, 0, 0, 0)


def getWeightRange(genus, species):
    fishInfo = __fishDict[genus][species]
    return (fishInfo[WEIGHT_MIN_INDEX], fishInfo[WEIGHT_MAX_INDEX])


def getRarity(genus, species):
    return __fishDict[genus][species][RARITY_INDEX]


def getValue(genus, species, weight):
    rarity = getRarity(genus, species)
    rarityValue = math.pow(RARITY_VALUE_SCALE * rarity, 1.5)
    weightValue = math.pow(WEIGHT_VALUE_SCALE * weight, 1.1000000000000001)
    value = OVERALL_VALUE_SCALE * (rarityValue + weightValue)
    return int(math.ceil(value))

__totalNumFish = 0
__emptyRodDict = { }
for rodIndex in __rodDict:
    __emptyRodDict[rodIndex] = { }

__anywhereDict = copy.deepcopy(__emptyRodDict)
__pondInfoDict = { }
for (genus, speciesList) in __fishDict.items():
    for species in range(len(speciesList)):
        __totalNumFish += 1
        speciesDesc = speciesList[species]
        rarity = speciesDesc[RARITY_INDEX]
        zoneList = speciesDesc[ZONE_LIST_INDEX]
        for zoneIndex in range(len(zoneList)):
            zone = zoneList[zoneIndex]
            effectiveRarity = getEffectiveRarity(rarity, zoneIndex)
            if zone == Anywhere:
                for (rodIndex, rarityDict) in __anywhereDict.items():
                    if canBeCaughtByRod(genus, species, rodIndex):
                        fishList = rarityDict.setdefault(effectiveRarity, [])
                        fishList.append((genus, species))
                    
                
            else:
                pondZones = [
                    zone]
                subZones = ToontownGlobals.HoodHierarchy.get(zone)
                if subZones:
                    pondZones.extend(subZones)
                
                for pondZone in pondZones:
                    if __pondInfoDict.has_key(pondZone):
                        rodDict = __pondInfoDict[pondZone]
                    else:
                        rodDict = copy.deepcopy(__emptyRodDict)
                        __pondInfoDict[pondZone] = rodDict
                    for (rodIndex, rarityDict) in rodDict.items():
                        if canBeCaughtByRod(genus, species, rodIndex):
                            fishList = rarityDict.setdefault(effectiveRarity, [])
                            fishList.append((genus, species))
                        
                    
                
        
    

for (zone, rodDict) in __pondInfoDict.items():
    for (rodIndex, anywhereRarityDict) in __anywhereDict.items():
        for (rarity, anywhereFishList) in anywhereRarityDict.items():
            rarityDict = rodDict[rodIndex]
            fishList = rarityDict.setdefault(rarity, [])
            fishList.extend(anywhereFishList)
        
    


def getTotalNumFish():
    return __totalNumFish


def testRarity():
    numIter = 10000
    d = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0 }
    for i in range(numIter):
        v = rollRarityDice()
        d[v] += 1
    
    for (rarity, count) in d.items():
        percentage = (count / float(numIter)) * 100
        d[rarity] = percentage
    
    print d


def getRandomFish():
    genus = random.choice(__fishDict.keys())
    species = random.randint(0, len(__fishDict[genus]) - 1)
    return (genus, species)


def getPondInfo():
    return __pondInfoDict

