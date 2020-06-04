# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\CatchGameGlobals.py
EndlessGame = config.GetBool('endless-catch-game', 0)
GameDuration = 55.0

class DropObject:
    __module__ = __name__

    def __init__(self, name, good, onscreenDurMult, modelPath):
        self.name = name
        self.good = good
        self.onscreenDurMult = onscreenDurMult
        self.modelPath = modelPath

    def isBaseline(self):
        return self.onscreenDurMult == 1.0


DropObjectTypes = [
 DropObject('apple', 1, 1.0, 'phase_4/models/minigames/apple'), DropObject('orange', 1, 1.0, 'phase_4/models/minigames/orange'), DropObject('pear', 1, 1.0, 'phase_4/models/minigames/pear'), DropObject('coconut', 1, 1.0, 'phase_4/models/minigames/coconut'), DropObject('watermelon', 1, 1.0, 'phase_4/models/minigames/watermelon'), DropObject('pineapple', 1, 1.0, 'phase_4/models/minigames/pineapple'), DropObject('anvil', 0, 0.4, 'phase_4/models/props/anvil-mod')]
Name2DropObjectType = {}
for type in DropObjectTypes:
    Name2DropObjectType[type.name] = type

Name2DOTypeId = {}
names = Name2DropObjectType.keys()
names.sort()
for i in range(len(names)):
    Name2DOTypeId[names[i]] = i

DOTypeId2Name = names
NumFruits = [{2000: 18, 1000: 19, 5000: 22, 4000: 24, 3000: 27, 9000: 28}, {2000: 30, 1000: 33, 5000: 38, 4000: 42, 3000: 46, 9000: 50}, {2000: 42, 1000: 48, 5000: 54, 4000: 60, 3000: 66, 9000: 71}, {2000: 56, 1000: 63, 5000: 70, 4000: 78, 3000: 85, 9000: 92}]