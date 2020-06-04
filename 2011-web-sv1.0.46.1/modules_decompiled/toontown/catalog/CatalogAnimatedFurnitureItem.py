# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\catalog\CatalogAnimatedFurnitureItem.py
from CatalogFurnitureItem import *
FTAnimRate = 6
AnimatedFurnitureItemKeys = (10020, 270, 990, 460, 470, 480, 490, 491, 492)

class CatalogAnimatedFurnitureItem(CatalogFurnitureItem):
    __module__ = __name__

    def loadModel(self):
        model = CatalogFurnitureItem.loadModel(self)
        self.setAnimRate(model, self.getAnimRate())
        return model

    def getAnimRate(self):
        item = FurnitureTypes[self.furnitureType]
        if FTAnimRate < len(item):
            animRate = item[FTAnimRate]
            if not animRate == None:
                return item[FTAnimRate]
            else:
                return 1
        else:
            return 1
        return

    def setAnimRate(self, model, rate):
        seqNodes = model.findAllMatches('**/seqNode*')
        for seqNode in seqNodes:
            seqNode.node().setPlayRate(rate)