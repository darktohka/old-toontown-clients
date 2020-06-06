# File: C (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject

class CConnectionRepository(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libdirect._inPiutgJJvB()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inPiutgHgqv:
            libdirect._inPiutgHgqv(self.this)
        

    
    def getOverflowEventName():
        returnValue = libdirect._inPiutg1_hh()
        return returnValue

    getOverflowEventName = staticmethod(getOverflowEventName)
    
    def getDcFile(self):
        returnValue = libdirect._inPiutgWMFU(self.this)
        import DCFile
        returnObject = DCFile.DCFile(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setClientDatagram(self, clientDatagram):
        returnValue = libdirect._inPiutgglKQ(self.this, clientDatagram)
        return returnValue

    
    def getClientDatagram(self):
        returnValue = libdirect._inPiutg9Vry(self.this)
        return returnValue

    
    def setPythonRepository(self, pythonRepository):
        returnValue = libdirect._inPiutgfmXG(self.this, pythonRepository)
        return returnValue

    
    def setConnectionHttp(self, channel):
        returnValue = libdirect._inPiutgqdPr(self.this, channel.this)
        return returnValue

    
    def checkDatagram(self):
        returnValue = libdirect._inPiutgg_F4(self.this)
        return returnValue

    
    def getDatagram(self, dg):
        returnValue = libdirect._inPiutg3q1u(self.this, dg.this)
        return returnValue

    
    def getDatagramIterator(self, di):
        returnValue = libdirect._inPiutgfoW8(self.this, di.this)
        return returnValue

    
    def getMsgChannel(self):
        returnValue = libdirect._inPiutgOsSR(self.this)
        return returnValue

    
    def getMsgSender(self):
        returnValue = libdirect._inPiutg3Atc(self.this)
        return returnValue

    
    def getSecCode(self):
        returnValue = libdirect._inPiutg24As(self.this)
        return returnValue

    
    def getMsgType(self):
        returnValue = libdirect._inPiutglfYY(self.this)
        return returnValue

    
    def isConnected(self):
        returnValue = libdirect._inPiutgd16m(self.this)
        return returnValue

    
    def sendDatagram(self, dg):
        returnValue = libdirect._inPiutg1hI9(self.this, dg.this)
        return returnValue

    
    def considerFlush(self):
        returnValue = libdirect._inPiutgz8dn(self.this)
        return returnValue

    
    def flush(self):
        returnValue = libdirect._inPiutgiJJd(self.this)
        return returnValue

    
    def disconnect(self):
        returnValue = libdirect._inPiutgggLs(self.this)
        return returnValue

    
    def setSimulatedDisconnect(self, simulatedDisconnect):
        returnValue = libdirect._inPiutgTlnx(self.this, simulatedDisconnect)
        return returnValue

    
    def getSimulatedDisconnect(self):
        returnValue = libdirect._inPiutgtFqe(self.this)
        return returnValue


