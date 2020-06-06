# File: A (Python 2.2)

from ShowBaseGlobal import *
from DirectGui import *
import PandaObject
import ToonHead
import FriendHandle
import LaffMeter
import Avatar
import DistributedObject
import FriendsListPanel
import ToontownGlobals
import AvatarDNA
import Localizer
import FriendSecret
import AvatarDetailPanel

class AvatarPanel(PandaObject.PandaObject):
    currentAvatarPanel = None
    
    def __init__(self, avatar):
        if AvatarPanel.currentAvatarPanel:
            AvatarPanel.currentAvatarPanel.cleanup()
        
        AvatarPanel.currentAvatarPanel = self
        self.friendsListShown = FriendsListPanel.isFriendsListShown()
        FriendsListPanel.hideFriendsList()
        self.laffMeter = None
        self.avName = avatar.getName()
        if isinstance(avatar, DistributedObject.DistributedObject) or isinstance(avatar, FriendHandle.FriendHandle):
            self.avId = avatar.doId
            self.avDisableName = avatar.uniqueName('disable')
            self.avGenerateName = avatar.uniqueName('generate')
            self.avHpChangeName = avatar.uniqueName('hpChange')
            if toonbase.tcr.doId2do.has_key(self.avId):
                avatar = toonbase.tcr.doId2do[self.avId]
            
        else:
            self.avDisableName = None
            self.avGenerateName = None
            self.avHpChangeName = None
            self.avId = None
        import Toon
        if not isinstance(avatar, Toon.Toon):
            pass
        self.isToon = isinstance(avatar, FriendHandle.FriendHandle)
        wantsLaffMeter = isinstance(avatar, Toon.Toon)
        toonbase.localToon.obscureFriendsListButton(1)
        if self.isToon:
            gui = loader.loadModelOnce('phase_3.5/models/gui/avatar_panel_gui')
            self.frame = DirectFrame(image = gui.find('**/avatar_panel'), relief = None, pos = (1.1000000000000001, 100, 0.52500000000000002))
        else:
            gui = loader.loadModelOnce('phase_3.5/models/gui/suit_detail_panel')
            self.frame = DirectFrame(geom = gui.find('**/avatar_panel'), geom_scale = 0.20999999999999999, geom_pos = (0, 0, 0.02), relief = None, pos = (1.1000000000000001, 100, 0.52500000000000002))
        disabledImageColor = Vec4(1, 1, 1, 0.40000000000000002)
        text0Color = Vec4(1, 1, 1, 1)
        text1Color = Vec4(0.5, 1, 0.5, 1)
        text2Color = Vec4(1, 1, 0.5, 1)
        text3Color = Vec4(1, 1, 1, 0.20000000000000001)
        if self.isToon:
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
        else:
            self.head = self.frame.attachNewNode('head')
            for part in avatar.headParts:
                copyPart = part.copyTo(self.head)
                copyPart.setDepthTest(1)
                copyPart.setDepthWrite(1)
            
            p1 = Point3()
            p2 = Point3()
            self.head.calcTightBounds(p1, p2)
            d = p2 - p1
            biggest = max(d[0], d[1], d[2])
            s = 0.29999999999999999 / biggest
            self.head.setPosHprScale(0, 0, 0, 180, 0, 0, s, s, s)
        if self.isToon:
            self.nameLabel = DirectLabel(parent = self.frame, pos = (0.012500000000000001, 0, 0.38500000000000001), relief = None, text = self.avName, text_font = avatar.getFont(), text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0), text_scale = 0.047, text_wordwrap = 7.5, text_shadow = (1, 1, 1, 1))
            self.closeButton = DirectButton(parent = self.frame, image = (gui.find('**/CloseBtn_UP'), gui.find('**/CloseBtn_DN'), gui.find('**/CloseBtn_Rllvr')), relief = None, pos = (0.15764400000000001, 0, -0.37916699999999998), command = self._AvatarPanel__handleClose)
            self.friendButton = DirectButton(parent = self.frame, image = (gui.find('**/Frnds_Btn_UP'), gui.find('**/Frnds_Btn_DN'), gui.find('**/Frnds_Btn_RLVR'), gui.find('**/Frnds_Btn_UP')), image3_color = disabledImageColor, relief = None, text = Localizer.AvatarPanelFriends, text_scale = 0.059999999999999998, pos = (-0.10299999999999999, 0, 0.096000000000000002), text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_pos = (0.059999999999999998, -0.02), text_align = TextNode.ALeft, command = self._AvatarPanel__handleFriend)
            self.whisperButton = DirectButton(parent = self.frame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR'), gui.find('**/ChtBx_ChtBtn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.10299999999999999, 0, -0.090499999999999997), text = Localizer.AvatarPanelWhisper, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = 0.059999999999999998, text_pos = (0.059999999999999998, -0.02), text_align = TextNode.ALeft, command = self._AvatarPanel__handleWhisper)
            self.secretsButton = DirectButton(parent = self.frame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR'), gui.find('**/ChtBx_ChtBtn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.10299999999999999, 0, -0.1875), text = Localizer.AvatarPanelSecrets, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = 0.059999999999999998, text_pos = (0.059999999999999998, -0.02), text_align = TextNode.ALeft, command = self._AvatarPanel__handleSecrets)
            self.goToButton = DirectButton(parent = self.frame, image = (gui.find('**/Go2_Btn_UP'), gui.find('**/Go2_Btn_DN'), gui.find('**/Go2_Btn_RLVR'), gui.find('**/Go2_Btn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.10299999999999999, 0, 0.0029399999999999999), text = Localizer.AvatarPanelGoTo, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = 0.059999999999999998, text_pos = (0.059999999999999998, -0.02), text_align = TextNode.ALeft, command = self._AvatarPanel__handleGoto)
            self.ignoreButton = DirectButton(parent = self.frame, image = (gui.find('**/Ignore_Btn_UP'), gui.find('**/Ignore_Btn_DN'), gui.find('**/Ignore_Btn_RLVR'), gui.find('**/Ignore_Btn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.103697, 0, -0.27487499999999998), text = Localizer.AvatarPanelIgnore, text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = 0.059999999999999998, text_pos = (0.059999999999999998, -0.02), text_align = TextNode.ALeft, command = self._AvatarPanel__handleIgnore)
            self.ignoreButton.hide()
            self.detailButton = DirectButton(parent = self.frame, image = (gui.find('**/ChtBx_BackBtn_UP'), gui.find('**/ChtBx_BackBtn_DN'), gui.find('**/ChtBx_BackBtn_Rllvr')), relief = None, pos = (-0.133773, 0, -0.38713199999999998), command = self._AvatarPanel__handleDetails)
        else:
            self.nameLabel = DirectLabel(parent = self.frame, pos = (0.012500000000000001, 0, 0.35999999999999999), relief = None, text = self.avName, text_font = avatar.getFont(), text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0), text_scale = 0.047, text_wordwrap = 7.5, text_shadow = (1, 1, 1, 1))
            level = avatar.getActualLevel()
            dept = AvatarDNA.getSuitDeptFullname(avatar.dna.name)
            self.levelLabel = DirectLabel(parent = self.frame, pos = (0, 0, -0.10000000000000001), relief = None, text = Localizer.AvatarPanelCogLevel % level, text_font = avatar.getFont(), text_align = TextNode.ACenter, text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0), text_scale = 0.050000000000000003, text_wordwrap = 8.0)
            corpIcon = avatar.corpMedallion.copyTo(hidden)
            corpIcon.iPosHprScale()
            self.corpIcon = DirectLabel(parent = self.frame, geom = corpIcon, geom_scale = 0.13, pos = (0, 0, -0.17499999999999999), relief = None)
            corpIcon.removeNode()
            self.deptLabel = DirectLabel(parent = self.frame, pos = (0, 0, -0.28000000000000003), relief = None, text = dept, text_font = avatar.getFont(), text_align = TextNode.ACenter, text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0), text_scale = 0.050000000000000003, text_wordwrap = 8.0)
            self.closeButton = DirectButton(parent = self.frame, relief = None, pos = (0.0, 0, -0.35999999999999999), text = Localizer.AvatarPanelCogDetailClose, text_font = avatar.getFont(), text0_fg = Vec4(0, 0, 0, 1), text1_fg = Vec4(0.5, 0, 0, 1), text2_fg = Vec4(1, 0, 0, 1), text_pos = (0, 0), text_scale = 0.050000000000000003, command = self._AvatarPanel__handleClose)
        gui.removeNode()
        if wantsLaffMeter:
            self._AvatarPanel__makeLaffMeter(avatar)
            self._AvatarPanel__updateHp(avatar.hp, avatar.maxHp)
            self.healthText.show()
            self.laffMeter.show()
        
        menuX = -0.050000000000000003
        menuScale = 0.064000000000000001
        if self.avDisableName:
            self.accept(self.avDisableName, self._AvatarPanel__handleDisableAvatar)
        
        if self.isToon:
            if self.avGenerateName:
                self.accept(self.avGenerateName, self._AvatarPanel__handleGenerateAvatar)
            
            if self.avHpChangeName:
                self.accept(self.avHpChangeName, self._AvatarPanel__updateHp)
            
        
        self.accept('updateLaffMeter', self._AvatarPanel__updateLaffMeter)
        self.frame.show()
        messenger.send('avPanelDone')

    
    def cleanup(self):
        if AvatarPanel.currentAvatarPanel != self:
            return None
        
        AvatarDetailPanel.unloadAvatarDetail()
        self.frame.destroy()
        del self.frame
        self.head.removeNode()
        del self.head
        if self.isToon:
            self.headModel.stopBlink()
            self.headModel.stopLookAroundNow()
            self.headModel.delete()
            del self.headModel
        
        toonbase.localToon.obscureFriendsListButton(-1)
        self.laffMeter = None
        if self.avDisableName:
            self.ignore(self.avDisableName)
        
        if self.avGenerateName:
            self.ignore(self.avGenerateName)
        
        if self.avHpChangeName:
            self.ignore(self.avHpChangeName)
        
        self.ignore('updateLaffMeter')
        AvatarPanel.currentAvatarPanel = None
        return None

    
    def _AvatarPanel__handleGoto(self):
        toonbase.localToon.chatMgr.noWhisper()
        messenger.send('gotoAvatar', [
            self.avId,
            self.avName,
            self.avDisableName])

    
    def _AvatarPanel__handleWhisper(self):
        toonbase.localToon.chatMgr.whisperTo(self.avName, self.avId)

    
    def _AvatarPanel__handleSecrets(self):
        toonbase.localToon.chatMgr.noWhisper()
        FriendSecret.showFriendSecret()

    
    def _AvatarPanel__handleFriend(self):
        toonbase.localToon.chatMgr.noWhisper()
        messenger.send('friendAvatar', [
            self.avId,
            self.avName,
            self.avDisableName])

    
    def _AvatarPanel__handleIgnore(self):
        print 'Ignore.'

    
    def _AvatarPanel__handleDetails(self):
        toonbase.localToon.chatMgr.noWhisper()
        messenger.send('avatarDetails', [
            self.avId,
            self.avName])

    
    def _AvatarPanel__handleClose(self):
        self.cleanup()
        AvatarPanel.currentAvatarPanel = None
        if self.friendsListShown:
            FriendsListPanel.showFriendsList()
        

    
    def _AvatarPanel__handleDisableAvatar(self):
        if self.isToon:
            if not toonbase.tcr.isFriend(self.avId):
                self.cleanup()
                AvatarPanel.currentAvatarPanel = None
            else:
                self.healthText.hide()
                if self.laffMeter != None:
                    self.laffMeter.stop()
                    self.laffMeter.destroy()
                    self.laffMeter = None
                
        else:
            self.cleanup()
            AvatarPanel.currentAvatarPanel = None

    
    def _AvatarPanel__handleGenerateAvatar(self, avatar):
        self._AvatarPanel__updateLaffMeter(avatar, avatar.hp, avatar.maxHp)

    
    def _AvatarPanel__updateLaffMeter(self, avatar, hp, maxHp):
        if self.laffMeter == None:
            self._AvatarPanel__makeLaffMeter(avatar)
        
        self._AvatarPanel__updateHp(avatar.hp, avatar.maxHp)
        self.laffMeter.show()
        self.healthText.show()

    
    def _AvatarPanel__makeLaffMeter(self, avatar):
        self.laffMeter = LaffMeter.LaffMeter(avatar.style, avatar.hp, avatar.maxHp)
        self.laffMeter.reparentTo(self.frame)
        self.laffMeter.setPos(-0.10000000000000001, 0, 0.20499999999999999)
        self.laffMeter.setScale(0.029999999999999999)

    
    def _AvatarPanel__updateHp(self, hp, maxHp):
        if self.laffMeter != None and hp != None and maxHp != None:
            self.laffMeter.adjustFace(hp, maxHp)
            self.healthText['text'] = '%d / %d' % (hp, maxHp)
        


