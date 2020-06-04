# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\RenderingEntity.py
from toontown.toonbase.ToontownGlobals import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.suit import GoonPathData
from otp.level import BasicEntities

class RenderingEntity(BasicEntities.NodePathEntity):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('PathMasterEntity')

    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        if hasattr(self, 'colorR'):
            self.setColorScale(self.colorR, self.colorG, self.colorB, self.colorA)
        if hasattr(self, 'blending'):
            self.setBlending(self.blending)
        if hasattr(self, 'fogOn'):
            self.setFogOn(self.fogOn)

    def destroy(self):
        BasicEntities.NodePathEntity.destroy(self)

    def setColorR(self, newColor):
        self.colorR = newColor
        self.setColorScale(self.colorR, self.colorG, self.colorB, self.colorA)

    def setColorG(self, newColor):
        self.colorG = newColor
        self.setColorScale(self.colorR, self.colorG, self.colorB, self.colorA)

    def setColorB(self, newColor):
        self.colorB = newColor
        self.setColorScale(self.colorR, self.colorG, self.colorB, self.colorA)

    def setColorA(self, newColor):
        self.colorA = newColor
        self.setColorScale(self.colorR, self.colorG, self.colorB, self.colorA)

    def setColorScale(self, R, G, B, A):
        BasicEntities.NodePathEntity.setColorScale(self, R, G, B, A)
        self.chooseBin()
        self.setBlending(self.blending)

    def chooseBin(self):
        if not hasattr(self, 'renderBin'):
            self.renderBin = 'default'
        self.setBin(self.renderBin, 0)

    def setBlending(self, blending):
        self.blending = blending
        if blending == 'Additive':
            self.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
            self.setDepthWrite(False)
        elif blending == 'Alpha':
            self.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MNone))
            self.setDepthWrite(True)
            self.setTransparency(1)
        else:
            self.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MNone))
            self.setDepthWrite(True)
            self.setTransparency(0)
        self.chooseBin()

    def setFogOn(self, fog):
        self.fogOn = fog
        if self.fogOn:
            myFog = Fog('Fog Rendering Fog of Rendering')
            myFog.setColor(1.0, 0.0, 0.0)
            myFog.setExpDensity(0.5)
            self.setFog(myFog)
        else:
            self.clearFog()