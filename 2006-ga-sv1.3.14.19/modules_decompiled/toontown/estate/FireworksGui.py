# File: F (Python 2.2)

from direct.gui.DirectGui import *
from direct.gui.DirectScrolledList import *
from toontown.toonbase import ToontownGlobals
import FireworkItemPanel
from direct.directnotify import DirectNotifyGlobal
from toontown.effects import FireworkGlobals
from toontown.effects import Fireworks
NUM_ITEMS_SHOWN = 4

class FireworksGui(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('FireworksGui')
    
    def __init__(self, doneEvent, shootEvent):
        DirectFrame.__init__(self, relief = None, geom = getDefaultDialogGeom(), geom_color = (0, 0.5, 1, 1), geom_scale = (0.42999999999999999, 1, 1.3999999999999999), pos = (1.1000000000000001, 0, 0))
        self.initialiseoptions(FireworksGui)
        self.doneEvent = doneEvent
        self.shootEvent = shootEvent
        self.itemList = []
        self.type = None
        self.load()

    
    def load(self):
        itemTypes = [
            0,
            1,
            2,
            3,
            4,
            5]
        itemStrings = []
        for i in itemTypes:
            itemStrings.append(FireworkGlobals.Names[i])
        
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        self.panelPicker = DirectScrolledList(parent = self, items = itemStrings, command = self.scrollItem, itemMakeFunction = FireworkItemPanel.FireworkItemPanel, itemMakeExtraArgs = [
            self,
            itemTypes,
            self.shootEvent], numItemsVisible = NUM_ITEMS_SHOWN, incButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_scale = (0.5, 1, -1), incButton_pos = (0, 0, -1.0800000000000001), incButton_image3_color = Vec4(1, 1, 1, 0.29999999999999999), decButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_scale = (0.5, 1, 1), decButton_pos = (0, 0, 0.20000000000000001), decButton_image3_color = Vec4(1, 1, 1, 0.29999999999999999))
        self.panelPicker.setPos(-0.059999999999999998, 0, 0.41999999999999998)
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        cancelImageList = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
        self.cancelButton = DirectButton(parent = self, relief = None, image = cancelImageList, pos = (0.14999999999999999, 0, -0.62), text_scale = 0.059999999999999998, text_pos = (0, -0.10000000000000001), command = self._FireworksGui__cancel)
        buttons.removeNode()
        self.hilightColor = VBase4(1, 1, 1, 1)
        self.bgColor = VBase4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
        self.colorButtons = []
        for i in Fireworks.colors.keys():
            color = Fireworks.colors[i]
            height = 0.070000000000000007
            paddedHeight = 0.10000000000000001
            buttonBg = DirectFrame(self, geom = getDefaultDialogGeom(), geom_scale = paddedHeight, geom_color = self.bgColor, pos = (0.14999999999999999, 0, 0.5 - (paddedHeight + 0.025000000000000001) * i), relief = None)
            self.initialiseoptions(buttonBg)
            button = DirectButton(buttonBg, image = (getDefaultDialogGeom(), getDefaultDialogGeom(), getDefaultDialogGeom()), relief = None, command = self._FireworksGui__handleColor, extraArgs = [
                i])
            button.setScale(height)
            button.setColor(color)
            self.colorButtons.append([
                button,
                buttonBg])
        
        self._FireworksGui__initColor(0)

    
    def unload(self):
        del self.parent
        del self.itemList
        del self.panelPicker

    
    def update(self):
        pass

    
    def _FireworksGui__cancel(self):
        messenger.send(self.doneEvent)
        return None

    
    def _FireworksGui__initColor(self, index):
        self.colorButtons[index][1]['geom_color'] = self.hilightColor
        self.colorButtons[index][1].setScale(1.2)
        self.curColor = index
        self.fadeColor = 0

    
    def _FireworksGui__handleColor(self, index):
        color = Fireworks.colors[index]
        for i in range(len(self.colorButtons)):
            self.colorButtons[i][1]['geom_color'] = self.bgColor
            self.colorButtons[i][1].setScale(1)
        
        self.colorButtons[index][1].setScale(1.2)
        if index == self.curColor:
            self.fadeColor = (self.fadeColor + 1) % len(Fireworks.colors)
        else:
            self.fadeColor = 0
        self.colorButtons[index][1]['geom_color'] = Fireworks.colors[self.fadeColor]
        self.curColor = index

    
    def scrollItem(self):
        pass

    
    def getCurColor(self):
        return (self.curColor, self.fadeColor)


