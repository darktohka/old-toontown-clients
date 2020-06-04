# File: l (Python 2.2)

import types
import libdirect
import DSearchPath
import GraphicsWindow
import ConfigConfigureGetConfigConfigShowbase

def getParticlePath():
    returnValue = libdirect._inPL4GTsp9F()
    import DSearchPath
    returnObject = DSearchPath.DSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def throwNewFrame():
    returnValue = libdirect._inPL4GTzKzG()
    return returnValue


def takeSnapshot(win, name):
    returnValue = libdirect._inPL4GTKCZr(win.this, name)
    return returnValue


def getConfigShowbase():
    returnValue = libdirect._inPL4GTQL_f()
    import ConfigConfigureGetConfigConfigShowbase
    returnObject = ConfigConfigureGetConfigConfigShowbase.ConfigConfigureGetConfigConfigShowbase(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def addFullscreenTestsize(xsize, ysize):
    returnValue = libdirect._inPL4GTrt19(xsize, ysize)
    return returnValue


def runtestFullscreenSizes(win):
    returnValue = libdirect._inPL4GTxFP_(win.this)
    return returnValue


def queryFullscreenTestresult(xsize, ysize):
    returnValue = libdirect._inPL4GTuU68(xsize, ysize)
    return returnValue

HCCUT = 1
HCFREE = 2
HCG1 = 3
HCSMOOTH = 4
PCTHPR = 2
PCTNONE = 0
PCTT = 3
PCTXYZ = 1
