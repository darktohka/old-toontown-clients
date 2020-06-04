# File: F (Python 2.2)

import ToontownGlobals
from DirectGui import *
import Localizer
import GenusPanel
import FishGlobals

class FishBrowser(DirectScrolledList):
    
    def __init__(self, parent = aspect2d, **kw):
        self.parent = parent
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        optiondefs = (('parent', self.parent, None), ('relief', None, None), ('incButton_image', (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), None), ('incButton_relief', None, None), ('incButton_scale', (1.3, 1.3, -1.3), None), ('incButton_pos', (0, 0, -0.52500000000000002), None), ('incButton_image3_color', Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 0.5), None), ('decButton_image', (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), None), ('decButton_relief', None, None), ('decButton_scale', (1.3, 1.3, 1.3), None), ('decButton_pos', (0, 0, 0.52500000000000002), None), ('decButton_image3_color', Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 0.5), None), ('numItemsVisible', 1, None), ('items', [], None), ('scrollSpeed', 4, None))
        gui.removeNode()
        self.defineoptions(kw, optiondefs)
        DirectScrolledList.__init__(self, parent)
        self.initialiseoptions(FishBrowser)

    
    def destroy(self):
        DirectScrolledList.destroy(self)

    
    def load(self):
        for genus in FishGlobals.getGenera():
            panel = GenusPanel.GenusPanel(genus = genus)
            panel.load()
            self.addItem(panel)
            panel.setPos(0.34999999999999998, 0, -0.40000000000000002)
            panel.setScale(1.2)
        

    
    def update(self):
        self.scrollBy(0)
        return None


