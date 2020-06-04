# File: D (Python 2.2)

from direct.gui.DirectGui import *
from toontown.toonbase.ToontownGlobals import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import ToontownGlobals
import DistributedFurnitureItem
from toontown.toonbase import TTLocalizer
from pandac import CollisionSphere
from pandac import CollisionNode
import BankGUI
from BankGlobals import *
from toontown.toontowngui import TTDialog
from toontown.catalog.CatalogFurnitureItem import FurnitureTypes
from toontown.catalog.CatalogFurnitureItem import FTScale

class DistributedBank(DistributedFurnitureItem.DistributedFurnitureItem):
    notify = directNotify.newCategory('DistributedBank')
    
    def __init__(self, cr):
        DistributedFurnitureItem.DistributedFurnitureItem.__init__(self, cr)
        self.bankGui = None
        self.bankTrack = None
        self.bankDialog = None
        self.hasLocalAvatar = 0
        self.hasJarOut = 0

    
    def generate(self):
        DistributedFurnitureItem.DistributedFurnitureItem.generate(self)
        self.bankSphereEvent = 'bankSphere'
        self.bankSphereEnterEvent = 'enter' + self.bankSphereEvent
        self.bankSphereExitEvent = 'exit' + self.bankSphereEvent
        self.bankGuiDoneEvent = 'bankGuiDone'

    
    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        self.accept(self.bankSphereEnterEvent, self._DistributedBank__handleEnterSphere)

    
    def disable(self):
        self.notify.debug('disable')
        self.ignore(self.bankSphereEnterEvent)
        self.ignore(self.bankSphereExitEvent)
        self.ignore(self.bankGuiDoneEvent)
        if self.bankTrack:
            self.bankTrack.pause()
            self.bankTrack = None
        
        if self.bankGui:
            self.bankGui.destroy()
            self.bankGui = None
        
        if self.bankDialog:
            self.bankDialog.cleanup()
            self.bankDialog = None
        
        if self.hasLocalAvatar:
            self.freeAvatar()
        
        self.ignoreAll()
        DistributedFurnitureItem.DistributedFurnitureItem.disable(self)

    
    def delete(self):
        self.notify.debug('delete')
        DistributedFurnitureItem.DistributedFurnitureItem.delete(self)

    
    def _DistributedBank__handleEnterSphere(self, collEntry):
        if self.smoothStarted:
            return None
        
        if self.hasLocalAvatar:
            self.freeAvatar()
        
        self.notify.debug('Entering Bank Sphere....')
        self.acceptOnce(self.bankSphereExitEvent, self._DistributedBank__handleExitSphere)
        self.ignore(self.bankSphereEnterEvent)
        self.cr.playGame.getPlace().fsm.request('banking')
        self.hasLocalAvatar = 1
        self.sendUpdate('avatarEnter', [])

    
    def _DistributedBank__handleExitSphere(self, collEntry):
        self.notify.debug('Exiting Bank Sphere....')
        if self.bankTrack is not None:
            self.bankTrack.pause()
            self.bankTrack = None
        
        if self.bankDialog is not None:
            self.bankDialog.cleanup()
            self.bankDialog = None
        
        self._DistributedBank__handleBankDone(0)

    
    def _DistributedBank__handleBankDone(self, transactionAmount):
        self.notify.debug('__handleBankDone(transactionAmount=%s' % (transactionAmount,))
        self.sendUpdate('transferMoney', [
            transactionAmount])
        self.ignore(self.bankGuiDoneEvent)
        self.ignore(self.bankSphereExitEvent)
        if self.bankGui is not None:
            self.bankGui.destroy()
            self.bankGui = None
        

    
    def freeAvatar(self):
        self.notify.debug('freeAvatar()')
        if self.hasLocalAvatar:
            base.localAvatar.posCamera(0, 0)
            base.cr.playGame.getPlace().setState('walk')
            self.hasLocalAvatar = 0
        
        self.accept(self.bankSphereEnterEvent, self._DistributedBank__handleEnterSphere)

    
    def showBankGui(self):
        if self.bankGui:
            self.bankGui.destroy()
        
        self.bankGui = BankGUI.BankGui(self.bankGuiDoneEvent)
        self.accept(self.bankGuiDoneEvent, self._DistributedBank__handleBankDone)

    
    def setMovie(self, mode, avId, timestamp):
        self.notify.debug('setMovie(mode=%s, avId=%s, timestamp=%s)' % (mode, avId, timestamp))
        timeStamp = globalClockDelta.localElapsedTime(timestamp)
        isLocalToon = avId == base.localAvatar.doId
        self.notify.info('setMovie: mode=%s, avId=%s, timeStamp=%s, isLocalToon=%s' % (mode, avId, timeStamp, isLocalToon))
        if mode == BANK_MOVIE_CLEAR:
            self.notify.debug('setMovie: clear')
        elif mode == BANK_MOVIE_GUI:
            self.notify.debug('setMovie: gui')
            track = Sequence()
            track.append(Func(self._DistributedBank__takeOutToonJar, avId))
            if isLocalToon:
                track.append(Wait(3.0))
                track.append(Func(self.showBankGui))
            
            track.start()
            self.bankTrack = track
        elif mode == BANK_MOVIE_DEPOSIT:
            self.notify.debug('setMovie: deposit')
            self._DistributedBank__putAwayToonJar(avId)
        elif mode == BANK_MOVIE_WITHDRAW:
            self.notify.debug('setMovie: withdraw')
            self._DistributedBank__putAwayToonJar(avId)
        elif mode == BANK_MOVIE_NO_OP:
            self.notify.debug('setMovie: no op')
            self._DistributedBank__putAwayToonJar(avId)
        elif mode == BANK_MOVIE_NOT_OWNER:
            self.notify.debug('setMovie: not owner')
            if isLocalToon:
                self.bankDialog = TTDialog.TTDialog(dialogName = 'BankNotOwner', style = TTDialog.Acknowledge, text = TTLocalizer.DistributedBankNotOwner, text_wordwrap = 15, fadeScreen = 1, command = self._DistributedBank__clearDialog)
            
        elif mode == BANK_MOVIE_NO_OWNER:
            self.notify.debug('setMovie: no owner')
            if isLocalToon:
                self.bankDialog = TTDialog.TTDialog(dialogName = 'BankNoOwner', style = TTDialog.Acknowledge, text = TTLocalizer.DistributedBankNoOwner, text_wordwrap = 15, fadeScreen = 1, command = self._DistributedBank__clearDialog)
            
        else:
            self.notify.warning('unknown mode in setMovie: %s' % mode)

    
    def _DistributedBank__clearDialog(self, event):
        self.notify.debug('__clearDialog(event=%s)' % (event,))
        if self.bankDialog is not None:
            self.bankDialog.cleanup()
            self.bankDialog = None
        
        self.freeAvatar()

    
    def _DistributedBank__takeOutToonJar(self, avId):
        self.notify.debug('__takeOutToonJar(avId=%s)' % (avId,))
        toon = base.cr.doId2do.get(avId)
        if toon == None:
            return None
        
        track = Sequence()
        index = self.item.furnitureType
        scale = FurnitureTypes[index][FTScale]
        print '\n### bank scale: ', scale
        walkToBank = Sequence(Func(toon.stopSmooth), Func(toon.loop, 'walk'), toon.posHprInterval(0.5, Point3(0, -3.125 * (scale + 0.20000000000000001), 0), Point3(0, 0, 0), other = self, blendType = 'easeInOut'), Func(toon.loop, 'neutral'), Func(toon.startSmooth))
        track.append(walkToBank)
        if not (toon.jar):
            toon.getJar()
        
        track.append(Func(toon.jar.reparentTo, toon.getRightHands()[0]))
        jarAndBank = Parallel(LerpScaleInterval(toon.jar, 1.5, 1.0, blendType = 'easeOut'), ActorInterval(base.cr.doId2do[avId], 'bank', endTime = 3.7999999999999998))
        track.append(jarAndBank)
        track.append(Func(base.cr.doId2do[avId].pingpong, 'bank', fromFrame = 48, toFrame = 92))
        track.start()
        self.hasJarOut = 1

    
    def _DistributedBank__putAwayToonJar(self, avId):
        self.notify.debug('__putAwayToonJar(avId=%s)' % (avId,))
        toon = base.cr.doId2do.get(avId)
        if toon is None:
            return None
        
        if not (self.hasJarOut):
            return None
        
        self.hasJarOut = 0
        if not (toon.jar):
            toon.getJar()
        
        track = Sequence()
        jarAndBank = Parallel(ActorInterval(base.cr.doId2do[avId], 'bank', startTime = 2.0, endTime = 0.0), LerpScaleInterval(toon.jar, 2.0, 0.0, blendType = 'easeIn'))
        track.append(jarAndBank)
        track.append(Func(toon.removeJar))
        track.append(Func(toon.loop, 'neutral'))
        if avId == base.localAvatar.doId:
            track.append(Func(self.freeAvatar))
        
        track.start()
        self.bankTrack = track


