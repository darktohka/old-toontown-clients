# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\chat\TTSCWhiteListTerminal.py
from otp.speedchat.SCTerminal import SCTerminal
from otp.otpbase.OTPLocalizer import SpeedChatStaticText
SCStaticTextMsgEvent = 'SCStaticTextMsg'

def decodeSCStaticTextMsg(textId):
    return SpeedChatStaticText.get(textId, None)


class TTSCWhiteListTerminal(SCTerminal):
    __module__ = __name__

    def __init__(self, textId, parentMenu=None):
        SCTerminal.__init__(self)
        self.parentClass = parentMenu
        self.textId = textId
        self.text = SpeedChatStaticText[self.textId]
        print 'SpeedText %s %s' % (self.textId, self.text)

    def handleSelect(self):
        SCTerminal.handleSelect(self)
        if not self.parentClass.whisperAvatarId:
            base.localAvatar.chatMgr.fsm.request('whiteListOpenChat')
        elif self.parentClass.toPlayer:
            base.localAvatar.chatMgr.fsm.request('whiteListPlayerChat', [self.parentClass.whisperAvatarId])
        else:
            base.localAvatar.chatMgr.fsm.request('whiteListAvatarChat', [self.parentClass.whisperAvatarId])