# File: l (Python 2.2)

import types
import libdirect
import ConfigVariableSearchPath
import ConfigConfigureGetConfigConfigShowbase
import GraphicsWindow

def getParticlePath():
    returnValue = libdirect._inPL4GTsp9F()
    import ConfigVariableSearchPath
    returnObject = ConfigVariableSearchPath.ConfigVariableSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def throwNewFrame():
    returnValue = libdirect._inPL4GTzKzG()
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
    returnValue = libdirect._inPL4GTqt19(xsize, ysize)
    return returnValue


def runtestFullscreenSizes(win):
    returnValue = libdirect._inPL4GTuFP_(win.this)
    return returnValue


def queryFullscreenTestresult(xsize, ysize):
    returnValue = libdirect._inPL4GTvU68(xsize, ysize)
    return returnValue

HCCUT = 1
HCFREE = 2
HCG1 = 3
HCSMOOTH = 4
PCTHPR = 2
PCTNONE = 0
PCTT = 3
PCTXYZ = 1
