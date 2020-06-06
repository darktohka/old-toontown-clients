# File: D (Python 2.2)

from DirectGui import *
from ToontownGlobals import *
from ToonBaseGlobal import *
from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
import ToontownGlobals
import DistributedFurnitureItem
import Localizer
import CollisionSphere
import CollisionNode
import BankGUI
from BankGlobals import *
import ToontownDialog

class DistributedBank(DistributedFurnitureItem.DistributedFurnitureItem):
    notify = directNotify.newCategory('DistributedBank')
    notify.setDebug(1)
    
    def __init__(self, cr):
        DistributedFurnitureItem.DistributedFurnitureItem.__init__(self, cr)
        self.bankGui = None
        self.bankDialog = None

    
    def generate(self):
        DistributedFurnitureItem.DistributedFurnitureItem.generate(self)
        self.bankSphereEvent = 'bankSphere'
        self.bankSphereEnterEvent = 'enter' + self.bankSphereEvent
        self.bankGuiDoneEvent = 'bankGuiDone'

    
    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        self.accept(self.bankSphereEnterEvent, self._DistributedBank__handleEnterSphere)

    
    def disable(self):
        self.notify.debug('disable')
        self.ignore(self.bankSphereEnterEvent)
        self.ignore(self.bankGuiDoneEvent)
        if self.bankGui:
            self.bankGui.destroy()
            self.bankGui = None
        
        if self.bankDialog:
            self.bankDialog.cleanup()
            self.bankDialog = None
        
        DistributedFurnitureItem.DistributedFurnitureItem.disable(self)

    
    def delete(self):
        self.notify.debug('delete')
        DistributedFurnitureItem.DistributedFurnitureItem.delete(self)

    
    def _DistributedBank__handleEnterSphere(self, collEntry):
        self.notify.debug('Entering Bank Sphere....')
        self.ignore(self.bankSphereEnterEvent)
        self.cr.playGame.getPlace().detectedBankCollision()
        self.sendUpdate('avatarEnter', [])

    
    def _DistributedBank__handleBankDone(self, transactionAmount):
        self.sendUpdate('transferMoney', [
            transactionAmount])
        self.ignore(self.bankGuiDoneEvent)
        self.bankGui.destroy()
        self.bankGui = None

    
    def freeAvatar(self):
        toonbase.localToon.posCamera(0, 0)
        toonbase.tcr.playGame.getPlace().setState('walk')
        self.accept(self.bankSphereEnterEvent, self._DistributedBank__handleEnterSphere)

    
    def showBankGui(self):
        self.bankGui = BankGUI.BankGui(self.bankGuiDoneEvent)
        self.accept(self.bankGuiDoneEvent, self._DistributedBank__handleBankDone)

    
    def setMovie(self, mode, avId, timestamp):
        timeStamp = globalClockDelta.localElapsedTime(timestamp)
        isLocalToon = avId == toonbase.localToon.doId
        self.notify.info('setMovie: %s %s %s %s' % (mode, avId, timeStamp, isLocalToon))
        if mode == BANK_MOVIE_CLEAR:
            self.notify.debug('setMovie: clear')
            return None
        elif mode == BANK_MOVIE_GUI:
            self.notify.debug('setMovie: gui')
            track = Sequence()
            track.append(Func(self._DistributedBank__takeOutToonJar, avId))
            if isLocalToon:
                track.append(Wait(3.0))
                track.append(Func(self.showBankGui))
            
            track.play()
            return None
        elif mode == BANK_MOVIE_DEPOSIT:
            self.notify.debug('setMovie: deposit')
            self._DistributedBank__putAwayToonJar(avId)
            return None
        elif mode == BANK_MOVIE_WITHDRAW:
            self.notify.debug('setMovie: withdraw')
            self._DistributedBank__putAwayToonJar(avId)
            return None
        elif mode == BANK_MOVIE_NO_OP:
            self.notify.debug('setMovie: no op')
            self._DistributedBank__putAwayToonJar(avId)
            return None
        elif mode == BANK_MOVIE_NOT_OWNER:
            self.notify.debug('setMovie: not owner')
            if isLocalToon:
                self.bankDialog = ToontownDialog.ToontownDialog(dialogName = 'BankNotOwner', style = ToontownDialog.Acknowledge, text = Localizer.DistributedBankNotOwner, text_wordwrap = 15, fadeScreen = 1, command = self._DistributedBank__clearDialog)
            
            return None
        elif mode == BANK_MOVIE_NO_OWNER:
            self.notify.debug('setMovie: no owner')
            if isLocalToon:
                self.bankDialog = ToontownDialog.ToontownDialog(dialogName = 'BankNoOwner', style = ToontownDialog.Acknowledge, text = Localizer.DistributedBankNoOwner, text_wordwrap = 15, fadeScreen = 1, command = self._DistributedBank__clearDialog)
            
            return None
        else:
            self.notify.warning('unknown mode in setMovie: %s' % mode)

    
    def _DistributedBank__clearDialog(self, event):
        self.bankDialog.cleanup()
        self.bankDialog = None
        self.freeAvatar()

    
    def _DistributedBank__takeOutToonJar(self, avId):
        toon = toonbase.tcr.doId2do[avId]
        track = Sequence()
        walkToBank = Sequence(Func(toon.stopSmooth), Func(toon.loop, 'walk'), toon.posHprInterval(0.5, Point3(0, -3.125, 0), Point3(0, 0, 0), other = self, blendType = 'easeInOut'), Func(toon.loop, 'neutral'), Func(toon.startSmooth))
        track.append(walkToBank)
        toon.jar = loader.loadModelOnce('phase_5.5/models/estate/jellybeanJar')
        toon.jar.setP(290.0)
        toon.jar.setY(0.5)
        toon.jar.setZ(0.5)
        toon.jar.setScale(0.0)
        track.append(Func(toon.jar.reparentTo, toon.getRightHands()[0]))
        jarAndBank = Parallel(LerpScaleInterval(toon.jar, 1.5, 1.0, blendType = 'easeOut'), ActorInterval(toonbase.tcr.doId2do[avId], 'bank', endTime = 3.7999999999999998))
        track.append(jarAndBank)
        track.append(Func(toonbase.tcr.doId2do[avId].pingpong, 'bank', 48, 92))
        track.play()

    
    def _DistributedBank__putAwayToonJar(self, avId):
        toon = toonbase.tcr.doId2do[avId]
        track = Sequence()
        jarAndBank = Parallel(ActorInterval(toonbase.tcr.doId2do[avId], 'bank', startTime = 2.0, endTime = 0.0), LerpScaleInterval(toon.jar, 2.0, 0.0, blendType = 'easeIn'))
        track.append(jarAndBank)
        track.append(Func(toon.jar.removeNode))
        track.append(Func(toon.loop, 'neutral'))
        if avId == toonbase.localToon.doId:
            track.append(Func(self.freeAvatar))
        
        track.play()


