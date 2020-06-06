# File: W (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from ToontownMsgTypes import *
from DirectGui import *
from TaskManagerGlobal import *
import OnscreenText
import StateData
import ToontownDialog
import FSM
import State
import DirectNotifyGlobal
import Task
import Localizer
import GuiScreen

class WelcomeScreen(StateData.StateData, GuiScreen.GuiScreen):
    notify = DirectNotifyGlobal.directNotify.newCategory('WelcomeScreen')
    
    def __init__(self, tcr, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        GuiScreen.GuiScreen.__init__(self)
        self.tcr = tcr
        self.fsm = FSM.FSM('WelcomeScreen', [
            State.State('off', self.enterOff, self.exitOff, [
                'display']),
            State.State('display', self.enterDisplay, self.exitDisplay, [])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def load(self):
        masterScale = 0.80000000000000004
        textScale = 0.10000000000000001 * masterScale
        entryScale = 0.080000000000000002 * masterScale
        lineHeight = 0.20999999999999999 * masterScale
        buttonScale = 1.3799999999999999 * masterScale
        buttonLineHeight = 0.17000000000000001 * masterScale
        self.screen = loader.loadModel('phase_3/models/gui/login-background').find('**/welcome')
        self.screen.hide()
        self.screen.reparentTo(aspect2d)
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.welcomeLabel = DirectLabel(parent = self.screen, relief = None, pos = (0, 0, -0.059999999999999998), text = Localizer.WelcomeScreenHeading, text_font = getMinnieFont(), text_scale = 0.16, text_fg = Vec4(0.59999999999999998, 0.10000000000000001, 0.10000000000000001, 1))
        self.sentence1Label = DirectLabel(parent = self.screen, relief = None, pos = (0, 0, -0.19), text = Localizer.WelcomeScreenSentence1, text_scale = 0.089999999999999997)
        self.toontownLabel = DirectLabel(parent = self.screen, relief = None, pos = (0, 0, -0.32000000000000001), text = Localizer.WelcomeScreenToontown, text_font = getMinnieFont(), text_scale = 0.089999999999999997, text_fg = Vec4(0.80000000000000004, 0.10000000000000001, 0.10000000000000001, 1))
        self.upsellLabel = DirectLabel(parent = self.screen, relief = None, pos = (0, 0, -0.44), scale = 0.34999999999999998, text = Localizer.WelcomeScreenSentence2, text_scale = 0.17000000000000001, text_fg = (0, 0, 0, 1), text_wordwrap = 20)
        self.okButton = DirectButton(parent = self.screen, relief = None, pos = (0, 0, -0.62), scale = buttonScale, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), text = Localizer.WelcomeScreenOk, text_scale = 0.059999999999999998, text_pos = (0, -0.02), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), command = self._WelcomeScreen__handleOkButton)
        guiButton.removeNode()

    
    def unload(self):
        self.screen.removeNode()
        self.welcomeLabel.destroy()
        self.sentence1Label.destroy()
        self.toontownLabel.destroy()
        self.upsellLabel.destroy()
        self.okButton.destroy()
        del self.screen
        del self.fsm

    
    def enter(self):
        self.fsm.request('display')

    
    def exit(self):
        self.fsm.requestFinalState()

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterDisplay(self):
        self.screen.show()

    
    def exitDisplay(self):
        self.screen.hide()

    
    def _WelcomeScreen__handleOkButton(self):
        messenger.send(self.doneEvent, [
            {
                'mode': 'ok' }])

    
    def _WelcomeScreen__handleQuitButton(self):
        messenger.send(self.doneEvent, [
            {
                'mode': 'quit' }])


