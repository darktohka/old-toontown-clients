# File: N (Python 2.2)

import ShtikerPage
from DirectGui import *
import NPCFriendPanel
import Localizer

class NPCFriendPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    
    def load(self):
        self.title = DirectLabel(parent = self, relief = None, text = Localizer.NPCFriendPageTitle, text_scale = 0.12, textMayChange = 0, pos = (0, 0, 0.59999999999999998))
        self.friendPanel = NPCFriendPanel.NPCFriendPanel(parent = self)
        self.friendPanel.setScale(0.1225)
        self.friendPanel.setZ(-0.029999999999999999)

    
    def unload(self):
        ShtikerPage.ShtikerPage.unload(self)
        del self.title
        del self.friendPanel

    
    def updatePage(self):
        self.friendPanel.update(toonbase.localToon.NPCFriendsDict, fCallable = 0)

    
    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)

    
    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)


