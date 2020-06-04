# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\chat\TTTalkAssistant.py
import string, sys
from direct.showbase import DirectObject
from otp.otpbase import OTPLocalizer
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPGlobals
from otp.speedchat import SCDecoders
from pandac.PandaModules import *
from otp.chat.ChatGlobals import *
from otp.chat.TalkGlobals import *
from otp.speedchat import SpeedChatGlobals
from otp.chat.TalkMessage import TalkMessage
from otp.chat.TalkAssistant import TalkAssistant
from toontown.speedchat import TTSCDecoders
import time

class TTTalkAssistant(TalkAssistant):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TTTalkAssistant')

    def __init__(self):
        TalkAssistant.__init__(self)

    def clearHistory(self):
        TalkAssistant.clearHistory(self)

    def sendPlayerWhisperToonTaskSpeedChat(self, taskId, toNpcId, toonProgress, msgIndex, receiverId):
        error = None
        base.cr.speedchatRelay.sendSpeedchatToonTask(receiverId, taskId, toNpcId, toonProgress, msgIndex)
        message = TTSCDecoders.decodeTTSCToontaskMsg(taskId, toNpcId, toonProgress, msgIndex)
        if self.logWhispers:
            receiverName = self.findName(receiverId, 1)
            newMessage = TalkMessage(self.countMessage(), self.stampTime(), message, localAvatar.doId, localAvatar.getName(), localAvatar.DISLid, localAvatar.DISLname, None, None, receiverId, receiverName, TALK_ACCOUNT, None)
            self.historyComplete.append(newMessage)
            self.addToHistoryDoId(newMessage, localAvatar.doId)
            self.addToHistoryDISLId(newMessage, base.cr.accountDetailRecord.playerAccountId)
            messenger.send('NewOpenMessage', [newMessage])
        return error

    def sendToonTaskSpeedChat(self, taskId, toNpcId, toonProgress, msgIndex):
        error = None
        messenger.send(SCChatEvent)
        messenger.send('chatUpdateSCToontask', [taskId, toNpcId, toonProgress, msgIndex])
        return error