# File: N (Python 2.2)

from ShowBaseGlobal import *
from ToontownGlobals import *
from ToontownMsgTypes import *
from DirectGui import *
import OnscreenText
import StateData
import FSM
import State
import DirectNotifyGlobal
import Localizer
import GuiScreen
import ToontownDialog

class NewPlayerScreen(StateData.StateData, GuiScreen.GuiScreen):
    notify = DirectNotifyGlobal.directNotify.newCategory('NewPlayerScreen')
    
    def __init__(self, tcr, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        GuiScreen.GuiScreen.__init__(self)
        self.tcr = tcr
        self.allowNewAccounts = tcr.accountServerConstants.getBool('allowNewAccounts')
        self.fsm = FSM.FSM('NewPlayerScreen', [
            State.State('off', self.enterOff, self.exitOff, [
                'display']),
            State.State('display', self.enterDisplay, self.exitDisplay, [
                'off'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def load(self):
        masterScale = 1.5
        textScale = 0.10000000000000001 * masterScale
        entryScale = 0.080000000000000002 * masterScale
        lineHeight = 0.20999999999999999 * masterScale
        buttonScale = 1.1499999999999999 * masterScale
        buttonLineHeight = 0.14000000000000001 * masterScale
        background = loader.loadModel('phase_3/models/gui/login-background')
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.frame = DirectFrame(parent = aspect2d, relief = None, image = background.find('**/first_time_install'))
        self.frame.hide()
        linePos = -0.29999999999999999
        if self.allowNewAccounts:
            image_color = Vec4(1, 1, 1, 1)
            imageSet = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
        else:
            g = 0.5
            image_color = Vec4(g, g, g, 1)
            imageSet = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_UP'))
        self.newAccountButton = DirectButton(parent = self.frame, relief = None, pos = (0, 0, linePos), scale = buttonScale, image = imageSet, image_color = image_color, text = Localizer.NewPlayerScreenNewAccount, text_scale = 0.059999999999999998, text_pos = (0, -0.02), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), command = self._NewPlayerScreen__handleNewAccountButton)
        linePos -= buttonLineHeight
        self.loginButton = DirectButton(parent = self.frame, relief = None, pos = (0, 0, linePos), scale = buttonScale, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), text = Localizer.NewPlayerScreenLogin, text_scale = 0.059999999999999998, text_pos = (0, -0.02), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), command = self._NewPlayerScreen__handleLoginButton)
        linePos -= buttonLineHeight
        self.quitButton = DirectButton(parent = self.frame, relief = None, pos = (0, 0, linePos), scale = buttonScale, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), text = Localizer.NewPlayerScreenQuit, text_scale = 0.059999999999999998, text_pos = (0, -0.02), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), command = self._NewPlayerScreen__handleQuitButton)
        linePos -= buttonLineHeight
        self.dialogDoneEvent = 'newPlayerDialogAck'
        self.dialog = ToontownDialog.GlobalDialog(doneEvent = self.dialogDoneEvent, message = '', style = ToontownDialog.Acknowledge)
        self.dialog.hide()
        background.removeNode()
        guiButton.removeNode()

    
    def unload(self):
        self.dialog.cleanup()
        del self.dialog
        self.frame.destroy()
        del self.frame
        del self.fsm

    
    def enter(self):
        self.fsm.request('display')

    
    def exit(self):
        self.ignore(self.dialogDoneEvent)
        self.fsm.requestFinalState()

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterDisplay(self):
        self.frame.show()

    
    def exitDisplay(self):
        self.frame.hide()

    
    def _NewPlayerScreen__handleNewAccountButton(self):
        if self.allowNewAccounts:
            messenger.send(self.doneEvent, [
                {
                    'mode': 'newAccount' }])
            return None
        
        self.dialog.setMessage(Localizer.LoginScreenNoNewAccounts)
        self.dialog.show()
        self.acceptOnce(self.dialogDoneEvent, self._NewPlayerScreen__handleNoNewAccountsAck)

    
    def _NewPlayerScreen__handleLoginButton(self):
        messenger.send(self.doneEvent, [
            {
                'mode': 'login' }])

    
    def _NewPlayerScreen__handleQuitButton(self):
        messenger.send(self.doneEvent, [
            {
                'mode': 'quit' }])

    
    def _NewPlayerScreen__handleNoNewAccountsAck(self):
        self.dialog.hide()


