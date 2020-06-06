# File: S (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Iostream

class SocketStream(Iostream.Iostream, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdBW2i:
            libpandaexpress._inP2KOdBW2i(self.this)
        

    
    def receiveDatagram(self, dg):
        returnValue = libpandaexpress._inP2KOdD7eO(self.this, dg.this)
        return returnValue

    
    def sendDatagram(self, dg):
        returnValue = libpandaexpress._inP2KOdKdSV(self.this, dg.this)
        return returnValue

    
    def isClosed(self):
        returnValue = libpandaexpress._inP2KOdC8Lh(self.this)
        return returnValue

    
    def close(self):
        returnValue = libpandaexpress._inP2KOd_VvS(self.this)
        return returnValue

    
    def setCollectTcp(self, collectTcp):
        returnValue = libpandaexpress._inP2KOdQsjT(self.this, collectTcp)
        return returnValue

    
    def getCollectTcp(self):
        returnValue = libpandaexpress._inP2KOdGQRW(self.this)
        return returnValue

    
    def setCollectTcpInterval(self, interval):
        returnValue = libpandaexpress._inP2KOdz1KB(self.this, interval)
        return returnValue

    
    def getCollectTcpInterval(self):
        returnValue = libpandaexpress._inP2KOdWrF2(self.this)
        return returnValue

    
    def considerFlush(self):
        returnValue = libpandaexpress._inP2KOdp5ln(self.this)
        return returnValue

    
    def flush(self):
        returnValue = libpandaexpress._inP2KOdPzDV(self.this)
        return returnValue

    
    def upcastToIostream(self):
        returnValue = libpandaexpress._inP2KOd8JpJ(self.this)
        import Iostream
        returnObject = Iostream.Iostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToOstream(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToIostream()
        returnValue = libpandaexpress._inPKoxt7W6h(upcastSelf.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def get(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToIostream()
        returnValue = libpandaexpress._inPKoxt4uln(upcastSelf.this)
        return returnValue

    
    def put(self, c):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToIostream()
        upcastSelf = upcastSelf.upcastToOstream()
        returnValue = libpandaexpress._inPKoxtiovs(upcastSelf.this, c)
        return returnValue


