# File: E (Python 2.2)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from ElevatorConstants import *

def closeDoors(leftDoor, rightDoor, big = 0):
    if big == 0:
        closedPosLeft = CLOSED_POS_LEFT
        closedPosRight = CLOSED_POS_RIGHT
    else:
        closedPosLeft = BIG_CLOSED_POS_LEFT
        closedPosRight = BIG_CLOSED_POS_RIGHT
    leftDoor.setPos(closedPosLeft)
    rightDoor.setPos(closedPosRight)


def openDoors(leftDoor, rightDoor, big = 0):
    leftDoor.setPos(OPEN_POS_LEFT)
    rightDoor.setPos(OPEN_POS_RIGHT)


def getLeftOpenInterval(distObj, leftDoor, big):
    if big == 0:
        openTime = ELEVATOR_OPEN_TIME
        closedPos = CLOSED_POS_LEFT
    else:
        openTime = BIG_ELEVATOR_OPEN_TIME
        closedPos = BIG_CLOSED_POS_LEFT
    leftOpenInterval = LerpPosInterval(leftDoor, openTime, OPEN_POS_LEFT, startPos = closedPos, blendType = 'easeOut', name = distObj.uniqueName('leftDoorOpen'))
    return leftOpenInterval


def getRightOpenInterval(distObj, rightDoor, big):
    if big == 0:
        openTime = ELEVATOR_OPEN_TIME
        closedPos = CLOSED_POS_RIGHT
    else:
        openTime = BIG_ELEVATOR_OPEN_TIME
        closedPos = BIG_CLOSED_POS_RIGHT
    rightOpenInterval = LerpPosInterval(rightDoor, openTime, OPEN_POS_RIGHT, startPos = closedPos, blendType = 'easeOut', name = distObj.uniqueName('rightDoorOpen'))
    return rightOpenInterval


def getOpenInterval(distObj, leftDoor, rightDoor, openSfx, finalOpenSfx, big = 0):
    left = getLeftOpenInterval(distObj, leftDoor, big)
    right = getRightOpenInterval(distObj, rightDoor, big)
    openDuration = left.getDuration()
    if big:
        sfxVolume = 0.69999999999999996
    else:
        sfxVolume = 1.0
    if finalOpenSfx:
        sound = Sequence(SoundInterval(openSfx, duration = openDuration, volume = sfxVolume, node = leftDoor), SoundInterval(finalOpenSfx, volume = sfxVolume, node = leftDoor))
    else:
        sound = SoundInterval(openSfx, volume = sfxVolume, node = leftDoor)
    return Parallel(sound, left, right)


def getLeftCloseInterval(distObj, leftDoor, big):
    if big == 0:
        closeTime = ELEVATOR_CLOSE_TIME
        closedPos = CLOSED_POS_LEFT
    else:
        closeTime = BIG_ELEVATOR_CLOSE_TIME
        closedPos = BIG_CLOSED_POS_LEFT
    leftCloseInterval = LerpPosInterval(leftDoor, closeTime, closedPos, startPos = OPEN_POS_LEFT, blendType = 'easeOut', name = distObj.uniqueName('leftDoorClose'))
    return leftCloseInterval


def getRightCloseInterval(distObj, rightDoor, big):
    if big == 0:
        closeTime = ELEVATOR_CLOSE_TIME
        closedPos = CLOSED_POS_RIGHT
    else:
        closeTime = BIG_ELEVATOR_CLOSE_TIME
        closedPos = BIG_CLOSED_POS_RIGHT
    rightCloseInterval = LerpPosInterval(rightDoor, closeTime, closedPos, startPos = OPEN_POS_RIGHT, blendType = 'easeOut', name = distObj.uniqueName('rightDoorClose'))
    return rightCloseInterval


def getCloseInterval(distObj, leftDoor, rightDoor, closeSfx, finalCloseSfx, big = 0):
    left = getLeftCloseInterval(distObj, leftDoor, big)
    right = getRightCloseInterval(distObj, rightDoor, big)
    closeDuration = left.getDuration()
    if big:
        sfxVolume = 0.69999999999999996
    else:
        sfxVolume = 1.0
    if finalCloseSfx:
        sound = Sequence(SoundInterval(closeSfx, duration = closeDuration, volume = sfxVolume, node = leftDoor), SoundInterval(finalCloseSfx, volume = sfxVolume, node = leftDoor))
    else:
        sound = SoundInterval(closeSfx, volume = sfxVolume, node = leftDoor)
    return Parallel(sound, left, right)


def getRideElevatorInterval(big = 0):
    if big:
        ival = Sequence(Wait(0.5), LerpPosInterval(camera, 0.5, Point3(0, 30, 7.7999999999999998), startPos = Point3(0, 30, 8), blendType = 'easeOut'), LerpPosInterval(camera, 0.5, Point3(0, 30, 8), startPos = Point3(0, 30, 7.7999999999999998)), Wait(1.0), LerpPosInterval(camera, 0.5, Point3(0, 30, 8.1999999999999993), startPos = Point3(0, 30, 8), blendType = 'easeOut'), LerpPosInterval(camera, 1.0, Point3(0, 30, 8), startPos = Point3(0, 30, 8.1999999999999993)))
    else:
        ival = Sequence(Wait(0.5), LerpPosInterval(camera, 0.5, Point3(0, 14, 3.7999999999999998), startPos = Point3(0, 14, 4), blendType = 'easeOut'), LerpPosInterval(camera, 0.5, Point3(0, 14, 4), startPos = Point3(0, 14, 3.7999999999999998)), Wait(1.0), LerpPosInterval(camera, 0.5, Point3(0, 14, 4.2000000000000002), startPos = Point3(0, 14, 4), blendType = 'easeOut'), LerpPosInterval(camera, 1.0, Point3(0, 14, 4), startPos = Point3(0, 14, 4.2000000000000002)))
    return ival

