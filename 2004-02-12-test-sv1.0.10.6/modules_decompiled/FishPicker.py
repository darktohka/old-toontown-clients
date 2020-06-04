# File: F (Python 2.2)

import ToontownGlobals
from DirectGui import *
import Localizer
import FishPanel

class FishPicker(DirectScrolledList):
    
    def __init__(self, parent = aspect2d, **kw):
        self.fishList = []
        self.parent = parent
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        optiondefs = (('parent', self.parent, None), ('relief', None, None), ('incButton_image', (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), None), ('incButton_relief', None, None), ('incButton_scale', (1.6000000000000001, 1.6000000000000001, -1.6000000000000001), None), ('incButton_pos', (0.16, 0, -0.46999999999999997), None), ('incButton_image3_color', Vec4(0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 0.75), None), ('decButton_image', (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), None), ('decButton_relief', None, None), ('decButton_scale', (1.6000000000000001, 1.6000000000000001, 1.6000000000000001), None), ('decButton_pos', (0.16, 0, 0.089999999999999997), None), ('decButton_image3_color', Vec4(0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 0.75), None), ('itemFrame_pos', (-0.025000000000000001, 0, 0), None), ('itemFrame_scale', 0.54000000000000004, None), ('itemFrame_relief', None, None), ('itemFrame_frameSize', (-0.050000000000000003, 0.75, -0.75, 0.050000000000000003), None), ('numItemsVisible', 10, None), ('items', [], None))
        self.defineoptions(kw, optiondefs)
        DirectScrolledList.__init__(self, parent)
        self.initialiseoptions(FishPicker)
        self.fishGui = loader.loadModelCopy('phase_3.5/models/gui/fishingBook').find('**/bucket')
        self.fishGui.find('**/fram1').removeNode()
        self.fishGui.find('**/bubble').removeNode()
        self.fishGui.reparentTo(self, -1)
        self.fishGui.setPos(0.63, 0.10000000000000001, -0.10000000000000001)
        self.fishGui.setScale(0.035000000000000003)
        self.info = DirectLabel(parent = self, relief = None, text = '', text_scale = 0.055, pos = (0.17999999999999999, 0, -0.67000000000000004))
        self.fishPanel = FishPanel.FishPanel(parent = self)
        gui.removeNode()

    
    def destroy(self):
        DirectScrolledList.destroy(self)

    
    def hideFishPanel(self):
        self.fishPanel.hide()

    
    def hide(self):
        self.fishPanel.hide()
        DirectScrolledList.hide(self)

    
    def show(self):
        if len(self.fishList) >= 1:
            self.showFishPanel(self.fishList[0][0])
        else:
            self.hideFishPanel()
        DirectScrolledList.show(self)

    
    def load(self):
        self.fishPanel.load()
        self.fishPanel.setPos(1.05, 0, 0.10000000000000001)
        self.fishPanel.setScale(0.90000000000000002)

    
    def update(self, newFishes):
        for (fish, fishButton) in self.fishList[:]:
            self.removeItem(fishButton)
            fishButton.destroy()
            self.fishList.remove([
                fish,
                fishButton])
        
        for fish in newFishes:
            fishButton = self.makeFishButton(fish)
            self.addItem(fishButton)
            self.fishList.append([
                fish,
                fishButton])
        
        if len(self.fishList) >= 1:
            self.showFishPanel(self.fishList[0][0])
        else:
            self.hideFishPanel()
        value = 0
        for fish in newFishes:
            value += fish.getValue()
        
        maxFish = toonbase.localToon.getMaxFishTank()
        self.info['text'] = Localizer.FishPickerTotalValue % (len(newFishes), maxFish, value)

    
    def makeFishButton(self, fish):
        return DirectButton(relief = None, text = fish.getSpeciesName(), text_scale = 0.070000000000000007, text_align = TextNode.ALeft, text1_bg = Vec4(1, 1, 0, 1), text2_bg = Vec4(0.5, 0.90000000000000002, 1, 1), text3_fg = Vec4(0.40000000000000002, 0.80000000000000004, 0.40000000000000002, 1), command = self.showFishPanel, extraArgs = [
            fish])

    
    def showFishPanel(self, fish):
        self.fishPanel.update(fish)
        self.fishPanel.showFish()
        self.fishPanel.show()


