# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\catalog\CatalogAtticItem.py
import CatalogItem
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals

class CatalogAtticItem(CatalogItem.CatalogItem):
    __module__ = __name__

    def storedInAttic(self):
        return 1

    def isDeletable(self):
        return 1

    def getHouseInfo(self, avatar):
        houseId = avatar.houseId
        if not houseId:
            self.notify.warning('Avatar %s has no houseId associated.' % avatar.doId)
            return (None, ToontownGlobals.P_InvalidIndex)
        house = simbase.air.doId2do.get(houseId)
        if not house:
            self.notify.warning('House %s (for avatar %s) not instantiated.' % (houseId, avatar.doId))
            return (None, ToontownGlobals.P_InvalidIndex)
        numAtticItems = len(house.atticItems) + len(house.atticWallpaper) + len(house.atticWindows)
        numHouseItems = numAtticItems + len(house.interiorItems)
        if numHouseItems >= ToontownGlobals.MaxHouseItems and not self.replacesExisting():
            return (
             house, ToontownGlobals.P_NoRoomForItem)
        return (house, ToontownGlobals.P_ItemAvailable)

    def requestPurchase(self, phone, callback):
        from toontown.toontowngui import TTDialog
        avatar = base.localAvatar
        itemsOnOrder = 0
        for item in avatar.onOrder + avatar.mailboxContents:
            if item.storedInAttic() and not item.replacesExisting():
                itemsOnOrder += 1

        numHouseItems = phone.numHouseItems + itemsOnOrder
        if numHouseItems >= ToontownGlobals.MaxHouseItems and not self.replacesExisting():
            self.requestPurchaseCleanup()
            buttonCallback = PythonUtil.Functor(self.__handleFullPurchaseDialog, phone, callback)
            self.dialog = TTDialog.TTDialog(style=TTDialog.YesNo, text=TTLocalizer.CatalogPurchaseHouseFull, text_wordwrap=15, command=buttonCallback)
            self.dialog.show()
        else:
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)

    def requestPurchaseCleanup(self):
        if hasattr(self, 'dialog'):
            self.dialog.cleanup()
            del self.dialog

    def __handleFullPurchaseDialog(self, phone, callback, buttonValue):
        from toontown.toontowngui import TTDialog
        self.requestPurchaseCleanup()
        if buttonValue == DGG.DIALOG_OK:
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)
        else:
            callback(ToontownGlobals.P_UserCancelled, self)

    def getAcceptItemErrorText(self, retcode):
        if retcode == ToontownGlobals.P_ItemAvailable:
            return TTLocalizer.CatalogAcceptInAttic
        elif retcode == ToontownGlobals.P_NoRoomForItem:
            return TTLocalizer.CatalogAcceptHouseFull
        return CatalogItem.CatalogItem.getAcceptItemErrorText(self, retcode)