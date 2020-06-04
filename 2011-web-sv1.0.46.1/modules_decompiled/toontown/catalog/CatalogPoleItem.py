# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\catalog\CatalogPoleItem.py
import CatalogItem
from toontown.toonbase import ToontownGlobals
from toontown.fishing import FishGlobals
from direct.actor import Actor
from toontown.toonbase import TTLocalizer
from direct.interval.IntervalGlobal import *

class CatalogPoleItem(CatalogItem.CatalogItem):
    __module__ = __name__
    sequenceNumber = 0

    def makeNewItem(self, rodId):
        self.rodId = rodId
        CatalogItem.CatalogItem.makeNewItem(self)

    def getPurchaseLimit(self):
        return 1

    def reachedPurchaseLimit(self, avatar):
        return avatar.getFishingRod() >= self.rodId or self in avatar.onOrder or self in avatar.mailboxContents

    def saveHistory(self):
        return 1

    def getTypeName(self):
        return TTLocalizer.PoleTypeName

    def getName(self):
        return TTLocalizer.FishingRod % TTLocalizer.FishingRodNameDict[self.rodId]

    def recordPurchase(self, avatar, optional):
        if self.rodId < 0 or self.rodId > FishGlobals.MaxRodId:
            self.notify.warning('Invalid fishing pole: %s for avatar %s' % (self.rodId, avatar.doId))
            return ToontownGlobals.P_InvalidIndex
        if self.rodId < avatar.getFishingRod():
            self.notify.warning('Avatar already has pole: %s for avatar %s' % (self.rodId, avatar.doId))
            return ToontownGlobals.P_ItemUnneeded
        avatar.b_setFishingRod(self.rodId)
        return ToontownGlobals.P_ItemAvailable

    def isGift(self):
        return 0

    def getDeliveryTime(self):
        return 24 * 60

    def getPicture(self, avatar):
        rodPath = FishGlobals.RodFileDict.get(self.rodId)
        pole = Actor.Actor(rodPath, {'cast': 'phase_4/models/props/fishing-pole-chan'})
        pole.setPosHpr(1.47, 0, -1.67, 90, 55, -90)
        pole.setScale(0.8)
        pole.setDepthTest(1)
        pole.setDepthWrite(1)
        frame = self.makeFrame()
        frame.attachNewNode(pole.node())
        name = 'pole-item-%s' % self.sequenceNumber
        CatalogPoleItem.sequenceNumber += 1
        track = Sequence(Func(pole.pose, 'cast', 130), Wait(100), name=name)
        self.hasPicture = True
        return (
         frame, track)

    def getAcceptItemErrorText(self, retcode):
        if retcode == ToontownGlobals.P_ItemAvailable:
            return TTLocalizer.CatalogAcceptPole
        elif retcode == ToontownGlobals.P_ItemUnneeded:
            return TTLocalizer.CatalogAcceptPoleUnneeded
        return CatalogItem.CatalogItem.getAcceptItemErrorText(self, retcode)

    def output(self, store=-1):
        return 'CatalogPoleItem(%s%s)' % (self.rodId, self.formatOptionalData(store))

    def getFilename(self):
        return FishGlobals.RodFileDict.get(self.rodId)

    def compareTo(self, other):
        return self.rodId - other.rodId

    def getHashContents(self):
        return self.rodId

    def getBasePrice(self):
        return FishGlobals.RodPriceDict[self.rodId]

    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.CatalogItem.decodeDatagram(self, di, versionNumber, store)
        self.rodId = di.getUint8()
        price = FishGlobals.RodPriceDict[self.rodId]

    def encodeDatagram(self, dg, store):
        CatalogItem.CatalogItem.encodeDatagram(self, dg, store)
        dg.addUint8(self.rodId)


def nextAvailablePole(avatar, duplicateItems):
    rodId = avatar.getFishingRod() + 1
    if rodId > FishGlobals.MaxRodId:
        return
    item = CatalogPoleItem(rodId)
    while item in avatar.onOrder or item in avatar.mailboxContents:
        rodId += 1
        if rodId > FishGlobals.MaxRodId:
            return
        item = CatalogPoleItem(rodId)

    return item


def getAllPoles():
    list = []
    for rodId in range(0, FishGlobals.MaxRodId + 1):
        list.append(CatalogPoleItem(rodId))

    return list