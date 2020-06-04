# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\estate\FlowerSellGUI.py
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.task import Task
import FlowerBase, FlowerPicker

class FlowerSellGUI(DirectFrame):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FlowerGui')

    def __init__(self, doneEvent):
        DirectFrame.__init__(self, relief=None, state='normal', geom=DGG.getDefaultDialogGeom(), geom_color=ToontownGlobals.GlobalDialogColor, geom_scale=(2.0,
                                                                                                                                                           1,
                                                                                                                                                           1.5), frameSize=(-1,
                                                                                                                                                                            1,
                                                                                                                                                                            -1,
                                                                                                                                                                            1), pos=(0,
                                                                                                                                                                                     0,
                                                                                                                                                                                     0), text='', text_wordwrap=26, text_scale=TTLocalizer.FSGUIdirectFrame, text_pos=(0,
                                                                                                                                                                                                                                                                       0.65))
        self.initialiseoptions(FlowerSellGUI)
        self.doneEvent = doneEvent
        self.picker = FlowerPicker.FlowerPicker(self)
        self.picker.load()
        self.picker.setPos(-0.59, 0, 0.03)
        self.picker.setScale(0.93)
        newBasketFlower = base.localAvatar.flowerBasket.getFlower()
        self.picker.update(newBasketFlower)
        self.picker.show()
        buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        okImageList = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        cancelImageList = (
         buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
        self.cancelButton = DirectButton(parent=self, relief=None, image=cancelImageList, pos=(0.3, 0, -0.58), text=TTLocalizer.FlowerGuiCancel, text_scale=TTLocalizer.FSGUIcancelButton, text_pos=(0, -0.1), command=self.__cancel)
        self.okButton = DirectButton(parent=self, relief=None, image=okImageList, pos=(0.6, 0, -0.58), text=TTLocalizer.FlowerGuiOk, text_scale=TTLocalizer.FSGUIokButton, text_pos=(0, -0.1), command=self.__sellFlower)
        buttons.removeNode()
        self.__updateFlowerValue()
        base.cr.playGame.getPlace().detectedFlowerSellUse()
        return

    def destroy(self):
        DirectFrame.destroy(self)
        base.cr.playGame.getPlace().detectedFlowerSellDone()

    def __cancel(self):
        messenger.send(self.doneEvent, [0])

    def __sellFlower(self):
        messenger.send(self.doneEvent, [1])

    def __updateFlowerValue(self):
        flowerBasket = base.localAvatar.getFlowerBasket()
        num = len(flowerBasket)
        value = flowerBasket.getTotalValue()
        self['text'] = TTLocalizer.FlowerBasketValue % {'name': base.localAvatar.getName(), 'num': num, 'value': value}
        self.setText()