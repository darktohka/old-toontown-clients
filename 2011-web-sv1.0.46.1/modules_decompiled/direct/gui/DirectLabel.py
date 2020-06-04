# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\gui\DirectLabel.py
__all__ = [
 'DirectLabel']
from pandac.PandaModules import *
import DirectGuiGlobals as DGG
from DirectFrame import *

class DirectLabel(DirectFrame):
    __module__ = __name__

    def __init__(self, parent=None, **kw):
        optiondefs = (
         (
          'pgFunc', PGItem, None), ('numStates', 1, None), ('state', self.inactiveInitState, None), ('activeState', 0, self.setActiveState))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.initialiseoptions(DirectLabel)
        return

    def setActiveState(self):
        self.guiItem.setState(self['activeState'])