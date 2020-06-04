# File: C (Python 2.2)

from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer
import CatalogItemTypes
import CatalogItem
from CatalogWallpaperItem import getAllWallpapers
from CatalogFlooringItem import getAllFloorings
from CatalogMouldingItem import getAllMouldings
from CatalogWainscotingItem import getAllWainscotings
from CatalogFurnitureItem import getAllFurnitures
CATALOG_PANEL_WORDWRAP = 8

class CatalogItemPanel(DirectFrame):
    
    def __init__(self, parent = aspect2d, **kw):
        optiondefs = (('item', None, INITOPT), ('type', CatalogItem.CatalogTypeUnspecified, INITOPT), ('relief', None, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.loaded = 0
        self.initialiseoptions(CatalogItemPanel)

    
    def load(self):
        if self.loaded:
            return None
        
        self.loaded = 1
        self.verify = None
        self.pictureFrame = self.attachNewNode('pictureFrame')
        self.pictureFrame.setScale(0.14999999999999999)
        self.itemIndex = 0
        self.ival = None
        typeCode = self['item'].getTypeCode()
        if self['item'].needsCustomize() and typeCode == CatalogItemTypes.WALLPAPER_ITEM and typeCode == CatalogItemTypes.FLOORING_ITEM and typeCode == CatalogItemTypes.MOULDING_ITEM and typeCode == CatalogItemTypes.FURNITURE_ITEM or typeCode == CatalogItemTypes.WAINSCOTING_ITEM:
            if typeCode == CatalogItemTypes.WALLPAPER_ITEM:
                self.items = getAllWallpapers(self['item'].patternIndex)
            elif typeCode == CatalogItemTypes.FLOORING_ITEM:
                self.items = getAllFloorings(self['item'].patternIndex)
            elif typeCode == CatalogItemTypes.MOULDING_ITEM:
                self.items = getAllMouldings(self['item'].patternIndex)
            elif typeCode == CatalogItemTypes.FURNITURE_ITEM:
                self.items = getAllFurnitures(self['item'].furnitureType)
            elif typeCode == CatalogItemTypes.WAINSCOTING_ITEM:
                self.items = getAllWainscotings(self['item'].patternIndex)
            
            self.numItems = len(self.items)
            if self.numItems > 1:
                guiItems = loader.loadModelCopy('phase_5.5/models/gui/catalog_gui')
                nextUp = guiItems.find('**/arrow_up')
                nextRollover = guiItems.find('**/arrow_Rollover')
                nextDown = guiItems.find('**/arrow_Down')
                prevUp = guiItems.find('**/arrowUp')
                prevDown = guiItems.find('**/arrowDown1')
                prevRollover = guiItems.find('**/arrowRollover')
                self.nextVariant = DirectButton(parent = self, relief = None, image = (nextUp, nextDown, nextRollover, nextUp), image3_color = (1, 1, 1, 0.40000000000000002), pos = (0.13, 0, 0), command = self.showNextVariant)
                self.prevVariant = DirectButton(parent = self, relief = None, image = (prevUp, prevDown, prevRollover, prevUp), image3_color = (1, 1, 1, 0.40000000000000002), pos = (-0.13, 0, 0), command = self.showPrevVariant, state = DISABLED)
                self.variantPictures = [
                    (None, None)] * self.numItems
            else:
                self.variantPictures = [
                    (None, None)]
            self.showCurrentVariant()
        else:
            (picture, self.ival) = self['item'].getPicture(base.localAvatar)
            if picture:
                picture.reparentTo(self)
                picture.setScale(0.14999999999999999)
            
            self.items = [
                self['item']]
            self.variantPictures = [
                (picture, self.ival)]
        self.typeLabel = DirectLabel(parent = self, relief = None, pos = (0, 0, 0.23999999999999999), scale = 0.074999999999999997, text = self['item'].getTypeName(), text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_font = ToontownGlobals.getInterfaceFont(), text_wordwrap = CATALOG_PANEL_WORDWRAP)
        self.auxText = DirectLabel(parent = self, relief = None, scale = 0.050000000000000003, pos = (-0.23999999999999999, 0, 0.16))
        self.auxText.setHpr(0, 0, 30)
        self.nameLabel = DirectLabel(parent = self, relief = None, text = self['item'].getDisplayName(), text_fg = (0, 0, 0, 1), text_font = ToontownGlobals.getInterfaceFont(), text_wordwrap = CATALOG_PANEL_WORDWRAP)
        if self['item'].getTypeCode() == CatalogItemTypes.CHAT_ITEM:
            numRows = self.nameLabel.component('text0').textNode.getNumRows()
            if numRows == 1:
                namePos = (0, 0, -0.059999999999999998)
            elif numRows == 2:
                namePos = (0, 0, -0.029999999999999999)
            else:
                namePos = (0, 0, 0)
            nameScale = 0.063
        else:
            namePos = (0, 0, -0.22)
            nameScale = 0.059999999999999998
        self.nameLabel.setPos(*namePos)
        self.nameLabel.setScale(nameScale)
        priceStr = str(self['item'].getPrice(self['type'])) + ' ' + TTLocalizer.CatalogCurrency
        priceScale = 0.070000000000000007
        if self['item'].isSaleItem():
            priceStr = TTLocalizer.CatalogSaleItem + priceStr
            priceScale = 0.059999999999999998
        
        self.priceLabel = DirectLabel(parent = self, relief = None, pos = (0, 0, -0.29999999999999999), scale = priceScale, text = priceStr, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_font = ToontownGlobals.getSignFont(), text_align = TextNode.ACenter)
        buttonModels = loader.loadModelOnce('phase_3.5/models/gui/inventory_gui')
        upButton = buttonModels.find('**/InventoryButtonUp')
        downButton = buttonModels.find('**/InventoryButtonDown')
        rolloverButton = buttonModels.find('**/InventoryButtonRollover')
        self.buyButton = DirectButton(parent = self, relief = None, pos = (0.20000000000000001, 0, 0.14999999999999999), scale = (0.69999999999999996, 1, 0.80000000000000004), text = TTLocalizer.CatalogBuyText, text_scale = (0.059999999999999998, 0.050000000000000003), text_pos = (-0.0050000000000000001, -0.01), image = (upButton, downButton, rolloverButton, upButton), image_color = (1.0, 0.20000000000000001, 0.20000000000000001, 1), image0_color = Vec4(1.0, 0.40000000000000002, 0.40000000000000002, 1), image3_color = Vec4(1.0, 0.40000000000000002, 0.40000000000000002, 0.40000000000000002), command = self._CatalogItemPanel__handlePurchaseRequest)
        self.updateBuyButton()

    
    def showNextVariant(self):
        self.hideCurrentVariant()
        self.itemIndex += 1
        if self.itemIndex >= self.numItems - 1:
            self.itemIndex = self.numItems - 1
            self.nextVariant['state'] = DISABLED
        else:
            self.nextVariant['state'] = NORMAL
        self.prevVariant['state'] = NORMAL
        self.showCurrentVariant()

    
    def showPrevVariant(self):
        self.hideCurrentVariant()
        self.itemIndex -= 1
        if self.itemIndex < 0:
            self.itemIndex = 0
            self.prevVariant['state'] = DISABLED
        else:
            self.prevVariant['state'] = NORMAL
        self.nextVariant['state'] = NORMAL
        self.showCurrentVariant()

    
    def showCurrentVariant(self):
        (newPic, self.ival) = self.variantPictures[self.itemIndex]
        if self.ival:
            self.ival.finish()
        
        if not newPic:
            variant = self.items[self.itemIndex]
            (newPic, self.ival) = variant.getPicture(base.localAvatar)
            self.variantPictures[self.itemIndex] = (newPic, self.ival)
        
        newPic.reparentTo(self.pictureFrame)
        if self.ival:
            self.ival.loop()
        

    
    def hideCurrentVariant(self):
        currentPic = self.variantPictures[self.itemIndex][0]
        if currentPic:
            currentPic.detachNode()
        

    
    def unload(self):
        if not (self.loaded):
            DirectFrame.destroy(self)
            return None
        
        self.loaded = 0
        self['item'].requestPurchaseCleanup()
        for (picture, ival) in self.variantPictures:
            if picture:
                picture.destroy()
            
            if ival:
                ival.finish()
            
        
        self.ival = None
        if self.verify:
            self.verify.cleanup()
        
        DirectFrame.destroy(self)

    
    def destroy(self):
        self.unload()

    
    def updateBuyButton(self):
        if not (self.loaded):
            return None
        
        orderCount = base.localAvatar.onOrder.count(self['item'])
        if orderCount > 0:
            if orderCount > 1:
                auxText = '%d %s' % (orderCount, TTLocalizer.CatalogOnOrderText)
            else:
                auxText = TTLocalizer.CatalogOnOrderText
        else:
            auxText = ''
        if self['item'].reachedPurchaseLimit(base.localAvatar):
            max = self['item'].getPurchaseLimit()
            if max <= 1:
                auxText = TTLocalizer.CatalogPurchasedText
            else:
                auxText = TTLocalizer.CatalogPurchasedMaxText
            self.buyButton['state'] = DISABLED
            self.buyButton.show()
        elif self['item'].getPrice(self['type']) <= base.localAvatar.getMoney() + base.localAvatar.getBankMoney():
            self.buyButton['state'] = NORMAL
            self.buyButton.show()
        else:
            self.buyButton['state'] = DISABLED
            self.buyButton.show()
        self.auxText['text'] = auxText

    
    def _CatalogItemPanel__handlePurchaseRequest(self):
        if self['item'].replacesExisting() and self['item'].hasExisting():
            message = TTLocalizer.CatalogOnlyOnePurchase % {
                'old': self['item'].getYourOldDesc(),
                'item': self['item'].getName(),
                'price': self['item'].getPrice(self['type']) }
        else:
            message = TTLocalizer.CatalogVerifyPurchase % {
                'item': self['item'].getName(),
                'price': self['item'].getPrice(self['type']) }
        self.verify = TTDialog.TTGlobalDialog(doneEvent = 'verifyDone', message = message, style = TTDialog.TwoChoice)
        self.verify.show()
        self.accept('verifyDone', self._CatalogItemPanel__handleVerifyPurchase)

    
    def _CatalogItemPanel__handleVerifyPurchase(self):
        status = self.verify.doneStatus
        self.ignore('verifyDone')
        self.verify.cleanup()
        del self.verify
        self.verify = None
        if status == 'ok':
            item = self.items[self.itemIndex]
            messenger.send('CatalogItemPurchaseRequest', [
                item])
        


