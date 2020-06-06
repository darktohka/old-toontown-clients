# File: R (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class RecorderController(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPc5FLgOQz()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPc5FLnwuH()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def beginRecord(self, filename):
        returnValue = libpanda._inPc5FLEoI_(self.this, filename.this)
        return returnValue

    
    def beginPlayback(self, filename):
        returnValue = libpanda._inPc5FLD04q(self.this, filename.this)
        return returnValue

    
    def close(self):
        returnValue = libpanda._inPc5FL3TyG(self.this)
        return returnValue

    
    def getStartTime(self):
        returnValue = libpanda._inPc5FL7lBc(self.this)
        return returnValue

    
    def setRandomSeed(self, randomSeed):
        returnValue = libpanda._inPc5FLEIcS(self.this, randomSeed)
        return returnValue

    
    def getRandomSeed(self):
        returnValue = libpanda._inPc5FLzhjD(self.this)
        return returnValue

    
    def isRecording(self):
        returnValue = libpanda._inPc5FL3xMb(self.this)
        return returnValue

    
    def isPlaying(self):
        returnValue = libpanda._inPc5FLBF0E(self.this)
        return returnValue

    
    def isOpen(self):
        returnValue = libpanda._inPc5FL7Ejw(self.this)
        return returnValue

    
    def getFilename(self):
        returnValue = libpanda._inPc5FLE6J_(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isError(self):
        returnValue = libpanda._inPc5FLm_or(self.this)
        return returnValue

    
    def getClockOffset(self):
        returnValue = libpanda._inPc5FLN6bw(self.this)
        return returnValue

    
    def getFrameOffset(self):
        returnValue = libpanda._inPc5FLyEgj(self.this)
        return returnValue

    
    def addRecorder(self, name, recorder):
        returnValue = libpanda._inPc5FLAnOD(self.this, name, recorder.this)
        return returnValue

    
    def hasRecorder(self, name):
        returnValue = libpanda._inPc5FLSl_W(self.this, name)
        return returnValue

    
    def getRecorder(self, name):
        returnValue = libpanda._inPc5FLNjK2(self.this, name)
        import RecorderBase
        returnObject = RecorderBase.RecorderBase(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def removeRecorder(self, name):
        returnValue = libpanda._inPc5FLcpvX(self.this, name)
        return returnValue

    
    def setFrameTie(self, frameTie):
        returnValue = libpanda._inPc5FLsgOd(self.this, frameTie)
        return returnValue

    
    def getFrameTie(self):
        returnValue = libpanda._inPc5FLzYut(self.this)
        return returnValue

    
    def recordFrame(self):
        returnValue = libpanda._inPc5FLDD1N(self.this)
        return returnValue

    
    def playFrame(self):
        returnValue = libpanda._inPc5FLcjvm(self.this)
        return returnValue


