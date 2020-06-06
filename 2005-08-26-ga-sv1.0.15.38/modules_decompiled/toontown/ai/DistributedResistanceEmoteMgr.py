# File: D (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.interval.IntervalGlobal import *
from otp.speedchat import SpeedChatGlobals
from otp.otpbase.OTPLocalizerEnglish import EmoteFuncDict
RESIST_INDEX = EmoteFuncDict['Resistance Salute']

class DistributedResistanceEmoteMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedResistanceEmoteMgr')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        
        def phraseSaid(phraseId):
            helpPhrase = 513
            if phraseId == helpPhrase:
                self.addResistanceEmote()
            

        self.accept(SpeedChatGlobals.SCStaticTextMsgEvent, phraseSaid)

    
    def announceGenerate(self):
        DistributedResistanceEmoteMgr.notify.debug('announceGenerate')

    
    def delete(self):
        self.ignore(SpeedChatGlobals.SCStaticTextMsgEvent)

    
    def addResistanceEmote(self):
        DistributedResistanceEmoteMgr.notify.debug('addResitanceEmote')
        av = base.localAvatar
        if not av.emoteAccess[RESIST_INDEX]:
            self.sendUpdate('addResistanceEmote', [])
            msgTrack = Sequence(Wait(1), Func(av.setSystemMessage, 0, 'Whispering Willow: Welcome to the Resistance!'), Wait(3), Func(av.setSystemMessage, 0, 'Whispering Willow: Use your new emote to identify yourself to other members.'), Wait(4), Func(av.setSystemMessage, 0, 'Whispering Willow: Good luck!'))
            msgTrack.start()
        


