# File: T (Python 2.2)

from ShowBaseGlobal import *
from DirectObject import *
from DirectGui import *
import DirectNotifyGlobal
import string
import ToontownGlobals
import Localizer
NoButtons = 0
Acknowledge = 1
CancelOnly = 2
TwoChoice = 3

class ToontownDialog(DirectDialog):
    
    def __init__(self, parent = aspect2d, style = NoButtons, **kw):
        self.style = style
        buttons = None
        if self.style != NoButtons:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        
        if self.style == TwoChoice:
            okImageList = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelImageList = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            buttonImage = [
                okImageList,
                cancelImageList]
            buttonText = [
                Localizer.ToontownDialogOK,
                Localizer.ToontownDialogCancel]
            buttonValue = [
                DIALOG_OK,
                DIALOG_CANCEL]
        elif self.style == Acknowledge:
            okImageList = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            buttonImage = [
                okImageList]
            buttonText = [
                Localizer.ToontownDialogOK]
            buttonValue = [
                DIALOG_OK]
        elif self.style == CancelOnly:
            cancelImageList = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            buttonImage = [
                cancelImageList]
            buttonText = [
                Localizer.ToontownDialogCancel]
            buttonValue = [
                DIALOG_CANCEL]
        elif self.style == NoButtons:
            buttonImage = []
            buttonText = []
            buttonValue = []
        else:
            self.notify.error('No such style as: ' + str(self.style))
        optiondefs = (('buttonImageList', buttonImage, INITOPT), ('buttonTextList', buttonText, INITOPT), ('buttonValueList', buttonValue, INITOPT), ('buttonPadSF', 2.2000000000000002, INITOPT), ('text_font', getDefaultFont(), None), ('text_wordwrap', 12, None), ('text_scale', 0.070000000000000007, None), ('buttonSize', (-0.050000000000000003, 0.050000000000000003, -0.050000000000000003, 0.050000000000000003), None), ('button_pad', (0, 0), None), ('button_relief', None, None), ('button_text_pos', (0, -0.10000000000000001), None), ('fadeScreen', 0.5, None), ('image_color', ToontownGlobals.GlobalDialogColor, None))
        self.defineoptions(kw, optiondefs)
        DirectDialog.__init__(self)
        self.initialiseoptions(ToontownDialog)
        if buttons != None:
            buttons.removeNode()
        



class GlobalDialog(ToontownDialog):
    notify = DirectNotifyGlobal.directNotify.newCategory('GlobalDialog')
    
    def __init__(self, message = '', doneEvent = None, style = NoButtons, okButtonText = Localizer.ToontownDialogOK, cancelButtonText = Localizer.ToontownDialogCancel, **kw):
        if doneEvent == None and style != NoButtons:
            self.notify.error('Boxes with buttons must specify a doneEvent.')
        
        self._GlobalDialog__doneEvent = doneEvent
        if style == NoButtons:
            buttonText = []
        elif style == Acknowledge:
            buttonText = [
                okButtonText]
        elif style == CancelOnly:
            buttonText = [
                cancelButtonText]
        else:
            buttonText = [
                okButtonText,
                cancelButtonText]
        optiondefs = (('dialogName', 'globalDialog', INITOPT), ('buttonTextList', buttonText, INITOPT), ('text', message, None), ('command', self.handleButton, None))
        self.defineoptions(kw, optiondefs)
        ToontownDialog.__init__(self, style = style)
        self.initialiseoptions(GlobalDialog)

    
    def handleButton(self, value):
        if value == DIALOG_OK:
            self.doneStatus = 'ok'
            messenger.send(self._GlobalDialog__doneEvent)
        elif value == DIALOG_CANCEL:
            self.doneStatus = 'cancel'
            messenger.send(self._GlobalDialog__doneEvent)
        


