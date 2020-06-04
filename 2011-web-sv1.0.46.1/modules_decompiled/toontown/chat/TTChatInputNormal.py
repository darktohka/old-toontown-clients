# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\chat\TTChatInputNormal.py
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from otp.chat import ChatInputNormal
from otp.otpbase import OTPLocalizer
from otp.otpbase import OTPGlobals

class TTChatInputNormal(ChatInputNormal.ChatInputNormal):
    __module__ = __name__

    def __init__(self, chatMgr):
        ChatInputNormal.ChatInputNormal.__init__(self, chatMgr)
        gui = loader.loadModel('phase_3.5/models/gui/chat_input_gui')
        self.chatFrame = DirectFrame(parent=aspect2dp, image=gui.find('**/Chat_Bx_FNL'), relief=None, pos=(-1.083,
                                                                                                           0,
                                                                                                           0.804), state=DGG.NORMAL, sortOrder=DGG.FOREGROUND_SORT_INDEX)
        self.chatFrame.hide()
        self.chatButton = DirectButton(parent=self.chatFrame, image=(gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos=(0.182, 0, -0.088), relief=None, text=('', OTPLocalizer.ChatInputNormalSayIt, OTPLocalizer.ChatInputNormalSayIt), text_scale=0.06, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.09), textMayChange=0, command=self.chatButtonPressed)
        self.cancelButton = DirectButton(parent=self.chatFrame, image=(gui.find('**/CloseBtn_UP'), gui.find('**/CloseBtn_DN'), gui.find('**/CloseBtn_Rllvr')), pos=(-0.151, 0, -0.088), relief=None, text=('', OTPLocalizer.ChatInputNormalCancel, OTPLocalizer.ChatInputNormalCancel), text_scale=0.06, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.09), textMayChange=0, command=self.cancelButtonPressed)
        self.whisperLabel = DirectLabel(parent=self.chatFrame, pos=(0.02, 0, 0.23), relief=DGG.FLAT, frameColor=(1,
                                                                                                                 1,
                                                                                                                 0.5,
                                                                                                                 1), frameSize=(-0.23, 0.23, -0.07, 0.05), text=OTPLocalizer.ChatInputNormalWhisper, text_scale=0.04, text_fg=Vec4(0, 0, 0, 1), text_wordwrap=9.5, textMayChange=1)
        self.whisperLabel.hide()
        self.chatEntry = DirectEntry(parent=self.chatFrame, relief=None, scale=0.05, pos=(-0.2, 0, 0.11), entryFont=OTPGlobals.getInterfaceFont(), width=8.6, numLines=3, cursorKeys=0, backgroundFocus=0, command=self.sendChat)
        self.chatEntry.bind(DGG.OVERFLOW, self.chatOverflow)
        self.chatEntry.bind(DGG.TYPE, self.typeCallback)
        return

    def delete(self):
        self.chatEntry.destroy()
        self.chatButton.destroy()
        self.cancelButton.destroy()
        ChatInputNormal.ChatInputNormal.delete(self)
        loader.unloadModel('phase_3.5/models/gui/chat_input_gui')

    def importExecNamespace(self):
        ChatInputNormal.ChatInputNormal.importExecNamespace(self)
        exec 'from toontown.toonbase.ToonBaseGlobal import *' in globals(), self.ExecNamespace

    def typeCallback(self, extraArgs):
        if localAvatar.chatMgr.chatInputWhiteList.isActive():
            return
        else:
            messenger.send('enterNormalChat')

    def checkForOverRide(self):
        return False
        if localAvatar.chatMgr.chatInputWhiteList.isActive():
            return True
        return False