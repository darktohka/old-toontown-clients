# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\catalog\CatalogBeanItem.py
import CatalogItem
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPLocalizer
from direct.interval.IntervalGlobal import *

class CatalogBeanItem(CatalogItem.CatalogItem):
    __module__ = __name__
    sequenceNumber = 0

    def makeNewItem(self, beanAmount, tagCode=1):
        self.beanAmount = beanAmount
        self.giftCode = tagCode
        CatalogItem.CatalogItem.makeNewItem(self)

    def getPurchaseLimit(self):
        return 0

    def reachedPurchaseLimit(self, avatar):
        if self in avatar.onOrder or self in avatar.mailboxContents or self in avatar.onGiftOrder or self in avatar.awardMailboxContents or self in avatar.onAwardOrder:
            return 1
        return 0

    def getAcceptItemErrorText(self, retcode):
        if retcode == ToontownGlobals.P_ItemAvailable:
            if self.giftCode == ToontownGlobals.GIFT_RAT:
                return TTLocalizer.CatalogAcceptRATBeans
            else:
                return TTLocalizer.CatalogAcceptBeans
        return CatalogItem.CatalogItem.getAcceptItemErrorText(self, retcode)

    def saveHistory(self):
        return 0

    def getTypeName(self):
        return TTLocalizer.BeanTypeName

    def getName(self):
        name = '%s %s' % (self.beanAmount, TTLocalizer.BeanTypeName)
        return name

    def recordPurchase(self, avatar, optional):
        if avatar:
            avatar.addMoney(self.beanAmount)
        return ToontownGlobals.P_ItemAvailable

    def getPicture(self, avatar):
        beanJar = loader.loadModel('phase_3.5/models/gui/jar_gui')
        frame = self.makeFrame()
        beanJar.reparentTo(frame)
        beanJar.setPos(0, 0, 0)
        beanJar.setScale(2.5)
        self.hasPicture = True
        return (
         frame, None)

    def output(self, store=-1):
        return 'CatalogBeanItem(%s%s)' % (self.beanAmount, self.formatOptionalData(store))

    def compareTo(self, other):
        return self.beanAmount - other.beanAmount

    def getHashContents(self):
        return self.beanAmount

    def getBasePrice(self):
        return self.beanAmount

    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.CatalogItem.decodeDatagram(self, di, versionNumber, store)
        self.beanAmount = di.getUint16()

    def encodeDatagram(self, dg, store):
        CatalogItem.CatalogItem.encodeDatagram(self, dg, store)
        dg.addUint16(self.beanAmount)