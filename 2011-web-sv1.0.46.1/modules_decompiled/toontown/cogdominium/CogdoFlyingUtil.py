# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\cogdominium\CogdoFlyingUtil.py
from otp.otpbase import OTPGlobals
from CogdoFlyingShadowPlacer import CogdoFlyingShadowPlacer

def loadMockup(fileName, dmodelsAlt='coffin'):
    try:
        model = loader.loadModel(fileName)
    except IOError:
        model = loader.loadModel('phase_4/models/props/%s' % dmodelsAlt)

    return model


def swapAvatarShadowPlacer(avatar, name):
    avatar.setActiveShadow(0)
    avatar.deleteDropShadow()
    avatar.initializeDropShadow()
    if avatar.shadowPlacer:
        avatar.shadowPlacer.delete()
        avatar.shadowPlacer = None
    shadowPlacer = CogdoFlyingShadowPlacer(base.shadowTrav, avatar.dropShadow, OTPGlobals.WallBitmask, OTPGlobals.FloorBitmask, name)
    avatar.shadowPlacer = shadowPlacer
    avatar.setActiveShadow(0)
    avatar.setActiveShadow(1)
    return