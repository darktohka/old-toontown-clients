# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.gui.DirectGui import *
from direct.showbase import PandaObject
import ToonHead
from toontown.friends import FriendHandle
import LaffMeter
from otp.avatar import Avatar
from direct.distributed import DistributedObject
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from otp.friends import FriendSecret
import ToonAvatarDetailPanel
from otp.avatar import AvatarPanel

class ToonAvatarPanel(AvatarPanel.AvatarPanel):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonAvatarPanel')
    notify.setInfo(True)
    
    def __init__(self, avatar):
        FriendsListPanel = FriendsListPanel
        import toontown.friends
        AvatarPanel.AvatarPanel.__init__(self, avatar, FriendsListPanel = FriendsListPanel)
        self.notify.info('Opening toon panel, avId=%d' % self.avId)
        self.laffMeter = None
        wantsLaffMeter = hasattr(avatar, 'hp')
        if not hasattr(avatar, 'style'):
            AvatarPanel.AvatarPanel.cleanup(self)
            return None
        
        base.localAvatar.obscureFriendsListButton(1)
        gui = loader.loadModelOnce('phase_3.5/models/gui/avatar_panel_gui')
        self.frame = DirectFrame(image = gui.find('**/avatar_panel'), relief = None, pos = (1.1000000000000001, 100, 0.52500000000000002))
        disabledImageColor = Vec4(1, 1, 1, 0.40000000000000002)
        text0Color = Vec4(1, 1, 1, 1)
        text1Color = Vec4(0.5, 1, 0.5, 1)
        text2Color = Vec4(1, 1, 0.5, 1)
        text3Color = Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1)
        self.head = self.frame.attachNewNode('head')
        self.head.setPos(0.02, 0, 0.28999999999999998)
        self.headModel = ToonHead.ToonHead()
        self.headModel.setupHead(avatar.style, forGui = 1)
        self.headModel.fitAndCenterHead(0.17499999999999999, forGui = 1)
        self.headModel.reparentTo(self.head)
        self.headModel.startBlink()
        self.headModel.startLookAround()
        self.healthText = DirectLabel(parent = self.frame, text = '', pos = (0.059999999999999998, 0, 0.16500000000000001), text_pos = (0, 0), text_scale = 0.050000000000000003)
        self.healthText.hide()
        self.nameLabel = DirectLabel(parent = self.frame, pos = (0.012500000000000001, 0, 0.38500000000000001), relief = None, text = self.avName, text_font = avatar.getFont(), text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0), text_scale = 0.047, text_wordwrap = 7.5, text_shadow = (1, 1, 1, 1))
        self.closeButton = DirectButton(parent = self.frame, image = (gui.find('**/CloseBtn_UP'), gui.find('**/CloseBtn_DN'), gui.find('**/CloseBtn_Rllvr'), gui.find('**/CloseBtn_UP')), relief = None, pos = (0.15764400000000001, 0, -0.37916699999999998), command = self._ToonAvatarPanel__handleClose)
        self.petButton = DirectButton(parent = self.frame, image = (gui.find('**/ChtBx_BackBtn_UP'), gui.find('**/ChtBx_BackBtn_DN'), gui.find('**/ChtBx_BackBtn_Rllvr'), gui.find('**/ChtBx_BackBtn_UP')), relief = None, pos = (0.02, -0.20000000000000001, -0.37916699999999998), text = ('', TTLocalizer.AvatarPanelPet, TTLocalizer.AvatarPanelPet, ''), text_fg = text2Color, text_shadow = (0, 0, 0, 1), text_scale = 0.050000000000000003, text_pos = (0.0, 0.044999999999999998), command = self._ToonAvatarPanel__handleToPet)
        if base.wantPets:
            pass
        if not avatar.hasPet():
            self.petButton['state'] = DISABLED
            self.petButton.hide()
        
        self.friendButton = DirectButton(parent = self.frame, image = (gui.find('**/Frnds_Btn_UP'), gui.find('**/Frnds_Btn_DN'), gui.find('**/Frnds_Btn_RLVR'), gui.find('**/Frnds_Btn_UP')), image3_color = disabledImageColor, relief = None, text = TTLocalizer.AvatarPanelFriends, text_scale = TTLocalizer.TAPfriendButton, pos = (-0.10299999999999999, 0, 0.096000000000000002), text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_pos = (0.059999999999999998, -0.02), text_align = TextNode.ALeft, command = self._ToonAvatarPanel__handleFriend)
        self.whisperButton = DirectButton(parent = self.frame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR'), gui.find('**/ChtBx_ChtBtn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.10299999999999999, 0, -0.090499999999999997), text = TTLocalizer.AvatarPanelWhisper, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = TTLocalizer.TAPwhisperButton, text_pos = (0.059999999999999998, -0.02), text_align = TextNode.ALeft, command = self._ToonAvatarPanel__handleWhisper)
        self.secretsButton = DirectButton(parent = self.frame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR'), gui.find('**/ChtBx_ChtBtn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.10299999999999999, 0, -0.1875), text = TTLocalizer.AvatarPanelSecrets, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = TTLocalizer.TAPsecretsButton, text_pos = (0.059999999999999998, -0.02), text_align = TextNode.ALeft, command = self._ToonAvatarPanel__handleSecrets)
        self.goToButton = DirectButton(parent = self.frame, image = (gui.find('**/Go2_Btn_UP'), gui.find('**/Go2_Btn_DN'), gui.find('**/Go2_Btn_RLVR'), gui.find('**/Go2_Btn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.10299999999999999, 0, 0.0029399999999999999), text = TTLocalizer.AvatarPanelGoTo, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = TTLocalizer.TAPgoToButton, text_pos = (0.059999999999999998, -0.02), text_align = TextNode.ALeft, command = self._ToonAvatarPanel__handleGoto)
        if not base.localAvatar.isTeleportAllowed():
            self.goToButton['state'] = DISABLED
        
        self.ignoreButton = DirectButton(parent = self.frame, image = (gui.find('**/Ignore_Btn_UP'), gui.find('**/Ignore_Btn_DN'), gui.find('**/Ignore_Btn_RLVR'), gui.find('**/Ignore_Btn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.103697, 0, -0.27487499999999998), text = TTLocalizer.AvatarPanelIgnore, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = TTLocalizer.TAPignoreButton, text_pos = (0.059999999999999998, -0.02), text_align = TextNode.ALeft, command = self._ToonAvatarPanel__handleIgnore)
        self.ignoreButton.hide()
        self.detailButton = DirectButton(parent = self.frame, image = (gui.find('**/ChtBx_BackBtn_UP'), gui.find('**/ChtBx_BackBtn_DN'), gui.find('**/ChtBx_BackBtn_Rllvr'), gui.find('**/ChtBx_BackBtn_UP')), relief = None, pos = (-0.133773, 0, -0.38713199999999998), command = self._ToonAvatarPanel__handleDetails)
        gui.removeNode()
        if wantsLaffMeter:
            self._ToonAvatarPanel__makeLaffMeter(avatar)
            self._ToonAvatarPanel__updateHp(avatar.hp, avatar.maxHp)
            self.healthText.show()
            self.laffMeter.show()
        
        menuX = -0.050000000000000003
        menuScale = 0.064000000000000001
        if self.avGenerateName:
            self.accept(self.avGenerateName, self._ToonAvatarPanel__handleGenerateAvatar)
        
        if self.avHpChangeName:
            self.accept(self.avHpChangeName, self._ToonAvatarPanel__updateHp)
        
        self.accept('updateLaffMeter', self._ToonAvatarPanel__updateLaffMeter)
        self.frame.show()
        messenger.send('avPanelDone')

    
    def disableAll(self):
        self.detailButton['state'] = DISABLED
        self.ignoreButton['state'] = DISABLED
        self.goToButton['state'] = DISABLED
        self.secretsButton['state'] = DISABLED
        self.whisperButton['state'] = DISABLED
        self.petButton['state'] = DISABLED
        self.friendButton['state'] = DISABLED
        self.closeButton['state'] = DISABLED

    
    def cleanup(self):
        if not hasattr(self, 'frame') or self.frame == None:
            return None
        
        self.notify.info('Clean up toon panel, avId=%d' % self.avId)
        ToonAvatarDetailPanel.unloadAvatarDetail()
        self.frame.destroy()
        del self.frame
        self.frame = None
        self.head.removeNode()
        del self.head
        self.headModel.stopBlink()
        self.headModel.stopLookAroundNow()
        self.headModel.delete()
        del self.headModel
        base.localAvatar.obscureFriendsListButton(-1)
        self.laffMeter = None
        self.ignore('updateLaffMeter')
        if hasattr(self.avatar, 'bFake') and self.avatar.bFake:
            self.avatar.delete()
        
        AvatarPanel.AvatarPanel.cleanup(self)
        return None

    
    def _ToonAvatarPanel__handleGoto(self):
        if base.localAvatar.isTeleportAllowed():
            base.localAvatar.chatMgr.noWhisper()
            messenger.send('gotoAvatar', [
                self.avId,
                self.avName,
                self.avDisableName])
        

    
    def _ToonAvatarPanel__handleToPet(self):
        toonAvatar = self.avatar
        petAvatar = base.cr.doId2do.get(toonAvatar.getPetId())
        self.disableAll()
        PetDetail = PetDetail
        import toontown.pets
        PetDetail.PetDetail(toonAvatar.getPetId(), self._ToonAvatarPanel__petDetailsLoaded)

    
    def _ToonAvatarPanel__petDetailsLoaded(self, avatar):
        self.cleanup()
        if avatar:
            messenger.send('clickedNametag', [
                avatar])
        

    
    def _ToonAvatarPanel__handleWhisper(self):
        base.localAvatar.chatMgr.whisperTo(self.avName, self.avId)

    
    def _ToonAvatarPanel__handleSecrets(self):
        base.localAvatar.chatMgr.noWhisper()
        FriendSecret.showFriendSecret()

    
    def _ToonAvatarPanel__handleFriend(self):
        base.localAvatar.chatMgr.noWhisper()
        messenger.send('friendAvatar', [
            self.avId,
            self.avName,
            self.avDisableName])

    
    def _ToonAvatarPanel__handleIgnore(self):
        print 'Ignore.'

    
    def _ToonAvatarPanel__handleDetails(self):
        base.localAvatar.chatMgr.noWhisper()
        messenger.send('avatarDetails', [
            self.avId,
            self.avName])

    
    def _ToonAvatarPanel__handleDisableAvatar(self):
        if not base.cr.isFriend(self.avId):
            self.cleanup()
            AvatarPanel.currentAvatarPanel = None
        else:
            self.healthText.hide()
            if self.laffMeter != None:
                self.laffMeter.stop()
                self.laffMeter.destroy()
                self.laffMeter = None
            

    
    def _ToonAvatarPanel__handleGenerateAvatar(self, avatar):
        self._ToonAvatarPanel__updateLaffMeter(avatar, avatar.hp, avatar.maxHp)

    
    def _ToonAvatarPanel__updateLaffMeter(self, avatar, hp, maxHp):
        if self.laffMeter == None:
            self._ToonAvatarPanel__makeLaffMeter(avatar)
        
        self._ToonAvatarPanel__updateHp(avatar.hp, avatar.maxHp)
        self.laffMeter.show()
        self.healthText.show()

    
    def _ToonAvatarPanel__makeLaffMeter(self, avatar):
        self.laffMeter = LaffMeter.LaffMeter(avatar.style, avatar.hp, avatar.maxHp)
        self.laffMeter.reparentTo(self.frame)
        self.laffMeter.setPos(-0.10000000000000001, 0, 0.20499999999999999)
        self.laffMeter.setScale(0.029999999999999999)

    
    def _ToonAvatarPanel__updateHp(self, hp, maxHp):
        if self.laffMeter != None and hp != None and maxHp != None:
            self.laffMeter.adjustFace(hp, maxHp)
            self.healthText['text'] = '%d / %d' % (hp, maxHp)
        

    
    def _ToonAvatarPanel__handleClose(self):
        self.cleanup()
        AvatarPanel.currentAvatarPanel = None
        if self.friendsListShown:
            self.FriendsListPanel.showFriendsList()
        


