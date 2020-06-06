# File: H (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
import DirectNotifyGlobal
import Place
import PandaObject
import StateData
import FSM
import State
import Task
import ToontownGlobals
import Localizer
import AvatarDNA

class House(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('House')
    
    def __init__(self, loader, avId, parentFSMState, doneEvent):
        Place.Place.__init__(self, loader, doneEvent)
        self.id = ToontownGlobals.MyEstate
        self.ownersAvId = avId
        self.dnaFile = 'phase_7/models/modules/toon_interior'
        self.isInterior = 1
        self.tfaDoneEvent = 'tfaDoneEvent'
        self.oldStyle = None
        self.fsm = FSM.FSM('House', [
            State.State('start', self.enterStart, self.exitStart, [
                'doorIn',
                'teleportIn',
                'tutorial']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'stickerBook',
                'doorOut',
                'DFA',
                'teleportOut',
                'quest',
                'purchase',
                'banking']),
            State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, [
                'walk',
                'DFA']),
            State.State('DFA', self.enterDFA, self.exitDFA, [
                'DFAReject',
                'teleportOut',
                'doorOut']),
            State.State('DFAReject', self.enterDFAReject, self.exitDFAReject, [
                'walk']),
            State.State('doorIn', self.enterDoorIn, self.exitDoorIn, [
                'walk']),
            State.State('doorOut', self.enterDoorOut, self.exitDoorOut, [
                'walk']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk']),
            State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, [
                'teleportIn']),
            State.State('quest', self.enterQuest, self.exitQuest, [
                'walk',
                'doorOut']),
            State.State('tutorial', self.enterTutorial, self.exitTutorial, [
                'walk',
                'quest']),
            State.State('purchase', self.enterPurchase, self.exitPurchase, [
                'walk',
                'doorOut']),
            State.State('banking', self.enterBanking, self.exitBanking, [
                'walk']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start',
                'teleportIn'])], 'start', 'final')
        self.parentFSMState = parentFSMState

    
    def load(self):
        Place.Place.load(self)
        self.parentFSMState.addChild(self.fsm)

    
    def unload(self):
        Place.Place.unload(self)
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        del self.fsm
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    
    def enter(self, requestStatus):
        self.zoneId = requestStatus['zoneId']
        self.fsm.enterInitialState()
        messenger.send('enterHouse')
        self.accept('doorDoneEvent', self.handleDoorDoneEvent)
        self.accept('DistributedDoor_doorTrigger', self.handleDoorTrigger)
        NametagGlobals.setMasterArrowsOn(1)
        self.fsm.request(requestStatus['how'], [
            requestStatus])

    
    def exit(self):
        self.ignoreAll()
        messenger.send('exitHouse')
        NametagGlobals.setMasterArrowsOn(0)

    
    def setState(self, state):
        self.fsm.request(state)

    
    def getZoneId(self):
        return self.zoneId

    
    def detectedClosetCollision(self):
        self.fsm.request('purchase')

    
    def detectedBankCollision(self):
        self.fsm.request('banking')

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterTutorial(self, requestStatus):
        print '### sending enterTutorialInterior'
        self.fsm.request('walk')
        toonbase.localToon.b_setParent(ToontownGlobals.SPRender)
        globalClock.tick()
        base.transitions.irisIn()
        messenger.send('enterTutorialInterior')

    
    def exitTutorial(self):
        pass

    
    def enterTeleportIn(self, requestStatus):
        toonbase.localToon.setPosHpr(2.5, 11.5, ToontownGlobals.FloorOffset, 45.0, 0.0, 0.0)
        Place.Place.enterTeleportIn(self, requestStatus)

    
    def enterTeleportOut(self, requestStatus):
        Place.Place.enterTeleportOut(self, requestStatus, self._House__teleportOutDone)

    
    def _House__teleportOutDone(self, requestStatus):
        self.notify.debug('House: teleportOutDone: requestStatus = %s' % requestStatus)
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        avId = requestStatus['avId']
        shardId = requestStatus['shardId']
        if hoodId == ToontownGlobals.MyEstate and zoneId == self.getZoneId():
            self.fsm.request('teleportIn', [
                requestStatus])
        elif hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent, [
                self.doneStatus])

    
    def goHomeFailed(self, task):
        self.notifyUserGoHomeFailed()
        self.ignore('setLocalEstateZone')
        self.doneStatus['avId'] = -1
        self.doneStatus['zoneId'] = self.getZoneId()
        self.fsm.request('teleportIn', [
            self.doneStatus])
        return Task.done

    
    def exitTeleportOut(self):
        pass

    
    def enterPurchase(self):
        Place.Place.enterPurchase(self, None)

    
    def exitPurchase(self):
        Place.Place.exitPurchase(self)

    
    def enterBanking(self):
        Place.Place.enterBanking(self)

    
    def exitBanking(self):
        Place.Place.exitBanking(self)

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass


