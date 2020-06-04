# File: D (Python 2.2)

import DistributedBattle
import DirectNotifyGlobal

class DistributedBattleTutorial(DistributedBattle.DistributedBattle):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBattleTutorial')
    
    def startTimer(self, ts = 0):
        self.townBattle.timer.hide()

    
    def playReward(self, ts):
        self.movie.playTutorialReward(ts, self.uniqueName('reward'), self.handleRewardDone)


