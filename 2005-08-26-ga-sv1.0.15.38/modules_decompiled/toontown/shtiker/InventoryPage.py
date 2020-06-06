# File: I (Python 2.2)

import ShtikerPage
from toontown.toonbase import ToontownBattleGlobals
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class InventoryPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.currentTrackInfo = None
        self.onscreen = 0

    
    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent = self, relief = None, text = TTLocalizer.InventoryPageTitle, text_scale = 0.12, textMayChange = 1, pos = (0, 0, 0.62))
        self.gagFrame = DirectFrame(parent = self, relief = None, pos = (0.10000000000000001, 0, -0.46999999999999997), scale = (0.34999999999999998, 0.34999999999999998, 0.34999999999999998), geom = getDefaultDialogGeom(), geom_color = ToontownGlobals.GlobalDialogColor)
        self.trackInfo = DirectFrame(parent = self, relief = None, pos = (-0.40000000000000002, 0, -0.46999999999999997), scale = (0.34999999999999998, 0.34999999999999998, 0.34999999999999998), geom = getDefaultDialogGeom(), geom_scale = (1.3999999999999999, 1, 1), geom_color = ToontownGlobals.GlobalDialogColor, text = '', text_wordwrap = 11, text_align = TextNode.ALeft, text_scale = 0.12, text_pos = (-0.65000000000000002, 0.29999999999999999), text_fg = (0.050000000000000003, 0.14000000000000001, 0.40000000000000002, 1))
        self.trackProgress = DirectWaitBar(parent = self.trackInfo, pos = (0, 0, -0.20000000000000001), relief = SUNKEN, frameSize = (-0.59999999999999998, 0.59999999999999998, -0.10000000000000001, 0.10000000000000001), borderWidth = (0.025000000000000001, 0.025000000000000001), scale = 1.1000000000000001, frameColor = (0.40000000000000002, 0.59999999999999998, 0.40000000000000002, 1), barColor = (0.90000000000000002, 1, 0.69999999999999996, 1), text = '0/0', text_scale = 0.14999999999999999, text_fg = (0.050000000000000003, 0.14000000000000001, 0.40000000000000002, 1), text_align = TextNode.ACenter, text_pos = (0, -0.22))
        self.trackProgress.hide()
        jarGui = loader.loadModel('phase_3.5/models/gui/jar_gui')
        self.moneyDisplay = DirectLabel(parent = self, relief = None, pos = (0.55000000000000004, 0, -0.5), scale = 0.80000000000000004, text = str(base.localAvatar.getMoney()), text_scale = 0.17999999999999999, text_fg = (0.94999999999999996, 0.94999999999999996, 0, 1), text_shadow = (0, 0, 0, 1), text_pos = (0, -0.10000000000000001, 0), image = jarGui.find('**/Jar'), text_font = ToontownGlobals.getSignFont())
        jarGui.removeNode()

    
    def unload(self):
        del self.title
        ShtikerPage.ShtikerPage.unload(self)

    
    def _InventoryPage__moneyChange(self, money):
        self.moneyDisplay['text'] = str(money)

    
    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        base.localAvatar.inventory.setActivateMode('book')
        base.localAvatar.inventory.show()
        base.localAvatar.inventory.reparentTo(self)
        self.moneyDisplay['text'] = str(base.localAvatar.getMoney())
        self.accept('enterBookDelete', self.enterDeleteMode)
        self.accept('exitBookDelete', self.exitDeleteMode)
        self.accept('enterTrackFrame', self.updateTrackInfo)
        self.accept('exitTrackFrame', self.clearTrackInfo)
        self.accept(localAvatar.uniqueName('moneyChange'), self._InventoryPage__moneyChange)

    
    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        self.clearTrackInfo(self.currentTrackInfo)
        self.ignore('enterBookDelete')
        self.ignore('exitBookDelete')
        self.ignore('enterTrackFrame')
        self.ignore('exitTrackFrame')
        self.ignore(localAvatar.uniqueName('moneyChange'))
        self.makePageWhite(None)
        base.localAvatar.inventory.hide()
        base.localAvatar.inventory.reparentTo(hidden)
        self.exitDeleteMode()

    
    def enterDeleteMode(self):
        self.title['text'] = TTLocalizer.InventoryPageDeleteTitle
        self.title['text_fg'] = (0, 0, 0, 1)
        self.book['image_color'] = Vec4(1, 1, 0, 1)

    
    def exitDeleteMode(self):
        self.title['text'] = TTLocalizer.InventoryPageTitle
        self.title['text_fg'] = (0, 0, 0, 1)
        self.book['image_color'] = Vec4(1, 1, 1, 1)

    
    def updateTrackInfo(self, trackIndex):
        self.currentTrackInfo = trackIndex
        trackName = TextEncoder.upper(ToontownBattleGlobals.Tracks[trackIndex])
        if base.localAvatar.hasTrackAccess(trackIndex):
            (curExp, nextExp) = base.localAvatar.inventory.getCurAndNextExpValues(trackIndex)
            if nextExp == ToontownBattleGlobals.MaxSkill:
                str = TTLocalizer.InventoryPageTrackFull % trackName
            else:
                morePoints = nextExp - curExp
                if morePoints == 1:
                    str = TTLocalizer.InventoryPageSinglePoint % {
                        'trackName': trackName,
                        'numPoints': morePoints }
                else:
                    str = TTLocalizer.InventoryPagePluralPoints % {
                        'trackName': trackName,
                        'numPoints': morePoints }
            self.trackInfo['text'] = str
            self.trackProgress['range'] = nextExp
            self.trackProgress['value'] = curExp
            self.trackProgress['text'] = '%s / %s' % (curExp, nextExp)
            self.trackProgress['frameColor'] = (ToontownBattleGlobals.TrackColors[trackIndex][0] * 0.59999999999999998, ToontownBattleGlobals.TrackColors[trackIndex][1] * 0.59999999999999998, ToontownBattleGlobals.TrackColors[trackIndex][2] * 0.59999999999999998, 1)
            self.trackProgress['barColor'] = (ToontownBattleGlobals.TrackColors[trackIndex][0], ToontownBattleGlobals.TrackColors[trackIndex][1], ToontownBattleGlobals.TrackColors[trackIndex][2], 1)
            self.trackProgress.show()
        else:
            str = TTLocalizer.InventoryPageNoAccess % trackName
            self.trackInfo['text'] = str
            self.trackProgress.hide()

    
    def clearTrackInfo(self, trackIndex):
        if self.currentTrackInfo == trackIndex:
            self.trackInfo['text'] = ''
            self.trackProgress.hide()
            self.currentTrackInfo = None
        
        return None

    
    def acceptOnscreenHooks(self):
        self.accept(ToontownGlobals.InventoryHotkeyOn, self.showInventoryOnscreen)
        self.accept(ToontownGlobals.InventoryHotkeyOff, self.hideInventoryOnscreen)

    
    def ignoreOnscreenHooks(self):
        self.ignore(ToontownGlobals.InventoryHotkeyOn)
        self.ignore(ToontownGlobals.InventoryHotkeyOff)

    
    def showInventoryOnscreen(self):
        if self.onscreen or base.localAvatar.questPage.onscreen:
            return None
        
        self.onscreen = 1
        base.localAvatar.inventory.setActivateMode('book')
        base.localAvatar.inventory.show()
        base.localAvatar.inventory.reparentTo(self)
        self.moneyDisplay['text'] = str(base.localAvatar.getMoney())
        self.accept('enterTrackFrame', self.updateTrackInfo)
        self.accept('exitTrackFrame', self.clearTrackInfo)
        self.accept(localAvatar.uniqueName('moneyChange'), self._InventoryPage__moneyChange)
        self.reparentTo(aspect2d)
        self.title.hide()
        self.show()

    
    def hideInventoryOnscreen(self):
        if not (self.onscreen):
            return None
        
        self.onscreen = 0
        self.ignore('enterTrackFrame')
        self.ignore('exitTrackFrame')
        self.ignore(localAvatar.uniqueName('moneyChange'))
        base.localAvatar.inventory.hide()
        base.localAvatar.inventory.reparentTo(hidden)
        self.reparentTo(self.book)
        self.title.show()
        self.hide()


