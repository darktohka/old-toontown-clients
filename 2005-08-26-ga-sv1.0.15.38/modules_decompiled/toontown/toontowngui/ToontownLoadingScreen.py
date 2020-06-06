# File: T (Python 2.2)

from pandac.PandaModules import *
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import random

class ToontownLoadingScreen:
    
    def __init__(self):
        self._ToontownLoadingScreen__expectedCount = 0
        self._ToontownLoadingScreen__count = 0
        self.gui = loader.loadModel('phase_3/models/gui/progress-background')
        self.banner = loader.loadModel('phase_3/models/gui/toon_council').find('**/scroll')
        self.banner.reparentTo(self.gui)
        self.banner.setScale(0.40000000000000002, 0.40000000000000002, 0.40000000000000002)
        self.tip = DirectLabel(guiId = 'ToontownLoadingScreenTip', parent = self.banner, relief = None, text = '', text_scale = 0.17999999999999999, textMayChange = 1, pos = (-1.2, 0.0, 0.10000000000000001), text_fg = (0.40000000000000002, 0.29999999999999999, 0.20000000000000001, 1), text_wordwrap = 13, text_align = TextNode.ALeft)
        self.title = DirectLabel(guiId = 'ToontownLoadingScreenTitle', parent = self.gui, relief = None, pos = (-1.0600000000000001, 0, -0.77000000000000002), text = '', textMayChange = 1, text_scale = 0.080000000000000002, text_fg = (0, 0, 0.5, 1), text_align = TextNode.ALeft)
        self.waitBar = DirectWaitBar(guiId = 'ToontownLoadingScreenWaitBar', parent = self.gui, frameSize = (-1.0600000000000001, 1.0600000000000001, -0.029999999999999999, 0.029999999999999999), pos = (0, 0, -0.84999999999999998), text = '')

    
    def destroy(self):
        self.tip.destroy()
        self.title.destroy()
        self.waitBar.destroy()
        self.banner.removeNode()
        self.gui.removeNode()

    
    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + '\n' + random.choice(TTLocalizer.TipDict.get(tipCategory))

    
    def begin(self, range, label, gui, tipCategory):
        self.waitBar['range'] = range
        self.title['text'] = label
        self.tip['text'] = self.getTip(tipCategory)
        self._ToontownLoadingScreen__count = 0
        self._ToontownLoadingScreen__expectedCount = range
        if gui:
            self.waitBar.reparentTo(self.gui)
            self.title.reparentTo(self.gui)
            self.gui.reparentTo(aspect2dp, NO_FADE_SORT_INDEX)
        else:
            self.waitBar.reparentTo(aspect2dp, NO_FADE_SORT_INDEX)
            self.title.reparentTo(aspect2dp, NO_FADE_SORT_INDEX)
            self.gui.reparentTo(hidden)
        self.waitBar.update(self._ToontownLoadingScreen__count)

    
    def end(self):
        self.waitBar.finish()
        self.waitBar.reparentTo(self.gui)
        self.title.reparentTo(self.gui)
        self.gui.reparentTo(hidden)
        return (self._ToontownLoadingScreen__expectedCount, self._ToontownLoadingScreen__count)

    
    def abort(self):
        self.gui.reparentTo(hidden)

    
    def tick(self):
        self._ToontownLoadingScreen__count = self._ToontownLoadingScreen__count + 1
        self.waitBar.update(self._ToontownLoadingScreen__count)


