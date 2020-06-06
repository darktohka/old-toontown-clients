# File: P (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from otp.otpbase.OTPGlobals import *
from direct.showbase.DirectObject import *
from direct.gui.DirectGui import *
from MultiPageTextFrame import *
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPLocalizer
from otp.otpgui import OTPDialog

class PrivacyPolicyTextPanel(getGlobalDialogClass()):
    notify = DirectNotifyGlobal.directNotify.newCategory('PrivacyPolicyTextPanel')
    
    def __init__(self, doneEvent, hidePageNum = 0, pageChangeCallback = None, textList = []):
        dialogClass = getGlobalDialogClass()
        dialogClass.__init__(self, parent = aspect2d, dialogName = 'privacyPolicyTextDialog', doneEvent = doneEvent, okButtonText = OTPLocalizer.PrivacyPolicyClose, style = OTPDialog.Acknowledge, text = '', topPad = 1.5, sidePad = 1.2, pos = (0, 0, -0.55000000000000004), scale = 0.90000000000000002)
        self.privacyPolicyText = MultiPageTextFrame(parent = self, textList = textList, hidePageNum = hidePageNum, pageChangeCallback = pageChangeCallback, pos = (0, 0, 0.69999999999999996), width = 2.3999999999999999, height = 1.5)
        self['image'] = self['image']
        self['image_pos'] = (0, 0, 0.65000000000000002)
        self['image_scale'] = (2.7000000000000002, 1, 1.8999999999999999)
        closeButton = self.getChild(0)
        closeButton.setZ(-0.13)



class PrivacyPolicyPanel(getGlobalDialogClass()):
    notify = DirectNotifyGlobal.directNotify.newCategory('PrivacyPolicyPanel')
    
    def __init__(self, doneEvent, hidePageNum = 0, pageChangeCallback = None, textList = 1):
        dialogClass = getGlobalDialogClass()
        dialogClass.__init__(self, parent = aspect2d, dialogName = 'privacyPolicyDialog', doneEvent = doneEvent, okButtonText = OTPLocalizer.PrivacyPolicyClose, style = OTPDialog.Acknowledge, text = '', topPad = 1.5, sidePad = 1.2, pos = (0, 0, -0.14999999999999999), scale = 0.59999999999999998)
        self.chatPrivacyPolicy = None
        self.fsm = ClassicFSM.ClassicFSM('privacyPolicyPanel', [
            State.State('off', self.enterOff, self.exitOff),
            State.State('version1Adult', self.enterVersion1Adult, self.exitPrivacyPolicy),
            State.State('version1Kids', self.enterVersion1Kids, self.exitPrivacyPolicy),
            State.State('version2Adult', self.enterVersion2Adult, self.exitPrivacyPolicy),
            State.State('version2Kids', self.enterVersion2Kids, self.exitPrivacyPolicy)], 'off', 'off')
        self.fsm.enterInitialState()
        guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
        moreButtonImage = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
        DirectFrame(self, pos = (-0.40000000000000002, 0.10000000000000001, 0.40000000000000002), relief = None, text = OTPLocalizer.PrivacyPolicyText_Intro, text_align = TextNode.ALeft, text_wordwrap = 28, text_scale = 0.089999999999999997, text_pos = (-0.81999999999999995, 1.0), textMayChange = 0)
        textScale = 0.050000000000000003
        buttonFrame = DirectFrame(self, pos = (0.0, 0.10000000000000001, 0.0), scale = 1.3999999999999999, relief = None)
        DirectButton(buttonFrame, image = moreButtonImage, image_scale = (1.75, 1.0, 1.0), relief = None, text = OTPLocalizer.ActivateChatPrivacyPolicy_Button1A, text_scale = textScale, text_pos = (0, -0.01), textMayChange = 0, pos = (-0.45000000000000001, 0.0, 0.40000000000000002), command = self._PrivacyPolicyPanel__handlePrivacyPolicy, extraArgs = [
            'version1Adult'])
        DirectButton(buttonFrame, image = moreButtonImage, image_scale = (1.75, 1.0, 1.0), relief = None, text = OTPLocalizer.ActivateChatPrivacyPolicy_Button1K, text_scale = textScale, text_pos = (0, -0.01), textMayChange = 0, pos = (-0.45000000000000001, 0.0, 0.20000000000000001), command = self._PrivacyPolicyPanel__handlePrivacyPolicy, extraArgs = [
            'version1Kids'])
        DirectButton(buttonFrame, image = moreButtonImage, image_scale = (1.75, 1.0, 1.0), relief = None, text = OTPLocalizer.ActivateChatPrivacyPolicy_Button2A, text_scale = textScale, text_pos = (0, -0.01), textMayChange = 0, pos = (0.45000000000000001, 0.0, 0.40000000000000002), command = self._PrivacyPolicyPanel__handlePrivacyPolicy, extraArgs = [
            'version2Adult'])
        DirectButton(buttonFrame, image = moreButtonImage, image_scale = (1.75, 1.0, 1.0), relief = None, text = OTPLocalizer.ActivateChatPrivacyPolicy_Button2K, text_scale = textScale, text_pos = (0, -0.01), textMayChange = 0, pos = (0.45000000000000001, 0.0, 0.20000000000000001), command = self._PrivacyPolicyPanel__handlePrivacyPolicy, extraArgs = [
            'version2Kids'])
        self['image'] = self['image']
        self['image_pos'] = (0, 0, 0.65000000000000002)
        self['image_scale'] = (2.7000000000000002, 1, 1.8999999999999999)
        closeButton = self.getChild(0)
        closeButton.setZ(-0.13)

    
    def delete(self):
        self.ignoreAll()
        del self.fsm
        if self.chatPrivacyPolicy:
            self.chatPrivacyPolicy.destroy()
            self.chatPrivacyPolicy = None
        

    
    def _PrivacyPolicyPanel__handlePrivacyPolicy(self, state, *oooo):
        self.fsm.request(state)

    
    def _PrivacyPolicyPanel__privacyPolicyTextDone(self):
        self.exitPrivacyPolicy()

    
    def enterPrivacyPolicy(self, textList):
        if self.chatPrivacyPolicy == None:
            self.chatPrivacyPolicy = PrivacyPolicyTextPanel('privacyPolicyTextDone', textList = textList)
        
        self.chatPrivacyPolicy.show()
        self.acceptOnce('privacyPolicyTextDone', self._PrivacyPolicyPanel__privacyPolicyTextDone)

    
    def exitPrivacyPolicy(self):
        self.ignore('privacyPolicyTextDone')
        if self.chatPrivacyPolicy:
            cleanupDialog('privacyPolicyTextDialog')
            self.chatPrivacyPolicy = None
        

    
    def enterVersion1Adult(self):
        self.enterPrivacyPolicy(OTPLocalizer.PrivacyPolicyText_1A)

    
    def enterVersion1Kids(self):
        self.enterPrivacyPolicy(OTPLocalizer.PrivacyPolicyText_1K)

    
    def enterVersion2Adult(self):
        self.enterPrivacyPolicy(OTPLocalizer.PrivacyPolicyText_2A)

    
    def enterVersion2Kids(self):
        self.enterPrivacyPolicy(OTPLocalizer.PrivacyPolicyText_2K)

    
    def enterOff(self):
        self.ignoreAll()
        self.exitPrivacyPolicy()

    
    def exitOff(self):
        pass


