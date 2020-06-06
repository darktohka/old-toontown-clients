# File: L (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.distributed.MsgTypes import *
from direct.gui.DirectGui import *
from direct.fsm import StateData
from otp.otpgui import OTPDialog
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from otp.otpbase import OTPLocalizer
import TTAccount
import GuiScreen
import time
from otp.otpbase import OTPGlobals
import os

class LoginScreen(StateData.StateData, GuiScreen.GuiScreen):
    AutoLoginName = base.config.GetString('%s-auto-login%s' % (game.name, os.getenv('otp_client', '')), '')
    AutoLoginPassword = base.config.GetString('%s-auto-password%s' % (game.name, os.getenv('otp_client', '')), '')
    notify = DirectNotifyGlobal.directNotify.newCategory('LoginScreen')
    ActiveEntryColor = Vec4(1, 1, 1, 1)
    InactiveEntryColor = Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1)
    
    def __init__(self, cr, doneEvent):
        self.notify.debug('__init__')
        StateData.StateData.__init__(self, doneEvent)
        GuiScreen.GuiScreen.__init__(self)
        self.cr = cr
        self.loginInterface = self.cr.loginInterface
        self.userName = ''
        self.password = ''
        self.fsm = ClassicFSM.ClassicFSM('LoginScreen', [
            State.State('off', self.enterOff, self.exitOff, [
                'login',
                'waitForLoginResponse']),
            State.State('login', self.enterLogin, self.exitLogin, [
                'waitForLoginResponse',
                'login',
                'showLoginFailDialog']),
            State.State('showLoginFailDialog', self.enterShowLoginFailDialog, self.exitShowLoginFailDialog, [
                'login',
                'showLoginFailDialog']),
            State.State('waitForLoginResponse', self.enterWaitForLoginResponse, self.exitWaitForLoginResponse, [
                'login',
                'showLoginFailDialog',
                'showConnectionProblemDialog']),
            State.State('showConnectionProblemDialog', self.enterShowConnectionProblemDialog, self.exitShowConnectionProblemDialog, [
                'login'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def load(self):
        self.notify.debug('load')
        masterScale = 0.80000000000000004
        textScale = 0.10000000000000001 * masterScale
        entryScale = 0.080000000000000002 * masterScale
        lineHeight = 0.20999999999999999 * masterScale
        buttonScale = 1.1499999999999999 * masterScale
        buttonLineHeight = 0.14000000000000001 * masterScale
        self.frame = DirectFrame(parent = aspect2d, relief = None, sortOrder = 20)
        self.frame.hide()
        linePos = -0.26000000000000001
        self.nameLabel = DirectLabel(parent = self.frame, relief = None, pos = (-0.20999999999999999, 0, linePos), text = OTPLocalizer.LoginScreenUserName, text_scale = textScale, text_align = TextNode.ARight)
        self.nameEntry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.01, 0.01), scale = entryScale, pos = (-0.125, 0.0, linePos), width = OTPGlobals.maxLoginWidth, numLines = 1, focus = 0, cursorKeys = 1)
        linePos -= lineHeight
        self.passwordLabel = DirectLabel(parent = self.frame, relief = None, pos = (-0.20999999999999999, 0, linePos), text = OTPLocalizer.LoginScreenPassword, text_scale = textScale, text_align = TextNode.ARight)
        self.passwordEntry = DirectEntry(parent = self.frame, relief = SUNKEN, borderWidth = (0.01, 0.01), scale = entryScale, pos = (-0.125, 0.0, linePos), width = OTPGlobals.maxLoginWidth, numLines = 1, focus = 0, cursorKeys = 1, obscured = 1, command = self._LoginScreen__handleLoginPassword)
        linePos -= lineHeight
        buttonImageScale = (1.7, 1.1000000000000001, 1.1000000000000001)
        self.loginButton = DirectButton(parent = self.frame, relief = RAISED, borderWidth = (0.01, 0.01), pos = (0, 0, linePos), scale = buttonScale, text = OTPLocalizer.LoginScreenLogin, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._LoginScreen__handleLoginButton)
        linePos -= buttonLineHeight
        self.createAccountButton = DirectButton(parent = self.frame, relief = RAISED, borderWidth = (0.01, 0.01), pos = (0, 0, linePos), scale = buttonScale, text = OTPLocalizer.LoginScreenCreateAccount, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._LoginScreen__handleCreateAccount)
        linePos -= buttonLineHeight
        self.quitButton = DirectButton(parent = self.frame, relief = RAISED, borderWidth = (0.01, 0.01), pos = (0, 0, linePos), scale = buttonScale, text = OTPLocalizer.LoginScreenQuit, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._LoginScreen__handleQuit)
        linePos -= buttonLineHeight
        self.dialogDoneEvent = 'loginDialogAck'
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.dialog = dialogClass(dialogName = 'loginDialog', doneEvent = self.dialogDoneEvent, message = '', style = OTPDialog.Acknowledge, sortOrder = NO_FADE_SORT_INDEX + 100)
        self.dialog.hide()
        self.failDialog = DirectFrame(relief = RAISED, borderWidth = (0.01, 0.01), pos = (0, 0.10000000000000001, 0), text = '', text_scale = 0.080000000000000002, text_pos = (0.0, 0.29999999999999999), text_wordwrap = 15, sortOrder = NO_FADE_SORT_INDEX)
        linePos = -0.050000000000000003
        self.failTryAgainButton = DirectButton(parent = self.failDialog, relief = RAISED, borderWidth = (0.01, 0.01), pos = (0, 0, linePos), scale = 0.90000000000000002, text = OTPLocalizer.LoginScreenTryAgain, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._LoginScreen__handleFailTryAgain)
        linePos -= buttonLineHeight
        self.failCreateAccountButton = DirectButton(parent = self.failDialog, relief = RAISED, borderWidth = (0.01, 0.01), pos = (0, 0, linePos), scale = 0.90000000000000002, text = OTPLocalizer.LoginScreenCreateAccount, text_scale = 0.059999999999999998, text_pos = (0, -0.02), command = self._LoginScreen__handleFailCreateAccount)
        linePos -= buttonLineHeight
        self.failDialog.hide()
        self.connectionProblemDialogDoneEvent = 'loginConnectionProblemDlgAck'
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.connectionProblemDialog = dialogClass(dialogName = 'connectionProblemDialog', doneEvent = self.connectionProblemDialogDoneEvent, message = '', style = OTPDialog.Acknowledge, sortOrder = NO_FADE_SORT_INDEX + 100)
        self.connectionProblemDialog.hide()

    
    def unload(self):
        self.notify.debug('unload')
        self.dialog.cleanup()
        del self.dialog
        self.failDialog.destroy()
        del self.failDialog
        self.connectionProblemDialog.cleanup()
        del self.connectionProblemDialog
        self.frame.destroy()
        del self.fsm
        del self.loginInterface
        del self.cr

    
    def enter(self):
        if self.cr.blue:
            self.userName = 'blue'
            self.password = self.cr.blue
            self.fsm.request('waitForLoginResponse')
        elif self.cr.playToken:
            self.userName = '*'
            self.password = self.cr.playToken
            self.fsm.request('waitForLoginResponse')
        elif self.AutoLoginName:
            self.userName = self.AutoLoginName
            self.password = self.AutoLoginPassword
            self.fsm.request('waitForLoginResponse')
        else:
            self.fsm.request('login')

    
    def exit(self):
        self.frame.hide()
        self.ignore(self.dialogDoneEvent)
        self.fsm.requestFinalState()

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterLogin(self):
        self.cr.resetPeriodTimer(None)
        self.userName = ''
        self.password = ''
        if launcher:
            self.userName = launcher.getLastLogin()
        
        if self.userName and self.nameEntry.get():
            if self.userName != self.nameEntry.get():
                self.userName = ''
            
        
        self.frame.show()
        self.nameEntry.enterText(self.userName)
        self.passwordEntry.enterText(self.password)
        self.focusList = [
            self.nameEntry,
            self.passwordEntry]
        focusIndex = 0
        if self.userName:
            focusIndex = 1
        
        self.startFocusMgmt(startFocus = focusIndex)

    
    def exitLogin(self):
        self.stopFocusMgmt()

    
    def enterShowLoginFailDialog(self, msg):
        base.transitions.fadeScreen(0.5)
        self.failDialog['text'] = msg
        self.failDialog.show()

    
    def _LoginScreen__handleFailTryAgain(self):
        self.fsm.request('login')

    
    def _LoginScreen__handleFailCreateAccount(self):
        messenger.send(self.doneEvent, [
            {
                'mode': 'createAccount' }])

    
    def _LoginScreen__handleFailNoNewAccountsAck(self):
        self.dialog.hide()
        self.fsm.request('showLoginFailDialog', [
            self.failDialog['text']])

    
    def exitShowLoginFailDialog(self):
        base.transitions.noTransitions()
        self.failDialog.hide()

    
    def _LoginScreen__handleLoginPassword(self, password):
        if password != '':
            if self.nameEntry.get() != '':
                self._LoginScreen__handleLoginButton()
            
        

    
    def _LoginScreen__handleLoginButton(self):
        self.removeFocus()
        self.userName = self.nameEntry.get()
        self.password = self.passwordEntry.get()
        if self.userName == '':
            self.dialog.setMessage(OTPLocalizer.LoginScreenLoginPrompt)
            self.dialog.show()
            self.acceptOnce(self.dialogDoneEvent, self._LoginScreen__handleEnterLoginAck)
        else:
            self.fsm.request('waitForLoginResponse')

    
    def _LoginScreen__handleQuit(self):
        self.removeFocus()
        messenger.send(self.doneEvent, [
            {
                'mode': 'quit' }])

    
    def _LoginScreen__handleCreateAccount(self):
        self.removeFocus()
        messenger.send(self.doneEvent, [
            {
                'mode': 'createAccount' }])

    
    def enterWaitForLoginResponse(self):
        self.cr.handler = self.handleWaitForLoginResponse
        self.cr.userName = self.userName
        self.cr.password = self.password
        
        try:
            error = self.loginInterface.authorize(self.userName, self.password)
        except TTAccount.TTAccountException:
            e = None
            self.fsm.request('showConnectionProblemDialog', [
                str(e)])
            return None

        if error:
            self.notify.info(error)
            freeTimeExpired = self.loginInterface.getErrorCode() == 10
            if freeTimeExpired:
                self.cr.logAccountInfo()
                messenger.send(self.doneEvent, [
                    {
                        'mode': 'freeTimeExpired' }])
            else:
                self.fsm.request('showLoginFailDialog', [
                    error])
        else:
            self.loginInterface.sendLoginMsg()
            self.waitForDatabaseTimeout(requestName = 'WaitForLoginResponse')

    
    def exitWaitForLoginResponse(self):
        self.cleanupWaitingForDatabase()
        self.cr.handler = None

    
    def enterShowConnectionProblemDialog(self, msg):
        self.connectionProblemDialog.setMessage(msg)
        self.connectionProblemDialog.show()
        self.acceptOnce(self.connectionProblemDialogDoneEvent, self._LoginScreen__handleConnectionProblemAck)

    
    def _LoginScreen__handleConnectionProblemAck(self):
        self.connectionProblemDialog.hide()
        self.fsm.request('login')

    
    def exitShowConnectionProblemDialog(self):
        pass

    
    def handleWaitForLoginResponse(self, msgType, di):
        if msgType == CLIENT_LOGIN_2_RESP:
            self.handleLoginResponseMsg2(di)
        elif msgType == CLIENT_LOGIN_RESP:
            self.handleLoginResponseMsg(di)
        elif msgType == CLIENT_SERVER_UP:
            self.cr.handleServerUp(di)
        elif msgType == CLIENT_SERVER_DOWN:
            self.cr.handleServerDown(di)
        else:
            self.cr.handleUnexpectedMsgType(msgType, di)

    
    def handleLoginResponseMsg2(self, di):
        now = time.time()
        returnCode = di.getUint8()
        errorString = di.getString()
        self.userName = di.getString()
        self.cr.userName = self.userName
        canChat = di.getUint8()
        self.cr.secretChatAllowed = canChat
        self.notify.info('Chat from game server login: %s' % canChat)
        sec = di.getUint32()
        usec = di.getUint32()
        serverTime = sec + usec / 1000000.0
        serverDelta = serverTime - now
        self.cr.setServerDelta(serverDelta)
        self.notify.setServerDelta(serverDelta, 28800)
        self.isPaid = di.getUint8()
        self.cr.setIsPaid(self.isPaid)
        if launcher and self.isPaid:
            launcher.setPaidUserLoggedIn()
        
        self.notify.info('Paid from game server login: %s' % self.isPaid)
        self.cr.resetPeriodTimer(None)
        if di.getRemainingSize() >= 4:
            minutesRemaining = di.getInt32()
            self.notify.info('Minutes remaining from server %s' % minutesRemaining)
            if self.isPaid:
                self.notify.info('Not spawning period timer for paid user')
            elif minutesRemaining >= 0:
                self.notify.info('Spawning period timer for unpaid user')
                self.cr.resetPeriodTimer(minutesRemaining * 60)
            else:
                self.notify.warning('Not paid, but also negative minutes remaining (?)')
        else:
            self.notify.info('Minutes remaining not returned from server; not spawning period timer')
        self.notify.info('Login response return code %s' % returnCode)
        if returnCode == 0:
            self._LoginScreen__handleLoginSuccess()
        elif returnCode == -13:
            self.notify.info('Period Time Expired')
            self.fsm.request('showLoginFailDialog', [
                OTPLocalizer.LoginScreenPeriodTimeExpired])
        else:
            self.notify.info('Login failed: %s' % errorString)
            messenger.send(self.doneEvent, [
                {
                    'mode': 'reject' }])

    
    def handleLoginResponseMsg(self, di):
        now = time.time()
        returnCode = di.getUint8()
        accountCode = di.getUint32()
        errorString = di.getString()
        sec = di.getUint32()
        usec = di.getUint32()
        serverTime = sec + usec / 1000000.0
        serverDelta = serverTime - now
        self.cr.setServerDelta(serverDelta)
        self.notify.setServerDelta(serverDelta, 28800)
        self.notify.info('Login response return code %s' % returnCode)
        if returnCode == 0:
            self._LoginScreen__handleLoginSuccess()
        elif returnCode == 12:
            self.notify.info('Bad password')
            self.fsm.request('showLoginFailDialog', [
                OTPLocalizer.LoginScreenBadPassword])
        elif returnCode == 14:
            self.notify.info('Bad word in user name')
            self.fsm.request('showLoginFailDialog', [
                OTPLocalizer.LoginScreenInvalidUserName])
        elif returnCode == 129:
            self.notify.info('Username not found')
            self.fsm.request('showLoginFailDialog', [
                OTPLocalizer.LoginScreenUserNameNotFound])
        else:
            self.notify.info('Login failed: %s' % errorString)
            messenger.send(self.doneEvent, [
                {
                    'mode': 'reject' }])

    
    def _LoginScreen__handleLoginSuccess(self):
        self.cr.logAccountInfo()
        if launcher:
            launcher.setGoUserName(self.userName)
            launcher.setLastLogin(self.userName)
            launcher.setUserLoggedIn()
            if self.loginInterface.freeTimeExpires == -1:
                launcher.setPaidUserLoggedIn()
            
        
        if self.loginInterface.needToSetParentPassword():
            messenger.send(self.doneEvent, [
                {
                    'mode': 'getChatPassword' }])
        else:
            messenger.send(self.doneEvent, [
                {
                    'mode': 'success' }])

    
    def _LoginScreen__handleEnterLoginAck(self):
        self.dialog.hide()
        self.fsm.request('login')

    
    def _LoginScreen__handleNoNewAccountsAck(self):
        self.dialog.hide()
        self.fsm.request('login')


