# File: Q (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.distributed.ToontownMsgTypes import *
from otp.otpbase import OTPGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import PandaObject
from direct.fsm import StateData
from direct.fsm import ClassicFSM
from direct.fsm import State
import ZoneUtil

class QuietZoneState(PandaObject.PandaObject, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('QuietZoneState')
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = ClassicFSM.ClassicFSM('QuietZoneState', [
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
            if zoneId == OTPGlobals.QuietZone:
                self.fsm.request('waitForZoneRedirect', [
                    base.cr.handlerArgs])
            
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            base.cr.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            base.cr.handleQuietZoneGenerateWithRequiredOther(di)
        elif msgType in QUIET_ZONE_IGNORED_LIST:
            self.notify.debug('ignoring unwanted message from previous zone')
        else:
            base.cr.handlePlayGame(msgType, di)

    
    def handleWaitForZoneRedirect(self, msgType, di):
        self.notify.debug('handleWaitForZoneRedirect(' + 'msgType=' + str(msgType) + ', di=' + str(di) + ')')
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            base.cr.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            base.cr.handleQuietZoneGenerateWithRequiredOther(di)
        else:
            base.cr.handlePlayGame(msgType, di)

    
    def handleWaitForSetZoneResponse(self, msgType, di):
        self.notify.debug('handleWaitForSetZoneResponse(' + 'msgType=' + str(msgType) + ', di=' + str(di) + ')')
        if msgType == CLIENT_GET_STATE_RESP:
            di.skipBytes(12)
            zoneId = di.getUint32()
            wantZoneId = base.cr.handlerArgs['zoneId']
            if zoneId == wantZoneId:
                self.notify.debug('handleWaitForSetZoneResponse: response for zoneId: %s' % zoneId)
                self.fsm.request('waitForSetZoneComplete', [
                    base.cr.handlerArgs])
            else:
                self.notify.warning('handleWaitForSetZoneResponse: unwanted zoneId: %s, waiting for: %s' % (zoneId, wantZoneId))
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            base.cr.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            base.cr.handleQuietZoneGenerateWithRequiredOther(di)
        else:
            base.cr.handlePlayGame(msgType, di)

    
    def handleWaitForSetZoneComplete(self, msgType, di):
        self.notify.debug('handleWaitForSetZoneComplete(' + 'msgType=' + str(msgType) + ', di=' + str(di) + ')')
        if msgType == CLIENT_DONE_SET_ZONE_RESP:
            zoneId = di.getUint32()
            wantZoneId = base.cr.handlerArgs['zoneId']
            if zoneId == wantZoneId:
                self.notify.debug('handleWaitForSetZoneComplete: completed zoneId: %s' % zoneId)
                base.localAvatar.startChat()
                messenger.send('setZoneComplete', [
                    zoneId])
                messenger.send(self.doneEvent)
            else:
                self.notify.warning('handleWaitForSetZoneComplete: unwanted zoneId: %s, waiting for: %s' % (zoneId, wantZoneId))
        else:
            base.cr.handlePlayGame(msgType, di)

    
    def enterOff(self):
        self.notify.debug('enterOff()')

    
    def exitOff(self):
        self.notify.debug('exitOff()')

    
    def enterWaitForQuietZoneResponse(self, doneStatus):
        self.notify.debug('enterWaitForQuietZoneResponse(doneStatus=' + str(doneStatus) + ')')
        base.cr.handler = self.handleWaitForQuietZoneResponse
        base.cr.handlerArgs = doneStatus
        base.cr.sendQuietZoneRequest()

    
    def exitWaitForQuietZoneResponse(self):
        self.notify.debug('exitWaitForQuietZoneResponse()')
        base.cr.handler = base.cr.handlePlayGame
        base.cr.handlerArgs = None

    
    def enterWaitForZoneRedirect(self, requestStatus):
        self.notify.debug('enterWaitForZoneRedirect(requestStatus=' + str(requestStatus) + ')')
        base.cr.handler = self.handleWaitForZoneRedirect
        base.cr.handlerArgs = requestStatus
        zoneId = requestStatus['zoneId']
        avId = requestStatus.get('avId', -1)
        allowRedirect = requestStatus.get('allowRedirect', 1)
        if avId != -1:
            allowRedirect = 0
        
        if not (base.cr.welcomeValleyManager):
            newZoneId = ZoneUtil.getCanonicalZoneId(zoneId)
            if newZoneId != zoneId:
                self.gotZoneRedirect(newZoneId)
                return None
            
        
        if allowRedirect and ZoneUtil.isWelcomeValley(zoneId):
            self.notify.info('Requesting AI redirect from zone %s.' % zoneId)
            base.cr.welcomeValleyManager.requestZoneId(zoneId, self.gotZoneRedirect)
        else:
            self.fsm.request('waitForSetZoneResponse', [
                base.cr.handlerArgs])

    
    def gotZoneRedirect(self, zoneId):
        self.notify.info('Redirecting to zone %s.' % zoneId)
        base.cr.handlerArgs['zoneId'] = zoneId
        base.cr.handlerArgs['hoodId'] = ZoneUtil.getHoodId(zoneId)
        self.fsm.request('waitForSetZoneResponse', [
            base.cr.handlerArgs])

    
    def exitWaitForZoneRedirect(self):
        self.notify.debug('exitWaitForZoneRedirect()')
        base.cr.handler = base.cr.handlePlayGame
        base.cr.handlerArgs = None

    
    def enterWaitForSetZoneResponse(self, requestStatus):
        self.notify.debug('enterWaitForSetZoneResponse(requestStatus=' + str(requestStatus) + ')')
        messenger.send('enterWaitForSetZoneResponse', [
            requestStatus])
        base.cr.handler = self.handleWaitForSetZoneResponse
        base.cr.handlerArgs = requestStatus
        zoneId = requestStatus['zoneId']
        base.cr.sendSetZoneMsg(zoneId)
        if base.cr.welcomeValleyManager:
            base.cr.welcomeValleyManager.d_clientSetZone(zoneId)
        

    
    def exitWaitForSetZoneResponse(self):
        self.notify.debug('exitWaitForSetZoneResponse()')
        base.cr.handler = base.cr.handlePlayGame
        base.cr.handlerArgs = None

    
    def enterWaitForSetZoneComplete(self, requestStatus):
        self.notify.debug('enterWaitForSetZoneComplete(requestStatus=' + str(requestStatus) + ')')
        base.cr.handler = self.handleWaitForSetZoneComplete
        base.cr.handlerArgs = requestStatus

    
    def exitWaitForSetZoneComplete(self):
        self.notify.debug('exitWaitForSetZoneComplete()')
        base.cr.handler = base.cr.handlePlayGame
        base.cr.handlerArgs = None


