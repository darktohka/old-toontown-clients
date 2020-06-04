# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\level\LevelUtil.py
import string, LevelConstants

def getZoneNum2Node(levelModel, logFunc=lambda str: str):

    def findNumberedNodes(baseString, model, caseInsens=1):
        srch = '**/%s*' % baseString
        if caseInsens:
            srch += ';+i'
        potentialNodes = model.findAllMatches(srch)
        num2node = {}
        for potentialNode in potentialNodes:
            name = potentialNode.getName()
            logFunc('potential match for %s: %s' % (baseString, name))
            name = name[len(baseString):]
            numDigits = 0
            while numDigits < len(name):
                if name[numDigits] not in string.digits:
                    break
                numDigits += 1

            if numDigits == 0:
                continue
            num = int(name[:numDigits])
            if num == LevelConstants.UberZoneEntId:
                logFunc('warning: cannot use UberZone zoneNum (%s). ignoring %s' % (LevelConstants.UberZoneEntId, potentialNode))
                continue
            if num < LevelConstants.MinZoneNum or num > LevelConstants.MaxZoneNum:
                logFunc('warning: zone %s is out of range. ignoring %s' % (num, potentialNode))
                continue
            if num in num2node:
                logFunc('warning: zone %s already assigned to %s. ignoring %s' % (num, num2node[num], potentialNode))
                continue
            num2node[num] = potentialNode

        return num2node

    zoneNum2node = findNumberedNodes('zone', levelModel)
    zoneNum2node[LevelConstants.UberZoneEntId] = levelModel
    return zoneNum2node