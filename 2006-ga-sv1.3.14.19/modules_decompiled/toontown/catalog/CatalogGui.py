# File: C (Python 2.2)

from direct.gui.DirectGui import *
import CatalogItemPanel
NUM_ITEMS_SHOWN = 3

class CatalogGui:
    
    def __init__(self, type, list = [], parent = None):
        self.type = type
        self.itemList = list
        self.parent = parent
        self.panelPicker = None
        self.frame = DirectFrame(parent = parent, relief = None)
        self.load()

    
    def show(self):
        self.frame.show()

    
    def hide(self):
        self.frame.hide()

    
    def load(self):
        itemStrings = []
        for i in range(0, len(self.itemList)):
            itemStrings.append(self.itemList[i].getName())
        
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        self.panelPicker = DirectScrolledList(parent = self.frame, items = itemStrings, command = self.scrollItem, itemMakeFunction = CatalogItemPanel.CatalogItemPanel, itemMakeExtraArgs = [
            self.itemList,
            self.type], numItemsVisible = NUM_ITEMS_SHOWN, pos = (0.5, 0, 0.40000000000000002), incButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_scale = (1.3, 1.3, -1.3), incButton_pos = (0, 0, -1.05), incButton_image3_color = Vec4(1, 1, 1, 0.29999999999999999), decButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_scale = (1.3, 1.3, 1.3), decButton_pos = (0, 0, 0.25), decButton_image3_color = Vec4(1, 1, 1, 0.29999999999999999))

    
    def unload(self):
        del self.parent
        del self.itemList
        del self.panelPicker
        self.frame.destroy()

    
    def update(self):
        for item in self.panelPicker['items']:
            if type(item) != type(''):
                item.updateBuyButton()
            
        

    
    def scrollItem(self):
        pass


