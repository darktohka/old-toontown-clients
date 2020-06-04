# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\FogOverlay.py
from pandac.PandaModules import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task import Task
from toontown.toonbase import ToontownGlobals
import math
from math import *

class FogOverlay:
    __module__ = __name__
    SomeCounter = 0

    def __init__(self, color=Point3(1.0, 1.0, 1.0)):
        self.color = color
        self.opacity = 1.0
        self.setup()

    def setup(self):
        self.baseNode = aspect2d.attachNewNode('targetGameTargets')
        self.overlayGN = GeomNode('Overlay Geometry')
        self.overlayNodePathGeom = self.baseNode.attachNewNode(self.overlayGN)
        self.overlayNodePathGeom.setDepthWrite(False)
        self.overlayNodePathGeom.setTransparency(TransparencyAttrib.MAlpha)
        shapeVertexs = []
        shapeVertexs.append((-2.0, 0.0, 1.0))
        shapeVertexs.append((-2.0, 0.0, -1.0))
        shapeVertexs.append((2.0, 0.0, 1.0))
        shapeVertexs.append((2.0, 0.0, -1.0))
        gFormat = GeomVertexFormat.getV3cp()
        overlayVertexData = GeomVertexData('holds my vertices', gFormat, Geom.UHDynamic)
        overlayVertexWriter = GeomVertexWriter(overlayVertexData, 'vertex')
        overlayColorWriter = GeomVertexWriter(overlayVertexData, 'color')
        for index in range(len(shapeVertexs)):
            overlayVertexWriter.addData3f(shapeVertexs[index][0], shapeVertexs[index][1], shapeVertexs[index][2])
            overlayColorWriter.addData4f(1.0, 1.0, 1.0, 1.0)

        overlayTris = GeomTristrips(Geom.UHStatic)
        for index in range(len(shapeVertexs)):
            overlayTris.addVertex(index)

        overlayTris.closePrimitive()
        overlayGeom = Geom(overlayVertexData)
        overlayGeom.addPrimitive(overlayTris)
        self.overlayGN.addGeom(overlayGeom)

    def setOpacity(self, opacity):
        self.opacity = opacity
        self.__applyColor()

    def setColor(self, color):
        self.color = color
        self.__applyColor()

    def __applyColor(self):
        self.overlayNodePathGeom.setColorScale(self.color[0], self.color[1], self.color[2], self.opacity)

    def delete(self):
        self.overlayGN.removeAllGeoms()
        self.baseNode.remove()