# File: S (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase import ToontownGlobals
from direct.showbase import PandaObject
from direct.fsm import StateData
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer

class ShtikerBook(DirectFrame, StateData.StateData):
    
    def __init__(self, doneEvent):
        DirectFrame.__init__(self, relief = None, sortOrder = BACKGROUND_SORT_INDEX)
        self.initialiseoptions(ShtikerBook)
        StateData.StateData.__init__(self, doneEvent)
        self.pages = []
        self.pageTabs = []
        self.currPageTabIndex = None
        self.pageTabFrame = DirectFrame(parent = self, relief = None, pos = (0.93000000000000005, 1, 0.57499999999999996), scale = 1.25)
        self.pageTabFrame.hide()
        self.currPageIndex = None
        self.entered = 0
        self.safeMode = 0
        self._ShtikerBook__obscured = 0
        self._ShtikerBook__shown = 0
        self._ShtikerBook__isOpen = 0
        self.hide()
        self.setPos(0, 0, 0.10000000000000001)

    
    def setSafeMode(self, setting):
        self.safeMode = setting

    
    def enter(self):
        if self.entered:
            return None
        
        self.entered = 1
        messenger.send('releaseDirector')
        base.playSfx(self.openSound)
        base.disableMouse()
        base.render.hide()
        base.setBackgroundColor(0.050000000000000003, 0.14999999999999999, 0.40000000000000002)
        base.setCellsAvailable([
            base.rightCells[0]], 0)
        self.oldMin2dAlpha = NametagGlobals.getMin2dAlpha()
        self.oldMax2dAlpha = NametagGlobals.getMax2dAlpha()
        NametagGlobals.setMin2dAlpha(0.80000000000000004)
        NametagGlobals.setMax2dAlpha(1.0)
        self._ShtikerBook__isOpen = 1
        self._ShtikerBook__setButtonVisibility()
        self.show()
        self.showPageArrows()
        if not (self.safeMode):
            self.accept('shtiker-page-done', self._ShtikerBook__pageDone)
            self.accept(ToontownGlobals.StickerBookHotkey, self._ShtikerBook__close)
            self.accept('arrow_right', self._ShtikerBook__pageChange, [
                1])
            self.accept('arrow_left', self._ShtikerBook__pageChange, [
                -1])
            self.pageTabFrame.show()
        
        self.pages[self.currPageIndex].enter()

    
    def exit(self):
        if not (self.entered):
            return None
        
        self.entered = 0
        base.playSfx(self.closeSound)
        self.pages[self.currPageIndex].exit()
        base.render.show()
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
        gsg = base.win.getGsg()
        if gsg:
            base.render.prepareScene(gsg)
        
        NametagGlobals.setMin2dAlpha(self.oldMin2dAlpha)
        NametagGlobals.setMax2dAlpha(self.oldMax2dAlpha)
        base.setCellsAvailable([
            base.rightCells[0]], 1)
        self._ShtikerBook__isOpen = 0
        self.hide()
        self.hideButton()
        cleanupDialog('globalDialog')
        self.pageTabFrame.hide()
        self.ignore('shtiker-page-done')
        self.ignore(ToontownGlobals.StickerBookHotkey)
        self.ignore('arrow_right')
        self.ignore('arrow_left')

    
    def load(self):
        bookModel = loader.loadModelOnce('phase_3.5/models/gui/stickerbook_gui')
        self['image'] = bookModel.find('**/big_book')
        self['image_scale'] = (2, 1, 1.5)
        self.resetFrameSize()
        self.bookOpenButton = DirectButton(image = (bookModel.find('**/BookIcon_CLSD'), bookModel.find('**/BookIcon_OPEN'), bookModel.find('**/BookIcon_RLVR')), relief = None, pos = (1.175, 0, -0.82999999999999996), scale = 0.30499999999999999, command = self._ShtikerBook__open)
        self.bookCloseButton = DirectButton(image = (bookModel.find('**/BookIcon_OPEN'), bookModel.find('**/BookIcon_CLSD'), bookModel.find('**/BookIcon_RLVR2')), relief = None, pos = (1.175, 0, -0.82999999999999996), scale = 0.30499999999999999, command = self._ShtikerBook__close)
        self.bookOpenButton.hide()
        self.bookCloseButton.hide()
        self.nextArrow = DirectButton(parent = self, relief = None, image = (bookModel.find('**/arrow_button'), bookModel.find('**/arrow_down'), bookModel.find('**/arrow_rollover')), scale = (0.10000000000000001, 0.10000000000000001, 0.10000000000000001), pos = (0.83799999999999997, 0, -0.66100000000000003), command = self._ShtikerBook__pageChange, extraArgs = [
            1])
        self.prevArrow = DirectButton(parent = self, relief = None, image = (bookModel.find('**/arrow_button'), bookModel.find('**/arrow_down'), bookModel.find('**/arrow_rollover')), scale = (-0.10000000000000001, 0.10000000000000001, 0.10000000000000001), pos = (-0.83799999999999997, 0, -0.66100000000000003), command = self._ShtikerBook__pageChange, extraArgs = [
            -1])
        bookModel.removeNode()
        self.openSound = base.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_open.mp3')
        self.closeSound = base.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_delete.mp3')
        self.pageSound = base.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_turn.mp3')

    
    def unload(self):
        loader.unloadModel('phase_3.5/models/gui/stickerbook_gui')
        self.destroy()
        self.bookOpenButton.destroy()
        del self.bookOpenButton
        self.bookCloseButton.destroy()
        del self.bookCloseButton
        del self.nextArrow
        del self.prevArrow
        for page in self.pages:
            page.unload()
        
        del self.pages
        del self.pageTabs
        del self.currPageTabIndex
        del self.openSound
        del self.closeSound
        del self.pageSound

    
    def addPage(self, page, pageName = 'Page'):
        self.pages.append(page)
        page.setBook(self)
        page.reparentTo(self)
        self.addPageTab(page, pageName)

    
    def addPageTab(self, page, pageName = 'Page'):
        tabIndex = len(self.pageTabs)
        
        def goToPage():
            messenger.send('wakeup')
            base.playSfx(self.pageSound)
            self.setPage(page)

        yOffset = 0.070000000000000007 * (len(self.pages) - 1)
        iconGeom = None
        iconImage = None
        iconScale = 1
        iconColor = Vec4(1)
        if pageName == TTLocalizer.OptionsPageTitle:
            iconModels = loader.loadModelOnce('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/switch')
            iconModels.detachNode()
        elif pageName == TTLocalizer.ShardPageTitle:
            iconModels = loader.loadModelOnce('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/district')
            iconModels.detachNode()
        elif pageName == TTLocalizer.MapPageTitle:
            iconModels = loader.loadModelOnce('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/teleportIcon')
            iconModels.detachNode()
        elif pageName == TTLocalizer.InventoryPageTitle:
            iconModels = loader.loadModelOnce('phase_3.5/models/gui/inventory_icons')
            iconGeom = iconModels.find('**/inventory_tart')
            iconScale = 7
            iconModels.detachNode()
        elif pageName == TTLocalizer.QuestPageToonTasks:
            iconModels = loader.loadModelOnce('phase_3.5/models/gui/stickerbook_gui')
            iconGeom = iconModels.find('**/questCard')
            iconScale = 0.90000000000000002
            iconModels.detachNode()
        elif pageName == TTLocalizer.TrackPageShortTitle:
            iconGeom = loader.loadModelOnce('phase_3.5/models/gui/filmstrip')
            iconModels = loader.loadModelOnce('phase_3.5/models/gui/filmstrip')
            iconScale = 1.1000000000000001
            iconColor = Vec4(0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 1)
            iconModels.detachNode()
        elif pageName == TTLocalizer.SuitPageTitle:
            iconModels = loader.loadModelOnce('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/gui_gear')
            iconModels.detachNode()
        elif pageName == TTLocalizer.FishPageTitle:
            iconModels = loader.loadModelOnce('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/fish')
            iconModels.detachNode()
        elif pageName == TTLocalizer.DisguisePageTitle:
            iconModels = loader.loadModelOnce('phase_3.5/models/gui/sos_textures')
            iconGeom = iconModels.find('**/disguise2')
            iconColor = Vec4(0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 1)
            iconModels.detachNode()
        elif pageName == TTLocalizer.NPCFriendPageTitle:
            iconModels = loader.loadModelOnce('phase_3.5/models/gui/playingCard')
            iconImage = iconModels.find('**/card_back')
            iconGeom = iconModels.find('**/logo')
            iconScale = 0.22
            iconModels.detachNode()
        
        pageTab = DirectButton(parent = self.pageTabFrame, relief = RAISED, frameSize = (-0.57499999999999996, 0.57499999999999996, -0.57499999999999996, 0.57499999999999996), borderWidth = (0.050000000000000003, 0.050000000000000003), text = ('', '', pageName, ''), text_align = TextNode.ALeft, text_pos = (1, -0.20000000000000001), text_scale = 0.75, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), image = iconImage, image_scale = iconScale, geom = iconGeom, geom_scale = iconScale, geom_color = iconColor, pos = (0, 0, -yOffset), scale = 0.059999999999999998, command = goToPage)
        self.pageTabs.append(pageTab)

    
    def setPage(self, page):
        if self.currPageIndex is not None:
            self.pages[self.currPageIndex].exit()
        
        self.currPageIndex = self.pages.index(page)
        self.setPageTabIndex(self.currPageIndex)
        self.showPageArrows()
        page.enter()

    
    def setPageTabIndex(self, pageTabIndex):
        if self.currPageTabIndex is not None and pageTabIndex != self.currPageTabIndex:
            self.pageTabs[self.currPageTabIndex]['relief'] = RAISED
        
        self.currPageTabIndex = pageTabIndex
        self.pageTabs[self.currPageTabIndex]['relief'] = SUNKEN

    
    def obscureButton(self, obscured):
        self._ShtikerBook__obscured = obscured
        self._ShtikerBook__setButtonVisibility()

    
    def isObscured(self):
        return self._ShtikerBook__obscured

    
    def showButton(self):
        self._ShtikerBook__shown = 1
        self._ShtikerBook__setButtonVisibility()

    
    def hideButton(self):
        self._ShtikerBook__shown = 0
        self._ShtikerBook__setButtonVisibility()

    
    def _ShtikerBook__setButtonVisibility(self):
        if self._ShtikerBook__isOpen:
            self.bookOpenButton.hide()
            self.bookCloseButton.show()
        elif self._ShtikerBook__shown and not (self._ShtikerBook__obscured):
            self.bookOpenButton.show()
            self.bookCloseButton.hide()
        else:
            self.bookOpenButton.hide()
            self.bookCloseButton.hide()

    
    def _ShtikerBook__open(self):
        messenger.send('enterStickerBook')

    
    def _ShtikerBook__close(self):
        base.playSfx(self.closeSound)
        self.pages[self.currPageIndex].exit()
        self.doneStatus = {
            'mode': 'close' }
        messenger.send('exitStickerBook')
        messenger.send(self.doneEvent)

    
    def _ShtikerBook__pageDone(self):
        page = self.pages[self.currPageIndex]
        pageDoneStatus = page.getDoneStatus()
        if pageDoneStatus:
            if pageDoneStatus['mode'] == 'close':
                self._ShtikerBook__close()
            else:
                self.doneStatus = pageDoneStatus
                messenger.send(self.doneEvent)
        

    
    def _ShtikerBook__pageChange(self, offset):
        messenger.send('wakeup')
        base.playSfx(self.pageSound)
        self.pages[self.currPageIndex].exit()
        self.currPageIndex = self.currPageIndex + offset
        messenger.send('stickerBookPageChange-' + str(self.currPageIndex))
        self.currPageIndex = max(self.currPageIndex, 0)
        self.currPageIndex = min(self.currPageIndex, len(self.pages) - 1)
        self.setPageTabIndex(self.currPageIndex)
        self.showPageArrows()
        self.pages[self.currPageIndex].enter()

    
    def showPageArrows(self):
        if self.currPageIndex == 0:
            self.prevArrow.hide()
            self.nextArrow.show()
        elif self.currPageIndex == len(self.pages) - 1:
            self.prevArrow.show()
            self.nextArrow.hide()
        else:
            self.prevArrow.show()
            self.nextArrow.show()

    
    def disableBookCloseButton(self):
        if self.bookCloseButton:
            self.bookCloseButton['command'] = None
        

    
    def enableBookCloseButton(self):
        if self.bookCloseButton:
            self.bookCloseButton['command'] = self._ShtikerBook__close
        


