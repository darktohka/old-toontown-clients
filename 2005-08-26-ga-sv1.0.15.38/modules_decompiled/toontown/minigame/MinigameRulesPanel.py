# File: M (Python 2.2)

from pandac.PandaModules import *
from direct.task import Task
from direct.fsm import StateData
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownTimer
from toontown.toonbase import TTLocalizer
import MinigameGlobals

class MinigameRulesPanel(StateData.StateData):
    TIMEOUT = MinigameGlobals.rulesDuration
    
    def __init__(self, panelName, gameTitle, instructions, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.gameTitle = gameTitle
        self.instructions = instructions

    
    def load(self):
        minigameGui = loader.loadModel('phase_4/models/gui/minigame_rules_gui')
        buttonGui = loader.loadModelOnce('phase_3.5/models/gui/inventory_gui')
        self.frame = DirectFrame(image = minigameGui.find('**/minigame-rules-panel'), relief = None, pos = (0.13750000000000001, 0, -0.66669999999999996))
        self.gameTitleText = DirectLabel(parent = self.frame, text = self.gameTitle, scale = 0.11, text_font = getSignFont(), text_fg = (1.0, 0.33000000000000002, 0.33000000000000002, 1.0), pos = (-0.045999999999999999, 0.20000000000000001, 0.091999999999999998), relief = None)
        self.instructionsText = DirectLabel(parent = self.frame, text = self.instructions, scale = 0.070000000000000007, text_align = TextNode.ALeft, text_wordwrap = 26.5, pos = (-1.05, 0.050000000000000003, 0), relief = None)
        self.playButton = DirectButton(parent = self.frame, relief = None, image = (buttonGui.find('**/InventoryButtonUp'), buttonGui.find('**/InventoryButtonDown'), buttonGui.find('**/InventoryButtonRollover')), image_color = Vec4(0, 0.90000000000000002, 0.10000000000000001, 1), text = TTLocalizer.MinigameRulesPanelPlay, text_fg = (1, 1, 1, 1), text_pos = (0, -0.02, 0), text_scale = 0.055, pos = (1.0024999999999999, 0, -0.20300000000000001), scale = 1.05, command = self.playCallback)
        minigameGui.removeNode()
        buttonGui.removeNode()
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(self.frame)
        self.timer.setScale(0.40000000000000002)
        self.timer.setPos(0.997, 0, 0.064000000000000001)
        self.frame.hide()

    
    def unload(self):
        self.frame.destroy()
        del self.frame
        del self.gameTitleText
        del self.instructionsText
        del self.playButton
        del self.timer

    
    def enter(self):
        self.frame.show()
        self.timer.countdown(self.TIMEOUT, self.playCallback)
        self.accept('enter', self.playCallback)

    
    def exit(self):
        self.frame.hide()
        self.timer.stop()
        self.ignore('enter')

    
    def playCallback(self):
        messenger.send(self.doneEvent)


