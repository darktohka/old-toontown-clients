# File: P (Python 2.2)

from DirectObject import *
from ShowBaseGlobal import *
from ToontownBattleGlobals import *
from ToontownGlobals import *
from SuitBattleGlobals import *
import DirectNotifyGlobal
import OnscreenText

class PlayByPlayText(OnscreenText.OnscreenText):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayByPlayText')
    
    def __init__(self):
        OnscreenText.OnscreenText.__init__(self, mayChange = 1, pos = (0.0, 0.75), scale = 0.10000000000000001, font = getSignFont())
        return None


