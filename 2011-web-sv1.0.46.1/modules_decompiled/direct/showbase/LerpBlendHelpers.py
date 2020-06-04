# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showbase\LerpBlendHelpers.py
__all__ = [
 'getBlend']
from pandac.PandaModules import *
easeIn = EaseInBlendType()
easeOut = EaseOutBlendType()
easeInOut = EaseInOutBlendType()
noBlend = NoBlendType()

def getBlend(blendType):
    if blendType == 'easeIn':
        return easeIn
    elif blendType == 'easeOut':
        return easeOut
    elif blendType == 'easeInOut':
        return easeInOut
    elif blendType == 'noBlend':
        return noBlend
    else:
        raise Exception('Error: LerpInterval.__getBlend: Unknown blend type')