# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\otp\src\otpbase\OTPRender.py
from pandac.PandaModules import *
MainCameraBitmask = BitMask32.bit(0)
ReflectionCameraBitmask = BitMask32.bit(1)
ShadowCameraBitmask = BitMask32.bit(2)
SkyReflectionCameraBitmask = BitMask32.bit(3)
GlowCameraBitmask = BitMask32.bit(4)
EnviroCameraBitmask = BitMask32.bit(5)

def setCameraBitmask(default, node_path, camera_bitmask, tag=None, tag_function=None, context=None):
    if node_path:
        show = default
        if tag_function:
            show = tag_function(default, tag, context)
        if show:
            node_path.show(camera_bitmask)
        else:
            node_path.hide(camera_bitmask)


def renderReflection(default, node_path, tag=None, tag_function=None, context=None):
    setCameraBitmask(default, node_path, ReflectionCameraBitmask, tag, tag_function, context)


def renderShadow(default, node_path, tag=None, tag_function=None, context=None):
    setCameraBitmask(default, node_path, ShadowCameraBitmask, tag, tag_function, context)


def renderSkyReflection(default, node_path, tag=None, tag_function=None, context=None):
    setCameraBitmask(default, node_path, SkyReflectionCameraBitmask, tag, tag_function, context)


def renderGlow(default, node_path, tag=None, tag_function=None, context=None):
    setCameraBitmask(default, node_path, GlowCameraBitmask, tag, tag_function, context)


def setAdditiveEffect(node_path, tag=None, bin_name=None, lighting_on=False, reflect=False):
    if node_path:
        node_path.setTransparency(True)
        node_path.setDepthWrite(False)
        node_path.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
        if lighting_on == False:
            node_path.setLightOff()
        node_path.setAttrib(ColorWriteAttrib.make(ColorWriteAttrib.CRed | ColorWriteAttrib.CGreen | ColorWriteAttrib.CBlue))
        if reflect == False:
            renderReflection(False, node_path, tag, None)
        if bin_name:
            node_path.setBin(bin_name, 0)
    return