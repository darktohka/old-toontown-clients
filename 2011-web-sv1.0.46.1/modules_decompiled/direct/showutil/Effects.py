# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\direct\src\showutil\Effects.py
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
SX_BOUNCE = 0
SY_BOUNCE = 1
SZ_BOUNCE = 2
TX_BOUNCE = 3
TY_BOUNCE = 4
TZ_BOUNCE = 5
H_BOUNCE = 6
P_BOUNCE = 7
R_BOUNCE = 8

def createScaleXBounce(nodeObj, numBounces, startValues, totalTime, amplitude):
    return createBounce(nodeObj, numBounces, startValues, totalTime, amplitude, SX_BOUNCE)


def createScaleYBounce(nodeObj, numBounces, startValues, totalTime, amplitude):
    return createBounce(nodeObj, numBounces, startValues, totalTime, amplitude, SY_BOUNCE)


def createScaleZBounce(nodeObj, numBounces, startValue, totalTime, amplitude):
    return createBounce(nodeObj, numBounces, startValue, totalTime, amplitude, SZ_BOUNCE)


def createXBounce(nodeObj, numBounces, startValues, totalTime, amplitude):
    return createBounce(nodeObj, numBounces, startValues, totalTime, amplitude, TX_BOUNCE)


def createYBounce(nodeObj, numBounces, startValues, totalTime, amplitude):
    return createBounce(nodeObj, numBounces, startValues, totalTime, amplitude, TY_BOUNCE)


def createZBounce(nodeObj, numBounces, startValues, totalTime, amplitude):
    return createBounce(nodeObj, numBounces, startValues, totalTime, amplitude, TZ_BOUNCE)


def createHBounce(nodeObj, numBounces, startValues, totalTime, amplitude):
    return createBounce(nodeObj, numBounces, startValues, totalTime, amplitude, H_BOUNCE)


def createPBounce(nodeObj, numBounces, startValues, totalTime, amplitude):
    return createBounce(nodeObj, numBounces, startValues, totalTime, amplitude, P_BOUNCE)


def createRBounce(nodeObj, numBounces, startValues, totalTime, amplitude):
    return createBounce(nodeObj, numBounces, startValues, totalTime, amplitude, R_BOUNCE)


def createBounce(nodeObj, numBounces, startValues, totalTime, amplitude, bounceType=SZ_BOUNCE):
    if not nodeObj or numBounces < 1 or totalTime == 0:
        self.notify.warning('createBounceIvals called with invalid parameter')
        return
    result = Sequence()
    bounceTime = totalTime / float(numBounces)
    currTime = bounceTime
    currAmplitude = amplitude
    if bounceType == SX_BOUNCE or bounceType == TX_BOUNCE or bounceType == H_BOUNCE:
        index = 0
    elif bounceType == SY_BOUNCE or bounceType == TY_BOUNCE or bounceType == P_BOUNCE:
        index = 1
    elif bounceType == SZ_BOUNCE or bounceType == TZ_BOUNCE or bounceType == R_BOUNCE:
        index = 2
    currBounceVal = startValues[index]
    for bounceNum in range(numBounces * 2):
        if bounceNum % 2:
            currBounceVal = startValues[index]
            blend = 'easeIn'
        else:
            currBounceVal = startValues[index] + currAmplitude
            blend = 'easeOut'
        newVec3 = Vec3(startValues)
        newVec3.setCell(index, currBounceVal)
        print '### newVec3 = ', newVec3
        if bounceType == SX_BOUNCE or bounceType == SY_BOUNCE or bounceType == SZ_BOUNCE:
            result.append(LerpScaleInterval(nodeObj, currTime, newVec3, blendType=blend))
        elif bounceType == TX_BOUNCE or bounceType == TY_BOUNCE or bounceType == TZ_BOUNCE:
            result.append(LerpPosInterval(nodeObj, currTime, newVec3, blendType=blend))
        elif bounceType == H_BOUNCE or bounceType == P_BOUNCE or bounceType == R_BOUNCE:
            result.append(LerpHprInterval(nodeObj, currTime, newVec3, blendType=blend))
        currAmplitude *= 0.5
        currTime = bounceTime

    return result