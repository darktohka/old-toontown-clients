# File: P (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.showbase import PandaObject
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from toontown.safezone import PublicWalk
from toontown.launcher import DownloadForceAcknowledge
import TrialerForceAcknowledge
import ZoneUtil
from toontown.friends import FriendsListManager
from toontown.toonbase import ToontownGlobals
from toontown.estate import HouseGlobals
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPLocalizer
from otp.avatar import Emote
from direct.task import Task
import QuietZoneState

class Place(PandaObject.PandaObject, StateData.StateData, FriendsListManager.FriendsListManager):
    notify = DirectNotifyGlobal.directNotify.newCategory('Place')
    
    def __init__(self, loader, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        FriendsListManager.FriendsListManager.__init__(self)
        self.loader = loader
        self.dfaDoneEvent = 'dfaDoneEvent'
        self.trialerFADoneEvent = 'trialerFADoneEvent'
        self.zoneId = None
        self.trialerFA = None

    
    def load(self):
        FriendsListManager.FriendsListManager.load(self)
        self.walkDoneEvent = 'walkDone'
        self.walkStateData = PublicWalk.PublicWalk(self.fsm, self.walkDoneEvent)
        self.walkStateData.load()
        base._preserveFriendsList = 0

    
    def unload(self):
        FriendsListManager.FriendsListManager.unload(self)
        taskMgr.remove('goHomeFailed')
        del self.walkDoneEvent
        self.walkStateData.unload()
        del self.walkStateData
        del self.loader
        if self.trialerFA:
            self.trialerFA.exit()
            del self.trialerFA
        

    
    def setState(self, state):
        if hasattr(self, 'fsm'):
            self.fsm.request(state)
        

    
    def preserveFriendsList(self):
        base._preserveFriendsList = 1

    
    def getZoneId(self):
        return self.zoneId

    
    def getTaskZoneId(self):
        return self.getZoneId()

    
    def isPeriodTimerEffective(self):
        return 1

    
    def handleTeleportQuery(self, fromAvatar, toAvatar):
        fromAvatar.d_teleportResponse(toAvatar.doId, 1, toAvatar.defaultShard, base.cr.playGame.getPlaceId(), self.getZoneId())

    
    def enablePeriodTimer(self):
        if self.isPeriodTimerEffective():
            if base.cr.periodTimerExpired:
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
        if base.localAvatar.book.isEntered:
            base.localAvatar.book.exit()
            base.localAvatar.b_setAnimState('CloseBook', 1, callback = self._Place__handlePeriodTimerBookClose)
        else:
            base.localAvatar.b_setAnimState('TeleportOut', 1, self._Place__handlePeriodTimerExitTeleport)

    
    def exitPeriodTimerExpired(self):
        pass

    
    def _Place__handlePeriodTimerBookClose(self):
        base.localAvatar.b_setAnimState('TeleportOut', 1, self._Place__handlePeriodTimerExitTeleport)

    
    def _Place__handlePeriodTimerExitTeleport(self):
        base.cr.loginFSM.request('periodTimeout')

    
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
        if not base.cr.isPaid() and base.localAvatar.tutorialAck:
            base.localAvatar.chatMgr.obscure(0, 0)
            base.localAvatar.chatMgr.normalButton.show()
        
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.questPage.acceptOnscreenHooks()
        base.localAvatar.invPage.acceptOnscreenHooks()
        self.walkStateData.fsm.request('walking')
        self.enablePeriodTimer()

    
    def exitWalk(self):
        if not base.cr.isPaid() and base.localAvatar.tutorialAck:
            base.localAvatar.chatMgr.obscure(1, 0)
        
        self.disablePeriodTimer()
        messenger.send('wakeup')
        self.walkStateData.exit()
        self.ignore(self.walkDoneEvent)
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        if base.cr.playGame.hood != None:
            base.cr.playGame.hood.hideTitleText()
        
        base.localAvatar.questPage.hideQuestsOnscreen()
        base.localAvatar.questPage.ignoreOnscreenHooks()
        base.localAvatar.invPage.ignoreOnscreenHooks()
        base.localAvatar.invPage.hideInventoryOnscreen()

    
    def handleWalkDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'StickerBook':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('stickerBook')
        elif mode == 'Options':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('stickerBook', [
                base.localAvatar.optionsPage])
        elif mode == 'Sit':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('sit')
        else:
            Place.notify.error('Invalid mode: %s' % mode)

    
    def enterSit(self):
        FriendsListManager.FriendsListManager.enter(self)
        base.localAvatar.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.b_setAnimState('SitStart', 1)
        self.accept('arrow_up', self.fsm.request, extraArgs = [
            'walk'])

    
    def exitSit(self):
        FriendsListManager.FriendsListManager.exit(self)
        base.localAvatar.laffMeter.stop()
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        self.ignore('arrow_up')

    
    def enterPush(self):
        FriendsListManager.FriendsListManager.enter(self)
        base.localAvatar.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.attachCamera()
        base.localAvatar.startUpdateSmartCamera()
        base.localAvatar.startPosHprBroadcast()
        base.localAvatar.b_setAnimState('Push', 1)

    
    def exitPush(self):
        FriendsListManager.FriendsListManager.exit(self)
        base.localAvatar.laffMeter.stop()
        base.localAvatar.setTeleportAvailable(0)
        base.localAvatar.stopUpdateSmartCamera()
        base.localAvatar.detachCamera()
        base.localAvatar.stopPosHprBroadcast()
        self.ignore('teleportQuery')

    
    def enterStickerBook(self, page = None):
        FriendsListManager.FriendsListManager.enter(self)
        base.localAvatar.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        if page:
            base.localAvatar.book.setPage(page)
        
        base.localAvatar.b_setAnimState('OpenBook', 1, self.enterStickerBookGUI)
        base.localAvatar.obscureMoveFurnitureButton(1)

    
    def enterStickerBookGUI(self):
        base.localAvatar.collisionsOn()
        base.localAvatar.book.showButton()
        base.localAvatar.book.enter()
        base.localAvatar.startSleepWatch(self._Place__handleFallingAsleep)
        self.accept('bookDone', self._Place__handleBook)
        self.accept(ToontownGlobals.OptionsPageHotkey, self._Place__escCloseBook)
        base.localAvatar.b_setAnimState('ReadBook', 1)
        self.enablePeriodTimer()

    
    def _Place__handleFallingAsleep(self, task):
        base.localAvatar.book.exit()
        base.localAvatar.b_setAnimState('CloseBook', 1, callback = self._Place__handleFallingAsleepBookClose)
        return Task.done

    
    def _Place__handleFallingAsleepBookClose(self):
        if hasattr(self, 'fsm'):
            self.fsm.request('walk')
        
        base.localAvatar.forceGotoSleep()

    
    def _Place__escCloseBook(self):
        base.localAvatar.stopSleepWatch()
        base.localAvatar.book.exit()
        base.localAvatar.b_setAnimState('CloseBook', 1, callback = self.handleBookClose)

    
    def exitStickerBook(self):
        base.localAvatar.stopSleepWatch()
        self.disablePeriodTimer()
        FriendsListManager.FriendsListManager.exit(self)
        base.localAvatar.laffMeter.stop()
        base.localAvatar.book.exit()
        base.localAvatar.book.hideButton()
        base.localAvatar.collisionsOff()
        self.ignore('bookDone')
        self.ignore(ToontownGlobals.OptionsPageHotkey)
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.obscureMoveFurnitureButton(-1)

    
    def _Place__handleBook(self):
        base.localAvatar.stopSleepWatch()
        base.localAvatar.book.exit()
        bookStatus = base.localAvatar.book.getDoneStatus()
        if bookStatus['mode'] == 'close':
            base.localAvatar.b_setAnimState('CloseBook', 1, callback = self.handleBookClose)
        elif bookStatus['mode'] == 'teleport':
            zoneId = bookStatus['hood']
            base.localAvatar.collisionsOff()
            base.localAvatar.b_setAnimState('CloseBook', 1, callback = self.handleBookCloseTeleport, extraArgs = [
                zoneId,
                zoneId])
        elif bookStatus['mode'] == 'exit':
            self.exitTo = bookStatus.get('exitTo')
            base.localAvatar.b_setAnimState('CloseBook', 1, callback = self._Place__handleBookCloseExit)
        elif bookStatus['mode'] == 'gohome':
            zoneId = bookStatus['hood']
            base.localAvatar.collisionsOff()
            base.localAvatar.b_setAnimState('CloseBook', 1, callback = self.goHomeNow, extraArgs = [
                zoneId])
        

    
    def handleBookCloseTeleport(self, hoodId, zoneId):
        self.requestLeave({
            'loader': ZoneUtil.getBranchLoaderName(zoneId),
            'where': ZoneUtil.getToonWhereName(zoneId),
            'how': 'teleportIn',
            'hoodId': hoodId,
            'zoneId': zoneId,
            'shardId': None,
            'avId': -1 })

    
    def _Place__handleBookCloseExit(self):
        base.localAvatar.b_setAnimState('TeleportOut', 1, self._Place__handleBookExitTeleport, [
            0])

    
    def _Place__handleBookExitTeleport(self, requestStatus):
        if base.cr.timeManager:
            base.cr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectBookExit)
        
        base.cr.loginFSM.request(self.exitTo)

    
    def goHomeNow(self, curZoneId):
        hoodId = ToontownGlobals.MyEstate
        self.requestLeave({
            'loader': 'safeZoneLoader',
            'where': 'estate',
            'how': 'teleportIn',
            'hoodId': hoodId,
            'zoneId': -1,
            'shardId': None,
            'avId': -1 })

    
    def handleBookClose(self):
        if hasattr(self, 'fsm'):
            self.fsm.request('walk')
        

    
    def requestLeave(self, requestStatus):
        if hasattr(self, 'fsm'):
            self.doRequestLeave(requestStatus)
        

    
    def doRequestLeave(self, requestStatus):
        self.fsm.request('DFA', [
            requestStatus])

    
    def enterDFA(self, requestStatus):
        self.acceptOnce(self.dfaDoneEvent, self.enterDFACallback, [
            requestStatus])
        self.dfa = DownloadForceAcknowledge.DownloadForceAcknowledge(self.dfaDoneEvent)
        self.dfa.enter(base.cr.hoodMgr.getPhaseFromHood(requestStatus['hoodId']))

    
    def exitDFA(self):
        self.ignore(self.dfaDoneEvent)

    
    def handleEnterTunnel(self, requestStatus, collEntry):
        self.requestLeave(requestStatus)

    
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

    
    def enterTrialerFA(self, requestStatus):
        self.acceptOnce(self.trialerFADoneEvent, self.trialerFACallback, [
            requestStatus])
        self.trialerFA = TrialerForceAcknowledge.TrialerForceAcknowledge(self.trialerFADoneEvent)
        self.trialerFA.enter(requestStatus['hoodId'])

    
    def exitTrialerFA(self):
        pass

    
    def trialerFACallback(self, requestStatus, doneStatus):
        if doneStatus['mode'] == 'pass':
            self.fsm.request('DFA', [
                requestStatus])
        elif doneStatus['mode'] == 'fail':
            self.fsm.request('trialerFAReject')
        else:
            Place.notify.error('Unknown done status for TrialerForceAcknowledge: %s' % doneStatus)

    
    def enterTrialerFAReject(self):
        self.fsm.request('walk')

    
    def exitTrialerFAReject(self):
        pass

    
    def enterDoorIn(self, requestStatus):
        NametagGlobals.setMasterArrowsOn(0)
        door = base.cr.doId2do.get(requestStatus['doorDoId'])
        door.readyToExit()
        base.localAvatar.obscureMoveFurnitureButton(1)

    
    def exitDoorIn(self):
        NametagGlobals.setMasterArrowsOn(1)
        base.localAvatar.obscureMoveFurnitureButton(-1)

    
    def enterDoorOut(self):
        base.localAvatar.obscureMoveFurnitureButton(1)

    
    def exitDoorOut(self):
        base.localAvatar.obscureMoveFurnitureButton(-1)

    
    def handleDoorDoneEvent(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    
    def handleDoorTrigger(self):
        self.fsm.request('doorOut')

    
    def enterTunnelIn(self, requestStatus):
        self.notify.debug('enterTunnelIn(requestStatus=' + str(requestStatus) + ')')
        tunnelOrigin = base.render.find(requestStatus['tunnelName'])
        self.accept('tunnelInMovieDone', self._Place__tunnelInMovieDone)
        base.localAvatar.reconsiderCheesyEffect()
        base.localAvatar.tunnelIn(tunnelOrigin)

    
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
            tunnelName = base.cr.hoodMgr.makeLinkTunnelName(self.loader.hood.id, fromZoneId)
        
        self.doneStatus = {
            'loader': ZoneUtil.getLoaderName(zoneId),
            'where': ZoneUtil.getToonWhereName(zoneId),
            'how': how,
            'hoodId': hoodId,
            'zoneId': zoneId,
            'shardId': None,
            'tunnelName': tunnelName }
        self.accept('tunnelOutMovieDone', self._Place__tunnelOutMovieDone)
        base.localAvatar.tunnelOut(tunnelOrigin)

    
    def _Place__tunnelOutMovieDone(self):
        self.ignore('tunnelOutMovieDone')
        messenger.send(self.doneEvent)

    
    def exitTunnelOut(self):
        pass

    
    def enterTeleportOut(self, requestStatus, callback):
        base.localAvatar.laffMeter.start()
        base.localAvatar.b_setAnimState('TeleportOut', 1, callback, [
            requestStatus])
        base.localAvatar.obscureMoveFurnitureButton(1)

    
    def exitTeleportOut(self):
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(-1)

    
    def enterDied(self, requestStatus, callback = None):
        if callback == None:
            callback = self._Place__diedDone
        
        base.localAvatar.laffMeter.start()
        camera.wrtReparentTo(render)
        base.localAvatar.b_setAnimState('Died', 1, callback, [
            requestStatus])
        base.localAvatar.obscureMoveFurnitureButton(1)

    
    def _Place__diedDone(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    
    def exitDied(self):
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(-1)

    
    def getEstateZoneAndGoHome(self, requestStatus):
        self.doneStatus = requestStatus
        avId = requestStatus['avId']
        print requestStatus
        self.acceptOnce('setLocalEstateZone', self.goHome)
        if avId > 0:
            base.cr.estateMgr.getLocalEstateZone(avId)
        else:
            base.cr.estateMgr.getLocalEstateZone(base.localAvatar.getDoId())
        if HouseGlobals.WANT_TELEPORT_TIMEOUT:
            taskMgr.doMethodLater(HouseGlobals.TELEPORT_TIMEOUT, self.goHomeFailed, 'goHomeFailed')
        

    
    def goHome(self, ownerId, zoneId):
        self.notify.debug('goHome ownerId = %s' % ownerId)
        taskMgr.remove('goHomeFailed')
        if ownerId > 0 and ownerId != base.localAvatar.doId and not base.cr.isFriend(ownerId):
            self.doneStatus['failed'] = 1
            self.goHomeFailed(None)
            return None
        
        if ownerId == 0 and zoneId == 0:
            if self.doneStatus['shardId'] is None or self.doneStatus['shardId'] is base.localAvatar.defaultShard:
                self.doneStatus['failed'] = 1
                self.goHomeFailed(None)
                return None
            else:
                self.doneStatus['hood'] = ToontownGlobals.MyEstate
                self.doneStatus['zone'] = base.localAvatar.lastHood
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
        self.doneStatus['hood'] = base.localAvatar.lastHood
        self.doneStatus['zone'] = base.localAvatar.lastHood
        self.fsm.request('teleportIn', [
            self.doneStatus])
        return Task.done

    
    def notifyUserGoHomeFailed(self):
        self.notify.debug('notifyUserGoHomeFailed')
        failedToVisitAvId = self.doneStatus.get('avId', -1)
        avName = None
        if failedToVisitAvId != -1:
            avatar = base.cr.identifyAvatar(failedToVisitAvId)
            if avatar:
                avName = avatar.getName()
            
        
        if avName:
            message = TTLocalizer.EstateTeleportFailedNotFriends % avName
        else:
            message = TTLocalizer.EstateTeleportFailed
        base.localAvatar.setSystemMessage(0, message)

    
    def enterTeleportIn(self, requestStatus):
        NametagGlobals.setMasterArrowsOn(0)
        base.localAvatar.laffMeter.start()
        base.localAvatar.reconsiderCheesyEffect()
        base.localAvatar.obscureMoveFurnitureButton(1)
        avId = requestStatus.get('avId', -1)
        if avId != -1:
            if base.cr.doId2do.has_key(avId):
                avatar = base.cr.doId2do[avId]
                avatar.forceToTruePosition()
                base.localAvatar.gotoNode(avatar)
                base.localAvatar.b_teleportGreeting(avId)
            else:
                friend = base.cr.identifyAvatar(avId)
                if friend != None:
                    base.localAvatar.setSystemMessage(avId, OTPLocalizer.WhisperTargetLeftVisit % (friend.getName(),))
                    friend.d_teleportGiveup(base.localAvatar.doId)
                
        
        base.transitions.irisIn()
        self.nextState = requestStatus.get('nextState', 'walk')
        base.localAvatar.attachCamera()
        base.localAvatar.startUpdateSmartCamera()
        base.localAvatar.startPosHprBroadcast()
        globalClock.tick()
        base.localAvatar.b_setAnimState('TeleportIn', 1, callback = self.teleportInDone)
        base.localAvatar.d_broadcastPositionNow()
        base.localAvatar.b_setParent(ToontownGlobals.SPRender)

    
    def teleportInDone(self):
        if hasattr(self, 'fsm'):
            self.fsm.request(self.nextState, [
                1])
        

    
    def exitTeleportIn(self):
        NametagGlobals.setMasterArrowsOn(1)
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(-1)
        base.localAvatar.stopUpdateSmartCamera()
        base.localAvatar.detachCamera()
        base.localAvatar.stopPosHprBroadcast()

    
    def requestTeleport(self, hoodId, zoneId, shardId, avId):
        loaderId = ZoneUtil.getBranchLoaderName(zoneId)
        whereId = ZoneUtil.getToonWhereName(zoneId)
        if hoodId == ToontownGlobals.MyEstate:
            loaderId = 'safeZoneLoader'
            whereId = 'estate'
        
        self.requestLeave({
            'loader': loaderId,
            'where': whereId,
            'how': 'teleportIn',
            'hoodId': hoodId,
            'zoneId': zoneId,
            'shardId': shardId,
            'avId': avId })

    
    def enterQuest(self, npcToon):
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()
        base.localAvatar.obscureMoveFurnitureButton(1)

    
    def exitQuest(self):
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(-1)

    
    def enterPurchase(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()
        base.localAvatar.obscureMoveFurnitureButton(1)

    
    def exitPurchase(self):
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(-1)

    
    def enterFishing(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()

    
    def exitFishing(self):
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()

    
    def enterBanking(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()
        base.localAvatar.obscureMoveFurnitureButton(1)

    
    def exitBanking(self):
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(-1)

    
    def enterPhone(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()
        base.localAvatar.obscureMoveFurnitureButton(1)

    
    def exitPhone(self):
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(-1)

    
    def enterPet(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        Emote.globalEmote.disableBody(base.localAvatar, 'enterPet')
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()
        FriendsListManager.FriendsListManager.enter(self)

    
    def exitPet(self):
        base.localAvatar.setTeleportAvailable(0)
        Emote.globalEmote.releaseBody(base.localAvatar, 'exitPet')
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        FriendsListManager.FriendsListManager.exit(self)

    
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
        how = base.cr.handlerArgs['how']
        self.fsm.request(how, [
            base.cr.handlerArgs])


