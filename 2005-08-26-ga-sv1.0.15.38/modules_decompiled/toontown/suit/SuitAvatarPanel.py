# File: S (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.gui.DirectGui import *
from direct.showbase import PandaObject
from otp.avatar import Avatar
from direct.distributed import DistributedObject
import SuitDNA
from toontown.toonbase import TTLocalizer
from otp.avatar import AvatarPanel
from toontown.friends import FriendsListPanel

class SuitAvatarPanel(AvatarPanel.AvatarPanel):
    currentAvatarPanel = None
    
    def __init__(self, avatar):
        AvatarPanel.AvatarPanel.__init__(self, avatar, FriendsListPanel = FriendsListPanel)
        self.avName = avatar.getName()
        gui = loader.loadModelOnce('phase_3.5/models/gui/suit_detail_panel')
        self.frame = DirectFrame(geom = gui.find('**/avatar_panel'), geom_scale = 0.20999999999999999, geom_pos = (0, 0, 0.02), relief = None, pos = (1.1000000000000001, 100, 0.52500000000000002))
        disabledImageColor = Vec4(1, 1, 1, 0.40000000000000002)
        text0Color = Vec4(1, 1, 1, 1)
        text1Color = Vec4(0.5, 1, 0.5, 1)
        text2Color = Vec4(1, 1, 0.5, 1)
        text3Color = Vec4(1, 1, 1, 0.20000000000000001)
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
        self.nameLabel = DirectLabel(parent = self.frame, pos = (0.012500000000000001, 0, 0.35999999999999999), relief = None, text = self.avName, text_font = avatar.getFont(), text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0), text_scale = 0.047, text_wordwrap = 7.5, text_shadow = (1, 1, 1, 1))
        level = avatar.getActualLevel()
        dept = SuitDNA.getSuitDeptFullname(avatar.dna.name)
        self.levelLabel = DirectLabel(parent = self.frame, pos = (0, 0, -0.10000000000000001), relief = None, text = TTLocalizer.AvatarPanelCogLevel % level, text_font = avatar.getFont(), text_align = TextNode.ACenter, text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0), text_scale = 0.050000000000000003, text_wordwrap = 8.0)
        corpIcon = avatar.corpMedallion.copyTo(hidden)
        corpIcon.iPosHprScale()
        self.corpIcon = DirectLabel(parent = self.frame, geom = corpIcon, geom_scale = 0.13, pos = (0, 0, -0.17499999999999999), relief = None)
        corpIcon.removeNode()
        self.deptLabel = DirectLabel(parent = self.frame, pos = (0, 0, -0.28000000000000003), relief = None, text = dept, text_font = avatar.getFont(), text_align = TextNode.ACenter, text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0), text_scale = 0.050000000000000003, text_wordwrap = 8.0)
        self.closeButton = DirectButton(parent = self.frame, relief = None, pos = (0.0, 0, -0.35999999999999999), text = TTLocalizer.AvatarPanelCogDetailClose, text_font = avatar.getFont(), text0_fg = Vec4(0, 0, 0, 1), text1_fg = Vec4(0.5, 0, 0, 1), text2_fg = Vec4(1, 0, 0, 1), text_pos = (0, 0), text_scale = 0.050000000000000003, command = self._SuitAvatarPanel__handleClose)
        gui.removeNode()
        menuX = -0.050000000000000003
        menuScale = 0.064000000000000001
        self.frame.show()
        messenger.send('avPanelDone')

    
    def cleanup(self):
        if self.frame == None:
            return None
        
        self.frame.destroy()
        del self.frame
        self.frame = None
        self.head.removeNode()
        del self.head
        AvatarPanel.AvatarPanel.cleanup(self)

    
    def _SuitAvatarPanel__handleClose(self):
        self.cleanup()
        AvatarPanel.currentAvatarPanel = None
        if self.friendsListShown:
            FriendsListPanel.showFriendsList()
        


