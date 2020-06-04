# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\toonbase\ToontownIntervals.py
from direct.interval.MetaInterval import Sequence
from direct.interval.FunctionInterval import Wait, Func
PULSE_GUI_DURATION = 0.2
PULSE_GUI_CHANGE = 0.333

def cleanup(name):
    taskMgr.remove(name)


def start(ival):
    cleanup(ival.getName())
    ival.start()
    return ival


def loop(ival):
    cleanup(ival.getName())
    ival.loop()
    return ival


def getPulseLargerIval(np, name, duration=PULSE_GUI_DURATION, scale=1):
    return getPulseIval(np, name, 1 + PULSE_GUI_CHANGE, duration=duration, scale=scale)


def getPulseSmallerIval(np, name, duration=PULSE_GUI_DURATION, scale=1):
    return getPulseIval(np, name, 1 - PULSE_GUI_CHANGE, duration=duration, scale=scale)


def getPulseIval(np, name, change, duration=PULSE_GUI_CHANGE, scale=1):
    return Sequence(np.scaleInterval(duration, scale * change, blendType='easeOut'), np.scaleInterval(duration, scale, blendType='easeIn'), name=name, autoFinish=1)


def getPresentGuiIval(np, name, waitDuration=0.5, moveDuration=1.0, parent=aspect2d, startPos=(0, 0, 0)):
    endPos = np.getPos()
    np.setPos(parent, startPos[0], startPos[1], startPos[2])
    return Sequence(Func(np.show), getPulseLargerIval(np, '', scale=np.getScale()), Wait(waitDuration), np.posInterval(moveDuration, endPos, blendType='easeInOut'), name=name, autoFinish=1)