# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\estate\FlowerBase.py
import GardenGlobals
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal

class FlowerBase:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FlowerBase')

    def __init__(self, species, variety):
        self.species = species
        self.variety = variety
        if self.species not in GardenGlobals.PlantAttributes.keys():
            print 'remove me when everyone is updated'
            self.species = 56
            species = 56

    def getSpecies(self):
        return self.species

    def setSpecies(self, species):
        self.species = species

    def getVariety(self):
        return self.variety

    def setVariety(self, variety):
        self.variety = variety

    def getVitals(self):
        return (
         self.species, self.variety)

    def getValue(self):
        return GardenGlobals.PlantAttributes[self.species]['varieties'][self.variety][2]

    def getSpeciesName(self):
        return TTLocalizer.FlowerSpeciesNames[self.species]

    def getVarietyName(self):
        return self.getFullName()

    def getFullName(self):
        return GardenGlobals.getFlowerVarietyName(self.species, self.variety)

    def getFullNameWithRecipe(self):
        name = GardenGlobals.getFlowerVarietyName(self.species, self.variety)
        recipeKey = GardenGlobals.PlantAttributes[self.species]['varieties'][self.variety][0]
        name += ' (%s)' % GardenGlobals.Recipes[recipeKey]['beans']
        return name

    def __str__(self):
        return '%s, value: %s' % (self.getFullName(), self.getValue())