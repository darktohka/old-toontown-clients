# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\MinigameAvatarScorePanel.py
from pandac.PandaModules import *
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toon import LaffMeter

class MinigameAvatarScorePanel(DirectFrame):
    __module__ = __name__

    def __init__(self, avId, avName):
        self.avId = avId
        if base.cr.doId2do.has_key(self.avId):
            self.avatar = base.cr.doId2do[self.avId]
        else:
            self.avatar = None
        DirectFrame.__init__(self, relief=None, image_color=GlobalDialogColor, image_scale=(0.4,
                                                                                            1.0,
                                                                                            0.24), image_pos=(0.0,
                                                                                                              0.1,
                                                                                                              0.0))
        self['image'] = DGG.getDefaultDialogGeom()
        self.scoreText = DirectLabel(self, relief=None, text='0', text_scale=TTLocalizer.MASPscoreText, pos=(0.1, 0.0, -0.09))
        if self.avatar:
            self.laffMeter = LaffMeter.LaffMeter(self.avatar.style, self.avatar.hp, self.avatar.maxHp)
            self.laffMeter.reparentTo(self)
            self.laffMeter.setPos(-0.085, 0, -0.035)
            self.laffMeter.setScale(0.05)
            self.laffMeter.start()
        else:
            self.laffMeter = None
        self.nameText = DirectLabel(self, relief=None, text=avName, text_scale=TTLocalizer.MASPnameText, text_pos=(0.0,
                                                                                                                   0.06), text_wordwrap=7.5, text_shadow=(1,
                                                                                                                                                          1,
                                                                                                                                                          1,
                                                                                                                                                          1))
        self.show()
        return

    def cleanup(self):
        if self.laffMeter:
            self.laffMeter.destroy()
            del self.laffMeter
        del self.scoreText
        del self.nameText
        self.destroy()

    def setScore(self, score):
        self.scoreText['text'] = str(score)

    def getScore(self):
        return int(self.scoreText['text'])

    def makeTransparent(self, alpha):
        self.setTransparency(1)
        self.setColorScale(1, 1, 1, alpha)