# File: E (Python 2.2)

from PandaModules import *
from IntervalGlobal import *
from ElevatorConstants import *

def getLeftOpenInterval(distObj, leftDoor):
    leftOpenInterval = LerpPosInterval(leftDoor, ELEVATOR_OPEN_TIME, OPEN_POS_LEFT, startPos = CLOSED_POS_LEFT, blendType = 'easeOut', name = distObj.uniqueName('leftDoorOpen'))
    return leftOpenInterval


def getRightOpenInterval(distObj, rightDoor):
    rightOpenInterval = LerpPosInterval(rightDoor, ELEVATOR_OPEN_TIME, OPEN_POS_RIGHT, startPos = CLOSED_POS_RIGHT, blendType = 'easeOut', name = distObj.uniqueName('rightDoorOpen'))
    return rightOpenInterval


def getOpenInterval(distObj, leftDoor, rightDoor, sfx):
    return Parallel(SoundInterval(sfx), getLeftOpenInterval(distObj, leftDoor), getRightOpenInterval(distObj, rightDoor))


def getLeftCloseInterval(distObj, leftDoor):
    leftCloseInterval = LerpPosInterval(leftDoor, ELEVATOR_CLOSE_TIME, CLOSED_POS_LEFT, startPos = OPEN_POS_LEFT, blendType = 'easeOut', name = distObj.uniqueName('leftDoorClose'))
    return leftCloseInterval


def getRightCloseInterval(distObj, rightDoor):
    rightCloseInterval = LerpPosInterval(rightDoor, ELEVATOR_CLOSE_TIME, CLOSED_POS_RIGHT, startPos = OPEN_POS_RIGHT, blendType = 'easeOut', name = distObj.uniqueName('rightDoorClose'))
    return rightCloseInterval


def getCloseInterval(distObj, leftDoor, rightDoor, sfx):
    return Parallel(SoundInterval(sfx), getLeftCloseInterval(distObj, leftDoor), getRightCloseInterval(distObj, rightDoor))

