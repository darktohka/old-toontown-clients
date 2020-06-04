# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\effects\RayBurst.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from EffectController import EffectController

class RayBurst(NodePath, EffectController):
    __module__ = __name__

    def __init__(self):
        NodePath.__init__(self, 'RayBurst')
        EffectController.__init__(self)
        self.fadeTime = 0.25
        self.effectScale = 1.0
        self.effectColor = Vec4(1, 1, 1, 1)
        model = loader.loadModel('phase_4/models/props/tt_m_efx_ext_fireworkCards')
        self.effectModel = model.find('**/tt_t_efx_ext_fireworkRays')
        self.effectModel.setBillboardPointWorld()
        self.effectModel.reparentTo(self)
        self.effectModel.setColorScale(0, 0, 0, 0)
        self.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
        self.setBillboardPointWorld()
        self.setDepthWrite(0)
        self.setLightOff()
        self.setFogOff()

    def createTrack(self):
        self.effectModel.setColorScale(1, 1, 1, 0)
        fadeBlast = self.effectModel.colorScaleInterval(self.fadeTime, Vec4(1, 1, 1, 0), startColorScale=Vec4(self.effectColor), blendType='easeIn')
        scaleBlast = self.effectModel.scaleInterval(self.fadeTime, 700 * self.effectScale, startScale=100 * self.effectScale, blendType='easeOut')
        self.track = Sequence(Parallel(fadeBlast, scaleBlast), Func(self.cleanUpEffect))

    def setEffectColor(self, color):
        self.effectColor = color

    def setEffectScale(self, scale):
        self.effectScale = scale