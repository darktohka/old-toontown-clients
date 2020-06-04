# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\shtiker\ShtikerPage.py
import ShtikerBook
from direct.fsm import StateData
from direct.gui.DirectGui import *
from pandac.PandaModules import *

class ShtikerPage(DirectFrame, StateData.StateData):
    __module__ = __name__

    def __init__(self):
        DirectFrame.__init__(self, relief=None, sortOrder=DGG.BACKGROUND_SORT_INDEX)
        self.initialiseoptions(ShtikerPage)
        StateData.StateData.__init__(self, 'shtiker-page-done')
        self.book = None
        self.hide()
        return

    def load(self):
        pass

    def unload(self):
        self.ignoreAll()
        del self.book

    def enter(self):
        self.show()

    def exit(self):
        self.hide()

    def setBook(self, book):
        self.book = book

    def setPageName(self, pageName):
        self.pageName = pageName

    def makePageWhite(self, item):
        white = Vec4(1, 1, 1, 1)
        self.book['image_color'] = white
        self.book.nextArrow['image_color'] = white
        self.book.prevArrow['image_color'] = white

    def makePageRed(self, item):
        red = Vec4(1, 0.5, 0.5, 1)
        self.book['image_color'] = red
        self.book.nextArrow['image_color'] = red
        self.book.prevArrow['image_color'] = red