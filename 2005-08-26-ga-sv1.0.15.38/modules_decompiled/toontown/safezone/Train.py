# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase.PandaObject import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from pandac import NodePath
from direct.directutil import Mopath
from toontown.toonbase import ToontownGlobals
from direct.actor import Actor

class Train(PandaObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('Train')
    nameId = 0
    Sfx_TrainPass = 'phase_10/audio/sfx/CBHQ_TRAIN_pass.mp3'
    Sfx_TrainStopStart = 'phase_10/audio/sfx/CBHQ_TRAIN_stopstart.mp3'
    LocomotiveFile = 'phase_10/models/cogHQ/CashBotLocomotive'
    CarFiles = [
        'phase_10/models/cogHQ/CashBotBoxCar',
        'phase_10/models/cogHQ/CashBotTankCar',
        'phase_10/models/cogHQ/CashBotFlatCar']
    CarLength = 88
    MarkDelta = 15
    
    def __init__(self, trackStartPos, trackEndPos, trackNum, numTotalTracks):
        self.trackStartPos = trackStartPos
        self.trackEndPos = trackEndPos
        self.numCars = len(self.CarFiles)
        self.locomotive = loader.loadModelCopy(self.LocomotiveFile)
        self.cars = []
        self.trainPassingSfx = base.loadSfx(self.Sfx_TrainPass)
        self.trainStopStartSfx = base.loadSfx(self.Sfx_TrainStopStart)
        self.trainId = trackNum
        self.bFlipped = False
        if trackStartPos[0] < trackEndPos[0]:
            self.locomotive.setHpr(180, 0, 0)
            self.bFlipped = True
        
        self.collNodeName = 'CollNode-%s' % self.trainId
        self.firstMark = (self.MarkDelta / numTotalTracks) * trackNum
        currentTime = self._Train__networkTimeInSeconds()
        currentRun = int((currentTime - self.firstMark) / self.MarkDelta)
        self.lastMark = currentRun * self.MarkDelta + self.firstMark
        self.doNextRun(True)
        self.hide()

    
    def hide(self):
        if self.locomotive:
            self.locomotive.reparentTo(hidden)
        

    
    def show(self):
        if self.locomotive:
            self.locomotive.reparentTo(render)
        

    
    def _Train__networkTimeInSeconds(self):
        time = globalClockDelta.getRealNetworkTime(bits = 32) / NetworkTimePrecision
        return time

    
    def doNextRun(self, bFirstRun = False):
        if self.locomotive:
            if bFirstRun:
                nextMark = self.lastMark
            else:
                nextMark = self.lastMark + self.MarkDelta
                self.nextRun.finish()
            self.notify.debug('Next mark %s' % nextMark)
            currentTime = self._Train__networkTimeInSeconds()
            timeTillNextMark = nextMark - currentTime
            self.notify.debug('Time diff %s' % timeTillNextMark)
            runNumber = int((nextMark - self.firstMark) / self.MarkDelta)
            S = random.getstate()
            random.seed(self.trainId + runNumber)
            self.nextRun = self._Train__getNextRun()
            random.setstate(S)
            self._Train__startNextRun(timeTillNextMark)
            self.lastMark = nextMark
        
        return Task.done

    
    def _Train__startNextRun(self, timeTillMark):
        if self.locomotive:
            self._Train__disableCollisions()
            if timeTillMark > 0:
                self.nextRun = Sequence(Wait(timeTillMark), self.nextRun)
                self.nextRun.start()
            else:
                self.nextRun.start(-1 * timeTillMark)
            self._Train__enableCollisions()
        
        return Task.done

    
    def _Train__cleanupCars(self):
        self._Train__disableCollisions()
        for car in self.cars:
            car.removeNode()
        
        self.cars = []

    
    def _Train__getCars(self):
        self._Train__cleanupCars()
        numCarsThisRun = random.randrange(1, 10)
        for nCar in range(numCarsThisRun):
            carType = random.randrange(0, self.numCars)
            car = loader.loadModelCopy(self.CarFiles[carType])
            car.reparentTo(self.locomotive)
            car.setPos(self.CarLength * (nCar + 1), 0, 0)
            self.cars.append(car)
        

    
    def _Train__showStart(self):
        self.notify.debug('Starting train %s at %s.' % (self.trainId, self._Train__networkTimeInSeconds()))

    
    def _Train__getNextRun(self):
        self._Train__getCars()
        trainShouldStop = random.randrange(0, 4)
        nextRun = Sequence(Func(self._Train__showStart))
        if trainShouldStop is 0:
            waitTime = 3
            totalTime = random.randrange(4, (self.MarkDelta - waitTime) / 2)
            sfxStopTime = 4.2999999999999998
            halfway = (self.trackStartPos + self.trackEndPos) / 2
            halfway.setX(150)
            nextRun.append(Parallel(Sequence(Wait(totalTime - sfxStopTime), SoundInterval(self.trainStopStartSfx, volume = 0.5)), Sequence(LerpPosInterval(self.locomotive, totalTime, halfway, self.trackStartPos, blendType = 'easeInOut'), WaitInterval(waitTime), LerpPosInterval(self.locomotive, totalTime, self.trackEndPos, halfway, blendType = 'easeIn'))))
        else:
            totalTime = random.randrange(6, self.MarkDelta - 1)
            sfxTime = 7
            sfxStartTime = totalTime / 2 - sfxTime / 2
            if self.bFlipped:
                sfxStartTime -= 1
            else:
                sfxStartTime += 1
            nextRun.append(Parallel(Sequence(Wait(sfxStartTime), SoundInterval(self.trainPassingSfx, volume = 0.5)), LerpPosInterval(self.locomotive, totalTime, self.trackEndPos, self.trackStartPos)))
        nextRun.append(Func(self.doNextRun))
        return nextRun

    
    def delete(self):
        self._Train__cleanupCars()
        self.locomotive.removeNode()
        self.locomotive = None
        self.nextRun.finish()
        self.nextRun = None
        del self.trainPassingSfx
        del self.trainStopStartSfx

    
    def uniqueName(self, name):
        Train.nameId += 1
        return name + '-%d' % Train.nameId

    
    def _Train__enableCollisions(self):
        allColls = self.locomotive.findAllMatches('**/+CollisionNode').asList()
        for car in self.cars:
            carColls = car.findAllMatches('**/+CollisionNode').asList()
            allColls += carColls
        
        for collNode in allColls:
            collNode.setName(self.collNodeName)
            collNode.setCollideMask(ToontownGlobals.WallBitmask)
        
        self.accept('enter' + self.collNodeName, self._Train__handleCollisionSphereEnter)

    
    def _Train__disableCollisions(self):
        self.ignore('enter' + self.collNodeName)

    
    def _Train__handleCollisionSphereEnter(self, collEntry = None):
        base.localAvatar.b_squish(10)


