# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from direct.showbase import PandaObject
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
import DistributedToon
from toontown.friends import FriendInviter
import ToonTeleportPanel
from toontown.toonbase import TTLocalizer
from toontown.hood import ZoneUtil
from toontown.toonbase.ToontownBattleGlobals import Tracks, Levels
globalAvatarDetail = None

def showAvatarDetail(avId, avName):
    global globalAvatarDetail
    if globalAvatarDetail != None:
        globalAvatarDetail.cleanup()
        globalAvatarDetail = None
    
    globalAvatarDetail = ToonAvatarDetailPanel(avId, avName)


def hideAvatarDetail():
    global globalAvatarDetail
    if globalAvatarDetail != None:
        globalAvatarDetail.cleanup()
        globalAvatarDetail = None
    


def unloadAvatarDetail():
    global globalAvatarDetail
    if globalAvatarDetail != None:
        globalAvatarDetail.cleanup()
        globalAvatarDetail = None
    


class ToonAvatarDetailPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonAvatarDetailPanel')
    
    def __init__(self, avId, avName, parent = aspect2d, **kw):
        buttons = loader.loadModelOnce('phase_3/models/gui/dialog_box_buttons_gui')
        gui = loader.loadModelOnce('phase_3.5/models/gui/avatar_panel_gui')
        detailPanel = gui.find('**/avatarInfoPanel')
        optiondefs = (('pos', (0.52500000000000002, 0.0, 0.52500000000000002), None), ('scale', 0.5, None), ('relief', None, None), ('image', detailPanel, None), ('image_color', GlobalDialogColor, None), ('text', '', None), ('text_wordwrap', 10.4, None), ('text_scale', 0.13200000000000001, None), ('text_pos', (0.0, 0.75), None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.dataText = DirectLabel(self, text = '', text_scale = 0.089999999999999997, text_align = TextNode.ALeft, text_wordwrap = 15, relief = None, pos = (-0.69999999999999996, 0.0, 0.55000000000000004))
        self.avId = avId
        self.avName = avName
        self.avatar = None
        self.createdAvatar = None
        self.fsm = ClassicFSM.ClassicFSM('ToonAvatarDetailPanel', [
            State.State('off', self.enterOff, self.exitOff, [
                'begin']),
            State.State('begin', self.enterBegin, self.exitBegin, [
                'query',
                'data',
                'off']),
            State.State('query', self.enterQuery, self.exitQuery, [
                'data',
                'invalid',
                'off']),
            State.State('data', self.enterData, self.exitData, [
                'off']),
            State.State('invalid', self.enterInvalid, self.exitInvalid, [
                'off'])], 'off', 'off')
        ToonTeleportPanel.hideTeleportPanel()
        FriendInviter.hideFriendInviter()
        self.bCancel = DirectButton(self, image = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), relief = None, text = TTLocalizer.AvatarDetailPanelCancel, text_scale = 0.050000000000000003, text_pos = (0.12, -0.01), pos = (-0.68000000000000005, 0.0, -0.76000000000000001), scale = 2.0, command = self._ToonAvatarDetailPanel__handleCancel)
        self.bCancel.hide()
        self.initialiseoptions(ToonAvatarDetailPanel)
        self.fsm.enterInitialState()
        self.fsm.request('begin')
        buttons.removeNode()
        gui.removeNode()

    
    def cleanup(self):
        if self.fsm:
            self.fsm.request('off')
            self.fsm = None
            base.cr.cancelAvatarDetailsRequest(self.avatar)
        
        if self.createdAvatar:
            self.avatar.delete()
            self.createdAvatar = None
        
        self.destroy()

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterBegin(self):
        myId = base.localAvatar.doId
        self['text'] = self.avName
        if self.avId == myId:
            self.avatar = base.localAvatar
            self.createdAvatar = 0
            self.fsm.request('data')
        else:
            self.fsm.request('query')

    
    def exitBegin(self):
        pass

    
    def enterQuery(self):
        self.dataText['text'] = TTLocalizer.AvatarDetailPanelLookup % self.avName
        self.bCancel.show()
        self.avatar = base.cr.doId2do.get(self.avId)
        if self.avatar != None and not (self.avatar.ghostMode):
            self.createdAvatar = 0
        else:
            self.avatar = DistributedToon.DistributedToon(base.cr)
            self.createdAvatar = 1
            self.avatar.doId = self.avId
        base.cr.getAvatarDetails(self.avatar, self._ToonAvatarDetailPanel__handleAvatarDetails)

    
    def exitQuery(self):
        self.bCancel.hide()

    
    def enterData(self):
        self.bCancel['text'] = TTLocalizer.AvatarDetailPanelClose
        self.bCancel.show()
        self._ToonAvatarDetailPanel__showData()

    
    def exitData(self):
        self.bCancel.hide()

    
    def enterInvalid(self):
        self.dataText['text'] = TTLocalizer.AvatarDetailPanelFailedLookup % self.avName

    
    def exitInvalid(self):
        self.bCancel.hide()

    
    def _ToonAvatarDetailPanel__handleCancel(self):
        unloadAvatarDetail()

    
    def _ToonAvatarDetailPanel__handleAvatarDetails(self, gotData, avatar):
        if not (self.fsm) or avatar != self.avatar:
            self.notify.warning('Ignoring unexpected request for avatar %s' % avatar.doId)
            return None
        
        if gotData:
            self.fsm.request('data')
        else:
            self.fsm.request('invalid')

    
    def _ToonAvatarDetailPanel__showData(self):
        av = self.avatar
        online = 1
        if base.cr.isFriend(self.avId):
            online = base.cr.isFriendOnline(self.avId)
        
        if online:
            shardName = base.cr.getShardName(av.defaultShard)
            hoodName = base.cr.hoodMgr.getFullnameFromId(av.lastHood)
            if ZoneUtil.isWelcomeValley(av.lastHood):
                shardName = '%s (%s)' % (TTLocalizer.WelcomeValley[-1], shardName)
            
            text = TTLocalizer.AvatarDetailPanelOnline % {
                'district': shardName,
                'location': hoodName }
        else:
            text = TTLocalizer.AvatarDetailPanelOffline
        self.dataText['text'] = text
        self._ToonAvatarDetailPanel__updateTrackInfo()
        self._ToonAvatarDetailPanel__updateTrophyInfo()
        self._ToonAvatarDetailPanel__updateLaffInfo()

    
    def _ToonAvatarDetailPanel__updateLaffInfo(self):
        avatar = self.avatar
        messenger.send('updateLaffMeter', [
            avatar,
            avatar.hp,
            avatar.maxHp])

    
    def _ToonAvatarDetailPanel__updateTrackInfo(self):
        xOffset = -0.32181399999999999
        xSpacing = 0.18636280298233032
        yOffset = 0.19352
        ySpacing = -0.12625433504581451
        inventory = self.avatar.inventory
        inventoryModels = loader.loadModelOnce('phase_3.5/models/gui/inventory_gui')
        buttonModel = inventoryModels.find('**/InventoryButtonUp')
        for track in range(0, len(Tracks)):
            DirectLabel(parent = self, relief = None, text = TextEncoder.upper(TTLocalizer.BattleGlobalTracks[track]), text_scale = 0.066000000000000003, text_align = TextNode.ALeft, pos = (-0.70999999999999996, 0, 0.17000000000000001 + track * ySpacing))
            if self.avatar.hasTrackAccess(track):
                (curExp, nextExp) = inventory.getCurAndNextExpValues(track)
                for item in range(0, len(Levels[track])):
                    level = Levels[track][item]
                    if curExp >= level:
                        numItems = inventory.numItem(track, item)
                        if numItems == 0:
                            image_color = Vec4(0.5, 0.5, 0.5, 1)
                            geom_color = Vec4(0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.5)
                        else:
                            image_color = Vec4(0, 0.59999999999999998, 1, 1)
                            geom_color = None
                        DirectLabel(parent = self, image = buttonModel, image_scale = (0.92000000000000004, 1, 1), image_color = image_color, geom = inventory.invModels[track][item], geom_color = geom_color, geom_scale = 0.59999999999999998, relief = None, pos = (xOffset + item * xSpacing, 0, yOffset + track * ySpacing))
                    else:
                        break
                
            
        

    
    def _ToonAvatarDetailPanel__updateTrophyInfo(self):
        if self.createdAvatar:
            return None
        
        if self.avatar.trophyScore >= TrophyStarLevels[2]:
            color = TrophyStarColors[2]
        elif self.avatar.trophyScore >= TrophyStarLevels[1]:
            color = TrophyStarColors[1]
        elif self.avatar.trophyScore >= TrophyStarLevels[0]:
            color = TrophyStarColors[0]
        else:
            color = None
        if color:
            gui = loader.loadModelOnce('phase_3.5/models/gui/avatar_panel_gui')
            star = gui.find('**/avatarStar')
            self.star = DirectLabel(parent = self, image = star, image_color = color, pos = (0.61016499999999996, 0, -0.76067799999999997), scale = 0.90000000000000002, relief = None)
            gui.removeNode()
        


