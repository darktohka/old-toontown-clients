# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\parties\PartyEditorGridSquare.py
from pandac.PandaModules import Vec3, Vec4, Point3, TextNode, VBase4
from direct.gui.DirectGui import DirectFrame, DirectButton, DirectLabel, DirectScrolledList, DirectCheckButton
from direct.gui import DirectGuiGlobals
from direct.showbase.DirectObject import DirectObject
from direct.showbase import PythonUtil
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.parties import PartyGlobals
from toontown.parties.PartyInfo import PartyInfo
from toontown.parties import PartyUtils

class PartyEditorGridSquare(DirectObject):
    __module__ = __name__
    notify = directNotify.newCategory('PartyEditorGridSquare')

    def __init__(self, partyEditor, x, y):
        self.partyEditor = partyEditor
        self.x = x
        self.y = y
        self.gridElement = None
        return

    def getPos(self):
        return Point3(PartyGlobals.PartyEditorGridBounds[0][0] + self.x * PartyGlobals.PartyEditorGridSquareSize[0] + PartyGlobals.PartyEditorGridSquareSize[0] / 2.0, 0.0, PartyGlobals.PartyEditorGridBounds[1][1] + (PartyGlobals.PartyEditorGridSize[1] - 1 - self.y) * PartyGlobals.PartyEditorGridSquareSize[1] + PartyGlobals.PartyEditorGridSquareSize[1] / 2.0)

    def destroy(self):
        del self.gridElement