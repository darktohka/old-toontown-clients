# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\directtools\DirectGrid.py
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
from DirectUtil import *
from DirectGeometry import *

class DirectGrid(NodePath, DirectObject):
    __module__ = __name__

    def __init__(self, gridSize=100.0, gridSpacing=5.0, planeColor=(0.5, 0.5, 0.5, 0.5), parent=None):
        NodePath.__init__(self, 'DirectGrid')
        useDirectRenderStyle(self)
        self.gridBack = loader.loadModel('models/misc/gridBack')
        self.gridBack.reparentTo(self)
        self.gridBack.setColor(*planeColor)
        self.lines = self.attachNewNode('gridLines')
        self.minorLines = LineNodePath(self.lines)
        self.minorLines.lineNode.setName('minorLines')
        self.minorLines.setColor(VBase4(0.3, 0.55, 1, 1))
        self.minorLines.setThickness(1)
        self.majorLines = LineNodePath(self.lines)
        self.majorLines.lineNode.setName('majorLines')
        self.majorLines.setColor(VBase4(0.3, 0.55, 1, 1))
        self.majorLines.setThickness(5)
        self.centerLines = LineNodePath(self.lines)
        self.centerLines.lineNode.setName('centerLines')
        self.centerLines.setColor(VBase4(1, 0, 0, 0))
        self.centerLines.setThickness(3)
        self.snapMarker = loader.loadModel('models/misc/sphere')
        self.snapMarker.node().setName('gridSnapMarker')
        self.snapMarker.reparentTo(self)
        self.snapMarker.setColor(1, 0, 0, 1)
        self.snapMarker.setScale(0.3)
        self.snapPos = Point3(0)
        self.fXyzSnap = 1
        self.fHprSnap = 1
        self.gridSize = gridSize
        self.gridSpacing = gridSpacing
        self.snapAngle = 15.0
        self.enable(parent=parent)

    def enable(self, parent=None):
        if parent:
            self.reparentTo(parent)
        else:
            self.reparentTo(base.direct.group)
        self.updateGrid()
        self.fEnabled = 1

    def disable(self):
        self.detachNode()
        self.fEnabled = 0

    def toggleGrid(self, parent=None):
        if self.fEnabled:
            self.disable()
        else:
            self.enable(parent=parent)

    def isEnabled(self):
        return self.fEnabled

    def updateGrid(self):
        self.minorLines.reset()
        self.majorLines.reset()
        self.centerLines.reset()
        numLines = int(math.ceil(self.gridSize / self.gridSpacing))
        scaledSize = numLines * self.gridSpacing
        center = self.centerLines
        minor = self.minorLines
        major = self.majorLines
        for i in range(-numLines, numLines + 1):
            if i == 0:
                center.moveTo(i * self.gridSpacing, -scaledSize, 0)
                center.drawTo(i * self.gridSpacing, scaledSize, 0)
                center.moveTo(-scaledSize, i * self.gridSpacing, 0)
                center.drawTo(scaledSize, i * self.gridSpacing, 0)
            elif i % 5 == 0:
                major.moveTo(i * self.gridSpacing, -scaledSize, 0)
                major.drawTo(i * self.gridSpacing, scaledSize, 0)
                major.moveTo(-scaledSize, i * self.gridSpacing, 0)
                major.drawTo(scaledSize, i * self.gridSpacing, 0)
            else:
                minor.moveTo(i * self.gridSpacing, -scaledSize, 0)
                minor.drawTo(i * self.gridSpacing, scaledSize, 0)
                minor.moveTo(-scaledSize, i * self.gridSpacing, 0)
                minor.drawTo(scaledSize, i * self.gridSpacing, 0)

        center.create()
        minor.create()
        major.create()
        if self.gridBack:
            self.gridBack.setScale(scaledSize)

    def setXyzSnap(self, fSnap):
        self.fXyzSnap = fSnap

    def getXyzSnap(self):
        return self.fXyzSnap

    def setHprSnap(self, fSnap):
        self.fHprSnap = fSnap

    def getHprSnap(self):
        return self.fHprSnap

    def computeSnapPoint(self, point):
        self.snapPos.assign(point)
        if self.fXyzSnap:
            self.snapPos.set(ROUND_TO(self.snapPos[0], self.gridSpacing), ROUND_TO(self.snapPos[1], self.gridSpacing), ROUND_TO(self.snapPos[2], self.gridSpacing))
        self.snapMarker.setPos(self.snapPos)
        return self.snapPos

    def computeSnapAngle(self, angle):
        return ROUND_TO(angle, self.snapAngle)

    def setSnapAngle(self, angle):
        self.snapAngle = angle

    def getSnapAngle(self):
        return self.snapAngle

    def setGridSpacing(self, spacing):
        self.gridSpacing = spacing
        self.updateGrid()

    def getGridSpacing(self):
        return self.gridSpacing

    def setGridSize(self, size):
        self.gridSize = size
        self.updateGrid()

    def getGridSize(self):
        return self.gridSize