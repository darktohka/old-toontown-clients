# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from direct.showbase import PandaObject
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
import ToonAvatarDetailPanel
from toontown.toonbase import TTLocalizer
from toontown.hood import ZoneUtil
globalTeleport = None

def showTeleportPanel(avId, avName, avDisableName):
    global globalTeleport
    if globalTeleport != None:
        globalTeleport.cleanup()
        globalTeleport = None
    
    globalTeleport = ToonTeleportPanel(avId, avName, avDisableName)


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
    


class ToonTeleportPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonTeleportPanel')
    
    def __init__(self, avId, avName, avDisableName):
        DirectFrame.__init__(self, pos = (0.29999999999999999, 0.10000000000000001, 0.65000000000000002), image_color = ToontownGlobals.GlobalDialogColor, image_scale = (1.0, 1.0, 0.59999999999999998), text = '', text_wordwrap = 13.5, text_scale = 0.059999999999999998, text_pos = (0.0, 0.17999999999999999))
        messenger.send('releaseDirector')
        self['image'] = getDefaultDialogGeom()
        self.avId = avId
        self.avName = avName
        self.avDisableName = avDisableName
        self.fsm = ClassicFSM.ClassicFSM('ToonTeleportPanel', [
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
        FriendInviter = FriendInviter
        import toontown.friends
        FriendInviter.hideFriendInviter()
        ToonAvatarDetailPanel.hideAvatarDetail()
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        self.bOk = DirectButton(self, image = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')), relief = None, text = TTLocalizer.TeleportPanelOK, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.0, 0.0, -0.10000000000000001), command = self._ToonTeleportPanel__handleOk)
        self.bOk.hide()
        self.bCancel = DirectButton(self, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), relief = None, text = TTLocalizer.TeleportPanelCancel, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.0, 0.0, -0.10000000000000001), command = self._ToonTeleportPanel__handleCancel)
        self.bCancel.hide()
        self.bYes = DirectButton(self, image = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr')), relief = None, text = TTLocalizer.TeleportPanelYes, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (-0.14999999999999999, 0.0, -0.14999999999999999), command = self._ToonTeleportPanel__handleYes)
        self.bYes.hide()
        self.bNo = DirectButton(self, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), relief = None, text = TTLocalizer.TeleportPanelNo, text_scale = 0.050000000000000003, text_pos = (0.0, -0.10000000000000001), pos = (0.14999999999999999, 0.0, -0.14999999999999999), command = self._ToonTeleportPanel__handleNo)
        self.bNo.hide()
        buttons.removeNode()
        self.accept(self.avDisableName, self._ToonTeleportPanel__handleDisableAvatar)
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
        myId = base.localAvatar.doId
        if self.avId == myId:
            self.fsm.request('self')
        elif base.cr.doId2do.has_key(self.avId):
            self.fsm.request('checkAvailability')
        elif base.cr.isFriend(self.avId):
            if base.cr.isFriendOnline(self.avId):
                self.fsm.request('checkAvailability')
            else:
                self.fsm.request('notOnline')
        else:
            self.fsm.request('wentAway')

    
    def exitBegin(self):
        pass

    
    def enterCheckAvailability(self):
        myId = base.localAvatar.getDoId()
        base.localAvatar.d_teleportQuery(myId, sendToId = self.avId)
        self['text'] = TTLocalizer.TeleportPanelCheckAvailability % self.avName
        self.accept('teleportResponse', self._ToonTeleportPanel__teleportResponse)
        self.bCancel.show()

    
    def exitCheckAvailability(self):
        self.ignore('teleportResponse')
        self.bCancel.hide()

    
    def enterNotAvailable(self):
        self['text'] = TTLocalizer.TeleportPanelNotAvailable % self.avName
        self.bOk.show()

    
    def exitNotAvailable(self):
        self.bOk.hide()

    
    def enterIgnored(self):
        self['text'] = TTLocalizer.TeleportPanelIgnored % self.avName
        self.bOk.show()

    
    def exitIgnored(self):
        self.bOk.hide()

    
    def enterNotOnline(self):
        self['text'] = TTLocalizer.TeleportPanelNotOnline % self.avName
        self.bOk.show()

    
    def exitNotOnline(self):
        self.bOk.hide()

    
    def enterWentAway(self):
        self['text'] = TTLocalizer.TeleportPanelWentAway % self.avName
        self.bOk.show()

    
    def exitWentAway(self):
        self.bOk.hide()

    
    def enterUnknownHood(self, hoodId):
        self['text'] = TTLocalizer.TeleportPanelUnknownHood % base.cr.hoodMgr.getFullnameFromId(hoodId)
        self.bOk.show()

    
    def exitUnknownHood(self):
        self.bOk.hide()

    
    def enterUnavailableHood(self, hoodId):
        self['text'] = TTLocalizer.TeleportPanelUnavailableHood % base.cr.hoodMgr.getFullnameFromId(hoodId)
        self.bOk.show()

    
    def exitUnavailableHood(self):
        self.bOk.hide()

    
    def enterSelf(self):
        self['text'] = TTLocalizer.TeleportPanelDenySelf
        self.bOk.show()

    
    def exitSelf(self):
        self.bOk.hide()

    
    def enterOtherShard(self, shardId, hoodId, zoneId):
        shardName = base.cr.getShardName(shardId)
        myShardName = base.cr.getShardName(base.localAvatar.defaultShard)
        self['text'] = TTLocalizer.TeleportPanelOtherShard % {
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
        if base.localAvatar.teleportCheat:
            hoodsVisited = ToontownGlobals.Hoods
        else:
            hoodsVisited = base.localAvatar.hoodsVisited
        canonicalHoodId = ZoneUtil.getCanonicalZoneId(hoodId)
        if hoodId == ToontownGlobals.MyEstate:
            if shardId == base.localAvatar.defaultShard:
                shardId = None
            
            place = base.cr.playGame.getPlace()
            place.requestTeleport(hoodId, zoneId, shardId, self.avId)
            unloadTeleportPanel()
        elif canonicalHoodId not in hoodsVisited:
            self.fsm.request('unknownHood', [
                hoodId])
        elif canonicalHoodId not in base.cr.hoodMgr.getAvailableZones():
            print 'hoodId %d not ready' % hoodId
            self.fsm.request('unavailableHood', [
                hoodId])
        elif shardId != base.localAvatar.defaultShard:
            base.localAvatar.detachNode()
            base.cr.gameFSM.request('waitOnEnterResponses', [
                shardId,
                hoodId,
                zoneId,
                self.avId])
        elif shardId == base.localAvatar.defaultShard:
            shardId = None
        
        place = base.cr.playGame.getPlace()
        place.requestTeleport(hoodId, zoneId, shardId, self.avId)
        unloadTeleportPanel()
        return None

    
    def exitTeleport(self):
        pass

    
    def _ToonTeleportPanel__handleOk(self):
        unloadTeleportPanel()

    
    def _ToonTeleportPanel__handleCancel(self):
        unloadTeleportPanel()

    
    def _ToonTeleportPanel__handleYes(self):
        self.fsm.request('teleport', [
            self.shardId,
            self.hoodId,
            self.zoneId])

    
    def _ToonTeleportPanel__handleNo(self):
        unloadTeleportPanel()

    
    def _ToonTeleportPanel__teleportResponse(self, avId, available, shardId, hoodId, zoneId):
        if avId != self.avId:
            return None
        
        if available == 0:
            self.fsm.request('notAvailable')
        elif available == 2:
            self.fsm.request('ignored')
        elif shardId != base.localAvatar.defaultShard:
            self.fsm.request('otherShard', [
                shardId,
                hoodId,
                zoneId])
        else:
            self.fsm.request('teleport', [
                shardId,
                hoodId,
                zoneId])

    
    def _ToonTeleportPanel__handleDisableAvatar(self):
        self.fsm.request('wentAway')


