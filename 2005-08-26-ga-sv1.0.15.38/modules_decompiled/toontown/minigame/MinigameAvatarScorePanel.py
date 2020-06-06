# File: M (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from toontown.toon import LaffMeter

class MinigameAvatarScorePanel(DirectFrame):
    
    def __init__(self, avId, avName):
        self.avId = avId
        if base.cr.doId2do.has_key(self.avId):
            self.avatar = base.cr.doId2do[self.avId]
        else:
            self.avatar = None
        DirectFrame.__init__(self, relief = None, image_color = GlobalDialogColor, image_scale = (0.40000000000000002, 1.0, 0.23999999999999999), image_pos = (0.0, 0.10000000000000001, 0.0))
        self['image'] = getDefaultDialogGeom()
        self.scoreText = DirectLabel(self, relief = None, text = '0', text_scale = 0.10000000000000001, pos = (0.10000000000000001, 0.0, -0.089999999999999997))
        if self.avatar:
            self.laffMeter = LaffMeter.LaffMeter(self.avatar.style, self.avatar.hp, self.avatar.maxHp)
            self.laffMeter.reparentTo(self)
            self.laffMeter.setPos(-0.085000000000000006, 0, -0.035000000000000003)
            self.laffMeter.setScale(0.050000000000000003)
            self.laffMeter.start()
        else:
            self.laffMeter = None
        self.nameText = DirectLabel(self, relief = None, text = avName, text_scale = 0.055, text_pos = (0.0, 0.059999999999999998), text_wordwrap = 7.5, text_shadow = (1, 1, 1, 1))
        self.show()

    
    def cleanup(self):
        if self.laffMeter:
            self.laffMeter.destroy()
            del self.laffMeter
        
        del self.scoreText
        del self.nameText
        self.destroy()

    
    def setScore(self, score):
        self.scoreText['text'] = str(score)

    
    def makeTransparent(self, alpha):
        self.setTransparency(1)
        self.setColorScale(1, 1, 1, alpha)


