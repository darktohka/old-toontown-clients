# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\ai\DistributedPolarPlaceEffectMgr.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.interval.IntervalGlobal import *
from otp.speedchat import SpeedChatGlobals
from toontown.toonbase import TTLocalizer

class DistributedPolarPlaceEffectMgr(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPolarPlaceEffectMgr')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

        def phraseSaid(phraseId):
            helpPhrase = 104
            if phraseId == helpPhrase:
                self.addPolarPlaceEffect()

        self.accept(SpeedChatGlobals.SCStaticTextMsgEvent, phraseSaid)

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        DistributedPolarPlaceEffectMgr.notify.debug('announceGenerate')

    def delete(self):
        self.ignore(SpeedChatGlobals.SCStaticTextMsgEvent)
        DistributedObject.DistributedObject.delete(self)

    def addPolarPlaceEffect(self):
        DistributedPolarPlaceEffectMgr.notify.debug('addResitanceEffect')
        av = base.localAvatar
        self.sendUpdate('addPolarPlaceEffect', [])
        msgTrack = Sequence(Func(av.setSystemMessage, 0, TTLocalizer.PolarPlaceEffect1), Wait(2), Func(av.setSystemMessage, 0, TTLocalizer.PolarPlaceEffect2), Wait(4), Func(av.setSystemMessage, 0, TTLocalizer.PolarPlaceEffect3))
        msgTrack.start()