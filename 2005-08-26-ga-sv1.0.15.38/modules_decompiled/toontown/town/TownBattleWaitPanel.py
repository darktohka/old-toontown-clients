# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.fsm import StateData
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer

class TownBattleWaitPanel(StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)

    
    def load(self):
        gui = loader.loadModelOnce('phase_3.5/models/gui/battle_gui')
        self.frame = DirectFrame(relief = None, image = gui.find('**/Waiting4Others'), text_align = TextNode.ALeft, pos = (0, 0, 0), scale = 0.65000000000000002)
        self.frame.hide()
        self.backButton = DirectButton(parent = self.frame, relief = None, image = (gui.find('**/PckMn_BackBtn'), gui.find('**/PckMn_BackBtn_Dn'), gui.find('**/PckMn_BackBtn_Rlvr')), pos = (-0.64700000000000002, 0, -0.010999999999999999), scale = 1.05, text = TTLocalizer.TownBattleWaitBack, text_scale = 0.050000000000000003, text_pos = (0.01, -0.012), text_fg = Vec4(0, 0, 0.80000000000000004, 1), command = self._TownBattleWaitPanel__handleBack)
        gui.removeNode()

    
    def unload(self):
        self.frame.destroy()
        del self.frame
        del self.backButton

    
    def enter(self, numParticipants):
        if numParticipants > 1:
            self.frame['text'] = TTLocalizer.TownBattleWaitTitle
            self.frame['text_pos'] = (0, 0.01, 0)
            self.frame['text_scale'] = 0.10000000000000001
        else:
            self.frame['text'] = TTLocalizer.TownSoloBattleWaitTitle
            self.frame['text_pos'] = (0, -0.050000000000000003, 0)
            self.frame['text_scale'] = 0.13
        self.frame.show()

    
    def exit(self):
        self.frame.hide()

    
    def _TownBattleWaitPanel__handleBack(self):
        doneStatus = {
            'mode': 'Back' }
        messenger.send(self.doneEvent, [
            doneStatus])


