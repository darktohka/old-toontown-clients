# File: F (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import string
from otp.otpbase import OTPLocalizer
from otp.otpbase import OTPGlobals
globalFriendSecret = None

def showFriendSecret():
    global globalFriendSecret
    if not base.cr.isPaid() and base.cr.productName == 'DisneyOnline-US':
        chatMgr = base.localAvatar.chatMgr
        chatMgr.fsm.request('unpaidChatWarning')
    elif not base.cr.isParentPasswordSet():
        chatMgr = base.localAvatar.chatMgr
        if base.cr.productName in [
            'DisneyOnline-UK',
            'ES',
            'Wanadoo',
            'T-Online',
            'JP']:
            chatMgr = base.localAvatar.chatMgr
            if not base.cr.isPaid():
                chatMgr.fsm.request('unpaidChatWarning')
            else:
                chatMgr.paidNoParentPassword = 1
                chatMgr.fsm.request('unpaidChatWarning')
        else:
            chatMgr.paidNoParentPassword = 1
            chatMgr.fsm.request('unpaidChatWarning')
    elif not base.cr.allowSecretChat():
        chatMgr = base.localAvatar.chatMgr
        if base.cr.productName in [
            'DisneyOnline-UK',
            'ES',
            'Wanadoo',
            'T-Online',
            'JP']:
            chatMgr = base.localAvatar.chatMgr
            if not base.cr.isPaid():
                chatMgr.fsm.request('unpaidChatWarning')
            else:
                chatMgr.paidNoParentPassword = 1
                chatMgr.fsm.request('unpaidChatWarning')
        else:
            chatMgr.fsm.request('noSecretChatWarning')
    elif base.cr.needParentPasswordForSecretChat():
        unloadFriendSecret()
        globalFriendSecret = FriendSecretNeedsParentPassword()
        globalFriendSecret.enter()
    else:
        openFriendSecret()


def openFriendSecret():
    global globalFriendSecret
    if globalFriendSecret != None:
        globalFriendSecret.unload()
    
    globalFriendSecret = FriendSecret()
    globalFriendSecret.enter()


def hideFriendSecret():
    if globalFriendSecret != None:
        globalFriendSecret.exit()
    


def unloadFriendSecret():
    global globalFriendSecret
    if globalFriendSecret != None:
        globalFriendSecret.unload()
        globalFriendSecret = None
    


class FriendSecretNeedsParentPassword(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendSecretNeedsParentPassword')
    
    def __init__(self):
        StateData.StateData.__init__(self, 'friend-secret-needs-parent-pw-done')
        self.dialog = None

    
    def enter(self):
        StateData.StateData.enter(self)
        base.localAvatar.chatMgr.fsm.request('otherDialog')
        if self.dialog == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            if base.cr.productName != 'Terra-DMC':
                okPos = (-0.22, 0.0, -0.34999999999999998)
                textPos = (0, 0.25)
                okCommand = self._FriendSecretNeedsParentPassword__handleOK
            else:
                self.passwordEntry = None
                okPos = (0, 0, -0.34999999999999998)
                textPos = (0, 0.125)
                okCommand = self._FriendSecretNeedsParentPassword__handleCancel
            self.dialog = DirectFrame(pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.3999999999999999, 1.0, 1.0), text = OTPLocalizer.FriendSecretNeedsPasswordWarning, text_wordwrap = 20, text_scale = 0.055, text_pos = textPos, textMayChange = 1)
            DirectButton(self.dialog, image = okButtonImage, relief = None, text = OTPLocalizer.FriendSecretNeedsPasswordWarningOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = okPos, command = okCommand)
            DirectLabel(parent = self.dialog, relief = None, pos = (0, 0, 0.34999999999999998), text = OTPLocalizer.FriendSecretNeedsPasswordWarningTitle, textMayChange = 0, text_scale = 0.080000000000000002)
            if base.cr.productName != 'Terra-DMC':
                self.passwordLabel = DirectLabel(parent = self.dialog, relief = None, pos = (-0.070000000000000007, 0.0, -0.20000000000000001), text = OTPLocalizer.ParentPassword, text_scale = 0.059999999999999998, text_align = TextNode.ARight, textMayChange = 0)
                self.passwordEntry = DirectEntry(parent = self.dialog, relief = None, image = nameBalloon, image1_color = (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1.0), scale = 0.064000000000000001, pos = (0.0, 0.0, -0.20000000000000001), width = OTPGlobals.maxLoginWidth, numLines = 1, focus = 1, cursorKeys = 1, obscured = 1, command = self._FriendSecretNeedsParentPassword__handleOK)
                DirectButton(self.dialog, image = cancelButtonImage, relief = None, text = OTPLocalizer.FriendSecretNeedsPasswordWarningCancel, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 1, pos = (0.20000000000000001, 0.0, -0.34999999999999998), command = self._FriendSecretNeedsParentPassword__handleCancel)
            
            buttons.removeNode()
            nameBalloon.removeNode()
        else:
            self.dialog['text'] = OTPLocalizer.FriendSecretNeedsPasswordWarning
            if self.passwordEntry:
                self.passwordEntry['focus'] = 1
                self.passwordEntry.enterText('')
            
        self.dialog.show()

    
    def exit(self):
        self.ignoreAll()
        if self.dialog:
            self.dialog.destroy()
            self.dialog = None
        
        if self.isEntered:
            base.localAvatar.chatMgr.fsm.request('mainMenu')
            StateData.StateData.exit(self)
        

    
    def _FriendSecretNeedsParentPassword__handleOK(self, *args):
        password = self.passwordEntry.get()
        tt = base.cr.loginInterface
        (okflag, message) = tt.authenticateParentPassword(base.cr.userName, base.cr.password, password)
        if okflag:
            openFriendSecret()
            self.exit()
        elif message:
            base.localAvatar.chatMgr.problemActivatingChat['text'] = OTPLocalizer.ProblemActivatingChat % message
            base.localAvatar.chatMgr.fsm.request('problemActivatingChat')
        else:
            self.dialog['text'] = OTPLocalizer.FriendSecretNeedsPasswordWarningWrongPassword
            self.passwordEntry['focus'] = 1
            self.passwordEntry.enterText('')

    
    def _FriendSecretNeedsParentPassword__handleCancel(self):
        self.exit()



class FriendSecret(DirectFrame, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendSecret')
    
    def __init__(self):
        DirectFrame.__init__(self, pos = (0, 0, 0.29999999999999999), relief = None, image = getDefaultDialogGeom(), image_scale = (1.6000000000000001, 1, 1.2), image_pos = (0, 0, -0.050000000000000003), image_color = OTPGlobals.GlobalDialogColor, borderWidth = (0.01, 0.01))
        StateData.StateData.__init__(self, 'friend-secret-done')
        self.initialiseoptions(FriendSecret)

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        self.isLoaded = 0
        self.exit()
        del self.introText
        del self.getSecret
        del self.enterSecretText
        del self.enterSecret
        del self.ok1
        del self.ok2
        del self.cancel
        del self.secretText
        DirectFrame.destroy(self)

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.isLoaded = 1
        self.introText = DirectLabel(parent = self, relief = None, pos = (0, 0, 0.40000000000000002), scale = 0.050000000000000003, text = OTPLocalizer.FriendSecretIntro, text_fg = (0, 0, 0, 1), text_wordwrap = 30)
        self.introText.hide()
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        self.getSecret = DirectButton(parent = self, relief = None, pos = (0, 0, -0.11), image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (1.25, 1, 1), text = OTPLocalizer.FriendSecretGetSecret, text_scale = OTPLocalizer.FSgetSecretButton, text_pos = (0, -0.02), command = self._FriendSecret__getSecret)
        self.getSecret.hide()
        self.enterSecretText = DirectLabel(parent = self, relief = None, pos = OTPLocalizer.FSenterSecretTextPos, scale = 0.050000000000000003, text = OTPLocalizer.FriendSecretEnterSecret, text_fg = (0, 0, 0, 1), text_wordwrap = 30)
        self.enterSecretText.hide()
        self.enterSecret = DirectEntry(parent = self, relief = SUNKEN, scale = 0.059999999999999998, pos = (-0.59999999999999998, 0, -0.38), frameColor = (0.80000000000000004, 0.80000000000000004, 0.5, 1), borderWidth = (0.10000000000000001, 0.10000000000000001), numLines = 1, width = 20, frameSize = (-0.40000000000000002, 20.399999999999999, -0.40000000000000002, 1.1000000000000001), command = self._FriendSecret__enterSecret)
        self.enterSecret.resetFrameSize()
        self.enterSecret.hide()
        self.ok1 = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.59999999999999998, 1, 1), text = OTPLocalizer.FriendSecretOK, text_scale = 0.059999999999999998, text_pos = (0, -0.02), pos = (0, 0, -0.5), command = self._FriendSecret__ok1)
        self.ok1.hide()
        self.ok2 = DirectButton(parent = self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.59999999999999998, 1, 1), text = OTPLocalizer.FriendSecretOK, text_scale = 0.059999999999999998, text_pos = (0, -0.02), pos = (0, 0, -0.56999999999999995), command = self._FriendSecret__ok2)
        self.ok2.hide()
        self.cancel = DirectButton(parent = self, relief = None, text = OTPLocalizer.FriendSecretCancel, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.59999999999999998, 1, 1), text_scale = 0.059999999999999998, text_pos = (0, -0.02), pos = (0, 0, -0.56999999999999995), command = self._FriendSecret__cancel)
        self.cancel.hide()
        self.nextText = DirectLabel(parent = self, relief = None, pos = (0, 0, 0.29999999999999999), scale = 0.059999999999999998, text = '', text_scale = OTPLocalizer.FSnextText, text_fg = (0, 0, 0, 1), text_wordwrap = 25.5)
        self.nextText.hide()
        self.secretText = DirectLabel(parent = self, relief = None, pos = (0, 0, -0.41999999999999998), scale = 0.10000000000000001, text = '', text_fg = (0, 0, 0, 1), text_wordwrap = 30)
        self.secretText.hide()
        guiButton.removeNode()

    
    def enter(self):
        if self.isEntered == 1:
            return None
        
        self.isEntered = 1
        if self.isLoaded == 0:
            self.load()
        
        self.show()
        self.introText.show()
        self.getSecret.show()
        self.enterSecretText.show()
        self.enterSecret.show()
        self.ok1.show()
        self.ok2.hide()
        self.cancel.hide()
        self.nextText.hide()
        self.secretText.hide()
        base.localAvatar.chatMgr.fsm.request('otherDialog')
        self.enterSecret['focus'] = 1
        NametagGlobals.setOnscreenChatForced(1)
        return None

    
    def exit(self):
        if self.isEntered == 0:
            return None
        
        self.isEntered = 0
        NametagGlobals.setOnscreenChatForced(0)
        self._FriendSecret__cleanupFirstPage()
        self.ignoreAll()
        self.hide()
        return None

    
    def _FriendSecret__getSecret(self):
        if not (base.cr.friendManager):
            self.notify.warning('No FriendManager available.')
            self.exit()
            return None
        
        self._FriendSecret__cleanupFirstPage()
        self.nextText['text'] = OTPLocalizer.FriendSecretGettingSecret
        self.nextText.setPos(0, 0, 0.29999999999999999)
        self.nextText.show()
        self.ok1.hide()
        self.cancel.show()
        self.accept('requestSecretResponse', self._FriendSecret__gotSecret)
        base.cr.friendManager.up_requestSecret()

    
    def _FriendSecret__gotSecret(self, result, secret):
        self.ignore('requestSecretResponse')
        if result == 1:
            self.nextText['text'] = OTPLocalizer.FriendSecretGotSecret
            self.nextText.setPos(*OTPLocalizer.FSgotSecretPos)
            self.secretText['text'] = secret
        else:
            self.nextText['text'] = OTPLocalizer.FriendSecretTooMany
        self.nextText.show()
        self.secretText.show()
        self.cancel.hide()
        self.ok1.hide()
        self.ok2.show()

    
    def _FriendSecret__enterSecret(self, secret):
        self.enterSecret.set('')
        secret = string.strip(secret)
        if not secret:
            self.exit()
            return None
        
        if not (base.cr.friendManager):
            self.notify.warning('No FriendManager available.')
            self.exit()
            return None
        
        self._FriendSecret__cleanupFirstPage()
        self.nextText['text'] = OTPLocalizer.FriendSecretTryingSecret
        self.nextText.setPos(0, 0, 0.29999999999999999)
        self.nextText.show()
        self.ok1.hide()
        self.cancel.show()
        self.accept('submitSecretResponse', self._FriendSecret__enteredSecret)
        base.cr.friendManager.up_submitSecret(secret)

    
    def _FriendSecret__enteredSecret(self, result, avId):
        self.ignore('submitSecretResponse')
        if result == 1:
            handle = base.cr.identifyAvatar(avId)
            if handle != None:
                self.nextText['text'] = OTPLocalizer.FriendSecretEnteredSecretSuccess % handle.getName()
            else:
                self.accept('friendsMapComplete', self._FriendSecret__nowFriends, [
                    avId])
                ready = base.cr.fillUpFriendsMap()
                if ready:
                    self._FriendSecret__nowFriends(avId)
                
                return None
        elif result == 0:
            self.nextText['text'] = OTPLocalizer.FriendSecretEnteredSecretUnknown
        elif result == 2:
            handle = base.cr.identifyAvatar(avId)
            if handle != None:
                self.nextText['text'] = OTPLocalizer.FriendSecretEnteredSecretFull % handle.getName()
            else:
                self.nextText['text'] = OTPLocalizer.FriendSecretEnteredSecretFullNoName
        elif result == 3:
            self.nextText['text'] = OTPLocalizer.FriendSecretEnteredSecretSelf
        
        self.nextText.show()
        self.cancel.hide()
        self.ok1.hide()
        self.ok2.show()

    
    def _FriendSecret__nowFriends(self, avId):
        self.ignore('friendsMapComplete')
        handle = base.cr.identifyAvatar(avId)
        if handle != None:
            self.nextText['text'] = OTPLocalizer.FriendSecretNowFriends % handle.getName()
        else:
            self.nextText['text'] = OTPLocalizer.FriendSecretNowFriendsNoName
        self.nextText.show()
        self.cancel.hide()
        self.ok1.hide()
        self.ok2.show()

    
    def _FriendSecret__ok1(self):
        secret = self.enterSecret.get()
        self._FriendSecret__enterSecret(secret)

    
    def _FriendSecret__ok2(self):
        self.exit()

    
    def _FriendSecret__cancel(self):
        self.exit()

    
    def _FriendSecret__cleanupFirstPage(self):
        self.introText.hide()
        self.getSecret.hide()
        self.enterSecretText.hide()
        self.enterSecret.hide()
        base.localAvatar.chatMgr.fsm.request('mainMenu')


