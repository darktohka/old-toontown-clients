# File: l (Python 2.2)

import types
import libpandaexpress
import TimeVal
import ConfigExpress
import Filename

def getTimeOfDay(tv):
    returnValue = libpandaexpress._inPJoxtEUNo(tv.this)
    return returnValue


def getConfigExpress():
    returnValue = libpandaexpress._inPJoxt5Q2z()
    import ConfigExpress
    returnObject = ConfigExpress.ConfigExpress(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def errorToText(err):
    returnValue = libpandaexpress._inPJoxtr1c1(err)
    return returnValue


def getWriteError():
    returnValue = libpandaexpress._inPJoxto_jp()
    return returnValue


def checkCrc(name):
    returnValue = libpandaexpress._inP2KOdZj2d(name.this)
    return returnValue


def checkAdler(name):
    returnValue = libpandaexpress._inP2KOdwHLZ(name.this)
    return returnValue

