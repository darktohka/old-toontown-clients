# File: C (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject

class CDistributedSmoothNodeBase(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libdirect._inPiutgYl7d()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inPiutgbyyh:
            libdirect._inPiutgbyyh(self.this)
        

    
    def setRepository(repository, isAi, aiId):
        returnValue = libdirect._inPiutg9rX6(repository.this, isAi, aiId)
        return returnValue

    setRepository = staticmethod(setRepository)
    
    def setClockDelta(clockDelta):
        returnValue = libdirect._inPiutg1CY3(clockDelta)
        return returnValue

    setClockDelta = staticmethod(setClockDelta)
    
    def initialize(self, nodePath, dclass, doId):
        returnValue = libdirect._inPiutglODQ(self.this, nodePath.this, dclass.this, doId)
        return returnValue

    
    def sendEverything(self):
        returnValue = libdirect._inPiutgkeGE(self.this)
        return returnValue

    
    def broadcastPosHprFull(self):
        returnValue = libdirect._inPiutguy5e(self.this)
        return returnValue

    
    def broadcastPosHprXyh(self):
        returnValue = libdirect._inPiutgCz2k(self.this)
        return returnValue


