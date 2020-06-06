# File: O (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Ostream

class OSocketStream(Ostream.Ostream, FFIExternalObject.FFIExternalObject):
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
        if libpandaexpress and libpandaexpress._inP2KOdYde7:
            libpandaexpress._inP2KOdYde7(self.this)
        

    
    def sendDatagram(self, dg):
        returnValue = libpandaexpress._inP2KOdpllt(self.this, dg.this)
        return returnValue

    
    def isClosed(self):
        returnValue = libpandaexpress._inP2KOd6STp(self.this)
        return returnValue

    
    def close(self):
        returnValue = libpandaexpress._inP2KOdR4ab(self.this)
        return returnValue

    
    def setCollectTcp(self, collectTcp):
        returnValue = libpandaexpress._inP2KOdPxk2(self.this, collectTcp)
        return returnValue

    
    def getCollectTcp(self):
        returnValue = libpandaexpress._inP2KOdtNkN(self.this)
        return returnValue

    
    def setCollectTcpInterval(self, interval):
        returnValue = libpandaexpress._inP2KOdfDcr(self.this, interval)
        return returnValue

    
    def getCollectTcpInterval(self):
        returnValue = libpandaexpress._inP2KOdrjiI(self.this)
        return returnValue

    
    def considerFlush(self):
        returnValue = libpandaexpress._inP2KOd1Wy2(self.this)
        return returnValue

    
    def flush(self):
        returnValue = libpandaexpress._inP2KOdeCPl(self.this)
        return returnValue

    
    def upcastToOstream(self):
        returnValue = libpandaexpress._inP2KOdQTlu(self.this)
        import Ostream
        returnObject = Ostream.Ostream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def put(self, c):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToOstream()
        returnValue = libpandaexpress._inPKoxtiovs(upcastSelf.this, c)
        return returnValue


