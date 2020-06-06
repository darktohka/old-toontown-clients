# File: S (Python 2.2)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.suit import DistributedSellbotBoss
from direct.directnotify import DirectNotifyGlobal
from toontown.coghq import CogHQBossBattle

class SellbotHQBossBattle(CogHQBossBattle.CogHQBossBattle):
    notify = DirectNotifyGlobal.directNotify.newCategory('SellbotHQBossBattle')
    
    def __init__(self, loader, parentFSM, doneEvent):
        CogHQBossBattle.CogHQBossBattle.__init__(self, loader, parentFSM, doneEvent)
        self.teleportInPosHpr = (0, 95, 18, 180, 0, 0)

    
    def load(self):
        CogHQBossBattle.CogHQBossBattle.load(self)

    
    def unload(self):
        CogHQBossBattle.CogHQBossBattle.unload(self)

    
    def enter(self, requestStatus):
        CogHQBossBattle.CogHQBossBattle.enter(self, requestStatus, DistributedSellbotBoss.OneBossCog)
        self._SellbotHQBossBattle__setupHighSky()

    
    def exit(self):
        CogHQBossBattle.CogHQBossBattle.exit(self)
        self._SellbotHQBossBattle__cleanupHighSky()

    
    def _SellbotHQBossBattle__setupHighSky(self):
        self.loader.hood.startSky()
        sky = self.loader.hood.sky
        sky.setH(150)
        sky.setZ(-100)

    
    def _SellbotHQBossBattle__cleanupHighSky(self):
        self.loader.hood.stopSky()
        sky = self.loader.hood.sky
        sky.setH(0)
        sky.setZ(0)


