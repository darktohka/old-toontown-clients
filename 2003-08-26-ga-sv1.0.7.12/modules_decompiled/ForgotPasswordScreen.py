# File: F (Python 2.2)

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
import TTAccount
import GuiScreen
import InputCheck

class ForgotPasswordScreen(StateData.StateData, GuiScreen.GuiScreen):
    notify = DirectNotifyGlobal.directNotify.newCategory('ForgotPasswordScreen')
    ActiveEntryColor = Vec4(1, 1, 1, 1)
    InactiveEntryColor = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
    
    def __init__(self, tcr, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        GuiScreen.GuiScreen.__init__(self)
        self.tcr = tcr
        self.loginInterface = self.tcr.loginInterface
        self.fsm = FSM.FSM('ForgotPasswordScreen', [
            State.State('off', self.enterOff, self.exitOff, [
                'getInput']),
            State.State('getInput', self.enterGetInput, self.exitGetInput, [
                'sendInfo']),
            State.State('sendInfo', self.enterSendInfo, self.exitSendInfo, [
                'getInput'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def load(self):
        masterScale = 0.80000000000000004
        textScale = 0.10000000000000001 * masterScale
        entryScale = 0.080000000000000002 * masterScale
        lineHeight = 0.20999999999999999 * masterScale
        buttonScale = 1.1499999999999999 * masterScale
        buttonLineHeight = 0.14000000000000001 * masterScale
        background = loader.loadModel('phase_3/models/gui/login-background')
        nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.frame = DirectFrame(parent = aspect2d, relief = FLAT, image = background.find('**/background_only'))
        self.frame.hide()
        linePos = 0.59999999999999998
        self.titleLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, linePos), text = Localizer.ForgotPasswordScreenTitle, text_scale = textScale, text_fg = (1, 1, 0, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        linePos -= lineHeight
        self.instructionsLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, linePos), text = Localizer.ForgotPasswordScreenInstructions, text_scale = textScale, text_fg = (1, 1, 0, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        linePos -= lineHeight
        linePos -= lineHeight / 2.0
        self.acctNameEntryLabel = DirectLabel(parent = self.frame, relief = None, pos = (-0.20999999999999999, 0, linePos), text = Localizer.ForgotPasswordScreenAcctNameEntryLabel, text_scale = textScale, text_align = TextNode.ARight, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        self.acctNameEntry = DirectEntry(parent = self.frame, relief = None, image = nameBalloon, image1_color = self.InactiveEntryColor, scale = entryScale, pos = (-0.125, 0.0, linePos), width = maxLoginWidth, numLines = 1, focus = 0, cursorKeys = 1, command = self._ForgotPasswordScreen__handleAcctNameEntry)
        linePos -= lineHeight
        self.orLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, linePos), text = Localizer.ForgotPasswordScreenOr, text_scale = textScale, text_fg = (1, 1, 0, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        linePos -= lineHeight
        self.emailLabel = DirectLabel(parent = self.frame, relief = None, pos = (-0.49625399999999997, 0, linePos), text = Localizer.ForgotPasswordScreenEmailEntryLabel, text_scale = textScale, text_align = TextNode.ARight, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_shadowOffset = (0.080000000000000002, 0.080000000000000002))
        self.emailEntry = DirectEntry(parent = self.frame, relief = None, image = nameBalloon, image1_color = self.InactiveEntryColor, image_scale = (2.1000000000000001, 1, 1), image_pos = (0.59999999999999998, 0, 0), scale = entryScale, pos = (-0.41125400000000001, 0.0, linePos), width = self.ENTRY_WIDTH, numLines = 1, focus = 0, cursorKeys = 1, command = self._ForgotPasswordScreen__handleEmailEntry)
        linePos -= lineHeight
        self.submitButton = DirectButton(parent = self.frame, relief = None, pos = (0, 0, linePos), scale = buttonScale, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), text = Localizer.ForgotPasswordScreenSubmit, text_scale = 0.059999999999999998, text_pos = (0, -0.02), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), command = self._ForgotPasswordScreen__handleSubmit)
        linePos -= buttonLineHeight
        self.cancelButton = DirectButton(parent = self.frame, relief = None, pos = (0, 0, linePos), scale = buttonScale, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1.3, 1.1000000000000001, 1.1000000000000001), image0_color = Vec4(1, 0.10000000000000001, 0.10000000000000001, 1), image1_color = Vec4(1, 0.10000000000000001, 0.10000000000000001, 1), image2_color = Vec4(1, 1, 1, 1), text = Localizer.ForgotPasswordScreenCancel, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._ForgotPasswordScreen__handleCancel)
        linePos -= buttonLineHeight
        self.dialogDoneEvent = 'ForgotPasswordDialogAck'
        self.dialog = ToontownDialog.GlobalDialog(doneEvent = self.dialogDoneEvent, message = '', style = ToontownDialog.Acknowledge)
        self.dialog.hide()
        background.removeNode()
        guiButton.removeNode()
        nameBalloon.removeNode()

    
    def unload(self):
        if self.dialog != None:
            self.dialog.cleanup()
            self.dialog = None
        
        self.frame.destroy()
        del self.fsm

    
    def enter(self):
        self.firstTime = 1
        self.frame.show()
        self.fsm.request('getInput')

    
    def exit(self):
        self.ignore(self.dialogDoneEvent)
        self.frame.hide()
        self.fsm.requestFinalState()

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterGetInput(self):
        self.notify.debug('enterGetInput')
        if self.firstTime:
            self.emailEntry.set('')
            self.acctNameEntry.set('')
        
        self.firstTime = 0
        self.focusList = [
            self.acctNameEntry,
            self.emailEntry]
        self.startFocusMgmt(enterPressBehavior = GuiScreen.GuiScreen.ENTERPRESS_REMOVE_FOCUS)
        if hasattr(self, 'lastFocusIndex'):
            self.setFocus(self.lastFocusIndex)
            del self.lastFocusIndex
        

    
    def exitGetInput(self):
        self.lastFocusIndex = self.getFocusIndex()
        self.stopFocusMgmt()

    
    def _ForgotPasswordScreen__handleEmailEntry(self, text):
        self.notify.debug('__handleEmailEntry')
        self._ForgotPasswordScreen__handleSubmit()

    
    def _ForgotPasswordScreen__handleAcctNameEntry(self, text):
        self.notify.debug('__handleAcctNameEntry')
        self._ForgotPasswordScreen__handleSubmit()

    
    def _ForgotPasswordScreen__handleSubmit(self):
        self.notify.debug('__handleSubmit')
        self.fsm.request('sendInfo')

    
    def enterSendInfo(self):
        self.notify.debug('enterSendInfo')
        focusItem = self.focusList[self.lastFocusIndex]
        self.removeFocus()
        if focusItem == self.acctNameEntry:
            isEmail = 0
            text = self.acctNameEntry.get()
        else:
            isEmail = 1
            text = self.emailEntry.get()
        if InputCheck.isBlank(text):
            self.fsm.request('getInput')
            return None
        
        if isEmail:
            if not InputCheck.isValidEmailAddr(text):
                self.dialog.setMessage(Localizer.ForgotPasswordScreenInvalidEmail)
                self.dialog.show()
                self.acceptOnce(self.dialogDoneEvent, self._ForgotPasswordScreen__handleFailureAck)
                return None
            
        
        
        try:
            if isEmail:
                error = self.loginInterface.requestPwdReminder(email = text)
                if error is None:
                    self.dialog.setMessage(Localizer.ForgotPasswordScreenEmailSuccess % text)
                    self.dialog.show()
                    self.acceptOnce(self.dialogDoneEvent, self._ForgotPasswordScreen__handleSuccessAck)
                else:
                    self.dialog.setMessage(Localizer.ForgotPasswordScreenEmailFailure % text)
                    self.dialog.show()
                    self.acceptOnce(self.dialogDoneEvent, self._ForgotPasswordScreen__handleFailureAck)
            else:
                error = self.loginInterface.requestPwdReminder(acctName = text)
                if error is None:
                    self.dialog.setMessage(Localizer.ForgotPasswordScreenAccountNameSuccess)
                    self.dialog.show()
                    self.acceptOnce(self.dialogDoneEvent, self._ForgotPasswordScreen__handleSuccessAck)
                elif self.loginInterface.getErrorCode() == 105:
                    self.dialog.setMessage(Localizer.ForgotPasswordScreenNoEmailAddress)
                    self.dialog.show()
                    self.acceptOnce(self.dialogDoneEvent, self._ForgotPasswordScreen__handleNoEmailAck)
                else:
                    self.dialog.setMessage(Localizer.ForgotPasswordScreenAccountNameFailure % text)
                    self.dialog.show()
                    self.acceptOnce(self.dialogDoneEvent, self._ForgotPasswordScreen__handleFailureAck)
        except TTAccount.TTAccountException:
            e = None
            self.notify.debug(str(e))
            self.dialog.setMessage(str(e))
            self.dialog.show()
            self.acceptOnce(self.dialogDoneEvent, self._ForgotPasswordScreen__handleConnectionProblemAck)
        


    
    def exitSendInfo(self):
        pass

    
    def _ForgotPasswordScreen__handleSuccessAck(self):
        self.dialog.hide()
        messenger.send(self.doneEvent, [
            {
                'mode': 'success' }])

    
    def _ForgotPasswordScreen__handleFailureAck(self):
        self.dialog.hide()
        self.fsm.request('getInput')

    
    def _ForgotPasswordScreen__handleConnectionProblemAck(self):
        self.dialog.hide()
        messenger.send(self.doneEvent, [
            {
                'mode': 'fail' }])

    
    def _ForgotPasswordScreen__handleCancel(self):
        self.dialog.hide()
        messenger.send(self.doneEvent, [
            {
                'mode': 'cancel' }])

    
    def _ForgotPasswordScreen__handleNoEmailAck(self):
        self.dialog.hide()
        messenger.send(self.doneEvent, [
            {
                'mode': 'cancel' }])


