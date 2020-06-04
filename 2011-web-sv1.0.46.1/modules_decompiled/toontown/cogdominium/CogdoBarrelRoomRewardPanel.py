# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\CogdoBarrelRoomRewardPanel.py
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.cogdominium import CogdoBarrelRoomConsts

class CogdoBarrelRoomRewardPanel(DirectFrame):
    __module__ = __name__

    def __init__(self):
        DirectFrame.__init__(self, relief=None, geom=DGG.getDefaultDialogGeom(), geom_color=ToontownGlobals.GlobalDialogColor, geom_scale=TTLocalizer.RPdirectFrame, pos=(0,
                                                                                                                                                                          0,
                                                                                                                                                                          0.587))
        self.initialiseoptions(CogdoBarrelRoomRewardPanel)
        self.avNameLabel = DirectLabel(parent=self, relief=None, pos=(0, 0, 0.3), text='Toon Ups', text_scale=0.08)
        self.rewardLines = []
        for i in range(CogdoBarrelRoomConsts.MaxToons):
            rewardLine = {}
            rewardLine['frame'] = DirectFrame(parent=self, relief=None, frameSize=(-0.5, 0.5, -0.045, 0.042), pos=(0, 0, 0.1 + -0.09 * i))
            rewardLine['name'] = DirectLabel(parent=rewardLine['frame'], relief=None, text='', text_scale=TTLocalizer.RPtrackLabels, text_align=TextNode.ALeft, pos=(-0.4, 0, 0), text_pos=(0, -0.02))
            rewardLine['laff'] = DirectLabel(parent=rewardLine['frame'], relief=None, text='', text_scale=0.05, text_align=TextNode.ARight, pos=(0.4,
                                                                                                                                                 0,
                                                                                                                                                 0), text_pos=(0, -0.02))
            self.rewardLines.append(rewardLine)

        return

    def setRewards(self, results):
        for p in range(len(results[0])):
            doId = results[0][p]
            laff = results[1][p]
            if doId > 0 and base.cr.doId2do.has_key(doId):
                toon = base.cr.doId2do[doId]
                self.rewardLines[p]['name'].setProp('text', toon.getName())
                self.rewardLines[p]['laff'].setProp('text', str(laff))
                if doId == base.localAvatar.getDoId():
                    self.rewardLines[p]['frame'].setProp('relief', DGG.RIDGE)
                    self.rewardLines[p]['frame'].setProp('borderWidth', (0.01, 0.01))
                    self.rewardLines[p]['frame'].setProp('frameColor', (1, 1, 1, 0.5))