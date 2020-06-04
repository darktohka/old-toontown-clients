# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\catalog\CatalogSurfaceItem.py
import CatalogItem, CatalogAtticItem
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from CatalogSurfaceColors import *
STWallpaper = 0
STMoulding = 1
STFlooring = 2
STWainscoting = 3
NUM_ST_TYPES = 4

class CatalogSurfaceItem(CatalogAtticItem.CatalogAtticItem):
    __module__ = __name__

    def makeNewItem(self):
        CatalogAtticItem.CatalogAtticItem.makeNewItem(self)

    def setPatternIndex(self, patternIndex):
        self.patternIndex = patternIndex

    def setColorIndex(self, colorIndex):
        self.colorIndex = colorIndex

    def saveHistory(self):
        return 1

    def recordPurchase(self, avatar, optional):
        self.giftTag = None
        (house, retcode) = self.getHouseInfo(avatar)
        if retcode >= 0:
            house.addWallpaper(self)
        return retcode

    def getDeliveryTime(self):
        return 60