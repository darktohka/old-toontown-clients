# File: T (Python 2.2)

import sys
from direct.showbase import PandaObject
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLocalizer
from toontown.toontowngui import TeaserPanel
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from otp.chat import ChatManager
from TTChatInputSpeedChat import TTChatInputSpeedChat
from TTChatInputNormal import TTChatInputNormal

class HackedDirectRadioButton(DirectCheckButton):
    
    def __init__(self, parent = None, **kw):
        optiondefs = ()
        self.defineoptions(kw, optiondefs)
        DirectCheckButton.__init__(self, parent)
        self.initialiseoptions(HackedDirectRadioButton)

    
    def commandFunc(self, event):
        if self['indicatorValue']:
            self['indicatorValue'] = 0
        
        DirectCheckButton.commandFunc(self, event)



class ToontownChatManager(ChatManager.ChatManager):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownChatManager')
    
    def __init__(self, cr, localAvatar):
        gui = loader.loadModelOnce('phase_3.5/models/gui/chat_input_gui')
        self.normalButton = DirectButton(image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (-1.2646999999999999, 0, 0.92800000000000005), scale = 1.179, relief = None, image_color = Vec4(1, 1, 1, 1), text = ('', OTPLocalizer.ChatManagerChat, OTPLocalizer.ChatManagerChat), text_align = TextNode.ALeft, text_scale = 0.059999999999999998, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (-0.052499999999999998, -0.089999999999999997), textMayChange = 0, sortOrder = FOREGROUND_SORT_INDEX, command = self._ToontownChatManager__normalButtonPressed)
        self.normalButton.hide()
        self.openScSfx = loader.loadSfx('phase_3.5/audio/sfx/GUI_quicktalker.mp3')
        self.openScSfx.setVolume(0.59999999999999998)
        self.scButton = DirectButton(image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (-1.129, 0, 0.92800000000000005), scale = 1.179, relief = None, image_color = Vec4(0.75, 1, 0.59999999999999998, 1), text = ('', OTPLocalizer.GlobalSpeedChatName, OTPLocalizer.GlobalSpeedChatName), text_scale = 0.059999999999999998, text_fg = Vec4(1, 1, 1, 1), text_shadow = Vec4(0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, sortOrder = FOREGROUND_SORT_INDEX, command = self._ToontownChatManager__scButtonPressed, clickSound = self.openScSfx)
        self.scButton.hide()
        self.whisperFrame = DirectFrame(parent = aspect2dp, relief = None, image = getDefaultDialogGeom(), image_scale = (0.45000000000000001, 0.45000000000000001, 0.45000000000000001), image_color = OTPGlobals.GlobalDialogColor, pos = (-0.40000000000000002, 0, 0.754), text = OTPLocalizer.ChatManagerWhisperTo, text_wordwrap = 7.0, text_scale = 0.059999999999999998, text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0.14000000000000001), textMayChange = 1, sortOrder = FOREGROUND_SORT_INDEX)
        self.whisperFrame.hide()
        self.whisperButton = DirectButton(parent = self.whisperFrame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos = (-0.125, 0, -0.10000000000000001), scale = 1.179, relief = None, image_color = Vec4(1, 1, 1, 1), text = ('', OTPLocalizer.ChatManagerChat, OTPLocalizer.ChatManagerChat, ''), image3_color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998), text_scale = 0.050000000000000003, text_fg = (0, 0, 0, 1), text_pos = (0, -0.089999999999999997), textMayChange = 0, command = self._ToontownChatManager__whisperButtonPressed)
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

    
    def sendSCResistanceChatMessage(self, textId):
        messenger.send('chatUpdateSCResistance', [
            textId])
        self.announceSCChat()

    
    def sendSCToontaskChatMessage(self, taskId, toNpcId, toonProgress, msgIndex):
        messenger.send('chatUpdateSCToontask', [
            taskId,
            toNpcId,
            toonProgress,
            msgIndex])
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
            self.openChatWarning = DirectFrame(parent = aspect2dp, pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.90000000000000002), text = OTPLocalizer.OpenChatWarning, text_wordwrap = 19, text_scale = 0.059999999999999998, text_pos = (0.0, 0.28000000000000003), textMayChange = 0)
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
            if base.cr.productName == 'DisneyOnline-UK':
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
                self.unpaidChatWarning = DirectFrame(parent = aspect2dp, pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.69999999999999996), text = directFrameText, text_wordwrap = 18, text_scale = 0.059999999999999998, text_pos = (0.0, 0.23000000000000001), textMayChange = 0)
                self.payButton = DirectButton(self.unpaidChatWarning, image = buttonImage, relief = None, text = payButtonText, image_scale = (1.75, 1, 1.1499999999999999), text_scale = 0.059999999999999998, text_pos = (0, -0.02), textMayChange = 0, pos = (0.0, 0.0, -0.080000000000000002), command = self._ToontownChatManager__handleUnpaidChatWarningPay)
                DirectButton(self.unpaidChatWarning, image = buttonImage, relief = None, text = directButtonText, textMayChange = 0, image_scale = (1.75, 1, 1.1499999999999999), text_scale = 0.059999999999999998, text_pos = (0, -0.02), pos = (0.0, 0.0, -0.23000000000000001), command = self._ToontownChatManager__handleUnpaidChatWarningContinue)
                guiButton.removeNode()
            
            if base.localAvatar.inTutorial:
                self.payButton.hide()
            else:
                self.payButton.show()
            self.unpaidChatWarning.show()
        elif self.unpaidChatWarning:
            self.unpaidChatWarning.hide()
        
        place = base.cr.playGame.getPlace()
        if place:
            place.fsm.request('stopped')
        
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
            self.noSecretChatAtAll = DirectFrame(parent = aspect2dp, pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.3999999999999999, 1.0, 1.0), text = OTPLocalizer.NoSecretChatAtAll, text_wordwrap = 20, textMayChange = 0, text_scale = 0.059999999999999998, text_pos = (0, 0.25))
            DirectLabel(parent = self.noSecretChatAtAll, relief = None, pos = (0, 0, 0.34999999999999998), text = OTPLocalizer.NoSecretChatAtAllTitle, textMayChange = 0, text_scale = 0.080000000000000002)
            DirectButton(self.noSecretChatAtAll, image = okButtonImage, relief = None, text = OTPLocalizer.NoSecretChatAtAllOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.34999999999999998), command = self._ToontownChatManager__handleNoSecretChatAtAllOK)
            buttons.removeNode()
        
        self.noSecretChatAtAll.show()

    
    def exitNoSecretChatAtAll(self):
        self.noSecretChatAtAll.hide()

    
    def enterNoSecretChatWarning(self, passwordOnly = 0):
        if not passwordOnly:
            warningText = OTPLocalizer.NoSecretChatWarning
        else:
            warningText = OTPLocalizer.ChangeSecretFriendsOptionsWarning
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
            self.noSecretChatWarning = DirectFrame(parent = aspect2dp, pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.3999999999999999, 1.0, 1.0), text = warningText, text_wordwrap = 20, text_scale = 0.055, text_pos = textPos, textMayChange = 1)
            DirectButton(self.noSecretChatWarning, image = okButtonImage, relief = None, text = OTPLocalizer.NoSecretChatWarningOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = okPos, command = okCommand)
            DirectLabel(parent = self.noSecretChatWarning, relief = None, pos = (0, 0, 0.34999999999999998), text = OTPLocalizer.NoSecretChatWarningTitle, textMayChange = 0, text_scale = 0.080000000000000002)
            if base.cr.productName != 'Terra-DMC':
                self.passwordLabel = DirectLabel(parent = self.noSecretChatWarning, relief = None, pos = (-0.070000000000000007, 0.0, -0.20000000000000001), text = OTPLocalizer.ParentPassword, text_scale = 0.059999999999999998, text_align = TextNode.ARight, textMayChange = 0)
                self.passwordEntry = DirectEntry(parent = self.noSecretChatWarning, relief = None, image = nameBalloon, image1_color = (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1.0), scale = 0.064000000000000001, pos = (0.0, 0.0, -0.20000000000000001), width = OTPGlobals.maxLoginWidth, numLines = 1, focus = 1, cursorKeys = 1, obscured = 1, command = self._ToontownChatManager__handleNoSecretChatWarningOK)
                DirectButton(self.noSecretChatWarning, image = cancelButtonImage, relief = None, text = OTPLocalizer.NoSecretChatWarningCancel, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 1, pos = (0.20000000000000001, 0.0, -0.34999999999999998), command = self._ToontownChatManager__handleNoSecretChatWarningCancel)
            
            buttons.removeNode()
            nameBalloon.removeNode()
        else:
            self.noSecretChatWarning['text'] = warningText
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
            nameShopGui = loader.loadModelOnce('phase_3/models/gui/nameshop_gui')
            circle = nameShopGui.find('**/namePanelCircle')
            self.activateChat = DirectFrame(parent = aspect2dp, pos = (0.0, 0.10000000000000001, 0.20000000000000001), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.8, 1.0, 1.6000000000000001), text = OTPLocalizer.ActivateChat, text_align = TextNode.ALeft, text_wordwrap = 33, text_scale = 0.050000000000000003, text_pos = (-0.81999999999999995, 0.57999999999999996), textMayChange = 0)
            innerCircle = circle.copyTo(hidden)
            innerCircle.setPos(0, 0, 0.20000000000000001)
            self.c1b = circle.copyTo(self.activateChat, -1)
            self.c1b.setColor(0, 0, 0, 1)
            self.c1b.setPos(-0.80000000000000004, 0, 0.28999999999999998)
            self.c1b.setScale(0.40000000000000002)
            c1f = circle.copyTo(self.c1b)
            c1f.setColor(1, 1, 1, 1)
            c1f.setScale(0.80000000000000004)
            self.c2b = circle.copyTo(self.activateChat, -2)
            self.c2b.setColor(0, 0, 0, 1)
            self.c2b.setPos(-0.80000000000000004, 0, 0.14000000000000001)
            self.c2b.setScale(0.40000000000000002)
            c2f = circle.copyTo(self.c2b)
            c2f.setColor(1, 1, 1, 1)
            c2f.setScale(0.80000000000000004)
            self.c3b = circle.copyTo(self.activateChat, -2)
            self.c3b.setColor(0, 0, 0, 1)
            self.c3b.setPos(-0.80000000000000004, 0, -0.01)
            self.c3b.setScale(0.40000000000000002)
            c3f = circle.copyTo(self.c3b)
            c3f.setColor(1, 1, 1, 1)
            c3f.setScale(0.80000000000000004)
            DirectLabel(self.activateChat, relief = None, text = OTPLocalizer.ActivateChatTitle, text_align = TextNode.ACenter, text_scale = 0.070000000000000007, text_pos = (0, 0.69999999999999996), textMayChange = 0)
            if base.cr.productName != 'NTT-DMC':
                DirectButton(self.activateChat, image = moreButtonImage, image_scale = (1.25, 1.0, 1.0), relief = None, text = OTPLocalizer.ActivateChatMoreInfo, text_scale = 0.059999999999999998, text_pos = (0, -0.02), textMayChange = 0, pos = (0.0, 0.0, -0.69999999999999996), command = self._ToontownChatManager__handleActivateChatMoreInfo)
            
            self.dcb1 = HackedDirectRadioButton(parent = self.activateChat, relief = None, scale = 0.10000000000000001, boxImage = innerCircle, boxImageScale = 2.5, boxImageColor = VBase4(0, 0.25, 0.5, 1), boxRelief = None, pos = (-0.745, 0, 0.29699999999999999), command = self._ToontownChatManager__updateCheckBoxen, extraArgs = [
                1])
            self.dcb2 = HackedDirectRadioButton(parent = self.activateChat, relief = None, scale = 0.10000000000000001, boxImage = innerCircle, boxImageScale = 2.5, boxImageColor = VBase4(0, 0.25, 0.5, 1), boxRelief = None, pos = (-0.745, 0, 0.14699999999999999), command = self._ToontownChatManager__updateCheckBoxen, extraArgs = [
                2])
            self.dcb3 = HackedDirectRadioButton(parent = self.activateChat, relief = None, scale = 0.10000000000000001, boxImage = innerCircle, boxImageScale = 2.5, boxImageColor = VBase4(0, 0.25, 0.5, 1), boxRelief = None, pos = (-0.745, 0, -0.0030000000000000001), command = self._ToontownChatManager__updateCheckBoxen, extraArgs = [
                3])
            DirectButton(self.activateChat, image = okButtonImage, relief = None, text = OTPLocalizer.ActivateChatYes, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (-0.34999999999999998, 0.0, -0.27000000000000002), command = self._ToontownChatManager__handleActivateChatYes)
            DirectButton(self.activateChat, image = cancelButtonImage, relief = None, text = OTPLocalizer.ActivateChatNo, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.34999999999999998, 0.0, -0.27000000000000002), command = self._ToontownChatManager__handleActivateChatNo)
            guiButton.removeNode()
            buttons.removeNode()
            nameShopGui.removeNode()
            innerCircle.removeNode()
        
        self._ToontownChatManager__initializeCheckBoxen()
        self.activateChat.show()

    
    def _ToontownChatManager__initializeCheckBoxen(self):
        if base.cr.secretChatAllowed and not (base.cr.secretChatNeedsParentPassword):
            self.dcb1['indicatorValue'] = 0
            self.dcb2['indicatorValue'] = 0
            self.dcb3['indicatorValue'] = 1
        elif base.cr.secretChatAllowed and base.cr.secretChatNeedsParentPassword:
            self.dcb1['indicatorValue'] = 0
            self.dcb2['indicatorValue'] = 1
            self.dcb3['indicatorValue'] = 0
        else:
            self.dcb1['indicatorValue'] = 1
            self.dcb2['indicatorValue'] = 0
            self.dcb3['indicatorValue'] = 0

    
    def _ToontownChatManager__updateCheckBoxen(self, value, checkBox):
        if value == 0:
            return None
        
        if checkBox == 1:
            self.dcb2['indicatorValue'] = 0
            self.dcb3['indicatorValue'] = 0
        elif checkBox == 2:
            self.dcb1['indicatorValue'] = 0
            self.dcb3['indicatorValue'] = 0
        else:
            self.dcb1['indicatorValue'] = 0
            self.dcb2['indicatorValue'] = 0

    
    def exitActivateChat(self):
        self.activateChat.hide()

    
    def enterSecretChatActivated(self, mode = 2):
        if mode == 0:
            modeText = OTPLocalizer.SecretChatDeactivated
        elif mode == 1:
            modeText = OTPLocalizer.RestrictedSecretChatActivated
        else:
            modeText = OTPLocalizer.SecretChatActivated
        if self.secretChatActivated == None:
            guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
            optionsButtonImage = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            buttonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.secretChatActivated = DirectFrame(parent = aspect2dp, pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.0, 1.0, 0.80000000000000004), text = modeText, text_align = TextNode.ACenter, text_wordwrap = 14, text_scale = 0.059999999999999998, text_pos = (0, 0.25))
            DirectButton(self.secretChatActivated, image = buttonImage, relief = None, text = OTPLocalizer.SecretChatActivatedOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), textMayChange = 0, pos = (0.0, 0.0, -0.10000000000000001), command = self._ToontownChatManager__handleSecretChatActivatedOK)
            buttons.removeNode()
            guiButton.removeNode()
        else:
            self.secretChatActivated['text'] = modeText
        self.secretChatActivated.show()

    
    def exitSecretChatActivated(self):
        self.secretChatActivated.hide()

    
    def enterProblemActivatingChat(self):
        if self.problemActivatingChat == None:
            buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
            buttonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            self.problemActivatingChat = DirectFrame(parent = aspect2dp, pos = (0.0, 0.10000000000000001, 0.40000000000000002), relief = None, image = getDefaultDialogGeom(), image_color = OTPGlobals.GlobalDialogColor, image_scale = (1.2, 1.0, 0.90000000000000002), text = '', text_align = TextNode.ALeft, text_wordwrap = 18, text_scale = 0.059999999999999998, text_pos = (-0.5, 0.28000000000000003), textMayChange = 1)
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
        elif base.cr.productName == 'NTT-DMC':
            if not base.cr.allowSecretChat():
                self.fsm.request('noSecretChatWarning')
            elif not base.localAvatar.canChat():
                self.fsm.request('openChatWarning')
            else:
                self.fsm.request('normalChat')
        elif base.cr.productName == 'DisneyOnline-UK':
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
        place = base.cr.playGame.getPlace()
        if place:
            place.handleBookClose()
        
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
        if self.dcb1['indicatorValue']:
            base.cr.secretChatAllowed = 0
            mode = 0
        elif self.dcb2['indicatorValue']:
            base.cr.secretChatAllowed = 1
            base.cr.secretChatNeedsParentPassword = 1
            mode = 1
        else:
            base.cr.secretChatAllowed = 1
            base.cr.secretChatNeedsParentPassword = 0
            mode = 2
        (okflag, message) = tt.enableSecretFriends(base.cr.userName, base.cr.password, password)
        if okflag:
            tt.resendPlayToken()
            self.fsm.request('secretChatActivated', [
                mode])
        elif message == None:
            message = 'Parent Password was invalid.'
        
        self.fsm.request('problemActivatingChat')
        self.problemActivatingChat['text'] = OTPLocalizer.ProblemActivatingChat % message

    
    def _ToontownChatManager__handleActivateChatMoreInfo(self):
        self.fsm.request('chatMoreInfo')

    
    def _ToontownChatManager__handleActivateChatNo(self):
        self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleSecretChatActivatedOK(self):
        self.fsm.request('mainMenu')

    
    def _ToontownChatManager__handleSecretChatActivatedChangeOptions(self):
        self.fsm.request('activateChat')

    
    def _ToontownChatManager__handleProblemActivatingChatOK(self):
        self.fsm.request('mainMenu')


