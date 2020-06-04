# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\ai\DistributedResistanceEmoteMgr.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.interval.IntervalGlobal import *
from otp.speedchat import SpeedChatGlobals
from otp.otpbase.OTPLocalizerEnglish import EmoteFuncDict
from toontown.toonbase import TTLocalizer
RESIST_INDEX = EmoteFuncDict['Resistance Salute']

class DistributedResistanceEmoteMgr(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedResistanceEmoteMgr')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

        def phraseSaid(phraseId):
            helpPhrase = 513
            if phraseId == helpPhrase:
                self.addResistanceEmote()

        self.accept(SpeedChatGlobals.SCStaticTextMsgEvent, phraseSaid)

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        DistributedResistanceEmoteMgr.notify.debug('announceGenerate')

    def delete(self):
        self.ignore(SpeedChatGlobals.SCStaticTextMsgEvent)
        DistributedObject.DistributedObject.delete(self)

    def addResistanceEmote(self):
        DistributedResistanceEmoteMgr.notify.debug('addResitanceEmote')
        av = base.localAvatar
        if not av.emoteAccess[RESIST_INDEX]:
            self.sendUpdate('addResistanceEmote', [])
            msgTrack = Sequence(Wait(1), Func(av.setSystemMessage, 0, TTLocalizer.ResistanceEmote1), Wait(3), Func(av.setSystemMessage, 0, TTLocalizer.ResistanceEmote2), Wait(4), Func(av.setSystemMessage, 0, TTLocalizer.ResistanceEmote3))
            msgTrack.start()