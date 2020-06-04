# File: C (Python 2.2)

import CatalogItem
import Localizer
import PythonUtil
import ToontownGlobals

class CatalogAtticItem(CatalogItem.CatalogItem):
    
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
            return (house, ToontownGlobals.P_NoRoomForItem)
        
        return (house, ToontownGlobals.P_ItemAvailable)

    
    def requestPurchase(self, phone, callback):
        import ToontownDialog
        avatar = toonbase.localToon
        itemsOnOrder = 0
        for item in avatar.onOrder + avatar.mailboxContents:
            if item.storedInAttic() and not item.replacesExisting():
                itemsOnOrder += 1
            
        
        numHouseItems = phone.numHouseItems + itemsOnOrder
        if numHouseItems >= ToontownGlobals.MaxHouseItems and not self.replacesExisting():
            self.requestPurchaseCleanup()
            buttonCallback = PythonUtil.Functor(self._CatalogAtticItem__handleFullPurchaseDialog, phone, callback)
            self.dialog = ToontownDialog.ToontownDialog(style = ToontownDialog.YesNo, text = Localizer.CatalogPurchaseHouseFull, text_wordwrap = 15, command = buttonCallback)
            self.dialog.show()
        else:
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)

    
    def requestPurchaseCleanup(self):
        if hasattr(self, 'dialog'):
            self.dialog.cleanup()
            del self.dialog
        

    
    def _CatalogAtticItem__handleFullPurchaseDialog(self, phone, callback, buttonValue):
        import ToontownDialog
        self.requestPurchaseCleanup()
        if buttonValue == ToontownDialog.DIALOG_OK:
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)
        else:
            callback(ToontownGlobals.P_UserCancelled, self)

    
    def getAcceptItemErrorText(self, retcode):
        if retcode == ToontownGlobals.P_ItemAvailable:
            return Localizer.CatalogAcceptInAttic
        elif retcode == ToontownGlobals.P_NoRoomForItem:
            return Localizer.CatalogAcceptHouseFull
        
        return CatalogItem.CatalogItem.getAcceptItemErrorText(self, retcode)


