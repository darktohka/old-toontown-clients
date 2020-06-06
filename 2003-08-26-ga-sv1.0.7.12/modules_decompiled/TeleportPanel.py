# File: T (Python 2.2)

from ShowBaseGlobal import *
from DirectGui import *
import ToontownGlobals
import PandaObject
import FSM
import State
import DirectNotifyGlobal
import FriendInviter
import AvatarDetailPanel
import Localizer
import ZoneUtil
globalTeleport = None

def showTeleportPanel(avId, avName, avDisableName):
    global globalTeleport
    if globalTeleport != None:
        globalTeleport.cleanup()
        globalTeleport = None
    
    globalTeleport = TeleportPanel(avId, avName, avDisableName)


def hideTeleportPanel():
    global globalTeleport
    if globalTeleport != None:
        globalTeleport.cleanup()
        globalTeleport = None
    


def unloadTeleportPanel():
    global globalTeleport
    if globalTeleport != None:
        globalTeleport.cleanup()
        globalTeleport = None
    


class TeleportPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('TeleportPanel')
    
    def __init__(self, avId, avName, avDisableName):
        DirectFrame.__init__(self, pos = (0.29999999999999999, 0.10000000000000001, 0.65000000000000002), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.0, 1.0, 0.59999999999999998), text = '', text_wordwrap = 13.5, text_scale = 0.059999999999999998, text_pos = (0.0, 0.17999999999999999))
        messenger.send('releaseDirector')
        self['image'] = getDefaultDialogGeom()
        self.avId = avId
        self.avName = avName
        self.avDisableName = avDisableName
        self.fsm = FSM.FSM('TeleportPanel', [
            State.State('off', self.enterOff, self.exitOff),
            State.State('begin', self.enterBegin, self.exitBegin),
            State.State('checkAvailability', self.enterCheckAvailability, self.exitCheckAvailability),
            State.State('notAvailable', self.enterNotAvailable, self.exitNotAvailable),
            State.State('ignored', self.enterIgnored, self.exitIgnored),
            State.State('notOnline', self.enterNotOnline, self.exitNotOnline),
            State.State('wentAway', self.enterWentAway, self.exitWentAway),
            State.State('self', self.enterSelf, self.exitSelf),
            State.State('unknownHood', self.enterUnknownHood, self.exitUnknownHood),
            State.State('unavailableHood', self.enterUnavailableHood, self.exitUnavailableHood),
            State.State('otherShard', self.enterOtherShard, self.exitOtherShard),
            State.State('teleport', self.enterTeleport, self.exitTeleport)], 'off', 'off')
        FriendInviter.hideFriendInviter()
        AvatarDetailPanel.hideAvatarDetail()
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        self.bOk = DirectButton(self, image = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')), relief = None, text = Localizer.TeleportPanelOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.0, 0.0, -0.10000000000000001), command = self._TeleportPanel__handleOk)
        self.bOk.hide()
        self.bCancel = DirectButton(self, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), relief = None, text = Localizer.TeleportPanelCancel, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.0, 0.0, -0.10000000000000001), command = self._TeleportPanel__handleCancel)
        self.bCancel.hide()
        self.bYes = DirectButton(self, image = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')), relief = None, text = Localizer.TeleportPanelYes, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (-0.14999999999999999, 0.0, -0.14999999999999999), command = self._TeleportPanel__handleYes)
        self.bYes.hide()
        self.bNo = DirectButton(self, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), relief = None, text = Localizer.TeleportPanelNo, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.14999999999999999, 0.0, -0.14999999999999999), command = self._TeleportPanel__handleNo)
        self.bNo.hide()
        buttons.removeNode()
        self.accept(self.avDisableName, self._TeleportPanel__handleDisableAvatar)
        self.show()
        self.fsm.enterInitialState()
        self.fsm.request('begin')

    
    def cleanup(self):
        self.fsm.request('off')
        del self.fsm
        self.ignore(self.avDisableName)
        self.destroy()

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterBegin(self):
        myId = toonbase.localToon.doId
        if self.avId == myId:
            self.fsm.request('self')
        elif toonbase.tcr.doId2do.has_key(self.avId):
            self.fsm.request('checkAvailability')
        elif toonbase.tcr.isFriend(self.avId):
            if toonbase.tcr.isFriendOnline(self.avId):
                self.fsm.request('checkAvailability')
            else:
                self.fsm.request('notOnline')
        else:
            self.fsm.request('wentAway')

    
    def exitBegin(self):
        pass

    
    def enterCheckAvailability(self):
        myId = toonbase.localToon.getDoId()
        toonbase.localToon.d_teleportQuery(myId, sendToId = self.avId)
        self['text'] = Localizer.TeleportPanelCheckAvailability % self.avName
        self.accept('teleportResponse', self._TeleportPanel__teleportResponse)
        self.bCancel.show()

    
    def exitCheckAvailability(self):
        self.ignore('teleportResponse')
        self.bCancel.hide()

    
    def enterNotAvailable(self):
        self['text'] = Localizer.TeleportPanelNotAvailable % self.avName
        self.bOk.show()

    
    def exitNotAvailable(self):
        self.bOk.hide()

    
    def enterIgnored(self):
        self['text'] = Localizer.TeleportPanelIgnored % self.avName
        self.bOk.show()

    
    def exitIgnored(self):
        self.bOk.hide()

    
    def enterNotOnline(self):
        self['text'] = Localizer.TeleportPanelNotOnline % self.avName
        self.bOk.show()

    
    def exitNotOnline(self):
        self.bOk.hide()

    
    def enterWentAway(self):
        self['text'] = Localizer.TeleportPanelWentAway % self.avName
        self.bOk.show()

    
    def exitWentAway(self):
        self.bOk.hide()

    
    def enterUnknownHood(self, hoodId):
        self['text'] = Localizer.TeleportPanelUnknownHood % toonbase.tcr.hoodMgr.getFullnameFromId(hoodId)
        self.bOk.show()

    
    def exitUnknownHood(self):
        self.bOk.hide()

    
    def enterUnavailableHood(self, hoodId):
        self['text'] = Localizer.TeleportPanelUnavailableHood % toonbase.tcr.hoodMgr.getFullnameFromId(hoodId)
        self.bOk.show()

    
    def exitUnavailableHood(self):
        self.bOk.hide()

    
    def enterSelf(self):
        self['text'] = Localizer.TeleportPanelDenySelf
        self.bOk.show()

    
    def exitSelf(self):
        self.bOk.hide()

    
    def enterOtherShard(self, shardId, hoodId, zoneId):
        shardName = toonbase.tcr.getShardName(shardId)
        myShardName = toonbase.tcr.getShardName(toonbase.localToon.defaultShard)
        self['text'] = Localizer.TeleportPanelOtherShard % {
            'avName': self.avName,
            'shardName': shardName,
            'myShardName': myShardName }
        self.bYes.show()
        self.bNo.show()
        self.shardId = shardId
        self.hoodId = hoodId
        self.zoneId = zoneId

    
    def exitOtherShard(self):
        self.bYes.hide()
        self.bNo.hide()

    
    def enterTeleport(self, shardId, hoodId, zoneId):
        if toonbase.localToon.teleportCheat:
            hoodsVisited = ToontownGlobals.Hoods
        else:
            hoodsVisited = toonbase.localToon.hoodsVisited
        canonicalHoodId = ZoneUtil.getCanonicalZoneId(hoodId)
        if hoodId == ToontownGlobals.MyEstate:
            if shardId == toonbase.localToon.defaultShard:
                shardId = None
            
            place = toonbase.tcr.playGame.getPlace()
            place.requestTeleport(hoodId, zoneId, shardId, self.avId)
            unloadTeleportPanel()
        elif canonicalHoodId not in hoodsVisited:
            self.fsm.request('unknownHood', [
                hoodId])
        elif canonicalHoodId not in toonbase.tcr.hoodMgr.getAvailableZones():
            print 'hoodId %d not ready' % hoodId
            self.fsm.request('unavailableHood', [
                hoodId])
        elif shardId != toonbase.localToon.defaultShard:
            toonbase.localToon.reparentTo(hidden)
            toonbase.tcr.gameFSM.request('waitOnEnterResponses', [
                shardId,
                hoodId,
                zoneId,
                self.avId])
        elif shardId == toonbase.localToon.defaultShard:
            shardId = None
        
        place = toonbase.tcr.playGame.getPlace()
        place.requestTeleport(hoodId, zoneId, shardId, self.avId)
        unloadTeleportPanel()
        return None

    
    def exitTeleport(self):
        pass

    
    def _TeleportPanel__handleOk(self):
        unloadTeleportPanel()

    
    def _TeleportPanel__handleCancel(self):
        unloadTeleportPanel()

    
    def _TeleportPanel__handleYes(self):
        self.fsm.request('teleport', [
            self.shardId,
            self.hoodId,
            self.zoneId])

    
    def _TeleportPanel__handleNo(self):
        unloadTeleportPanel()

    
    def _TeleportPanel__teleportResponse(self, avId, available, shardId, hoodId, zoneId):
        if avId != self.avId:
            return None
        
        if available == 0:
            self.fsm.request('notAvailable')
        elif available == 2:
            self.fsm.request('ignored')
        elif shardId != toonbase.localToon.defaultShard:
            self.fsm.request('otherShard', [
                shardId,
                hoodId,
                zoneId])
        else:
            self.fsm.request('teleport', [
                shardId,
                hoodId,
                zoneId])

    
    def _TeleportPanel__handleDisableAvatar(self):
        self.fsm.request('wentAway')


