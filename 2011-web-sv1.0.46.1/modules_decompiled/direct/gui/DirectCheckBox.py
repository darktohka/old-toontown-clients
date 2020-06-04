# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\gui\DirectCheckBox.py
from direct.gui.DirectGui import *
from pandac.PandaModules import *

class DirectCheckBox(DirectButton):
    __module__ = __name__

    def __init__(self, parent=None, **kw):
        optiondefs = (
         (
          'pgFunc', PGButton, None), ('numStates', 4, None), ('state', DGG.NORMAL, None), ('relief', DGG.RAISED, None), ('invertedFrames', (1, ), None), ('command', None, None), ('extraArgs', [], None), ('commandButtons', (DGG.LMB,), self.setCommandButtons), ('rolloverSound', DGG.getDefaultRolloverSound(), self.setRolloverSound), ('clickSound', DGG.getDefaultClickSound(), self.setClickSound), ('pressEffect', 1, DGG.INITOPT), ('uncheckedImage', None, None), ('checkedImage', None, None), ('isChecked', False, None))
        self.defineoptions(kw, optiondefs)
        DirectButton.__init__(self, parent)
        self.initialiseoptions(DirectCheckBox)
        return

    def commandFunc(self, event):
        self['isChecked'] = not self['isChecked']
        if self['isChecked']:
            self['image'] = self['checkedImage']
        else:
            self['image'] = self['uncheckedImage']
        self.setImage()
        if self['command']:
            apply(self['command'], [self['isChecked']] + self['extraArgs'])