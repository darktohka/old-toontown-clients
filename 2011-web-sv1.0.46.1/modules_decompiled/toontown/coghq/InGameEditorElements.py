# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\InGameEditorElements.py
from direct.showbase import DirectObject

class InGameEditorElement(DirectObject.DirectObject):
    __module__ = __name__
    elementId = 0

    def __init__(self, children=[]):
        self.elementId = InGameEditorElement.elementId
        InGameEditorElement.elementId += 1
        self.setChildren(children)
        self.feName = self.getTypeName()

    def getName(self):
        return self.feName

    def setNewName(self, newName):
        self.feName = newName

    def getTypeName(self):
        return 'Level Element'

    def id(self):
        return self.elementId

    def getChildren(self):
        return self.children

    def setChildren(self, children):
        self.children = list(children)

    def addChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.remove(child)

    def getNumChildren(self):
        return len(self.children)