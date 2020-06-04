# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\chat\TalkHandle.py
from otp.avatar.AvatarHandle import AvatarHandle

class TalkHandle(AvatarHandle):
    __module__ = __name__

    def __init__(self, doId, message):
        self.avatarId = doId
        self.avatarName = None
        self.accountId = None
        self.accountName = None
        self.addMessageInfo(message)
        return

    def getName(self):
        return self.avatarName

    def isUnderstandable(self):
        return False

    def isOnline(self):
        return False

    def addMessageInfo(self, message):
        if self.avatarId == message.getSenderAvatarId():
            if not self.avatarName and message.getSenderAvatarName():
                self.avatarName = message.getSenderAvatarName()
            if not self.accountId and message.getSenderAccountId():
                self.accountId = message.getSenderAccountId()
            if not self.accountName and message.getSenderAccountName():
                self.accountName = message.getSenderAccountName()
        elif self.avatarId == message.getReceiverAvatarId():
            if not self.avatarName and message.getReceiverAvatarName():
                self.avatarName = message.getReceiverAvatarName()
            if not self.accountId and message.getReceiverAccountId():
                self.accountId = message.getReceiverAccountId()
            if not self.accountName and message.getReceiverAccountName():
                self.accountName = message.getReceiverAccountName()

    def setTalkWhisper(self, fromAV, fromAC, avatarName, chat, mods, flags):
        (newText, scrubbed) = localAvatar.scrubTalk(chat, mods)
        base.talkAssistant.receiveWhisperTalk(fromAV, avatarName, fromAC, None, self.avatarId, self.getName(), newText, scrubbed)
        return