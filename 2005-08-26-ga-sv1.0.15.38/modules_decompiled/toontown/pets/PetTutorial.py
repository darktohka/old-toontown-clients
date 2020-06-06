# File: P (Python 2.2)

from direct.gui.DirectGui import *
from direct.fsm import FSM
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class PetTutorial(DirectFrame, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('PetTutorial')
    
    def __init__(self, doneEvent):
        FSM.FSM.__init__(self, 'PetTutorial')
        self.doneEvent = doneEvent
        self.setStateArray([
            'Page1',
            'Page2',
            'Page3'])
        DirectFrame.__init__(self, pos = (0.0, 0.0, 0.0), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.5, 1.5, 0.90000000000000002), text = '', text_scale = 0.059999999999999998)
        self['image'] = getDefaultDialogGeom()
        self.title = DirectLabel(self, relief = None, text = '', text_pos = (0.0, 0.32000000000000001), text_fg = (1, 0, 0, 1), text_scale = 0.13, text_font = ToontownGlobals.getSignFont())
        images = loader.loadModelOnce('phase_5.5/models/gui/PetTutorial')
        self.iPage1 = DirectFrame(self, image = images.find('**/PetTutorialPanel'), scale = 0.75, pos = (-0.55000000000000004, -0.10000000000000001, 0))
        self.iPage1.hide()
        self.iPage2 = DirectFrame(self, image = images.find('**/PetTutorialSpeedChat'), scale = 0.75, pos = (0.42999999999999999, -0.10000000000000001, 0.050000000000000003))
        self.iPage2.hide()
        self.iPage3 = DirectFrame(self, image = images.find('**/PetTutorialCattlelog'), scale = 0.75, pos = (-0.55000000000000004, -0.10000000000000001, 0))
        self.iPage3.hide()
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
        self.bNext = DirectButton(self, image = (gui.find('**/Horiz_Arrow_UP'), gui.find('**/Horiz_Arrow_DN'), gui.find('**/Horiz_Arrow_Rllvr'), gui.find('**/Horiz_Arrow_UP')), image3_color = Vec4(1, 1, 1, 0.5), relief = None, text = TTLocalizer.PetTutorialNext, text3_fg = Vec4(0, 0, 0, 0.5), text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.20000000000000001, -0.29999999999999999, -0.25), command = self.requestNext)
        self.bPrev = DirectButton(self, image = (gui.find('**/Horiz_Arrow_UP'), gui.find('**/Horiz_Arrow_DN'), gui.find('**/Horiz_Arrow_Rllvr'), gui.find('**/Horiz_Arrow_UP')), image3_color = Vec4(1, 1, 1, 0.5), image_scale = (-1.0, 1.0, 1.0), relief = None, text = TTLocalizer.PetTutorialPrev, text3_fg = Vec4(0, 0, 0, 0.5), text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (-0.20000000000000001, -0.29999999999999999, -0.25), command = self.requestPrev)
        self.bQuit = DirectButton(self, image = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')), relief = None, text = TTLocalizer.PetTutorialDone, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.55000000000000004, -0.29999999999999999, -0.25), command = self._PetTutorial__handleQuit)
        self.bQuit.hide()
        buttons.removeNode()
        gui.removeNode()
        self.request('Page1')

    
    def enterPage1(self, *args):
        self.title['text'] = (TTLocalizer.PetTutorialTitle1,)
        self['text'] = TTLocalizer.PetTutorialPage1
        self['text_pos'] = (0.14999999999999999, 0.13)
        self['text_wordwrap'] = 16.5
        self.bPrev['state'] = DISABLED
        self.iPage1.show()

    
    def exitPage1(self, *args):
        self.bPrev['state'] = NORMAL
        self.iPage1.hide()

    
    def enterPage2(self, *args):
        self.title['text'] = (TTLocalizer.PetTutorialTitle2,)
        self['text'] = TTLocalizer.PetTutorialPage2
        self['text_pos'] = (-0.27000000000000002, 0.16)
        self['text_wordwrap'] = 13.5
        self.iPage2.show()

    
    def exitPage2(self, *args):
        self.iPage2.hide()

    
    def enterPage3(self, *args):
        self.title['text'] = (TTLocalizer.PetTutorialTitle3,)
        self['text'] = TTLocalizer.PetTutorialPage3
        self['text_pos'] = (0.14999999999999999, 0.13)
        self['text_wordwrap'] = 16.5
        self.bQuit.show()
        self.bNext['state'] = DISABLED
        self.iPage3.show()

    
    def exitPage3(self, *args):
        self.bNext['state'] = NORMAL
        self.iPage3.hide()
        self.bQuit.hide()

    
    def _PetTutorial__handleQuit(self):
        base.localAvatar.b_setPetTutorialDone(True)
        messenger.send(self.doneEvent)


