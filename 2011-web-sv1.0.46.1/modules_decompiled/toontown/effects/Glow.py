# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\effects\Glow.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from EffectController import EffectController
from PooledEffect import PooledEffect

class Glow(PooledEffect, EffectController):
    __module__ = __name__

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)

    def createTrack(self):
        model = loader.loadModel('phase_4/models/props/tt_m_efx_ext_particleCards')
        self.spark = model.find('**/tt_t_efx_ext_particleSparkle')
        self.effectModel = self.attachNewNode('effectModelNode')
        self.spark.reparentTo(self.effectModel)
        self.effectColor = Vec4(1, 1, 1, 1)
        self.effectModel.hide()
        self.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
        self.setBillboardPointWorld()
        self.setDepthWrite(0)
        self.setLightOff()
        self.setFogOff()
        self.effectModel.hide()
        self.effectModel.setColorScale(self.effectColor)
        pulseIval = Sequence(Wait(0.1), Func(self.effectModel.setColorScale, self.effectColor), Wait(0.1), Func(self.effectModel.setColorScale, Vec4(1, 1, 1, 0.7)))
        self.startEffect = Sequence(Func(self.effectModel.show), Func(pulseIval.loop))
        self.endEffect = Sequence(Func(pulseIval.finish), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(1.0), self.endEffect)

    def cleanUpEffect(self):
        self.effectModel.hide()
        EffectController.cleanUpEffect(self)
        if self.pool and self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)