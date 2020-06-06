# File: l (Python 2.2)

import types
import libpandaexpress
import TimeVal
import ConfigExpress
import Filename

def getTimeOfDay(tv):
    returnValue = libpandaexpress._inPKoxtFUNo(tv.this)
    return returnValue


def getConfigExpress():
    returnValue = libpandaexpress._inPKoxt_Q2z()
    import ConfigExpress
    returnObject = ConfigExpress.ConfigExpress(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def encryptString(source, password):
    returnValue = libpandaexpress._inPKoxtiH_H(source, password)
    return returnValue


def decryptString(source, password):
    returnValue = libpandaexpress._inPKoxtJ1fC(source, password)
    return returnValue


def errorToText(err):
    returnValue = libpandaexpress._inPKoxts1c1(err)
    return returnValue


def getWriteError():
    returnValue = libpandaexpress._inPKoxtp_jp()
    return returnValue


def passwordHash(password, salt, iters, keylen):
    returnValue = libpandaexpress._inPKoxtG9V_(password, salt, iters, keylen)
    return returnValue


def checkCrc(name):
    returnValue = libpandaexpress._inP2KOdZj2d(name.this)
    return returnValue


def checkAdler(name):
    returnValue = libpandaexpress._inP2KOdwHLZ(name.this)
    return returnValue

HCCUT = 1
HCFREE = 2
HCG1 = 3
HCSMOOTH = 4
PCTHPR = 2
PCTNONE = 0
PCTT = 3
PCTXYZ = 1
