# File: C (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.gui.DirectGui import *
from pandac.PandaModules import *

class CatalogNotifyDialog:
    notify = DirectNotifyGlobal.directNotify.newCategory('CatalogNotifyDialog')
    
    def __init__(self, message):
        self.message = message
        self.messageIndex = 0
        self.frame = DirectFrame(relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.40000000000000002), text = message[0], text_wordwrap = 16, text_scale = 0.059999999999999998, text_pos = (-0.10000000000000001, 0.10000000000000001), pos = (0.40000000000000002, 0, 0.78000000000000003))
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        cancelImageList = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
        okImageList = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
        self.nextButton = DirectButton(parent = self.frame, relief = None, image = okImageList, command = self.handleButton, pos = (0, 0, -0.14000000000000001))
        self.doneButton = DirectButton(parent = self.frame, relief = None, image = cancelImageList, command = self.handleButton, pos = (0, 0, -0.14000000000000001))
        if len(message) == 1:
            self.nextButton.hide()
        else:
            self.doneButton.hide()

    
    def handleButton(self):
        self.messageIndex += 1
        if self.messageIndex >= len(self.message):
            self.cleanup()
            return None
        
        self.frame['text'] = self.message[self.messageIndex]
        if self.messageIndex + 1 == len(self.message):
            self.nextButton.hide()
            self.doneButton.show()
        

    
    def cleanup(self):
        if self.frame:
            self.frame.destroy()
        
        self.frame = None
        self.nextButton = None
        self.doneButton = None

    
    def _CatalogNotifyDialog__handleButton(self, value):
        self.cleanup()


