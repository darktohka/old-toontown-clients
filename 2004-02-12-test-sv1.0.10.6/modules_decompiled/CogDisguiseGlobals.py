# File: C (Python 2.2)

import AvatarDNA
import types
import Localizer
PartsPerSuit = (17, 14, 12, 10)
PartsPerSuitBitmasks = (131071, 130175, 56447, 56411)
AllBits = 131071
MinPartLoss = 2
MaxPartLoss = 4
MeritsPerLevel = ((50, 60, 70, 80, 500), (60, 70, 80, 90, 600), (70, 80, 90, 100, 700), (80, 90, 100, 110, 800), (90, 100, 110, 120, 900), (100, 110, 120, 130, 1000), (110, 120, 130, 140, 1100), (120, 130, 140, 150, 10000), (40, 50, 60, 70, 400), (50, 60, 70, 80, 500), (60, 70, 80, 90, 600), (70, 80, 90, 100, 700), (80, 90, 100, 110, 800), (90, 100, 110, 120, 900), (100, 110, 120, 130, 1000), (110, 120, 130, 140, 10000), (30, 40, 50, 60, 300), (40, 50, 60, 70, 400), (50, 60, 70, 80, 500), (60, 70, 80, 90, 600), (70, 80, 90, 100, 700), (80, 90, 100, 110, 800), (90, 100, 110, 120, 900), (100, 110, 120, 130, 10000), (20, 30, 40, 50, 200), (40, 50, 60, 70, 300), (60, 80, 100, 120, 500), (100, 130, 160, 190, 800), (160, 210, 260, 310, 1300), (260, 340, 420, 500, 2100), (520, 550, 680, 810, 3400), (780, 890, 1100, 5500, 10000))
leftLegUpper = 1
leftLegLower = 2
leftLegFoot = 4
rightLegUpper = 8
rightLegLower = 16
rightLegFoot = 32
torsoLeftShoulder = 64
torsoRightShoulder = 128
torsoChest = 256
torsoHealthMeter = 512
torsoPelvis = 1024
leftArmUpper = 2048
leftArmLower = 4096
leftArmHand = 8192
rightArmUpper = 16384
rightArmLower = 32768
rightArmHand = 65536
leftLegIndex = 0
rightLegIndex = 1
torsoIndex = 2
leftArmIndex = 3
rightArmIndex = 4
PartsQueryShifts = (leftLegUpper, rightLegUpper, torsoLeftShoulder, leftArmUpper, rightArmUpper)
PartsQueryMasks = (leftLegFoot + leftLegLower + leftLegUpper, rightLegFoot + rightLegLower + rightLegUpper, torsoPelvis + torsoHealthMeter + torsoChest + torsoRightShoulder + torsoLeftShoulder, leftArmHand + leftArmLower + leftArmUpper, rightArmHand + rightArmLower + rightArmUpper)
PartNameStrings = Localizer.CogPartNames
SimplePartNameStrings = Localizer.CogPartNamesSimple
PartsQueryNames = ({
    1: PartNameStrings[0],
    2: PartNameStrings[1],
    4: PartNameStrings[2],
    8: PartNameStrings[3],
    16: PartNameStrings[4],
    32: PartNameStrings[5],
    64: PartNameStrings[6],
    128: PartNameStrings[7],
    256: PartNameStrings[8],
    512: PartNameStrings[9],
    1024: PartNameStrings[10],
    2048: PartNameStrings[11],
    4096: PartNameStrings[12],
    8192: PartNameStrings[13],
    16384: PartNameStrings[14],
    32768: PartNameStrings[15],
    65536: PartNameStrings[16] }, {
    1: PartNameStrings[0],
    2: PartNameStrings[1],
    4: PartNameStrings[2],
    8: PartNameStrings[3],
    16: PartNameStrings[4],
    32: PartNameStrings[5],
    64: SimplePartNameStrings[0],
    128: SimplePartNameStrings[0],
    256: SimplePartNameStrings[0],
    512: SimplePartNameStrings[0],
    1024: PartNameStrings[10],
    2048: PartNameStrings[11],
    4096: PartNameStrings[12],
    8192: PartNameStrings[13],
    16384: PartNameStrings[14],
    32768: PartNameStrings[15],
    65536: PartNameStrings[16] }, {
    1: PartNameStrings[0],
    2: PartNameStrings[1],
    4: PartNameStrings[1],
    8: PartNameStrings[3],
    16: PartNameStrings[4],
    32: PartNameStrings[4],
    64: SimplePartNameStrings[0],
    128: SimplePartNameStrings[0],
    256: SimplePartNameStrings[0],
    512: SimplePartNameStrings[0],
    1024: PartNameStrings[10],
    2048: PartNameStrings[11],
    4096: PartNameStrings[12],
    8192: PartNameStrings[13],
    16384: PartNameStrings[14],
    32768: PartNameStrings[15],
    65536: PartNameStrings[16] }, {
    1: PartNameStrings[0],
    2: PartNameStrings[1],
    4: PartNameStrings[1],
    8: PartNameStrings[3],
    16: PartNameStrings[4],
    32: PartNameStrings[4],
    64: SimplePartNameStrings[0],
    128: SimplePartNameStrings[0],
    256: SimplePartNameStrings[0],
    512: SimplePartNameStrings[0],
    1024: PartNameStrings[10],
    2048: PartNameStrings[11],
    4096: PartNameStrings[12],
    8192: PartNameStrings[12],
    16384: PartNameStrings[14],
    32768: PartNameStrings[15],
    65536: PartNameStrings[15] })

def getNextPart(parts, partIndex, dept):
    dept = dept2deptIndex(dept)
    needMask = PartsPerSuitBitmasks[dept] & PartsQueryMasks[partIndex]
    haveMask = parts[dept] & PartsQueryMasks[partIndex]
    nextPart = ~needMask | haveMask
    nextPart = nextPart ^ nextPart + 1
    nextPart = nextPart + 1 >> 1
    return nextPart


def getPartName(partArray):
    index = 0
    for part in partArray:
        if part:
            return PartsQueryNames[index][part]
        
        index += 1
    


def isSuitComplete(parts, dept):
    dept = dept2deptIndex(dept)
    for p in range(len(PartsQueryMasks)):
        if getNextPart(parts, p, dept):
            return 0
        
    
    return 1


def getTotalMerits(toon, index):
    import AvatarDNA
    import SuitBattleGlobals
    cogIndex = toon.cogTypes[index] + AvatarDNA.suitsPerDept * index
    cogTypeStr = AvatarDNA.suitHeadTypes[cogIndex]
    cogBaseLevel = SuitBattleGlobals.SuitAttributes[cogTypeStr]['level']
    cogLevel = toon.cogLevels[index] - cogBaseLevel
    cogLevel = max(min(cogLevel, 4), 0)
    return MeritsPerLevel[cogIndex][cogLevel]


def getTotalParts(bitString, shiftWidth = 32):
    sum = 0
    for shift in range(0, shiftWidth):
        sum = sum + (bitString >> shift & 1)
    
    return sum


def asBitstring(number):
    array = []
    shift = 0
    if number == 0:
        array.insert(0, '0')
    
    while pow(2, shift) <= number:
        if number >> shift & 1:
            array.insert(0, '1')
        else:
            array.insert(0, '0')
        shift += 1
    str = ''
    for i in range(0, len(array)):
        str = str + array[i]
    
    return str


def asNumber(bitstring):
    num = 0
    for i in range(0, len(bitstring)):
        if bitstring[i] == '1':
            num += pow(2, len(bitstring) - 1 - i)
        
    
    return num


def dept2deptIndex(dept):
    if type(dept) == types.StringType:
        dept = AvatarDNA.suitDepts.index(dept)
    
    return dept

