# File: P (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from direct.showbase import PandaObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer
from toontown.pets import PetTricks
from otp.otpbase import OTPLocalizer
from direct.showbase.PythonUtil import lerp
FUDGE_FACTOR = 0.01

class PetDetailPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('PetDetailPanel')
    
    def __init__(self, pet, closeCallback, parent = aspect2d, **kw):
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        gui = loader.loadModelOnce('phase_3.5/models/gui/avatar_panel_gui')
        detailPanel = gui.find('**/PetBattlePannel2')
        optiondefs = (('pos', (-4.5199999999999996, 0.0, 3.0499999999999998), None), ('scale', 3.5800000000000001, None), ('relief', None, None), ('image', detailPanel, None), ('image_color', GlobalDialogColor, None), ('text', TTLocalizer.PetDetailPanelTitle, None), ('text_wordwrap', 10.4, None), ('text_scale', 0.13200000000000001, None), ('text_pos', (-0.20000000000000001, 0.61250000000000004), None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.dataText = DirectLabel(self, text = '', text_scale = 0.089999999999999997, text_align = TextNode.ALeft, text_wordwrap = 15, relief = None, pos = (-0.69999999999999996, 0.0, 0.55000000000000004))
        self.bCancel = DirectButton(self, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), relief = None, text = TTLocalizer.AvatarDetailPanelCancel, text_scale = 0.050000000000000003, text_pos = (0.12, -0.01), pos = (-0.88, 0.0, -0.68000000000000005), scale = 2.0, command = closeCallback)
        self.initialiseoptions(PetDetailPanel)
        self.labels = { }
        self.bars = { }
        self.update(pet)
        buttons.removeNode()
        gui.removeNode()

    
    def cleanup(self):
        del self.labels
        del self.bars
        self.destroy()

    
    def update(self, pet):
        if not pet:
            return None
        
        for trickId in PetTricks.TrickId2scIds.keys():
            trickText = TTLocalizer.PetTrickStrings[trickId]
            if trickId < len(pet.trickAptitudes):
                aptitude = pet.trickAptitudes[trickId]
                bar = self.bars.get(trickId)
                label = self.bars.get(trickId)
                if aptitude != 0:
                    healRange = PetTricks.TrickHeals[trickId]
                    hp = lerp(healRange[0], healRange[1], aptitude)
                    if hp == healRange[1]:
                        hp = healRange[1]
                        length = 1
                        barColor = (0.69999999999999996, 0.80000000000000004, 0.5, 1)
                    else:
                        (hp, length) = divmod(hp, 1)
                        barColor = (0.90000000000000002, 1, 0.69999999999999996, 1)
                    if not label:
                        self.labels[trickId] = DirectLabel(parent = self, relief = None, pos = (0, 0, 0.42999999999999999 - trickId * 0.155), scale = 0.69999999999999996, text = trickText, text_scale = 0.17000000000000001, text_fg = (0.050000000000000003, 0.14000000000000001, 0.40000000000000002, 1), text_align = TextNode.ALeft, text_pos = (-1.3999999999999999, -0.050000000000000003))
                    else:
                        label['text'] = trickText
                    if not bar:
                        self.bars[trickId] = DirectWaitBar(parent = self, pos = (0, 0, 0.42999999999999999 - trickId * 0.155), relief = SUNKEN, frameSize = (-0.5, 0.90000000000000002, -0.10000000000000001, 0.10000000000000001), borderWidth = (0.025000000000000001, 0.025000000000000001), scale = 0.69999999999999996, frameColor = (0.40000000000000002, 0.59999999999999998, 0.40000000000000002, 1), barColor = barColor, range = 1.0 + FUDGE_FACTOR, value = length + FUDGE_FACTOR, text = str(int(hp)) + ' ' + TTLocalizer.Laff, text_scale = 0.17000000000000001, text_fg = (0.050000000000000003, 0.14000000000000001, 0.40000000000000002, 1), text_align = TextNode.ALeft, text_pos = (0.0, -0.050000000000000003))
                    else:
                        bar['value'] = length + FUDGE_FACTOR
                        bar['text'] = (str(int(hp)) + ' ' + TTLocalizer.Laff,)
                
            
        


