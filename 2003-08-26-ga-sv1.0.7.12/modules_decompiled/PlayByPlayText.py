# File: P (Python 2.2)

from DirectObject import *
from ShowBaseGlobal import *
from ToontownBattleGlobals import *
from ToontownGlobals import *
from SuitBattleGlobals import *
from IntervalGlobal import *
import DirectNotifyGlobal
import string
import OnscreenText
import BattleBase

class PlayByPlayText(OnscreenText.OnscreenText):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayByPlayText')
    
    def __init__(self):
        OnscreenText.OnscreenText.__init__(self, mayChange = 1, pos = (0.0, 0.75), scale = 0.20000000000000001, fg = (1, 0, 0, 1), font = getSignFont(), wordwrap = 13)
        return None

    
    def getShowInterval(self, text, duration):
        return Sequence(Func(self.hide), Wait(duration * 0.29999999999999999), Func(self.setText, text), Func(self.show), Wait(duration * 0.69999999999999996), Func(self.hide))

    
    def getToonsDiedInterval(self, textList, duration):
        track = Sequence(Func(self.hide), Wait(duration * 0.29999999999999999))
        waitGap = (0.59999999999999998 / len(textList)) * duration
        for text in textList:
            newList = [
                Func(self.setText, text),
                Func(self.show),
                Wait(waitGap),
                Func(self.hide)]
            track += newList
        
        track.append(Wait(duration * 0.10000000000000001))
        return track


