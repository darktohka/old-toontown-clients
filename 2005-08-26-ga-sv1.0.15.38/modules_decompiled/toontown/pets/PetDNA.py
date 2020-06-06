# File: P (Python 2.2)

from toontown.toon import ToonDNA
from pandac.PandaModules import VBase4
from toontown.toonbase import TTLocalizer, ToontownGlobals
from direct.showbase import PythonUtil
NumFields = 9
Fields = {
    'head': 0,
    'ears': 1,
    'nose': 2,
    'tail': 3,
    'body': 4,
    'color': 5,
    'colorScale': 6,
    'eyes': 7,
    'gender': 8 }
HeadParts = [
    'feathers']
EarParts = [
    'horns',
    'antennae',
    'dogEars',
    'catEars',
    'rabbitEars']
EarTextures = {
    'horns': None,
    'antennae': None,
    'dogEars': None,
    'catEars': 'phase_4/maps/BeanCatEar6.jpg',
    'rabbitEars': 'phase_4/maps/BeanBunnyEar6.jpg' }
ExoticEarTextures = {
    'horns': None,
    'antennae': None,
    'dogEars': None,
    'catEars': 'phase_4/maps/BeanCatEar3Yellow.jpg',
    'rabbitEars': 'phase_4/maps/BeanBunnyEar6.jpg' }
NoseParts = [
    'clownNose',
    'dogNose',
    'ovalNose',
    'pigNose']
TailParts = [
    'catTail',
    'longTail',
    'birdTail',
    'bunnyTail']
TailTextures = {
    'catTail': 'phase_4/maps/beanCatTail6.jpg',
    'longTail': 'phase_4/maps/BeanLongTail6.jpg',
    'birdTail': None,
    'bunnyTail': None }
GiraffeTail = 'phase_4/maps/BeanLongTailGiraffe.jpg'
LeopardTail = 'phase_4/maps/BeanLongTailLepord.jpg'
GenericBodies = [
    'dots',
    'threeStripe',
    'tigerStripe',
    'tummy']
SpecificBodies = [
    'turtle',
    'giraffe',
    'leopard']
BodyTypes = GenericBodies + SpecificBodies
PetRarities2 = (('leopard', 0.0050000000000000001), ('giraffe', 0.014999999999999999), ('turtle', 0.044999999999999998), ('tigerStripe', 0.115), ('dots', 0.26500000000000001), ('tummy', 0.52500000000000002), ('threeStripe', 1.0))
PetRarities = {
    'body': {
        ToontownGlobals.ToontownCentral: {
            'threeStripe': 50,
            'tummy': 30,
            'dots': 20 },
        ToontownGlobals.DonaldsDock: {
            'threeStripe': 35,
            'tummy': 30,
            'dots': 20,
            'tigerStripe': 15 },
        ToontownGlobals.DaisyGardens: {
            'threeStripe': 15,
            'tummy': 20,
            'dots': 20,
            'tigerStripe': 20,
            'turtle': 15 },
        ToontownGlobals.MinniesMelodyland: {
            'threeStripe': 10,
            'tummy': 15,
            'dots': 30,
            'tigerStripe': 25,
            'turtle': 20 },
        ToontownGlobals.TheBrrrgh: {
            'threeStripe': 5,
            'tummy': 10,
            'dots': 20,
            'tigerStripe': 25,
            'turtle': 25,
            'giraffe': 15 },
        ToontownGlobals.DonaldsDreamland: {
            'threeStripe': 5,
            'tummy': 5,
            'dots': 15,
            'tigerStripe': 20,
            'turtle': 25,
            'giraffe': 20,
            'leopard': 10 } } }
BodyTextures = {
    'dots': 'phase_4/maps/BeanbodyDots6.jpg',
    'threeStripe': 'phase_4/maps/Beanbody3stripes6.jpg',
    'tigerStripe': 'phase_4/maps/BeanbodyZebraStripes6.jpg',
    'turtle': 'phase_4/maps/BeanbodyTurtle.jpg',
    'giraffe': 'phase_4/maps/BeanbodyGiraffe1.jpg',
    'leopard': 'phase_4/maps/BeanbodyLepord2.jpg',
    'tummy': 'phase_4/maps/BeanbodyTummy6.jpg' }
FeetTextures = {
    'normal': 'phase_4/maps/BeanFoot6.jpg',
    'turtle': 'phase_4/maps/BeanFootTurttle.jpg',
    'giraffe': 'phase_4/maps/BeanFootYellow3.jpg',
    'leopard': 'phase_4/maps/BeanFootYellow3.jpg' }
AllPetColors = (VBase4(1.0, 1.0, 1.0, 1.0), VBase4(0.96875, 0.69140599999999997, 0.69921900000000003, 1.0), VBase4(0.93359400000000003, 0.265625, 0.28125, 1.0), VBase4(0.86328099999999997, 0.40625, 0.41796899999999998, 1.0), VBase4(0.71093799999999996, 0.234375, 0.4375, 1.0), VBase4(0.57031200000000004, 0.44921899999999998, 0.16406200000000001, 1.0), VBase4(0.640625, 0.35546899999999998, 0.26953100000000002, 1.0), VBase4(0.99609400000000003, 0.69531200000000004, 0.51171900000000003, 1.0), VBase4(0.83203099999999997, 0.5, 0.296875, 1.0), VBase4(0.99218799999999996, 0.48046899999999998, 0.16796900000000001, 1.0), VBase4(0.99609400000000003, 0.89843799999999996, 0.32031199999999999, 1.0), VBase4(0.99609400000000003, 0.95703099999999997, 0.59765599999999997, 1.0), VBase4(0.85546900000000003, 0.93359400000000003, 0.49218800000000001, 1.0), VBase4(0.55078099999999997, 0.82421900000000003, 0.32421899999999998, 1.0), VBase4(0.24218799999999999, 0.74218799999999996, 0.515625, 1.0), VBase4(0.30468800000000001, 0.96875, 0.40234399999999998, 1.0), VBase4(0.43359399999999998, 0.90625, 0.83593799999999996, 1.0), VBase4(0.34765600000000002, 0.82031200000000004, 0.953125, 1.0), VBase4(0.19140599999999999, 0.5625, 0.77343799999999996, 1.0), VBase4(0.55859400000000003, 0.58984400000000003, 0.875, 1.0), VBase4(0.28515600000000002, 0.328125, 0.72656200000000004, 1.0), VBase4(0.46093800000000001, 0.37890600000000002, 0.82421900000000003, 1.0), VBase4(0.546875, 0.28125, 0.75, 1.0), VBase4(0.72656200000000004, 0.47265600000000002, 0.859375, 1.0), VBase4(0.89843799999999996, 0.61718799999999996, 0.90625, 1.0), VBase4(0.69999999999999996, 0.69999999999999996, 0.80000000000000004, 1.0))
GenericPetColors = [
    0,
    1,
    3,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    21,
    22,
    23,
    24,
    25]
SpecificPetColors = [
    0,
    1,
    3,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    16,
    17,
    18,
    23,
    24,
    25]
ColorScales = [
    0.80000000000000004,
    0.84999999999999998,
    0.90000000000000002,
    0.94999999999999996,
    1.0,
    1.05,
    1.1000000000000001,
    1.1499999999999999,
    1.2]
PetEyeColors = (VBase4(0.28999999999999998, 0.28999999999999998, 0.68999999999999995, 1.0), VBase4(0.48999999999999999, 0.48999999999999999, 0.98999999999999999, 1.0), VBase4(0.68999999999999995, 0.48999999999999999, 0.28999999999999998, 1.0), VBase4(0.98999999999999999, 0.68999999999999995, 0.48999999999999999, 1.0), VBase4(0.28999999999999998, 0.68999999999999995, 0.28999999999999998, 1.0), VBase4(0.48999999999999999, 0.98999999999999999, 0.48999999999999999, 1.0))
PetGenders = [
    0,
    1]

def getRandomPetDNA(zoneId = ToontownGlobals.DonaldsDreamland):
    choice = choice
    import random
    head = choice(range(-1, len(HeadParts)))
    ears = choice(range(-1, len(EarParts)))
    nose = choice(range(-1, len(NoseParts)))
    tail = choice(range(-1, len(TailParts)))
    body = getSpecies(zoneId)
    color = choice(range(0, len(getColors(body))))
    colorScale = choice(range(0, len(ColorScales)))
    eyes = choice(range(0, len(PetEyeColors)))
    gender = choice(range(0, len(PetGenders)))
    return [
        head,
        ears,
        nose,
        tail,
        body,
        color,
        colorScale,
        eyes,
        gender]


def getSpecies(zoneId):
    body = PythonUtil.weightedRand(PetRarities['body'][zoneId])
    return BodyTypes.index(body)


def getColors(bodyType):
    if BodyTypes[bodyType] in GenericBodies:
        return GenericPetColors
    else:
        return SpecificPetColors


def getFootTexture(bodyType):
    if BodyTypes[bodyType] == 'turtle':
        texName = FeetTextures['turtle']
    elif BodyTypes[bodyType] == 'giraffe':
        texName = FeetTextures['giraffe']
    elif BodyTypes[bodyType] == 'leopard':
        texName = FeetTextures['leopard']
    else:
        texName = FeetTextures['normal']
    return texName


def getEarTexture(bodyType, earType):
    if BodyTypes[bodyType] == 'giraffe' or BodyTypes[bodyType] == 'leopard':
        dict = ExoticEarTextures
    else:
        dict = EarTextures
    return dict[earType]


def getBodyRarity(bodyIndex):
    bodyName = BodyTypes[bodyIndex]
    totalWeight = 0.0
    weight = { }
    for zoneId in PetRarities['body']:
        for body in PetRarities['body'][zoneId]:
            totalWeight += PetRarities['body'][zoneId][body]
            if weight.has_key(body):
                weight[body] += PetRarities['body'][zoneId][body]
            else:
                weight[body] = PetRarities['body'][zoneId][body]
        
    
    minWeight = min(weight.values())
    rarity = (weight[bodyName] - minWeight) / (totalWeight - minWeight)
    return rarity


def getRarity(dna):
    body = dna[Fields['body']]
    rarity = getBodyRarity(body)
    return rarity


def getGender(dna):
    return dna[Fields['gender']]


def setGender(dna, gender):
    dna[Fields['gender']] = gender


def getGenderString(dna = None, gender = -1):
    if dna != None:
        gender = getGender(dna)
    
    if gender:
        return TTLocalizer.GenderShopBoyButtonText
    else:
        return TTLocalizer.GenderShopGirlButtonText

