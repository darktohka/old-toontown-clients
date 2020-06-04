# File: O (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Ostream

class OSocketStream(Ostream.Ostream, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdfde7:
            libpandaexpress._inP2KOdfde7(self.this)
        

    
    def sendDatagram(self, dg):
        returnValue = libpandaexpress._inP2KOdollt(self.this, dg.this)
        return returnValue

    
    def isClosed(self):
        returnValue = libpandaexpress._inP2KOd5STp(self.this)
        return returnValue

    
    def close(self):
        returnValue = libpandaexpress._inP2KOdR4ab(self.this)
        return returnValue

    
    def setCollectTcp(self, collectTcp):
        returnValue = libpandaexpress._inP2KOdMxk2(self.this, collectTcp)
        return returnValue

    
    def getCollectTcp(self):
        returnValue = libpandaexpress._inP2KOdtNkN(self.this)
        return returnValue

    
    def setCollectTcpInterval(self, interval):
        returnValue = libpandaexpress._inP2KOdYDcr(self.this, interval)
        return returnValue

    
    def getCollectTcpInterval(self):
        returnValue = libpandaexpress._inP2KOdrjiI(self.this)
        return returnValue

    
    def considerFlush(self):
        returnValue = libpandaexpress._inP2KOdyWy2(self.this)
        return returnValue

    
    def flush(self):
        returnValue = libpandaexpress._inP2KOdfCPl(self.this)
        return returnValue


