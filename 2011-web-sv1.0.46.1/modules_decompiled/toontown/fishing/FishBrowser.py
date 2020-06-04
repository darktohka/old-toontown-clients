# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\fishing\FishBrowser.py
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer
import GenusPanel, FishGlobals

class FishBrowser(DirectScrolledList):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FishBrowser')

    def __init__(self, parent=aspect2d, **kw):
        self.parent = parent
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        optiondefs = (
         (
          'parent', self.parent, None), ('relief', None, None), ('incButton_image', (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), None), ('incButton_relief', None, None), ('incButton_scale', (1.3, 1.3, -1.3), None), ('incButton_pos', (0, 0, -0.525), None), ('incButton_image3_color', Vec4(0.8, 0.8, 0.8, 0.5), None), ('decButton_image', (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), None), ('decButton_relief', None, None), ('decButton_scale', (1.3, 1.3, 1.3), None), ('decButton_pos', (0, 0, 0.525), None), ('decButton_image3_color', Vec4(0.8, 0.8, 0.8, 0.5), None), ('numItemsVisible', 1, None), ('items', map(str, FishGlobals.getGenera()), None), ('scrollSpeed', 4, None), ('itemMakeFunction', GenusPanel.GenusPanel, None), ('itemMakeExtraArgs', None, None))
        gui.removeNode()
        self.defineoptions(kw, optiondefs)
        DirectScrolledList.__init__(self, parent)
        self.initialiseoptions(FishBrowser)
        return

    def destroy(self):
        DirectScrolledList.destroy(self)
        self.parent = None
        return

    def update(self):
        pass

    def show(self):
        if not self.parent.isHidden():
            self['items'][self.index].show()
            DirectScrolledList.show(self)

    def hide(self):
        self['items'][self.index].hide()
        DirectScrolledList.hide(self)