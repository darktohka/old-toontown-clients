# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\battle\BattleExperience.py
from toontown.toonbase import ToontownBattleGlobals

def genRewardDicts(entries):
    toonRewardDicts = []
    for (toonId, origExp, earnedExp, origQuests, items, missedItems, origMerits, merits, parts) in entries:
        if toonId != -1:
            dict = {}
            toon = base.cr.doId2do.get(toonId)
            if toon == None:
                continue
            dict['toon'] = toon
            dict['origExp'] = origExp
            dict['earnedExp'] = earnedExp
            dict['origQuests'] = origQuests
            dict['items'] = items
            dict['missedItems'] = missedItems
            dict['origMerits'] = origMerits
            dict['merits'] = merits
            dict['parts'] = parts
            toonRewardDicts.append(dict)

    return toonRewardDicts