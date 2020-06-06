# File: l (Python 2.2)

import types
import libpandaexpress
import ConfigExpress
import TimeVal
import Filename
import HashVal

def getConfigExpress():
    returnValue = libpandaexpress._inPJoxt5Q2z()
    import ConfigExpress
    returnObject = ConfigExpress.ConfigExpress(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def getTimeOfDay(tv):
    returnValue = libpandaexpress._inPJoxtEUNo(tv.this)
    return returnValue


def errorToText(err):
    returnValue = libpandaexpress._inPJoxtr1c1(err)
    return returnValue


def getWriteError():
    returnValue = libpandaexpress._inPJoxto_jp()
    return returnValue


def md5AFile(fname, ret):
    returnValue = libpandaexpress._inPJoxtG2va(fname.this, ret.this)
    return returnValue


def checkCrc(name):
    returnValue = libpandaexpress._inP2KOdZj2d(name.this)
    return returnValue


def checkAdler(name):
    returnValue = libpandaexpress._inP2KOdwHLZ(name.this)
    return returnValue

