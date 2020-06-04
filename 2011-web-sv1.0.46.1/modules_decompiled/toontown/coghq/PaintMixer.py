# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\coghq\PaintMixer.py
import PlatformEntity

class PaintMixer(PlatformEntity.PlatformEntity):
    __module__ = __name__

    def start(self):
        PlatformEntity.PlatformEntity.start(self)
        model = self.platform.model
        shaft = model.find('**/PaintMixerBase1')
        shaft.setSz(self.shaftScale)
        shaft.node().setPreserveTransform(0)
        shaftChild = shaft.find('**/PaintMixerBase')
        shaftChild.node().setPreserveTransform(0)
        model.flattenMedium()