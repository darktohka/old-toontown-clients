# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\shtiker\NewsPage.py
from direct.fsm import StateData
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectGui import DirectLabel
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.shtiker import ShtikerPage
from toontown.toonbase import TTLocalizer
UseDirectNewsFrame = config.GetBool('use-direct-news-frame', True)
HaveNewsFrame = True
if UseDirectNewsFrame:
    from toontown.shtiker import DirectNewsFrame
else:
    try:
        from toontown.shtiker import InGameNewsFrame
    except:
        HaveNewsFrame = False

class NewsPage(ShtikerPage.ShtikerPage):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('NewsPage')

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    def load(self):
        self.noNewsLabel = DirectLabel(parent=self, relief=None, text=TTLocalizer.NewsPageImportError, text_scale=0.12)
        if HaveNewsFrame:
            if UseDirectNewsFrame:
                import datetime
                start = datetime.datetime.now()
                self.newsFrame = DirectNewsFrame.DirectNewsFrame(parent=self)
                ending = datetime.datetime.now()
                self.notify.info('time to load news = %s' % str(ending - start))
            else:
                self.newsFrame = InGameNewsFrame.InGameNewsFrame(parent=self)
                self.newsFrame.activate()
        return

    def unload(self):
        if HaveNewsFrame:
            self.newsFrame.unload()
            del self.newsFrame

    def clearPage(self):
        pass

    def updatePage(self):
        pass

    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)
        if HaveNewsFrame:
            if self.book:
                self.book.prevArrow.hide()
                self.book.disableAllPageTabs()
            self.newsFrame.activate()
            base.setCellsAvailable(base.leftCells, 0)
            base.setCellsAvailable([base.rightCells[1]], 0)
            localAvatar.book.bookCloseButton.hide()
            localAvatar.setLastTimeReadNews(base.cr.toontownTimeManager.getCurServerDateTime())

    def exit(self):
        self.clearPage()
        if self.book:
            self.book.prevArrow.show()
            self.book.enableAllPageTabs()
        ShtikerPage.ShtikerPage.exit(self)
        if HaveNewsFrame:
            self.newsFrame.deactivate()
            base.setCellsAvailable(base.leftCells, 1)
            base.setCellsAvailable([base.rightCells[1]], 1)
            if localAvatar.book.shouldBookButtonBeHidden():
                localAvatar.book.bookCloseButton.hide()
            else:
                localAvatar.book.bookCloseButton.show()

    def doSnapshot(self):
        if HaveNewsFrame:
            return self.newsFrame.doSnapshot()
        else:
            return 'No News Frame'