# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\pets\PetBase.py
from toontown.pets.PetConstants import AnimMoods
from toontown.pets import PetMood
import string

class PetBase:
    __module__ = __name__

    def getSetterName(self, valueName, prefix='set'):
        return '%s%s%s' % (prefix, string.upper(valueName[0]), valueName[1:])

    def getAnimMood(self):
        if self.mood.getDominantMood() in PetMood.PetMood.ExcitedMoods:
            return AnimMoods.EXCITED
        elif self.mood.getDominantMood() in PetMood.PetMood.UnhappyMoods:
            return AnimMoods.SAD
        else:
            return AnimMoods.NEUTRAL

    def isExcited(self):
        return self.getAnimMood() == AnimMoods.EXCITED

    def isSad(self):
        return self.getAnimMood() == AnimMoods.SAD