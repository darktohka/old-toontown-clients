# File: P (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
import PandaObject
import DirectNotifyGlobal
import StateData
import PublicWalk
import DownloadForceAcknowledge
import ZoneUtil
import FriendsListManager
import ToontownGlobals
import HouseGlobals
import Localizer
import Task

class Place(PandaObject.PandaObject, StateData.StateData, FriendsListManager.FriendsListManager):
    notify = DirectNotifyGlobal.directNotify.newCategory('Place')
    
    def __init__(self, loader, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        FriendsListManager.FriendsListManager.__init__(self)
        self.loader = loader
        self.dfaDoneEvent = 'dfaDoneEvent'
        return None

    
    def load(self):
        FriendsListManager.FriendsListManager.load(self)
        self.walkDoneEvent = 'walkDone'
        self.walkStateData = PublicWalk.PublicWalk(self.fsm, self.walkDoneEvent)
        self.walkStateData.load()
        return None

    
    def unload(self):
        FriendsListManager.FriendsListManager.unload(self)
        taskMgr.remove('goHomeFailed')
        del self.walkDoneEvent
        self.walkStateData.unload()
        del self.walkStateData
        del self.loader
        return None

    
    def setState(self, state):
        if hasattr(self, 'fsm'):
            self.fsm.request(state)
        

    
    def getZoneId(self):
        return None

    
    def isPeriodTimerEffective(self):
        return 1

    
    def handleTeleportQuery(self, fromAvatar, toAvatar):
        fromAvatar.d_teleportResponse(toAvatar.doId, 1, toAvatar.defaultShard, toonbase.tcr.playGame.getPlaceId(), self.getZoneId())

    
    def enablePeriodTimer(self):
        if self.isPeriodTimerEffective():
            if toonbase.tcr.periodTimerExpired:
                taskMgr.doMethodLater(5, self.redoPeriodTimer, 'redoPeriodTimer')
            
            self.accept('periodTimerExpired', self.periodTimerExpired)
        

    
    def disablePeriodTimer(self):
        taskMgr.remove('redoPeriodTimer')
        self.ignore('periodTimerExpired')

    
    def redoPeriodTimer(self, task):
        messenger.send('periodTimerExpired')
        return Task.done

    
    def periodTimerExpired(self):
        self.fsm.request('final')
        if toonbase.localToon.book.isEntered:
            toonbase.localToon.book.exit()
            toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self._Place__handlePeriodTimerBookClose)
        else:
            toonbase.localToon.b_setAnimState('TeleportOut', 1, self._Place__handlePeriodTimerExitTeleport)

    
    def exitPeriodTimerExpired(self):
        pass

    
    def _Place__handlePeriodTimerBookClose(self):
        toonbase.localToon.b_setAnimState('TeleportOut', 1, self._Place__handlePeriodTimerExitTeleport)

    
    def _Place__handlePeriodTimerExitTeleport(self):
        toonbase.tcr.loginFSM.request('periodTimeout')

    
    def enterWalk(self, teleportIn = 0):
        self.walkStateData.enter()
        if teleportIn == 0:
            self.walkStateData.fsm.request('walking')
        
        self.acceptOnce(self.walkDoneEvent, self.handleWalkDone)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.questPage.acceptOnscreenHooks()
        self.walkStateData.fsm.request('walking')
        self.enablePeriodTimer()
        return None

    
    def exitWalk(self):
        self.disablePeriodTimer()
        messenger.send('wakeup')
        self.walkStateData.exit()
        self.ignore(self.walkDoneEvent)
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        if toonbase.tcr.playGame.hood != None:
            toonbase.tcr.playGame.hood.hideTitleText()
        
        toonbase.localToon.questPage.hideQuestsOnscreen()
        toonbase.localToon.questPage.ignoreOnscreenHooks()
        return None

    
    def handleWalkDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'StickerBook':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('stickerBook')
        elif mode == 'Options':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('stickerBook', [
                toonbase.localToon.optionsPage])
        else:
            Place.notify.error('Invalid mode: %s' % mode)
        return None

    
    def enterStickerBook(self, page = None):
        FriendsListManager.FriendsListManager.enter(self)
        toonbase.localToon.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        if page:
            toonbase.localToon.book.setPage(page)
        
        toonbase.localToon.b_setAnimState('OpenBook', 1, self.enterStickerBookGUI)

    
    def enterStickerBookGUI(self):
        toonbase.localToon.collisionsOn()
        toonbase.localToon.book.showButton()
        toonbase.localToon.book.enter()
        toonbase.localToon.startSleepWatch(self._Place__handleFallingAsleep)
        self.accept('bookDone', self._Place__handleBook)
        self.accept(ToontownGlobals.OptionsPageHotkey, self._Place__escCloseBook)
        toonbase.localToon.b_setAnimState('ReadBook', 1)
        self.enablePeriodTimer()

    
    def _Place__handleFallingAsleep(self, task):
        toonbase.localToon.book.exit()
        toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self._Place__handleFallingAsleepBookClose)
        return Task.done

    
    def _Place__handleFallingAsleepBookClose(self):
        self.fsm.request('walk')
        toonbase.localToon.forceGotoSleep()

    
    def _Place__escCloseBook(self):
        toonbase.localToon.stopSleepWatch()
        toonbase.localToon.book.exit()
        toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self.handleBookClose)
        return None

    
    def exitStickerBook(self):
        toonbase.localToon.stopSleepWatch()
        self.disablePeriodTimer()
        FriendsListManager.FriendsListManager.exit(self)
        toonbase.localToon.laffMeter.stop()
        toonbase.localToon.book.exit()
        toonbase.localToon.book.hideButton()
        toonbase.localToon.collisionsOff()
        self.ignore('bookDone')
        self.ignore(ToontownGlobals.OptionsPageHotkey)
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')

    
    def _Place__handleBook(self):
        toonbase.localToon.stopSleepWatch()
        toonbase.localToon.book.exit()
        bookStatus = toonbase.localToon.book.getDoneStatus()
        if bookStatus['mode'] == 'close':
            toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self.handleBookClose)
        elif bookStatus['mode'] == 'teleport':
            zoneId = bookStatus['hood']
            toonbase.localToon.collisionsOff()
            toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self.handleBookCloseTeleport, extraArgs = [
                zoneId,
                zoneId])
        elif bookStatus['mode'] == 'exit':
            self.exitTo = bookStatus.get('exitTo')
            toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self._Place__handleBookCloseExit)
        elif bookStatus['mode'] == 'gohome':
            zoneId = bookStatus['hood']
            toonbase.localToon.collisionsOff()
            toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self._Place__handleBookCloseGoHome, extraArgs = [
                zoneId])
        

    
    def handleBookCloseTeleport(self, hoodId, zoneId):
        if hasattr(self, 'fsm'):
            self.fsm.request('DFA', [
                {
                    'loader': ZoneUtil.getBranchLoaderName(zoneId),
                    'where': ZoneUtil.getToonWhereName(zoneId),
                    'how': 'teleportIn',
                    'hoodId': hoodId,
                    'zoneId': zoneId,
                    'shardId': None,
                    'avId': -1 }])
        

    
    def _Place__handleBookCloseExit(self):
        toonbase.localToon.b_setAnimState('TeleportOut', 1, self._Place__handleBookExitTeleport, [
            0])

    
    def _Place__handleBookExitTeleport(self, requestStatus):
        if toonbase.tcr.timeManager:
            toonbase.tcr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectBookExit)
        
        toonbase.tcr.loginFSM.request(self.exitTo)

    
    def _Place__handleBookCloseGoHome(self, curZoneId):
        hoodId = ToontownGlobals.MyEstate
        if hasattr(self, 'fsm'):
            self.fsm.request('DFA', [
                {
                    'loader': 'estateLoader',
                    'where': 'estate',
                    'how': 'teleportIn',
                    'hoodId': hoodId,
                    'zoneId': -1,
                    'shardId': None,
                    'avId': -1 }])
        

    
    def handleBookClose(self):
        if hasattr(self, 'fsm'):
            self.fsm.request('walk')
        

    
    def enterDFA(self, requestStatus):
        self.acceptOnce(self.dfaDoneEvent, self.enterDFACallback, [
            requestStatus])
        self.dfa = DownloadForceAcknowledge.DownloadForceAcknowledge(self.dfaDoneEvent)
        self.dfa.enter(toonbase.tcr.hoodMgr.getPhaseFromHood(requestStatus['hoodId']))

    
    def exitDFA(self):
        self.ignore(self.dfaDoneEvent)

    
    def handleEnterTunnel(self, requestStatus, collEntry):
        self.fsm.request('DFA', [
            requestStatus])

    
    def enterDFACallback(self, requestStatus, doneStatus):
        self.dfa.exit()
        del self.dfa
        if doneStatus['mode'] == 'complete':
            if requestStatus.get('tutorial', 0):
                out = {
                    'teleportIn': 'tunnelOut' }
            else:
                out = {
                    'teleportIn': 'teleportOut',
                    'tunnelIn': 'tunnelOut',
                    'doorIn': 'doorOut' }
            self.fsm.request(out[requestStatus['how']], [
                requestStatus])
        elif doneStatus['mode'] == 'incomplete':
            self.fsm.request('DFAReject')
        else:
            Place.notify.error('Unknown done status for DownloadForceAcknowledge: ' + `doneStatus`)
        return None

    
    def enterDFAReject(self):
        self.fsm.request('walk')

    
    def exitDFAReject(self):
        pass

    
    def enterDoorIn(self, requestStatus):
        NametagGlobals.setMasterArrowsOn(0)
        door = toonbase.tcr.doId2do.get(requestStatus['doorDoId'])
        door.readyToExit()

    
    def exitDoorIn(self):
        NametagGlobals.setMasterArrowsOn(1)

    
    def enterDoorOut(self):
        pass

    
    def exitDoorOut(self):
        pass

    
    def handleDoorDoneEvent(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    
    def handleDoorTrigger(self):
        self.fsm.request('doorOut')

    
    def enterTunnelIn(self, requestStatus):
        Place.notify.debug('enterTunnelIn(requestStatus=' + str(requestStatus) + ')')
        tunnelOrigin = base.render.find(requestStatus['tunnelName'])
        self.accept('tunnelInMovieDone', self._Place__tunnelInMovieDone)
        toonbase.localToon.reconsiderCheesyEffect()
        toonbase.localToon.tunnelIn(tunnelOrigin)

    
    def _Place__tunnelInMovieDone(self):
        self.ignore('tunnelInMovieDone')
        self.fsm.request('walk')

    
    def exitTunnelIn(self):
        pass

    
    def enterTunnelOut(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        how = requestStatus['how']
        tunnelOrigin = requestStatus['tunnelOrigin']
        tunnelName = toonbase.tcr.hoodMgr.makeLinkTunnelName(self.loader.hood.id, self.getZoneId())
        self.doneStatus = {
            'loader': ZoneUtil.getLoaderName(zoneId),
            'where': ZoneUtil.getToonWhereName(zoneId),
            'how': how,
            'hoodId': hoodId,
            'zoneId': zoneId,
            'shardId': None,
            'tunnelName': tunnelName }
        self.accept('tunnelOutMovieDone', self._Place__tunnelOutMovieDone)
        toonbase.localToon.tunnelOut(tunnelOrigin)

    
    def _Place__tunnelOutMovieDone(self):
        self.ignore('tunnelOutMovieDone')
        messenger.send(self.doneEvent)

    
    def exitTunnelOut(self):
        pass

    
    def enterTeleportOut(self, requestStatus, callback):
        toonbase.localToon.laffMeter.start()
        toonbase.localToon.b_setAnimState('TeleportOut', 1, callback, [
            requestStatus])

    
    def exitTeleportOut(self):
        toonbase.localToon.laffMeter.stop()

    
    def getEstateZoneAndGoHome(self, requestStatus):
        self.doneStatus = requestStatus
        avId = requestStatus['avId']
        self.acceptOnce('setLocalEstateZone', self.goHome)
        if avId > 0:
            toonbase.tcr.estateMgr.getLocalEstateZone(avId)
        else:
            toonbase.tcr.estateMgr.getLocalEstateZone(toonbase.localToon.getDoId())
        if HouseGlobals.WANT_TELEPORT_TIMEOUT:
            taskMgr.doMethodLater(HouseGlobals.TELEPORT_TIMEOUT, self.goHomeFailed, 'goHomeFailed')
        

    
    def goHome(self, ownerId, zoneId):
        self.notify.debug('goHome ownerId = %s' % ownerId)
        taskMgr.remove('goHomeFailed')
        if ownerId > 0 and toonbase.tcr.identifyFriend(ownerId) == None:
            self.doneStatus['failed'] = 1
            taskMgr.add(self.goHomeFailed, 'goHomeFailed')
            return None
        
        if ownerId == 0 and zoneId == 0:
            self.doneStatus['hood'] = ToontownGlobals.MyEstate
            self.doneStatus['zone'] = toonbase.localToon.lastHood
            self.doneStatus['loaderId'] = 'estateLoader'
            self.doneStatus['whereId'] = 'estate'
            self.doneStatus['how'] = 'teleportIn'
            messenger.send(self.doneEvent)
            return None
        
        if self.doneStatus['zoneId'] == -1:
            self.doneStatus['zoneId'] = zoneId
        elif self.doneStatus['zoneId'] != zoneId:
            self.doneStatus['where'] = 'house'
        
        self.doneStatus['ownerId'] = ownerId
        messenger.send(self.doneEvent)
        messenger.send('localToonLeft')

    
    def goHomeFailed(self, task):
        self.notify.debug('goHomeFailed')
        self.notifyUserGoHomeFailed()
        self.ignore('setLocalEstateZone')
        self.doneStatus['hood'] = toonbase.localToon.lastHood
        self.doneStatus['zone'] = toonbase.localToon.lastHood
        self.fsm.request('deathAck', [
            self.doneStatus])
        return Task.done

    
    def notifyUserGoHomeFailed(self):
        self.notify.debug('notifyUserGoHomeFailed')
        failedToVisitAvId = self.doneStatus.get('avId')
        if failedToVisitAvId:
            message = Localizer.EstateTeleportFailedNotFriends % toonbase.tcr.identifyAvatar(failedToVisitAvId).getName()
        else:
            message = Localizer.EstateTeleportFailed
        toonbase.localToon.setSystemMessage(0, message)

    
    def enterTeleportIn(self, requestStatus):
        NametagGlobals.setMasterArrowsOn(0)
        toonbase.localToon.laffMeter.start()
        toonbase.localToon.reconsiderCheesyEffect()
        avId = requestStatus.get('avId', -1)
        if avId != -1:
            if toonbase.tcr.doId2do.has_key(avId):
                avatar = toonbase.tcr.doId2do[avId]
                avatar.forceToTruePosition()
                toonbase.localToon.gotoNode(avatar)
                toonbase.localToon.b_teleportGreeting(avId)
            else:
                friend = toonbase.tcr.identifyAvatar(avId)
                if friend != None:
                    toonbase.localToon.setSystemMessage(avId, Localizer.WhisperTargetLeftVisit % friend.getName())
                    friend.d_teleportGiveup(toonbase.localToon.doId)
                
        
        base.transitions.irisIn()
        if requestStatus.has_key('nextState'):
            self.nextState = requestStatus['nextState']
        else:
            self.nextState = 'walk'
        toonbase.localToon.startPosHprBroadcast()
        toonbase.localToon.startBlink()
        toonbase.localToon.attachCamera()
        toonbase.localToon.startUpdateSmartCamera()
        toonbase.localToon.detachCamera()
        globalClock.tick()
        toonbase.localToon.b_setAnimState('TeleportIn', 1, callback = self.teleportInDone)
        toonbase.localToon.d_broadcastPositionNow()
        toonbase.localToon.b_setParent(ToontownGlobals.SPRender)

    
    def teleportInDone(self):
        if hasattr(self, 'fsm'):
            self.fsm.request(self.nextState, [
                1])
        

    
    def exitTeleportIn(self):
        NametagGlobals.setMasterArrowsOn(1)
        toonbase.localToon.laffMeter.stop()

    
    def requestTeleport(self, hoodId, zoneId, shardId, avId):
        loaderId = ZoneUtil.getBranchLoaderName(zoneId)
        whereId = ZoneUtil.getToonWhereName(zoneId)
        if hoodId == ToontownGlobals.MyEstate:
            loaderId = 'estateLoader'
            whereId = 'estate'
        
        if hasattr(self, 'fsm'):
            self.fsm.request('DFA', [
                {
                    'loader': loaderId,
                    'where': whereId,
                    'how': 'teleportIn',
                    'hoodId': hoodId,
                    'zoneId': zoneId,
                    'shardId': shardId,
                    'avId': avId }])
        

    
    def enterQuest(self, npcToon):
        toonbase.localToon.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.laffMeter.start()

    
    def exitQuest(self):
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        toonbase.localToon.laffMeter.stop()

    
    def enterPurchase(self, npcToon):
        toonbase.localToon.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.laffMeter.start()

    
    def exitPurchase(self):
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        toonbase.localToon.laffMeter.stop()

    
    def enterFishing(self):
        toonbase.localToon.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.laffMeter.start()

    
    def exitFishing(self):
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        toonbase.localToon.laffMeter.stop()

    
    def enterBanking(self):
        toonbase.localToon.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.laffMeter.start()

    
    def exitBanking(self):
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        toonbase.localToon.laffMeter.stop()


