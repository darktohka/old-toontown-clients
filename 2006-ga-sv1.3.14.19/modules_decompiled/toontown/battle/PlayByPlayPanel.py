# File: P (Python 2.2)

from direct.showbase.DirectObject import *
from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownBattleGlobals import *
from toontown.toonbase.ToontownGlobals import *
from SuitBattleGlobals import *
from direct.directnotify import DirectNotifyGlobal
from direct.gui import OnscreenText

class PlayByPlayText(OnscreenText.OnscreenText):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayByPlayText')
    
    def __init__(self):
        OnscreenText.OnscreenText.__init__(self, mayChange = 1, pos = (0.0, 0.75), scale = 0.10000000000000001, font = getSignFont())


