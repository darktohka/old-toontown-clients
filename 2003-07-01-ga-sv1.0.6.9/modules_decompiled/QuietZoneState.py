# File: Q (Python 2.2)

from ShowBaseGlobal import *
from ToontownMsgTypes import *
import ToontownGlobals
import DirectNotifyGlobal
import PandaObject
import StateData
import FSM
import State

class QuietZoneState(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = FSM.FSM('QuietZoneState', [
            State.State('off', self.enterOff, self.exitOff, [
                'waitForQuietZoneResponse']),
            State.State('waitForQuietZoneResponse', self.enterWaitForQuietZoneResponse, self.exitWaitForQuietZoneResponse, [
                'waitForSetZoneResponse']),
            State.State('waitForSetZoneResponse', self.enterWaitForSetZoneResponse, self.exitWaitForSetZoneResponse, [
                'waitForSetZoneComplete']),
            State.State('waitForSetZoneComplete', self.enterWaitForSetZoneComplete, self.exitWaitForSetZoneComplete, [
                'off'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def load(self):
        pass

    
    def unload(self):
        del self.fsm

    
    def enter(self, requestStatus):
        base.transitions.fadeScreen(1.0)
        self.fsm.request('waitForQuietZoneResponse', [
            requestStatus])

    
    def exit(self):
        base.transitions.noFade()
        self.fsm.request('off')

    
    def handleWaitForQuietZoneResponse(self, msgType, di):
        if msgType == CLIENT_GET_STATE_RESP:
            di.skipBytes(12)
            zoneId = di.getUint16()
            if zoneId == ToontownGlobals.QuietZone:
                self.fsm.request('waitForSetZoneResponse', [
                    toonbase.tcr.handlerArgs])
            
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            toonbase.tcr.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            toonbase.tcr.handleQuietZoneGenerateWithRequiredOther(di)
        elif msgType in QUIET_ZONE_IGNORED_LIST:
            pass
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def handleWaitForSetZoneResponse(self, msgType, di):
        if msgType == CLIENT_GET_STATE_RESP:
            di.skipBytes(12)
            zoneId = di.getUint16()
            wantZoneId = toonbase.tcr.handlerArgs['zoneId']
            if zoneId == wantZoneId:
                self.fsm.request('waitForSetZoneComplete', [
                    toonbase.tcr.handlerArgs])
            
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            toonbase.tcr.handleQuietZoneGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            toonbase.tcr.handleQuietZoneGenerateWithRequiredOther(di)
        elif msgType in QUIET_ZONE_IGNORED_LIST:
            pass
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def handleWaitForSetZoneComplete(self, msgType, di):
        if msgType == CLIENT_DONE_SET_ZONE_RESP:
            zoneId = di.getUint16()
            wantZoneId = toonbase.tcr.handlerArgs['zoneId']
            if zoneId == wantZoneId:
                toonbase.localToon.startChat()
                messenger.send(self.doneEvent)
            
        else:
            toonbase.tcr.handlePlayGame(msgType, di)

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterWaitForQuietZoneResponse(self, doneStatus):
        toonbase.tcr.handler = self.handleWaitForQuietZoneResponse
        toonbase.tcr.handlerArgs = doneStatus
        toonbase.tcr.sendQuietZoneRequest()

    
    def exitWaitForQuietZoneResponse(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None

    
    def enterWaitForSetZoneResponse(self, requestStatus):
        messenger.send('enterWaitForSetZoneResponse', [
            requestStatus])
        toonbase.tcr.handler = self.handleWaitForSetZoneResponse
        toonbase.tcr.handlerArgs = requestStatus
        zoneId = requestStatus['zoneId']
        toonbase.tcr.sendSetZoneMsg(zoneId)

    
    def exitWaitForSetZoneResponse(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None

    
    def enterWaitForSetZoneComplete(self, requestStatus):
        toonbase.tcr.handler = self.handleWaitForSetZoneComplete
        toonbase.tcr.handlerArgs = requestStatus

    
    def exitWaitForSetZoneComplete(self):
        toonbase.tcr.handler = toonbase.tcr.handlePlayGame
        toonbase.tcr.handlerArgs = None


