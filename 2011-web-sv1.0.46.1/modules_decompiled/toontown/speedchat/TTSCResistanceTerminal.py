# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\speedchat\TTSCResistanceTerminal.py
from otp.speedchat.SCTerminal import SCTerminal
from toontown.chat import ResistanceChat
TTSCResistanceMsgEvent = 'TTSCResistanceMsg'

def decodeTTSCResistanceMsg(textId):
    return ResistanceChat.getChatText(textId)


class TTSCResistanceTerminal(SCTerminal):
    __module__ = __name__

    def __init__(self, textId, charges):
        SCTerminal.__init__(self)
        self.setCharges(charges)
        self.textId = textId
        self.text = ResistanceChat.getItemText(self.textId)

    def isWhisperable(self):
        return False

    def handleSelect(self):
        SCTerminal.handleSelect(self)
        messenger.send(self.getEventName(TTSCResistanceMsgEvent), [
         self.textId])