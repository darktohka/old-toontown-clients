# File: D (Python 2.2)


class DropScheduler:
    
    def __init__(self, gameDuration, firstDropDelay, dropPeriod, maxDropDuration, fasterDropDelay, fasterDropPeriodMult):
        self.gameDuration = gameDuration
        self.firstDropDelay = firstDropDelay
        self._DropScheduler__dropPeriod = dropPeriod
        self.maxDropDuration = maxDropDuration
        self.fasterDropDelay = fasterDropDelay
        self.fasterDropPeriodMult = fasterDropPeriodMult
        self.curT = self.firstDropDelay

    
    def getT(self):
        return self.curT

    
    def getDropPeriod(self):
        delay = self._DropScheduler__dropPeriod
        if self.curT >= self.fasterDropDelay:
            delay *= self.fasterDropPeriodMult
        
        return delay

    
    def doneDropping(self):
        landTime = self.getT() + self.maxDropDuration
        return landTime >= self.gameDuration + self.getDropPeriod()

    
    def stepT(self):
        self.curT += self.getDropPeriod()


