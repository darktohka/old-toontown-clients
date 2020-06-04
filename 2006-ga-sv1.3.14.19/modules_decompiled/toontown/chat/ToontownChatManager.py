# File: T (Python 2.2)

import sys
from direct.showbase import PandaObject
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLocalizer
from toontown.toonbase import TTLocalizer
from toontown.toontowngui import TeaserPanel
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from otp.chat import ChatManager
from TTChatInputSpeedChat import TTChatInputSpeedChat
from TTChatInputNormal import TTChatInputNormal
SCToontaskChatEvent = 'SCToontaskChatEvent'

class ToontownChatManager(ChatManager.ChatManager):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownChatManager')
    
    def __init__(self, cr, localAvatar):
        gui = loader.loadModelOnce('phase_3.5/models/gui/chat_input_gui')
        self.normalButton = DirectButton(image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (-1.2646999999999999, 0, 0.92800000000000005), scale = 1.179, relief = None, image_color = Vec4(1, 1, 1, 1), text = ('', OTPLocalizer.ChatManagerChat, OTPLocalizer.ChatManagerChat), text_align = TextNode.ALeft, text_scale = TTLocalizer.CMnormalButton, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (-0.052499999999999998, -0.089999999999999997), textMayChange = 0, sortOrder = FOREGROUND_SORT_INDEX, command = self._ToontownChatManager__normalButtonPressed)
        self.normalButton.hide()
        self.openScSfx = loader.loadSfx('phase_3.5/audio/sfx/GUI_quicktalker.mp3')
        self.openScSfx.setVolume(0.59999999999999998)
        self.scButton = DirectButton(image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = TTLocalizer.CMscButtonPos, scale = 1.179, relief = None, image_color = Vec4(0.75, 1, 0.59999999999999998, 1), text = ('', OTPLocalizer.GlobalSpeedChatName, OTPLocalizer.GlobalSpeedChatName), text_scale = TTLocalizer.CMscButton, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, sortOrder = FOREGROUND_SORT_INDEX, command = self._ToontownChatManager__scButtonPressed, clickSound = self.openScSfx)
        self.scButton.hide()
        self.whisperFrame = DirectFrame(relief = None, image = getDefaultDialogGeom(), image_scale = (0.45000000000000001, 0.45000000000000001, 0.45000000000000001), image_color = OTPGlobals.GlobalDialogColor, pos = (-0.40000000000000002, 0, 0.754), text = OTPLocalizer.ChatManagerWhisperTo, text_wordwrap = 7.0, text_scale = TTLocalizer.CMwhisperFrame, text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0.14000000000000001), textMayChange = 1, sortOrder = FOREGROUND_SORT_INDEX)
        self.whisperFrame.hide()
        self.whisperButton = DirectButton(parent = self.whisperFrame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (-0.125, 0, -0.10000000000000001), scale = 1.179, relief = None, image_color = Vec4(1, 1, 1, 1), text = ('', OTPLocalizer.ChatManagerChat, OTPLocalizer.ChatManagerChat, ''), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), text_scale = TTLocalizer.CMwhisperButton, text_fg = (0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, command = self._ToontownChatManager__whisperButtonPressed)
        self.whisperScButton = DirectButton(parent = self.whisperFrame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (0.0, 0, -0.10000000000000001), scale = 1.179, relief = None, image_color = Vec4(0.75, 1, 0.59999999999999998, 1), text = ('', OTPLocalizer.GlobalSpeedChatName, OTPLocalizer.GlobalSpeedChatName, ''), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, command = self._ToontownChatManager__whisperScButtonPressed)
        self.whisperCancelButton = DirectButton(parent = self.whisperFrame, image = (gui.find('**/CloseBtn_UP'), gui.find('**/CloseBtn_DN'), gui.find('**/CloseBtn_Rllvr')), pos = (0.125, 0, -0.10000000000000001), scale = 1.179, relief = None, text = ('', OTPLocalizer.ChatManagerCancel, OTPLocalizer.ChatManagerCancel), text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, command = self._ToontownChatManager__whisperCancelPressed)
        gui.removeNode()
        ChatManager.ChatManager.__init__(self, cr, localAvatar)
        self.chatInputSpeedChat = TTChatInputSpeedChat(self)
        self.chatInputNormal = TTChatInputNormal(self)

    
    def delete(self):
        ChatManager.ChatManager.delete(self)
        loader.unloadModel('phase_3.5/models/gui/chat_input_gui')
        self.normalButton.destroy()
        del self.normalButton
        self.scButton.destroy()
        del self.scButton
        del self.openScSfx
        self.whisperFrame.destroy()
        del self.whisperFrame
        del self.whisperButton
        del self.whisperScButton
        del self.whisperCancelButton

    
    def sendSCToontaskChatMessage(self, taskId, toNpcId, toonProgress, msgIndex):
        messenger.send('chatUpdateSCToontask', [
            taskId,
            toNpcId,
            toonProgress,
            msgIndex])
        messenger.send(SCToontaskChatEvent)
        self.announceSCChat()

    
    def sendSCToontaskWhisperMessage(self, taskId, toNpcId, toonProgress, msgIndex, whisperAvatarId):
        messenger.send('whisperUpdateSCToontask', [
            taskId,
            toNpcId,
            toonProgress,
            msgIndex,
            whisperAvatarId])

    
    def enterOpenChatWarning(self):
        if self.openChatWarning == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            buttonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.openChatWarning = DirectFrame(pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.90000000000000002), text = OTPLocalizer.OpenChatWarning, text_wordwrap = 19, text_scale = TTLocalizer.CMopenChatWarning, text_pos = (0.0, 0.28000000000000003), textMayChange = 0)
            DirectButton(self.openChatWarning, image = buttonImage, relief = None, text = OTPLocalizer.OpenChatWarningOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.28000000000000003), command = self._ToontownChatManager__handleOpenChatWarningOK)
            buttons.removeNode()
        
        self.openChatWarning.show()
        (normObs, scObs) = self.isObscured()
        if not scObs:
            self.scButton.show()
        

    
    def exitOpenChatWarning(self):
        self.openChatWarning.hide()
        self.scButton.hide()

    
    def enterUnpaidChatWarning(self):
        if self.paidNoParentPassword:
            if base.cr.productName in [
                'DisneyOnline-UK',
                'ES',
                'Wanadoo',
                'T-Online',
                'JP']:
                directFrameText = OTPLocalizer.PaidParentPasswordUKWarning
                payButtonText = OTPLocalizer.PaidParentPasswordUKWarningSet
                directButtonText = OTPLocalizer.PaidParentPasswordUKWarningContinue
            else:
                directFrameText = OTPLocalizer.PaidNoParentPasswordWarning
                payButtonText = OTPLocalizer.PaidNoParentPasswordWarningSet
                directButtonText = OTPLocalizer.PaidNoParentPasswordWarningContinue
            if self.unpaidChatWarning == None:
                guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
                buttonImage = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
                self.unpaidChatWarning = DirectFrame(pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.69999999999999996), text = directFrameText, text_wordwrap = TTLocalizer.CMunpaidChatWarningwordwrap, text_scale = TTLocalizer.CMunpaidChatWarning, text_pos = (0.0, 0.23000000000000001), textMayChange = 0)
                self.payButton = DirectButton(self.unpaidChatWarning, image = buttonImage, relief = None, text = payButtonText, image_scale = (1.75, 1, 1.1499999999999999), text_scale = TTLocalizer.CMpayButton, text_pos = (0, -0.02), textMayChange = 0, pos = (0.0, 0.0, -0.080000000000000002), command = self._ToontownChatManager__handleUnpaidChatWarningPay)
                DirectButton(self.unpaidChatWarning, image = buttonImage, relief = None, text = directButtonText, textMayChange = 0, image_scale = (1.75, 1, 1.1499999999999999), text_scale = 0.059999999999999998, text_pos = (0, -0.02), pos = (0.0, 0.0, -0.23000000000000001), command = self._ToontownChatManager__handleUnpaidChatWarningContinue)
                guiButton.removeNode()
            
            if base.localAvatar.inTutorial:
                self.payButton.hide()
            else:
                self.payButton.show()
            self.unpaidChatWarning.show()
        elif self.unpaidChatWarning:
            self.unpaidChatWarning.hide()
        
        base.cr.playGame.getPlace().fsm.request('phone')
        self.teaser = TeaserPanel.TeaserPanel('secretChat', self._ToontownChatManager__handleUnpaidChatWarningDone)
        if base.localAvatar.inTutorial:
            self.teaser.hidePay()
        
        (normObs, scObs) = self.isObscured()
        if not scObs:
            self.scButton.show()
        

    
    def exitUnpaidChatWarning(self):
        if self.unpaidChatWarning:
            self.unpaidChatWarning.hide()
        
        self.scButton.hide()

    
    def enterNoSecretChatAtAll(self):
        if self.noSecretChatAtAll == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.noSecretChatAtAll = DirectFrame(pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.3999999999999999, 1.0, 1.0), text = OTPLocalizer.NoSecretChatAtAll, text_wordwrap = 20, textMayChange = 0, text_scale = 0.059999999999999998, text_pos = (0, 0.25))
            self.noSecretChatAtAll.setBin('gui-popup', 10)
            DirectLabel(parent = self.noSecretChatAtAll, relief = None, pos = (0, 0, 0.34999999999999998), text = OTPLocalizer.NoSecretChatAtAllTitle, textMayChange = 0, text_scale = 0.080000000000000002)
            DirectButton(self.noSecretChatAtAll, image = okButtonImage, relief = None, text = OTPLocalizer.NoSecretChatAtAllOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.34999999999999998), command = self._ToontownChatManager__handleNoSecretChatAtAllOK)
            buttons.removeNode()
        
        self.noSecretChatAtAll.show()

    
    def exitNoSecretChatAtAll(self):
        self.noSecretChatAtAll.hide()

    
    def enterNoSecretChatWarning(self):
        if self.noSecretChatWarning == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            if base.cr.productName != 'Terra-DMC':
                okPos = (-0.22, 0.0, -0.34999999999999998)
                textPos = (0, 0.25)
                okCommand = self._ToontownChatManager__handleNoSecretChatWarningOK
            else:
                self.passwordEntry = None
                okPos = (0, 0, -0.34999999999999998)
                textPos = (0, 0.125)
                okCommand = self._ToontownChatManager__handleNoSecretChatWarningCancel
            self.noSecretChatWarning = DirectFrame(pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.3999999999999999, 1.0, 1.0), text = OTPLocalizer.NoSecretChatWarning, text_wordwrap = 20, text_scale = 0.055, text_pos = textPos, textMayChange = 1)
            self.noSecretChatWarning.setBin('gui-popup', 10)
            DirectButton(self.noSecretChatWarning, image = okButtonImage, relief = None, text = OTPLocalizer.NoSecretChatWarningOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = okPos, command = okCommand)
            DirectLabel(parent = self.noSecretChatWarning, relief = None, pos = (0, 0, 0.34999999999999998), text = OTPLocalizer.NoSecretChatWarningTitle, textMayChange = 0, text_scale = 0.080000000000000002)
            if base.cr.productName != 'Terra-DMC':
                self.passwordLabel = DirectLabel(parent = self.noSecretChatWarning, relief = None, pos = (-0.070000000000000007, 0.0, -0.20000000000000001), text = OTPLocalizer.ParentPassword, text_scale = 0.059999999999999998, text_align = TextNode.ARight, textMayChange = 0)
                self.passwordEntry = DirectEntry(parent = self.noSecretChatWarning, relief = None, image = nameBalloon, image1_color = (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1.0), scale = 0.064000000000000001, pos = (0.0, 0.0, -0.20000000000000001), width = OTPGlobals.maxLoginWidth, numLines = 1, focus = 1, cursorKeys = 1, obscured = 1, command = self._ToontownChatManager__handleNoSecretChatWarningOK)
                DirectButton(self.noSecretChatWarning, image = cancelButtonImage, relief = None, text = OTPLocalizer.NoSecretChatWarningCancel, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 1, pos = (0.20000000000000001, 0.0, -0.34999999999999998), command = self._ToontownChatManager__handleNoSecretChatWarningCancel)
            
            buttons.removeNode()
            nameBalloon.removeNode()
        else:
            self.noSecretChatWarning['text'] = OTPLocalizer.NoSecretChatWarning
            if self.passwordEntry:
                self.passwordEntry['focus'] = 1
                self.passwordEntry.enterText('')
            
        self.noSecretChatWarning.show()

    
    def exitNoSecretChatWarning(self):
        self.noSecretChatWarning.hide()

    
    def enterActivateChat(self):
        if self.activateChat == None:
            guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            moreButtonImage = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
            self.activateChat = DirectFrame(pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.8, 1.0, 1.3), text = OTPLocalizer.ActivateChat, text_align = TextNode.ALeft, text_wordwrap = 28, text_scale = TTLocalizer.CMactivateChat, text_pos = (-0.81999999999999995, 0.5), textMayChange = 0)
            if base.cr.productName != 'JP':
                DirectButton(self.activateChat, image = moreButtonImage, image_scale = (1.25, 1.0, 1.0), relief = None, text = OTPLocalizer.ActivateChatMoreInfo, text_scale = 0.059999999999999998, text_pos = (0, -0.02), textMayChange = 0, pos = (0.0, 0.0, 0.29999999999999999), command = self._ToontownChatManager__handleActivateChatMoreInfo)
            
            DirectButton(self.activateChat, image = okButtonImage, relief = None, text = OTPLocalizer.ActivateChatYes, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (-0.5, 0.0, -0.5), command = self._ToontownChatManager__handleActivateChatYes)
            DirectButton(self.activateChat, image = cancelButtonImage, relief = None, text = OTPLocalizer.ActivateChatNo, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.5, 0.0, -0.5), command = self._ToontownChatManager__handleActivateChatNo)
            if base.cr.productName != 'JP':
                DirectButton(self.activateChat, image = moreButtonImage, image_scale = (1.75, 1.0, 1.0), relief = None, text = OTPLocalizer.ActivateChatPrivacyPolicy, text_scale = 0.059999999999999998, text_pos = (0, -0.02), textMayChange = 0, pos = (0.0, 0.0, -0.5), command = self._ToontownChatManager__handleActivateChatPrivacyPolicy)
            
            guiButton.removeNode()
            buttons.removeNode()
        
        self.activateChat.show()

    
    def exitActivateChat(self):
        self.activateChat.hide()

    
    def enterSecretChatActivated(self):
        if self.secretChatActivated == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            buttonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.secretChatActivated = DirectFrame(pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.80000000000000004), text = OTPLocalizer.SecretChatActivated, text_align = TextNode.ALeft, text_wordwrap = 17.5, text_scale = TTLocalizer.CMchatActivated, text_pos = (-0.5, 0.25), textMayChange = 0)
            DirectButton(self.secretChatActivated, image = buttonImage, relief = None, text = OTPLocalizer.SecretChatActivatedOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.22), command = self._ToontownChatManager__handleSecretChatActivatedOK)
            buttons.removeNode()
        
        self.secretChatActivated.show()

    
    def exitSecretChatActivated(self):
        self.secretChatActivated.hide()

    
    def enterProblemActivatingChat(self):
        if self.problemActivatingChat == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            buttonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.problemActivatingChat = DirectFrame(pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.90000000000000002), text = '', text_align = TextNode.ALeft, text_wordwrap = 18, text_scale = 0.059999999999999998, text_pos = (-0.5, 0.28000000000000003), textMayChange = 1)
            DirectButton(self.problemActivatingChat, image = buttonImage, relief = None, text = OTPLocalizer.ProblemActivatingChatOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.28000000000000003), command = self._ToontownChatManager__handleProblemActivatingChatOK)
            buttons.removeNode()
        
        self.problemActivatingChat.show()

    
    def exitProblemActivatingChat(self):
        self.problemActivatingChat.hide()

    
    def _ToontownChatManager__normalButtonPressed(self):
        if base.cr.productName == 'DisneyOnline-US':
            if not base.cr.isPaid():
                self.fsm.request('unpaidChatWarning')
            elif not base.cr.isParentPasswordSet():
                self.paidNoParentPassword = 1
                self.fsm.request('unpaidChatWarning')
            elif not base.cr.allowSecretChat():
                tt = base.cr.loginInterface
                if tt.supportsParentPassword():
                    self.fsm.request('noSecretChatWarning')
                else:
                    self.fsm.request('noSecretChatAtAll')
            elif not base.localAvatar.canChat():
                self.fsm.request('openChatWarning')
            else:
                self.fsm.request('normalChat')
        elif base.cr.productName == 'Terra-DMC':
            if not base.cr.allowSecretChat():
                self.fsm.request('noSecretChatWarning')
            elif not base.localAvatar.canChat():
                self.fsm.request('openChatWarning')
            else:
                self.fsm.request('normalChat')
        elif base.cr.productName in [
            'DisneyOnline-UK',
            'ES',
            'Wanadoo',
            'T-Online',
            'JP']:
            if not base.cr.isPaid():
                self.fsm.request('unpaidChatWarning')
            elif not base.cr.isParentPasswordSet():
                self.paidNoParentPassword = 1
                self.fsm.request('unpaidChatWarning')
            elif not base.cr.allowSecretChat():
                self.paidNoParentPassword = 1
                self.fsm.request('unpaidChatWarning')
            elif not base.localAvatar.canChat():
                self.fsm.request('openChatWarning')
            else:
                self.fsm.request('normalChat')
        else:
            print 'ChatManager: productName: %s not recognized' % base.cr.productName

    
    def _ToontownChatManager__scButtonPressed(self):
        self.fsm.request('speedChat')

    
    def _ToontownChatManager__whisperButtonPressed(self, avatarName, avatarId):
        self.fsm.request('whisperChat', [
            avatarName,
            avatarId])

    
    def _ToontownChatManager__whisperScButtonPressed(self, avatarId):
        self.fsm.request('whisperSpeedChat', [
            avatarId])

    
    def _ToontownChatManager__whisperCancelPressed(self):
        self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleOpenChatWarningOK(self):
        self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleUnpaidChatWarningDone(self):
        base.cr.playGame.getPlace().handleBookClose()
        self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleUnpaidChatWarningContinue(self):
        self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleUnpaidChatWarningPay(self):
        if base.cr.isWebPlayToken():
            self.fsm.request('leaveToPayDialog')
        else:
            self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleNoSecretChatAtAllOK(self):
        self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleNoSecretChatWarningOK(self, *args):
        password = self.passwordEntry.get()
        tt = base.cr.loginInterface
        (okflag, message) = tt.authenticateParentPassword(base.cr.userName, base.cr.password, password)
        if okflag:
            self.fsm.request('activateChat')
        elif message:
            self.fsm.request('problemActivatingChat')
            self.problemActivatingChat['text'] = OTPLocalizer.ProblemActivatingChat % message
        else:
            self.noSecretChatWarning['text'] = OTPLocalizer.NoSecretChatWarningWrongPassword
            self.passwordEntry['focus'] = 1
            self.passwordEntry.enterText('')

    
    def _ToontownChatManager__handleNoSecretChatWarningCancel(self):
        self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleActivateChatYes(self):
        password = self.passwordEntry.get()
        tt = base.cr.loginInterface
        (okflag, message) = tt.enableSecretFriends(base.cr.userName, base.cr.password, password)
        if okflag:
            tt.resendPlayToken()
            base.cr.secretChatAllowed = 1
            self.fsm.request('secretChatActivated')
        elif message == None:
            message = 'Parent Password was invalid.'
        
        self.fsm.request('problemActivatingChat')
        self.problemActivatingChat['text'] = OTPLocalizer.ProblemActivatingChat % message

    
    def _ToontownChatManager__handleActivateChatMoreInfo(self):
        self.fsm.request('chatMoreInfo')

    
    def _ToontownChatManager__handleActivateChatPrivacyPolicy(self):
        self.fsm.request('chatPrivacyPolicy')

    
    def _ToontownChatManager__handleActivateChatNo(self):
        self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleSecretChatActivatedOK(self):
        self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleProblemActivatingChatOK(self):
        self.fsm.request('mainMenu')


