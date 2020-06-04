# File: Q (Python 2.2)

from ShowBaseGlobal import *
from ToontownMsgTypes import *
import ToontownGlobals
import DirectNotifyGlobal
import PandaObject
import StateData
import FSM
import State
import ZoneUtil

class QuietZoneState(PandaObject.PandaObject, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('QuietZoneState')
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = FSM.FSM('QuietZoneState', [
            State.State('off', self.enterOff, self.exitOff, [
                'waitForQuietZoneResponse']),
            State.State('waitForQuietZoneResponse', self.enterWaitForQuietZoneResponse, self.exitWaitForQuietZoneResponse, [
                'waitForZoneRedirect']),
            State.State('waitForZoneRedirect', self.enterWaitForZoneRedirect, self.exitWaitForZoneRedirect, [
                'waitForSetZoneResponse']),
            State.State('waitForSetZoneResponse', self.enterWaitForSetZoneResponse, self.exitWaitForSetZoneResponse, [
                'waitForSetZoneComplete']),
            State.State('waitForSetZoneComplete', self.enterWaitForSetZoneComplete, self.exitWaitForSetZoneComplete, [
                'off'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def load(self):
        self.notify.debug('load()')

    
    def unload(self):
        self.notify.debug('unload()')
        del self.fsm

    
    def enter(self, requestStatus):
        self.notify.debug('enter(requestStatus=' + str(requestStatus) + ')')
        base.transitions.fadeScreen(1.0)
        self.fsm.request('waitForQuietZoneResponse', [
            requestStatus])

    
    def exit(self):
        self.notify.debug('exit()')
        base.transitions.noFade()
        self.fsm.request('off')

    
    def handleWaitForQuietZoneResponse(self, msgType, di):
        self.notify.debug('handleWaitForQuietZoneResponse(' + 'msgType=' + str(msgType) + ', di=' + str(di) + ')')
        if msgType == CLIENT_GET_STATE_RESP:
            di.skipBytes(12)
            zoneId = di.getUint32()
            if zoneId == ToontownGlobals.QuietZone:
                self.fsm.request('waitForZoneRedirect', [
                    toonbase.tcr.handlerArgs])
            
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            toonbase.tcr.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            toonbase.tcr.handleQuietZoneGenerateWithRequiredOther(di)
        elif msgType in QUIET_ZONE_IGNORED_LIST:
            self.notify.debug('ignoring unwanted message from previous zone')
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def handleWaitForZoneRedirect(self, msgType, di):
        self.notify.debug('handleWaitForZoneRedirect(' + 'msgType=' + str(msgType) + ', di=' + str(di) + ')')
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            toonbase.tcr.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            toonbase.tcr.handleQuietZoneGenerateWithRequiredOther(di)
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def handleWaitForSetZoneResponse(self, msgType, di):
        self.notify.debug('handleWaitForSetZoneResponse(' + 'msgType=' + str(msgType) + ', di=' + str(di) + ')')
        if msgType == CLIENT_GET_STATE_RESP:
            di.skipBytes(12)
            zoneId = di.getUint32()
            wantZoneId = toonbase.tcr.handlerArgs['zoneId']
            if zoneId == wantZoneId:
                self.notify.debug('handleWaitForSetZoneResponse: response for zoneId: %s' % zoneId)
                self.fsm.request('waitForSetZoneComplete', [
                    toonbase.tcr.handlerArgs])
            else:
                self.notify.warning('handleWaitForSetZoneResponse: unwanted zoneId: %s, waiting for: %s' % (zoneId, wantZoneId))
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            toonbase.tcr.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            toonbase.tcr.handleQuietZoneGenerateWithRequiredOther(di)
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def handleWaitForSetZoneComplete(self, msgType, di):
        self.notify.debug('handleWaitForSetZoneComplete(' + 'msgType=' + str(msgType) + ', di=' + str(di) + ')')
        if msgType == CLIENT_DONE_SET_ZONE_RESP:
            zoneId = di.getUint32()
            wantZoneId = toonbase.tcr.handlerArgs['zoneId']
            if zoneId == wantZoneId:
                self.notify.debug('handleWaitForSetZoneComplete: completed zoneId: %s' % zoneId)
                toonbase.localToon.startChat()
                messenger.send('setZoneComplete', [
                    zoneId])
                messenger.send(self.doneEvent)
            else:
                self.notify.warning('handleWaitForSetZoneComplete: unwanted zoneId: %s, waiting for: %s' % (zoneId, wantZoneId))
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def enterOff(self):
        self.notify.debug('enterOff()')

    
    def exitOff(self):
        self.notify.debug('exitOff()')

    
    def enterWaitForQuietZoneResponse(self, doneStatus):
        self.notify.debug('enterWaitForQuietZoneResponse(doneStatus=' + str(doneStatus) + ')')
        toonbase.tcr.handler = self.handleWaitForQuietZoneResponse
        toonbase.tcr.handlerArgs = doneStatus
        toonbase.tcr.sendQuietZoneRequest()

    
    def exitWaitForQuietZoneResponse(self):
        self.notify.debug('exitWaitForQuietZoneResponse()')
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None

    
    def enterWaitForZoneRedirect(self, requestStatus):
        self.notify.debug('enterWaitForZoneRedirect(requestStatus=' + str(requestStatus) + ')')
        toonbase.tcr.handler = self.handleWaitForZoneRedirect
        toonbase.tcr.handlerArgs = requestStatus
        zoneId = requestStatus['zoneId']
        avId = requestStatus.get('avId', -1)
        allowRedirect = requestStatus.get('allowRedirect', 1)
        if avId != -1:
            allowRedirect = 0
        
        if not (toonbase.tcr.welcomeValleyManager):
            newZoneId = ZoneUtil.getCanonicalZoneId(zoneId)
            if newZoneId != zoneId:
                self.gotZoneRedirect(newZoneId)
                return None
            
        
        if allowRedirect and ZoneUtil.isWelcomeValley(zoneId):
            self.notify.info('Requesting AI redirect from zone %s.' % zoneId)
            toonbase.tcr.welcomeValleyManager.requestZoneId(zoneId, self.gotZoneRedirect)
        else:
            self.fsm.request('waitForSetZoneResponse', [
                toonbase.tcr.handlerArgs])

    
    def gotZoneRedirect(self, zoneId):
        self.notify.info('Redirecting to zone %s.' % zoneId)
        toonbase.tcr.handlerArgs['zoneId'] = zoneId
        toonbase.tcr.handlerArgs['hoodId'] = ZoneUtil.getHoodId(zoneId)
        self.fsm.request('waitForSetZoneResponse', [
            toonbase.tcr.handlerArgs])

    
    def exitWaitForZoneRedirect(self):
        self.notify.debug('exitWaitForZoneRedirect()')
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None

    
    def enterWaitForSetZoneResponse(self, requestStatus):
        self.notify.debug('enterWaitForSetZoneResponse(requestStatus=' + str(requestStatus) + ')')
        messenger.send('enterWaitForSetZoneResponse', [
            requestStatus])
        toonbase.tcr.handler = self.handleWaitForSetZoneResponse
        toonbase.tcr.handlerArgs = requestStatus
        zoneId = requestStatus['zoneId']
        toonbase.tcr.sendSetZoneMsg(zoneId)
        if toonbase.tcr.welcomeValleyManager:
            toonbase.tcr.welcomeValleyManager.d_clientSetZone(zoneId)
        

    
    def exitWaitForSetZoneResponse(self):
        self.notify.debug('exitWaitForSetZoneResponse()')
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None

    
    def enterWaitForSetZoneComplete(self, requestStatus):
        self.notify.debug('enterWaitForSetZoneComplete(requestStatus=' + str(requestStatus) + ')')
        toonbase.tcr.handler = self.handleWaitForSetZoneComplete
        toonbase.tcr.handlerArgs = requestStatus

    
    def exitWaitForSetZoneComplete(self):
        self.notify.debug('exitWaitForSetZoneComplete()')
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None


