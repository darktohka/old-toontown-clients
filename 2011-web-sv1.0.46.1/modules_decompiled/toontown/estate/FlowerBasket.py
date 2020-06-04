# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\estate\FlowerBasket.py
import GardenGlobals
from direct.directnotify import DirectNotifyGlobal
import FlowerBase

class FlowerBasket:
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FlowerBasket')

    def __init__(self):
        self.flowerList = []

    def __len__(self):
        return len(self.flowerList)

    def getFlower(self):
        return self.flowerList

    def makeFromNetLists(self, speciesList, varietyList):
        self.flowerList = []
        for (species, variety) in zip(speciesList, varietyList):
            self.flowerList.append(FlowerBase.FlowerBase(species, variety))

    def getNetLists(self):
        speciesList = []
        varietyList = []
        for flower in self.flowerList:
            speciesList.append(flower.getSpecies())
            varietyList.append(flower.getVariety())

        return [
         speciesList, varietyList]

    def hasFlower(self, species, variety):
        for flower in self.flowerList:
            if flower.getSpecies() == species and flower.getVariety() == variety:
                return 1

        return 0

    def addFlower(self, species, variety):
        self.flowerList.append(FlowerBase.FlowerBase(species, variety))
        return 1

    def removeFishAtIndex(self, index):
        if index >= len(self.flowerList):
            return 0
        else:
            del self.flowerList[i]
            return 1

    def generateRandomBasket(self):
        import random
        numFish = random.randint(1, 20)
        self.flowerList = []
        for i in range(numFish):
            (species, variety) = GardenGlobals.getRandomFlower()
            self.addFlower(species, variety)

    def getTotalValue(self):
        value = 0
        for flower in self.flowerList:
            value += flower.getValue()

        return value

    def __str__(self):
        numFlower = len(self.flowerList)
        value = 0
        txt = 'Flower Basket (%s flower):' % numFlower
        for flower in self.flowerList:
            txt += '\n' + str(flower)

        value = self.getTotalValue()
        txt += '\nTotal value: %s' % value
        return txt