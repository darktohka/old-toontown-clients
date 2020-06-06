# File: D (Python 2.2)

import DistributedObject
import ToontownGlobals
import MailboxGlobals
import CatalogItem
import CatalogItemList
import ToontownDialog
import Localizer
import MailboxScreen
from DirectNotifyGlobal import *
from ClockDelta import *
from PandaModules import *
import random
FlagPitchEmpty = -70
FlagPitchFull = 0

class DistributedMailbox(DistributedObject.DistributedObject):
    notify = directNotify.newCategory('DistributedMailbox')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.model = None
        self.flag = None
        self.flagIval = None
        self.nameText = None
        self.fullIndicator = 0
        self.mailboxGui = None
        self.mailboxDialog = None
        self.mailboxSphereEvent = None
        self.mailboxSphereEnterEvent = None
        self.mailboxGuiDoneEvent = 'mailboxGuiDone'

    
    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        self.mailboxSphereEvent = self.taskName('mailboxSphere')
        self.mailboxSphereEnterEvent = 'enter' + self.mailboxSphereEvent
        if self.houseId == toonbase.localToon.houseId:
            self.accept(self.mailboxSphereEnterEvent, self._DistributedMailbox__handleEnterSphere)
        
        self.load()

    
    def load(self):
        randomGenerator = random.Random()
        randomGenerator.seed(self.houseId)
        r = randomGenerator.random()
        g = randomGenerator.random()
        b = randomGenerator.random()
        self.nameColor = (r, g, b, 1)
        houseNode = self.cr.playGame.hood.loader.houseNode[self.housePosInd]
        estateNode = houseNode.getParent()
        self.model = loader.loadModelCopy('phase_5.5/models/estate/mailboxHouse')
        self.model.reparentTo(estateNode)
        self.model.setPos(houseNode, 18, -4, 0)
        self.model.setH(houseNode, 90)
        self.flag = self.model.find('**/mailbox_flag')
        if self.fullIndicator:
            self.flag.setP(FlagPitchFull)
        else:
            self.flag.setP(FlagPitchEmpty)
        self._DistributedMailbox__setupName()
        sphere = CollisionSphere(0, 0, 0, 0.20000000000000001)
        sphereNode = CollisionNode(self.mailboxSphereEvent)
        sphereNode.setIntoCollideMask(ToontownGlobals.WallBitmask)
        sphereNode.addSolid(sphere)
        self.model.attachNewNode(sphereNode)

    
    def disable(self):
        self.notify.debug('disable')
        self.ignoreAll()
        if self.flagIval:
            self.flagIval.finish()
            self.flagIval = None
        
        if self.model:
            self.model.removeNode()
            self.model = None
        
        if self.nameText:
            self.nameText.removeNode()
            self.nameText = None
        
        if self.mailboxGui:
            self.mailboxGui.hide()
            self.mailboxGui.unload()
            self.mailboxGui = None
        
        if self.mailboxDialog:
            self.mailboxDialog.cleanup()
            self.mailboxDialog = None
        
        self.mailboxSphereEvent = None
        self.mailboxSphereEnterEvent = None
        DistributedObject.DistributedObject.disable(self)

    
    def setHouseId(self, houseId):
        self.houseId = houseId

    
    def setHousePos(self, housePosInd):
        self.housePosInd = housePosInd

    
    def setName(self, name):
        self.name = name

    
    def setFullIndicator(self, full):
        if self.fullIndicator != full:
            self.fullIndicator = full
            if self.flag:
                p = FlagPitchEmpty
                if self.fullIndicator:
                    p = FlagPitchFull
                
                if self.flagIval:
                    self.flagIval.pause()
                    self.flagIval = None
                
                self.flagIval = self.flag.hprInterval(0.5, VBase3(0, p, 0), blendType = 'easeInOut')
                self.flagIval.start()
            
        

    
    def _DistributedMailbox__handleEnterSphere(self, collEntry):
        self.notify.debug('Entering Mailbox Sphere....')
        self.ignore(self.mailboxSphereEnterEvent)
        self.cr.playGame.getPlace().detectedMailboxCollision()
        av = toonbase.localToon
        if len(av.mailboxContents) == 0:
            if len(av.onOrder) == 0:
                self.setMovie(MailboxGlobals.MAILBOX_MOVIE_EMPTY, av.doId)
            else:
                self.setMovie(MailboxGlobals.MAILBOX_MOVIE_WAITING, av.doId)
        else:
            self.sendUpdate('avatarEnter', [])

    
    def _DistributedMailbox__handleMailboxDone(self):
        self.sendUpdate('avatarExit', [])
        self.ignore(self.mailboxGuiDoneEvent)
        self.mailboxGui = None

    
    def freeAvatar(self):
        toonbase.tcr.playGame.getPlace().setState('walk')
        self.accept(self.mailboxSphereEnterEvent, self._DistributedMailbox__handleEnterSphere)

    
    def setMovie(self, mode, avId):
        isLocalToon = avId == toonbase.localToon.doId
        self.notify.info('setMovie: %s %s %s' % (mode, avId, isLocalToon))
        if mode == MailboxGlobals.MAILBOX_MOVIE_CLEAR:
            self.notify.debug('setMovie: clear')
            return None
        elif mode == MailboxGlobals.MAILBOX_MOVIE_EMPTY:
            self.notify.debug('setMovie: empty')
            if isLocalToon:
                self.mailboxDialog = ToontownDialog.ToontownDialog(dialogName = 'MailboxEmpty', style = ToontownDialog.Acknowledge, text = Localizer.DistributedMailboxEmpty, text_wordwrap = 15, fadeScreen = 1, command = self._DistributedMailbox__clearDialog)
            
            return None
        elif mode == MailboxGlobals.MAILBOX_MOVIE_WAITING:
            self.notify.debug('setMovie: waiting')
            if isLocalToon:
                self.mailboxDialog = ToontownDialog.ToontownDialog(dialogName = 'MailboxWaiting', style = ToontownDialog.Acknowledge, text = Localizer.DistributedMailboxWaiting, text_wordwrap = 15, fadeScreen = 1, command = self._DistributedMailbox__clearDialog)
            
            return None
        elif mode == MailboxGlobals.MAILBOX_MOVIE_READY:
            self.notify.debug('setMovie: ready')
            if isLocalToon:
                self.mailboxGui = MailboxScreen.MailboxScreen(self, toonbase.localToon, self.mailboxGuiDoneEvent)
                self.mailboxGui.show()
                self.accept(self.mailboxGuiDoneEvent, self._DistributedMailbox__handleMailboxDone)
            
            return None
        elif mode == MailboxGlobals.MAILBOX_MOVIE_NOT_OWNER:
            self.notify.debug('setMovie: not owner')
            if isLocalToon:
                self.mailboxDialog = ToontownDialog.ToontownDialog(dialogName = 'MailboxNotOwner', style = ToontownDialog.Acknowledge, text = Localizer.DistributedMailboxNotOwner, text_wordwrap = 15, fadeScreen = 1, command = self._DistributedMailbox__clearDialog)
            
            return None
        else:
            self.notify.warning('unknown mode in setMovie: %s' % mode)

    
    def acceptItem(self, item, index, callback, optional = -1):
        blob = item.getBlob(store = CatalogItem.Customization)
        context = self.getCallbackContext(callback, [
            item,
            index])
        self.sendUpdate('acceptItemMessage', [
            context,
            blob,
            index,
            optional])

    
    def acceptItemResponse(self, context, retcode):
        self.doCallbackContext(context, [
            retcode])

    
    def _DistributedMailbox__setupName(self):
        self.notify.debug('__setupName')
        if self.nameText:
            self.nameText.removeNode()
            self.nameText = None
        
        nameOrigin = self.model.find('**/nameLocator')
        if not nameOrigin.isEmpty():
            text = TextNode('nameText')
            text.setTextColor(*self.nameColor)
            text.setAlign(TextNode.ACenter)
            text.setFont(ToontownGlobals.getToonFont())
            text.setWordwrap(7.5)
            text.setText(self.name)
            self.nameText = nameOrigin.attachNewNode(text)
            self.nameText.setH(90)
            self.nameText.setScale(0.20000000000000001)
        

    
    def _DistributedMailbox__clearDialog(self, event):
        self.mailboxDialog.cleanup()
        self.mailboxDialog = None
        self.freeAvatar()


