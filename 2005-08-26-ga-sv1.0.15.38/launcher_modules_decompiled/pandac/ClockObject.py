# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class ClockObject(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    MNonRealTime = 1
    MForced = 2
    MDegrade = 3
    MNormal = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaexpress._inPKoxtwP2R()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxt4bD_:
            libpandaexpress._inPKoxt4bD_(self.this)
        

    
    def getGlobalClock():
        returnValue = libpandaexpress._inPKoxtb_iD()
        returnObject = ClockObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalClock = staticmethod(getGlobalClock)
    
    def setMode(self, mode):
        returnValue = libpandaexpress._inPKoxtsf6_(self.this, mode)
        return returnValue

    
    def getMode(self):
        returnValue = libpandaexpress._inPKoxtC0lD(self.this)
        return returnValue

    
    def getFrameTime(self):
        returnValue = libpandaexpress._inPKoxtQ13s(self.this)
        return returnValue

    
    def getRealTime(self):
        returnValue = libpandaexpress._inPKoxt94v7(self.this)
        return returnValue

    
    def getLongTime(self):
        returnValue = libpandaexpress._inPKoxt8RD3(self.this)
        return returnValue

    
    def reset(self):
        returnValue = libpandaexpress._inPKoxtVWd9(self.this)
        return returnValue

    
    def setRealTime(self, time):
        returnValue = libpandaexpress._inPKoxtx4ev(self.this, time)
        return returnValue

    
    def setFrameTime(self, time):
        returnValue = libpandaexpress._inPKoxt2d9O(self.this, time)
        return returnValue

    
    def setFrameCount(self, frameCount):
        returnValue = libpandaexpress._inPKoxtc2uN(self.this, frameCount)
        return returnValue

    
    def getFrameCount(self):
        returnValue = libpandaexpress._inPKoxtmz0Y(self.this)
        return returnValue

    
    def getNetFrameRate(self):
        returnValue = libpandaexpress._inPKoxtiXAn(self.this)
        return returnValue

    
    def getDt(self):
        returnValue = libpandaexpress._inPKoxtsvG2(self.this)
        return returnValue

    
    def setDt(self, dt):
        returnValue = libpandaexpress._inPKoxtMQK2(self.this, dt)
        return returnValue

    
    def getMaxDt(self):
        returnValue = libpandaexpress._inPKoxta66A(self.this)
        return returnValue

    
    def setMaxDt(self, maxDt):
        returnValue = libpandaexpress._inPKoxt_bSs(self.this, maxDt)
        return returnValue

    
    def getDegradeFactor(self):
        returnValue = libpandaexpress._inPKoxtYmhR(self.this)
        return returnValue

    
    def setDegradeFactor(self, degradeFactor):
        returnValue = libpandaexpress._inPKoxtTHAP(self.this, degradeFactor)
        return returnValue

    
    def setAverageFrameRateInterval(self, time):
        returnValue = libpandaexpress._inPKoxth4_P(self.this, time)
        return returnValue

    
    def getAverageFrameRateInterval(self):
        returnValue = libpandaexpress._inPKoxt1N1j(self.this)
        return returnValue

    
    def getAverageFrameRate(self):
        returnValue = libpandaexpress._inPKoxtBu1t(self.this)
        return returnValue

    
    def tick(self):
        returnValue = libpandaexpress._inPKoxtnDUl(self.this)
        return returnValue

    
    def syncFrameTime(self):
        returnValue = libpandaexpress._inPKoxtA_dx(self.this)
        return returnValue


