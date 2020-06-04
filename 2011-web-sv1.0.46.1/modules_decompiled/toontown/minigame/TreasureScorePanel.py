# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\TreasureScorePanel.py
from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from toontown.toon import LaffMeter
from toontown.toonbase import TTLocalizer

class TreasureScorePanel(DirectFrame):
    __module__ = __name__

    def __init__(self):
        DirectFrame.__init__(self, relief=None, image_color=GlobalDialogColor, image_scale=(0.24,
                                                                                            1.0,
                                                                                            0.24), image_pos=(0.0,
                                                                                                              0.1,
                                                                                                              0.0))
        self.score = 0
        self.scoreText = DirectLabel(self, relief=None, text=str(self.score), text_scale=0.08, pos=(0.0, 0.0, -0.09))
        self.nameText = DirectLabel(self, relief=None, text=TTLocalizer.DivingGameTreasuresRetrieved, text_scale=0.05, text_pos=(0.0,
                                                                                                                                 0.06), text_wordwrap=7.5, text_shadow=(1,
                                                                                                                                                                        1,
                                                                                                                                                                        1,
                                                                                                                                                                        1))
        self.show()
        return

    def cleanup(self):
        del self.scoreText
        del self.nameText
        self.destroy()

    def incrScore(self):
        self.score += 1
        self.scoreText['text'] = str(self.score)

    def makeTransparent(self, alpha):
        self.setTransparency(1)
        self.setColorScale(1, 1, 1, alpha)