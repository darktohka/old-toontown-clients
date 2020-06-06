# File: I (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Istream

class ISocketStream(Istream.Istream, FFIExternalObject.FFIExternalObject):
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
        if libpandaexpress and libpandaexpress._inP2KOdyeEe:
            libpandaexpress._inP2KOdyeEe(self.this)
        

    
    def receiveDatagram(self, dg):
        returnValue = libpandaexpress._inP2KOdabxT(self.this, dg.this)
        return returnValue

    
    def isClosed(self):
        returnValue = libpandaexpress._inP2KOdQnLp(self.this)
        return returnValue

    
    def close(self):
        returnValue = libpandaexpress._inP2KOdrVVb(self.this)
        return returnValue

    
    def upcastToIstream(self):
        returnValue = libpandaexpress._inP2KOd6pzq(self.this)
        import Istream
        returnObject = Istream.Istream(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def get(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToIstream()
        returnValue = libpandaexpress._inPKoxt4uln(upcastSelf.this)
        return returnValue


