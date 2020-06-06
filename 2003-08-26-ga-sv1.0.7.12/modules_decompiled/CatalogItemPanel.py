# File: C (Python 2.2)

from DirectGui import *
import ToontownGlobals
import ToontownDialog
import Localizer
import CatalogItemTypes
import CatalogItem
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
        (self.picture, self.ival) = self['item'].getPicture(toonbase.localToon)
        if self.picture:
            self.picture.reparentTo(self)
            self.picture.setScale(0.14999999999999999)
        
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
        self.priceLabel = DirectLabel(parent = self, relief = None, pos = (0, 0, -0.29999999999999999), scale = 0.070000000000000007, text = str(self['item'].getPrice(self['type'])) + ' ' + Localizer.CatalogCurrency, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_font = ToontownGlobals.getSignFont(), text_align = TextNode.ACenter)
        buttonModels = loader.loadModelOnce('phase_3.5/models/gui/inventory_gui')
        upButton = buttonModels.find('**/InventoryButtonUp')
        downButton = buttonModels.find('**/InventoryButtonDown')
        rolloverButton = buttonModels.find('**/InventoryButtonRollover')
        self.buyButton = DirectButton(parent = self, relief = None, pos = (0.20000000000000001, 0, 0.14999999999999999), scale = (0.69999999999999996, 1, 0.80000000000000004), text = Localizer.CatalogBuyText, text_scale = (0.059999999999999998, 0.050000000000000003), text_pos = (-0.0050000000000000001, -0.01), image = (upButton, downButton, rolloverButton, upButton), image_color = (1.0, 0.20000000000000001, 0.20000000000000001, 1), image0_color = Vec4(1.0, 0.40000000000000002, 0.40000000000000002, 1), image3_color = Vec4(1.0, 0.40000000000000002, 0.40000000000000002, 0.40000000000000002), command = self._CatalogItemPanel__handlePurchaseRequest)
        self.updateBuyButton()

    
    def unload(self):
        if not (self.loaded):
            DirectFrame.destroy(self)
            return None
        
        self.loaded = 0
        self['item'].requestPurchaseCleanup()
        DirectFrame.destroy(self)
        del self.typeLabel
        del self.auxText
        del self.nameLabel
        del self.priceLabel
        del self.buyButton
        del self.picture
        if self.ival:
            self.ival.finish()
            del self.ival
        
        if self.verify:
            self.verify.cleanup()
            del self.verify
        

    
    def destroy(self):
        self.unload()

    
    def updateBuyButton(self):
        if not (self.loaded):
            return None
        
        if self['item'].reachedPurchaseLimit(toonbase.localToon):
            max = self['item'].getPurchaseLimit()
            if max <= 1:
                self.auxText['text'] = Localizer.CatalogPurchasedText
            else:
                self.auxText['text'] = Localizer.CatalogPurchasedMaxText
            self.buyButton['state'] = DISABLED
            self.buyButton.show()
        elif self['item'].getPrice(self['type']) <= toonbase.localToon.getMoney() + toonbase.localToon.getBankMoney():
            orderCount = toonbase.localToon.onOrder.count(self['item'])
            if orderCount > 0:
                if orderCount > 1:
                    self.auxText['text'] = '%d %s' % (orderCount, Localizer.CatalogOnOrderText)
                else:
                    self.auxText['text'] = Localizer.CatalogOnOrderText
            else:
                self.auxText['text'] = ''
            self.buyButton['state'] = NORMAL
            self.buyButton.show()
        else:
            self.auxText['text'] = ''
            self.buyButton['state'] = DISABLED
            self.buyButton.show()

    
    def _CatalogItemPanel__handlePurchaseRequest(self):
        if self['item'].replacesExisting() and self['item'].hasExisting():
            message = Localizer.CatalogOnlyOnePurchase % {
                'old': self['item'].getYourOldDesc(),
                'item': self['item'].getName(),
                'price': self['item'].getPrice(self['type']) }
        else:
            message = Localizer.CatalogVerifyPurchase % {
                'item': self['item'].getName(),
                'price': self['item'].getPrice(self['type']) }
        self.verify = ToontownDialog.GlobalDialog(doneEvent = 'verifyDone', message = message, style = ToontownDialog.TwoChoice)
        self.verify.show()
        self.accept('verifyDone', self._CatalogItemPanel__handleVerifyPurchase)

    
    def _CatalogItemPanel__handleVerifyPurchase(self):
        status = self.verify.doneStatus
        self.ignore('verifyDone')
        self.verify.cleanup()
        del self.verify
        self.verify = None
        if status == 'ok':
            messenger.send('CatalogItemPurchaseRequest', [
                self['item']])
        


