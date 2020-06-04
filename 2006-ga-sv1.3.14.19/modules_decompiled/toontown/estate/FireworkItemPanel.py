# File: F (Python 2.2)

from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.effects import FireworkGlobals
from toontown.effects import Fireworks
import FireworksGui

class FireworkItemPanel(DirectFrame):
    
    def __init__(self, itemName, itemNum, *extraArgs):
        self.gui = extraArgs[0][0]
        self.type = extraArgs[0][1][itemNum]
        self.shootEvent = extraArgs[0][2]
        self.name = FireworkGlobals.Names[self.type]
        DirectFrame.__init__(self, image = getDefaultDialogGeom(), image_color = (0.75, 0.75, 0.75, 1), image_scale = (0.25, 0, 0.25), relief = None)
        self.initialiseoptions(FireworkItemPanel)
        self.load()

    
    def load(self):
        self.picture = DirectButton(parent = self, image = (getDefaultDialogGeom(), getDefaultDialogGeom(), getDefaultDialogGeom()), relief = None, command = self._FireworkItemPanel__launchFirework, extraArgs = [
            self.type], image_color = (0.80000000000000004, 0.90000000000000002, 1, 1))
        self.picture.setScale(0.20000000000000001)
        self.picture.setPos(0, 0, 0)
        self.picture.initialiseoptions(self.picture)
        panelWidth = 7
        nameFont = ToontownGlobals.getInterfaceFont()
        self.quantityLabel = DirectLabel(parent = self.picture, relief = None, pos = (0, 0, 0.0), scale = 0.45000000000000001, text = self.name, text_scale = 0.59999999999999998, text_fg = (0, 0, 0, 1), text_pos = (0, -0.14000000000000001, 0), text_font = nameFont, text_wordwrap = panelWidth)

    
    def unload(self):
        del self.picture
        self.quantityLabel.destroy()
        del self.quantityLabel
        DirectFrame.destroy(self)

    
    def destroy(self):
        self.unload()

    
    def _FireworkItemPanel__launchFirework(self, index):
        messenger.send(self.shootEvent, [
            index])

    
    def _FireworkItemPanel__dimSky(self):
        self.oldSkyScale = base.cr.playGame.hood.loader.sky.getColorScale()
        base.cr.playGame.hood.loader.sky.setColorScale(0.29999999999999999, 0.29999999999999999, 0.29999999999999999, 1)

    
    def _FireworkItemPanel__resetSky(self):
        base.cr.playGame.hood.loader.sky.setColorScale(self.oldSkyScale)


