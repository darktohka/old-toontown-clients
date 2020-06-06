# File: F (Python 2.2)

from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.task import Task
import FishBase
import FishPicker

class FishSellGUI(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('FishGui')
    
    def __init__(self, doneEvent):
        DirectFrame.__init__(self, relief = None, state = 'normal', geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor, geom_scale = (2.0, 1, 1.5), frameSize = (-1, 1, -1, 1), pos = (0, 0, 0), text = '', text_wordwrap = 26, text_scale = 0.059999999999999998, text_pos = (0, 0.65000000000000002))
        self.initialiseoptions(FishSellGUI)
        self.doneEvent = doneEvent
        self.picker = FishPicker.FishPicker(self)
        self.picker.load()
        self.picker.setPos(-0.58999999999999997, 0, 0.029999999999999999)
        self.picker.setScale(0.93000000000000005)
        newTankFish = base.localAvatar.fishTank.getFish()
        self.picker.update(newTankFish)
        self.picker.show()
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        okImageList = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        cancelImageList = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
        self.cancelButton = DirectButton(parent = self, relief = None, image = cancelImageList, pos = (0.29999999999999999, 0, -0.57999999999999996), text = TTLocalizer.FishGuiCancel, text_scale = 0.059999999999999998, text_pos = (0, -0.10000000000000001), command = self._FishSellGUI__cancel)
        self.okButton = DirectButton(parent = self, relief = None, image = okImageList, pos = (0.59999999999999998, 0, -0.57999999999999996), text = TTLocalizer.FishGuiOk, text_scale = 0.059999999999999998, text_pos = (0, -0.10000000000000001), command = self._FishSellGUI__sellFish)
        buttons.removeNode()
        self._FishSellGUI__updateFishValue()

    
    def destroy(self):
        DirectFrame.destroy(self)

    
    def _FishSellGUI__cancel(self):
        messenger.send(self.doneEvent, [
            0])

    
    def _FishSellGUI__sellFish(self):
        messenger.send(self.doneEvent, [
            1])

    
    def _FishSellGUI__updateFishValue(self):
        fishTank = base.localAvatar.getFishTank()
        num = len(fishTank)
        value = fishTank.getTotalValue()
        self['text'] = TTLocalizer.FishTankValue % {
            'name': base.localAvatar.getName(),
            'num': num,
            'value': value }
        self.setText()


