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
import QuietZoneState

class Place(PandaObject.PandaObject, StateData.StateData, FriendsListManager.FriendsListManager):
    notify = DirectNotifyGlobal.directNotify.newCategory('Place')
    
    def __init__(self, loader, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        FriendsListManager.FriendsListManager.__init__(self)
        self.loader = loader
        self.dfaDoneEvent = 'dfaDoneEvent'
        self.zoneId = None

    
    def load(self):
        FriendsListManager.FriendsListManager.load(self)
        self.walkDoneEvent = 'walkDone'
        self.walkStateData = PublicWalk.PublicWalk(self.fsm, self.walkDoneEvent)
        self.walkStateData.load()

    
    def unload(self):
        FriendsListManager.FriendsListManager.unload(self)
        taskMgr.remove('goHomeFailed')
        del self.walkDoneEvent
        self.walkStateData.unload()
        del self.walkStateData
        del self.loader

    
    def setState(self, state):
        if hasattr(self, 'fsm'):
            self.fsm.request(state)
        

    
    def getZoneId(self):
        return self.zoneId

    
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

    
    def detectedPhoneCollision(self):
        self.fsm.request('phone')

    
    def detectedFishingCollision(self):
        self.fsm.request('fishing')

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def enterFinal(self):
        pass

    
    def exitFinal(self):
        pass

    
    def enterWalk(self, teleportIn = 0):
        self.walkStateData.enter()
        if teleportIn == 0:
            self.walkStateData.fsm.request('walking')
        
        self.acceptOnce(self.walkDoneEvent, self.handleWalkDone)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.questPage.acceptOnscreenHooks()
        toonbase.localToon.invPage.acceptOnscreenHooks()
        self.walkStateData.fsm.request('walking')
        self.enablePeriodTimer()

    
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
        toonbase.localToon.invPage.ignoreOnscreenHooks()
        toonbase.localToon.invPage.hideInventoryOnscreen()

    
    def handleWalkDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'StickerBook':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('stickerBook')
        elif mode == 'Options':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('stickerBook', [
                toonbase.localToon.optionsPage])
        elif mode == 'Sit':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('sit')
        else:
            Place.notify.error('Invalid mode: %s' % mode)

    
    def enterSit(self):
        FriendsListManager.FriendsListManager.enter(self)
        toonbase.localToon.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.b_setAnimState('SitStart', 1)
        self.accept('arrow_up', self.fsm.request, extraArgs = [
            'walk'])

    
    def exitSit(self):
        FriendsListManager.FriendsListManager.exit(self)
        toonbase.localToon.laffMeter.stop()
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        self.ignore('arrow_up')

    
    def enterPush(self):
        FriendsListManager.FriendsListManager.enter(self)
        toonbase.localToon.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.attachCamera()
        toonbase.localToon.startUpdateSmartCamera()
        toonbase.localToon.startPosHprBroadcast()
        toonbase.localToon.b_setAnimState('Push', 1)

    
    def exitPush(self):
        FriendsListManager.FriendsListManager.exit(self)
        toonbase.localToon.laffMeter.stop()
        toonbase.localToon.setTeleportAvailable(0)
        toonbase.localToon.stopUpdateSmartCamera()
        toonbase.localToon.detachCamera()
        toonbase.localToon.stopPosHprBroadcast()
        self.ignore('teleportQuery')

    
    def enterStickerBook(self, page = None):
        FriendsListManager.FriendsListManager.enter(self)
        toonbase.localToon.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        if page:
            toonbase.localToon.book.setPage(page)
        
        toonbase.localToon.b_setAnimState('OpenBook', 1, self.enterStickerBookGUI)
        toonbase.localToon.obscureMoveFurnitureButton(1)

    
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
        toonbase.localToon.obscureMoveFurnitureButton(-1)

    
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
            toonbase.localToon.b_setAnimState('CloseBook', 1, callback = self.goHomeNow, extraArgs = [
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

    
    def goHomeNow(self, curZoneId):
        hoodId = ToontownGlobals.MyEstate
        if hasattr(self, 'fsm'):
            self.fsm.request('DFA', [
                {
                    'loader': 'safeZoneLoader',
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

    
    def enterDFAReject(self):
        self.fsm.request('walk')

    
    def exitDFAReject(self):
        pass

    
    def enterDoorIn(self, requestStatus):
        NametagGlobals.setMasterArrowsOn(0)
        door = toonbase.tcr.doId2do.get(requestStatus['doorDoId'])
        door.readyToExit()
        toonbase.localToon.obscureMoveFurnitureButton(1)

    
    def exitDoorIn(self):
        NametagGlobals.setMasterArrowsOn(1)
        toonbase.localToon.obscureMoveFurnitureButton(-1)

    
    def enterDoorOut(self):
        toonbase.localToon.obscureMoveFurnitureButton(1)

    
    def exitDoorOut(self):
        toonbase.localToon.obscureMoveFurnitureButton(-1)

    
    def handleDoorDoneEvent(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    
    def handleDoorTrigger(self):
        self.fsm.request('doorOut')

    
    def enterTunnelIn(self, requestStatus):
        self.notify.debug('enterTunnelIn(requestStatus=' + str(requestStatus) + ')')
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
        fromZoneId = ZoneUtil.getCanonicalZoneId(self.getZoneId())
        tunnelName = requestStatus.get('tunnelName')
        if tunnelName == None:
            tunnelName = toonbase.tcr.hoodMgr.makeLinkTunnelName(self.loader.hood.id, fromZoneId)
        
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
        toonbase.localToon.obscureMoveFurnitureButton(1)

    
    def exitTeleportOut(self):
        toonbase.localToon.laffMeter.stop()
        toonbase.localToon.obscureMoveFurnitureButton(-1)

    
    def enterDied(self, requestStatus, callback = None):
        if callback == None:
            callback = self._Place__diedDone
        
        toonbase.localToon.laffMeter.start()
        camera.wrtReparentTo(render)
        toonbase.localToon.b_setAnimState('Died', 1, callback, [
            requestStatus])
        toonbase.localToon.obscureMoveFurnitureButton(1)

    
    def _Place__diedDone(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    
    def exitDied(self):
        toonbase.localToon.laffMeter.stop()
        toonbase.localToon.obscureMoveFurnitureButton(-1)

    
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
        if ownerId > 0 and ownerId != toonbase.localToon.doId and not toonbase.tcr.isFriend(ownerId):
            self.doneStatus['failed'] = 1
            self.goHomeFailed(None)
            return None
        
        if ownerId == 0 and zoneId == 0:
            self.doneStatus['hood'] = ToontownGlobals.MyEstate
            self.doneStatus['zone'] = toonbase.localToon.lastHood
            self.doneStatus['loaderId'] = 'safeZoneLoader'
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
        self.fsm.request('teleportIn', [
            self.doneStatus])
        return Task.done

    
    def notifyUserGoHomeFailed(self):
        self.notify.debug('notifyUserGoHomeFailed')
        failedToVisitAvId = self.doneStatus.get('avId', -1)
        avName = None
        if failedToVisitAvId != -1:
            avatar = toonbase.tcr.identifyAvatar(failedToVisitAvId)
            if avatar:
                avName = avatar.getName()
            
        
        if avName:
            message = Localizer.EstateTeleportFailedNotFriends % avName
        else:
            message = Localizer.EstateTeleportFailed
        toonbase.localToon.setSystemMessage(0, message)

    
    def enterTeleportIn(self, requestStatus):
        NametagGlobals.setMasterArrowsOn(0)
        toonbase.localToon.laffMeter.start()
        toonbase.localToon.reconsiderCheesyEffect()
        toonbase.localToon.obscureMoveFurnitureButton(1)
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
        toonbase.localToon.attachCamera()
        toonbase.localToon.startUpdateSmartCamera()
        toonbase.localToon.startPosHprBroadcast()
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
        toonbase.localToon.obscureMoveFurnitureButton(-1)
        toonbase.localToon.stopUpdateSmartCamera()
        toonbase.localToon.detachCamera()
        toonbase.localToon.stopPosHprBroadcast()

    
    def requestTeleport(self, hoodId, zoneId, shardId, avId):
        loaderId = ZoneUtil.getBranchLoaderName(zoneId)
        whereId = ZoneUtil.getToonWhereName(zoneId)
        if hoodId == ToontownGlobals.MyEstate:
            loaderId = 'safeZoneLoader'
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
        toonbase.localToon.obscureMoveFurnitureButton(1)

    
    def exitQuest(self):
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        toonbase.localToon.laffMeter.stop()
        toonbase.localToon.obscureMoveFurnitureButton(-1)

    
    def enterPurchase(self):
        toonbase.localToon.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.laffMeter.start()
        toonbase.localToon.obscureMoveFurnitureButton(1)

    
    def exitPurchase(self):
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        toonbase.localToon.laffMeter.stop()
        toonbase.localToon.obscureMoveFurnitureButton(-1)

    
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
        toonbase.localToon.obscureMoveFurnitureButton(1)

    
    def exitBanking(self):
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        toonbase.localToon.laffMeter.stop()
        toonbase.localToon.obscureMoveFurnitureButton(-1)

    
    def enterPhone(self):
        toonbase.localToon.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        toonbase.localToon.setTeleportAvailable(1)
        toonbase.localToon.laffMeter.start()
        toonbase.localToon.obscureMoveFurnitureButton(1)

    
    def exitPhone(self):
        toonbase.localToon.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        toonbase.localToon.laffMeter.stop()
        toonbase.localToon.obscureMoveFurnitureButton(-1)

    
    def enterQuietZone(self, requestStatus):
        self.quietZoneDoneEvent = 'quietZoneDone'
        self.acceptOnce(self.quietZoneDoneEvent, self.handleQuietZoneDone)
        self.quietZoneStateData = QuietZoneState.QuietZoneState(self.quietZoneDoneEvent)
        self.quietZoneStateData.load()
        self.quietZoneStateData.enter(requestStatus)

    
    def exitQuietZone(self):
        self.ignore(self.quietZoneDoneEvent)
        del self.quietZoneDoneEvent
        self.quietZoneStateData.exit()
        self.quietZoneStateData.unload()
        self.quietZoneStateData = None

    
    def handleQuietZoneDone(self):
        how = toonbase.tcr.handlerArgs['how']
        self.fsm.request(how, [
            toonbase.tcr.handlerArgs])


