# File: D (Python 2.2)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleBase import *
from toontown.coghq import DistributedLevelBattle
from direct.directnotify import DirectNotifyGlobal
from toontown.toon import TTEmote
from otp.avatar import Emote
from toontown.battle import SuitBattleGlobals
import whrandom
from toontown.suit import SuitDNA
from direct.fsm import State
from direct.fsm import ClassicFSM
from toontown.toonbase import ToontownGlobals

class DistributedMintBattle(DistributedLevelBattle.DistributedLevelBattle):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMintBattle')
    
    def __init__(self, cr):
        DistributedLevelBattle.DistributedLevelBattle.__init__(self, cr)
        self.fsm.addState(State.State('MintReward', self.enterMintReward, self.exitMintReward, [
            'Resume']))
        offState = self.fsm.getStateNamed('Off')
        offState.addTransition('MintReward')
        playMovieState = self.fsm.getStateNamed('PlayMovie')
        playMovieState.addTransition('MintReward')

    
    def enterMintReward(self, ts):
        self.notify.info('enterMintReward()')
        self.disableCollision()
        self.delayDeleteMembers()
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
            if self.bossBattle:
                messenger.send('localToonConfrontedMintBoss')
            
        
        self.movie.playReward(ts, self.uniqueName('building-reward'), self._DistributedMintBattle__handleMintRewardDone)

    
    def _DistributedMintBattle__handleMintRewardDone(self):
        self.notify.info('mint reward done')
        if self.hasLocalToon():
            self.d_rewardDone(base.localAvatar.doId)
        
        self.movie.resetReward()
        self.fsm.request('Resume')

    
    def exitMintReward(self):
        self.notify.info('exitMintReward()')
        self.movie.resetReward(finish = 1)
        self.membersKeep = None
        NametagGlobals.setMasterArrowsOn(1)


