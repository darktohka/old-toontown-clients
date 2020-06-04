# File: S (Python 2.2)

import ShtikerBook
import StateData
from DirectGui import *

class ShtikerPage(DirectFrame, StateData.StateData):
    
    def __init__(self):
        DirectFrame.__init__(self, relief = None, sortOrder = BACKGROUND_SORT_INDEX)
        self.initialiseoptions(ShtikerPage)
        StateData.StateData.__init__(self, 'shtiker-page-done')
        self.book = None
        self.hide()

    
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


