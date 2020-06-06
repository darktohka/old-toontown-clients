# File: L (Python 2.2)

import ToontownGlobals
import Localizer
from DirectGui import *

class LeaveToPayDialog:
    
    def __init__(self, destructorHook = None):
        self.destructorHook = destructorHook
        self.dialog = None
        self.okHandler = self._LeaveToPayDialog__handleLeaveToPayOK
        self.cancelHandler = self._LeaveToPayDialog__handleLeaveToPayCancel

    
    def setOK(self, handler):
        self.okHandler = handler

    
    def setCancel(self, handler):
        self.cancelHandler = handler

    
    def show(self):
        if self.dialog == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            self.dialog = DirectFrame(pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (0.90000000000000002, 1.0, 0.5), text = Localizer.LeaveToPay, text_align = TextNode.ALeft, text_wordwrap = 14, text_scale = 0.059999999999999998, text_pos = (-0.40000000000000002, 0.14999999999999999), textMayChange = 0)
            DirectButton(self.dialog, image = okButtonImage, relief = None, text = Localizer.LeaveToPayYes, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (-0.29999999999999999, 0.0, -0.10000000000000001), command = self.okHandler)
            DirectButton(self.dialog, image = cancelButtonImage, relief = None, text = Localizer.LeaveToPayNo, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.29999999999999999, 0.0, -0.10000000000000001), command = self.cancelHandler)
            buttons.removeNode()
        
        self.dialog.show()

    
    def hide(self):
        self.dialog.hide()

    
    def destroy(self):
        if self.destructorHook:
            self.destructorHook()
        
        if self.dialog:
            self.dialog.hide()
            self.dialog.destroy()
        
        self.dialog = None
        self.okHandler = None
        self.cancelHandler = None

    
    def _LeaveToPayDialog__handleLeaveToPayOK(self):
        self.destroy()
        if launcher:
            launcher.setRegistry('EXIT_PAGE', 'purchase')
        
        toonbase.tcr.loginFSM.request('shutdown')

    
    def _LeaveToPayDialog__handleLeaveToPayCancel(self):
        self.destroy()


