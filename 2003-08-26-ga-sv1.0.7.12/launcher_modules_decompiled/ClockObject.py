# File: C (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class ClockObject(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    MNonRealTime = 1
    MNormal = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpandaexpress._inPJoxtwP2R()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPJoxt5bD_:
            libpandaexpress._inPJoxt5bD_(self.this)
        

    
    def getGlobalClock():
        returnValue = libpandaexpress._inPJoxtb_iD()
        returnObject = ClockObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalClock = staticmethod(getGlobalClock)
    
    def setMode(self, mode):
        returnValue = libpandaexpress._inPJoxtvf6_(self.this, mode)
        return returnValue

    
    def getMode(self):
        returnValue = libpandaexpress._inPJoxtC0lD(self.this)
        return returnValue

    
    def getFrameTime(self):
        returnValue = libpandaexpress._inPJoxtP13s(self.this)
        return returnValue

    
    def getRealTime(self):
        returnValue = libpandaexpress._inPJoxt84v7(self.this)
        return returnValue

    
    def getLongTime(self):
        returnValue = libpandaexpress._inPJoxt9RD3(self.this)
        return returnValue

    
    def reset(self):
        returnValue = libpandaexpress._inPJoxtWWd9(self.this)
        return returnValue

    
    def setRealTime(self, time):
        returnValue = libpandaexpress._inPJoxtu4ev(self.this, time)
        return returnValue

    
    def setFrameTime(self, time):
        returnValue = libpandaexpress._inPJoxt2d9O(self.this, time)
        return returnValue

    
    def setFrameCount(self, frameCount):
        returnValue = libpandaexpress._inPJoxtc2uN(self.this, frameCount)
        return returnValue

    
    def getFrameCount(self):
        returnValue = libpandaexpress._inPJoxtmz0Y(self.this)
        return returnValue

    
    def getFrameRate(self):
        returnValue = libpandaexpress._inPJoxtQG_U(self.this)
        return returnValue

    
    def getDt(self):
        returnValue = libpandaexpress._inPJoxttvG2(self.this)
        return returnValue

    
    def setDt(self, dt):
        returnValue = libpandaexpress._inPJoxtNQK2(self.this, dt)
        return returnValue

    
    def getMaxDt(self):
        returnValue = libpandaexpress._inPJoxta66A(self.this)
        return returnValue

    
    def setMaxDt(self, maxDt):
        returnValue = libpandaexpress._inPJoxt_bSs(self.this, maxDt)
        return returnValue

    
    def tick(self):
        returnValue = libpandaexpress._inPJoxtmDUl(self.this)
        return returnValue

    
    def syncFrameTime(self):
        returnValue = libpandaexpress._inPJoxtH_dx(self.this)
        return returnValue


